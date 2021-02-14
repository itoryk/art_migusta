from django.db import models
from django.db.models import Manager

# Create your models here.


class PostManager(Manager):
    pass


class FeedbackModel(models.Model):
    objects = PostManager()
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=400)
