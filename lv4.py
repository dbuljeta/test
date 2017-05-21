from Tkinter import*
class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

root = Tk() 
app = Application(root)     
app.pack()
        
  
m = Menu(root)
filemenu = Menu(m, tearoff=0)
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Exit")
m.add_cascade(label="File", menu=filemenu)
root.config(menu=m)
C = Canvas(root, bg="white", height=600, width=800)
C.pack()
    
class GrafLik:
    def __init__(self,boja='crna',*k1):
        self.boja=boja
        self.k1=k1
    def SetColor(self):
        self.boja=boja
    def GetColor(self):
        return self.boja
    def Draw(self):
        pass

class Linija(GrafLik):
    def __init__(self,  boja  ,*k1):
        GrafLik.__init__(self,boja,*k1)
    def Draw(self):
        C.create_line(self.k1,fill=self.boja)

class Trokut(Linija):
    def __init__(self,boja,*k1):
        GrafLik.__init__(self,boja,*k1)
        self.k1=k1
    def Draw(self):
        C.create_polygon(k1,k2,k3,outline=boja,fill='')
class Pravokutnik(GrafLik):
    k2=[0,0]
    boja='red'
    def __init__(self, boja,k2):
        GrafLik.__init__(self,k1,boja)
        self.k2=k2
    def Draw(self):
        C.create_rectangle(k1,k2,k3,outline=boja,fill='')
class Poligon(GrafLik):
    def __init__(self,boja,*k2):
        GrafLik.__init__(self,boja,*k1)
        self.*k2=*k2
    def Draw(self):
        C.create_polygon(self.*k2,fill=self.boja)
    
class Kruznica(GrafLik):
    radius=0
    def __init__(self,radius):
        GrafLik.__init__(self,boja,k1)
        self.radius=radius
    def Draw(self):
        C.create_oval(k1,k1+radius,outline='boja',fill='')
class Elipsa(Kruznica):
    a=0
    b=0
    def __init__(self, a,b):
        GrafLik.__init__(self,boja,k1)
        Kruznica.__init__(self,radius)
        self.a=a
        self.b=b
    def Draw(self):
        C.create_oval(k1,k2,outline='boja',fill='')

    #Linija() 
    lin=Linija('green',321,136,283.0,177.6)
    Linija.Draw(lin)
    root.mainloop()
