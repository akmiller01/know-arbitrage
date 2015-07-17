from django.contrib import admin
from blog.models import Post
from blog.models import Tag
from blog.models import Page
from blog.models import Stock
from blog.models import Comment

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

def validate_comment(modeladmin, request, queryset):
    queryset.update(validated=True)
validate_comment.short_description = "Validate selected comments"

def unvalidate_comment(modeladmin, request, queryset):
    queryset.update(validated=False)
unvalidate_comment.short_description = "Unvalidate selected comments"

class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]
    #fields display on change list
    list_display = ['post','body','author','author_ip','validated']
    #fields to filter the change list with
    list_filter = ['validated','created','author','author_ip']
    #fields to search in change list
    search_fields = ['author','body']
    #enable the date drill down on change list
    date_hierarchy = 'created'
    actions = [validate_comment,unvalidate_comment]
    save_on_top = True
    
class StockAdmin(admin.ModelAdmin):
    save_on_top = True
    
class PageAdmin(admin.ModelAdmin):
    #fields display on change list
    list_display = ['title','order']
    #fields to filter the change list with
    list_filter = ['published']
    #fields to search in change list
    search_fields = ['title','content']
    #prepopulate the slug from the title
    prepopulated_fields = {"slug":("title",)}
    #enable the save buttons on top of change form
    save_on_top = True

admin.site.register(Post,PostAdmin)

admin.site.register(Tag,TagAdmin)

admin.site.register(Comment, CommentAdmin)

admin.site.register(Stock,StockAdmin)

admin.site.register(Page,PageAdmin)