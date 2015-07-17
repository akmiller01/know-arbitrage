from django.db import models
from django.core.urlresolvers import reverse
from redactor.fields import RedactorField
from django.contrib.auth.models import User
from django.utils.html import strip_tags

class Stock(models.Model):
    company = models.CharField(max_length=255, unique=True)
    symbol = models.CharField(max_length=10, unique=True)
    
    class Meta:
        ordering = ['company']
    
    def __str__(self):
        return self.company

class Page(models.Model):
    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    order = models.IntegerField(unique=True)
    content = RedactorField(verbose_name=u'Text')
    published = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def get_absolute_url(self):
        return reverse('blog.views.page',args=[self.slug])
    
    def __unicode__(self):
        return u'%s' % self.title

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,
                            max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True,help_text="Leave blank for auto-fill")
    author = models.ForeignKey(User, null=True, blank=True,editable=False)
    content = RedactorField(verbose_name=u'Text')
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name="posts", related_query_name="post", blank=True)
    stock = models.ManyToManyField(Stock,related_name="posts",related_query_name="post", blank=True)
    imageURL = models.URLField(max_length=255, null=True, blank=True,help_text="Aim for 900x300 resolution")
    
    class Meta:
        ordering = ['-created']
    
    def __unicode__(self):
        return u'%s' % self.title
    
    def get_absolute_url(self):
        return reverse('blog.views.post',args=[self.slug])
    
    def get_comment_url(self):
        return reverse('blog.views.add_comment',args=[self.slug])
    
    def save(self, *args, **kwargs):
        if self.content and (self.description is None or self.description == ""):
            suffix = "..."
            length = 100
            content = strip_tags(self.content)
            self.description = content if len(content) <= length else content[:length-len(suffix)].rsplit(' ', 1)[0] + suffix
        super(Post, self).save(*args, **kwargs)
        
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    author_ip = models.GenericIPAddressField(null=True,blank=True)
    body = models.TextField()
    post = models.ForeignKey(Post)
    validated = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.body[:60])
    
    class Meta:
        ordering = ['-created']
