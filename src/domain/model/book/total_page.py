from dataclasses import dataclass


@dataclass(frozen=True)
class TotalPage:
    """
    - [ ] 上限は1,000ページくらいにしてもいいと思う
    """
    value: int

    def __post_init__(self):
        if not isinstance(self.value, int):
            raise TypeError(f"Total page must be int, not {type(self.value)}")

        if self.value <= 0:
            raise ValueError(f"Total page must be over 0")
