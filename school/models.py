from django.db import models
# from staff.models import *
# Create your models here.

class School_details(models.Model):
    Sid = models.CharField(verbose_name="School ID",primary_key=True, max_length=15) 
    S_name = models.CharField(verbose_name="School Name",max_length=50)
    S_loc = models.CharField(verbose_name="School Address",max_length=150)
    S_logo = models.ImageField(verbose_name="School Logo",upload_to='logo')
    S_moto = models.CharField(verbose_name="School Moto or Description", blank=True, max_length=150)
    S_tel1 = models.CharField(verbose_name="Contact Number1", max_length=15)
    S_tel2 = models.CharField(verbose_name="Contact Number2", blank=True ,max_length=15)
    S_tel3 = models.CharField(verbose_name="Contact Number3", blank=True ,max_length=15)
    class Meta:
        verbose_name = "School Detail"
        db_table = 'school'

class subject(models.Model):
    id = models.CharField(verbose_name="Subject Code",primary_key=True, max_length=10)
    name = models.CharField(verbose_name="Subject Name", max_length=10)


    class Meta:
        verbose_name = "Subject"
        db_table = "subjects"
    def __str__(self):
        return self.name +" "+ self.id
    @property
    def subject_name(self):
        # "Returns the person's full name."
        return '%s %s' % (self.name, self.id)

class classes(models.Model):
    code = models.CharField(verbose_name="Class Code",primary_key=True, max_length=10)
    name = models.CharField(verbose_name="Class Name", max_length=20)
    # CT = models.ForeignKey("staff.Staff", verbose_name="Class Teacher", default=None, on_delete=models.SET_DEFAULT)
    CT = models.OneToOneField("staff.Staff", verbose_name="Class Teacher", default=None ,on_delete=models.SET_DEFAULT)
    sub_teacher = models.ManyToManyField("staff.tss", verbose_name="Subject Teacher", default=None)
    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        db_table = "classes"
    def __str__(self):
        return self.name + " " + self.code

    # def get_absolute_url(self):
    #     return reverse("classes_detail", kwargs={"pk": self.pk})

