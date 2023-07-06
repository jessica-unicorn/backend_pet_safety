from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProductDetail
from .serializers import ProductDetailSerializer

@api_view(['GET'])
def product_list(request):
    query_set = ProductDetail.objects.all()
    serializer = ProductDetailSerializer(query_set, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, product_id):
    single_product = ProductDetail.objects.get(id=product_id)
    serializer = ProductDetailSerializer(single_product)
    return Response(serializer.data)
