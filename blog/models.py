from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

class Post(models.Model):
    """A blog post"""
    author = models.FoeignKey('auth.User')
    title = models.CharField(max_length=128)
    summary = models.TextField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def get_posts(self):
        posts = Post.objects.exclude(published_date__isnull=True).exclude(published_date__exact='').order_by('-published_date')
        return posts

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('blog_post', kwargs={'post_pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    """A comment on a blog post"""
    author = models.CharField(max_length=128)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(models.Post)

