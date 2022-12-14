# Generated by Django 4.0.6 on 2022-07-29 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_alter_classes_ct'),
        ('student', '0003_eca'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='img',
            field=models.ImageField(blank=True, upload_to='student_image', verbose_name='Student Image'),
        ),
        migrations.CreateModel(
            name='academic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField(auto_now_add=True, verbose_name='Year of Result')),
                ('marks_eca', models.CharField(blank=True, help_text='Extra Curricular activities (ECA)', max_length=3, verbose_name='Marks In ECA')),
                ('ECA_records', models.ManyToManyField(blank=True, default=None, to='student.eca', verbose_name='Extra Curricular activities records')),
                ('cc', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='school.classes', verbose_name='Current Class')),
                ('stud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student', verbose_name='Student')),
            ],
            options={
                'verbose_name_plural': 'Academics Result',
                'db_table': 'academic_result',
            },
        ),
    ]
