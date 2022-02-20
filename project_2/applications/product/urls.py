from django.urls import path
from applications.product.views import ProductListView


urlpatterns = [
    path('product/', ProductListView.as_view()),
]
