from src.domain.book_id import BookId
from src.domain.page_number import PageNumber
from src.domain.quotation import Quotation
from src.domain.quotation_id import QuotationId
from src.domain.quotation_section import QuotationSection
from src.domain.quotation_statement import QuotationStatement
from src.infrastracture.book_repository_interface import BookRepositoryInterface
from src.infrastracture.quotation_repository_interface import QuotationRepositoryInterface


class QuotationApplicationService:
    def __init__(self, book_repository: BookRepositoryInterface, quotation_repository: QuotationRepositoryInterface):
        self.book_repository = book_repository
        self.quotation_repository = quotation_repository

    def register(self, book_id: int, start_page: int, last_page: int, quotation_statement: str) -> None:
        """新しい引用情報を登録する"""
        # 対象の書籍を取得
        book_id = BookId(book_id)
        book = self.book_repository.find(book_id)

        # 引用オブジェクトを準備
        quotation_id = QuotationId(1)  # TODO: 新規登録時のQuotationIdはよくわからん。。。
        quotation_section = QuotationSection(PageNumber(start_page), PageNumber(last_page))
        quotation = Quotation(quotation_id,
                              book_id,
                              quotation_section,
                              QuotationStatement(quotation_statement))

        if quotation.is_out_of_range(book):
            print("正常に登録できませんでした。ページの範囲が不正です。")
        else:
            self.quotation_repository.add(quotation_id, quotation)

    def update(self, quotation_id: int, start_page: int, last_page: int, quotation_statement: str) -> None:
        """既存の引用情報を更新する"""
        # 対象の書籍を取得
        quotation_id = QuotationId(quotation_id)
        quotation = self.quotation_repository.find(quotation_id)

        # 対象の書籍を取得
        book = self.book_repository.find(quotation.book_id)

        # 引用オブジェクトを準備
        quotation_section = QuotationSection(PageNumber(start_page), PageNumber(last_page))
        quotation = Quotation(quotation.quotation_id,
                              quotation.book_id,
                              quotation_section,
                              QuotationStatement(quotation_statement))

        if quotation.is_out_of_range(book):
            print("正常に登録できませんでした。ページの範囲が不正です。")
        else:
            self.quotation_repository.update(quotation.quotation_id, quotation)
