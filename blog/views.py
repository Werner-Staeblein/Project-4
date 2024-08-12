from django.core.paginator import Paginator
from django.shortcuts import render
from .models import DividendPosts

# When path is /blog then index is called / database with blog entries(objects) is queried and stored in post_list
# database queried data stored in post_list passed on as context to index.html
# I query for published "objects" or blog entries in database that are status of 1 only

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
