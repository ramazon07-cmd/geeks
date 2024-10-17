from django.contrib import admin
from .models import Course, Category, Teacher, Lesson, Video, CustomUser
# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(CustomUser)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
