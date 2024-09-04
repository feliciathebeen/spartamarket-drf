from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Product


@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    serializer = ArticleSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ArticleSerializer(product)
    return Response(serializer.data)