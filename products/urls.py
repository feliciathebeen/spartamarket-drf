from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.ArticleListAPIView.as_view(), name="product_list"),
    path("<int:pk>/", views.ArticleDetailAPIView.as_view(), name="product_detail"),
]
