from rest_framework import serializers
from . models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('all')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('all')

