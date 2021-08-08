from django.db import models
from vendor.models import Vendor
# Create your models here.

class Post(models.Model):
    vendor = models.ForeignKey( Vendor , on_delete= models.CASCADE, null = True, blank = True)
    name =  models.TextField(max_length = 1500)
    description = models.TextField(max_length = 1500)
    date_posted = models.DateTimeField( auto_now_add=True)
    likes = models.IntegerField(default = 0)
    photo = models.ImageField( upload_to='post-image', null = True, blank = True)

    def __str__(self):
        return f'{self.name} by {self.vendor.user.username}'


class Comment(models.Model):
    post = models.ForeignKey( Post , on_delete=models.CASCADE)
    text = models.TextField(max_length = 1500)


class Testimonial(models.Model):
    # user = models.OneToOneField( User,  on_delete=models.CASCADE)
    text = models.TextField(max_length = 1500)
    date_posted = models.DateTimeField( auto_now_add=True)




