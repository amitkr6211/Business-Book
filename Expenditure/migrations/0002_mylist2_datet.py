# Generated by Django 2.2.17 on 2020-12-10 11:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Expenditure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylist2',
            name='datet',
            field=models.DateField(default=datetime.datetime(2020, 12, 10, 11, 33, 43, 597415, tzinfo=utc)),
            preserve_default=False,
        ),
    ]