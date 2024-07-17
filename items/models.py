from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    Created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name',]
    
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    product_count = models.PositiveIntegerField(default=0)
    total_price = models.FloatField(default=0.0)

    def update_totals(self):
        # Calculate total price and product count from related CartItems
        cart_items = self.cartitem_set.all()
        total_price = sum(cart_item.quantity * cart_item.item.price for cart_item in cart_items)
        product_count = sum(cart_item.quantity for cart_item in cart_items)

        # Update the fields in the Cart model
        self.total_price = total_price
        self.product_count = product_count
        self.save()

    def __str__(self):
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.quantity} x {self.item.name} in cart of {self.cart.user.username}"
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.quantity} x {self.item.name} in order {self.order.id}"