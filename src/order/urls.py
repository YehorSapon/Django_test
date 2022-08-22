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

from django.urls import path
from order import views
app_name = 'order'


urlpatterns = [
    path('add-in-cart/',
         views.AddToCart.as_view(), name='add-in-cart'),
    path('delele-from-cart/<int:pk>',
         views.DeleteFromCart.as_view(), name='delele-from-cart'),
    path('update-cart/',
         views.UpdateCart.as_view(), name='update-cart'),
    path('order/<int:pk>',
         views.UpdateCart.as_view(), name='order'),
    path('order/edit/<int:pk>/',
         views.UpdateCart.as_view(), name='order-edit'),
    path('order/del/<int:pk>/',
         views.UpdateCart.as_view(), name='order-del'),
]
