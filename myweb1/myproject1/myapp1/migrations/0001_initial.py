# Generated by Django 4.2.4 on 2023-08-30 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sturollno', models.IntegerField(primary_key=True, serialize=False)),
                ('stuname', models.CharField(max_length=60)),
                ('branch', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60)),
            ],
        ),
    ]
