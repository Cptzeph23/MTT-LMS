from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/<str:role>/', views.login_role, name='login_role'),
    path('logout/', views.logout_view, name='logout'),

    path('student/', views.student_dashboard, name='student_dashboard'),
    path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('courses/', views.courses, name='courses'),
    path('teacher/courses/', views.teacher_courses, name='teacher_courses'),
    path('upload/', views.upload_content, name='upload_content'),

    path('admin/users/', views.user_management, name='user_management'),
    path('admin/reports/', views.reports, name='reports'),

    path('profile/', views.profile, name='profile'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),

    path('staff/', views.staff_list, name='staff_list'),
    path('staff/add/', views.add_staff, name='add_staff'),
    path('staff/<int:staff_id>/', views.staff_detail, name='staff_detail'),

    path('students/pdf/', views.student_pdf, name='student_pdf'),
    path('staff/pdf/', views.staff_pdf, name='staff_pdf'),

    # Fee Categories
    path('fees/categories/', views.fee_category_list, name='fee_category_list'),
    path('fees/categories/add/', views.add_fee_category, name='add_fee_category'),

    # Fee Structures
    path('fees/structure/', views.fee_structure_list, name='fee_structure_list'),
    path('fees/structure/add/', views.add_fee_structure, name='add_fee_structure'),


        # Password reset
    path('password-reset/',
     auth_views.PasswordResetView.as_view(template_name='core/password_reset.html'),
     name='password_reset'),
    path('password-reset/done/',
     auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'),
     name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name='core/password_reset_confirm.html'),
     name='password_reset_confirm'),
    path('password-reset-complete/',
     auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'),
     name='password_reset_complete'),


]
