from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProductDetail
from .serializers import ProductDetailSerializer

@api_view(['GET'])
def get_product_list(request):
    query_set = ProductDetail.objects.all()
    serializer = ProductDetailSerializer(query_set, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product_detail(request, product_id):
    single_product = ProductDetail.objects.get(id=product_id)
    serializer = ProductDetailSerializer(single_product)
    return Response(serializer.data)

@api_view(['POST'])
def create_product(request):
    newItem = ProductDetail.objects.create(
        name=request.data["name"],
        description=request.data["description"]
    )
    serializer = ProductDetailSerializer(instance=newItem)
    return Response(serializer.data, status=201) 
