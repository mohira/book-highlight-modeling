import unittest

from src.domain.model.book.book import Book
from src.domain.model.book.book_id import BookId
from src.domain.model.book.page_number import PageNumber
from src.domain.model.book.total_page import TotalPage
from src.domain.model.quotation.quotation import Quotation
from src.domain.model.quotation.quotation_id import QuotationId
from src.domain.model.quotation.quotation_section import QuotationSection
from src.domain.model.quotation.quotation_statement import QuotationStatement


class TestQuotation(unittest.TestCase):
    def test_引用終了ページ番号が書籍の総ページ数を上回ってはならない(self):
        book_id = BookId(1)
        book = Book(book_id, TotalPage(5))

        quotation = Quotation(QuotationId(1),
                              book_id,
                              QuotationSection(PageNumber(6), PageNumber(7)),
                              QuotationStatement("Pythonはプログラミング言語の1つです"))

        self.assertTrue(quotation.is_out_of_range(book))


if __name__ == "__main__":
    unittest.main()
