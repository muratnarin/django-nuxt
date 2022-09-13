from rest_framework.filters import BaseFilterBackend
#
# from project.utils import get_model_field_names
#
#
# class ProviderPermissionFilter(BaseFilterBackend):
#
#     def filter_queryset(self, request, queryset, view=None):
#         user = request.user
#         user_queryset = queryset.none()
#         if queryset.model.__name__ == 'User':
#             user_queryset = queryset.filter(id=user.id)
#
#         if queryset.model.__name__ == 'Employee':
#             user_queryset = queryset.filter(user__id=user.id)
#
#         if user.is_superuser:
#             return queryset
#         elif user.provider_id is None:
#             queryset = queryset.none()
#
#         model_field_names = get_model_field_names(queryset.model)
#
#         if 'provider' in model_field_names:
#             queryset = queryset.filter(provider_id=user.provider_id)
#
#         return queryset | user_queryset
#
#
class ParameterFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view=None):
        if view.action != 'list':
            return queryset
        parameter_name_filters = request.data.get('parameter_name_filters')

        if parameter_name_filters is None:
            return queryset
        else:
            return queryset.filter(parameter_group__name__in=parameter_name_filters)
