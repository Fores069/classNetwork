from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ('cat_id', 'pk')
    prepopulated_fields = {"slug": ("description",)}

class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(models.Posts, PostAdmin)
admin.site.register(models.Category, CatAdmin)