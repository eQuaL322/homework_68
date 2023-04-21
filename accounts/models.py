from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices


class UserTypeChoice(TextChoices):
    CANDIDATE = 'Соискатель', 'Соискатель'
    COMPANY = 'Компания', 'Компания'


class CustomUser(AbstractUser):
    type = models.CharField(
        verbose_name='type',
        choices=UserTypeChoice.choices,
        default=UserTypeChoice.CANDIDATE,
        blank=False,
        null=False,
    )
    username = models.CharField(
        verbose_name='Username',
        unique=True, null=False,
        blank=False,
        max_length=150,
    )
    first_name = models.CharField(
        verbose_name='First name',
        null=True,
        blank=True,
        max_length=150
    )

    last_name = models.CharField(
        verbose_name='Last name',
        null=True,
        blank=True,
        max_length=150
    )
    email = models.EmailField(
        verbose_name='Email',
        unique=True,
        null=False,
        blank=False,
    )
    avatar = models.ImageField(
        verbose_name='Avatar',
        null=True,
        blank=True,
        upload_to='avatars',
    )
    phone = models.CharField(
        verbose_name='Phone',
        null=False,
        blank=False,
        max_length=100,
    )

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
