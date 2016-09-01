from django.conf.urls import url
from core import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact/', views.contact, name='contact'),
]
