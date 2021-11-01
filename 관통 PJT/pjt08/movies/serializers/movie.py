from rest_framework import serializers
from ..models import Actor,Movie,Review


class MovieListSerializer(serializers.ModelSerializer):
    # list
    class Meta:
        model = Movie
        fields = ('pk', 'title',)


class MovieSerializer(serializers.ModelSerializer):
   
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('pk', 'name', )

    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('pk', 'title')

    title = serializers.CharField(min_length=2, max_length=100)
    reviews = ReviewSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    actor_pks = serializers.ListField(write_only=True)

    def create(self, validated_data):
        actor_pks = validated_data.pop('actor_pks')
        movie = Movie.objects.create(**validated_data)

        for actor_pk in actor_pks:
            movie.actors.add(actor_pk)
        
        return movie

    def update(self, movie, validated_data):
        actor_pks = validated_data.pop('actor_pks')

        for attr, value in validated_data.items():
            setattr(movie, attr, value)
            movie.save()
        
        # reset relation
        movie.actors.clear()
        
        # set relation
        for actor_pk in actor_pks:
            movie.actors.add(actor_pk)

        return movie


    class Meta:
        model = Movie
        fields = ('id', 'title', 'reviews', 'actors', 'actor_pks')