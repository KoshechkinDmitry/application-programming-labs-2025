from pathlib import Path
from typing import Iterator, Union
import csv


class ImagePathIterator:
    def __init__(self, source: Union[str, Path]) -> None:
        """
        Итератор по изображениям.
        source: CSV-файл или папка
        """
        self.source: Path = Path(source)
        self._files: list[Path] = []
        self._index: int = 0

        if self.source.is_file() and self.source.suffix == ".csv":
            self._load_from_csv(self.source)
        elif self.source.is_dir():
            self._files = list(self.source.rglob("*.*"))
        else:
            raise ValueError("Источник должен быть CSV-файлом или папкой")

    def _load_from_csv(self, csv_file: Path) -> None:
        with open(csv_file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                path: Path = Path(row["absolute_path"])
                if path.exists():
                    self._files.append(path)

    def __iter__(self) -> Iterator[Path]:
        self._index = 0
        return self

    def __next__(self) -> Path:
        if self._index < len(self._files):
            result: Path = self._files[self._index]
            self._index += 1
            return result
        raise StopIteration
