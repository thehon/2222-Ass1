# Generated by Django 3.0.2 on 2020-03-27 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ed', '0005_auto_20200327_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ed.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chats', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ed.Message')),
                ('users', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ed.Profile')),
            ],
        ),
    ]
