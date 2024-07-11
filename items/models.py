from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    Created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    

    class Meta:
        ordering = ['name',]
    
    def __str__(self):
        return self.name