from django.db import models as md
from django.utils import timezone as tz


# Create your models here.

class Board(md.Model):
    title = md.CharField(max_length=200)
    text = md.TextField()
    created_date = md.DateTimeField(default=tz.now())
    published_date = md.DateTimeField("published time")

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = tz.now()
        self.save()