# Generated by Django 5.0.4 on 2024-04-10 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='savingaccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=200)),
                ('mobile_number', models.IntegerField(verbose_name=12)),
                ('addhar_number', models.IntegerField(verbose_name=12)),
                ('password', models.CharField(max_length=24)),
                ('Account_type', models.CharField(max_length=20)),
            ],
        ),
    ]
