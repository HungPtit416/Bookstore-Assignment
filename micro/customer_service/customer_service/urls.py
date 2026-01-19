from django.contrib import admin
from django.urls import path
from customers.views import register, get_customers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/register/', register),
    path('customers/', get_customers),
]
