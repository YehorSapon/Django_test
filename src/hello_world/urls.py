from django.urls import path
from hello_world import views


urlpatterns = [
    path("", views.hello_world_view, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    ]
