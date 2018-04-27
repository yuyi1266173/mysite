from django.contrib import admin
from . import models
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'pub_time')
	list_filter = ('pub_time', )

	#fields = ('title', )

	fieldsets = (
		['Main', {'fields': ('title',)}],
		['Advance', {'classes' : ('collapse',) , 
					 'fields' : ('content',)}]
		)

	search_fields = ('title',)

admin.site.register(models.Article, ArticleAdmin)