# Generated by Django 4.2 on 2023-04-19 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=150, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=150, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='type',
            field=models.CharField(choices=[('Соискатель', 'Соискатель'), ('Компания', 'Компания')], default='Соискатель', verbose_name='type'),
        ),
    ]