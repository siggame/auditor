from django.contrib import admin
from .models import Meeting, Attendance


class AttendanceInlineAdmin(admin.TabularInline):
    model = Attendance
    fields = ('user', 'date')
    readonly_fields = ('date',)
    extra = 0


@admin.register(Meeting)
class MeetingAdmin (admin.ModelAdmin):
    inlines = (
        AttendanceInlineAdmin,
    )
    list_display = ('name', 'date', 'head_count', 'attendance_open')
