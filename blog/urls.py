from django.urls import path

# . means current folder
from . import views

urlpatterns =[
    # path that takes in 3 arguments - path url(/pagename), function you want to run when you go to the url, and if you want to create seperate name for the function that the view can use
    path('', views.post_list, name = 'post _list'),
]