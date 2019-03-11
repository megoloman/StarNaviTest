from django.views.generic import ListView

from apps.post.models import Post


class PostList(ListView):
    template_name = 'posts.html'
    model = Post

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')
