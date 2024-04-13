from apps.user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Anime(models.Model):
    title = models.CharField(
        max_length=200
    )
    description = models.TextField()
    release_date = models.DateField()
    cover_image = models.ImageField(
        upload_to='anime_covers/',
        default='default_cover.jpeg'
    )
    trailer_link = models.URLField()
    genres = models.ManyToManyField('Genre')
    category = models.ManyToManyField('Category')
    age = models.ManyToManyField('Age')

    def __str__(self):
        return self.title


class Season(models.Model):
    title = models.CharField(
        max_length=200
    )
    anime = models.ForeignKey(
        Anime,
        on_delete=models.CASCADE,
        related_name='seasons'
    )

    def __str__(self):
        return f'{self.anime.title} - {self.title}'


class Episode(models.Model):
    title = models.CharField(
        max_length=200
    )
    episode_number = models.PositiveIntegerField()
    video_link = models.URLField()
    release_date = models.DateField()
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        related_name='episodes'
    )

    def __str__(self):
        return f"{self.episode_number}: {self.title}"


class Genre(models.Model):
    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    anime = models.ForeignKey(
        Anime,
        on_delete=models.CASCADE
    )
    added_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.anime.title}"


class WatchHistory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    episode = models.ForeignKey(
        Episode,
        on_delete=models.CASCADE
    )
    watched_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-watched_at']

    def __str__(self):
        return f"{self.user.username} - {self.episode.title} - {self.watched_at}"


class Rating(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    anime = models.ForeignKey(
        Anime,
        on_delete=models.CASCADE, related_name='ratings'
    )
    value = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ])

    class Meta:
        unique_together = ('user', 'anime')

    def __str__(self):
        return f"{self.user.username} - {self.anime.title}: {self.value}"


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    anime = models.ForeignKey(
        Anime,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.anime.title}"


class Age(models.Model):
    age = models.CharField(max_length=10)

    def __str__(self):
        return self.age