from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Books
from django.urls import reverse_lazy


# Create your views here.

class index(ListView):
    context_object_name = 'books_list'
    model = Books
    template_name = 'Library-App/index.html'


class CreateBooks(CreateView):
    model = Books
    template_name = 'Library-App/add_books.html'
    fields = '__all__'
    success_url = reverse_lazy('library_app:index')


class UpdateBook(UpdateView):
    model = Books
    template_name = 'Library-App/edit_books.html'
    fields = '__all__'
    success_url = reverse_lazy('library_app:index')


class DeleteBook(DeleteView):
    context_object_name = 'books_list'
    model = Books
    template_name = 'Library-App/delete_books.html'
    success_url = reverse_lazy('library_app:index')

