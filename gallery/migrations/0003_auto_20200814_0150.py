# Generated by Django 2.2.2 on 2020-08-13 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20200814_0044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='profession',
            new_name='instagram',
        ),
        migrations.RemoveField(
            model_name='members',
            name='experience',
        ),
        migrations.AddField(
            model_name='members',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
