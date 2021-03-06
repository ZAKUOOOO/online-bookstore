# Generated by Django 3.0.3 on 2020-06-05 10:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ISBN', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('BookName', models.CharField(max_length=50)),
                ('BookAuthor', models.CharField(max_length=50)),
                ('BookNum', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)])),
                ('BookPrice', models.FloatField(validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)])),
                ('PublishDate', models.DateField(null=True, verbose_name='date published')),
                ('ShelfDate', models.DateField(null=True, verbose_name='date shelfed')),
                ('BookInformation', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserName', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('UserAddress', models.CharField(max_length=50)),
                ('UserKey', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShoppingNum', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(1)])),
                ('ISBN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_bookstore.Book')),
                ('UserName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_bookstore.User')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderID', models.AutoField(primary_key=True, serialize=False)),
                ('OrderCard', models.CharField(max_length=19)),
                ('OrderAddress', models.TextField()),
                ('OrderTime', models.DateTimeField(verbose_name='date ordered')),
                ('OrderInformation', models.TextField()),
                ('UserName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_bookstore.User')),
            ],
        ),
    ]
