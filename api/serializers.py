from rest_framework import serializers
from .models import BlogPost,Category
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class BlogPostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    # Shows the category name instead of just the ID
    category_name = serializers.ReadOnlyField(source='category.name')
    slug = serializers.ReadOnlyField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'content', 'category', 'category_name', 'author_name', 'published_date']

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'access', 'refresh')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        validated_data['access'] = str(refresh.access_token)
        validated_data['refresh'] = str(refresh)
        return user
