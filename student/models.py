from django.db import models
from school.models import *
from staff.models import *
# Create your models here.

class student(family_details):
    stid = models.CharField(verbose_name ="Student ID", primary_key = True ,max_length=20)
    study_in = models.ForeignKey("school.classes", verbose_name="Current Class", default=None ,on_delete=models.SET_DEFAULT)    
    img = models.ImageField(verbose_name=("Student Image"), upload_to='student_image',blank=True)
    class Meta:
        verbose_name_plural = "Students"
        db_table = "student"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})

class ECA(models.Model):
    id = models.CharField(verbose_name="Activity Code",primary_key=True, max_length=10)
    name = models.CharField(verbose_name="Activity Name", max_length=10)
    year = models.DateField(verbose_name="Year of Event", auto_now_add=True)
    s_date = models.DateTimeField(verbose_name="Start Date", auto_now=False, auto_now_add=False)
    e_date = models.DateTimeField(verbose_name="End Date", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name_plural = "Extra Curricular activities"
        db_table = "ECA"
        unique_together = (('name', 'year'),)
    def __str__(self):
        return self.name + "  " + self.year

    # def get_absolute_url(self):
    #     return reverse("ECA_detail", kwargs={"pk": self.pk})

class academic(models.Model):
    year = models.DateField(verbose_name="Year of Result", auto_now_add=True)
    stud = models.ForeignKey(student, verbose_name="Student", on_delete=models.CASCADE)
    cc = models.ForeignKey("school.classes", verbose_name="Current Class", default = None ,on_delete=models.SET_DEFAULT)
    ECA_records = models.ManyToManyField("student.ECA", verbose_name="Extra Curricular activities records", blank=True,default=None)
    marks_eca = models.CharField(verbose_name="Marks In ECA", help_text="Extra Curricular activities (ECA)", blank=True, max_length=3)
    class Meta:
        verbose_name_plural = "Academics Records"
        db_table = "academic_result"
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("academic_detail", kwargs={"pk": self.pk})
