from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^about/$', views.about, name='about'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^posts/$', views.post_list, name='post_list'),
    url(r'^posts/(?P<post_pk>[0-9]+)/$', views.blog_post, name='blog_post'),
    url(r'^posts/(?P<post_pk>[0-9]+)/comment/$', views.submit_comment,
        name='comment'),
]

