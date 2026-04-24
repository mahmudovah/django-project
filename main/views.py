from django.shortcuts import render, redirect
from .models import Book, Author

def main_page(request):
    if request.method == 'POST':

            # kitob qo'shish
        title = request.POST.get("title")
        author_name = request.POST.get("author")

        author = Author.objects.filter(name__icontains=author_name).first()
        if not author:
            author = Author.objects.create(name=author_name, age=1991) 

        book = Book.objects.create(
            title=title,
            author=author
        )

    elif request.method == 'POST':

            #author qo'shish
        name = request.POST.get("name")
        age = request.POST.get('age')
       
        autho = Author.objects.create(name=name,age=age)
    

        return redirect("index")


    books = Book.objects.all()
    authors = Author.objects.all()

    return render(request,"index.html", context={"mualliflar":authors, "kitob": books})
