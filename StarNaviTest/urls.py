from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path(r'admin/', admin.site.urls),

    url(r'auth/', include('rest_auth.urls')),
    url(r'accounts/', include('rest_registration.api.urls')),

    url(r'', include(('apps.post.api.urls', 'apps.post'), namespace='post-api')),
    url(r'', include(('apps.post.urls', 'apps.post'), namespace='post')),
]
