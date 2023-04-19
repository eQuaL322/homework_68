from django.db import models


class Experience(models.Model):
    company = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Компания'
    )
    vacancy = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Должность'
    )
    start_date = models.IntegerField(
        verbose_name='Дата начала работы',
        null=False,
        blank=False
    )
    end_date = models.IntegerField(
        verbose_name='Дата окончания работы',
        null=False,
        blank=False
    )
    resume = models.ForeignKey(
        to='Resume',
        related_name='experience',
        null=False,
        blank=False,
        verbose_name='Резюме',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.company} - {self.vacancy}'
