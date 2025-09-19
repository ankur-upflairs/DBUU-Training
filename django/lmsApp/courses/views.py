from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Courses

courses = [
    {
        "id": 1,
        "title": "JavaScript Fundamentals",
        "description": "Learn the basics of JavaScript programming, including variables, functions, and DOM manipulation. Perfect for beginners starting their web development journey.",
        "instructor": "John Smith",
        "duration": 40,
        "createdAt": "2024-01-15",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png"
    },
    {
        "id": 2,
        "title": "React Development",
        "description": "Master React.js and build modern web applications with components, hooks, and state management. Create dynamic and interactive user interfaces.",
        "instructor": "Sarah Johnson",
        "duration": 60,
        "createdAt": "2024-02-10",
        "image": "https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg"
    },
    {
        "id": 3,
        "title": "Python Data Science",
        "description": "Dive into data science with Python, pandas, numpy, and machine learning fundamentals. Analyze data and build predictive models.",
        "instructor": "Mike Chen",
        "duration": 80,
        "createdAt": "2024-01-20",
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"
    },
    {
        "id": 4,
        "title": "Web Design Essentials",
        "description": "Learn HTML, CSS, and responsive design principles to create beautiful and functional websites. Master modern design techniques.",
        "instructor": "Emily Rodriguez",
        "duration": 35,
        "createdAt": "2024-03-05",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/61/HTML5_logo_and_wordmark.svg"
    }
]

def all_courses(request):
    allCourses=Courses.objects.all()
    
    return render(request,'courses.html',{
        "title":"All Courses - EduPlatform",
        "courses":allCourses
    })

def single_course_by_id(request,id):
    selected_course=None
    for course in courses:
        if course['id'] == id:
            selected_course=course
    if selected_course is None :
        return HttpResponseNotFound('Course not found')
    else:
        return render(request,'course-detail.html',{
            "title":selected_course['title'],
            "course":selected_course
        })

def create_course(request):
    # print(request.method)
    if request.method=='GET':
        return render(request,'add-course.html')
    else:
        # print(request.POST)
        title=request.POST.get('title')
        duration=request.POST.get('duration')
        instructor=request.POST.get('instructor')
        description=request.POST.get('description')
        image=request.POST.get('image')   
        # print(title)
        course=Courses(title=title,duration=duration,instructor=instructor,description=description,image=image)
        course.save()
        return render(request,'thank-you.html')
    
def manage_courses(request):
    courses= Courses.objects.all()
    return render(request,'manage-courses.html',{"courses":courses})