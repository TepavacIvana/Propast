# Generated by Django 2.2.12 on 2021-09-13 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prodavnica', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telefon',
            old_name='owner',
            new_name='user',
        ),
    ]
