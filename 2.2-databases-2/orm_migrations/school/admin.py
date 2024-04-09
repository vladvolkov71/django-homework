from django.contrib import admin

from .models import Student, Teacher

class StudentInline(admin.TabularInline):
    model = Student.teachers.through
    verbose_name = 'Учитель'
    verbose_name_plural = 'Учителя'
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    list_filter = ('group',)
    inlines = [StudentInline]
    exclude = ('teachers',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    list_filter = ('subject',)