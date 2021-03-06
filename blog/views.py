from django.core import serializers
from django.shortcuts import redirect
from django.shortcuts import render
from . import forms
from . import models
from blog import settings

def homepage(request):
    posts = models.Post.get_posts()[:1]  # only display most recent post
    context = {
        'page_title': settings.BLOG_TITLE,
        'posts': posts,
        'site_title': settings.BLOG_TITLE,
        'titlebar': settings.BLOG_TITLE,
    }
    return render(request, 'blog/post_list.html', context)

def about(request):
    context = {
        'page_title': 'About',
        'site_title': settings.BLOG_TITLE,
        'titlebar': 'About - ' + settings.BLOG_TITLE,
    }
    return render(request, 'blog/about.html', context)

def archive(request):
    posts = models.Post.get_posts()
    context = {
        'page_title': 'Archive',
        'posts': posts,
        'site_title': settings.BLOG_TITLE,
        'titlebar': 'Archive - ' + settings.BLOG_TITLE,
    }
    return render(request, 'blog/archive.html', context)

def blog_post(request, post_pk, comment_form=None):
    post = models.Post.objects.get(pk=post_pk)

    if not post.is_published():
        return redirect('homepage')

    comments_queryset = models.Comment.objects.filter(blog_post=post)
    fields = ('author', 'date', 'text')
    comments = serializers.serialize('json', comments_queryset, fields=fields)
    form = comment_form or forms.CommentForm()
    context = {
        'comment_form': form,
        'comments': comments,
        'page_title': post.title,
        'post': post,
        'site_title': settings.BLOG_TITLE,
        'titlebar': post.title + ' - ' + settings.BLOG_TITLE,
    }
    return render(request, 'blog/blog_post.html', context)

def post_list(request):
    posts = models.Post.get_posts()
    context = {
        'page_title': settings.BLOG_TITLE,
        'posts': posts,
        'site_title': settings.BLOG_TITLE,
        'titlebar': 'All posts - ' + settings.BLOG_TITLE,
    }
    return render(request, 'blog/post_list.html', context)

def submit_comment(request, post_pk):
    if request.method == 'POST':
        post = models.Post.objects.get(pk=post_pk)

        if not post.is_published():
            return redirect('homepage')

        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_post = post
            comment.save()
            return redirect('blog_post', post_pk=post_pk)
        else:
            return blog_post(request, post_pk, form)
    else:
        return redirect('blog_post', post_pk=post_pk)

