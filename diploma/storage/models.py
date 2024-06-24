from django.db import models
from django.utils.html import mark_safe


class Seller(models.Model):
    sellerID = models.AutoField(primary_key=True, auto_created=True)
    sellerName = models.CharField(max_length=256)
    sellerEmail = models.CharField(max_length=256)
    sellerPhone = models.CharField(max_length=256)

    def __str__(self):
        return self.sellerName


class CarImage(models.Model):
    fileName = models.CharField(max_length=256, null=True)
    imageID = models.AutoField(primary_key=True, auto_created=True)
    file = models.FileField(upload_to='storage/car_image/', null=True)
    imageURL = models.CharField(max_length=256, null=True)

    @property
    def media_preview(self):
        if self.file and self.file.name.endswith(('.png', '.jpeg', '.jpg', '.img')):
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.file.url))
        return ""

    def __str__(self):
        return self.fileName


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

    sellerID = models.ManyToManyField(Seller, related_name='seller')
    imageID = models.ManyToManyField(CarImage, related_name='image')

    def __str__(self):
        return self.vin


class User(models.Model):
    userID = models.AutoField(primary_key=True, auto_created=True)
    userName = models.CharField(max_length=256)
    userEmail = models.CharField(max_length=256)
    userPhone = models.CharField(max_length=256)

    def __str__(self):
        return self.userName


class PurchaseRequest(models.Model):
    requestID = models.AutoField(primary_key=True, auto_created=True)
    requestDate = models.DateField()
    status = models.CharField(max_length=256)

    carID = models.OneToOneField(Car, related_name='carIDsPurchase', null=True, on_delete=models.SET_NULL)
    userID = models.ManyToManyField(User, related_name='userIDsPurchase')

    def __str__(self):
        return self.status


class SellerReview(models.Model):
    reviewName = models.CharField(max_length=256, null=True)
    reviewID = models.AutoField(primary_key=True, auto_created=True)
    rating = models.IntegerField()
    comment = models.CharField(max_length=256)

    sellerID = models.OneToOneField(Seller, related_name='sellerReview', null=True, on_delete=models.SET_NULL)
    userID = models.OneToOneField(User, related_name='userIDsReview', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.reviewName


class PartImage(models.Model):
    fileName = models.CharField(max_length=256, null=True)
    imageID = models.AutoField(primary_key=True, auto_created=True)
    file = models.FileField(upload_to='storage/part_image/', null=True)
    imageURL = models.CharField(max_length=256, null=True)

    @property
    def media_preview(self):
        if self.file and self.file.name.endswith(('.png', '.jpeg', '.jpg', '.img')):
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.file.url))
        return ""

    def __str__(self):
        return self.fileName


class Part(models.Model):
    partID = models.AutoField(primary_key=True, auto_created=True)
    partName = models.CharField(max_length=256)
    partPrice = models.IntegerField()
    condition = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    stock = models.IntegerField()

    sellerID = models.ManyToManyField(Seller, related_name='partSeller')
    partImageID = models.ManyToManyField(PartImage, related_name='partImageID')
