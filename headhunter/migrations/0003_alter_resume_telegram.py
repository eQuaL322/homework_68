# Generated by Django 4.2 on 2023-04-20 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headhunter', '0002_experience_about_alter_resume_vacancy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='telegram',
            field=models.CharField(max_length=200, verbose_name='Telegram'),
        ),
    ]
