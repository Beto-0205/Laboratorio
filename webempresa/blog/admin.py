from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields =('created', 'updated')

from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

#customize admin panel
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','author','published','post_categories') #<== show information
    ordering = ('author','published')
    #v== search with author
    search_fields = ('title','content','author__username','categories__name')
    date_hierarchy = 'published'#<== filter for time
    list_filter = ('author__username','categories__name')
    #^== filters available 

    def post_categories(self,obj):
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])
    
    post_categories.short_description = 'Categorías'


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)

