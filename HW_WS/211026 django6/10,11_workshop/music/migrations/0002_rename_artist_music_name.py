# Generated by Django 3.2.8 on 2021-10-26 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='artist',
            new_name='name',
        ),
    ]