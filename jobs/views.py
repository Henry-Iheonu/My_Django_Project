from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job

@login_required
def post_job_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        job_type = request.POST.get('job_type')
        salary = request.POST.get('salary')
        educational_requirements = request.POST.get('educational_requirements')
        description = request.POST.get('description')

        # Create a new job post
        job = Job.objects.create(
            employer=request.user,
            title=title,
            job_type=job_type,
            salary=salary,
            educational_requirements=educational_requirements,
            description=description
        )
        messages.success(request, "Job listing posted successfully.")
        return redirect('employer_dashboard')  # Redirect to the employer's dashboard

    return render(request, 'jobs/post_job.html')