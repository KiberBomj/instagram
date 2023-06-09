# Generated by Django 4.0.4 on 2022-07-27 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_remove_userprofile_django_user_model_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
