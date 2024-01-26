from django.urls import path
from . import views

urlpatterns = [
    path('', views.listView, name='home' ),
    path("create", views.createView, name='create'),
    path('delete/<str:pk>', views.deleteView, name='delete')
]