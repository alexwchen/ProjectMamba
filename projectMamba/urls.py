from django.conf.urls import patterns, include, url

# static file
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projectMamba.views.home', name='home'),
    # url(r'^projectMamba/', include('projectMamba.foo.urls')),
    
    # admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #resume
    url(r'^(?P<user_name>\w+)/resume/', include('resume.urls')),
    
    #contact
    url(r'^(?P<user_name>\w+)/contact/', include('contact.urls')),

    #portfolio
    url(r'^(?P<user_name>\w+)/projects/', include('project.urls')),
    url(r'^(?P<user_name>\w+)$','project.views.project_ranking_page'),
    url(r'^(?P<user_name>\w+)/$','project.views.project_ranking_page'),
   
    #publication
    url(r'^(?P<user_name>\w+)/publication/$','project.views.publication_rank'),
    url(r'^(?P<user_name>\w+)/publication/(?P<proj_title>\w+)/$','project.views.publication_link'),


    # static files 
    url(r'^static_media_alex/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^.*/static_media_alex/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
