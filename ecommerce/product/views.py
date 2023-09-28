from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework import status

from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def search(request):
    query = request.data.get('query', '')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'products': []})

    

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    

class ProductDetailView(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except:
            raise Http404
        
    def get(self, request, category_slug, product_slug):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
class CategoryListView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    
class CategoryDetailView(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)



