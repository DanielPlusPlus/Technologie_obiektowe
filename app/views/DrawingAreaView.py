from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QPoint


class DrawingAreaView(QWidget):
    def __init__(self, DrawingAreaController):
        super().__init__()
        self.DrawingAreaController = DrawingAreaController
        self.setMouseTracking(True)

    def setupUI(self):
        self.setObjectName(u"DrawingArea")
        self.cursorPosition = QPoint()

    def mouseMoveEvent(self, event):
        self.DrawingAreaController.handleMouseMove(event)

    def mousePressEvent(self, event):
        self.DrawingAreaController.handleMousePress(event)
