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
        return Response({'message':'product added successfully.', 'data':serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#get all product
@api_view(['GET'])
def get_all(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



#get single product
@api_view(['GET'])
def get(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


# update product 
@api_view(['PATCH'])
def update(request, id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Deleted Product
@api_view(['DELETE'])
def delete(request, pk):
    product = Product.objects.get(pk=pk)
    
    product.delete()
    
    return Response({'message':'Deleted Successfully.'}, status=status.HTTP_204_NO_CONTENT)