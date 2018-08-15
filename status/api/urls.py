from django.conf.urls import include, url
from django.contrib import admin
from .views import (
    StatusAPIView, 
    StatusDetailAPIView, 
)

urlpatterns = [
    # Examples:
    url(r'^$', StatusAPIView.as_view()),
    url(r'^(?P<pk>\d+)/detail/$', StatusDetailAPIView.as_view()),
    # url(r'^blog/', include('blog.urls')),
]
