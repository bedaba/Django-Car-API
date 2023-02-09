
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index),
    path('car', views.add_car),
    path('cars/', views.get_all_cars),
    path('car/<str:car_name>', views.update_car),
    path('car/<str:car_name>', views.delete_car),
]
