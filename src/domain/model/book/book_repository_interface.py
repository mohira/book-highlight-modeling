from abc import ABCMeta, abstractmethod

from src.domain.model.book.book import Book
from src.domain.model.book.book_id import BookId


class BookRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def find(self, book_id: BookId) -> Book:
        pass
