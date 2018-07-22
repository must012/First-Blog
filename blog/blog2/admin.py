from django.contrib import admin
from .models import Post


# Register your models here.

# list_filter-> 인수 컬럼으로 설정된 filter list를 생성

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ('title',)}


admin.site.register(Post, PostAdmin)
