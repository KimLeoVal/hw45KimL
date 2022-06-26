from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Task(models.Model):
    title = models.TextField(max_length=30, default='', verbose_name='Задачи')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    status = models.CharField(max_length=40, null=False, blank=False, choices=STATUS_CHOICES,
                              default=STATUS_CHOICES[0][0], verbose_name='Статус')
    date = models.CharField(max_length=40, null=True, blank=True, verbose_name='Дата выполнения')

    def __str__(self):
        return f'id:{self.pk}, description: {self.description}'

    class Meta:
        db_table = "webapp_task"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"