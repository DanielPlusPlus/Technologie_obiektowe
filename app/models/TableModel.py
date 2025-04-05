from PySide6.QtCore import QPoint, QRect


class Table:
    def __init__(self, x, y, width, rowHeight, rowsNumber, tableNumber):
        self.rectangle = QRect(x - width // 2, y - (rowHeight * rowsNumber) // 2, width, rowHeight * rowsNumber)
        self.rowHeight = rowHeight
        self.rowsNumber = rowsNumber
        self.tableNumber = tableNumber

    def getRectangle(self):
        return self.rectangle

    def getTop(self):
        return self.rectangle.top()

    def getLeft(self):
        return self.rectangle.left()

    def getRight(self):
        return self.rectangle.right()

    def getRowHeight(self):
        return self.rowHeight

    def getRowsNumber(self):
        return self.rowsNumber

    def getTableNumber(self):
        return self.tableNumber

    def contains(self, point):
        if self.rectangle.contains(point):
            return True


class TableModel:
    def __init__(self):
        self.tables = []
        self.tableNumber = 1

    def addTable(self, position, width=100, rowsHeight=20, rowsNumber=5):
        createdTable = Table(position.x(), position.y(), width, rowsHeight, rowsNumber, self.tableNumber)
        self.tables.append(createdTable)
        self.tableNumber += 1

    def clearTables(self):
        self.tables.clear()

    def getTables(self):
        return self.tables

    def deleteSelectedTable(self, SelectedTable):
        self.tables.remove(SelectedTable)

    def getTableFromPosition(self, position):
        for ObtainedTable in self.tables:
            if ObtainedTable.contains(QPoint(position.x(), position.y())):
                return ObtainedTable
        return None
