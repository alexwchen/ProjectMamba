from django.http import HttpResponse
from contact.models import Contact, Supervisor, Supervisor_Affiliation, Supervisor_Department, Supervisor_Famous_paper
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.conf import settings

def contact_display(request, user_name):
    Contacts =  Contact.objects.get(pk=1)
    Supervisors =  Supervisor.objects.all()
    supervisor_list = []    
    for supervisor_for_loop in Supervisors:
        s = {}
        affiliation = Supervisor_Affiliation.objects.filter(supervisor = supervisor_for_loop)
        department = Supervisor_Department.objects.filter(supervisor = supervisor_for_loop)
        famous_paper = Supervisor_Famous_paper.objects.filter(supervisor = supervisor_for_loop)

        s['affiliation'] = affiliation
        s['department'] = department
        s['famous_paper'] = famous_paper 
        s['supervisor'] = supervisor_for_loop 
        s['research_interest'] = str(supervisor_for_loop.research_interest).split(',')
        supervisor_list.append(s) 

        print s['affiliation'][0]
    return render_to_response(
        'contact/contact.html',
        {
           'Contact': Contacts,
           'UserName': user_name,
           'Supervisors': Supervisors,
           'Supervisor_detail': supervisor_list
        }
    )
