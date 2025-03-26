"""
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QMenuBar, QScrollArea
from PySide6.QtGui import QPainter, QPen, QColor, QAction
from PySide6.QtCore import Qt, QPoint, QRect
import sys


class PaintWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.drawing = False
        self.cursor_position = QPoint()
        self.tables = []  # Lista przechowująca narysowane tabele
        self.row_height = 20  # Wysokość pojedynczego wiersza
        self.num_rows = 5  # Liczba wierszy w tabeli
        self.table_width = 100  # Szerokość tabeli
        self.setMinimumSize(800, 600)  # Minimalny rozmiar obszaru roboczego

    def mouseMoveEvent(self, event):
        self.cursor_position = event.position().toPoint()
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            table_rect = QRect(self.cursor_position.x() - self.table_width // 2,
                               self.cursor_position.y() - (self.row_height * self.num_rows) // 2,
                               self.table_width, self.row_height * self.num_rows)
            self.tables.append(table_rect)
            self.adjustCanvasSize(table_rect)
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(Qt.GlobalColor.black), 2, Qt.PenStyle.SolidLine))

        for table in self.tables:
            self.drawTable(painter, table)

        # Rysowanie podążającej tabeli
        temp_rect = QRect(self.cursor_position.x() - self.table_width // 2,
                          self.cursor_position.y() - (self.row_height * self.num_rows) // 2,
                          self.table_width, self.row_height * self.num_rows)
        self.drawTable(painter, temp_rect)

    def drawTable(self, painter, rect):
        for i in range(self.num_rows + 1):
            y = rect.top() + i * self.row_height
            painter.drawLine(rect.left(), y, rect.right(), y)
        painter.drawRect(rect)

    def adjustCanvasSize(self, rect):
        new_width = max(self.width(), rect.right() + 50)
        new_height = max(self.height(), rect.bottom() + 50)
        self.setMinimumSize(new_width, new_height)
        self.resize(new_width, new_height)


class PaintApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dynamic Paint - PySide6")
        self.setGeometry(100, 100, 800, 600)

        self.scroll_area = QScrollArea(self)
        self.canvas = PaintWidget()
        self.scroll_area.setWidget(self.canvas)
        self.scroll_area.setWidgetResizable(True)
        self.setCentralWidget(self.scroll_area)

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        if not menubar:
            menubar = QMenuBar(self)
            self.setMenuBar(menubar)

        tools_menu = menubar.addMenu("Narzędzia")

        table_action = QAction("Tabela", self)
        table_action.triggered.connect(self.selectTableTool)
        tools_menu.addAction(table_action)

        self.statusBar().showMessage("Tryb rysowania tabeli z wierszami")

    def selectTableTool(self):
        self.canvas.tables.clear()
        self.canvas.update()
        self.statusBar().showMessage("Tryb rysowania tabeli z wierszami")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PaintApp()
    window.show()
    sys.exit(app.exec())
"""

"""
from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar, QScrollArea, QMessageBox, QWidget
from PySide6.QtGui import QPainter, QPen, QColor, QAction
from PySide6.QtCore import Qt, QPoint, QRect
import sys


class PaintWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.tables = []  # Lista tabel (prostokąty + numer)
        self.row_height = 20  # Wysokość pojedynczego wiersza
        self.num_rows = 5  # Liczba wierszy w tabeli
        self.table_width = 100  # Szerokość tabeli
        self.setMinimumSize(800, 600)  # Minimalny rozmiar obszaru roboczego
        self.table_counter = 1  # Numerowanie tabel
        self.drawing_enabled = False  # 🔹 Kontrola rysowania nowej tabeli

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            clicked_pos = event.position().toPoint()

            # 🔹 Sprawdzenie, czy kliknięto istniejącą tabelę
            for table_rect, table_number in self.tables:
                if table_rect.contains(clicked_pos):
                    self.showTableDialog(table_number)
                    return  # 🔹 Jeśli kliknięto tabelę, zakończ funkcję – nie rysuj nowej!

            # 🔹 Jeśli rysowanie tabel jest włączone – narysuj nową tabelę
            if self.drawing_enabled:
                table_rect = QRect(clicked_pos.x() - self.table_width // 2,
                                   clicked_pos.y() - (self.row_height * self.num_rows) // 2,
                                   self.table_width, self.row_height * self.num_rows)

                self.tables.append((table_rect, self.table_counter))  # Dodaj tabelę z numerem
                self.table_counter += 1  # Zwiększ numer tabeli
                self.drawing_enabled = False  # 🔹 Wyłącz rysowanie po postawieniu tabeli
                self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(Qt.GlobalColor.black), 2, Qt.PenStyle.SolidLine))

        # Rysowanie wszystkich tabel
        for table_rect, table_number in self.tables:
            self.drawTable(painter, table_rect)

    def drawTable(self, painter, rect):
        for i in range(self.num_rows + 1):
            y = rect.top() + i * self.row_height
            painter.drawLine(rect.left(), y, rect.right(), y)
        painter.drawRect(rect)

    def showTableDialog(self, table_number):
        msg = QMessageBox(self)
        msg.setWindowTitle("Informacja o tabeli")
        msg.setText(f"Kliknięto tabelę nr {table_number}")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()


class PaintApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rysowanie tabel - PySide6")
        self.setGeometry(100, 100, 800, 600)

        self.scroll_area = QScrollArea(self)
        self.canvas = PaintWidget()
        self.scroll_area.setWidget(self.canvas)
        self.scroll_area.setWidgetResizable(True)
        self.setCentralWidget(self.scroll_area)

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        tools_menu = menubar.addMenu("Narzędzia")

        # Akcja rysowania tabeli
        table_action = QAction("Rysuj tabelę", self)
        table_action.triggered.connect(self.selectTableTool)
        tools_menu.addAction(table_action)

        self.statusBar().showMessage("Wybierz opcję rysowania tabeli z menu")

    def selectTableTool(self):
        self.canvas.drawing_enabled = True
        self.statusBar().showMessage("Kliknij, aby narysować tabelę")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PaintApp()
    window.show()
    sys.exit(app.exec())
"""