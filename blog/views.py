from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from home.models import Partners, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchVector
from .forms import CommentForm, SearchForm
from taggit.models import Tag
from django.db.models import Count


def blog(request, tag_slug=None):
    object_list = Post.objects.all()
    title = 'Blog - The Little Pawn'
    partners = Partners.objects.all()
    links = Link.objects.all()

    # Tags
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag, slug=tag_slug)
        object_list=object_list.filter(tags__in=[tag])

    # Paginator
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
            'page': page,
            'posts': posts,
            'partners': partners,
            'links': links,
            'tag': tag,
            'title': title,
        }
    return render(request, 'blog_list.html', context)

 
def detail(request, slug):
    post = Post.objects.get(slug=slug)
    title = post.title
    partners = Partners.objects.all()
    links = Link.objects.all()
    # List of similar posts
    post_tags_ids = post.tags.values_list('id',flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:3]


    # Comments
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)

            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    context = {
        'post': post, 
        'title': title, 
        'partners': partners,
        'links': links,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'similar_posts': similar_posts
        }
    
    return render(request, 'detail.html', context)

# def post_search(request):
#     form = SearchForm()
#     query = None
#     title = 'Search - The little Pawn'
#     partners = Partners.objects.all()
#     results = []
#     if 'query' in request.GET:
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             results = Post.objects.annotate(
#                 search=SearchVector('title', 'body'), 
#             ).filter(search=query)

#     context = {
#         'form': form,
#         'results': results,
#         'title': title,
#         'partners': partners,
#     }
#     return render(request, 'search.html', context)