from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

# Create your views here.

class BookListView(ListView):
    template_name='book_list.html'
    model = Book

class BookDetailView(DetailView):
    template_name='book_details.html'
    model = Book

class BookCreateView(CreateView):
    template_name='create_book.html'
    model = Book
    fields=['title', 'author', 'summary', 'owner']
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    template_name='update_book.html'
    model = Book
    fields=['title', 'author', 'summary', 'owner']

class BookDeleteView(DeleteView):
    template_name='delete_book.html'
    model = Book
    success_url = reverse_lazy('book_list')