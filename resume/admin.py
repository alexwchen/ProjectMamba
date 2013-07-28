from resume.models import Education, Job, Affiliation
from django.contrib import admin

###############################
#   Resume related models
###############################

class JobsAdmin(admin.ModelAdmin):
    fields = [
    'user',
    'title',
    'job_type',
    'company',
    'period',
    'start_date',
    'end_date',
    'detail'
    ]

class EducationAdmin(admin.ModelAdmin):
    fields = [
    'user',
    'title',
    'degree',
    'program',
    'duration',
    'skills_programming_languages',
    'skills_design_tools',
    ]

class AffiliationAdmin(admin.ModelAdmin):
    fields= [
    'user',
    'title',
    'period',
    ]

###############################################
# the following section is not displayed due 
# to clearity of the admin interface
###############################################

admin.site.register(Education, EducationAdmin)
admin.site.register(Affiliation, AffiliationAdmin)
admin.site.register(Job, JobsAdmin)
