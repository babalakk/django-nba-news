from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets

from .models import Articles
from .serializers import ArticleSerializer


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serial_class = ArticleSerializer

def index(request):
    return HttpResponse("This is Index")

def article(request, article_id):
    arti = Articles.objects.get(id=article_id)
    return HttpResponse(arti.title)
