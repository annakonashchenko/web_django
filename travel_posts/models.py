from django.db import models

class Comments(models.Model):
    full_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False)
    comment_text = models.TextField(blank=False)
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.full_name

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publish_date = models.DateField()
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
