# Generated by Django 3.1.3 on 2020-11-23 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201123_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='brand',
            field=models.CharField(default=1, max_length=50, verbose_name='Бренд'),
            preserve_default=False,
        ),
    ]
