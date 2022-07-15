from django.contrib import admin
from inventoryApp.models import registerModel,productModel,purchaseModel,customerModel,stockModel,sellModel,returnPurchaseModel,returnSellModel
# Register your models here.

class registerAdmin(admin.ModelAdmin):
    list_display = ['id','firstname','lastName','email','gender','password']

class productAdmin(admin.ModelAdmin):
    list_display = ['id','profileName','productName','productDescription']

class purchaseAdmin(admin.ModelAdmin):
    list_display = ['id','productId','customerId','purchaseDate','invoice','rate','quantity','discount','CGST','IGST','taxableAmount','totalAmount']

class customerAdmin(admin.ModelAdmin):
    list_display = ['id','profileName','customerName','address','mobileNumber','GSTno']

class stockAdmin(admin.ModelAdmin):
    list_display = ['id','purchaseId','date','quantity']

class sellAdmin(admin.ModelAdmin):
    list_display = ['id','stockId','customerId','sellDate','invoice','rate','quantity','discount','CGST','IGST','taxableAmount','totalAmount']

class returnPurchaseAdmin(admin.ModelAdmin):
    list_display = ['id','purchaseReturnId','custNameId','purchaseReturnDate','returnQuantity']

class returnSellAdmin(admin.ModelAdmin):
    list_display = ['id','sellReturnProductId','sellReturnSellId','sellReturnDate','sellReturnQuantity']

admin.site.register(registerModel,registerAdmin)
admin.site.register(productModel,productAdmin)
admin.site.register(purchaseModel,purchaseAdmin)
admin.site.register(customerModel,customerAdmin)
admin.site.register(stockModel,stockAdmin)
admin.site.register(sellModel,sellAdmin)
admin.site.register(returnPurchaseModel,returnPurchaseAdmin)
admin.site.register(returnSellModel,returnSellAdmin)
