#CustomUser, Resume, Summary, WorkExperience, Education, Publication, Skill, Reference

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from resumes.models import CustomUser, Resume, Summary, WorkExperience, Education, Publication, Skill, Reference
from django.core.exceptions import ObjectDoesNotExist

#As a resume, there is really no point of having multiple views, for now we'll get a
#list/index view
def index(request):
    latest_resume_list = Resume.objects.all().order_by('last_modified_date')[:5]
    return render_to_response('resumes/index.html', {'latest_resume_list':latest_resume_list})
    
def detail(request, resume_id):
    r = get_object_or_404(Resume, pk=resume_id)
    customuser = get_object_or_404(CustomUser,pk=r.user)
    summary = Summary.objects.get(resume=resume_id)
    
    try:
        workexperience_list = WorkExperience.objects.filter(resume=resume_id)
    except ObjectDoesNotExist:
        workexperience_list = {}
    
    try:
        education_list = Education.objects.filter(resume=resume_id)
    except ObjectDoesNotExist:
        education_list = {}
    
    try:
        publication_list = Publication.objects.filter(resume=resume_id)
    except ObjectDoesNotExist:
        publication_list = {}
    
    try:
        skill_list = Skill.objects.filter(resume=resume_id)
    except ObjectDoesNotExist:
        skill_list = {}

    try:
        reference_list = Reference.objects.filter(resume=resume_id)
    except ObjectDoesNotExist:
        reference_list = {}
     
    return render_to_response('resumes/detail.html', 
                              {'resume':r,
                               'customuser':customuser,
                               'summary':summary,
                               'workexperience_list':workexperience_list,
                               'education_list':education_list,
                               'publication_list':publication_list,
                               'skill_list':skill_list,
                               'reference_list':reference_list,
                               },
                              context_instance=RequestContext(request))
