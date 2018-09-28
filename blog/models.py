import os

from django.db import models
from django.db.models import ImageField
from django.dispatch import receiver
from django.utils import timezone
from django.utils.datetime_safe import datetime


class Blog(models.Model):
    post_title = models.CharField(max_length=60)
    post_content = models.TextField()

    pub_date = models.DateTimeField('date published')


    def was_published(self):
        now = timezone.now()
        return self.pub_date <= now
    was_published.admin_order_field = 'pub_date'
    was_published.boolean = True
    was_published.short_description = 'Published?'





    def __str__(self):
        return self.post_title


class Gallery(models.Model):
    post = models.ForeignKey(Blog, default=None, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="photos/",verbose_name='Image')


    def __str__(self):
        return str(self.image.url)


@receiver(models.signals.post_delete, sender=Gallery)
def auto_delete_file_on_delete(sender, instance, **kwargs):
        """
        Deletes file from filesystem
        when corresponding `gallery` object is deleted.
        """
        print(instance)
        if instance:
            if os.path.isfile(str(instance)):
                os.remove(str(instance))