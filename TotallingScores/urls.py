from django.contrib import admin
from django.urls import path
from totalingapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name='home'),
path('grades/', views.grade_list, name='grade_list'),
    path('grades/create/', views.grade_create, name='grade_create'),
    path('create/', views.student_create, name='student_create'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/',views.user_create,name='create_user'),
    path('subject/',views.subject_create,name='subject_create'),
    path('score/',views.input_view,name='input'),
]
