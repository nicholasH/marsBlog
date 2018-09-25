from django.contrib import admin

from .models import Blog,Gallery

class PhotoInline(admin.StackedInline):
    model = Gallery
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'post_title','was_published')
    list_filter = ['pub_date']
    search_fields = ['post_title']
    inlines = [PhotoInline]

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.photos.create(image=afile)



admin.site.register(Blog,BlogAdmin)
admin.site.register(Gallery)




