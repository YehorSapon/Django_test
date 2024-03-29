# Generated by Django 4.0.6 on 2022-08-10 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0003_alter_bookincart_book_alter_bookincart_cart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='usercarts', to=settings.AUTH_USER_MODEL, verbose_name='Customer'),
        ),
    ]
