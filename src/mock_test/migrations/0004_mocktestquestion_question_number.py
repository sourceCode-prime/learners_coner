# Generated by Django 3.2 on 2021-04-15 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mock_test', '0003_mocktest_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='mocktestquestion',
            name='question_number',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
