from django.core.validators import MaxValueValidator
from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
