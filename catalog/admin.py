from django.contrib import admin
from catalog.models import (Cart, OrderProducts, Order, Promocode, Product_img, Product, Comment, Category,
                            Comment_image, Discount, Seller, CashBack)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('article', 'name', 'price')
    search_fields = ('article', 'name', 'category__name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(OrderProducts)
admin.site.register(Order)
admin.site.register(Promocode)
admin.site.register(Product_img)
admin.site.register(Comment_image)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Seller)
admin.site.register(CashBack)