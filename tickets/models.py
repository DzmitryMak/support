from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Ticket(models.Model):
    title = models.CharField(verbose_name='тема', max_length=64)
    content = models.TextField(verbose_name='Описание', blank=True)
    author = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    STATUS_CHOISES = (
        ('not resolved', 'не решен'),
        ('resolved', 'решен'),
        ('frozen', 'заморожен'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOISES, default='not resolved')

