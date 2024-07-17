# Generated by Django 5.0.6 on 2024-07-14 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0006_cart_cartitem_order_orderitem"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="product_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="cart",
            name="total_price",
            field=models.FloatField(default=0.0),
        ),
    ]
