from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from bboard import config


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Дата публикации',
    )
    rubric = models.ForeignKey(
        'Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика',
    )

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


class ExpensesArea(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    @classmethod
    def get_default_pk(cls):
        area, created = cls.objects.get_or_create(
            name=config.DEFAULT_AREA,
        )
        return area.pk

    class Meta:
        verbose_name_plural = 'Места размещения'
        verbose_name = 'Место размещения'
        ordering = ['name']


class ExpensesType(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Группы расходов'
        verbose_name = 'Группа расходов'
        ordering = ['name']


class Expenses(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    expenses_type = models.ForeignKey(
        'ExpensesType', null=True, on_delete=models.PROTECT, verbose_name='Группа расходов',
    )
    expense_area = models.ForeignKey(
        'ExpensesArea',
        default=ExpensesArea.get_default_pk,
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Местоположение',
    )

    def __str__(self):
        return f'{self.name}/{self.expense_area}'

    class Meta:
        verbose_name_plural = 'Виды расходов'
        verbose_name = 'Вид расходов'
        ordering = ['name']
        unique_together = ('name', 'expense_area')


class ExpensesPlan(models.Model):
    expense = models.ForeignKey(
        'Expenses', null=True, on_delete=models.PROTECT, verbose_name='Вид расходов',
    )
    purchase_date = models.DateField(verbose_name='Дата расхода')
    unit = models.CharField(null=True, max_length=20, verbose_name='Единица измерения')
    number = models.PositiveIntegerField(null=True, verbose_name='Кол-во')
    price = models.FloatField(null=True, verbose_name='Цена')
    cost = models.FloatField(null=True, verbose_name='Стоимость')

    def clean(self):
        errors = {}
        if self.cost != self.number * self.price:
            errors['cost'] = ValidationError(
                'Значение в поле стоимость не равно произведению цены и количества',
            )
        if self.purchase_date < config.BaseDates().start.date():
            errors['purchase_date'] = ValidationError('Дата расходов меньше даты начала проекта')
        if errors:
            raise ValidationError(errors)

    class Meta:
        verbose_name_plural = 'Расходы планируемые'
        verbose_name = 'Расходы'
        ordering = ['purchase_date', 'expense']
        unique_together = ('expense', 'purchase_date')


class Incomes(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Виды доходов'
        verbose_name = 'Вид доходов'
        ordering = ['name']


class IncomePlan(models.Model):
    name = models.ForeignKey(
        'Incomes', null=True, on_delete=models.PROTECT, verbose_name='Вид доходов',
    )
    amount = models.FloatField(null=True, verbose_name='Величина доходов')
    income_date = models.DateField(verbose_name='Дата доходов')

    class Meta:
        verbose_name_plural = 'Доходы планируемые'
        verbose_name = 'Доходы'
        ordering = ['income_date', 'name']


class IncomeFactoryBoard(models.Model):
    name = models.ForeignKey(
        'Incomes', null=True, on_delete=models.PROTECT, verbose_name='Вид доходов',
    )
    lesson_start = models.TimeField(verbose_name='Начало урока')
    lesson_date = models.DateField(verbose_name='Дата урока')
    duration = models.DurationField(verbose_name='Продолжительность')
    lesson_price = models.FloatField(verbose_name='Цена урока')
    filling = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        verbose_name='Наполненность занятия',
    )
    amount = models.FloatField(verbose_name='Стоимость')

    def clean(self):
        errors = {}
        if self.amount != self.filling * self.lesson_price:
            errors['cost'] = ValidationError(
                'Значение в поле стоимость не равно произведению цены и посещения',
            )
        if self.lesson_date < config.BaseDates().start.date():
            errors['purchase_date'] = ValidationError('Дата занятия меньше даты начала проекта')
        if errors:
            raise ValidationError(errors)

    class Meta:
        verbose_name_plural = 'Доходы от бордов'
        verbose_name = 'Доходы'
        ordering = ['name']
