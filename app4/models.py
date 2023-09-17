from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
import datetime
# from django.urls import reverse
# Create your models here.
class slider(models.Model):
    DISCOUNT_DEAL = (
        ('HOT DEALS','HOT DEALS'),
        ('New Arraivels','New Arraivels'),
    )

    image = models.ImageField(upload_to='media/slider_imgs')
    Discount_Deal = models.CharField(choices=DISCOUNT_DEAL,max_length=100)
    SALE = models.IntegerField()
    Brand_Name = models.CharField(max_length=200)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=200)

    def __str__(self):
        return self.Brand_Name
    

class banner_area(models.Model):
    image = models.ImageField(upload_to='media/banner_img')
    Discount_Deal = models.CharField(max_length=100)
    Quote = models.CharField(max_length=100)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=200, null=True, default = '')
    

    def __str__(self):
        return self.Quote



class largban_area(models.Model):
    image = models.ImageField(upload_to='media/largban_img')
    text = models.CharField(max_length=100)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=200, null=True, default = '')
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.text




class special_offer(models.Model):
    image = models.ImageField(upload_to='media/specialOffer_img')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    Link = models.CharField(max_length=200, null=True, default = '')

    def __str__(self):
        return self.name


class Main_Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
 
     

class Category(models.Model):
    main_category = models.ForeignKey(Main_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + '--' + self.main_category.name


class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.category.main_category.name + '--' + self.category.name + '--' + self.name

    
class First_Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
     

class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Color(models.Model):
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.code

    
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Coupon_Code(models.Model):
    code = models.CharField(max_length=100)
    discount = models.IntegerField()

    def __str__(self):
        return self.code
    



# class SmartPhone(models.Model):
#     total_quantity = models.IntegerField()
#     Availibility = models.IntegerField()
#     phone_image = models.CharField(max_length=100)
#     smartphone_name = models.CharField(max_length=100)
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
#     price = models.IntegerField()
#     Discount = models.IntegerField()
#     tax = models.IntegerField(null=True)
#     packing_cost = models.IntegerField(null=True)
#     product_information = RichTextField()
#     model_name = models.CharField(max_length=100)
#     categories = models.ForeignKey(Category, on_delete=models.CASCADE)
#     color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True)
#     Tags = models.CharField(max_length=100)
#     Description = RichTextField()
#     section = models.ForeignKey(Section, on_delete= models.DO_NOTHING)
#     slug = models.SlugField(default='', max_length=500, null=True, blank=True)


#     def __str__(self):
#         return self.smartphone_name


#     def get_absolute_url(self):
#         from django.urls import reverse
#         return reverse("product_detail", kwargs={'slug': self.slug})

#     class Meta:
#         db_table = "app4_SmartPhone"

  


# class SmartPhone_Image(models.Model):
#     smartphone = models.ForeignKey(SmartPhone, on_delete=models.CASCADE)
#     image_url = models.CharField(max_length=100)



# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.smartphone_name)
#     if new_slug is not None:
#         slug = new_slug
#     qs = SmartPhone.objects.filter(slug=slug).order_by('-id')
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" % (slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug


# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)

# pre_save.connect(pre_save_post_receiver, SmartPhone)

    

   



    

class Product(models.Model):
    total_quantity = models.IntegerField()
    Availibility = models.IntegerField()
    feature_image = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    Discount = models.IntegerField()
    tax = models.IntegerField(null=True)
    packing_cost = models.IntegerField(null=True)
    product_information = RichTextField()
    model_name = models.CharField(max_length=100)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True)
    Tags = models.CharField(max_length=100)
    Description = RichTextField()
    section = models.ForeignKey(Section, on_delete= models.DO_NOTHING)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.product_name


    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_detail", kwargs={'slug': self.slug})

    class Meta:
        db_table = "app4_Product"






def create_slug(instance, new_slug=None):
    slug = slugify(instance.product_name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Product)

    

class Product_Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=100)


class Additional_Information(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    firstname = models.CharField(max_length=100,)
    lastname = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=50)
    postcode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    additional_info = models.TextField()
    amount = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/order_images')
    Quantity = models.CharField(max_length=20)
    price = models.CharField(max_length=50)
    total = models.CharField(max_length=100)

    def __str__(self):
        return self.order.user.username


class Contact(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
        

# class Wishlist(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     product = models.ManyToManyField(Product,)


#     def __str__(self):
#         return self.user.username

#     def get_absolute_url(self):
#         return reverse("wishlist", args=[str(self.id)])
    
        



    # def __str__(self):
    #     return f"{self.user.username}'s Wishlist"

    # def add_product(self,product):
    #     self.products.add(product)

    # def remove_product(self,product):
    #     self.products.romove(product)

    # def clear(self):
    #     self.products.clear()

    # def get_products(self):
    #     return self.products.all()

    # def has_product(self):
    #     return self.products.filter(id=product.id).exists()
    
    
# class Checkout(models.Model):
#     state = models.CharField(max_length=40, default='')
#     firstname = models.CharField(max_length=20, default='')
#     lastname = models.CharField(max_length=20, default='')
#     address = models.TextField(max_length=100, default='')
#     city = models.CharField(max_length=20, default='')
#     postcode = models.IntegerField(default='')
#     email = models.EmailField(default='')
#     phone = models.CharField(max_length=15)
#     # phone = models.IntegerField(default=1)
#     amount = models.CharField(max_length=50)

#     def __str__(self):
#         return self.email
    
# class Contact(models.Model):
#     name = models.CharField(max_length=10)
#     address = models.TextField(max_length=100, default='')
#     zip = models.IntegerField()
#     city = models.CharField(max_length=20, default='')

#     def __str__(self):
#         return self.name
    