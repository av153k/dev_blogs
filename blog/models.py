from django.db import models
from django.contrib.auth.models import User

class blogs(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField()
    created_on = models.DateTimeField(auto_now_add=True)
    blog_header = models.ImageField(upload_to="blog_pictures", default="dev_blog.png")
    body = models.TextField()


