from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()
    fields = ['username', 'email']

class PostSerializer(serializers.ModelSerializer):
  # username = serializers.ReadOnlyField(source='author.username')
  author_name = serializers.ReadOnlyField(source='author.username')

  # author = AuthorSerializer()
  class Meta:
    model = Post
    fields = [
      'pk','author_name','message','created_at','updated_at','is_public','ip'
    ]
