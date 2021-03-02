from django.db import models
from django.contrib.auth.models import User
from products.models import Address
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    image = models.ImageField(upload_to = 'profile_pics', default='default.jpg')
    def __str__(self):
        return f'{self.user.username}"s profile'
    
        
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    issue = models.TextField()
    
