# Generated by Django 3.0.2 on 2023-05-29 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0006_auto_20230529_0153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expenses',
            options={'ordering': ['name'], 'verbose_name': 'Вид расходов', 'verbose_name_plural': 'Виды расходов'},
        ),
    ]