# Generated by Django 5.0.4 on 2024-04-12 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='savingaccount',
            name='a_number',
            field=models.IntegerField(default=10000),
        ),
        migrations.AddField(
            model_name='savingaccount',
            name='ocupation',
            field=models.CharField(default='Other', max_length=20),
        ),
    ]
