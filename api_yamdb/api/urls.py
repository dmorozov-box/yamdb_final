from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    get_jwt_token, register, CategoryViewSet, GenreViewSet,
    TitlesViewSet, ReviewViewSet, CommentViewSet, UserViewSet
)

router = DefaultRouter()

router.register('titles', TitlesViewSet, basename='titles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')

router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='review'
)

router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router.register('users', UserViewSet)

urlpatterns = [
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token'),
    path('v1/', include(router.urls)),
]
