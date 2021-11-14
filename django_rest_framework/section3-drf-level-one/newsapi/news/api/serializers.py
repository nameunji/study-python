from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from ..models import Article, Journalist


# Use ModelSerializer
class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    # author = serializers.StringRelatedField()  # ForeignKey로 연결된 모델의 __str__ 메소드에서 정의한 string를 리턴
    # author = JournalistSerializer(read_only=True)  # 참조할 모델의 Serializer를 가져와서 사용 (참조할 Serializer가 더 위에 위치해야 참조할 수 있음)

    class Meta:
        model = Article
        exclude = ("id",)
        # field = "__all__"  # we want all the fields of our model.
        # field = ("title", "description", "body")  # we want to choose a couple of fields

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    def validate(self, data):
        """check that description and title are different"""
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and Description must be different from one another!")
        return data

    def validate_title(self, value):
        if len(value) < 30:
            raise serializers.ValidationError("The title has to be at least 30 chars long!")
        return value


class JournalistSerializer(serializers.ModelSerializer):
    # articles = ArticleSerializer(many=True, read_only=True)  # Journalist를 참조한 article들을 가져옴

    # HyperlinkedRelatedField는 ForgeignKey로 연결된 타겟 필드의 API url을 리턴
    articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="article-detail")

    class Meta:
        model = Journalist
        fields = "__all__"


# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         print(validated_data)
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         # validated_data.get(a, b) -> # validated_data의 a라는 키가 있으면 그 키의 값을 가져오고, 없으면 기존 인스턴스의 값을 그대로 사용.
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.publication_date = validated_data.get('publication_date', instance.publication_date)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     def validate(self, data):
#         """check that description and title are different"""
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError("Title and Description must be different from one another!")
#         return data
#
#     def validate_title(self, value):
#         if len(value) < 60:
#             raise serializers.ValidationError("The title has to be at least 60 chars long!")
#         return value