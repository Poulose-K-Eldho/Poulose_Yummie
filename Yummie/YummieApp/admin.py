from django.contrib import admin
from .models import FoodCategory,FoodProduct
# Register your models here.
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(FoodCategory,FoodCategoryAdmin)
class FoodProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(FoodProduct, FoodProductAdmin)

