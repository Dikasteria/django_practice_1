# Generated by Django 3.2.3 on 2021-05-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.BooleanField(default=False),
        ),
    ]
