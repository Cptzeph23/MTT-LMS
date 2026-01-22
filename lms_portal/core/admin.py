from django.contrib import admin
from .models import (
    Student,
    Staff,
    FeeCategory,
    FeeStructure,
    Profile
)

# ---------------------
# STUDENT
# ---------------------
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'admission_number',
        'full_name',
        'class_name',
        'academic_year',
        'created_at'
    )
    search_fields = ('admission_number', 'full_name')
    list_filter = ('class_name', 'academic_year')


# ---------------------
# STAFF
# ---------------------
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'staff_number',
        'full_name',
        'role',
        'department',
        'phone'
    )
    search_fields = ('staff_number', 'full_name')
    list_filter = ('role', 'department')


# ---------------------
# FEE CATEGORY
# ---------------------
@admin.register(FeeCategory)
class FeeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


# ---------------------
# FEE STRUCTURE
# ---------------------
@admin.register(FeeStructure)
class FeeStructureAdmin(admin.ModelAdmin):
    list_display = (
        'fee_category',
        'class_name',
        'amount',
        'academic_year'
    )
    list_filter = ('academic_year', 'class_name')
    search_fields = ('class_name',)


# ---------------------
# PROFILE (USER ROLE)
# ---------------------
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username',)



















