# Generated by Django 4.2.7 on 2023-12-02 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Department',
            new_name='department',
        ),
    ]
