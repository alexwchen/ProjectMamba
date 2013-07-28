from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('project.views',

    # get project ranking page
    url(r'^$', 'project_ranking_page'),

    # this is API, used to retreieve rank of all project
    url(r'^rankfilter/$', 'rankfilter'),

    # create new project page
    url(r'^create/$', 'create_new_project'),

    # display indivisual projects
    url(r'^(?P<proj_title>\w+)/$', 'single_project_page'),
    


)
