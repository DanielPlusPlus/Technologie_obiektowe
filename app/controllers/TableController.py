from app.views.ConfirmationDialogView import ConfirmationDialogView


class TableController:
    def __init__(self, ParentWindow, TableView, TableModel):
        self.ParentWindow = ParentWindow
        self.TableView = TableView
        self.TableModel = TableModel
        dialogTitle = "WARNING"
        dialogText = "Are you about deleting this table?"
        self.ConfirmationDialogView = ConfirmationDialogView(self.ParentWindow, dialogTitle, dialogText)

    def addTable(self, cursorPosition):
        self.TableModel.addTable(cursorPosition)

    def deleteTable(self, cursorPosition):
        ObtainedTable = self.TableModel.getTableFromPosition(cursorPosition)
        if ObtainedTable is not None:
            if self.ConfirmationDialogView.displayDialog():
                self.TableModel.deleteSelectedTable(ObtainedTable)

    def displayTable(self, cursorPosition):
        ObtainedTable = self.TableModel.getTableFromPosition(cursorPosition)
        if ObtainedTable is not None:
            print(ObtainedTable.getTableNumber())

    def selectDrawTempTable(self, position):
        self.TableView.drawTempTable(position)

    def selectDrawTable(self):
        self.TableView.drawTables()
