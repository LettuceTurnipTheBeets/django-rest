from django.urls import path, re_path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = format_suffix_patterns([
    path('Animal/List/', views.AnimalList.as_view()),
    re_path('Animal/Id/(?P<pk>[0-9]+)/$', views.AnimalDetail.as_view()),
])
