from django.urls import path
from django.urls.resolvers import URLPattern
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns=[
    path('', BookListView.as_view(), name="book_list"),
    path('<int:pk>', BookDetailView.as_view(), name="book_details"),
    path('new/', BookCreateView.as_view(), name="create_book"),
    path('<int:pk>/update/', BookUpdateView.as_view(), name="update_book"),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name="delete_book"),
]