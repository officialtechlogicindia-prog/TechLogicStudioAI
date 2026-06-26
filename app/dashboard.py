from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt


class Dashboard(QLabel):

    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)

        self.setText(
            """
<h1>🚀 TechLogic Studio AI</h1>

<p>Welcome Sandeep</p>

Version 1.0
"""
        )