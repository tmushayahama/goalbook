from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                           # url(r'^$', 'rooms_101.views.home', name='home'),
                       # url(r'^rooms_101/', include('rooms_101.foo.urls')),
                       
                       # Uncomment the admin/doc line below to enable admin documentation:
                           # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                           url(r'^admin/', include(admin.site.urls)),
)
