from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator
# Create your models here.

from django.contrib.auth.models import AbstractUser,PermissionsMixin,AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from firstapp.managers import CustomUserManager

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email address main'), unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    is_customer = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address = models.CharField(max_length=1000)

class Seller(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    gst = models.CharField(max_length = 10)
    warehouse_location = models.CharField(max_length = 1000)    



class Product(models.Model):
    product_id = models.AutoField(primary_key=True) 
    product_name = models.CharField(max_length=255) 
    price = models.FloatField()

    @classmethod
    def upadateprice(cls,product_id,price):
        product = Product.objects.filter(product_id = product_id).first()
        product.price = price
        product.save()
        return product
    

    @classmethod
    def create(cls,product_name,price):
        product = Product(product_name=product_name,price=price).save()
        return product

    def _str_(self):
        return self.product_name


class CartManager(models.Manager):
    def create_cart(self,user):
        cart = self.create(user = user)
        return cart

class Cart (models.Model):
    cart_id = models.AutoField (primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE) 
    created_on = models.DateTimeField(default = timezone.now)

    objects = CartManager()


class ProductInCart (models.Model):
    class Meta:
        unique_together = (('cart', 'product'),)
    product_in_cart_id = models.AutoField(primary_key=True) 
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE) 
    quantity = models.PositiveIntegerField()




class Order (models.Model): 
    status_choices = ( 
    (1, 'Not Packed'),
    (2, 'Ready For Shipment'),
    (3, 'Shipped'),
    (4, 'Delivered')) 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.IntegerField(choices = status_choices, default=1)

class Deal(models.Model):
    user = models.ManyToManyField(CustomUser)
    deal_name = models.CharField(max_length = 255)