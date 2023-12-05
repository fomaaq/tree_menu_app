from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Наименование меню'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def get_absolute_url(self):
        return reverse('draw_menu', kwargs={'path': self.name})


class MenuItem(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Наименование пункта меню',
        unique=True,
    )
    parent = models.ForeignKey(
        'self',
        verbose_name='Родительский пункт подменю',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    menu = models.ForeignKey(
        Menu,
        verbose_name='Основное меню',
        on_delete=models.CASCADE,
        related_name='menu_itmes',
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
