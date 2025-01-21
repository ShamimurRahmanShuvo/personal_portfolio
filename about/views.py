from django.shortcuts import render
from about.models import Biography, Skill


# Create your views here.
def about_index(request):
    bio = Biography.objects.first()
    skills = Skill.objects.all()
    context = {
        "bio": bio,
        "skills": skills
    }
    return render(request, "about/about_index.html", context)
