from django.shortcuts import render, redirect
from items.models import Item, Cart, Order, OrderItem
from .forms import AddRetailerForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.user.is_superuser:
        # Fetch all orders and order items for superusers
        orders = Order.objects.all()
        order_items = OrderItem.objects.all()
        context = {
            "orders": orders,
            "order_items": order_items,
            "user": request.user,
            "is_superuser": True,
        }
    else:
        items = Item.objects.all()
        cart, created = Cart.objects.get_or_create(user=request.user)
        context = {
            "items": items, 
            "user": request.user,
            "cart": cart,
            "is_superuser": False,
        }

    return render(request, "core/index.html", context)

def contact(request):
    return render(request, "core/contact.html")

def add_retailer(request):
    if request.method == "POST":
        form = AddRetailerForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = AddRetailerForm()

    return render(request, "core/add_retailer.html", {"form": form})
