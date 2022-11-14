
from dataclasses import fields
from rest_framework import serializers
from .models import Actor, Movie, Review


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)

class ActorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'
        read_only = ('name',)

class ActorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = ('id','name','movies')

class ActornameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = ('name',)

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title','overview',)


class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActornameSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('id','actors','title','overview','release_date','poster_path')



class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('title','content',)

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
