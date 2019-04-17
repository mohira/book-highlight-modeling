from abc import ABCMeta, abstractmethod

from src.domain.quotation import Quotation
from src.domain.quotation_id import QuotationId


class QuotationRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def find(self, quotation_id: QuotationId) -> Quotation:
        pass

    @abstractmethod
    def add(self, quotation_id: QuotationId, quotation: Quotation) -> None:
        pass

    @abstractmethod
    def update(self, quotation_id: QuotationId, quotation: Quotation) -> None:
        pass
