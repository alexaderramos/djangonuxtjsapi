from django.contrib import admin

# Register your models here.
from .models import Recipe  # add this

# Register your models here.

admin.site.register(Recipe)  # add this
