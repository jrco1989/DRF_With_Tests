from django.db import models


class Post(models.Model):

    userId = models.PositiveIntegerField(
        blank=False,
        null=False,
        verbose_name='post user id',
    )

    id = models.PositiveIntegerField(
        primary_key=True,
        blank=False,
        null=False,
        verbose_name='post id',
    )

    title = models.CharField(
        max_length=200,
        null=False,
        verbose_name='post title',
    )

    body = models.TextField(
        null=False,
        verbose_name='post body',
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    def __str__(self):
        return self.title

    