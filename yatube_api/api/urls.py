from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

API_VERSION = 'v1'

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path(f'{API_VERSION}/', include(router.urls)),
    path(f'{API_VERSION}/', include('djoser.urls')),
    path(f'{API_VERSION}/', include('djoser.urls.jwt')),
]
