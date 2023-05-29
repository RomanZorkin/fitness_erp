# Generated by Django 3.0.2 on 2023-05-29 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0005_auto_20230528_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpensesType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Группа расходов',
                'verbose_name_plural': 'Группы расходов',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='servicecost',
            options={'ordering': ['purchase_date', 'service_type'], 'verbose_name': 'Расходы на услуги', 'verbose_name_plural': 'Расходы на услуги'},
        ),
        migrations.RemoveField(
            model_name='devicecost',
            name='device_group',
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
                ('expenses_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.ExpensesType', verbose_name='Группа расходов')),
            ],
            options={
                'verbose_name': 'Вид оборудования',
                'verbose_name_plural': 'Виды оборудования',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='devicecost',
            name='device_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.Expenses', verbose_name='Вид оборудования'),
        ),
        migrations.AlterField(
            model_name='servicecost',
            name='service_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.Expenses', verbose_name='Вид услуги'),
        ),
    ]
