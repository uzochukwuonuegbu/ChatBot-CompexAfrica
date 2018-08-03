from django.conf.urls import include, url
from django.contrib import admin




urlpatterns = [
    # Examples:
    # url(r'^$', 'chatterbott.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^status/', include('status.api.urls')),
    url(
        r'^chatterbot/',
        include('chatterbot.ext.django_chatterbot.urls',
        namespace='chatterbot')
    ),
]
