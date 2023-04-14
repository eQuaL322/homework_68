from django.db import models
from django.db.models import TextChoices


class EducationChoices(TextChoices):
    COURSES = 'Курсы', 'Курсы'
    SECONDARY = 'Среднее образование', 'Среднее образование'
    HIGHER = 'Высшее образование', 'Высшее образование'
    NONE = 'Без образования', 'Без образования'
class Education(models.Model):
    education_form = models.CharField(
        verbose_name='Вид образования',
        max_length=100,
        null=True,
        blank=False,
        choices=EducationChoices.choices
    )
    education = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Место обучения'
    )
    profession = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Специальность'
    )
    start_date = models.IntegerField(
        verbose_name='Дата начала обучения',
        null=False,
        blank=False
    )
    end_date = models.IntegerField(
        verbose_name='Дата окончания обучения',
        null=False,
        blank=False
    )
    #тут почему то не видит resume
    resume = models.ForeignKey(
        to='resume.Resume',
        related_name='education',
        null=False,
        blank=False,
        verbose_name='Резюме',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.education} - {self.profession}'