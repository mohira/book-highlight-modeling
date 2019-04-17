import unittest

from src.domain.model.book.page_number import PageNumber
from src.domain.model.quotation.quotation_section import QuotationSection


class TestQuotationSection(unittest.TestCase):
    def test_引用開始ページ番号は引用終了ページ番号を上回ってはいけない(self):
        with self.assertRaises(ValueError):
            QuotationSection(start_page_number=PageNumber(4), last_page_number=PageNumber(3))


if __name__ == "__main__":
    unittest.main()
