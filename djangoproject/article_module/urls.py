from django.urls import path
from . import views

urlpatterns = [
    path('article', views.ArticleListView.as_view(), name='article-list'),
    path('cat/<str:category>', views.ArticleListView.as_view(), name='articles_by_category_list'),
    path('article/<slug:slug>/', views.ArticleDetailView.as_view(), name='articles_detail'),
    path('article/add_article_comment', views.add_article_comment, name='add_article_comment')
]
