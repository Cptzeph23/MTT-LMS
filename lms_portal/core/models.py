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

class Staff(models.Model):
    ROLE_CHOICES = [
        ('teacher', 'Teacher'),
        ('cook', 'Cook'),
        ('driver', 'Driver'),
        ('secretary', 'Secretary'),
        ('security', 'Security'),
    ]

    staff_number = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=200)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    department = models.CharField(max_length=100, blank=True)
    date_joined = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.role})"


class FeeCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class FeeStructure(models.Model):
    fee_category = models.ForeignKey(FeeCategory, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    academic_year = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.fee_category.name} - {self.class_name} ({self.academic_year})"




