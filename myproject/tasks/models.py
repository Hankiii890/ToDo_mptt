from django.db import models

from mptt.models import TreeForeignKey, MPTTModel


class Tasks(MPTTModel):
    title = models.CharField(255)
    description = models.TextField(blank=True, null=True)  # Поле может быть пустым при отправке в форму джанго / в БД это поле может быть пустым
    due_date = models.DateTimeField(blank=True, null=True)  # Поле срока выполнения задачи
    is_completed = models.BooleanField(default=False)

    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subtask')

    class MPTTMeta:
        order_selection_by = ['']  # Упорядочиваем по срокам выполненности

    def __str__(self):
        return self.title
