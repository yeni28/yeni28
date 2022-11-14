from django.urls import path
from . import views

urlpatterns = [
    
    path('actors/', views.actor_list),
    path('actors/<int:actors_pk>/', views.actor_detail),
    path('movies/', views.movie_list),
    path('movies/<int:movies_pk>/', views.movie_detail),
    path('reviews/', views.review_list),
    path('reviews/<int:reviews_pk>/', views.review_detail),
    path('movies/<int:movies_pk>/reviews/', views.review_create),
    
]