# Generated by Django 2.2.17 on 2020-12-10 14:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Expenditure', '0003_remove_mylist2_datet'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylist2',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
