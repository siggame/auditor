from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    # Built-in admin
    url(r'^admin/', include(admin.site.urls)),

    # Login for rest framework's browsable API
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Attendance API
    url(r'^api/attendance/', include('auditor.attendance.urls')),

    # Audit API
    url(r'^api/audit/', include('auditor.audit.urls')),
)
