from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework.views import APIView

class ArticleView(APIView):
    def get(self, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, req):
        article=req.data
        serializer=ArticleSerializer(data=article)
        serializer.save()
        return Response(serializer.data)

class SingleArticleView(APIView):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, post_id):
        data = request.data
        article = Article.objects.get(id=article_id)
        article.title = data["title"]
        article.content = data["content"]
        article.save()
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

class ArticleDeleteView(APIView):
    def post(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response()
