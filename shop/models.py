from django.db import models


class Store(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    location = models.TextField(null=False)
    contact = models.BigIntegerField(blank=True, null=True)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=256, null=False)


class Customer(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, null=False)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=256, null=False)


class Product(models.Model):
    prod_id = models.AutoField(primary_key=True)
    store_id = models.ForeignKey('Store', on_delete=models.CASCADE)
    name = models.CharField(max_length=32, null=False)
    details = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Review(models.Model):
    rev_id = models.AutoField(primary_key=True)
    prod_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    cust_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    store_id = models.ForeignKey('Store', on_delete=models.CASCADE)
    rating = models.IntegerField(null=False)
    remarks = models.TextField()


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    store_id = models.ForeignKey('Store', on_delete=models.SET_NULL, null=True)
    prod_id = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=False)
    delivered = models.BooleanField(null=False, default=False)
    address = models.TextField(null=False)


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)