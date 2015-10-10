from django.conf import settings

BLOG_TITLE = getattr(settings, 'SITE_TITLE', 'My blog')

