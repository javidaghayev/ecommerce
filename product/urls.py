from django.urls import path
from product.views import create_product




urlpatterns = [
    path('create', create_product, name='create_product')

]