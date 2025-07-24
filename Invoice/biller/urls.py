from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='Homepage'),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('addproduct/',views.addproduct,name="Add Product"),
    path('deleteproduct/',views.deleteproduct,name="Delete Product"),
    path('addcustomer/',views.addcustomer,name="Add Customer"),
    path('editproduct/',views.editproduct,name="Edit Product"),
    path('searchproduct/',views.searchproduct,name="Search Product"),
    path('Login/',views.login,name="Login")    
    # Add more URL patterns as needed
]
