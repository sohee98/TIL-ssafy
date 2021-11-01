from rest_framework import serializers
from ..models import Actor,Movie,Review


class TopReviewListSerializer(serializers.ModelSerializer):

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('pk', 'name',)

    actors = ActorSerializer(many=True)

    class Meta:
        model = Review
        fields = ('pk', 'title', 'actors')


class ReviewSerializer(serializers.ModelSerializer):

    
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = '__all__'

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'

    lyric = serializers.CharField(required=False)
    movie = MovieSerializer(read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    actor_pks = serializers.ListField(write_only=True)

    class Meta:
        model = Review
        fields = ('pk', 'title', 'actors', 'actor_pks', 'movie', 'lyric')
        
    def create(self, validated_data):
        actor_pks = validated_data.pop('actor_pks')
        review = Review.objects.create(**validated_data)
        for actor_pk in actor_pks:
            review.actors.add(actor_pk)
        return review

    def update(self, review, validated_data):
        actor_pks = validated_data.pop('actor_pks')
        for attr, value in validated_data.items():
            setattr(review, attr, value)
        review.save()

        review.actors.clear()
        for actor_pk in actor_pks:
            review.actors.add(actor_pk)
        return review
