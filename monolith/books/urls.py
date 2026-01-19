from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
]