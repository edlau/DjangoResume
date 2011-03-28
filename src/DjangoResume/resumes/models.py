from django.db import models
from django.contrib.auth.models import User, UserManager

class CustomUser(User):
    timezone=models.CharField(max_length=50, default='America/New York')
    objects = UserManager()
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=25, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=50, blank=True)
    display_name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.display_name
    
class Resume(models.Model):
    user = models.ForeignKey(CustomUser)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    last_modified_date = models.DateTimeField('last date modified')
    def __unicode__(self):
        return self.title

class Summary(models.Model):
    resume = models.OneToOneField(Resume)
    headline = models.CharField(max_length=1000)
    details = models.CharField(max_length=2000, blank=True)
    def __unicode__(self):
        return self.headline

class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume)
    company_name = models.CharField(max_length=200) 
    title = models.CharField(max_length=200)
    start_date = models.DateField('date started')
    end_date = models.DateField('date ended', null=True, blank=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=25, blank=True)
    summary = models.CharField(max_length=1000, blank=True)
    details = models.CharField(max_length=2000, blank=True)
    def __unicode__(self):
        return u'%s - %s - %s' % (self.resume, self.company_name, self.title)

class Education(models.Model):
    resume = models.ForeignKey(Resume)
    title = models.CharField(max_length=200)
    institution_name = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    summary = models.CharField(max_length=1000, blank=True)
    details = models.CharField(max_length=2000, blank=True)
    url = models.URLField('link', blank=True) 
    def __unicode__(self):
        return u'%s - %s - %s' % (self.resume, self.institution_name, self.title)
     
class Publication(models.Model):
    resume = models.ForeignKey(Resume)
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    details = models.CharField(max_length=2000, blank=True)
    url = models.URLField('link', blank=True)  
    def __unicode__(self):
        return u'%s - %s' % (self.resume, self.title)
    
class Skill(models.Model):
    resume = models.ForeignKey(Resume)
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=1000, blank=True)
    rating = models.PositiveIntegerField()
    years = models.PositiveIntegerField()
    def __unicode__(self):
        return u'%s - %s' % (self.resume, self.title)
    
class Reference(models.Model):
    resume = models.ForeignKey(Resume)
    name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=50, blank=True)
    summary = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return u'%s - %s' % (self.resume, self.name)  
