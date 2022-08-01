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

publhs_patterns = ([
    path('list/', views.PublhList.as_view(), name='publh-list'),
    path('<int:pk>/', views.PublhView.as_view(), name='publh'),
    path('del/<int:pk>/', views.PublhDelete.as_view(), name='publh-del'),
    path('add/', views.PublhAdd.as_view(), name='publh-add'),
    path('edit/<int:pk>/', views.PublhEdit.as_view(), name='publh-edit'),
])

series_patterns = ([
    path('list/', views.SeriesList.as_view(), name='series-list'),
    path('<int:pk>/', views.SeriesView.as_view(), name='series'),
    path('del/<int:pk>/', views.SeriesDelete.as_view(), name='series-del'),
    path('add/', views.SeriesAdd.as_view(), name='series-add'),
    path('edit/<int:pk>/', views.SeriesEdit.as_view(), name='series-edit'),
])

genres_patterns = ([
    path('list/', views.GenreList.as_view(), name='genre-list'),
    path('<int:pk>/', views.GenreView.as_view(), name='genre'),
    path('del/<int:pk>/', views.GenreDelete.as_view(), name='genre-del'),
    path('add/', views.GenreAdd.as_view(), name='genre-add'),
    path('edit/<int:pk>/', views.GenreEdit.as_view(), name='genre-edit'),
])

urlpatterns = [
    path('author/', include(authors_patterns)),
    path('publh/', include(publhs_patterns)),
    path('series/', include(series_patterns)),
    path('genre/', include(genres_patterns)),
]
