from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
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
                       url(r'^$', 'rm.views.login_user'),
                       url(r'^rm/', include('rm.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/$', 'rm.views.login_user'),
                       url(r'^logout/$', 'rm.views.logout_user'),
                       url(r'^home/$', 'rm.views.home_page'),
                       url(r'^register/$', 'rm.views.register_user'),
                       #url(r'^(?P<name>.*)/$', 'rm.views.'),
)
if settings.DEBUG:
    urlpatterns += static('/css/', document_root='rm/static/css/')
    urlpatterns += static('/images/', document_root='rm/static/images/')
    urlpatterns += static('/js/', document_root='rm/static/js/')
