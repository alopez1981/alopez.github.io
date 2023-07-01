# Generated by Django 4.2.1 on 2023-06-11 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('mobile', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('notas', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
