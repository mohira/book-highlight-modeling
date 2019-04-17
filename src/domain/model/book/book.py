from dataclasses import dataclass

from src.domain.model.book.book_id import BookId
from src.domain.model.book.total_page import TotalPage


@dataclass(frozen=True)
class Book:
    book_id: BookId
    total_page: TotalPage
