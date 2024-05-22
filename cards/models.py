from django.db import models
from django.contrib.auth.models import User


class Cards(models.Model):
    front_text = models.CharField(max_length=1000, default='default content', verbose_name='Передний текст')
    back_text = models.CharField(max_length=1000, default='default content', verbose_name='Перевод')
    image = models.ImageField(blank=True, upload_to='images')

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    deck = models.ForeignKey('Deck', on_delete=models.CASCADE, verbose_name='Колоды')

    def __str__(self):
        return f'{self.front_text}'


class Deck(models.Model):
    name = models.CharField(max_length=50, default=False, verbose_name='Название колоды')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец колоды')

    def __str__(self):
        return f'{self.name}'

