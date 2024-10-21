from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import InventoryChangeLog, InventoryItem, Category
from .serializers import InventoryItemSerializer, CategorySerializer

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Allow users to view only their inventory items
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the user as the creator of the item
        serializer.save(user=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

from rest_framework import filters

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category__name', 'price', 'quantity']
    
    def get_queryset(self):
        queryset = InventoryItem.objects.filter(user=self.request.user)
        category = self.request.query_params.get('category', None)
        low_stock = self.request.query_params.get('low_stock', None)

        if category:
            queryset = queryset.filter(category__name=category)
        if low_stock:
            queryset = queryset.filter(quantity__lte=low_stock)
        
        return queryset

from rest_framework.response import Response

class InventoryChangeLogViewSet(viewsets.ModelViewSet):
    queryset = InventoryChangeLog.objects.all()

    def list(self, request, item_id=None):
        logs = self.queryset.filter(item__id=item_id)
        return Response(InventoryChangeLog(logs, many=True).data)
