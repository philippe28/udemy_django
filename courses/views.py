from django.shortcuts import render, get_object_or_404

from .models import Courses
from .forms import ContactCourse

def index(request):
    courses = Courses.objects.all()
    template_name = 'courses/index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)


def details(request, slug):
    courses = get_object_or_404(Courses, slug=slug)
    context = {}
    if request.method == 'POST':
        forms = ContactCourse(request.POST)
        if forms.is_valid():
            context['is_valid'] = True
            forms.send_mail(courses)
            #print(forms.cleaned_data)
            forms = ContactCourse()
    else:
        forms = ContactCourse()
    context['forms'] = forms
    context['courses'] = courses
    template_name = 'courses/details.html'
    return render(request, template_name, context)
