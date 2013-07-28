from django.db import models
from django.contrib.auth.models import User

##################################
# Contact & Supervisor Content Model
##################################
        
class Contact(models.Model): 
    user = models.OneToOneField(User)
    title_contact = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    title_research = models.CharField(max_length=200)
    research_interest = models.TextField(max_length=200)

    def __unicode__(self):
        return '('+str(self.user)+')' + "--" + self.title_contact

# supervisor related model starts here
class Supervisor(models.Model): 
    contact = models.ForeignKey(Contact)
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    display_order = models.IntegerField()
    email = models.CharField(max_length=200)
    field = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    image_path = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    research_interest = models.TextField(max_length=200)

    def __unicode__(self):
        return self.name

class Supervisor_Affiliation(models.Model):
    supervisor = models.ForeignKey(Supervisor)
    title = models.CharField(max_length=200, default="none")
    def __unicode__(self):
        return self.title

class Supervisor_Department(models.Model):
    supervisor = models.ForeignKey(Supervisor)
    title = models.CharField(max_length=200, default="none")
    def __unicode__(self):
        return self.title

class Supervisor_Famous_paper(models.Model):
    supervisor = models.ForeignKey(Supervisor)
    title = models.CharField(max_length=200, default="none")
    author = models.CharField(max_length=200, default="none")
    conference = models.CharField(max_length=200, default="none")
    def __unicode__(self):
        return self.title
