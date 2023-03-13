from rest_framework.serializers import HyperlinkedModelSerializer
from books.models import Book

class BookDetailSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ['title', 'author']