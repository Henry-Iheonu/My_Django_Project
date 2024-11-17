from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

# Custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, phone_number, role, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone_number=phone_number, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, name, phone_number, "employer", password, **extra_fields)

# Custom user model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('employer', 'Employer'),
        ('employee', 'Employee'),
    )

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number', 'role']

    def _str_(self):
        return self.email
# Create models here.
