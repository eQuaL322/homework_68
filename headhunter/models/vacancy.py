from django.contrib.auth import get_user_model
from django.db import models

from headhunter.models.resume import VacancyChoices


class Vacancy(models.Model):
    author = models.ForeignKey(
        verbose_name='Работодатель',
        to=get_user_model(),
        related_name='vacancy_author',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        verbose_name = 'Наименование вакансии',
        max_length=100,
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name = 'Описание вакансии',
        max_length=3000,
        null=True,
        blank=True
    )
    salary = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Заработная плата',
        blank=False,
        null=True,
    )
    category = models.CharField(
        verbose_name='Сфера деятельности',
        max_length=30,
        null=False,
        blank=False,
        choices=VacancyChoices.choices
    )
    exp_from = models.IntegerField(
        verbose_name='Стаж от',
        null=False,
        blank=False
    )
    exp_to = models.IntegerField(
        verbose_name='Стаж до',
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата редактирования',
        auto_now=True
    )
    is_hidden = models.BooleanField(
        verbose_name='Скрытое резюме',
        default=False,
        null=False
    )