from django.conf.urls import patterns, include, url
from django.shortcuts import render_to_response
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home.html', 'MontyHall.views.home', name='home'),
    url(r'^play/', include('monty.urls')),
    # url(r'^MontyHall/', include('MontyHall.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'MontyHall.views.home', name='home'),
    (r'^media_url/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/will/MontyHall/images/'}),
)
