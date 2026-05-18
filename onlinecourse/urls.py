from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # Rutas originales del proyecto base
    path(route='', view=views.CourseListView.as_view(), name='popular_course_list'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    
    # Rutas del sistema de exámenes (Task 5 y Task 6)
    path('<int:course_id>/submit/', views.submit, name='submit'),
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='exam_result'),
]