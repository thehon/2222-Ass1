# Generated by Django 3.0.2 on 2020-03-28 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ed', '0016_discussion'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Is admin'),
        ),
    ]
