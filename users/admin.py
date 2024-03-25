from django.contrib import admin
from catalog.models import Category, Seller, Discount, Product, Cart, Promocode, CashBack, Order, M2M_order, Comments


admin.site.register(Category)
admin.site.register(Seller)
admin.site.register(Discount)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Promocode)
admin.site.register(CashBack)
admin.site.register(Order)
admin.site.register(M2M_order)
admin.site.register(Comments)
