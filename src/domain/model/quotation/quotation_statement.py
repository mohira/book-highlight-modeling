from dataclasses import dataclass


@dataclass(frozen=True)
class QuotationStatement:
    """
    - [ ] 引用は文字列のみに制限するかどうかはどうしよう？
        - [ ] 図や数式なども引用したい場合は別オブジェクトになるかな？
    """

    value: str

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise TypeError(f"Quotation statement must be str, not {type(self.value)}")

        if len(self.value) <= 0:
            raise ValueError(f"Quotation statement length must be over 0")

    def __str__(self) -> str:
        return self.value
