# Generated by Django 3.1 on 2020-08-10 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_categories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
    ]
