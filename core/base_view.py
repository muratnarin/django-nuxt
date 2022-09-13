from django.conf import settings
from django.core.paginator import InvalidPage
from django.shortcuts import get_object_or_404
from django.urls import path
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, filters
from rest_framework.exceptions import APIException, NotFound
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

# from project.filters import ContractorPermissionFilter
from core.utils import in_model_fields


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = 'itemsPerPage'

    def get_paginated_response(self, data):
        return Response({
            'total': self.page.paginator.count,
            'result': data
        })

    def paginate_queryset(self, queryset, request, view=None):
        page_size = request.data.get(self.page_size_query_param, self.page_size)
        if not page_size:
            return None

        page_size = settings.MAX_ROWS_PER_PAGE if page_size == '-1' else page_size

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = request.data.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages

        try:
            self.page = paginator.page(page_number)
        except InvalidPage as exc:
            msg = self.invalid_page_message.format(
                page_number=page_number, message=str(exc)
            )
            raise NotFound(msg)

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)


class CustomOrderingFilter(OrderingFilter):
    def get_ordering(self, request, queryset, view):
        params = request.data.get(self.ordering_param)
        if params:
            fields = [param.strip() for param in params.split(',')]
            ordering = self.remove_invalid_fields(queryset, fields, view, request)
            if ordering:
                return ordering

        return self.get_default_ordering(view)


class CustomSearchFilter(filters.SearchFilter):
    def get_search_terms(self, request):
        params = request.data.get(self.search_param, '')
        if params is None:
            params = ''
        params = params.replace('\x00', '')  # strip null characters
        params = params.replace(',', ' ')
        return params.split()


class CustomDjangoFilterBackend(DjangoFilterBackend):
    def get_filterset_kwargs(self, request, queryset, view):
        return {
            'data': request.data,
            'queryset': queryset,
            'request': request,
        }


class BaseViewSet(ModelViewSet):
    pagination_class = CustomPagination
    # default_filters = [CustomSearchFilter, CustomDjangoFilterBackend, ContractorPermissionFilter, CustomOrderingFilter]
    default_filters = [CustomSearchFilter, CustomDjangoFilterBackend, CustomOrderingFilter]

    def get_queryset(self):
        queryset = super(BaseViewSet, self).get_queryset()
        if in_model_fields(queryset.model, 'created_at'):
            queryset = queryset.order_by('-created_at')
        return queryset

    @classmethod
    def use_for(cls, method):
        return cls.as_view({'post': method})

    def get_serializer_class(self):
        read_serializer_class = getattr(self, 'read_serializer_class', None)
        if read_serializer_class and self.action in ['list', 'retrieve']:
            return read_serializer_class
        else:
            return self.serializer_class

    def get_object(self):
        queryset = self.get_queryset()
        data = self.request.data
        _id = data.get("id")
        _slug = data.get("slug")
        if _id is None:
            if _slug is None:
                raise APIException(detail="id or slug is required")
            else:
                obj = get_object_or_404(queryset, slug=_slug)
        else:
            obj = get_object_or_404(queryset, pk=_id)
        self.check_object_permissions(self.request, obj)
        return obj

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends + self.default_filters):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def create(self, request, *args, **kwargs):
        if request.user and request.user.contractor_id:
            # request.data['contractor'] = request.user.contractor_id
            if request.user:
                request.data['operation_user'] = request.user.id
        return super(BaseViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.user and request.user.contractor_id:
            # request.data['contractor'] = request.user.contractor_id
            if request.user:
                request.data['operation_user'] = request.user.id
        return super(BaseViewSet, self).update(request, *args, **kwargs)

    def bulk_update(self, request, *args, **kwargs):
        data = request.data
        ids = []
        queryset = self.get_queryset()
        for datum in data:
            _id = datum.get('id')
            if _id is not None:
                ids.append(_id)
                obj = get_object_or_404(queryset, pk=_id)
                serializer = self.get_serializer(obj, data=datum)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
        instances = queryset.filter(id__in=ids)
        serializer = self.get_serializer(instances, many=True)
        return Response(serializer.data)


def create_view_paths(path_name, view):
    return [
        path('get{0}s/'.format(path_name), view.use_for('list')),
        path('get{0}byid/'.format(path_name), view.use_for('retrieve')),
        path('create{0}/'.format(path_name), view.use_for('create')),
        path('update{0}/'.format(path_name), view.use_for('update')),
        path('delete{0}/'.format(path_name), view.use_for('destroy')),
        path('bulkupdate{0}/'.format(path_name), view.use_for('bulk_update'))
    ]
