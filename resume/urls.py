from django.urls import path
from resume import views


urlpatterns = [
    path('', views.resume_index, name='resume')
]
