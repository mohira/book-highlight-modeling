from dataclasses import dataclass

from src.domain.book_id import BookId
from src.domain.total_page import TotalPage


@dataclass(frozen=True)
class Book:
    book_id: BookId
    total_page: TotalPage
