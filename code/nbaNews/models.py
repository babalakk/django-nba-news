from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image_url = models.URLField()
    source_url = models.URLField()
    publish_time = models.DateTimeField(auto_now=False)
