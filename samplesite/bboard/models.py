from django.db import models


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


class DeviceRoom(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

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
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    expenses_type =  models.ForeignKey(
        'bboard.ExpensesType', null=True, on_delete=models.PROTECT, verbose_name='Группа расходов',
    )

    class Meta:
        verbose_name_plural = 'Виды расходов'
        verbose_name = 'Вид расходов'
        ordering = ['name']



class ServiceCost(models.Model):
    service_type = models.ForeignKey(
        'bboard.Expenses', null=True, on_delete=models.PROTECT, verbose_name='Вид услуги',
    )
    purchase_date = models.DateField(verbose_name='Дата расхода')
    unit = models.CharField(null=True, max_length=20, verbose_name='Единица измерения')
    number = models.PositiveIntegerField(null=True, verbose_name='Кол-во')
    price = models.FloatField(null=True, verbose_name='Цена')
    cost = models.FloatField(null=True, verbose_name='Стоимость')

    class Meta:
        verbose_name_plural = 'Расходы на услуги'
        verbose_name = 'Расходы на услуги'
        ordering = ['purchase_date', 'service_type']


class DeviceCost(models.Model):
    device_type = models.ForeignKey(
        'Expenses', null=True, on_delete=models.PROTECT, verbose_name='Вид оборудования',
    )    
    device_room = models.ForeignKey(
        'DeviceRoom', null=True, on_delete=models.PROTECT, verbose_name='Место размещения',
    )
    unit = models.CharField(max_length=20, verbose_name='Единица измерения')
    number = models.PositiveIntegerField(verbose_name='Кол-во')
    price = models.FloatField(verbose_name='Цена')
    cost = models.FloatField(verbose_name='Стоимость')    
    purchase_date = models.DateTimeField(verbose_name='Дата расхода')

    class Meta:
        verbose_name_plural = 'Расходы на оборудование'
        verbose_name = 'Расходы на оборудование'
        ordering = ['purchase_date']
