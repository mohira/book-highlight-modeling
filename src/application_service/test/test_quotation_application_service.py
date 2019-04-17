import unittest

from src.application_service.quotation_application_service import QuotationApplicationService
from src.infrastracture.in_memory_book_repository import InMemoryBookRepository
from src.infrastracture.in_memory_quotation_repository import InMemoryQuotationRepository


class QuotationApplicationServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = QuotationApplicationService(book_repository=InMemoryBookRepository(),
                                                   quotation_repository=InMemoryQuotationRepository())

    def test_新規の引用を登録できる(self):
        self.service.register(book_id=1,
                              start_page=5,
                              last_page=6,
                              quotation_statement="Pythonはプログラミング言語の1つです")

    def test_既存の引用を更新できる(self):
        self.service.update(quotation_id=1,
                            start_page=5,
                            last_page=6,
                            quotation_statement="Rubyはプログラミング言語の1つです")


if __name__ == "__main__":
    unittest.main()
