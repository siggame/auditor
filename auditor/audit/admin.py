from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import Service, ServiceAlias, ServiceComponent, Role, Need


class ServiceAdmin(admin.ModelAdmin):
    pass


class ServiceAliasInlineAdmin(admin.StackedInline):
    model = ServiceAlias


class ServiceComponentAdmin(admin.ModelAdmin):
    pass


class RoleAdmin(admin.ModelAdmin):
    pass


class NeedAdmin(admin.ModelAdmin):
    pass


class UserAdmin(UserAdmin):
    inlines = (
        ServiceAliasInlineAdmin,
    )


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceComponent, ServiceComponentAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Need, NeedAdmin)
admin.site.register(User, UserAdmin)
