from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cinema, Comment, Movie, Schedule, Hall


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = ('title', 'poster', 'country', 'premiere', 'duration', 'age', 'description')
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        # fields = ('movie', 'author', 'text', 'date')
        fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        # fields = ('title', 'poster', 'address', 'phone', 'description')
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True, many=False)
    # cinema = CinemaSerializer(read_only=True, many=False)
    fixture = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Schedule
        # fields = ('movie', 'fixture', 'adult_price', 'child_price', 'student_price')
        fields = '__all__'


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        # fields = ('movie', 'fixture', 'adult_price', 'child_price', 'student_price')
        fields = '__all__'


