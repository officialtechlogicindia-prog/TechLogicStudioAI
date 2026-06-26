from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout
)

from app.sidebar import Sidebar
from app.dashboard import Dashboard


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TechLogic Studio AI")
        self.resize(1600, 900)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        self.sidebar = Sidebar()
        self.dashboard = Dashboard()

        layout.addWidget(self.sidebar)
        layout.addWidget(self.dashboard)