from rest_framework import serializers
from ..models import Ebook, Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"


class EbookSerializer(serializers.ModelSerializer):
    # 하나의 ebook에는 여러개의 review가 달릴 수 있기 때문에 many=True
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = "__all__"