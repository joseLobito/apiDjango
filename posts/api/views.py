from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from posts.api.permissions import IsAdminOrReadOnly
from posts.models import *
from posts.api.serializers import *


class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSeriñizer
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    #filterset_fiels = ['category']
    filterset_fields = ['category','category__slug']
