# Generated by Django 4.2.5 on 2024-01-11 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.CharField(max_length=100),
        ),
    ]
