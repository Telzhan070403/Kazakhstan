# Generated by Django 4.0.2 on 2022-04-15 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_firs_name_user_firs_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Person',
        ),
    ]
