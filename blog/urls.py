from django.conf.urls import url
# imported file to work with views
from blog import views as blog_views
# imported file to work with views
from djangostarter import views as django_views

urlpatterns = [
    url(r'^$', django_views.index),
    url(r'^blogs/$', blog_views.blogs),
    url(r'^(?P<blog_id>\d+)/$', blog_views.blog)
]