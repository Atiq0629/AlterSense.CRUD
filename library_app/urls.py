from django.urls import path
from library_app import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

from django.conf.urls import url

app_name = "library_app"

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('add_book', views.CreateBooks.as_view(), name='add_books'),
    path('edit_book/<pk>/', views.UpdateBook.as_view(), name='edit_books'),
    path('delete_book/<pk>/', views.DeleteBook.as_view(), name='delete_books'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
