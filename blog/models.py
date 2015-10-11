from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
import markdown

class Post(models.Model):
    """A blog post"""
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=128)
    summary = models.TextField()  # TODO blank=True
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def get_summary(self):
        return markdown.markdown(self.summary)

    def get_text(self):
        return markdown.markdown(self.text)

    @staticmethod
    def get_posts():
        """Return all published blog posts, sorted by date descending"""
        posts = Post.objects.exclude(published_date__isnull=True).order_by('-published_date')
        return posts

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('blog_post', kwargs={'post_pk': self.pk})

    def is_published(self):
        return self.published_date != None and self.published_date != ''

    def __str__(self):
        return self.title


class Comment(models.Model):
    """A comment on a blog post"""
    author = models.CharField(max_length=128)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    blog_post = models.ForeignKey(Post)

