import unittest

from src.domain.total_page import TotalPage


class TestTotalPage(unittest.TestCase):
    def test_総ページ数は正の整数でなければならない(self):
        with self.subTest("'10' は不正な値である"):
            with self.assertRaises(TypeError):
                TotalPage("10")

        with self.subTest("0 は不正な値である"):
            with self.assertRaises(ValueError):
                TotalPage(0)

        with self.subTest("-1 は不正な値である"):
            with self.assertRaises(ValueError):
                TotalPage(-1)


if __name__ == "__main__":
    unittest.main()
