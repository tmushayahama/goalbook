from django.conf.urls import patterns, url

from rm import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^login/$', 'rm.views.login_user'),
)
