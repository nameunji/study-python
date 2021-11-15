from django.db import models


class JobOffer(models.Model):
    company_name = models.CharField(max_length=50)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=60)
    job_description = models.TextField()
    salary = models.PositiveIntegerField()
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.company_name} : {self.job_title}"


c = {
    "company_name": "Google",
    "company_email": "google@gmail.com",
    "job_title": "Backend Junior Developer",
    "job_description": "We find a backend junior developer.",
    "salary": 40000,
    "city": "Seoul",
    "state": "Gurogu",
    "available": True
}