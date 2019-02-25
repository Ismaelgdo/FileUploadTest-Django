from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse

from .forms import BookForm
from .models import Book
import os
from django.db import models
from django.conf import settings

class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST' :
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        # print(uploaded_file.name)
        # print(uploaded_file.size)
    return render(request, 'upload.html', context)

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
    # passing it to the template
            'books': books
    })


def upload_book(request):
    if request.method == 'POST' :
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })

# \pk means primary key
def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk = pk)
        book.delete()
    return redirect ('book_list')


def update_book(request, pk):
    book_info = get_object_or_404(Book, pk=pk)
    pdf = ''
    cover = ''
    if request.method == 'POST'  :
        try:
            pdf = request.FILES['pdf']
            filelocation = book_info.pdf.path
            os.remove(filelocation)
        except:
            pass


        try:
            cover = request.FILES['cover']
            coverlocation = book_info.cover.path
            os.remove(coverlocation)
        except:
            pass

        title = request.POST.get('title')
        author = request.POST.get('author')
        book_info.title =  title
        book_info.author =  author

        if len(cover) > 0:
            book_info.cover =  cover

        if len(pdf) > 0:
            book_info.pdf =  pdf

        book_info.save()
        # return HttpResponse(filelocation)
        return redirect ('book_list')
    context = {"book_info": book_info}
    return render(request, 'update_book.html', context)

class BookListView(ListView):
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'


class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'
