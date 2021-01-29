import wx

pos = (0, 0)
draw = False

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='PyPressure by OblivionCreator')
        self.panel = wx.Panel(self)
        self.panel.Bind(wx.EVT_LEFT_DOWN, self.onClickDown)
        self.panel.Bind(wx.EVT_LEFT_UP, self.onClickRelease)
        self.panel.Bind(wx.EVT_MOTION, self.onMouseMove)
        self.panel.BackgroundColour = wx.RED
        self.Show()

    def onClickRelease(self, event):
        global draw

        self.panel.BackgroundColour = wx.GREEN
        self.panel.Refresh()
        draw = False

    def onClickDown(self, event):
        global pos
        global draw
        print(f"CLICK AT {pos}")
        self.panel.BackgroundColour = wx.BLUE
        self.panel.Refresh()
        draw = True
        dc = wx.ClientDC(self)
        dc.DrawCircle(300, 125, 50)
        dc.SetBrush(wx.Brush(wx.Colour(255, 255, 255)))
        dc.DrawCircle(300, 125, 30)

    def onMouseMove(self, event):
        global pos
        global draw
        dc = wx.ClientDC(self)
        pos = event.GetLogicalPosition(dc)
        print(pos)

        if draw != True:
            return
        brush = wx.Brush(wx.Colour(255, 255, 0))
        dc0.SetBrush(brush)
        x, y = pos
        dc0.DrawCircle(x, y, 50)
        self.panel.Refresh()

    def onPaint(self, e):
        dc = wx.PaintDC(self, e)







if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()