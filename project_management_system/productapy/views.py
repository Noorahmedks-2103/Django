from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
def build_response(message,status_code,data=None,errors=None):
    response_data={
        'status_code':status_code,
        'message':message
    }
    if data is not None:
        response_data['data']=data
    if errors is not None:
        response_data['errors']=errors
    return Response(data=response_data,status=status_code)
class ProductsListView(APIView):
    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(instance=products,many=True)
        return build_response("All Products Fetched successfully",status_code=200,data=serializer.data)
    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()#create
            return build_response('Product created SuccessFully',status_code=201,data=serializer.data)
        else:
            return build_response('Validation Failed',status_code=status.HTTP_400_BAD_REQUEST,errors=serializer.errors)
class ProductDetailsView(APIView):
    def get(self,request,product_id):
        product=get_object_or_404(Product,pk=product_id)
        serializer=ProductSerializer(instance=product)
        return build_response("product Found successfully",status_code=status.HTTP_200_OK,data=serializer.data)
    def put(self,request,product_id):
        product=get_object_or_404(Product,pk=product_id)
        serializer=ProductSerializer(data=request.data,instance=product)
        if serializer.is_valid():
            serializer.save()#update()
            return build_response("product replaced successfully",status_code=status.HTTP_200_OK,data=serializer.data)
        else:
            return build_response("Validation Failed",status_code=status.HTTP_400_BAD_REQUEST,errors=serializer.errors)
    def patch(self,request,product_id):
        product=get_object_or_404(Product,pk=product_id)
        serializer=ProductSerializer(data=request.data,instance=product,partial=True)
        if serializer.is_valid():
            serializer.save()
            return build_response("Product updated successfully",status_code=status.HTTP_200_OK,data=serializer.data)
        else:
            return build_response("Validation Failed",status_code=status.HTTP_400_BAD_REQUEST,errors=serializer.errors)
    def delete(self,request,product_id):
        product=get_object_or_404(Product,pk=product_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)