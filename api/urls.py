from django.urls import path

from api.views import ProductModelViewSet

app_name = "api"

urlpatterns = [
    path("product-list/", ProductModelViewSet.as_view(), name="product_list"),
]
