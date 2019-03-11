from rest_framework import serializers

from apps.post.models import Post


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('id', 'text', 'author')


class PostUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'likes', 'dislikes')
