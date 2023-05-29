# Generated by Django 3.0.2 on 2023-05-29 07:35

import bboard.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Вид расходов',
                'verbose_name_plural': 'Виды расходов',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ExpensesArea',
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
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ServiceCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField(verbose_name='Дата расхода')),
                ('unit', models.CharField(max_length=20, null=True, verbose_name='Единица измерения')),
                ('number', models.PositiveIntegerField(null=True, verbose_name='Кол-во')),
                ('price', models.FloatField(null=True, verbose_name='Цена')),
                ('cost', models.FloatField(null=True, verbose_name='Стоимость')),
                ('service_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.Expenses', verbose_name='Вид услуги')),
            ],
            options={
                'verbose_name': 'Расходы на услуги',
                'verbose_name_plural': 'Расходы на услуги',
                'ordering': ['purchase_date', 'service_type'],
            },
        ),
        migrations.AddField(
            model_name='expenses',
            name='expense_area',
            field=models.ForeignKey(default=bboard.models.ExpensesArea.get_default_pk, null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.ExpensesArea', verbose_name='Местоположение'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='expenses_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.ExpensesType', verbose_name='Группа расходов'),
        ),
        migrations.CreateModel(
            name='Bb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Товар')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Цена')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
                ('rubric', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.Rubric', verbose_name='Рубрика')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='ExpensesPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField(verbose_name='Дата расхода')),
                ('unit', models.CharField(max_length=20, null=True, verbose_name='Единица измерения')),
                ('number', models.PositiveIntegerField(null=True, verbose_name='Кол-во')),
                ('price', models.FloatField(null=True, verbose_name='Цена')),
                ('cost', models.FloatField(null=True, verbose_name='Стоимость')),
                ('expense', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.Expenses', verbose_name='Вид расходов')),
            ],
            options={
                'verbose_name': 'Расходы на услуги',
                'verbose_name_plural': 'Расходы на услуги',
                'ordering': ['purchase_date', 'expense'],
                'unique_together': {('expense', 'purchase_date')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='expenses',
            unique_together={('name', 'expense_area')},
        ),
    ]
