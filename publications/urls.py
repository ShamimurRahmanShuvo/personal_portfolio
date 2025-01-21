from django.urls import path
from publications import views


urlpatterns = [
    path('', views.publication_index, name='publications'),
    path("<int:pk>/", views.publication_detail, name="publication_detail"),
]
