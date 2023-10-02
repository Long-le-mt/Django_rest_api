from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    # def has_permission(self, request, view):
    #     user = request.user
    #     print(request.user, user.get_all_permissions())

    #     # cách này không hiệu quả vì chỉ cần 1 rule tồn tại thì tất cả các rule sau đều pass
    #     # Ex: user chỉ có quyền add, người dùng vào edit thì vẫn pass vì lúc này ta đã check user có quyền add và return True
    #     if user.is_staff:
    #         if user.has_perm("products.add_product"): #app_verb_model
    #             return True
    #         if user.has_perm("products.delete_product"):
    #             return True
    #         if user.has_perm("products.change_product"):
    #             return True
    #         if user.has_perm("products.view_product"):
    #             return True
    #         return False
    #     return False

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)