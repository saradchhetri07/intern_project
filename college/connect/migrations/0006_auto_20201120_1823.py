# Generated by Django 3.1.3 on 2020-11-20 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0005_auto_20201119_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='tid',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]