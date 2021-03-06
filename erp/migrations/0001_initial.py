# Generated by Django 3.0.2 on 2020-01-28 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Erp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'this name already exist'}, max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('ph', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('gender', models.CharField(max_length=10)),
                ('experience', models.IntegerField(default=0)),
                ('hospital_name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
