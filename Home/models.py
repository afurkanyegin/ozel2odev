from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe

from Hotel.models import Hotel


class Setting(models.Model):
    STATUS=(('True','Evet'),('False','Hayır'),)
    title=models.CharField(max_length=150)
    keywords=models.CharField(max_length=255)
    description=models.CharField(blank=True,max_length=255)
    company=models.CharField(blank=True,max_length=150)
    address=models.CharField(blank=True,max_length=150)
    phone=models.CharField(blank=True,max_length=15)
    fax=models.CharField(blank=True,max_length=15)
    email=models.CharField(blank=True,max_length=25)
    smtpserver=models.CharField(blank=True,max_length=25)
    smtppassword=models.CharField(blank=True,max_length=25)
    smtpport=models.CharField(blank=True,max_length=5)
    icon=models.ImageField(blank=True,upload_to='images/')
    facebook=models.CharField(blank=True,max_length=50)
    instagram=models.CharField(blank=True,max_length=50)
    twitter=models.CharField(blank=True,max_length=50)
    aboutus=models.TextField(blank=True)
    contact=models.TextField(blank=True)
    references=models.TextField(blank=True)
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True,max_length=15)
    address=models.CharField(blank=True,max_length=255)
    city=models.CharField(blank=True,max_length=55)
    country=models.CharField(blank=True,max_length=55)
    image=models.ImageField(blank=True,upload_to='images/users/')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return  self.user.first_name + ' ' + self.user.last_name + ' ' + '[' + self.user.username + '] '

    def user_id(self):
        return self.user.id

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone','address','city','country','image',]


class ContactFormMessage(models.Model):
    STATUS = (
        ('New','New'),
        ('Read','Read'),
    )
    name = models.CharField(blank=True,max_length=20)
    email = models.CharField(blank=True,max_length=50)
    subject = models.CharField(blank=True,max_length=50)
    message = models.CharField(blank=True,max_length=255)
    status = models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True,max_length=20)
    note = models.CharField(blank=True,max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields =['name', 'email','subject','message']
        widgets = {
            'name':    TextInput(attrs={'class':'input','placeholder':'Name & Surname'}),
            'subject': TextInput(attrs={'class':'input','placeholder':'Subject'}),
            'email':   TextInput(attrs={'class':'input','placeholder':'Email Address'}),
            'message': Textarea(attrs={'class':'input','placeholder':'Your Message','rows':'5'}),
        }

