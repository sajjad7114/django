from django.conf.urls import url
from .views import show_program, create, edit, delete

urlpatterns = [
    url(r'^$', show_program),
    url(r'^create/', create),
    url(r'^edit/(?P<event_title>[\w-]+)/', edit),
    url(r'^delete/(?P<event_title>[\w-]+)/', delete),
]