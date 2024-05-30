from django.urls import path
from product.views import *




urlpatterns = [
    path('create', create_product, name='create_product'),
    path('update/<int:id>', update_product, name='update_product'),
    path('detail/<int:id>', detail_product, name='detail_product'),
    path('delete/<int:id>', delete_product, name='delete_product'),
]