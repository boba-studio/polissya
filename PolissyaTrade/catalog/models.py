from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Abilities(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Зазначте здібності!",
                            verbose_name="Здібності")

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Зазначте посаду!",
                            verbose_name="Посада")

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100,
                                  help_text="Введіть ім'я!",
                                  verbose_name="Ім'я",)
    last_name = models.CharField(max_length=100,
                                 help_text="Введіть прізвище!",
                                 verbose_name="Прізвище")
    date_of_birth = models.DateField(
        help_text="Введіть дату народження!",
        verbose_name="Дата народження",
        null=True, blank=True)
    date_of_enrollment = models.DateField(
        help_text="Введіть дату приєднання до колективу!",
        verbose_name="Приєднався до нас",
        null=True, blank=True)
    def __str__(self):
        return self.last_name

class Employee(models.Model):
    title = models.CharField(max_length=200,
                             help_text="Введіть коротке ім'я!",
                             verbose_name="Коротке ім'я")
    abilities = models.ManyToManyField('Abilities',
                                  help_text="Оберіть здібності!",
                                  verbose_name="Здібність")
    position = models.ForeignKey('Position',
                                 on_delete=models.CASCADE,
                                 help_text="Оберіть посаду!",
                                 verbose_name="Посада", null=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE,
                                    help_text="Оберіть працівника!",
                                    verbose_name="Працівник", null=True)
    summary = models.TextField(max_length=1000,
                               help_text="Охарактеризуйте працівника!",
                               verbose_name="Характеристика працівника")
    isbn = models.CharField(max_length=13,
                            help_text="Введіть номер телефону!",
                            verbose_name="Номер телевону!")

    def display_abilities(self):
       return ', '.join([ability for ability in str(self.abilities.items())])

    display_abilities.short_description = "Здібності"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('employee-detail', args=[str(self.id)])

class Status(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Введіть статус",
                            verbose_name="Статус")

    def __str__(self):
        return self.name

class Person(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True)
    iin = models.CharField(max_length=20, null=True,
                           help_text="Введіть ідентифікаційний номер!",
                           verbose_name="Ідентифікаційний номер")
    passport = models.CharField(max_length=200,
                                help_text="Введіть дані паспорта!",
                                verbose_name="Паспорт")
    status = models.ForeignKey('Status', on_delete=models.CASCADE,
                               null=True,
                               help_text="Змінити статус",
                               verbose_name="Статус")
    due_back = models.DateField(null=True, blank=True,
                                help_text="Введіть кінець терміну статусу!",
                                verbose_name="Дата закінчення статусу")
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 verbose_name="Замовник",
                                 help_text='Оберіть замовника')
    def __str__(self):
        return '%s %s' % (self.employee, self.status)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False