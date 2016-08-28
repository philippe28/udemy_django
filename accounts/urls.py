from django.conf.urls import url, include
from accounts import views


urlpatterns = [
    url(r'^entrar/', include('django.contrib.auth.urls'),
        {'template_name': 'login.html'}, name='login'),

    url(r'^cadastre-se/', views.register,
        name='register'),
]
