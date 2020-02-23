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




def home(request):
    return HttpResponse('<h1>Blog Home </h1>')


def about(request):
    return HttpResponse('<h1>Blog About </h1>')











