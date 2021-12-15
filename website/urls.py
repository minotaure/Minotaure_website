from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page, name='index'),
    path('team/', views.team, name="team"),
    path('contact/', views.contact, name="contact"),
]
