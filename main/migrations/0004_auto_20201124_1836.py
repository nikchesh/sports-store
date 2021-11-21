# Generated by Django 3.1.3 on 2020-11-24 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_task_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='discount',
            field=models.IntegerField(default=0, verbose_name='Скидка'),
        ),
        migrations.AddField(
            model_name='task',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='section',
            field=models.IntegerField(default=0, verbose_name='Номер отдела'),
            preserve_default=False,
        ),
    ]
