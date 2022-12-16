from django.contrib import admin
from .models import users,student

# Register your models here.
class usersInfoAdmin(admin.ModelAdmin):
    list_display = [ 'username', 'password']
class studentInfoAdmin(admin.ModelAdmin):
    list_display = [ 'student_no', 'student_name','gender','birth','native_p','class_no_id','dept_no_id']
 
admin.site.register(users, usersInfoAdmin)
admin.site.register(student, studentInfoAdmin)