# Generated by Django 4.0.4 on 2022-07-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_post_logo_alter_userprofile_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]