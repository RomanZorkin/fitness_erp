from django.contrib import admin

from bboard import models


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'expenses_type', 'expense_area')
    list_display_links = ('name', 'expenses_type', 'expense_area')
    search_fields = ('name', 'expenses_type__name', 'expense_area__name')


class ExpensePlanAdmin(admin.ModelAdmin):
    list_display = ('purchase_date', 'expense', 'number', 'price', 'cost')
    list_display_links = ('purchase_date', 'expense')
    search_fields = ('purchase_date', 'expense__name')


admin.site.register(models.Bb, BbAdmin)
admin.site.register(models.Rubric)
admin.site.register(models.ExpensesArea)
admin.site.register(models.ExpensesType)
admin.site.register(models.Expenses, ExpenseAdmin)
admin.site.register(models.ExpensesPlan, ExpensePlanAdmin)
admin.site.register(models.Incomes)
admin.site.register(models.IncomePlan)
