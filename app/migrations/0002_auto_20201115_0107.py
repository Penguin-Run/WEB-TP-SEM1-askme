# Generated by Django 3.1.2 on 2020-11-15 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='titile',
            new_name='title',
        ),
    ]