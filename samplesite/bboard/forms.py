from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from bboard import config, models


class BbForm(forms.ModelForm):
    class Meta:
        model = models.Bb
        fields = ('title', 'content', 'price', 'rubric')


class AddDevice(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddDevice, self).__init__(*args, **kwargs)
        self.fields['expense'].choices = [
            (row.pk, f'{row.name} : {row.expense_area}') for row in models.Expenses.objects.filter(
                expenses_type=config.ExpenseType().device,
            )
        ]

    class Meta:
        model = models.ExpensesPlan
        fields = ('expense', 'purchase_date', 'unit', 'number', 'price', 'cost')
        widgets = {
            'purchase_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'},
            ),
        }


class AddService(forms.Form):

    def __init__(self, *args, **kwargs):
        super(AddService, self).__init__(*args, **kwargs)
        self.fields['service_type'].choices = [
            (row.pk, f'{row.name} : {row.expense_area}') for row in models.Expenses.objects.filter(
                expenses_type=config.ExpenseType().service,
            )
        ]

    def clean(self):
        cleaned_data = super().clean()
        end_period = cleaned_data.get('periodicity_end')
        start_period = cleaned_data.get('periodicity_start')
        periodicity = int(cleaned_data.get('periodicity'))
        start_project = config.BaseDates().start.date()
        count_cost = cleaned_data.get('price') * cleaned_data.get('number')
        cost = cleaned_data.get('cost')
        new_date = date(
            year=start_period.year,
            month=start_period.month,
            day=int(cleaned_data.get('purchase_day')),
        )
        if end_period <= start_period:
            raise ValidationError(
                f'Дата окончания расходов меньше или равна дате начала расходов {start_period}'
            )
        if start_period < start_project:
            raise ValidationError(
                f'Дата начала расходов меньше даты начала проекта {start_project}'
            )
        if periodicity == 0:
            if new_date < start_period:
                raise ValidationError(
                    f'Число расходов {new_date} ранее даты начала расходов {start_project}'
                )
        if cost != count_cost:
            raise ValidationError(
                'Значение в поле стоимость не равно произведению цены и количества',
            )
        return cleaned_data

    service_type = forms.ChoiceField(label='Вид услуги')
    purchase_day = forms.ChoiceField(
        choices=[(day, day) for day in range(1, 32)],
        label='Число месяца',
    )
    periodicity = forms.ChoiceField(choices=config.get_period_list(), label='Периодичность')
    periodicity_start = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'},
        ),
        label='Дата начала расходов'
    )
    periodicity_end = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'},
        ),
        label='Дата окончания расходов',
    )
    unit = forms.CharField(max_length=10, label='Единица измерения')
    number = forms.IntegerField(max_value=10000000, label='Кол-во')
    price = forms.FloatField(max_value=10000000, label='Цена')
    cost = forms.FloatField(max_value=10000000, label='Стоимость')
