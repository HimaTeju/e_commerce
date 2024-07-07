from django.shortcuts import render, redirect
from items.models import Category,Item
from .forms import AddRetailerForm

# Create your views here.
def index(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, "core/index.html",
    {"items": items, "categories": categories})

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