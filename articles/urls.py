from django.urls import path
from .views import *

urlpatterns = [
    path("", ArticleList.as_view(), name="article_list"),
    path("create/", ArticleCreate.as_view(), name="article_create"),
    path("<int:pk>/", ArticleDetail.as_view(), name="article_detail"),
    path("<int:pk>/edit/", ArticleUpdate.as_view(), name="article_edit"),
    path("<int:pk>/delete/", ArticleDelete.as_view(), name="article_delete"),
    path('<int:pk>/like/', ArticleLike.as_view(), name='article_like'),
]