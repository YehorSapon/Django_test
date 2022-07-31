# Generated by Django 4.0.6 on 2022-07-31 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0002_genre_book_series_book'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcard',
            name='genre',
            field=models.ManyToManyField(related_name='seres_book', to='reference.genre_book'),
        ),
        migrations.AddField(
            model_name='bookcard',
            name='publ_hous',
            field=models.ManyToManyField(related_name='publ_house_book', to='reference.publishinghous'),
        ),
        migrations.AddField(
            model_name='bookcard',
            name='series',
            field=models.ManyToManyField(related_name='seres_book', to='reference.series_book'),
        ),
        migrations.RemoveField(
            model_name='bookcard',
            name='author',
        ),
        migrations.AddField(
            model_name='bookcard',
            name='author',
            field=models.ManyToManyField(related_name='author_book', to='reference.author'),
        ),
        migrations.AlterField(
            model_name='bookcard',
            name='book_cover',
            field=models.CharField(choices=[('1', 'Cardboard'), ('2', 'Hardback'), ('3', 'Hidebound'), ('4', 'Soft')], default='soft', max_length=20),
        ),
    ]
