from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^Animal/List/$', views.AnimalList.as_view()),
    url(r'^Animal/ID/(?P<pk>[0-9]+)/$', views.AnimalDetail.as_view()),
    url(r'^Animal/Create/$', views.AnimalCreate.as_view()),
    url(r'^Animal/Delete/(?P<pk>[0-9]+)/$', views.AnimalDelete),
]

urlpatterns = format_suffix_patterns(urlpatterns)
