# Generated by Django 2.2.2 on 2020-08-13 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='members',
            options={'verbose_name': 'Members', 'verbose_name_plural': 'Members'},
        ),
        migrations.AlterModelOptions(
            name='photos',
            options={'verbose_name': 'Photos', 'verbose_name_plural': 'Photos'},
        ),
        migrations.AlterModelOptions(
            name='videos',
            options={'verbose_name': 'Videos', 'verbose_name_plural': 'Videos'},
        ),
        migrations.AlterField(
            model_name='photos',
            name='category',
            field=models.CharField(choices=[('wedding', 'wedding'), ('birthday', 'birthday'), ('engagement', 'engagement')], max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='videos',
            name='category',
            field=models.CharField(choices=[('wedding', 'wedding'), ('birthday', 'birthday'), ('engagement', 'engagement')], max_length=11, null=True),
        ),
    ]