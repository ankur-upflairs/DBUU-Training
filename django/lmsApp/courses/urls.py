from django.urls import path
from .views import *

urlpatterns = [
   path("",all_courses,name='courses'),
   path('manage-courses',manage_courses),
   path('edit/<int:id>',edit_course),
   path('create-course',create_course),
   path("<int:id>",single_course_by_id,name='course-details'),
]


