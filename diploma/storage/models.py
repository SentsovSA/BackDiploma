from django.db import models
from django.utils.html import mark_safe


# Seller (продавец):
# SellerID (идентификатор продавца)
# Name (имя)
# Email (электронная почта)
# Phone (телефон)

class Seller(models.Model):
    sellerID = models.AutoField(primary_key=True, auto_created=True)
    sellerName = models.CharField(max_length=256)
    sellerEmail = models.CharField(max_length=256)
    sellerPhone = models.CharField(max_length=256)

    def __str__(self):
        return self.sellerName

# Car (автомобиль):
# CarID (идентификатор автомобиля)
# Brand (марка)
# Model (модель)
# Year (год выпуска)
# Price (цена)
# Condition (состояние)
# SellerID (идентификатор продавца)


class Car(models.Model):
    carId = models.AutoField(primary_key=True, auto_created=True)
    brand = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    vin = models.CharField(max_length=17)
    year = models.CharField(max_length=256)
    price = models.IntegerField()
    condition = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    stock = models.IntegerField()

    sellerID = models.OneToOneField(Seller, related_name='seller', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.vin


# User (пользователь):
# UserID (идентификатор пользователя)
# Name (имя)
# Email (электронная почта)
# Phone (телефон)


class User(models.Model):
    userID = models.AutoField(primary_key=True, auto_created=True)
    userName = models.CharField(max_length=256)
    userEmail = models.CharField(max_length=256)
    userPhone = models.CharField(max_length=256)

    def __str__(self):
        return self.userName


# PurchaseRequest (заявка на покупку):
# RequestID (идентификатор заявки)
# CarID (идентификатор автомобиля)
# UserID (идентификатор пользователя)
# RequestDate (дата заявки)
# Status (статус заявки)


class PurchaseRequest(models.Model):
    requestID = models.AutoField(primary_key=True, auto_created=True)
    requestDate = models.DateField()
    status = models.CharField(max_length=256)

    carID = models.OneToOneField(Car, related_name='carIDsPurchase', null=True, on_delete=models.SET_NULL)
    userID = models.OneToOneField(User, related_name='userIDsPurchase', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.requestID


# CarImage (изображение автомобиля):
# ImageID (идентификатор изображения)
# CarID (идентификатор автомобиля)
# ImageURL (URL изображения)


class CarImage(models.Model):
    imageID = models.AutoField(primary_key=True, auto_created=True)
    carID = models.OneToOneField(Car, related_name='carIDs', null=True, on_delete=models.SET_NULL)
    file = models.FileField(upload_to='car_image/')
    imageURL = models.CharField(max_length=256)

    @property
    def media_preview(self):
        if self.file and self.file.name.endswith(('.png', '.jpeg', '.jpg', '.img')):
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.file.url))
        return ""

    def __str__(self):
        return self.imageID


# SellerReview (отзыв о продавце):
# ReviewID (идентификатор отзыва)
# SellerID (идентификатор продавца)
# UserID (идентификатор пользователя)
# Rating (рейтинг)
# Comment (комментарий)


class SellerReview(models.Model):
    reviewID = models.CharField(primary_key=True, auto_created=True)
    rating = models.IntegerField()
    comment = models.CharField(max_length=256)

    sellerID = models.OneToOneField(Seller, related_name='sellerReview', null=True, on_delete=models.SET_NULL)
    userID = models.OneToOneField(User, related_name='userIDsReview', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.reviewID



