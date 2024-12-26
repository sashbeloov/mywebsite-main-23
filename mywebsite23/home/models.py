from django.db import models
from django.forms import Textarea, ModelForm,TextInput


# Create your models here.

class Setting(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    phone = models.CharField(max_length=500)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    smtp_server = models.CharField(blank=True,max_length=50)
    smtp_email = models.CharField(blank=True,max_length=50)
    smtp_password = models.CharField(blank=True,max_length=10)
    smtp_port = models.CharField(blank=True,max_length=5)
    youtube = models.URLField(blank=True, max_length=50)
    instagram = models.URLField(blank=True, max_length=50)
    facebook = models.URLField(blank=True, max_length=50)
    icon = models.ImageField(blank=True, upload_to='images/')
    aboutus = models.TextField(max_length=500)
    contact = models.TextField(max_length=500)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(blank=True, max_length=20)
    phone = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'subject', 'message']
        widgets = {
            'name':TextInput(attrs={'class':'input', 'placeholder': 'Name & Surname'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'Phone Number'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Your Message', 'rows': '5'}),
        }

