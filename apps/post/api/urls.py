from django.conf.urls import url

from apps.post.api.views import PostCreateAPIView, PostUpdateAPIView

urlpatterns = [

    url(r'^post/$', PostCreateAPIView.as_view(), name='post-create'),
    url(r'^post-detail/(?P<pk>[0-9a-f-]+)/$', PostUpdateAPIView.as_view(), name='item-detail'),
]
