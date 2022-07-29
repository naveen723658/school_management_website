# Generated by Django 4.0.6 on 2022-07-28 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
        ('school', '0002_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Class Code')),
                ('name', models.CharField(max_length=20, verbose_name='Class Name')),
                ('CT', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='staff.staff', verbose_name='Class Teacher')),
                ('sub_teacher', models.ManyToManyField(default=None, to='staff.tss', verbose_name='Subject Teacher')),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
                'db_table': 'classes',
            },
        ),
    ]
