from django.urls import path
from .views import signup_view, login_view, dashboard_view, employer_dashboard_view, employee_dashboard_view, logout_view

urlpatterns = [
    path('', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard/employer/', employer_dashboard_view, name='employer_dashboard'),
    path('dashboard/employee/', employee_dashboard_view, name='employee_dashboard'),
    path('logout/', logout_view, name='logout'),  # Logout URL
]