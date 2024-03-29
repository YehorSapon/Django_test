"""proj URL Configuration
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

from django.urls import path, include
from book import views
app_name = 'book'


books_patterns = ([
    path('list/', views.BookList.as_view(), name='book-list'),
    path('<int:pk>/', views.BookView.as_view(), name='book'),
    path('del/<int:pk>/', views.BookDelete.as_view(), name='book-del'),
    path('add/', views.BookAdd.as_view(), name='book-add'),
    path('edit/<int:pk>/', views.BookEdit.as_view(), name='book-edit'),
])

urlpatterns = [
    path('books/', include(books_patterns)),
]
