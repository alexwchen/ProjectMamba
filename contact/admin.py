from contact.models import Contact, Supervisor, Supervisor_Affiliation, Supervisor_Department, Supervisor_Famous_paper
from django.contrib import admin

###############################
#   Supervisor related models
###############################
class Supervisor_AffiliationInline(admin.TabularInline):
    model=Supervisor_Affiliation
    extra=0

class Supervisor_DepartmentInline(admin.TabularInline):
    model=Supervisor_Department
    extra=0

class Supervisor_Famous_paperInline(admin.TabularInline):
    model=Supervisor_Famous_paper
    extra=0

class SupervisorAdmin(admin.ModelAdmin):
    fieldsets=[
    ('Personal Info', {'fields':['name', 'email', 'position', 'university']}),
    ('Meta Info', {'fields':['contact', 'start_date', 'end_date', 'image_path', 'link','display_order']}),
    ('Tag Info', {'fields':['field', 'research_interest']}),
    ]

    inlines = [Supervisor_AffiliationInline,Supervisor_DepartmentInline,Supervisor_Famous_paperInline]

###############################
#   Contact related models
###############################

class SupervisorInline(admin.StackedInline):
    model=Supervisor
    extra=0
   
class ContactAdmin(admin.ModelAdmin):
    fields= [
    'user',
    'title_contact',
    'email',
    'title_research',
    'research_interest',
    ]
    inlines = [SupervisorInline]


###############################################
# the following section is not displayed due 
# to clearity of the admin interface
###############################################

admin.site.register(Supervisor,SupervisorAdmin)
admin.site.register(Contact, ContactAdmin)
