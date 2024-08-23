from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import DividendPosts, Discussion
from .forms import CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def landing(request):
    return render(request, 'landing.html')  # the view for the landing page

# When path is /blog then index is called / database with blog entries(objects)
# is queried and stored in post_list database queried data stored in post_list
# passed on as context to index.html. I query for published "objects" or blog
# entries in database that are status of 1 only


def blog_index(request):
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

def blogpost_detail(request, slug):
    """
    Show the details of a specific blog post and handle comment submissions.

    **Context Provided:**
    - `post`: The blog post object.
    - `comments`: All approved comments associated with the post.
    - `comment_count`: The number of approved comments.
    - `comment_form`: The form for submitting a new comment.

    **Template:**
    - `blog/single_post.html`: The template displaying the post details and comments.
    """
    # Get the post object, ensuring it has a status of 1 (published)
    queryset = DividendPosts.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    # Get all approved comments related to the post, ordered by creation date
    comments = post.discussions.filter(approved=True).order_by("-comment_date")
    comment_submitted = False

    # Count the number of approved comments
    comment_count = post.discussions.filter(approved=True).count()

    # Handle the comment form submission
    if request.method == "POST":

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.commentator = request.user  # Set the current user as the commentator
            new_comment.article = post  # Associate the comment with the post
            new_comment.save()  # Save the comment

            # Display a success message to the user
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval.'
            )

            # render the post detail page with the message
            return render(request, 'blog/single_post.html', {
                'post': post,
                'comments': comments,
                'comment_submitted': comment_submitted,
            })

    else:
        comment_form = CommentForm()  # Handle GET request

    # Render the template with the provided context
    return render(
        request,
        "blog/single_post.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form
        },
    )

def landing(request):
    return render(request, 'landing.html')  # the view for the landing page

# When path is /blog then index is called / database with blog entries(objects)
# is queried and stored in post_list database queried data stored in post_list
# passed on as context to index.html. I query for published "objects" or blog
# entries in database that are status of 1 only


def blog_index(request):
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

def blogpost_detail(request, slug):
    """
    Show the details of a specific blog post and handle comment submissions.
    """
    # Get the post object, ensuring it has a status of 1 (published)
    queryset = DividendPosts.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    # Get all approved comments related to the post, ordered by creation date
    comments = post.discussions.filter(approved=True).order_by("-comment_date")

    # Count the number of approved comments
    comment_count = comments.count()

    # Handle the comment form submission
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.commentator = request.user  # Set the current user as the commentator
            new_comment.article = post  # Associate the comment with the post
            new_comment.save()  # Save the comment

            # Display a success message to the user
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval.'
            )

            # After submitting, redirect to the same blog post detail page
            return redirect('blogpost_detail', slug=slug)  # Redirect to the detail view

    else:
        comment_form = CommentForm()  # Handle GET request

    # Render the template with the provided context
    return render(
        request,
        "blog/single_post.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """View to allow users to edit their own comments."""
    
    # Fetch the post using the slug
    post = get_object_or_404(DividendPosts, slug=slug)
    
    # Fetch the comment using the comment_id
    comment = get_object_or_404(Discussion, pk=comment_id, commentator=request.user)
    
    # Ensure the user is the author of the comment
    if comment.commentator != request.user:
        messages.error(request, "You do not have permission to edit this comment.")
        return HttpResponseRedirect(reverse('blogpost_detail', args=[slug]))

    # Pre-fill the form with the existing comment for GET requests
    comment_form = CommentForm(instance=comment)

    if request.method == "POST":
        # Populate the form with the new data and the existing comment instance
        comment_form = CommentForm(request.POST, instance=comment)
        
        if comment_form.is_valid():
            updated_comment = comment_form.save(commit=False)
            updated_comment.approved = False  # Reset approval since the comment was edited
            updated_comment.save()
            messages.success(request, "Comment updated successfully and is awaiting approval.")
            return HttpResponseRedirect(reverse('blogpost_detail', args=[slug]))

    return render(request, 'blog/edit_comment.html', {
        'post': post,
        'comment': comment,
        'comment_form': comment_form,
    })

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)
