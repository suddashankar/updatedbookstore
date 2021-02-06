from django.contrib import admin
from bookapp.models import Category,Book,Profile
models=[Category,Book,Profile]
admin.site.register(models)
