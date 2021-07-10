import wx
import string
import random
import sys
#import time
alpha = list(string.ascii_uppercase)
#Optional
"""
arr = []
words = []
for arg in sys.argv:
    arr.append(arg)
file = arr[1]
f = open(file)
for line in f:
    words.append(line[0:-1])
"""
words = ["GAME", "SOUND", "OWL"]
w = words.copy()
class Example(wx.Frame):
    
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        
        self.word = random.choice(w)
        #w.remove(self.word)
        if not w:
            for i in words:
                w.append(i)
            
        self.n = 2
        self.sz = len(self.word) - self.n
        self.tries = 6
        
        self.font = wx.Font(26, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.pnl = wx.Panel(self)
        self.hangman = wx.Bitmap('1hang_small.png',
wx.BITMAP_TYPE_PNG)
        self.img=wx.StaticBitmap(self.pnl, 0, self.hangman,
            pos=(220,250))
        

        self.heading = wx.StaticText(self.pnl, label = "", pos = (200, 390))
        self.heading.SetFont(self.font)
        self.guess_word = self.word[0] + self.sz*"_" + self.word[-1]
        self.hang = wx.StaticText(self.pnl, label = self.guess_word, pos = (220, 10))
        self.hang.SetFont(self.font)
        
        
        #self.a = wx.ToggleButton(self.pnl, label = "u", pos=(25,75), size = (25,25))
        #self.a.Bind(wx.EVT_TOGGLEBUTTON, self.Check)
        self.buttons = []
        self.pressed = {} #clear rechnik
        m = 120
        n = 80
        j = 0
        for i in range((26)):
            self.buttons.append(wx.ToggleButton(self.pnl, label = alpha[i], pos = ((n + j*20, m)), size = wx.Size((30, 30))))
            self.pressed[alpha[i]] = False
            j +=2
            if i == 10 or i == 21:
                n = 80
                m += 35
                j = 0
        for i in range(26):
            self.buttons[i].Bind(wx.EVT_TOGGLEBUTTON, self.Check)
        self.InitUI()


    def InitUI(self):
        self.SetSize((600, 480))
        self.SetTitle('Hangman')
        self.Centre()
        self.Show(True)
    def Reset(self,e):
        try:
            self.word = random.choice(w)
        except:
            for i in words:
                #print(i)
                w.append(i)
            #print(w)
            self.word = random.choice(w)
        #w.remove(self.word)
       
        self.n = 2
        self.sz = len(self.word) - self.n
        self.tries = 6
        self.guess_word = self.word[0] + self.sz*"_" + self.word[-1]
        for i in range(26):
            self.pressed[alpha[i]] = False
            self.buttons[i].Enable()
            self.buttons[i].SetValue(False)
        self.heading.SetLabel(" ")
        self.hang.SetLabel(self.guess_word)
        self.hangman.LoadFile("1hang_small.png", wx.BITMAP_TYPE_PNG)
        self.img.SetBitmap(self.hangman)
        self.rbtn.Disable()
        self.rbtn.Hide()

    def Check(self,e):
        obj = e.GetEventObject()
        obj.Disable()
        strn = obj.GetLabel()
        strn = strn.upper()
        
        if strn in self.word:
            self.sz = self.sz - 1
            #print(len(self.word))
            new_word = [""] * len(self.word)
             
            for i in range(0, len(self.word)):
                if(self.word[i] != strn):
                    new_word[i] = self.guess_word[i]
                else:
                    new_word[i] = strn
                #print(new_word)
            
            new_word_str = "".join(new_word)
            self.guess_word = new_word_str
            #print(new_word_str)
            self.hang.SetLabel(new_word_str)
            if self.guess_word == self.word:
                self.heading.SetLabel("You have won!")
                #time.sleep(5)
                w.remove(self.word)
                self.rbtn = wx.Button(self.pnl, label='Reset', pos=(250, 75))
                self.rbtn.Bind(wx.EVT_BUTTON, self.Reset)
                for i in range(0, 26):
                    self.buttons[i].Disable()
                #self.Reset()
        else:
            if self.pressed[strn] == False:
                self.tries = self.tries - 1
                if self.tries == 5:
                    self.hangman.LoadFile("2head_small.png", wx.BITMAP_TYPE_PNG)
                    self.img.SetBitmap(self.hangman)
                if self.tries == 4:
                    self.hangman.LoadFile("3body_small.png", wx.BITMAP_TYPE_PNG)
                    self.img.SetBitmap(self.hangman)
                if self.tries == 3:
                    self.hangman.LoadFile("4handleft_small.png", wx.BITMAP_TYPE_PNG)
                    self.img.SetBitmap(self.hangman)
                if self.tries == 2:
                    self.hangman.LoadFile("5bothhands_small.png", wx.BITMAP_TYPE_PNG)
                    self.img.SetBitmap(self.hangman)
                if self.tries == 1:
                    self.hangman.LoadFile("6legleft_small.png", wx.BITMAP_TYPE_PNG)
                    self.img.SetBitmap(self.hangman)
                if self.tries == 0:
                    self.hangman.LoadFile("7hangman_small.png", wx.BITMAP_TYPE_PNG)
                    self.img.SetBitmap(self.hangman)

            if self.tries > 0:
                self.heading.SetLabel("You have {} tries left".format(self.tries))
            else:
                self.heading.SetLabel("   Game Over!")
                #time.sleep(5)
                #self.Reset()
                self.rbtn = wx.Button(self.pnl, label='Reset', pos=(250, 75))
                self.rbtn.Bind(wx.EVT_BUTTON, self.Reset)
                for i in range(0, 26):
                    self.buttons[i].Disable()
        self.pressed[strn] = True


ex = wx.App()
Example(None)
ex.MainLoop()