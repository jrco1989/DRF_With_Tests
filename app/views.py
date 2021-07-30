#from django.http import request
from .models import Post
from .serializers import PostSerializer

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
#import json
#from django.views.generic import TemplateView
from rest_framework.generics import GenericAPIView
#from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests


#This function show us all the database posts in the template 'posts_list'
def getPosts(request):
    url= "https://jsonplaceholder.typicode.com/posts"
    response_posts = requests.get(url=url)
    data = response_posts.json()

    for post in data:
        print(post['id'])
        Post(
            userId = post['userId'],
            id= post['id'],
            title= post['title'],
            body= post['body'],
            ).save()
    
    posts = Post.objects.all()
    return render(request,'posts_list.html',{'posts': posts})

#This function allow us consult all the database pots
@api_view(['GET'])
def postList(request):
    queryset = Post.objects.all().order_by('id')
    serializer = PostSerializer(
        queryset,
        many=True
        )

    return Response(serializer.data)

#This function allow us consult the a post detail
@api_view(['GET'])
def postDetail(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(
        post,
        many=False
    )
    return Response(serializer.data)

#@api_view(['POST'])
#@require_http_methods(["GET", "POST"])
'''class postCreate(GenericAPIView):
    
    #allowed_methods = ['POST',]
    allowed_methods = ('POST',)
    #http_method_names = ['get', 'post', 'head']
    def post_create(request):
        serializer = PostSerializer(
            data = request.data
            )
        print("·········")
        print(serializer)

        if serializer.is_valid():
            
            serializer.save()
        return Response(serializer.data)
'''
#This function allow us create a posts
@api_view(['POST'])
def postCreate(request):
        serializer = PostSerializer(
            data = request.data
            )
        print("·········")
        print(serializer)

        if serializer.is_valid():
            
            serializer.save()
        return Response(serializer.data)
#This function allow us update a post
@api_view(['POST'])
def postUpdate(request, pk):    
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(
        instance= post, 
        data = request.data
        )

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#This function allow us delete a post
@api_view(['DELETE'])
def postDelete(request, pk):    
    post = Post.objects.get(id=pk)
    post.delete()
    return Response('deleted')










