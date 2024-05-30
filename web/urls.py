from django.urls import path
from web import views


urlpatterns = [
    path('', views.home, name='home'),
    path('calc/', views.calc_view, name='calc'),
]

