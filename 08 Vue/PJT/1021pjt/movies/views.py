import re
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Actor, Movie, Review
from .serializers import ActorListSerializer, ActorSerializer, MovieListSerializer, MovieDetailSerializer, ReviewListSerializer, ReviewSerializer
from django.shortcuts import render, get_object_or_404

from movies import serializers
# Create your views here.

@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actors_pk):
    actor = get_object_or_404(Actor, pk=actors_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movies_pk):
    movie = get_object_or_404(Movie, pk=movies_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def review_detail(request, reviews_pk):
    review = get_object_or_404(Review, pk=reviews_pk)
    if request.method=='GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method=='DELETE':
        review.delete()
        data ={
            'delete' : f'reviews {reviews_pk} is deleted',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def review_create(request, movies_pk):
    movie = get_object_or_404(Movie, pk=movies_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

actors-A .
if serializer.is_valid(raise)
    serializer.save(actors=actros)