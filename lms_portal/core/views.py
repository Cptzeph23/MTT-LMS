from django.shortcuts import render

def login_view(request):
    return render(request, "core/login.html")

def student_dashboard(request):
    return render(request, "core/student_dashboard.html")

def courses(request):
    return render(request, "core/courses.html")

def course_details(request):
    return render(request, "core/course_details.html")

def teacher_dashboard(request):
    return render(request, "core/teacher_dashboard.html")

def admin_dashboard(request):
    return render(request, "core/admin_dashboard.html")

from django.shortcuts import redirect

def login_role(request, role):
    request.session['role'] = role

    if role == "student":
        return redirect('student_dashboard')
    elif role == "teacher":
        return redirect('teacher_dashboard')
    elif role == "admin":
        return redirect('admin_dashboard')

def role_required(allowed_roles):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            role = request.session.get('role')
            if role not in allowed_roles:
                return redirect('login')
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

@role_required(['student'])
def student_dashboard(request):
    return render(request, "core/student_dashboard.html")

@role_required(['student'])
def courses(request):
    return render(request, "core/courses.html")

@role_required(['teacher'])
def teacher_dashboard(request):
    return render(request, "core/teacher_dashboard.html")

@role_required(['admin'])
def admin_dashboard(request):
    return render(request, "core/admin_dashboard.html")

def logout_view(request):
    request.session.flush()
    return redirect('login')




