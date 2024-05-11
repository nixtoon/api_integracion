from django.urls import path
from . import views

urlpatterns = [
  path('get-marcas', views.get_marcas),
  path('create-marca', views.create_marcas),
  path('get-marca/<str:pk>', views.get_marca),
  path('update-marca/<str:pk>', views.update_marca),
  path('delete-marca/<str:pk>', views.delete_marca),
  path('', views.get_productos),
  path('create-producto', views.create_producto),
  path('get-producto/<str:pk>', views.get_producto),
  path('update-producto/<str:pk>', views.update_producto),
  path('delete-producto/<str:pk>', views.delete_producto)
]