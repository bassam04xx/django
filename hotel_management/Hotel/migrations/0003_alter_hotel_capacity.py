# Generated by Django 5.1.1 on 2024-10-03 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0002_income_expense_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='capacity',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
