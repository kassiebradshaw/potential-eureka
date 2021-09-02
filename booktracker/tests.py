from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Book

# Create your tests here.

class BookTests(TestCase):
    def setUp(self):    
        self.user = get_user_model().objects.create_user(
            username = "tester",
            email = "tester@email.com",
            password = "pass"
        )
        self.book = Book.objects.create(
            title="book",
            author="author",
            summary="summary",
            owner=self.user
        )
    
    def test_model_string_repr(self):
        self.assertEqual(str(self.book), "book")

    def test_model_title(self):
        self.assertEqual(f"{self.book.title}", "book")

    def test_model_author(self):
        self.assertEqual(f"{self.book.author}", "author")

    def test_model_summary(self):
        self.assertEqual(f"{self.book.summary}", "summary")
    
    def test_model_owner(self):
        self.assertEqual(f"{self.book.owner}", "tester@email.com")
    
    def test_book_list_status(self):
        url = reverse('book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_book_details_status(self):
        response = self.client.get(reverse("book_details", args="1"))
        self.assertEqual(response.status_code, 200)
    
    def test_book_list_view(self):
        url = reverse('book_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'book_list.html')
        self.assertTemplateUsed(response, 'base.html')
    
    def test_book_details_view(self):
        url = reverse("book_details", args="1")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'book_details.html')
        self.assertTemplateUsed(response, 'base.html')
    
    def test_create_book_view(self):
        url = reverse("create_book")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'create_book.html')
        self.assertTemplateUsed(response, 'base.html')
    
    def test_update_book_view(self):
        url = reverse("update_book", args="1")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'update_book.html')
        self.assertTemplateUsed(response, 'base.html')
    
    def test_delete_book_view(self):
        url = reverse("delete_book", args="1")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'delete_book.html')
        self.assertTemplateUsed(response, 'base.html')