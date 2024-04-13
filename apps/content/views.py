from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from apps.user.permissions import *
from .serializers import *


class AnimeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeListSerializer
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ['title']
    permission_classes = [IsSuperuserOrReadOnly]


class AnimeRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class SeasonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class SeasonRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class EpisodeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class EpisodeRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class GenreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ['name']
    permission_classes = [IsSuperuserOrReadOnly]


class GenreRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ['name']
    permission_classes = [IsSuperuserOrReadOnly]


class CategoryRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperuserOrReadOnly]


class FavoriteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsOwnerOrAdminCanChange]


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrCreateOnly]