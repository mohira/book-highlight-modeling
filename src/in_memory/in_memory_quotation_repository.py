from src.domain.model.book.book_id import BookId
from src.domain.model.book.page_number import PageNumber
from src.domain.model.quotation.quotation import Quotation
from src.domain.model.quotation.quotation_id import QuotationId
from src.domain.model.quotation.quotation_repository_interface import QuotationRepositoryInterface
from src.domain.model.quotation.quotation_section import QuotationSection
from src.domain.model.quotation.quotation_statement import QuotationStatement


class InMemoryQuotationRepository(QuotationRepositoryInterface):
    def find(self, quotation_id: QuotationId) -> Quotation:
        return Quotation(quotation_id,
                         BookId(1),
                         QuotationSection(PageNumber(1), PageNumber(2)),
                         QuotationStatement("Pythonです"))

    def add(self, quotation_id: QuotationId, quotation: Quotation) -> None:
        print("新規の引用を登録しました")
        print(quotation)

    def update(self, quotation_id: QuotationId, quotation: Quotation) -> None:
        print("引用情報を更新しました")
        print(quotation)
