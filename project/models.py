from django.db import models
from bunguo.utils import generate_pk
from bunguo.base_model import BaseModel
from user.models import *
import os
from django.template.defaultfilters import slugify

def banner_directory_path(instance, filename):
    return 'banner_files/{0}/{1}'.format(instance.id, filename)


class Banner(BaseModel):
    file = models.FileField(upload_to=banner_directory_path, blank=True, null=True)
    order = models.IntegerField(default=0)
    id_prefix = "BNR"

    @property
    def filename(self):
        return os.path.basename(self.file.name)

    class Meta:
        db_table = 'banners'


def blog_directory_path(instance, filename):
    return 'blog_files/{0}/{1}'.format(instance.id, filename)


class Blog(BaseModel):
    image = models.FileField(upload_to=blog_directory_path, blank=True, null=True)
    title_tr = models.CharField(max_length=1000)
    title_en = models.CharField(max_length=1000)
    summary_tr = models.TextField(blank=True, null=True, max_length=150)
    summary_en = models.TextField(blank=True, null=True, max_length=150)
    description_tr = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True)
    id_prefix = "BLG"

    @property
    def filename(self):
        return os.path.basename(self.file.name)

    class Meta:
        db_table = 'blogs'


def announcement_directory_path(instance, filename):
    return 'announcement_files/{0}/{1}'.format(instance.id, filename)


class Announcement(BaseModel):
    image = models.FileField(upload_to=announcement_directory_path, blank=True, null=True)
    title_tr = models.CharField(max_length=1000)
    title_en = models.CharField(max_length=1000)
    summary_tr = models.TextField(blank=True, null=True, max_length=150)
    summary_en = models.TextField(blank=True, null=True, max_length=150)
    description_tr = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True)
    id_prefix = "ANN"

    @property
    def filename(self):
        return os.path.basename(self.file.name)

    class Meta:
        db_table = 'announcements'


class ExchangeProgram(BaseModel):
    title_tr = models.CharField(max_length=1000)
    title_en = models.CharField(max_length=1000)
    icon = models.CharField(max_length=200, blank=True, null=True)
    icon_color = models.CharField(max_length=200, blank=True, null=True)
    summary_tr = models.TextField(blank=True, null=True, max_length=150)
    summary_en = models.TextField(blank=True, null=True, max_length=150)
    id_prefix = "EXP"

    class Meta:
        db_table = 'exchangeprograms'


class Contact(BaseModel):
    phone = models.CharField(max_length=1000, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address_tr = models.TextField(blank=True, null=True)
    address_en = models.TextField(blank=True, null=True)
    linkedin = models.CharField(max_length=150, blank=True, null=True)
    facebook = models.CharField(max_length=150, blank=True, null=True)
    instagram = models.CharField(max_length=150, blank=True, null=True)
    pinterest = models.CharField(max_length=150, blank=True, null=True)
    tiktok = models.CharField(max_length=150, blank=True, null=True)
    twitter = models.CharField(max_length=150, blank=True, null=True)
    youtube = models.CharField(max_length=150, blank=True, null=True)
    id_prefix = "CNT"

    class Meta:
        db_table = 'contacts'


def country_directory_path(instance, filename):
    return 'country_files/{0}/{1}'.format(instance.id, filename)


class Country(BaseModel):
    image = models.FileField(upload_to=country_directory_path, blank=True, null=True)
    name_tr = models.CharField(max_length=1000, blank=True, null=True)
    name_en = models.CharField(max_length=1000, blank=True, null=True)
    iso2 = models.CharField(max_length=1000, blank=True, null=True)
    iso3 = models.CharField(max_length=1000, blank=True, null=True)
    numeric_code = models.CharField(max_length=1000, blank=True, null=True)
    phone_code = models.CharField(max_length=1000, blank=True, null=True)
    capital = models.CharField(max_length=1000, blank=True, null=True)
    currency = models.CharField(max_length=1000, blank=True, null=True)
    currency_name = models.CharField(max_length=1000, blank=True, null=True)
    currency_symbol = models.CharField(max_length=1000, blank=True, null=True)
    native = models.CharField(max_length=1000, blank=True, null=True)
    region = models.CharField(max_length=1000, blank=True, null=True)
    subregion = models.CharField(max_length=1000, blank=True, null=True)
    latitude = models.CharField(max_length=1000, blank=True, null=True)
    longitude = models.CharField(max_length=1000, blank=True, null=True)
    emoji = models.CharField(max_length=1000, blank=True, null=True)

    id_prefix = "CNT"

    class Meta:
        db_table = 'countries'


def city_directory_path(instance, filename):
    return 'city_files/{0}/{1}'.format(instance.id, filename)
class City(BaseModel):
    image = models.FileField(upload_to=city_directory_path, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    latitude = models.CharField(max_length=1000, blank=True, null=True)
    longitude = models.CharField(max_length=1000, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True, related_name='city_country')
    id_prefix = "CTY"

    class Meta:
        db_table = 'cities'


def school_directory_path(instance, filename):
    return 'school_files/{0}/{1}'.format(instance.id, filename)

class School(BaseModel):
    title_tr = models.CharField(max_length=1000)
    title_en = models.CharField(max_length=1000)
    description_tr = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    summary_tr = models.TextField(blank=True, null=True, max_length=150)
    summary_en = models.TextField(blank=True, null=True, max_length=150)
    price = models.FloatField(default=0)
    price_unit = models.ForeignKey(Parameter, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='school_price_unit')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True,
                                related_name='school_country')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True, related_name='school_city')
    type = models.ForeignKey(Parameter, on_delete=models.SET_NULL, blank=True, null=True, related_name='school_type')
    image = models.FileField(upload_to=school_directory_path, blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True)
    id_prefix = "SCH"


    class Meta:
        db_table = 'schools'
