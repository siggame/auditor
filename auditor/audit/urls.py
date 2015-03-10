from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ServiceList


urlpatterns = [
    url(r'^services/$', ServiceList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
