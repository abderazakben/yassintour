from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
# moel admin 
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=300, null=True , blank=True)
    mobile = models.CharField(max_length=20 ,  null=True , blank=True )
    def __str__(self):
        return self.user.username

########### Models Hotel databesece
class HotelAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Full_name = models.CharField(max_length=300 , null=True , blank=True) 
    email = models.EmailField(max_length=300,null=True,blank=True)

    def __str__(self):
        return str(self.user.username)

#####  model Activites
class Activities(models.Model):
    #adress 3ando 3ala b Map
    address = models.CharField(max_length=200, null=True , verbose_name='Enter Your city')
    name_activities = models.CharField(max_length=200, null=True , verbose_name='Enter Your name activite')
    A_image = models.ImageField(null=True ,blank=True, upload_to="images/", verbose_name='Enter Your name image' )
    A_Text  =  models.TextField(max_length=600 , verbose_name='Enter Your  commenter')
    price  = models.IntegerField(null=True ,blank=True ,verbose_name='Enter Your price')
    date = models.DateTimeField(auto_now_add=True ,verbose_name='Enter Your datae')
    def __str__(self):
        return str(self.name_activities)
#####  model Excursions
class Excursions(models.Model):
    #adress 3ando 3ala b Map
    address_E = models.CharField(max_length=200, null=True ,verbose_name='Enter Your city')
    name_E = models.CharField(max_length=200, null=True ,verbose_name='Enter Your name Excursions ')
    image_E = models.ImageField(null=True ,blank=True,upload_to="images/" ,verbose_name='Enter Your image ')
    Text_E  =  models.TextField(max_length=600 ,verbose_name='Enter Your commenter ')
    price_E  = models.IntegerField(null=True ,blank=True ,verbose_name='Enter Your price ')
    date_E = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True ,blank= True )
    def save(self, *args , **kwargs):
        # save daata
        self.slug = slugify(self.name_E)
        super(Excursions,self).save(*args , **kwargs)
    def __str__(self):
        return self.address_E
    class Meta:
        ordering = ('address_E',)            

class Images(models.Model):
    excursions= models.ForeignKey(Excursions , on_delete=models.CASCADE)
    images = models.ImageField(upload_to="images/exurus")

    def __str__(self):
        return self.excursions.name_E

ORDER_CAR= (
     ("Ecomi" , "200"),
     ("Besnis" , "200"),
     ("4X4" , "200"),
     ("Minibost" , "200"),
     ("autobost" , "200"),
    
 )
class Traget(models.Model):
    Ctiy_start = models.CharField(max_length=400 , null=True , blank=True)
    Ctiy_and = models.CharField(max_length=400 , null=True , blank=True)
    Date_dipart = models.DateTimeField(null=True, blank=True, default=None)
    Date_final = models.DateTimeField(null=True, blank=True)
    Cart_status = models.CharField(max_length=200, null=True,blank=True , choices=ORDER_CAR )
    Adults_t = models.PositiveIntegerField()
    Enfants_t = models.PositiveIntegerField()
    Bebe_t = models.PositiveIntegerField()


class Cart(models.Model):
    costomer = models.ForeignKey(HotelAdmin,on_delete=models.SET_NULL,null=True , blank=True)
    costemer2 = models.ForeignKey(User, on_delete=models.CASCADE , null=True , blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart: " + str(self.id) 

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    produt = models.ForeignKey(Excursions , on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField() 
    def __str__(self):
        return "Cart: " + str(self.cart.id) + "CartProduct:  " + str(self.id) 


ORDER_STATUS= (
     ("Order Received" , "Order Received"),
     ("Order Processing" , "Order Processing"),
     ("On the way" , "On the way"),
     ("Order Completed" , "Order Completed"),
     ("Order Canceled" , "Order Canceled"),
    
 )



class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    hotel = models.OneToOneField(HotelAdmin , on_delete=models.CASCADE)
    order_name = models.CharField(max_length=200)
    namber_room = models.CharField(max_length=200)
    Date_dipart = models.DateTimeField(null=True, blank=True, default=None)
    
    
    subtotal = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50 , choices=ORDER_STATUS)
     

    def __str__(self):
        return "order: " + str(self.id)
          

