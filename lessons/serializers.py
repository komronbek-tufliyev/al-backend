from rest_framework import serializers
from .models import (
    Category,
    Book,
    BookImage,
    Archive,
    ArchiveImage,
    Topic,
    TopicImage,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    images = BookImageSerializer(many=True, read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

class ArchiveImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchiveImage
        fields = '__all__'

class ArchiveSerializer(serializers.ModelSerializer):   
    images = ArchiveImageSerializer(many=True, read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Archive
        fields = '__all__'

class TopicImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicImage
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    images = TopicImageSerializer(many=True, read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'

# Path: lessons\views.py


