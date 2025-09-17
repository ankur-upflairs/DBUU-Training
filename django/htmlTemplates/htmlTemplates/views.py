from django.shortcuts import render
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
    return render(request,'courses.html',{
        "title":"All Courses - EduPlatform",
        "courses":courses
    })
