from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    PostViewSet,
    CommentViewSet,
    GroupViewSet,
    FollowViewSet
)

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='Follow')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='Comment'
)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
]
