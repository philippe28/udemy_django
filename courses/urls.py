from django.conf.urls import url
from courses import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),
]
