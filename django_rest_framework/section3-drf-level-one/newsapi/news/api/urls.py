from django.urls import path
from .views import (
    article_list_create_api_view,
    article_detail_api_view,
    ArticleListCreateAPIView,
    ArticleDetailAPIView
)

urlpatterns = [
    # path("articles/", article_list_create_api_view, name="article-list"),
    # path("articles/<int:pk>/", article_detail_api_view, name="article-detail"),
    path("articles/", ArticleListCreateAPIView.as_view(), name="article-list"),
    path("articles/<int:pk>/", ArticleDetailAPIView.as_view(), name="article-detail"),
]