from django.db import models
# from django_soft_deletion.models import SoftDeletionModel

# Create your models here.

# class Post(models.Model):
class Post(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.TextField(null=True)