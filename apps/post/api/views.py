from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.post.api.serializers import PostCreateSerializer, PostUpdateSerializer
from apps.post.models import Post


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = (IsAuthenticated, )


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    permission_classes = (IsAuthenticated, )

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        like = request.data.get('like')
        dislike = request.data.get('dislike')
        if like:
            instance.likes += 1
        elif dislike:
            instance.dislikes += 1
        instance.save()
        return self.partial_update(request, *args, **kwargs)
