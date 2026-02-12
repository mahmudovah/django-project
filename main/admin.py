from django.contrib import admin
from .models import Quote, Book, Author

admin.site.register(Quote)
admin.site.register(Book)
admin.site.register(Author)