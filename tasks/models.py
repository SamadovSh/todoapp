from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils import timezone


class TodoItem(models.Model):
    description = models.CharField(max_length=64)
    is_completed = models.BooleanField('Выполнено', default=False)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks')

    def __str__(self):
        return self.description.lower()

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return redirect('tasks/details', args=[self.pk])
