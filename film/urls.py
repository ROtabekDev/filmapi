from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import MovieViewSet, ActorViewSet, MovieActorAPIView, CommentAPIView

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)

urlpatterns =[
    path('', include(router.urls)),
    path('movies/<int:id>/actors', MovieActorAPIView.as_view(), name='movie_actors'),
    path('comments/', CommentAPIView.as_view(), name='comments'),
    path('comments/<int:pk>/', CommentAPIView.as_view(), name='comments-pk'),
    path("auth/", obtain_auth_token)
]
