from Tkinter import*
import tkFileDialog
class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        m = Menu(root)
        filemenu = Menu(m, tearoff=0)
        filemenu.add_command(label="Open",command=self.FunOpen)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        m.add_cascade(label="File", menu=filemenu)
        root.config(menu=m)

    def FunOpen(self):
        inputfile=tkFileDialog.askopenfilename(filetypes = [('All files','*.*'),('txt files', '*.txt')])
        for line in open(inputfile):
            sent=line.split()
            if sent[0]=='Line':
                boja=sent[1]
                k=sent[2:]
                lin=Linija(boja,k)
                Linija.Draw(lin)
            if sent[0]=='Triangle':
                boja = sent[1]
                k=sent [2:]
                trok = Trokut(boja, k)
                Trokut.Draw(trok)
            if sent[0]=='Rectangle':
                boja=sent[1]
                k=sent[2:]
                k = [float(a) for a in k]
                prav=Pravokutnik(boja,k[0],k[1],k[0]+k[2],k[1]+k[3])
                Pravokutnik.Draw(prav)
            if sent[0]=='Polygon':
                boja=sent[1]
                k=sent[2:]
                poligon=Poligon(boja,k)
                Poligon.Draw(poligon)
            if sent[0]=='Circle':
                boja=sent[1]
                k=sent[2:]
                k = [float(a) for a in k]
                r=k[2]
                kruz=Kruznica(boja, k[0]-r, k[1]-r, k[0]+r, k[1]+r)
                Kruznica.Draw(kruz)
            if sent[0]=='Ellipse':
                boja=sent[1]
                k=sent[2:]
                k = [float(a) for a in k]
                a=k[2]
                b=k[3]
                elip=Elipsa(boja,k[0]-a,k[1]-b,k[0]+a,k[1]+b)
                Elipsa.Draw(elip)
            
                
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
        C.create_polygon(self.k1,outline=self.boja,fill='')

class Pravokutnik(GrafLik):
    def __init__(self, boja,*k1):
        GrafLik.__init__(self,boja,*k1)
    def Draw(self):
        C.create_rectangle(self.k1,outline=self.boja,fill='')

class Poligon(GrafLik):
    def __init__(self,boja,*k1):
        GrafLik.__init__(self,boja,*k1)
    def Draw(self):
        C.create_polygon(self.k1,outline=self.boja,fill='')
    
class Kruznica(GrafLik):
    def __init__(self,boja,*k1):
        GrafLik.__init__(self,boja,*k1)
    def Draw(self):
        C.create_oval(self.k1,outline=self.boja,fill='')

class Elipsa(Kruznica):
    def __init__(self,boja, *k1):
        GrafLik.__init__(self,boja,*k1)
    def Draw(self):
        C.create_oval(self.k1,outline=self.boja,fill='')


##Tests
##Linija() 
#lin=Linija('green',321,136,283.0,177.6)
#Linija.Draw(lin)

##Trokut() 
#trok=Trokut('green',659,80 ,612.4, 124.2, 670.4, 40.9)
#Trokut.Draw(trok)

##Poligon
#poligon=Poligon('red' ,64 ,70, 63.0, 29.0, 27.9, 56.2, 66.7, 114.9, 89.6, 75.6, 87.3, 75.2, 64.3 ,91.0)
#Poligon.Draw(poligon)

##Pravokuntik
#prav=Pravokutnik('black', 52, 311, 8.8, 40.4)
#Pravokutnik.Draw(prav)
#prav1=Pravokutnik('red', 80, 370, 80-46.5, 370+46.2)
#Pravokutnik.Draw(prav1)

##Kruznica
#kruz=Kruznica('green', 307.0-11.8, 399-11.8, 307.0+11.8, 399+11.8)
#Kruznica.Draw(kruz)

#Elipsa
#elip=Elipsa('black',626-49,389-5,626+49,389+5)
#Elipsa.Draw(elip)

#root.mainloop()

root = Tk() 
app = Application(root)     
app.pack()
C = Canvas(root, bg="#999999",width=800, height=600)
C.pack()

if __name__ == '__main__':
    root.mainloop()
    root.destroy()   





