from resumes.models import CustomUser, Resume, Summary, WorkExperience, Education, Publication, Skill, Reference
from django.contrib import admin
#CustomUser, Resume, Summary, WorkExperience, Education, Publication, Skill, Reference

admin.site.register(CustomUser)
admin.site.register(Resume)
admin.site.register(Summary)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Publication)
admin.site.register(Skill)
admin.site.register(Reference)

