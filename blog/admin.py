from django.contrib import admin

from .models import Blog,Gallery

class BlogAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'post_title','was_published')
    list_filter = ['pub_date']
    search_fields = ['post_title']

class galleryAdmin(admin.ModelAdmin):
        inlines = [ Gallery ]


admin.site.register(Blog,BlogAdmin)
admin.site.register(Gallery,galleryAdmin)




