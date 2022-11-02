from django.urls import path
from blog import views
from .feeds import LatestPostsFeed


urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('tag/<slug:tag_slug>/', views.blog, name='blog_by_tag'),
    path('blog/<slug:slug>/', views.detail, name='detail'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    # path('search/', views.post_search, name='post_search'),
]