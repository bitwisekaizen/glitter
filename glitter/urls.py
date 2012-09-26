from django.conf.urls import patterns, include, url
from backend.views import Messages

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'backend.views.index'),
    url(r'^messages/?', Messages.as_view()),
    # Examples:
    # url(r'^$', 'glitter.views.home', name='home'),
    # url(r'^glitter/', include('glitter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
