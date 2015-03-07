from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import Service, ServiceAlias, ServiceComponent, Role, Need


# Unregister default admins for User and Group
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


class ServiceAliasInlineAdmin(admin.StackedInline):
    model = ServiceAlias


@admin.register(ServiceComponent)
class ServiceComponentAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Need)
class NeedAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(UserAdmin):
    inlines = (
        ServiceAliasInlineAdmin,
    )
