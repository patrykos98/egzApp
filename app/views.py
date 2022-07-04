from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework.views import APIView

class Post(APIView):
    def get(self, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, req):
        post=req.data
        serializer=PostSerializer(data=post)
        serializer.save()
        return Response(serializer.data)

    
