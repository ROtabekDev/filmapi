from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Movie, Actor, Comment
import datetime


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'first_name', 'last_name', 'birthdate', 'gender')

    def validate_birthdate(self, value):
        date = datetime.date(1950, 1, 1)
        if value < date:
            raise ValidationError(detail="01.01.1950 dan katta bo`lsin.")

        return value


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'movie', 'user', 'text')