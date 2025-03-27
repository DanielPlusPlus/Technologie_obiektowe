from PySide6.QtWidgets import QWidget, QScrollArea


class ScrollAreaView(QWidget):
    def __init__(self):
        super().__init__()
        self.ScrollArea = QScrollArea(self)

    def setupUI(self, DrawingAreaView):
        self.ScrollArea.setWidget(DrawingAreaView)
        self.ScrollArea.setWidgetResizable(True)
