# Generated by Django 3.1.7 on 2021-03-07 16:59

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classroom', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=70, unique=True)),
                ('note', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('term', models.IntegerField(default=1)),
                ('week', models.PositiveIntegerField(help_text='lecture week')),
                ('timestamp', models.DateField(auto_now=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.class')),
                ('subject', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='classroom.subject')),
            ],
        ),
    ]
