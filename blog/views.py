from django.shortcuts import render
from . import forms
from . import models
from blog import settings

def homepage(request):
    posts = models.Post.get_posts()[0]  # only display most recent post
    context = {
        'page_title': settings.BLOG_TITLE,
        'posts': posts,
        'site_title': settings.BLOG_TITLE,
    }
    return render(request, 'blog/homepage.html', context)

def archive(request, post_pk):
    posts = models.Post.get_posts()
    context = {
        'page_title': 'Archive - ' + settings.BLOG_TITLE,
        'posts': posts,
        'site_title': settings.BLOG_TITLE,
    }
    return render(request, 'blog/archive.html', context)

def blog_post(request, post_pk, comment_form=None):
    post = models.Post.objects.get(pk=post_pk)

    if not post.is_published()
        return redirect('homepage')

    comments = models.Post.objects.filter(comment__post=post).order_by('-date')
    form = commment_form or forms.PostForm()
    context = {
        'comment_form': form,
        'comments': comments,
        'page_title': post.title,
        'post': post,
        'site_title': settings.BLOG_TITLE,
    }
    return render(request, 'blog/blog_post.html', context)

def submit_comment(request, post_pk):
    if request.method == 'POST':
        post = models.Post.objects.get(pk=post_pk)

        if not post.is_published():
            return redirect('homepage')

        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog.views.post', pk=blog_post.pk)
        else:
            return blog_post(request, post_pk, form)
    else:
        return redirect('blog_post', pk=post_pk)

