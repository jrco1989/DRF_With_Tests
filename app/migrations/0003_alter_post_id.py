# Generated by Django 3.2.5 on 2021-07-29 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_post_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='post id'),
        ),
    ]
