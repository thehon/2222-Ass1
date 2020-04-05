# Generated by Django 3.0.4 on 2020-03-26 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ed', '0002_auto_20200326_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ed.Course')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ed.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='members',
            field=models.ManyToManyField(through='ed.MemberShip', to='ed.Profile'),
        ),
    ]