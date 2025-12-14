from pathlib import Path

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
    QMessageBox,
)
from PySide6.QtCore import Qt

from gui.image_viewer import ImageViewer


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Просмотр датасета изображений")
        self.resize(900, 700)

        # Виджеты
        self.image_label: QLabel = QLabel("Изображение не загружено")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumSize(400, 300)

        self.open_button: QPushButton = QPushButton("Выбрать папку или CSV")
        self.next_button: QPushButton = QPushButton("Следующее изображение")

        # Viewer
        self.viewer: ImageViewer = ImageViewer(self.image_label)

        # Layout
        layout: QVBoxLayout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.open_button)
        layout.addWidget(self.next_button)

        container: QWidget = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Сигналы
        self.open_button.clicked.connect(self.open_source)
        self.next_button.clicked.connect(self.show_next_image)

    def open_source(self) -> None:
        path_str, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите CSV или изображение",
            "",
            "CSV files (*.csv);;All files (*)"
        )

        if not path_str:
            return

        source: Path = Path(path_str)
        if source.is_file() and source.suffix.lower() != ".csv":
            source = source.parent

        try:
            self.viewer.load_source(source)
            QMessageBox.information(self, "Успех", f"Источник загружен:\n{source}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def show_next_image(self) -> None:
        try:
            self.viewer.show_next()
        except StopIteration:
            QMessageBox.information(self, "Конец", "Изображения закончились")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", str(e))
