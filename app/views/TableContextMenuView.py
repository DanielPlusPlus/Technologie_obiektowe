from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QAction


class TableContextMenuView(QMenu):
    def __init__(self, ParentWindow):
        super().__init__(ParentWindow)

    def setup_UI(self):
        self.actionEditTable = QAction("Edit table", self)
        self.actionDeleteTable = QAction("Delete table", self)

        self.addAction(self.actionEditTable)
        self.addAction(self.actionDeleteTable)
