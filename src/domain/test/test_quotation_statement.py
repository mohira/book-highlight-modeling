import unittest

from src.domain.quotation_statement import QuotationStatement


class TestQuotationStatement(unittest.TestCase):
    def test_引用文は長さ1以上の文字列でなければならない(self):
        with self.subTest("10 は不正な値である"):
            with self.assertRaises(TypeError):
                QuotationStatement(10)

        with self.subTest("'' は不正な値である"):
            with self.assertRaises(ValueError):
                QuotationStatement("")


if __name__ == "__main__":
    unittest.main()
