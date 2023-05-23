from django.contrib.auth.models import AbstractUser
from django.db import models


class UserFoodgram(AbstractUser):
    email = models.EmailField(
        max_length=254,
        blank=False
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Польльзователи'

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        UserFoodgram,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
        help_text='Подписчик',
    )
    author = models.ForeignKey(
        UserFoodgram,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
        help_text='Автор',
    )

    class Meta:
        unique_together = (
            'user',
            'author',
        )
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
