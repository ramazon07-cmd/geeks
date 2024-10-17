from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('teachers/', teachers, name="teachers"),
    path('courses/', all_courses, name="all_courses"),
    path('create/', CourseCreateView.as_view(), name="create"),
    path('update/<int:pk>/', CourseUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', CourseDeleteView.as_view(), name='delete'),
    path('teacher/<int:id>/', teacher_detail, name='teacher_detail'),
    path('<int:id>/', detail, name='detail'),
    path('search/', search, name='search'),
    path('course/<int:id>/lesson/<int:lesson_id>/videos/<slug:slug>/', lesson_detail, name='lesson_detail'),
    path('categories/<int:id>/', courses, name='courses'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
