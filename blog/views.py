from django.shortcuts import render
from django.http import HttpResponse

# home function to handle the trafic comming fomr the home page.
# this function takes a request argument which contains all the necessary
# request details

# within this function we're
# simply going to return what we want the
# user to see when they're sent to this
# route so this is where the logic goes
# for how we want to handle certain routes 


"""
VIDEO 3>

def home(request):
    return HttpResponse('<h1>Blog Home </h1>')

the above code was only returning a simple html response to add a full html response 
and avoid repetative code we use templates .
for that first create template folder in you app i.e here as blog is one of our app
for this project we will create the template folder in the blog and keep all the html
in it
by default django looks for
a templates subdirectory and each of our
installed apps

since django is possibly
going to be looking in other locations
for additional templates we're going to
want to create another subdirectory
within our templates directory with the
same name as our app so that we know
that these are the templates specific to
this blog application now that may sound
a bit redundant to make another
directory and here with the same name as
our current app but that's just the
django convention 


there are a
couple different ways of loading in a
template now one way would be to load
the template in and then render it and
pass that to our HTTP response but that
way is a few more steps than what it
needs to be and Django actually provides
a shortcut that does all of this in just
one piece of code and that shortcut is
in the Django.shortcuts module

now we can return a
rendered template instead of our HTTP response 
(A view always return a HTTPResponse or an exception here the render function in the 
background is actually returning a rendered HttpResponse)


eg-
instead of this 
    return HttpResponse('<h1>Blog Home </h1>')

we can wirte 
    return render(request,'blog/home.html',context)

1st argu = the request parameter

2nd = the tempelate to be renderd ,here we have template directory in the blog directory 
and that template dirctory is again having a blog directory in which the actual html files
need to render are present 
so django will by default search for the template as root and the path which we specify after it 

3rd = (optional) it is a way to pass information into out template



"""


#dummy data
posts = [
     {
         'author':'Nehal',
         'title':'Blog Post 1',
         'content':'First post content',
         'date_posted':'August 27, 2018'
     },
     {
         'author':'Jhon Doe',
         'title':'Blog Post 2',
         'content':'Second post content',
         'date_posted':'August 28, 2018'
     }
     
 ]



def home(request):
    context = {
        'posts':posts,
        'title':'Home'
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html')











