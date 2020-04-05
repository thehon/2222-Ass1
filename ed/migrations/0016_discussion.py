# Generated by Django 3.0.4 on 2020-03-28 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ed', '0015_group_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ed.Course')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ed.Profile')),
            ],
        ),
    ]
