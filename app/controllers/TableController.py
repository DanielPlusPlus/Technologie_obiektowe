class TableController:
    def __init__(self, TableView):
        self.TableView = TableView

    def selectTempTable(self, position):
        self.TableView.drawTempTable(position)

    def selectDrawTable(self):
        self.TableView.drawTables()