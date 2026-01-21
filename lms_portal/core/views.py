from django.shortcuts import render, redirect
from .utils import render_to_pdf
from .models import Student, Staff

def role_required(allowed_roles):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            role = request.session.get('role')
            if role not in allowed_roles:
                return redirect('login')
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


def login_view(request):
    return render(request, "core/login.html")

def login_role(request, role):
    request.session['role'] = role

    # All admin roles go to admin dashboard
    return redirect('admin_dashboard')


def logout_view(request):
    request.session.flush()
    return redirect('login')

@role_required(['student'])
def student_dashboard(request):
    return render(request, "core/student_dashboard.html")

@role_required(['teacher'])
def teacher_dashboard(request):
    return render(request, "core/teacher_dashboard.html")

@role_required(['super_admin', 'finance_admin', 'academic_admin', 'staff_admin'])
def admin_dashboard(request):
    return render(request, "core/admin_dashboard.html")

@role_required(['student'])
def courses(request):
    return render(request, "core/courses.html")

@role_required(['teacher'])
def teacher_courses(request):
    return render(request, "core/teacher_courses.html")

@role_required(['teacher'])
def upload_content(request):
    return render(request, "core/upload_content.html")

@role_required(['admin'])
def user_management(request):
    return render(request, "core/user_management.html")

@role_required(['admin'])
def reports(request):
    return render(request, "core/reports.html")

@role_required(['student','teacher'])
def profile(request):
    return render(request, "core/profile.html")



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
            date_of_birth=request.POST.get("date_of_birth") or None,
            class_name=request.POST.get("class_name"),
            academic_year=request.POST.get("academic_year"),
            guardian_name=request.POST.get("guardian_name"),
            guardian_phone=request.POST.get("guardian_phone"),
        )
        return redirect('student_list')

    return render(request, "core/add_student.html")

@role_required(['super_admin', 'academic_admin'])
def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, "core/student_detail.html", {"student": student})


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
    staff = Staff.objects.get(id=staff_id)
    return render(request, "core/staff_detail.html", {"staff": staff})


# Student PDF
@role_required(['super_admin', 'academic_admin'])
def student_pdf(request):
    students = Student.objects.all()
    return render_to_pdf("core/student_pdf.html", {"students": students})

# Staff PDF
@role_required(['super_admin', 'staff_admin'])
def staff_pdf(request):
    staff_members = Staff.objects.all()
    return render_to_pdf("core/staff_pdf.html", {"staff_members": staff_members})


