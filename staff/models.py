from django.db import models
from school.models import *

gender = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]
class family_details(models.Model):
    father_fname = models.CharField(verbose_name="Father's First Name", max_length=15) 
    father_lname = models.CharField(verbose_name="Father's Last Name",max_length=15)
    mother_fname = models.CharField(verbose_name="Mother's First Name",max_length=15)
    mother_lname = models.CharField(verbose_name="Mother's Last Name",max_length=15)
    father_con = models.CharField(verbose_name="Father's Contact Number",max_length=13)
    mother_con = models.CharField(verbose_name="Mother's Contact Number",max_length=13)
    father_alter = models.CharField(verbose_name="Father's Alternate Number",blank=True,max_length=13)
    mother_alter = models.CharField(verbose_name="Mother's Alternate Number",blank=True,max_length=13)
    father_prof = models.CharField(verbose_name="Father's Profession",max_length=50)
    mother_prof = models.CharField(verbose_name="Mother's Profession",max_length=50)
    father_img = models.ImageField(verbose_name="Father's Image",upload_to='image')
    mother_img = models.ImageField(verbose_name="Mother's Image",upload_to='image')
    f_name = models.CharField(verbose_name="First Name",max_length=20)
    l_name = models.CharField(verbose_name="Last Name",max_length=20)
    sex = models.CharField(verbose_name="Sex",max_length=1,choices=gender, default=gender[1])
    dob = models.DateField(verbose_name="Date of Birth", blank = True, null = True,auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=150)
    contact1 = models.CharField(verbose_name="Contact Number", max_length=15)
    contact2 = models.CharField(verbose_name="Alternate Number", max_length=15, blank=True)
    from_date = models.DateTimeField(verbose_name="Joining Date", auto_now=True)
    to_date = models.DateTimeField(verbose_name="Leaving Date", auto_now_add=False, blank=True, null=True)
    class Meta:
        abstract = True

class Staff(family_details):
    school = models.ForeignKey(School_details, on_delete=models.CASCADE)
    id = models.CharField(verbose_name="Staff ID",primary_key=True, max_length=20)  
    salary = models.IntegerField(verbose_name="Salary", blank = True)
    img = models.ImageField(verbose_name=("Staff Image"), upload_to='staff_image',blank=True)
    cv = models.FileField(verbose_name="Upload Resume", max_length=400, upload_to='files')
    hod = models.BooleanField(verbose_name="Is HOD", default=False)
    manager = models.BooleanField(verbose_name="Is manager", default=False)
    subject_speciality = models.ManyToManyField(subject, through='tss',verbose_name="Speciality", default=None)
    class Meta:
        db_table = 'staffs'

    @property
    def full_name(self):
        # "Returns the person's full name."
        return '%s %s' % (self.f_name, self.l_name)
    def __str__(self):
        return self.full_name + " | " + self.id

class tss(models.Model):
    staff = models.ForeignKey("staff.Staff", verbose_name="Teacher" ,on_delete=models.DO_NOTHING)
    sub = models.ForeignKey(subject, verbose_name="Subject" ,on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'teacher_subject_speciality'
        verbose_name_plural = "Teacher Subject Speciality"
        unique_together = (('staff', 'sub'),)

    def __str__(self):
        return self.sub.subject_name + " By " + self.staff.full_name

 