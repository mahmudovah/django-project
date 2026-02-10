from django.db import models

# Iqtiboslar uchun jsdval .

class Quote(models.Model):
    book_name = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book_name} - {self.book_author}"
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=120)
    birthday = models.IntegerField()
    country = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
