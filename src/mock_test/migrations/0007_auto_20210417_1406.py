# Generated by Django 3.2 on 2021-04-17 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mock_test', '0006_auto_20210417_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mocktestquestion',
            name='timer',
        ),
        migrations.AddField(
            model_name='mocktest',
            name='timer',
            field=models.CharField(choices=[('30', '30'), ('40', '40'), ('45', '45'), ('60', '60')], default='30', max_length=2),
        ),
    ]
