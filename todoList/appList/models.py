from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.task}'

    class Meta:
        ordering = ('-id',)