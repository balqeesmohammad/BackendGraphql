# Generated by Django 3.0.6 on 2020-05-09 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_auto_20200509_0534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album_name',
            new_name='albumname',
        ),
    ]
