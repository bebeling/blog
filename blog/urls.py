from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^posts/$', views.homepage, name='archive'),
    url(r'^posts/(?P<post_pk>[0-9]+)/$', views.blog_post, name='blog_post')
]

