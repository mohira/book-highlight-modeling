from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PageNumber:
    """
    - [ ] ギリシャ数字でページ数が表現されている場合(目次など)の対応はどうする？ int じゃなくて str じゃないか？
    """
    value: int

    def __post_init__(self):
        if not isinstance(self.value, int):
            raise TypeError(f"Page number must be int, not {type(self.value)}")

        if self.value <= 0:
            raise ValueError(f"Page number must be over 0")

    def __gt__(self, other: PageNumber) -> bool:
        return self.value > other.value

    def __str__(self) -> str:
        return str(self.value)
