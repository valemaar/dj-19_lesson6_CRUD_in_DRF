from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from demo.models import Comment


'''
# используем простой сериализатор
class CommentSerializer(serializers.Serializer):

    # введем ограничения для полей, это тоже механизм простой валидации
    author = serializers.CharField(max_length=50)

    text = serializers.CharField()
    rating = serializers.IntegerField()

    # производим валидацию (проверку) данных в каком-то поле (атрибуте), например, author
    def validate_author(self, value):
        if 'client' in value:
            raise ValidationError('Error! incorrect author name')
        print(value)
        return value

    # проверим все поля сразу используя метод validate
    def validate(self, attrs):
        if 'cool' in attrs['text'] and attrs['rating'] < 4:
            raise ValidationError('Attention! check your text')
        return attrs

    # реализуем метод для создания объектов
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    # реализуем метод для модификации (обновления) объектов
    def update(self, instance, validated_data):
        pass
'''

# упростим создание сериализатора, используя
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'rating']

    author = serializers.CharField(max_length=50)

    text = serializers.CharField()
    rating = serializers.IntegerField()

    def validate_author(self, value):
        if 'client' in value:
            raise ValidationError('Error! incorrect author name')
        print(value)
        return value

    def validate(self, attrs):
        if 'cool' in attrs['text'] and attrs['rating'] < 4:
            raise ValidationError('Attention! check your text')
        return attrs
