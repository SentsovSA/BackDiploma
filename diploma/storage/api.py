from .models import (
    Seller,
    Car,
    User,
    PurchaseRequest,
    CarImage,
    SellerReview,
)
from rest_framework import viewsets, permissions

from .serializers import (
    SellerSerializer,
    CarSerializer,
    UserSerializer,
    PurchaseRequestSerializer,
    CarImageSerializer,
    SellerReviewSerializer,
)


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SellerSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class PurchaseRequestViewSet(viewsets.ModelViewSet):
    queryset = PurchaseRequest.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PurchaseRequestSerializer


class CarImageViewSet(viewsets.ModelViewSet):
    queryset = CarImage.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarImageSerializer


class SellerReviewViewSet(viewsets.ModelViewSet):
    queryset = SellerReview.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SellerReviewSerializer
