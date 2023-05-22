# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the main window
    window = QMainWindow()
    window.setWindowTitle("Yoobee Project")
    window.resize(375, 812)

    # Load the stylesheet file
    style_file = QFile(str(Path("style.qss")))
    style_file.open(QFile.ReadOnly | QFile.Text)

    # Apply the stylesheet to the application
    app.setStyleSheet(style_file.readAll().data().decode())

    # Add widgets to the main window
    sidebarButton = QPushButton("Sidebar", window)
    sidebarButton.setGeometry(23, 39, 61, 61)
    sidebarButton.setObjectName("sidebarButton")

    liveButton = QPushButton("Live Chat", window)
    liveButton.setGeometry(289, 39, 61, 61)
    liveButton.setObjectName("liveButton")

    cards = QPushButton("", window)
    cards.setGeometry(25, 175, 325, 200)
    cards.setObjectName("cards")

    plus = QPushButton("+", cards)
    plus.setGeometry(132, 75, 50, 50)
    plus.setObjectName("plusCircle")

    # Load the main window as the root object
    window.show()

    # Code

    sys.exit(app.exec())
