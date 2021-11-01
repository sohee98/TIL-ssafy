from rest_framework import serializers
from ..models import Actor,Movie,Review


# 1. validation (C, U)      - Write
# 2. 데이터의 구조를 결정 (R)  - Read
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name',)


class ActorSerializer(serializers.ModelSerializer):
    
    # class TrackSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Track
    #         fields = ('id', 'title')
    
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title','overview','release_date','poster_path')

    name = serializers.CharField(min_length=1, max_length=100)
    # tracks = TrackSerializer(many=True, read_only=True)
    movies = MovieSerializer(many=True, read_only=True)
    # album_count = serializers.IntegerField(
    #     source='albums.count',
    #     read_only=True
    # )

    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies')
