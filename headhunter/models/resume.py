from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextChoices


class VacancyChoices(TextChoices):
    IT = 'IT', 'IT'
    EDUCATION = 'Образование', 'Образование'
    PR = 'PR', 'PR'
    COMMERCE = 'Торговля', 'Торговля'


class SexChoices(TextChoices):
    MALE = 'Мужчина'
    FEMALE = 'Женщина'


class Resume(models.Model):
    author = models.ForeignKey(
        verbose_name='Соискатель',
        to=get_user_model(),
        related_name='resume_author',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        verbose_name='Наименование резюме',
        null=False,
        blank=False,
        max_length=200
    )
    vacancy = models.CharField(
        verbose_name='Категория',
        max_length=100,
        null=True,
        blank=False,
        choices=VacancyChoices.choices
    )
    sex = models.CharField(
        verbose_name='Пол',
        max_length=100,
        null=True,
        blank=False,
        choices=SexChoices.choices
    )
    about = models.TextField(
        verbose_name='О себе',
        max_length=3000,
        null=True,
        blank=True
    )
    salary = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Уровень дохода',
        blank=False,
        null=True,
    )
    phone = models.CharField(
        verbose_name='Номер телефона',
        null=False,
        blank=False,
        max_length=25
    )
    telegram = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Telegram'
    )
    facebook = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Facebook'
    )
    linkedin = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Linkedin'
    )
    email = models.EmailField(
        verbose_name='Email',
        unique=False,
        null=False,
        blank=False,
    )
    is_hidden = models.BooleanField(
        verbose_name='Скрытое резюме',
        default=False,
        null=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата редактирования',
        auto_now=True
    )

    def __str__(self):
        return f'{self.author} - {self.title}'
