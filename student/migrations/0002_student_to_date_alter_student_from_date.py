# Generated by Django 4.0.6 on 2022-07-28 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='to_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Leaving Date'),
        ),
        migrations.AlterField(
            model_name='student',
            name='from_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Joining Date'),
        ),
    ]