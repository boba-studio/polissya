# Generated by Django 5.0.4 on 2024-05-08 07:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_employee_abilities_remove_employee_author_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='borrower',
            field=models.ForeignKey(blank=True, help_text='Оберіть замовника', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Замовник'),
        ),
    ]
