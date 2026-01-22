from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .models import Student, Staff, FeeCategory, FeeStructure
from reportlab.pdfgen import canvas
from io import BytesIO

# ======================================================
# ROLE DECORATOR
# ======================================================
def role_required(allowed_roles):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')

            role = request.user.profile.role

            if role not in allowed_roles:
                return redirect('login')

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


# ======================================================
# AUTH
# ======================================================
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


def user_logout(request):
    logout(request)
    return redirect('login')


# ======================================================
# DASHBOARDS
# ======================================================
@role_required(['super_admin'])
def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')


@role_required(['finance_admin'])
def finance_dashboard(request):
    return render(request, 'core/finance_dashboard.html')


@role_required(['academic_admin'])
def academic_dashboard(request):
    return render(request, 'core/academic_dashboard.html')


@role_required(['staff_admin'])
def staff_dashboard(request):
    return render(request, 'core/staff_dashboard.html')


# ======================================================
# STUDENTS
# ======================================================
@role_required(['super_admin', 'academic_admin'])
def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})


@role_required(['super_admin', 'academic_admin'])
def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            admission_number=request.POST['admission_number'],
            full_name=request.POST['full_name'],
            class_name=request.POST['class_name'],
            academic_year=request.POST['academic_year']
        )
        return redirect('student_list')
    return render(request, 'core/add_student.html')


@role_required(['super_admin', 'academic_admin'])
def student_pdf(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    y = 800

    for student in Student.objects.all():
        p.drawString(40, y, f"{student.admission_number} - {student.full_name}")
        y -= 20

    p.showPage()
    p.save()
    buffer.seek(0)

    return HttpResponse(buffer, content_type='application/pdf')


# ======================================================
# STAFF
# ======================================================
@role_required(['super_admin', 'staff_admin'])
def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'core/staff_list.html', {'staff': staff})


@role_required(['super_admin', 'staff_admin'])
def add_staff(request):
    if request.method == "POST":
        Staff.objects.create(
            staff_number=request.POST['staff_number'],
            full_name=request.POST['full_name'],
            role=request.POST['role'],
            department=request.POST['department'],
            phone=request.POST['phone']
        )
        return redirect('staff_list')
    return render(request, 'core/add_staff.html')


@role_required(['super_admin', 'staff_admin'])
def staff_pdf(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    y = 800

    for staff in Staff.objects.all():
        p.drawString(40, y, f"{staff.staff_number} - {staff.full_name}")
        y -= 20

    p.showPage()
    p.save()
    buffer.seek(0)

    return HttpResponse(buffer, content_type='application/pdf')


# ======================================================
# FEES
# ======================================================
@role_required(['super_admin', 'finance_admin'])
def fee_structure_list(request):
    fees = FeeStructure.objects.all()
    return render(request, 'core/fee_structure_list.html', {'fees': fees})


@role_required(['super_admin', 'finance_admin'])
def add_fee_structure(request):
    categories = FeeCategory.objects.all()

    if request.method == "POST":
        FeeStructure.objects.create(
            fee_category_id=request.POST['fee_category'],
            class_name=request.POST['class_name'],
            academic_year=request.POST['academic_year'],
            amount=request.POST['amount']
        )
        return redirect('fee_structure_list')

    return render(request, 'core/add_fee_structure.html', {
        'categories': categories
    })
