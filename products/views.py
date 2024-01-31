# views.py
from django.shortcuts import render
from django.views import View
from rest_framework import generics
from products.models import ItemMaster
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from .load_excel import load_data

class IndexView(View):
    def get(self, request):
        return render(request, 'products/index.html')

class CategoryListView(generics.ListAPIView):
    queryset = ItemMaster.objects.values('CATEGORY').distinct()
    serializer_class = CategorySerializer

class BrandListView(generics.ListAPIView):
    queryset = ItemMaster.objects.values('BRAND').distinct()
    serializer_class = BrandSerializer

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        brand = self.request.query_params.get('brand', None)
        search_query = self.request.query_params.get('search', None)

        queryset =ItemMaster.objects.all()

        if category:
            queryset = queryset.filter(CATEGORY=category)
        if brand:
            queryset = queryset.filter(BRAND=brand)
        if search_query:
            queryset = queryset.filter(ITEM_NAME__icontains=search_query)

        return queryset[:25] if not (category or brand) else queryset.order_by('?')[:25]


