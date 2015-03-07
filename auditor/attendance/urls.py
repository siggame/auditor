from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserList, MeetingList, AttendanceCreate


urlpatterns = [
    url(r'^users/$', UserList.as_view()),
    url(r'^meetings/$', MeetingList.as_view()),
    url(r'^create/$', AttendanceCreate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
