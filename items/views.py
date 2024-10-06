from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import json

from .forms import NewItemForm
from .models import Item, Cart, CartItem, Order, OrderItem

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

@login_required
def confirm_order(request):
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Cart not found'})
    
    cart_items = CartItem.objects.filter(cart=cart)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.update_totals()

    if not cart_items.exists():
        return JsonResponse({'success': False, 'error': 'No items in cart'})

    return render(request, 'items/confirm_order.html', {
        'cart_items': cart_items,
        'cart': cart,})

@login_required
def place_order(request):
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Cart not found'})
    
    cart_items = CartItem.objects.filter(cart=cart)

    if not cart_items.exists():
        return JsonResponse({'success': False, 'error': 'No items in cart'})

    order = Order.objects.create(
        user=user,
        total_price=cart.total_price
    )

    for cart_item in cart_items:
        OrderItem.objects.create(
            order=order,
            item=cart_item.item,
            quantity=cart_item.quantity,
            amount=cart_item.item.price * cart_item.quantity
        )

    cart_items.delete()  # Clear the cart items after creating the order
    cart.delete() # Reset the cart totals

    return JsonResponse({'success': True})