from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

#veiws is use dot hadnle request and provide a response
# we take the requets information and handle it in some way
# then we fetch the information from the datbase to send it to html page
# finall we creat ea respons eto sen dbakc to the client

def post_list(request):
    # returna a rexponse th e respone will return a request back to the user
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})