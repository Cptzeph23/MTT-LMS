from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('courses/', views.courses, name='courses'),
    path('course/', views.course_details, name='course_details'),
    path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('login/<str:role>/', views.login_role, name='login_role'),
    path('logout/', views.logout_view, name='logout'),


]
