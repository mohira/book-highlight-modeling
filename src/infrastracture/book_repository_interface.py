from abc import ABCMeta, abstractmethod

from src.domain.book import Book
from src.domain.book_id import BookId


class BookRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def find(self, book_id: BookId) -> Book:
        pass
