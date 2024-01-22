from django.contrib import admin

from .models import Seller, Car, User, PurchaseRequest, CarImage, SellerReview, Part, PartImage


class SellerAdmin(admin.ModelAdmin):
    list_display = ('sellerID', 'sellerName', 'sellerEmail', 'sellerPhone',)
    list_display_links = ('sellerID', 'sellerName',)
    search_fields = ('sellerID', 'sellerName',)


admin.site.register(Seller, SellerAdmin)


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'vin', 'year', 'price', 'condition', 'description', 'stock',)
    list_display_links = ('brand', 'vin',)
    search_fields = ('brand', 'model', 'vin', 'year', 'stock',)
    list_editable = ('stock',)
    list_filter = ('stock',)


admin.site.register(Car, CarAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('userID', 'userName', 'userEmail', 'userPhone',)
    list_display_links = ('userID', 'userName',)
    search_fields = ('userID', 'userName', 'userEmail',)


admin.site.register(User, UserAdmin)


class PurchaseRequestAdmin(admin.ModelAdmin):
    list_display = ('requestID', 'requestDate', 'status',)
    list_display_links = ('requestID',)
    search_fields = ('requestID',)


admin.site.register(PurchaseRequest, PurchaseRequestAdmin)


class CarImageAdmin(admin.ModelAdmin):
    list_display = ('imageID', 'file', 'imageURL',)
    list_display_links = ('imageID',)
    search_fields = ('imageID',)


admin.site.register(CarImage, CarImageAdmin)


class SellerReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewID', 'rating', 'comment',)
    list_display_links = ('reviewID',)
    search_fields = ('reviewID',)


admin.site.register(SellerReview, SellerReviewAdmin)


class PartImageAdmin(admin.ModelAdmin):
    list_display = ('fileName', 'imageID', 'file', 'imageURL',)
    list_display_links = ('imageID',)
    search_fields = ('imageID',)


admin.site.register(PartImage, PartImageAdmin)


class PartAdmin(admin.ModelAdmin):
    list_display = ('partID', 'partName', 'partPrice', 'condition', 'description', 'stock',)
    list_display_links = ('partID', 'partName',)
    search_fields = ('partID', 'partName',)


admin.site.register(Part, PartAdmin)
