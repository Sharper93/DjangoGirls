# blogs/ 
# blogs folder

# from python
from datetime import datetime, timezone, timedelta 

# from thrid parties
from django.shortcuts import render

# my own creations
from .models import Post # the . in from of model is to let it know to search in current folder for file named models

# Create your views here.

# POST_LIST.HTML IS A DJANGO TEMPLATE
    
def post_list(request):  # passing request object - could have loads of information such as command line parameters or environment variables
    time_now = datetime.now(timezone(timedelta(hours=-5 )))
    posts = Post.objects.filter(published_date__lte=time_now).order_by('published_date') # render post_list.html -- empty list {} shows we are not passing into any variables  
    return render(request, 'blog/post_list.html', {'posts': posts}) 