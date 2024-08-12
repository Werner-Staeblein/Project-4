from django.shortcuts import render
from .models import DividendPosts

# When path is /blog then index is called / database with blog entries(objects) is queried and stored in post_list
# database queried data stored in post_list passed on as context to index.html
# I query for published "objects" or blog entries in database that are status of 1 only

def index(request):
    post_list = DividendPosts.objects.filter(status=1)
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)

