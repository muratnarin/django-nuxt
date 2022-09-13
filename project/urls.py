from core.base_view import create_view_paths
from project.views import *
from django.urls import path

urlpatterns = [
    *create_view_paths('banner', BannerViewSet),
    *create_view_paths('blog', BlogViewSet),
    *create_view_paths('announcement', AnnouncementViewSet),
    *create_view_paths('exchangeprogram', ExchangeProgramViewSet),
    *create_view_paths('contact', ContactViewSet),
    *create_view_paths('school', SchoolViewSet),
    *create_view_paths('city', CityViewSet),
    *create_view_paths('country', CountryViewSet),
    path('getmainpageschools/', get_main_page_schools),
    path('savetocrm/', save_to_crm),
    path('getpricerange/', get_price_range),

]

# TODO: Yapılacaklar
# edvisor api


# from django-nuxt import jobs
#
# jobs.start()

# from . import hubspot
