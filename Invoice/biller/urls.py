from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='Homepage'),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('addproduct/',views.addproduct,name="Add Product"),
    path('deleteproduct/',views.deleteproduct,name="Delete Product"),
    
    # Add more URL patterns as needed
]
