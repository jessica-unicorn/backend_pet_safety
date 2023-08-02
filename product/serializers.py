from rest_framework import serializers
from .models import ProductDetail

class ProductDetailSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(max_length=255)
	description = serializers.CharField()
	image_name = serializers.CharField(max_length=255, required=False)

	class Meta:
		model = ProductDetail
		fields = ['id', 'name', 'description', 'image_name']