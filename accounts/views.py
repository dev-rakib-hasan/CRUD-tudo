from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

# Create your views here.
@api_view(['POST'])
def add(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'product added successfully.', 'data':serializer.data} status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#get single product
@api_view(['GET'])
def get(request, pk):
    product

#get all product
@api_view(['GET'])
def get_product(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)