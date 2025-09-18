from django.urls import path
from .views import *

urlpatterns = [
   path("",all_courses,name='courses'),
   path("<int:id>",single_course_by_id,name='course-details')
]


