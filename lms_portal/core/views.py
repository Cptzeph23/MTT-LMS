from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student, Staff, FeeCategory, FeeStructure, Profile
from .utils import render_to_pdf


# -------------------------------
# Role-Based Decorator
# -------------------------------
def role_required(allowed_roles):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            role = getattr(request.user.profile, 'role', None)
            if role not in allowed_roles:
                return redirect('login')
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


# -------------------------------
# LOGIN / LOGOUT
# -------------------------------
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            role = user.profile.role

            if role == "finance_admin":
                return redirect('finance_dashboard')
            elif role == "academic_admin":
                return redirect('academic_dashboard')
            elif role == "staff_admin":
                return redirect('staff_dashboard')
            else:
                return redirect('admin_dashboard')

        else:
            messages.error(request, "Invalid credentials")

    return render(request, "core/login.html")

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


# -------------------------------
# ADMIN DASHBOARD
# -------------------------------
@login_required
def admin_dashboard(request):
    return render(request, "core/admin_dashboard.html")


# -------------------------------
# STUDENT VIEWS
# -------------------------------
@role_required(['super_admin', 'academic_admin'])
def student_list(request):
    students = Student.objects.all().order_by('-created_at')
    return render(request, "core/student_list.html", {"students": students})


@role_required(['super_admin', 'academic_admin'])
def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            admission_number=request.POST.get("admission_number"),
            full_name=request.POST.get("full_name"),
            gender=request.POST.get("gender"),
            class_name=request.POST.get("class_name"),
            academic_year=request.POST.get("academic_year"),
        )
        return redirect('student_list')
    return render(request, "core/add_student.html")


@role_required(['super_admin', 'academic_admin'])
def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, "core/student_detail.html", {"student": student})


# -------------------------------
# STAFF VIEWS
# -------------------------------
@role_required(['super_admin', 'staff_admin'])
def staff_list(request):
    staff_members = Staff.objects.all().order_by('-created_at')
    return render(request, "core/staff_list.html", {"staff_members": staff_members})


@role_required(['super_admin', 'staff_admin'])
def add_staff(request):
    if request.method == "POST":
        Staff.objects.create(
            staff_number=request.POST.get("staff_number"),
            full_name=request.POST.get("full_name"),
            role=request.POST.get("role"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            department=request.POST.get("department"),
            date_joined=request.POST.get("date_joined") or None,
        )
        return redirect('staff_list')
    return render(request, "core/add_staff.html")


@role_required(['super_admin', 'staff_admin'])
def staff_detail(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    return render(request, "core/staff_detail.html", {"staff": staff})


# -------------------------------
# FEE CATEGORY & STRUCTURE
# -------------------------------
@role_required(['super_admin', 'finance_admin'])
def fee_category_list(request):
    categories = FeeCategory.objects.all()
    return render(request, "core/fee_category_list.html", {"categories": categories})


@role_required(['super_admin', 'finance_admin'])
def add_fee_category(request):
    if request.method == "POST":
        FeeCategory.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description")
        )
        return redirect('fee_category_list')
    return render(request, "core/add_fee_category.html")


@role_required(['super_admin', 'finance_admin'])
def fee_structure_list(request):
    fees = FeeStructure.objects.all()
    return render(request, "core/fee_structure_list.html", {"fees": fees})


@role_required(['super_admin', 'finance_admin'])
def add_fee_structure(request):
    categories = FeeCategory.objects.all()
    if request.method == "POST":
        FeeStructure.objects.create(
            fee_category=FeeCategory.objects.get(id=request.POST.get("fee_category")),
            class_name=request.POST.get("class_name"),
            amount=request.POST.get("amount"),
            academic_year=request.POST.get("academic_year")
        )
        return redirect('fee_structure_list')
    return render(request, "core/add_fee_structure.html", {"categories": categories})


# -------------------------------
# PDF VIEWS
# -------------------------------
@role_required(['super_admin', 'academic_admin'])
def student_pdf(request):
    students = Student.objects.all()
    return render_to_pdf("core/student_pdf.html", {"students": students})


@role_required(['super_admin', 'staff_admin'])
def staff_pdf(request):
    staff_members = Staff.objects.all()
    return render_to_pdf("core/staff_pdf.html", {"staff_members": staff_members})

@role_required(['super_admin'])
def admin_dashboard(request):
    return render(request, 'core/dashboard_admin.html')


@role_required(['finance_admin'])
def finance_dashboard(request):
    return render(request, 'core/dashboard_finance.html')


@role_required(['academic_admin'])
def academic_dashboard(request):
    return render(request, 'core/dashboard_academic.html')


@role_required(['staff_admin'])
def staff_dashboard(request):
    return render(request, 'core/dashboard_staff.html')


