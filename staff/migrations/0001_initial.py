# Generated by Django 4.0.6 on 2022-07-28 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0002_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('father_fname', models.CharField(max_length=15, verbose_name="Father's First Name")),
                ('father_lname', models.CharField(max_length=15, verbose_name="Father's Last Name")),
                ('mother_fname', models.CharField(max_length=15, verbose_name="Mother's First Name")),
                ('mother_lname', models.CharField(max_length=15, verbose_name="Mother's Last Name")),
                ('father_con', models.CharField(max_length=13, verbose_name="Father's Contact Number")),
                ('mother_con', models.CharField(max_length=13, verbose_name="Mother's Contact Number")),
                ('father_alter', models.CharField(blank=True, max_length=13, verbose_name="Father's Alternate Number")),
                ('mother_alter', models.CharField(blank=True, max_length=13, verbose_name="Mother's Alternate Number")),
                ('father_prof', models.CharField(max_length=50, verbose_name="Father's Profession")),
                ('mother_prof', models.CharField(max_length=50, verbose_name="Mother's Profession")),
                ('father_img', models.ImageField(upload_to='image', verbose_name="Father's Image")),
                ('mother_img', models.ImageField(upload_to='image', verbose_name="Mother's Image")),
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Staff ID')),
                ('f_name', models.CharField(max_length=20, verbose_name='First Name')),
                ('l_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default=('F', 'Female'), max_length=1, verbose_name='Sex')),
                ('contact1', models.CharField(max_length=15, verbose_name='Contact Number')),
                ('contact2', models.CharField(blank=True, max_length=15, verbose_name='Alternate Number')),
                ('address', models.CharField(max_length=150)),
                ('salary', models.IntegerField(blank=True, verbose_name='Salary')),
                ('img', models.ImageField(blank=True, upload_to='staff_image', verbose_name='Staff Image')),
                ('from_date', models.DateTimeField(auto_now=True, verbose_name='Date From')),
                ('to_date', models.DateTimeField(blank=True, null=True, verbose_name='Date To')),
                ('cv', models.FileField(max_length=400, upload_to='files', verbose_name='Upload Resume')),
                ('hod', models.BooleanField(default=False, verbose_name='Is HOD')),
                ('manager', models.BooleanField(default=False, verbose_name='Is manager')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school_details')),
            ],
            options={
                'db_table': 'staffs',
            },
        ),
        migrations.CreateModel(
            name='tss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='staff.staff', verbose_name='Teacher')),
                ('sub', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.subject', verbose_name='Subject')),
            ],
            options={
                'verbose_name_plural': 'Teacher Subject Speciality',
                'db_table': 'teacher_subject_speciality',
                'unique_together': {('staff', 'sub')},
            },
        ),
        migrations.AddField(
            model_name='staff',
            name='subject_speciality',
            field=models.ManyToManyField(default=None, through='staff.tss', to='school.subject', verbose_name='Speciality'),
        ),
    ]
