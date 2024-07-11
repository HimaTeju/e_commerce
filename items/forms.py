from django import forms
from .models import Item

INPUT_CLASSES = 'mt-2 w-full py-4 px-6 rounded-xl border border-gray-400'
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image']
    
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES,}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES,}),
            'price': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASSES}),
        }