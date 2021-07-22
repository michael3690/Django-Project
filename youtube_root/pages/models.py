from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from ckeditor.fields import RichTextField
timezone.localtime(timezone.now())

class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated', default=timezone.now)
    create_date = models.DateTimeField('First Published', default=timezone.now)
    bodytext = models.TextField('Page Content', blank=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=60)
    create_date = models.DateTimeField('Date Published', default=timezone.now)
    maintext = RichTextField('Post Content')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image  = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title + " - " + str(self.author)