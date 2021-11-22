from rest_framework import serializers
from ..models import Ebook, Review


class ReviewSerializer(serializers.ModelSerializer):

    # StringRelatedField : ForgeignKey로 연결된 모델의 __str__ 메소드에서 정의한 string를 리턴
    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ("ebook", )


class EbookSerializer(serializers.ModelSerializer):
    # 하나의 ebook에는 여러개의 review가 달릴 수 있기 때문에 many=True
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = "__all__"