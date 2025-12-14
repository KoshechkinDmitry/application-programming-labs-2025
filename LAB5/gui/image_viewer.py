from pathlib import Path
from typing import Optional, Iterator

from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from iterator import ImagePathIterator


class ImageViewer:
    def __init__(self, label: QLabel) -> None:
        self.label: QLabel = label
        self.iterator: Optional[Iterator[Path]] = None

    def load_source(self, source: Path) -> None:
        """
        Создаёт итератор по папке или CSV-файлу
        """
        self.iterator = iter(ImagePathIterator(source))

    def show_next(self) -> None:
        """
        Отображает следующее изображение
        """
        if self.iterator is None:
            raise RuntimeError("Итератор не инициализирован")

        image_path: Path = next(self.iterator)

        pixmap: QPixmap = QPixmap(str(image_path))
        if pixmap.isNull():
            raise RuntimeError("Не удалось загрузить изображение")

        scaled: QPixmap = pixmap.scaled(
            self.label.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.label.setPixmap(scaled)
