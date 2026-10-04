import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, imgpath=None): 
        wx.Frame.__init__(self, parent, -1, style=wx.BORDER_NONE)

        self.SetSize(150,150)
        self.SetPosition((100,100))

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        self.Layout()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, imgpath=r'C:/Users/joaquin/Desktop/llave.jpg') 
    frame.Show()
    app.MainLoop()