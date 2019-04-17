import unittest

from src.domain.model.book.page_number import PageNumber


class TestPageNumber(unittest.TestCase):
    def test_ページ番号は正の整数でなければならない(self):
        with self.subTest("'10' は不正な値である"):
            with self.assertRaises(TypeError):
                PageNumber("10")

        with self.subTest("0 は不正な値である"):
            with self.assertRaises(ValueError):
                PageNumber(0)

        with self.subTest("-1 は不正な値である"):
            with self.assertRaises(ValueError):
                PageNumber(-1)

    def test_ページ番号は大小比較ができる(self):
        with self.subTest("4ページ は 3ページ より大きい"):
            self.assertTrue(PageNumber(4) > PageNumber(3))

        with self.subTest("3ページ は 4ページ より小さい"):
            self.assertTrue(PageNumber(3) < PageNumber(4))


if __name__ == "__main__":
    unittest.main()
