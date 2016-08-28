from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.conf import settings
from .forms import RegisterForm

# Create your views here.


def register(request):

    template_name = 'register.html'
    if request.method == 'POST':

        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():

            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = RegisterForm()
    context = {
        'form': RegisterForm()
    }
    return render(request, template_name, context)
