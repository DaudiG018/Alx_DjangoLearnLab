from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'items', InventoryItemViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls
