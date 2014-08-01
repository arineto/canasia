from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^logout/$', 'core.views.logout_aux', name='logout'),
    url(r'^overview/$', 'core.views.overview', name='overview'),
    url(r'^overview/(?P<filter_value>.+)/$', 'core.views.overview', name='overview'),
    url(r'^dashboard/$', 'core.views.dashboard', name='dashboard'),

    url(r'^forgot_password/$', 'core.views.forgot_password', name='forgot_password'),  
    url(r'^change_password/$', 'core.views.change_password', name='change_password'), 

    url(r'^add_project/$', 'core.views.add_project', name='add_project'),
    url(r'^edit_project/(?P<project_id>\d+)/$', 'core.views.edit_project', name='edit_project'),
    url(r'^delete_project/(?P<project_id>\d+)/$', 'core.views.delete_project', name='delete_project'),

    url(r'^admin/', include(admin.site.urls)),
)
