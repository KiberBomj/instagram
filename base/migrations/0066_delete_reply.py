# Generated by Django 4.0.4 on 2022-09-25 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0065_alter_reply_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
