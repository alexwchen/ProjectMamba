from django.db import models
from django.contrib.auth.models import User

##################################
# Resume Content Models
##################################

class Education (models.Model):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    skills_programming_languages = models.TextField()
    skills_design_tools = models.TextField()
    
    def __unicode__(self):
        return '('+str(self.user)+')' + "--" + self.title

class Job(models.Model): 
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    period = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    detail = models.TextField()
    job_type = models.CharField(max_length=200)

    def __unicode__(self):
        return '('+str(self.user)+')' + "--" + self.title

class Affiliation(models.Model): 
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    period = models.CharField(max_length=200)

    def __unicode__(self):
        return '('+str(self.user)+')' + "--" + self.title

