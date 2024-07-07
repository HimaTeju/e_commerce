from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import NewItemForm
from .models import Item

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