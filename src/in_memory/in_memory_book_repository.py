from src.domain.model.book.book import Book
from src.domain.model.book.book_id import BookId
from src.domain.model.book.book_repository_interface import BookRepositoryInterface
from src.domain.model.book.total_page import TotalPage


class InMemoryBookRepository(BookRepositoryInterface):
    def find(self, book_id: BookId) -> Book:
        return Book(book_id, TotalPage(10))
