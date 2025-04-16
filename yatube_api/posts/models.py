from django.contrib.auth import get_user_model
from django.db import models

from .constants import (MAX_GROUP_DESCRIPTION_LENGTH, MAX_GROUP_SLUG_LENGTH,
                        MAX_GROUP_TITLE_LENGTH, MAX_STR_REPRESENTATION_LENGTH)

User = get_user_model()


class Post(models.Model):
    """Модель публикации."""
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField(
        'Фото', upload_to='posts/', null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='posts', verbose_name='Автор')
    group = models.ForeignKey(
        'Group', on_delete=models.SET_NULL, blank=True, null=True,
        related_name='posts', verbose_name='Сообщество')

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return f'{self.text[:MAX_STR_REPRESENTATION_LENGTH]}...'


class Comment(models.Model):
    """Модель комментария к публикации."""
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments', verbose_name='Автор')
    post = models.ForeignKey(
        'Post', on_delete=models.CASCADE,
        related_name='comments', verbose_name='Публикация')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.text[:MAX_STR_REPRESENTATION_LENGTH]}...'


class Follow(models.Model):
    """Модель подписки на автора публикаций."""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='followers', verbose_name='Подписчик')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='following', verbose_name='Автор')

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                name='unique_following',
                fields=('user', 'following')
            ),
        ]

    def __str__(self):
        return f'{self.user} подписан на {self.following}'


class Group(models.Model):
    """Модель группы, к которой может быть прикреплена публикация."""
    title = models.CharField(
        'Название', max_length=MAX_GROUP_TITLE_LENGTH, unique=True)
    slug = models.SlugField(
        'URL', max_length=MAX_GROUP_SLUG_LENGTH, unique=True)
    description = models.TextField(
        'Описание', max_length=MAX_GROUP_DESCRIPTION_LENGTH)

    class Meta:
        verbose_name = 'Сообщество'
        verbose_name_plural = 'Сообщества'

    def __str__(self):
        return f'{self.title[:MAX_STR_REPRESENTATION_LENGTH]}...'
