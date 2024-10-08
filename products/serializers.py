from rest_framework import serializers
from .models import Product


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ArticleDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


