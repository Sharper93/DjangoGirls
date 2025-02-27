# blogs/ 
# blogs folder

# from python
from datetime import datetime, timezone, timedelta 

# from thrid parties
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# my own creations
from .models import Post # the . in from of model is to let it know to search in current folder for file named models
from .forms import PostForm

# Create your views here.

# POST_LIST.HTML IS A DJANGO TEMPLATE
    
def post_list(request):  # passing request object - could have loads of information such as command line parameters or environment variables
    time_now = datetime.now(timezone(timedelta(hours=-5 )))
    posts = Post.objects.filter(published_date__lte=time_now).order_by('published_date') # render post_list.html -- empty list {} shows we are not passing into any variables  
    return render(request, 'blog/post_list.html', {'posts': posts}) 

def post_detail(request, pk): # web requests for requesst - pk is the url that is defined in url.py file int:pk 
    post = get_object_or_404(Post, pk=pk) # creating post object to get the object or display 404
    return render(request, 'blog/post_detail.html', {'post': post}) # render page and pass post:post into the view as post variable


@login_required # adding decorator for login_required -included with Django
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid(): # if form is valid, save it submit author and date
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.now() # change timezone to datetime.now()
            post.save()
            return redirect('post_detail', pk=post.pk) # redirect does get operations on teh post detail page where Pk = post.pk
    else:
        form = PostForm()# class importing from forms.py
        
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required # adding decorator for login_required -included with Django
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) # get post and existing key for post
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.now() # change timezone to datetime.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def logout_view(request):
    logout(request)
