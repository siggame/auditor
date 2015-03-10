from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import Service, ServiceAlias, ServiceComponent, Role, Need


# Unregister default admins for User and Group
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


class ServiceAliasInlineAdmin(admin.StackedInline):
    model = ServiceAlias


@admin.register(ServiceComponent)
class ServiceComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'service')
    ordering = ('service', 'name')


class NeedInlineAdmin(admin.StackedInline):
    model = Need
    fields = ('role', 'component')
    extra = 0


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    inlines = (
        NeedInlineAdmin,
    )


@admin.register(User)
class UserAdmin(UserAdmin):
    inlines = (
        ServiceAliasInlineAdmin,
    )
