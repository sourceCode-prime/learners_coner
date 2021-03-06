# Generated by Django 3.1.7 on 2021-03-10 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('podcast', models.FileField(default='', upload_to='%Y%M%d')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
