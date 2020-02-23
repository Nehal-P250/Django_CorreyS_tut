"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

"""
so whenever we enter a url it is first checks in this file if it is found then it redirects it to 
the view/urls file  responsible to handle it  else 404

ex. = localhost:8000/blogs/

whenever Jango encounters this include function it chops off whatever
part of the URL has matched up to that point and only sends the remaining 
string to the included URLs module for further processing so in our example
it's already processed this blog part of the URL so it's going to get rid
of that and just send what's remaining to the blog URLs now there's nothing
remaining after we chop off blog so it's just going to send an empty string to blog URLs


"""



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
]
