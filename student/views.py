import datetime
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import render,HttpResponse,redirect
from student import models

# Create your views here.

def home(request):
   return render(request,"home.html")

def login(request):
   if request.method == 'POST':
      user_name = request.POST.get('username')
      getuser = models.users.objects.filter(username=user_name).first()
      if getuser is None:
         messages.info(request, '没这个人啊！')
         return render(request,"login.html")
      password = request.POST.get('password')
      user_password = getuser.password
      if password == user_password:
         user_obj = models.users.objects.all()
         return redirect('/studentinfo/', locals())
      else:
         messages.info(request, '密码错啦！')
   return render(request,"login.html")

def register(request):
   if request.method == 'POST':
      user_name = request.POST.get('username')
      user_password = request.POST.get('password')

      message = models.users.objects.filter(username=user_name).first()
      if message is None:
         models.users.objects.create(username=user_name, password=user_password) 
      else:
         messages.info(request, '注册过啦，请登录！')
      return  redirect("/login/", locals())
   return render(request,"register.html")

def studentinfo(request):
   student_list = models.student.objects.all()
   c = {"student_list": student_list, }
   return render(request, "studentinfo.html", c)

def gradeinfo(request):
   grade_list = models.gradeinfo.objects.all()
   b = {"grade_list": grade_list, }
   return render(request, "gradeinfo.html",b)

def insert(request):
   if request.method == 'POST':
      studentno = request.POST.get('student_no')
      studentname = request.POST.get('student_name')
      gender = request.POST.get('gender')
      birth= request.POST.get('birth')
      nativep = request.POST.get('native_p')
      classno = request.POST.get('class_no')
      deptno = request.POST.get('dept_no')

      models.student.objects.create(
         student_no = studentno,
         student_name = studentname,
         gender = gender,
         birth = birth,
         native_p = nativep,
         class_no_id = classno,
         dept_no_id = deptno)
      return redirect('/studentinfo/', locals())
   return render(request, 'insert.html')

def insertsc(request):
   studentno = request.GET.get('insert_num')
   stu_obj  = models.student.objects.filter(student_no = studentno).first()
   if  request.method == 'POST':
      courseno = request.POST.get('course_no')
      grade = request.POST.get('grade')
      crs_obj  = models.courses.objects.filter(course_no = courseno).first()
      models.sc.objects.create(
         student_no = stu_obj,
         course_no = crs_obj,
         grade = grade)
      return redirect(("/scinfo/?sc_no="+studentno), locals())
   b = {'insert_num': studentno}
   return render(request, 'insertsc.html',b)

def delete(request):
   delete_num = request.GET.get('delete_num')
   models.student.objects.get(student_no = delete_num).delete()
   messages.info(request, '删除成功！')
   return redirect("/studentinfo/")

def deletesc(request):
   delete_num = request.GET.get('delete_num')
   delete_student = models.scinfo.objects.filter(course_no = delete_num).first()
   models.sc.objects.get(student_no = delete_student.student_no,course_no = delete_num).delete()
   messages.info(request, '删除成功！')
   return redirect("/scinfo/?sc_no="+delete_student.student_no)

def update(request):
   time = timezone.localtime()
   update_num = request.GET.get('update_num')
   update_student = models.student.objects.filter(student_no = update_num).first()
   if request.POST:
      studentname = request.POST.get('student_name')
      birth = request.POST.get('birth')
      nativep = request.POST.get('native_p')
      classno = request.POST.get('class_no')
      deptno = request.POST.get('dept_no')
      changemage = request.POST.get('change_mage')
      models.student.objects.filter(student_no = update_num).update(
         student_name = studentname,
         birth = birth,
         native_p = nativep,
         class_no_id = classno,
         dept_no_id = deptno)
      models.change.objects.create(
         student_no = update_student,
         change_note = "修改",
         change_time = time,
         change_mage = changemage)
      #stu_obj = models.student.objects.all()
      return redirect('/changeinfo/', locals())
   return render(request, "update.html",locals())

def updatesc(request):
   update_num = request.GET.get('update_num')
   sc_no = request.GET.get('sc_no')
   update_student = models.scinfo.objects.filter(student_no = sc_no, course_no = update_num).first()
   if request.POST:
      gradenew = request.POST.get('grade')
      models.sc.objects.filter(student_no = update_student.student_no, course_no = update_student.course_no).update(
         grade = gradenew)
      return redirect(("/scinfo/?sc_no="+update_student.student_no), locals())
   return render(request, "updatesc.html",locals())

def changeinfo(request):
   change_list = models.change.objects.all()
   b = {"change_list": change_list, }
   return render(request, "changeinfo.html",b)


def sc(request):
   sc_no = request.GET.get('sc_no')
   scinfo_list = models.scinfo.objects.filter(student_no = sc_no).all()
   b = {'scinfo_list': scinfo_list, 'sc_no': sc_no}
   return render(request,"scinfo.html",b)

