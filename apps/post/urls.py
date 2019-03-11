from django.conf.urls import url

from apps.post.views import PostList

urlpatterns = [
    url(r'^posts/$', PostList.as_view(), name='post-list'),
]
