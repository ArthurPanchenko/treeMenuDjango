from django.db import models
from django.urls import reverse


class Menu(models.Model):
    """Модель для представления меню"""

    title = models.CharField(max_length=63)

    def __str__(self):
        return self.title


class Category(models.Model):
    """Модель для представления элементов меню"""
    
    root = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='nested'
    )
    title = models.CharField(max_length=63)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.title