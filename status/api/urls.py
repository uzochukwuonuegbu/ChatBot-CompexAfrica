from django.conf.urls import include, url
from django.contrib import admin
from .views import (
    StatusAPIView, 
    StatusCreateAPIView,
    StatusDetailAPIView, 
    StatusUpdateAPIView, 
    StatusDeleteAPIView)

urlpatterns = [
    # Examples:
    url(r'^$', StatusAPIView.as_view()),
    url(r'^create/$', StatusCreateAPIView.as_view()),
    url(r'^(?P<pk>\d+)/update/$', StatusUpdateAPIView.as_view()),
    url(r'^(?P<pk>\d+)/detail/$', StatusDetailAPIView.as_view()),
    url(r'^(?P<pk>\d+)/delete/$', StatusDeleteAPIView.as_view()),
    # url(r'^blog/', include('blog.urls')),
]
