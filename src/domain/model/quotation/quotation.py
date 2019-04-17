from dataclasses import dataclass

from src.domain.model.book.book import Book
from src.domain.model.book.book_id import BookId
from src.domain.model.quotation.quotation_id import QuotationId
from src.domain.model.quotation.quotation_section import QuotationSection
from src.domain.model.quotation.quotation_statement import QuotationStatement


@dataclass(frozen=True)
class Quotation:
    """
    - [ ] 引用箇所の完全重複は許可しない？
    - [ ] 引用箇所が部分的に重なる場合は許可しない？
    """
    quotation_id: QuotationId
    book_id: BookId
    quotation_section: QuotationSection
    quotation_statement: QuotationStatement

    def is_out_of_range(self, book: Book) -> bool:
        return self.quotation_section.last_page_number.value > book.total_page.value

    def __str__(self) -> str:
        return f"QuotationId: {self.quotation_id.value}\n" \
            f"BookId: {self.book_id.value}\n" \
            f"QuotationSection: {self.quotation_section}\n" \
            f"QuotationStatement: {self.quotation_statement}\n"
