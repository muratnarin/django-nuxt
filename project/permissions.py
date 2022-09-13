from rest_framework.permissions import BasePermission

from datetime import datetime
import pytz


# from project.models import Role


class RolePermission(BasePermission):
    # action_types = {
    #     'list': 'read',
    #     'retrieve': 'read',
    #     'update': 'write',
    #     'create': 'create',
    #     'destroy': 'delete',
    # }
    #
    # admin_models = ['unit', 'sku', 'role']

    # has_pemission her requestte girer
    # has_object_permission sadece delete, update put vs. zamanda girer.
    def has_permission(self, request, view):
        user = request.user
        if user.is_superuser:
            return True
        action = getattr(view, 'action', None)
        if action is None:
            return True
        # request_type = self.action_types.get(action)
        if action == 'list' or action == 'retrieve':
            return True
        elif action == 'update':
            if not user.is_superuser:
                return False
        elif action == 'create':
            if not user.is_superuser:
                return False
        elif action == 'delete':
            if not user.is_superuser:
                return False
        # _data = view.queryset.model.objects.filter(id=request.data['id']).first()
        # has_contractor = getattr(view.queryset.model, 'contractor', None)
        # if _data:
        #     if has_contractor:
        #         if not _data.contractor_id == request.user.contractor_id:
        #             return False

        # content = view.queryset.model.__name__.lower()
        #
        # if content in self.admin_models:
        #     return False
        # utc = pytz.UTC
        # if user.contractor.expire_date < datetime.now().date():
        #     return False
        #
        # if content is not None and request_type is not None:
        #     # user_roles = Role.objects.filter(code__in=user.get_roles())
        #     # for role in user_roles:
        #     #     module_codes = role.get_module_codes(request_type)
        #     #     if content in module_codes:
        #     #         return True
        #     return True
        # else:
        #     return False
