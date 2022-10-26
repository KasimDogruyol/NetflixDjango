from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    isim = models.CharField(max_length = 100)
    resim = models.FileField(upload_to = 'profiles/')
    slug = models.SlugField(null = True,blank =True, unique = True, editable = False)
    def __str__(self):
        return self.isim
    def save(self,*args,**kwargs):
        self.slug = slugify(self.isim)
        super().save(*args, **kwargs)

class Account(models.Model):
    user =models.OneToOneField(User,on_delete = models.CASCADE)
    resim = models.FileField(upload_to = 'profilResimleri/', verbose_name = 'Profil Resmi')
    tel = models.IntegerField(verbose_name = 'Telefon Numarası')
    
    def __str__(self):
        return self.user.username