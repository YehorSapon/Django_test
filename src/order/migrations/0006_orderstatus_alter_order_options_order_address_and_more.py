# Generated by Django 4.0.6 on 2022-08-19 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_bookincart_cart_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Enter title oorder status', max_length=25, null=True, verbose_name='Title order status')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-create_date',), 'verbose_name_plural': 'Orders'},
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Adress'),
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='statuses', to='order.orderstatus', verbose_name='Order status'),
        ),
    ]
