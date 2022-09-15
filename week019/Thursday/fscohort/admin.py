from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display =  ("name", "number", "is_active","register_date")
    list_filter = ("is_active", "update_date")

admin.site.register(Student, StudentAdmin)