from django.db import models
from django.db.models import ImageField
from django.utils import timezone
from django.utils.datetime_safe import datetime


class Blog(models.Model):
    post_title = models.CharField(max_length=60)
    post_content = models.TextField()

    pub_date = models.DateTimeField('date published')


    #not sure if this will work
    image = ImageField(upload_to="photos/", blank=True, null=True)

    def was_published(self):
        now = timezone.now()
        return self.pub_date <= now
    was_published.admin_order_field = 'pub_date'
    was_published.boolean = True
    was_published.short_description = 'Published?'