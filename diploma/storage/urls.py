from rest_framework import routers
from .api import (
    SellerViewSet,
    CarViewSet,
    UserViewSet,
    PurchaseRequestViewSet,
    CarImageViewSet,
    SellerReviewViewSet,
)


router = routers.DefaultRouter()

router.register('SellerViewSet', SellerViewSet)
router.register('CarViewSet', CarViewSet)
router.register('UserViewSet', UserViewSet)
router.register('PurchaseRequestViewSet', PurchaseRequestViewSet)
router.register('CarImageViewSet', CarImageViewSet)
router.register('SellerReviewViewSet', SellerReviewViewSet)

urlpatterns = []

urlpatterns += router.urls



