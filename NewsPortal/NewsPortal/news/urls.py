from django.urls import path
from .views import *


urlpatterns = [
    path('news/', PostList.as_view(), name='news'),
    path('news/<int:pk>', PostDetail.as_view(), name='news_detail'),
    path('news/create/', PostCreate.as_view(), name='news_create'),
    path('news/<int:pk>/update/', PostUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),

    path('article/', PostList.as_view(), name='news'),
    path('article/<int:pk>', PostDetail.as_view(), name='news_detail'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),

    path('subscriptions/', subscriptions, name='subscriptions'),
]