from django.shortcuts import render, redirect
from items.models import Item, Cart
from .forms import AddRetailerForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    items = Item.objects.all()
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, "core/index.html",{
        "items": items, 
        "user": request.user,
        "cart": cart})

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