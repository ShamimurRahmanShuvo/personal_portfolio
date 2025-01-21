from django.shortcuts import render
from pages.models import Profile


# Create your views here.
def home(request):
    profiles = Profile.objects.first()
    context = {
        "profiles": profiles
    }
    return render(request, "pages/home.html", context)
