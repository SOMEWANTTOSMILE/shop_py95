from django.urls import path
from catalog.views import CategoryListView, CategoryProductsView, SellerListView, SellerProductView, DiscountProductView


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/<int:category_id>/', CategoryProductsView.as_view(), name='category-products'),
    path('seller/', SellerListView.as_view(), name='sellers'),
    path('seller/<int:seller_id>/', SellerProductView.as_view(), name='seller-products'),
    path('discount/<int:discount_id>/', DiscountProductView.as_view(), name='seller-products'),
]