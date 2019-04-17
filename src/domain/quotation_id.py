from dataclasses import dataclass


@dataclass(frozen=True)
class QuotationId:
    value: int  # いったん int にしておく
