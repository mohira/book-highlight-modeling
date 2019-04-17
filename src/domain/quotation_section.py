from dataclasses import dataclass

from src.domain.page_number import PageNumber


@dataclass(frozen=True)
class QuotationSection:
    """
    - [ ] 引用開始ページ番号 と 引用終了ページ番号 が一致はありうる(引用ページが1ページの場合)
    - [ ] 引用の性質上、どんなに長くても3ページで収まると思う
    """
    start_page_number: PageNumber
    last_page_number: PageNumber

    def __post_init__(self):
        if self.start_page_number > self.last_page_number:
            raise ValueError("引用開始ページ番号 は 引用終了ページ番号 を上回ってはいけません")

    def __str__(self) -> str:
        return f"p.{self.start_page_number} - p.{self.last_page_number}"
