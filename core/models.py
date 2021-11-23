from django.db import models

class BlogPost(models.Model):
    title       = models.CharField(max_length=255)
    sub_title   = models.TextField(default="")
    miniature   = models.TextField(default="")
    slug        = models.TextField(default="")
    content     = models.TextField(default="")

    def __str__(self):
        return self.title

class Career(models.Model):
    title       = models.CharField(max_length=255)
    miniature   = models.TextField(default="")
    slug        = models.TextField(default="")
    description = models.TextField(default="")
    positions   = models.IntegerField(default=1)

    def __str__(self):
        return self.title
