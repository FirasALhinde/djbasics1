from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000,null=True,blank=True) 
    publish_date = models.DateField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to = 'posts/')
    category = models.ForeignKey(to='Category',on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        # ordering = ['publish_date']
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
    def __str__(self):
            return self.name