# Generated by Django 3.2 on 2021-04-17 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mock_test', '0005_mocktestquestion_timer'),
    ]

    operations = [
        migrations.AddField(
            model_name='mocktestquestion',
            name='e',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='mocktestquestion',
            name='c',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='mocktestquestion',
            name='d',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
    ]