from rest_framework import serializers

from .models import Seller, Car, User, PurchaseRequest, CarImage, SellerReview, Part, PartImage


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PurchaseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRequest
        fields = '__all__'


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = '__all__'


class SellerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerReview
        fields = '__all__'


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'


class PartImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartImage
        fields = '__all__'
