from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# each mode class in basically a database schema or table with the 
# attributes as the column name



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    # https://www.geeksforgeeks.org/datetimefield-django-models/
    author = models.ForeignKey(User , on_delete = models.CASCADE)
    # the author (User) is the foreign key for this table  and the 
    # on_delete defines what action to take if the user is deleted 

    # magic / special methods
    def __str__(self):
        return self.title
