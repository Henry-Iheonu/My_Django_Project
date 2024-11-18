from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from jobs.models import Job
from django.utils.timezone import now

User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        role = request.POST.get('role')
        password = request.POST.get('password')

        # Check if the user already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('signup')

        # Create a new user
        user = User.objects.create_user(
            email=email, name=name, phone_number=phone_number, role=role, password=password
        )
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')

    return render(request, 'user_account/signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('dashboard')  # Redirect to the dashboard upon successful login
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')

    return render(request, 'user_account/login.html')

@login_required
def dashboard_view(request):
    if request.user.role == 'employer':
        return redirect('employer_dashboard')
    elif request.user.role == 'employee':
        return redirect('employee_dashboard')
    else:
        # Handle users with unrecognized roles
        return render(request, 'user_account/unknown_role.html')

@login_required
def employee_dashboard_view(request):
    jobs = Job.objects.all()
    context = {
        'jobs': jobs,
        'current_time': now(),
    }
    return render(request, 'user_account/employee_dashboard.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')  # Redirect to login page after logout

@login_required
def employer_dashboard_view(request):
    # Get the logged-in employer's jobs
    employer_jobs = Job.objects.filter(employer=request.user)
    num_jobs_posted = employer_jobs.count()

    # Pass the count to the template
    context = {
        'num_jobs_posted': num_jobs_posted,
    }
    return render(request, 'user_account/employer_dashboard.html', context)