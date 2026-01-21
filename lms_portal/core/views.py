from django.shortcuts import render, redirect

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
    return redirect(f"{role}_dashboard")

def logout_view(request):
    request.session.flush()
    return redirect('login')

@role_required(['student'])
def student_dashboard(request):
    return render(request, "core/student_dashboard.html")

@role_required(['teacher'])
def teacher_dashboard(request):
    return render(request, "core/teacher_dashboard.html")

@role_required(['admin'])
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
