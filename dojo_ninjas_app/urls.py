from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add_dojo', views.add_dojo),
    path('add_ninja', views.add_ninja),
    path('delete_dojo/<int:dojo_id>/delete', views.delete_dojo)
]
