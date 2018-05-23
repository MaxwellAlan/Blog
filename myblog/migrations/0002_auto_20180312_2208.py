# Generated by Django 2.0.2 on 2018-03-12 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_time',)},
        ),
        migrations.AddField(
            model_name='post',
            name='view_times',
            field=models.PositiveIntegerField(default=0),
        ),
    ]