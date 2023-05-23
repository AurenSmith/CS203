# this Python file uses the following encoding: utf-8
import sys
from pathlib import Path

from PySide6.QtCore import QFile, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFrame, QVBoxLayout, QHBoxLayout, QMenu

import variables as var

if __name__ == "__main__":    
    # create application
    app = QApplication(sys.argv)

    # create the main window
    window = QMainWindow()
    window.setWindowTitle("Yoobee Project")
    window.resize(375, 812)

    # load the stylesheet file
    style_file = QFile(str(Path("style.qss")))
    style_file.open(QFile.ReadOnly | QFile.Text)

    # apply the stylesheet to the application
    app.setStyleSheet(style_file.readAll().data().decode())

    # add widgets to the main window

    # sidebar button
    sidebarButton = QPushButton("Sidebar", window)
    #sidebarButton.setGeometry(23, 39, 61, 61)
    sidebarButton.setObjectName("sidebarButton")

    # live chat button
    liveButton = QPushButton("Live Chat", window)
    liveButton.setGeometry(289, 39, 61, 61)
    liveButton.setObjectName("liveButton")

    # add new cards button
    #cards = QPushButton("", window)
    #cards.setGeometry(25, 175, 325, 200)
    #cards.setObjectName("cards")

    # circle plus button on cards
    #plus = QPushButton("+", cards)
    #plus.setGeometry(137, 75, 50, 50)
    #plus.setObjectName("plus")

    menu = QPushButton("", window)
    menu.setGeometry(25, 175, 325, 200)
    menu.setObjectName("noBorder")

    menuBorder = QPushButton("", window)
    menuBorder.setGeometry(25, 175, 325, 200)
    menuBorder.setObjectName("noBorder")

    # load the main window as the root object
    window.show()

    # code
    sidebarButton.clicked.connect(var.buttonPressed)

    menuOpen = False
    def menuPressed():
        global menuOpen
        menuOpen = not menuOpen
        if menuOpen:
            menu.setGeometry(25, 175, 325, 592)
            menuBorder.setStyleSheet("border: 5px solid #545454;")
            menuBorder.setGeometry(20, 170, 335, 210)
        else:
            menu.setGeometry(25, 175, 325, 200)
            menuBorder.setStyleSheet("border: none;")
            menuBorder.setGeometry(25, 175, 325, 200)

    menuBorder.clicked.connect(menuPressed)

    sys.exit(app.exec())
