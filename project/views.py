# Http 
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader


# Database
from django.contrib.auth.models import User
from project.models import Project, Feature, Project_Type

# Utility
import datetime
from django.conf import settings
from django.utils import simplejson


####################################
#
# Project Ranking Page ( Portfolio Main )
# Description :
#   show a list of project in terms of its ranking 
#
####################################
def project_ranking_page(request, user_name):

    selected_user = User.objects.get(username=user_name)
    
    AllProj =  Project.objects.filter(user = selected_user)
    FullPath = request.get_full_path()    
        
    return render_to_response(
        'project/project_ranking_page.html',
        {
           'AllProj': AllProj,
           'UserName':user_name,
           'FullPath':FullPath,
        }
    )

####################################################################
###   Ranking Filter
###   Can Be Ranked By Project Type, Complete Time, Ranking Algorithm 
###   Handle Jquery Request, Return List Of Project ID
###   Future:
###    *1. If server don't support python upto 2.7, importing "simpleJson" is a problem.
###     2. Recommend For You is still under construction
###     3. Best Rank didn't involve user time on page
####################################################################
def rankfilter(request, user_name):

    # message variable = debuggin use
    message = "welcome to rankfilter, you should not see this" 
    selected_user = User.objects.get(username=user_name)
    
    # next 3 if conditions handle jquery request
    if request.is_ajax():
        if request.method == u'GET':
            GET = request.GET
            if GET.has_key(u'filter_option'):
                filter_option = GET[u'filter_option']
                
                # Dictionary is created to return sorted list to client
                j_dict = {'total':0, 'sortedlist':[]} 
                
                # Get total # of projects
                allobj = len(Project.objects.filter(user=selected_user))
                j_dict['total'] = allobj
                
                # Best: Havn't add user time on page
                if filter_option =='Best':
                    
                    bestproj = Project.objects.filter(user=selected_user).order_by('-base_vote')
                    bestlist = []
                    for proj in bestproj:
                        bestlist.append(proj.id)
                    j_dict['sortedlist'] = bestlist
                    json_return = simplejson.dumps(j_dict)
                    
                    return HttpResponse(json_return)

                # Most Recent
                if filter_option =='Most Recent':
                    timeproj = Project.objects.filter(user=selected_user).order_by('-complete_date')
                    timelist = []
                    for proj in timeproj:
                        timelist.append(proj.id)
                    j_dict['sortedlist'] = timelist
                    json_return = simplejson.dumps(j_dict)
                    return HttpResponse(json_return)
                
                # Less Recent 
                if filter_option =='Less Recent':
                    timeproj = Project.objects.filter(user=selected_user).order_by('complete_date')
                    timelist = []
                    for proj in timeproj:
                        timelist.append(proj.id)
                    j_dict['sortedlist'] = timelist
                    json_return = simplejson.dumps(j_dict)

                    return HttpResponse(json_return)

    return HttpResponse(message)


def single_project_page(request, user_name, proj_title):
    selected_user = User.objects.get(username=user_name)

    P_object = Project.objects.get(link = proj_title, user = selected_user)
    F_object = Feature.objects.filter(project = P_object.id).order_by('feature_order')
    FullPath = request.get_full_path()    

    return render_to_response(
        'project/single_project_page.html',
        {
            'project': P_object,
            'featurelist': F_object,
            'UserName':user_name,
            'FullPath': FullPath,
        }
    )

def publication_rank(request, user_name):
    
    selected_user = User.objects.get(username=user_name)
    P_object = Project.objects.filter(user = selected_user)
    FullPath = request.get_full_path()    
    Publist = []
    for i in P_object:
        if i.PDF !='none':
            Publist.append(i)

    return render_to_response(
        'project/publication_rank.html',
        {
            'publications': Publist,
            'FullPath': FullPath,
            'UserName':user_name,
        }
    )


def publication_link(request, user_name, proj_title):
    
    P_object = Project.objects.get(link = proj_title, user = selected_user)
    F_object = Feature.objects.filter(project = P_object.id).order_by('feature_order')
    FullPath = request.get_full_path()    

    return render_to_response(
        'project/show_proj.html',
        {
            'project': P_object,
            'featurelist': F_object,
            'UserName':user_name,
            'FullPath': FullPath,
        }
    )

def create_new_project(request, user_name):

    return render_to_response(
        'project/createpage.html',

        {
            'UserName':user_name,
        }
    )
