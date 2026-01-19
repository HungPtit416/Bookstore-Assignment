from django.contrib import admin
from django.urls import path
from cart.views import create_cart, add_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/create/', create_cart),
    path('cart/add/', add_item),
]
