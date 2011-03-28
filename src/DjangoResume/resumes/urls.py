from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('resumes.views',
    (r'^$', 'index'),
    (r'^(?P<resume_id>\d+)/$', 'detail'),
)
