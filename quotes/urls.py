from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="inicio"),
    path('nosotros.html', views.nosotros, name="nosotros"),
    path('add_stock.html', views.add_stock, name="add_stock"),
    path('borrar/<stock_id>', views.delete, name="delete"),
    path('delete_stock.html', views.delete_stock, name="delete_stock"),
]