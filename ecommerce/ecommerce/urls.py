"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from ecommapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Homeview.as_view(),name='home_view'),
    path('reg',views.RegisterView.as_view(),name='reg_view'),
    path('log',views.LoginView.as_view(),name='log_view'),
    path('logout',views.UserLogout.as_view(),name='logout_view'),
    path('productdetail/<int:id>',views.ProductDetails.as_view(),name='product_detail'),
    path('addtocart/<int:id>',views.AddToCartView.as_view(),name='add_cart'),
    path('cart/list',views.CartListView.as_view(),name='list_cart'),
    path('place/order/<int:cart_id>',views.PlaceOrderView.as_view(),name='place_order'),
    path('cart/delete/<int:id>',views.CartDelete.as_view(),name='list_delete'),




    # path('add/cart',views.AddToCartView.as_view(),name='addto_cart')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
