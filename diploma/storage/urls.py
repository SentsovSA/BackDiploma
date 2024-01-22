from rest_framework import routers
from .api import (
    SellerViewSet,
    CarViewSet,
    UserViewSet,
    PurchaseRequestViewSet,
    CarImageViewSet,
    SellerReviewViewSet,
    PartViewSet,
    PartImageViewSet
)


router = routers.DefaultRouter()

router.register('SellerViewSet', SellerViewSet)
router.register('CarViewSet', CarViewSet)
router.register('UserViewSet', UserViewSet)
router.register('PurchaseRequestViewSet', PurchaseRequestViewSet)
router.register('CarImageViewSet', CarImageViewSet)
router.register('SellerReviewViewSet', SellerReviewViewSet)
router.register('PartViewSet', PartViewSet)
router.register('PartImageViewSet', PartImageViewSet)

urlpatterns = []

urlpatterns += router.urls



