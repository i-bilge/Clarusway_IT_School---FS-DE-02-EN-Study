from time import timezone
from django.contrib import admin
from .models import Review, Student, Category
from django.utils import timezone
from django.utils.safestring import mark_safe

# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    classes = ('collapse',)

class StudentAdmin(admin.ModelAdmin):
    list_display =  ("name", "number", "is_active","register_date", "added_since", "bring_img_to_list")
    actions = ("is_active",)
    list_filter = ("is_active", "update_date")
    ordering = ("name", "update_date")
    search_fields = ("name", "about")
    list_editable = ("is_active",)
    list_per_page = 15
    prepopulated_fields = {'slug': ('about',)}
    date_hierarchy = "register_date"
    inlines = (ReviewInline,)

    fieldsets = (
        (None, {
            "fields": (
                ('name','number'),'is_active'
            )
        }),
        ('Advenced Options', {
            "fields": ('about', 'slug', 'categories', 'product_img',),
            "classes": ('collapse',),
            "description": "You can use this action for optional settings"
        })
    )
    filter_horizontal = ("categories",)

    def bring_img_to_list(self, obj):
        if obj.student_img:
            return mark_safe(f"<img src={obj.student_img.url} width=50 height=50></img>")
        return mark_safe("*******")
    bring_img_to_list.short_description = "product_image"

    def is_active(self, request, queryset):
        count = queryset.update(is_active=True)
        self.message_user(request, f"{count} students activated")

    is_active.short_description = 'activate selected students'

    def added_since(self, student):
        difference = timezone.now() - student.register_date
        return difference.days

admin.site.register(Student, StudentAdmin)
admin.site.register(Review)
admin.site.register(Category)