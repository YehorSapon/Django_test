"""proj URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from . import views
from django.urls import path
from django.urls import include

app_name = 'reference'

authors_patterns = ([
    path('list/', views.AuthorList.as_view(), name='author-list'),
    path('<int:pk>/', views.AuthorView.as_view(), name='author'),
    path('del/<int:pk>/', views.AuthorDelete.as_view(), name='author-del'),
    path('add/', views.AuthorAdd.as_view(), name='author-add'),
    path('edit/<int:pk>/', views.AuthorEdit.as_view(), name='author-edit'),
])

urlpatterns = [
    path('author/', include(authors_patterns)),
]
