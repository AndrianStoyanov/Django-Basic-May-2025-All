from django.db import models

from posts.choices import LanguageChoices
from posts.validators import BadWordValidator


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(
        validators=[BadWordValidator(
            bad_words=['bad_word_1', 'bad_word_2'],
        )]
    )
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(
        max_length=20,
        choices=LanguageChoices,
        default=LanguageChoices.OTHER,
    )