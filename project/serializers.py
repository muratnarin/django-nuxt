from rest_framework import serializers
from project.models import *


class BaseSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if 'image' in ret:
            ret['image'] = instance.image.url if instance.image else None
        if 'file' in ret:
            ret['file'] = instance.file.url if instance.file else None
        if 'avatar' in ret:
            ret['avatar'] = instance.avatar.url if instance.avatar else None
        return ret


class BannerSerializer(BaseSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class BlogSerializer(BaseSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class AnnouncementSerializer(BaseSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


class ExchangeProgramSerializer(BaseSerializer):
    class Meta:
        model = ExchangeProgram
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class SchoolSerializer(BaseSerializer):
    class Meta:
        model = School
        fields = '__all__'


class SchoolDetailSerializer(BaseSerializer):
    price_unit_name_tr = serializers.SerializerMethodField()
    price_unit_name_en = serializers.SerializerMethodField()
    country_name_tr = serializers.SerializerMethodField()
    country_name_en = serializers.SerializerMethodField()
    city_name = serializers.SerializerMethodField()
    type_name_tr = serializers.SerializerMethodField()
    type_name_en = serializers.SerializerMethodField()

    def get_price_unit_name_tr(self, obj):
        return obj.price_unit.display_name_tr if obj.price_unit else ""

    def get_price_unit_name_en(self, obj):
        return obj.price_unit.display_name_en if obj.price_unit else ""

    def get_country_name_tr(self, obj):
        return obj.country.name_tr if obj.country else ""

    def get_country_name_en(self, obj):
        return obj.country.name_en if obj.country else ""

    def get_city_name(self, obj):
        return obj.city.name if obj.city else ""

    def get_type_name_tr(self, obj):
        return obj.type.display_name_tr if obj.type else ""

    def get_type_name_en(self, obj):
        return obj.type.display_name_en if obj.type else ""

    class Meta:
        model = School
        fields = '__all__'
