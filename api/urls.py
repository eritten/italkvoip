from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url

urlpatterns = [
    path('servers/', views.get_servers, name='servers'),
]
format_suffix_patterns(urlpatterns)