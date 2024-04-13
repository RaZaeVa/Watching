from rest_framework import serializers
from .models import User
from apps.content.serializers import WatchHistorySerializer

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number', 'username', 'password', 'email')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            if field == 'password':
                instance.set_password(value)
            else:
                setattr(instance, field, value)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    latest_watch = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'latest_watch')

    def get_latest_watch(self, user):
        # Получаем последние три аниме для данной категории
        latest_watch = user.watchhistory_set.order_by('-watched_at')[:3]
        # Сериализуем аниме
        serializer = WatchHistorySerializer(latest_watch, many=True)
        return serializer.data