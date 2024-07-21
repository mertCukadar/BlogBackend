from rest_framework import serializers
from .models import BlogPost , Category

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['description','markdown','title','created_at', 'updated_at']

class BlogPostHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id','title','description','created_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']