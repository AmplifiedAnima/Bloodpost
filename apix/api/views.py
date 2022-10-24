from rest_framework.decorators import api_view
from rest_framework.response import Response
from apix.models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def getRoutes(request):
    routes=[
        'Get /api',
        'GET /api/posts',
        'GET /post/posts/:id'
        'GET /post/posts/images'
    ]
    return Response(routes)

@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    
    serializer= PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPost(request,pk):
    post = Post.objects.get(id=pk)

    serializer= PostSerializer(posts, many=True)
    
    return Response(serializer.data)