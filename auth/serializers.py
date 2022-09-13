from rest_framework import serializers

from user.models import User, Customer, Parameter, ParameterGroup, Contractor
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import datetime
import pytz

from bunguo import utils



# from project.models import Role


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        # token['name'] = user.name
        # ...

        return token

    def validate(self, attrs):
        user = User.objects.filter(email=attrs['email'])
        if len(user) > 0:
            user = user[0]
            if not user.is_superuser and not user.is_valid:
                raise serializers.ValidationError({'detail': "User is not valid, please check your email box."})
        return super().validate(attrs)


class UserSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()
    contractor_name = serializers.CharField(source='contractor.name', read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

    def get_permissions(self, obj):
        if obj.is_superuser:
            return []
        request_types = ['read', 'write', 'create', 'delete']
        # roles = Role.objects.filter(code__in=obj.get_roles())
        roles = []
        if len(roles) == 0:
            return []

        permissions = {}

        for request_type in request_types:
            permitted_modules = []

            for role in roles:
                codes = role.get_module_codes(request_type)
                permitted_modules += codes

            permissions.update({request_type: list(set(permitted_modules))})

        return permissions

    class Meta:
        model = User
        exclude = ('password', 'last_login', 'is_staff', 'date_joined', 'groups', 'role')


class UserDetailSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()
    contractor_name = serializers.CharField(source='contractor.name', read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    end_date = serializers.SerializerMethodField()
    start_date = serializers.SerializerMethodField()
    # package = serializers.SerializerMethodField()  # Package method not found
    user_count = serializers.SerializerMethodField()

    def get_user_count(self, obj):
        if obj.contractor:
            return obj.contractor.user_count
        return 0

    def get_start_date(self, obj):
        if obj.contractor and obj.contractor.created_at:
            return str(obj.contractor.created_at.strftime("%d-%m-%Y"))
        return ''

    def get_end_date(self, obj):
        if obj.contractor and obj.contractor.expire_date:
            return str(obj.contractor.expire_date.strftime("%d-%m-%Y"))

        return ''

    def get_permissions(self, obj):
        if obj.is_superuser:
            return []
        request_types = ['read', 'write', 'create', 'delete']
        # roles = Role.objects.filter(code__in=obj.get_roles())
        roles = []
        if len(roles) == 0:
            return []

        permissions = {}

        for request_type in request_types:
            permitted_modules = []

            for role in roles:
                codes = role.get_module_codes(request_type)
                permitted_modules += codes

            permissions.update({request_type: list(set(permitted_modules))})

        return permissions

    class Meta:
        model = User
        exclude = ('password', 'last_login', 'is_staff', 'date_joined', 'groups', 'role')


class ParameterGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParameterGroup
        fields = '__all__'


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = '__all__'


class ParameterDetailSerializer(serializers.ModelSerializer):
    parameter_group = ParameterGroupSerializer()

    class Meta:
        model = Parameter
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    # currency_unit_name = serializers.CharField(source='currency_unit.name', read_only=True)

    # currency_unit = ParameterSerializer()

    class Meta:
        model = Customer
        fields = '__all__'


class ContractorSerializer(serializers.ModelSerializer):
    user_count = serializers.SerializerMethodField(read_only=True)

    def get_user_count(self, obj):
        return User.objects.filter(contractor__id=obj.id).count()

    class Meta:
        model = Contractor
        fields = '__all__'


class CustomerDetailSerializer(serializers.ModelSerializer):
    currency_unit_name = serializers.CharField(source='currency_unit.display_name')
    balance = serializers.SerializerMethodField()
    check_balance = serializers.SerializerMethodField()
    bill_balance = serializers.SerializerMethodField()
    purchase_total = serializers.SerializerMethodField()
    order_total = serializers.SerializerMethodField()
    not_paid = serializers.SerializerMethodField()


    class Meta:
        model = Customer
        fields = '__all__'
