from django.contrib import admin

# Register your models here.
from blog.models import Category
from blog.models import Post

admin.site.register(Category)
admin.site.register(Post)
