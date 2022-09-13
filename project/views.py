from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from core.base_view import BaseViewSet
from project.filters import SchoolPriceRangeFilter
from project.serializers import *
from rest_framework.decorators import api_view, throttle_classes, permission_classes
from rest_framework.throttling import ScopedRateThrottle
from user.throttles import LoginThrottle, PortalThrottle, SendEmailThrottle
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from project import hubspot
from django.db.models import Avg, Max, Min, Sum
from rest_framework.exceptions import APIException


def index(request, *args, **kwargs):
    return render(request, 'index.html')


class BannerViewSet(BaseViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    # filter_backends = [ContractorPermissionFilter]
    search_fields = ["order"]
    filterset_fields = ['id']
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'portal'


class BlogViewSet(BaseViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # filter_backends = [ContractorPermissionFilter]
    search_fields = ["title_tr", "title_en", "description_tr", "description_en"]
    filterset_fields = ['id']
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'portal'
    ordering = ('-date')


class AnnouncementViewSet(BaseViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    # filter_backends = [ContractorPermissionFilter]
    search_fields = ["title_tr", "title_en", "description_tr", "description_en"]
    filterset_fields = ['id']
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'portal'
    ordering = ('-date')


class ExchangeProgramViewSet(BaseViewSet):
    queryset = ExchangeProgram.objects.all()
    serializer_class = ExchangeProgramSerializer
    # filter_backends = [ContractorPermissionFilter]
    search_fields = ["title_tr", "title_en", "description_tr", "description_en"]
    filterset_fields = ['id']
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'portal'


class ContactViewSet(BaseViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # filter_backends = [ContractorPermissionFilter]
    search_fields = ["phone", "email", "address_tr", "address_en"]
    filterset_fields = ['id']
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'portal'


class CountryViewSet(BaseViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    # filter_backends = [ContractorPermissionFilter]
    search_fields = ["name_tr", "name_en", "iso2", "iso3", "native", "region", "subregion", "phone_code", "capital"]
    filterset_fields = ['id']
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'portal'
    ordering = ('name_en')


class CityViewSet(BaseViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    # filter_backends = [ContractorPermissionFilter]
    search_fields = ["name", "country__name_tr", "country__name_en"]
    filterset_fields = ['id', 'country_id']
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'portal'
    ordering = ('name')


class SchoolViewSet(BaseViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    read_serializer_class = SchoolDetailSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SchoolPriceRangeFilter]
    search_fields = ["title_tr", "title_en", "description_tr", "description_en", "price"
        , "price_unit__display_name_tr", "price_unit__display_name_en"
        , "country__name_tr", "country__name_en"
        , "city__name"
        , "type__display_name_tr", "type__display_name_en"
                     ]
    filterset_fields = ['id', 'country', 'city', "type"]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'portal'


@api_view(('POST',))
# @permission_classes([IsAuthenticated, ])
@throttle_classes([PortalThrottle])
def get_main_page_schools(request):
    result = []
    scholls = School.objects.values(
        'country__name_tr', 'country_id', 'country__image', 'country__name_en'
    ).annotate(count=Count('country__id')).order_by('-count')

    for sc in scholls:
        result.append(
            {
                "id": sc['country_id'],
                "name_tr": sc['country__name_tr'],
                "name_en": sc['country__name_en'],
                "image": sc['country__image'],
                "count": sc['count']
            }
        )

    return Response(result)


@api_view(('POST',))
@permission_classes([IsAdminUser, ])
@throttle_classes([PortalThrottle])
def save_to_crm(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    user = User.objects.filter(email=email).first()
    if user:
        try:
            if user.is_send_crm:
                raise APIException("Already save to crm!")
            hubspot.create_contact(first_name=first_name, last_name=last_name, email=email)
            user.is_send_crm = True
            user.save()
        except Exception as e:
            raise APIException(e.msg)

        return Response({'result': 1})


@api_view(('POST',))
# @permission_classes([IsAdminUser, ])
@throttle_classes([PortalThrottle])
def get_price_range(request):
    country = request.data.get('country')
    type = request.data.get('type')
    city = request.data.get('city')
    kwargs = {}
    if country:
        kwargs['country'] = country
    if type:
        kwargs['type'] = type
    if city:
        kwargs['city'] = city

    max = School.objects.filter(**kwargs).aggregate(Max('price'))
    min = School.objects.filter(**kwargs).aggregate(Min('price'))
    return Response({'max': max['price__max'] if max['price__max'] else 0 , 'min': min['price__min'] if min['price__min'] else 0 })
