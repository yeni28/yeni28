
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index'), #사용자에게 index.html을 보여주게된다.
    path('greeting/',views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch' ),
    path('hello/<name>',views.hello,name='hello'),
]