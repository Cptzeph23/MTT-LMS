from django.db import models

class Student(models.Model):
    admission_number = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField(null=True, blank=True)

    class_name = models.CharField(max_length=100)
    academic_year = models.CharField(max_length=20)

    guardian_name = models.CharField(max_length=200)
    guardian_phone = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.admission_number})"
