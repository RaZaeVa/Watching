from django.db.models import Avg
from rest_framework import serializers
from .models import *


class CategoryAnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anime
        fields = ['id', 'title']


class CategorySerializer(serializers.ModelSerializer):
    anime = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'anime']

    def get_anime(self, category):
        # Получаем последние три аниме для данной категории
        latest_anime = category.anime_set.order_by('-release_date')[:3]
        # Сериализуем аниме
        serializer = CategoryAnimeSerializer(latest_anime, many=True)
        return serializer.data


class WatchHistorySerializer(serializers.Serializer):

    class Meta:
        model = WatchHistory
        fields = 'episode'


class GenreSerializer(serializers.ModelSerializer):
    anime = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ('id', 'name', 'anime')

    def get_anime(self, genre):
        latest_anime = genre.anime_set.order_by('-release_date')[:3]
        serializer = CategoryAnimeSerializer(latest_anime, many=True)
        return serializer.data


class FavoriteSerializer(serializers.ModelSerializer):
    anime = CategoryAnimeSerializer()

    class Meta:
        model = Favorite
        fields = '__all__'


class EpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Episode
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Season
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['value']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('user', 'text', 'created_at')


class AnimeSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Anime
        fields = '__all__'

    def get_average_rating(self, obj):
        average_rating = obj.ratings.aggregate(Avg('value'))['value__avg']
        return round(average_rating, 1) if average_rating is not None else None


class AnimeListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Anime
        fields = '__all__'

    def get_average_rating(self, obj):
        average_rating = obj.ratings.aggregate(Avg('value'))['value__avg']
        return round(average_rating, 1) if average_rating is not None else None