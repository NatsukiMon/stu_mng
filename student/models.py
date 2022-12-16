from django.db import models

# Create your models here.

class users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=8)

class courses(models.Model):
    course_no = models.CharField(max_length=4,primary_key=True,verbose_name="课程号")
    def __str__(self):
        return str(self.course_no)
    course_name = models.CharField(max_length=20,verbose_name="课程名")

class depts(models.Model):
    dept_no = models.CharField(max_length=4,primary_key=True,verbose_name="院系编号")
    dept_name = models.CharField(max_length=20,unique=True,verbose_name="院系名")
    def __str__(self):
        return str(self.dept_no)

class classes(models.Model):
    class_no = models.CharField(max_length=4,primary_key=True,verbose_name="班号")
    def __str__(self):
        return str(self.class_no)
    dept_name = models.ForeignKey(depts,on_delete=models.CASCADE,verbose_name="院系")

class student(models.Model):
    student_no = models.CharField(max_length=8,primary_key=True,verbose_name="学号")
    def __str__(self):
        return str(self.student_no)
    student_name = models.CharField(max_length=10,verbose_name="姓名")
    choices = (('男','男'),('女','女'))
    gender = models.CharField(choices=choices,max_length=2,verbose_name="性别")
    birth = models.DateField(verbose_name="出生年月")
    native_p = models.CharField(max_length=10,verbose_name="籍贯")
    class_no = models.ForeignKey(classes,on_delete=models.CASCADE,verbose_name="班号")
    dept_no = models.ForeignKey(depts,on_delete=models.CASCADE,verbose_name="院系编号")

class change(models.Model): 
    id = models.AutoField(primary_key=True,verbose_name="记录编号")
    student_no = models.ForeignKey(student,on_delete=models.CASCADE,verbose_name="学生学号")
    change_note = models.CharField(max_length=20,verbose_name="变更情况")
    change_time = models.DateTimeField(verbose_name="记录时间")
    change_mage = models.CharField(max_length=50,null=True,verbose_name="详情描述")

class sc(models.Model):
    student_no = models.ForeignKey(student,on_delete=models.CASCADE,verbose_name="学号")
    course_no = models.ForeignKey(courses,on_delete=models.CASCADE,verbose_name="课程号")
    grade = models.FloatField(verbose_name="成绩")
    class Meta:
        unique_together = ("student_no","course_no")

class gradeinfo(models.Model):
    student_no = models.CharField(max_length=8,primary_key=True,verbose_name="学号")
    student_name = models.CharField(max_length=20,verbose_name="姓名")
    #class_no = models.ForeignKey(classes,on_delete=models.CASCADE,verbose_name="班号")
    class_no = models.CharField(max_length=4, verbose_name="班号")
    grade_avg = models.FloatField(null=True,verbose_name="平均成绩")
    class Meta:
        db_table = 'student_grade_view'
        managed=False

class scinfo(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="编号")
    student_no = models.CharField(max_length=8,verbose_name="学号")
    course_no = models.CharField(max_length=4,verbose_name="课程号")
    course_name = models.CharField(max_length=20,verbose_name="课程名")
    grade = models.FloatField(verbose_name="成绩")
    class Meta:
        unique_together = ("student_no","course_no")
        db_table = 'student_sc_view'
        managed=False
