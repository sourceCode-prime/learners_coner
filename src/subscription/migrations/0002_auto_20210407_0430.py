# Generated by Django 3.1.7 on 2021-04-07 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='user_type',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='flw_ref',
            field=models.CharField(max_length=160),
        ),
    ]
