# Generated by Django 4.0.4 on 2022-06-19 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_rename_username_post_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
    ]
