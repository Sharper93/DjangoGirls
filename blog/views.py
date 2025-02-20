# blogs/ 
# blogs folder

from django.shortcuts import render

# Create your views here.

def post_list(request): # django is pasing in requests object
    return render(request, 'blog/post_list.html', {}) # render the post list html  -- {} not passing in variables