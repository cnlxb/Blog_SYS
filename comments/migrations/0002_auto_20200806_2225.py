# Generated by Django 3.0.7 on 2020-08-06 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_time',
            new_name='create_time',
        ),
    ]
