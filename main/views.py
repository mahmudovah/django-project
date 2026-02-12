from django.shortcuts import render, redirect
from .models import Book, Author

def main_page(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        author_name = request.POST.get("author")

        author = Author.objects.filter(name__icontains=author_name).first()
        if not author:
            author = Author.objects.create(name=author_name, age=1991) 

        book = Book.objects.create(
            title=title,
            author=author
        )
        return redirect("index")


    books = Book.objects.all()
    authors = Author.objects.all()

    return render(request,"index.html", context={"mualliflar":authors, "kitob": books})
