from django.http import HttpResponse

courses=[
    {
        "id":1,
        "title":"HTML",
        "description":
            "hyper text markup language"
    },
    {
        "id":2,
        "title":"CSS",
        "description":"casecading style sheet"
    }   
]
def all_courses(request):
    courseHtml=''
    for course in courses:
        courseHtml+=f"""<li> <h3>
                    Title = {course['title']}</h3>
                    <p>{course['description']} </p>
                    </li><hr>                    
                    """
    return HttpResponse(courseHtml)

def single_course_by_title(request,title):
    select_course=None
    print(title)
    for course in courses:
        if course["title"] == title:
            select_course=course
            break
    if select_course is None:
        return HttpResponse('course not found')
    else:
        course_html=f"""<h3>{select_course['title']}</h3>
                    <p>{select_course['description']}</p>"""
        return HttpResponse(course_html)
def single_course_by_id(request,id):
    select_course=None
    for course in courses:
        if course["id"] == id:
            select_course=course
            break
    if select_course is None:
        return HttpResponse('course not found')
    else:
        course_html=f"""<h3>{select_course['title']}</h3>
                    <p>{select_course['description']}</p>"""
        return HttpResponse(course_html)

def home(request):
    return HttpResponse('This is Home page')

def about(request):
    return HttpResponse('This is About page')
def contact(request):
    return HttpResponse('This is Contact page')
