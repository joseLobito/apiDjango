from rest_framework import serializers
from posts.models import *
from users.api.serializer import *
from categories.api.serializers import *

class PostSeriñizer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'miniature', 'created_at', 'published', 'user', 'category']