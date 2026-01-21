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

