# Generated by Django 3.1.3 on 2020-11-25 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201124_1836'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': (('admin_permission', 'admin permission'),), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]