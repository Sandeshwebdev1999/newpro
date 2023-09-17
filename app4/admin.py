from django.contrib import admin
from .models import *


# Register your models here.

# class SmartPhone_Images(admin.TabularInline):
#     model = SmartPhone_Image


# class SmartPhone_Admin(admin.ModelAdmin):
#     inlines = [SmartPhone_Images]
  





class Product_Images(admin.TabularInline):
    model = Product_Image


class Additional_Informations(admin.TabularInline):
    model = Additional_Information


class Product_Admin(admin.ModelAdmin):
    inlines = (Product_Images,Additional_Informations)
    list_display = ('product_name','price','categories','section','color')
    list_editable = ('categories','section','color')


class Laptops_Admin(admin.ModelAdmin):
    inlines = (Product_Images,Additional_Informations)
    


class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTabularInline]

admin.site.register(slider)
admin.site.register(banner_area)
admin.site.register(Main_Category)
admin.site.register(Category)
admin.site.register(Sub_Category)


admin.site.register(Section)
admin.site.register(Product,Product_Admin)
admin.site.register(Product_Image)
admin.site.register(Additional_Information)
admin.site.register(Color)
admin.site.register(Brand)

admin.site.register(Coupon_Code)


admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Contact)
admin.site.register(special_offer)

#admin.site.register(SmartPhone,SmartPhone_Admin)
admin.site.register(largban_area)