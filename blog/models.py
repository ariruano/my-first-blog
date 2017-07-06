from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.TextField()
    createdDate = models.DateTimeField(
        default=timezone.now)
    publishedDate = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()
    def _str_(self):
        return self.title

# Create your models here.
