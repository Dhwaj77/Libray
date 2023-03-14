from django.shortcuts import render, HttpResponse, redirect
from .models import Book
# Create your views here.

def home(request):   # http request
    print(request.method)
    if request.method == "POST":
        print(request.POST)
        bid = request.POST.get("book_id")
        name = request.POST.get("book_name")
        qty = request.POST.get("book_qty")
        price = request.POST.get("book_price")
        author = request.POST.get("book_author")
        is_published = request.POST.get("book_is_published")
        # print(name, qty, price, author, is_published)
        # print(request.POST)

        if is_published == "Yes":
            is_published = True
        else:
            is_published = False
        
        if not bid:
            Book.objects.create(name=name, qty=qty, price=price, author=author, is_published=is_published)
        else:
            book_obj = Book.objects.get(id=bid)
            book_obj.name = name
            book_obj.qty = qty
            book_obj.price = price
            book_obj.author = author
            book_obj.is_published = is_published
            book_obj.save()
        
        
        return redirect("home_page")
        # return HttpResponse("Success")

    elif request.method == "GET":
        # print(request.GET)   # get quary parameters
        return render(request, 'home.html',context={"person_name":"mohini"})

def show_books(request):
    return render(request, "show_books.html",context={"all_books": Book.objects.filter(is_active=True)})


def update_books(request, pk):
    book_obj = Book.objects.get(id=pk)
    return render(request, 'home.html', context={'single_book': book_obj})

def delete_books(request, id):
    Book.objects.get(id=id).delete()
    return redirect("all_books")

def soft_delete_books(request, id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_active = False
    book_obj.save()
    return redirect("all_books")



from django.views.generic.edit import CreateView  
  
class BookCreate(CreateView):  
    model = Book  
  
    fields = '__all__'  