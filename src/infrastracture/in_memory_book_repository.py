from src.domain.book import Book
from src.domain.book_id import BookId
from src.domain.total_page import TotalPage
from src.infrastracture.book_repository_interface import BookRepositoryInterface


class InMemoryBookRepository(BookRepositoryInterface):
    def find(self, book_id: BookId) -> Book:
        return Book(book_id, TotalPage(10))
