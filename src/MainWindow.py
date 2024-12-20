from PyQt5.QtWidgets import (QMainWindow, QMessageBox,
                             QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QComboBox, QPushButton)
# from PyQt5.QtCore import pyqtSlot
import Material

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Список материалов')
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        search_edit = QLineEdit(parent=self)
        hbox.addWidget(search_edit)
        sort_cbox = QComboBox(parent=self)
        hbox.addWidget(sort_cbox)
        filter_cbox = QComboBox(parent=self)
        hbox.addWidget(filter_cbox)
        vbox.addLayout(hbox)
        v = Material.View(self)
        vbox.addWidget(v)
        bbox = QHBoxLayout()
        bbox.addStretch()
        add_btn = QPushButton("Добавить", parent=self)
        bbox.addWidget(add_btn)
        next_btn = QPushButton("Следующие", parent=self)
        bbox.addWidget(next_btn)
        vbox.addLayout(bbox)
        self.setLayout(vbox)


