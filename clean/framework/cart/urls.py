from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_to_cart),
    path('<int:customer_id>/', views.view_cart),
]