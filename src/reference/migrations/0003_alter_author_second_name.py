# Generated by Django 4.0.6 on 2022-08-09 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0002_genre_book_series_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='second_name',
            field=models.CharField(blank=True, help_text='Enter second author name', max_length=25, null=True),
        ),
    ]