from PySide6.QtWidgets import QMainWindow

from app.views.MainWindowView import MainWindowView
from app.views.ToolBarView import ToolBarView
from app.views.DrawingAreaView import DrawingAreaView
from app.controllers.ToolBarController import ToolBarController
from app.controllers.DrawingAreaController import DrawingAreaController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # views
        self.MainWindowView = MainWindowView()
        self.MainWindowView.setupUi(self)

        self.ToolBarView = ToolBarView(self)
        self.ToolBarView.setupUI()
        self.addToolBar(self.ToolBarView)

        # controllers
        self.ToolBarController = ToolBarController(self.ToolBarView)
        self.DrawingAreaController = DrawingAreaController()

        # views
        self.drawingAreaView = DrawingAreaView(self.DrawingAreaController)
        self.drawingAreaView.setupUI()
        self.MainWindowView.addCentralWidget(self.drawingAreaView)

        # controllers
        self.DrawingAreaController.setView(self.drawingAreaView)

