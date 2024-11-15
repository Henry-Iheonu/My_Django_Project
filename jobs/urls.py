from django.urls import path
from .views import post_job_view

urlpatterns = [
    path('post-job/', post_job_view, name='post_job'),  # URL for posting a job
]