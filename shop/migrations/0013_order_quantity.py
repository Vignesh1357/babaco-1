# Generated by Django 3.1.3 on 2020-12-07 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_remove_order_store_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]