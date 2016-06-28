from django.shortcuts import render, get_object_or_404

from .models import Courses

def index(request):
    courses = Courses.objects.all()
    template_name = 'courses/index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)

    
def details(request,slug):
    courses = get_object_or_404(Courses, slug=slug)
    context = {
        'courses': courses
    }
    template_name = 'courses/details.html'
    return render(request, template_name, context)
