from django.db import models
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'


class Seller(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    contact = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Discount(models.Model):
    name = models.CharField(max_length=255)
    percent = models.PositiveIntegerField()
    exp_date = models.DateField()

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    count_on_stock = models.PositiveBigIntegerField()
    article = models.CharField(max_length=255)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name}, {self.article}'


class Cart(models.Model):
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    count = models.PositiveBigIntegerField(blank=True, null=True)


class Promocode(models.Model):
    name = models.CharField(max_length=255)
    is_cimilative = models.BooleanField(default=False)
    exp_data = models.DateField()

    def __str__(self):
        return self.name


class CashBack(models.Model):
    percent = models.PositiveBigIntegerField()
    threshold = models.PositiveBigIntegerField()


class Product_img(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f'image for product: {self.product}'


class Order(models.Model):

    status_order_choices = (
        ('in processing', 'in processing'),
        ('accepted by the store', 'accepted by the store'),
        ('sent', 'sent'),
        ('delivered', 'delivered'),
        ('on the way', 'on the way'),
        ('on stock', 'on stock'),
        ('received', 'received'),
    )

    delivery_method_choice = (
        ('to the point of issue', 'to the point of issue'),
        ('courier', 'courier'),
    )

    payment_status_choice = (
        ('paid', 'paid'),
        ('not paid', 'not paid'),
        ('cancelled', 'cancelled'),
    )

    payment_method_choice = (
        ('by card', 'by card'),
        ('in cash', 'in cash'),
    )

    is_notif_reqired = (
        ('within in 1 hour', 'within in 1 hour'),
        ('within in 6 hour', 'within in 3 hour'),
        ('within in 24 hour', 'within in 24 hour'),
        ('without', 'without')
    )

    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255, choices=status_order_choices, blank=False)
    delivery_method = models.CharField(max_length=255, choices=delivery_method_choice, blank=False)
    datetime = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    payment_status = models.CharField(max_length=255, choices=payment_status_choice, blank=False, default='not paid')
    payment_method = models.CharField(max_length=255, choices=payment_method_choice, blank=False)
    delivery_address = models.CharField(max_length=255)
    is_notif_required = models.CharField(max_length=255, choices=is_notif_reqired, blank=False,
                                         default='within in 1 hour')

    def __str__(self):
        return f'number of order:{self.id}, user: {self.id}'


class OrderProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(null=True, blank=True)


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'user: {self.user}, product: {self.product}'


class Comment_image(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comment_images/')

    def __str__(self):
        return f'image for {self.comment}'
