from django.contrib import admin

from kiwitest.students.models import Student, Group, Log

class StudentInline(admin.TabularInline):
    model = Student
    extra = 1
    
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_group', 'surname', 'name', 'patronymic')
    list_filter = ('student_group', )
    search_fields = ('surname', 'name', 'student_ID')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'head')
    inlines = [StudentInline]

class LogAdmin(admin.ModelAdmin):
    list_display = ('create_date', 'type', 'model', 'log')
    list_filter = ('create_date',)

admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Log, LogAdmin)
  