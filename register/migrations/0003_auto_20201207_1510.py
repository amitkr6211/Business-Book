# Generated by Django 2.2.17 on 2020-12-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20201207_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='amitkumar', max_length=100),
        ),
    ]
