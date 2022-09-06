from django.urls import path
from . views import ArticleView
from . views import SingleArticleView
from . views import ArticleDeleteView

urlpatterns = [
    path('articles/', ArticleView, name='article'),
    path('article/add', ArticleView.as_view(), name='add_article_view'),
    path('article/<int:article_id>/', SingleArticleView.as_view(), name='get_single_article_view'),
    path('article/delete/<int:article_id>/', ArticleDelete.as_view(), name='delete_article'),
    path('article/update/<int:article_id>/', ArticleDetailView.as_view(), name='update_article_view'),
]