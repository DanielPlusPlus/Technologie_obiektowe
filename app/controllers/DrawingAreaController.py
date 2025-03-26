class DrawingAreaController:
    def __init__(self):
        self.DrawingAreaView = None

    def setView(self, DrawingAreaView):
        self.DrawingAreaView = DrawingAreaView

    def handleMouseMove(self, event):
        print("Ruszono")

    def handleMousePress(self, event):
        print("Wciesnieto")
