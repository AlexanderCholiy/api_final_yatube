from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('comments', CommentViewSet, basename='comment')
router.register('follow', FollowViewSet, basename='follow')
router.register('groups', GroupViewSet, basename='group')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/posts/<int:post_id>/comments/', CommentViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='comment-list'),
    path('v1/posts/<int:post_id>/comments/<int:pk>/', CommentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='comment-detail'),
]
