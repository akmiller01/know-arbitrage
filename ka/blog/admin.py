from django.contrib import admin
from blog.models import Post
from blog.models import Tag
from blog.models import About
from blog.models import Stock

class PostAdmin(admin.ModelAdmin):
    #fields display on change list
    list_display = ['title','description','author']
    #fields to filter the change list with
    list_filter = ['published','created','author']
    #fields to search in change list
    search_fields = ['title','description','content']
    #enable the date drill down on change list
    date_hierarchy = 'created'
    #enable the save buttons on top of change form
    save_on_top = True
    #prepopulate the slug from the title
    prepopulated_fields = {"slug":("title",)}
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
    
class TagAdmin(admin.ModelAdmin):
    #enable the save buttons on top of change form
    save_on_top = True
    #prepopulate the slug from the title
    prepopulated_fields = {"slug":("name",)}
    
class StockAdmin(admin.ModelAdmin):
    save_on_top = True
    
class AboutAdmin(admin.ModelAdmin):
    save_on_top = True

admin.site.register(Post,PostAdmin)

admin.site.register(Tag,TagAdmin)

admin.site.register(Stock,StockAdmin)

admin.site.register(About,AboutAdmin)