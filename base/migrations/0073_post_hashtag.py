# Generated by Django 4.0.4 on 2022-09-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0072_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hashtag',
            field=models.ManyToManyField(to='base.hashtag'),
        ),
    ]
