from .models import Articles

from rest_framework import serializers

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Articles
        fields = ['title','content','image_url','source_url','publish_time']
