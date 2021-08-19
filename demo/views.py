from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from demo.models import Comment
from demo.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # фильтрация данных настраивается во ViewSet, либо в settings.py
    # filter_backends = [DjangoFilterBackend, SearchFilter]

    # указываем поля, по которым можно фильтровать записи, например:
    # http://localhost:8000/api/v1/comments/?author=client007&rating>4
    filterset_fields = ['rating', 'author']

    # указываем поля, по которым можно искать записи, например:
    # http://localhost:8000/api/v1/comments/?search=cool
    # чтобы заменить зарезервированное ключевое слово search на другое
    # в настройках REST_FRAMEWORK меняем параметр 'SEARCH_PARAM'
    # http://localhost:8000/api/v1/comments/?q=cool
    search_fields = ['text', 'author']

    # указываем поля, по которым можно упорядочить записи, например:
    # http://localhost:8000/api/v1/comments/?search=bond&ordering=rating, -id
    # чтобы заменить зарезервированное ключевое слово ordering на другое
    # в настройках REST_FRAMEWORK меняем параметр 'ORDERING_PARAM'
    # http://localhost:8000/api/v1/comments/?q=bond&o=rating, -id
    ordering_fields = ['rating', 'author', 'id']

    # для реализации пагинации указываем pagination_class для каждого ViewSet
    # либо в настройках REST_FRAMEWORK указываем параметры 'DEFAULT_PAGINATION_CLASS' и 'PAGE_SIZE
    # http://localhost:8000/api/v1/comments/?page=2
    pagination_class = PageNumberPagination
