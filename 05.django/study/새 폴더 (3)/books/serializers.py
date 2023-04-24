from rest_framework import serializers
from .models import Book, Comment

# Q 1.
class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title',)

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields=('book',)
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('book', None)
        return rep

class BookSerializer(serializers.ModelSerializer):
    comment = CommentListSerializer(many=True)
    class Meta:
        model = Book
        fields = '__all__'

# Q 3.
class BookDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentListSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = rep.pop('comment_set', [])
        return rep

