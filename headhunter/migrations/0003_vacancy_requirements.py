# Generated by Django 4.2 on 2023-04-21 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headhunter', '0002_vacancy'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='requirements',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Требования'),
        ),
    ]
