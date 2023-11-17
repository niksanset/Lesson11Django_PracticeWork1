from django.urls import path 
from .views import *


urlpatterns = [
    path('', info_students_view, name= 'info_students'),
    path('student/<slug:student_slug>/',info_student_and_change_view, name='data_change'),
    path('add_student/',add_student_view , name='add_student'),
]
