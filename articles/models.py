from django.db import models
from django.urls import reverse
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    views = models.IntegerField(default=0)
    viewers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='viewed_articles',
        blank=True
    )
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_articles',
        blank=True
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
    
class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
    )
    comment = models.TextField(default="your article was great....")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse("article_list")
     