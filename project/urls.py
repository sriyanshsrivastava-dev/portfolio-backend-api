from django.urls import path

from project.views import ProjectCollection

urlpatterns = [
    path('all', ProjectCollection.as_view(), name="all_projects"),
]