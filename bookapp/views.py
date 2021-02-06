from django.http import HttpResponse
from django.shortcuts import render
from bookapp.models import Book,Profile
from django.db.models import Q
from django.core.paginator import Paginator, Page, PageNotAnInteger, EmptyPage


def home(request):
    books = Book.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(books, 12)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'books': books})

def details(request,pk):
    books=Book.objects.get(pk=pk)
    return render(request,'detail.html',{'book':books})

def search(request):
    print("inside search")
    if request.method == 'POST':
        author = request.POST['author']
        # category = request.POST['category']
        # print("author:", author, "category:", category)
        # if category:
        #     print("inside if category:", category)
        #     book = Book.objects.filter(Q(category__name=category))
        #     return render(request, 'search.html', {'books': book, 'author': author})
        # elif author:
        print("inside if author:", author)
        book = Book.objects.filter(Q(author=author))
        return render(request, 'search.html', {'books': book, 'author': author})
    else:
        pass
    return render(request, 'search.html')

def profile(request):
    if request.method=='POST':
        name=request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        address = request.POST['address']
        message = request.POST['message']
        profile_details=Profile.objects.create(name=name,mobile=mobile,email=email,address=address,messege=message)
        profile_details.save()
        return render(request,'profile.html')
    else:
        return render(request,'profile.html')


