# Generated by Django 4.2.5 on 2024-01-11 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapi', '0002_alter_employee_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]