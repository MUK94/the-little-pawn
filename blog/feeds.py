from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatechars
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog')
    description = 'New Posts of my Blog.'

    def items(self):
        return Post.objects.all()[:5]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return truncatechars(item.body, 30)