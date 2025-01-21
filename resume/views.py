from django.shortcuts import render
from resume.models import Summary, Education, Experience, JobResponsibility


# Create your views here.
def resume_index(request):
    summary = Summary.objects.first()
    educations = Education.objects.all()
    experiences = Experience.objects.all().order_by('-start_year').values()
    job_responsibilities = JobResponsibility.objects.all()
    context = {
        "summary": summary,
        "educations": educations,
        "experiences": experiences,
        "job_responsibilities": job_responsibilities
    }
    return render(request, "resume/resume_index.html", context)
