# Generated by Django 5.0.4 on 2024-04-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_alter_savingaccount_a_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='savingaccount',
            name='loan',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='savingaccount',
            name='salary',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='addhar_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='mobile_number',
            field=models.IntegerField(),
        ),
    ]