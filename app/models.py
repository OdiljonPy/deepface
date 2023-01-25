from django.db import models


class Image(models.Model):
    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images')

    created_at = models.DateTimeField(auto_now_add=True)


class Result(models.Model):
    img1 = models.CharField(max_length=150)
    img2 = models.CharField(max_length=150)
    response = models.TextField()
    idx = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)



