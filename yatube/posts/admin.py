from django.contrib import admin
from .models import Post, Group

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)

    # # Перечисляем поля, которые должны отображаться в админке
    # list_display = ('title', 'date', 'artist', 'genre') 
    # # Добавляем интерфейс для поиска по тексту постов
    # search_fields = ('title',) 
    # # Добавляем возможность фильтрации по дате
    # list_filter = ('date', 'genre',) 

    # empty_value_display = '-пусто-'