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
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView
from proj.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls), ]

urlpatterns += [
    path('', RedirectView.as_view(url='y_bookside/',
                                  permanent=True)),
    path('y_bookside/', include('y_bookside.urls',
                                namespace='y_bookside')),
    path('reference/', include('reference.urls',
                               namespace='reference')),
    path('registration/', include('user_app.urls',
                                  namespace='user_app')),
    path('orders/', include('order.urls',
                            namespace='order')),
    path('search/', include('search.urls',
                            namespace='search')),
    path('book/', include('book.urls',
                          namespace='book')), ]


if DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
