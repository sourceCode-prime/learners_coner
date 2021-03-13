# Generated by Django 3.1.7 on 2021-03-10 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='referral_code',
            field=models.CharField(default='', help_text='Enter referral phone number', max_length=40, null=True),
        ),
    ]
