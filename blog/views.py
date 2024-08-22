from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import DividendPosts
from .forms import CommentForm


def landing(request):
    return render(request, 'landing.html')  # the view for the landing page

# When path is /blog then index is called / database with blog entries(objects)
# is queried and stored in post_list database queried data stored in post_list
# passed on as context to index.html. I query for published "objects" or blog
# entries in database that are status of 1 only


def index(request):
    post_list = DividendPosts.objects.filter(status=1)
    paginator = Paginator(post_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'post_list': page_obj.object_list,
        'page_obj': page_obj,
        'is_paginated': paginator.num_pages > 1,
    }
    return render(request, 'blog/index.html', context)


def single_post(request, post_slug):
    """
    Show the details of a specific blog post.

    This view is doing the following:
    -   Look up a blog post based on its unique identifier (the slug).
    -   Find the post from the database that is published (queryset has
        status of 1 which means that only published blog posts are searched
        for in the database)
    -   Pass this post to a page where it will be displayed.

    **Template Used:**
    -   `blog/post_detail.html`: This is the web page where detals of a
        specific clicked post are shown.

    **Context Provided:**
    -   `post`: This contains all the information about this individual
        blog post clicked (title and content).
    -   "context" is what is passed on to the post_detail.html to be displayed
        in this post_detai.html
    """
    queryset = DividendPosts.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=post_slug)

    return render(
        request,
        "blog/single_post.html",
        {"post": post},
    )
   
def blogpost_detail(request, slug):
    post = get_object_or_404(DividendPosts, slug=slug, status=1)  # Ensure the post is published
    comments = post.discussions.filter(approved=True)  # Fetch only approved comments
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = post  # Associate the comment with the post
            new_comment.commentator = request.user  # Associate the comment with the logged-in user
            new_comment.save()
            # Redirect or reload the page to show the new comment
            return redirect('single_post.html', slug=post.slug)

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'blog/single_post.html', context)


def custom_404(request, exception=None):
    return render(request, '404.html', status=404)
