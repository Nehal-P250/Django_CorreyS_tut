from django.contrib import admin
from .models import Post

# to access the models in the admin page gui we need to register them here 

admin.site.register(Post)