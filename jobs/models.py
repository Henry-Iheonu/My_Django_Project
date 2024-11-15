from django.db import models
from django.conf import settings

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('part_time', 'Part-Time'),
        ('full_time', 'Full-Time'),
        ('contract', 'Contract'),
    ]

    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    educational_requirements = models.TextField()
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.title} ({self.get_job_type_display()}) - {self.employer.name}"
# Create your models here.
