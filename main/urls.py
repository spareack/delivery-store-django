from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page),
    path('category/<int:category_id>', views.show_category),
    path('meal/<int:food_id>', views.show_meal),
    path('sales', views.open_sales),
]


