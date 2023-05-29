# Generated by Django 3.0.2 on 2023-05-28 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_devicecost_devicegroup_deviceroom_devicetype_servicecost_servicetype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicecost',
            name='month_num',
        ),
        migrations.RemoveField(
            model_name='servicecost',
            name='month_num',
        ),
        migrations.RemoveField(
            model_name='servicecost',
            name='periodicity',
        ),
        migrations.RemoveField(
            model_name='servicecost',
            name='periodicity_end',
        ),
        migrations.RemoveField(
            model_name='servicecost',
            name='purchase_day',
        ),
        migrations.AddField(
            model_name='servicecost',
            name='number',
            field=models.PositiveIntegerField(null=True, verbose_name='Кол-во'),
        ),
        migrations.AddField(
            model_name='servicecost',
            name='price',
            field=models.FloatField(null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='servicecost',
            name='unit',
            field=models.CharField(max_length=20, null=True, verbose_name='Единица измерения'),
        ),
        migrations.AlterField(
            model_name='servicecost',
            name='cost',
            field=models.FloatField(null=True, verbose_name='Стоимость'),
        ),
    ]
