from django.urls import path

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'articles',views.ArticleViewset)

urlpatterns = [
    path('',views.index,name='index'),
    path('article/<int:article_id>',views.article,name='article'),
]
