
from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'new.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^add/$', 'plivoapp.views.new_contact', name='new_contact'),
    url(r'^edit/$', 'plivoapp.views.edit_contact', name='edit_contact'),
    url(r'^delete/$', 'plivoapp.views.delete_contact', name='delete_contact'),
    url(r'^search/$', 'plivoapp.views.search_term')
    
)
