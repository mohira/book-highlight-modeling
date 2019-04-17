from dataclasses import dataclass


@dataclass(frozen=True)
class BookId:
    value: int  # いったん int にしておく
