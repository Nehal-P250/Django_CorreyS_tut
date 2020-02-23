from django.urls import path
from . import views
#  ' . ' indicates current directory and as we want to call the home() present in the views we need to import it 

# simply adding it here won't work , there is a urls file in the main project directory which routes all the url requests
# so the route also needs to be added in the main url file , which is path('blog/',include('blog.urls'))
# so any the below given url will open when we call blog/
# once we add
# some URL patterns then it should no
# longer display the default development
# site like it did before so now it's just
# going to try to match our specific routes


urlpatterns = [
    path('', views.home,name='blog-home'),
    path('about/', views.about,name='blog-about'),
]