from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('resume.views',
    url(r'^$', 'resume_display'),

)
