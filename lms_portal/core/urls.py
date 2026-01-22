from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [


    path('admin/', admin.site.urls),
    # AUTH
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # DASHBOARDS
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/finance/', views.finance_dashboard, name='finance_dashboard'),
    path('dashboard/academic/', views.academic_dashboard, name='academic_dashboard'),
    path('dashboard/staff/', views.staff_dashboard, name='staff_dashboard'),

    # STUDENTS
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/pdf/', views.student_pdf, name='student_pdf'),

    # STAFF
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/add/', views.add_staff, name='add_staff'),
    path('staff/pdf/', views.staff_pdf, name='staff_pdf'),

    # FEES
    path('fees/', views.fee_structure_list, name='fee_structure_list'),
    path('fees/add/', views.add_fee_structure, name='add_fee_structure'),

        # PASSWORD RESET
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
