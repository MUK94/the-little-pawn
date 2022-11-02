from django import template
from blog.models import Post
from django.db.models import Count 

register = template.Library()

@register.inclusion_tag('latest_posts_home.html')
def show_latest_posts_home(count=1):
    latest_posts_home = Post.objects.order_by('-publish')[:count]
    return {
        'latest_posts_home': latest_posts_home
    }

@register.inclusion_tag('home_blog.html')
def show_posts_home(count=6):
    posts_home = Post.objects.order_by('-publish')[:count]
    return {
        'posts_home': posts_home
    }