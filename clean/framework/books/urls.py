from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books),
    path('<int:book_id>/', views.get_book),
]