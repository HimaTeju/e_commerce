from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import json

from .forms import NewItemForm
from .models import Item, Cart, CartItem

# Create your views here.
@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('core:index')

    form = NewItemForm()

    return render(request, 'items/form.html', {
        'form': form,
        'title': 'New Item',
    })

@login_required
@require_POST
def add_to_cart(request):
    try:
        data = json.loads(request.body)
        item_id = data.get('item_id')
        quantity = data.get('quantity')

        item = get_object_or_404(Item, id=item_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
        cart_item.quantity += int(quantity)
        cart_item.amount = int(item.price) * int(quantity)
        cart_item.save()
        cart.update_totals()
        

        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)
    
@login_required
def show_cart_items(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.update_totals()
    cart_items = CartItem.objects.filter(cart__user=request.user)
        
    return render(request, 'items/view_cart.html', {
        'cart_items': cart_items,
        'cart': cart,
    })
