from .views import *
from django.urls import path


urlpatterns = [
    path('anime/', AnimeListCreateAPIView.as_view()),
    path('anime/<int:pk>/', AnimeRetrieveAPIView.as_view()),
    path('season/', SeasonListCreateAPIView.as_view()),
    path('season/<int:pk>/', SeasonRetrieveAPIView.as_view()),
    path('episode/', EpisodeListCreateAPIView.as_view()),
    path('episode/<int:pk>/', EpisodeRetrieveAPIView.as_view()),
    path('genre/', GenreListCreateAPIView.as_view()),
    path('genre/<int:pk>/', GenreRetrieveAPIView.as_view()),
    path('category/', CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveAPIView.as_view()),
    path('favorite/<int:pk>/', FavoriteRetrieveAPIView.as_view()),

]