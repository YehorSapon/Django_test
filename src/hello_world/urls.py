from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from hello_world import views


urlpatterns = [
    path("", views.hello_world_view, name="home"),
    path("<name>", views.hello_there, name="hello_there"),
    path("log/", views.log_message, name="log"),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
