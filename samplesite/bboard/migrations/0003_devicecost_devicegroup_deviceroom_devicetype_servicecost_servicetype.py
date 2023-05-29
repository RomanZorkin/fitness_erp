# Generated by Django 3.0.2 on 2023-05-27 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20230525_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Группа оборудования',
                'verbose_name_plural': 'Группы оборудования',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DeviceRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Место размещения',
                'verbose_name_plural': 'Места размещения',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Вид оборудования',
                'verbose_name_plural': 'Виды оборудования',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Вид услуги',
                'verbose_name_plural': 'Виды услуг',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ServiceCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField(verbose_name='Стоимость')),
                ('purchase_date', models.DateTimeField(verbose_name='Дата расхода')),
                ('month_num', models.PositiveIntegerField(verbose_name='Номер месяца')),
                ('purchase_day', models.PositiveIntegerField(help_text='Указывается число в которое оказывается услуга, с установленной периодичностью', verbose_name='Число месяца')),
                ('periodicity', models.PositiveIntegerField(help_text='Указывается количество месяцев, через которое повторяется расход', verbose_name='Периодичность')),
                ('periodicity_end', models.DateTimeField(verbose_name='Дата окончания расходов')),
                ('service_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.ServiceType', verbose_name='Вид услуги')),
            ],
            options={
                'verbose_name': 'Расходы на услуги',
                'verbose_name_plural': 'Расходы на услуги',
                'ordering': ['purchase_date'],
            },
        ),
        migrations.CreateModel(
            name='DeviceCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=20, verbose_name='Единица измерения')),
                ('number', models.PositiveIntegerField(verbose_name='Кол-во')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('cost', models.FloatField(verbose_name='Стоимость')),
                ('month_num', models.PositiveIntegerField(verbose_name='Номер месяца')),
                ('purchase_date', models.DateTimeField(verbose_name='Дата расхода')),
                ('device_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.DeviceGroup', verbose_name='Группа оборудования')),
                ('device_room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.DeviceRoom', verbose_name='Место размещения')),
                ('device_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.DeviceType', verbose_name='Вид оборудования')),
            ],
            options={
                'verbose_name': 'Расходы на оборудование',
                'verbose_name_plural': 'Расходы на оборудование',
                'ordering': ['purchase_date'],
            },
        ),
    ]
