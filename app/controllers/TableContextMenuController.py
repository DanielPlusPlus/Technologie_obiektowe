class TableContextMenuController:
    def __init__(self, TableContextMenuView):
        self.isEditTableSelected = False
        self.isDeleteTableSelected = False
        TableContextMenuView.actionEditTable.triggered.connect(self.selectEditTable)
        TableContextMenuView.actionDeleteTable.triggered.connect(self.selectDeleteTable)

    def selectEditTable(self):
        self.isEditTableSelected = True

    def unselectEditTable(self):
        self.isEditTableSelected = False

    def getSelectEditTableStatus(self):
        return self.isEditTableSelected

    def selectDeleteTable(self):
        self.isDeleteTableSelected = True

    def unselectDeleteTable(self):
        self.isDeleteTableSelected = False

    def getSelectDeleteTableStatus(self):
        return self.isDeleteTableSelected
