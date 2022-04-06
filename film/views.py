from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Actor, Movie, Comment
from .serializer import ActorSerializer, MovieSerializer, CommentSerializer


class MovieViewSet(ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['genre']
    search_fields = ["title"]
    ordering_fields = ['imdb', '-imdb']

    @action(detail=True, methods=["POST"])
    def add_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        data = request.data
        first_name = data['first_name']
        last_name = data['last_name']
        birthdate = data['birthdate']
        gender = data['gender']
        actor = Actor.objects.create(
            first_name=first_name,
            last_name=last_name,
            birthdate=birthdate,
            gender=gender
        )
        movie.actors.add(actor)
        actors = movie.actors.all()
        serializer = ActorSerializer(actors, many=True)

        return Response(serializer.data)

    @action(detail=True, methods=["POST"])
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor_id = request.data["pk"]
        actor = Actor.objects.get(pk=actor_id)

        movie.actors.remove(actor)

        actors = movie.actors.all()
        serializer = ActorSerializer(actors, many=True)

        return Response(serializer.data)


class MovieActorAPIView(APIView):
    def get(self, request, id, *args, **kwargs):
        movie = Movie.objects.get(pk=id)
        actors = movie.actors.all()
        serializer = ActorSerializer(actors, many=True)

        return Response(serializer.data)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CommentAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        request.data['user'] = request.user.id

        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)

    def get(self, request):

        comments = Comment.objects.filter(user=request.user)
        serializer = CommentSerializer(comments, many=True)

        length = len(serializer.data)
        array = []

        for i in range(length):
            dict_type = dict(serializer.data[i])
            dict_type.pop('user')
            array.append(dict_type)

        return Response(data=array)

    def delete(self, request, pk):
        comment = Comment.objects.filter(user=request.user)[pk-1]
        comment.delete()

        comments = Comment.objects.filter(user=request.user)
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)

