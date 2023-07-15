from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    PostViewSet,
    CommentViewSet,
    GroupViewSet,
    FollowViewSet
)

router = DefaultRouter()
router.register('posts', PostViewSet, basename='Post')
router.register('groups', GroupViewSet, basename='Group')
router.register('follow', FollowViewSet, basename='Follow')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='Comment'
)

app_name = 'api'

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
