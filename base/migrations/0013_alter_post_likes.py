# Generated by Django 4.0.4 on 2022-07-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
