from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_account.urls')),  # Redirects root URL to the user_accounts app
    path('jobs/', include('jobs.urls')),
]