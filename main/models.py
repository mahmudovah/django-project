from django.db import models

# Iqtiboslar uchun jadval .

class Quote(models.Model):
    book_name = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book_name} - {self.book_author}"
    
class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.SmallIntegerField()

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name ="Muallif"
        verbose_name_plural = "Mualliflar"

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    description =models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
