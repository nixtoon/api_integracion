# Generated by Django 5.0.6 on 2024-05-19 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
    ]