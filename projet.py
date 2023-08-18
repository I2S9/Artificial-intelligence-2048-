###PROJET ARBRES DE RECHERCHE

### 1ère fenêtre - Acceuil
import tkinter as TK

'''
class Noeud:
    def __init__(self, valeur):
        self.valeur_noeud = valeur
        self.SAG = None
        self.SAD = None

    def insert_dans_SAG(self, valeur):
        self.SAG = Noeud(valeur)
    def insert_dans_SAD(self, valeur):
        self.SAD = Noeud(valeur)

    def get_valeur_noeud(self):
        return self.valeur_noeud

    def get_SAG(self):
        return self.SAG
    def get_SAD(self):
        return self.SAD

def affiche_arbre(noeud):
    if noeud!=None:
        return(noeud.get_valeur_noeud(),affiche_arbre(noeud.get_SAG()),affiche_arbre(noeud.get_SAD()))
'''

def affp(*args):
    fen3.mainloop()

def settings(*args):
    fen2.mainloop()

fen1 = TK.Tk()
fen1.title("Arbres binaires de recherche")
#fen.iconbitmap(False, TK.PhotoImage(file='tree.ico'))
canvas=TK.Canvas(fen1,width=600,height=600,background='#B0E0E6')

B2=TK.Canvas.create_rectangle(canvas,390,530,200,490, fill="#6db4bf", tags = "affp-Button")
B3=TK.Canvas.create_rectangle(canvas,200,550,390,590, fill="#6db4bf", tags = "settings-Button")

font1=('Calibri',11,'bold')

TK.Canvas.create_text(canvas, 295, 510, text= "Affichage et parcours",font=font1, fill="white", tags = "affp-Button")
TK.Canvas.create_text(canvas, 295, 570, text= "Paramètres de l'arbre",font=font1, fill="white", tags = "settings-Button")

canvas.pack()
#Ajout des actions aux boutons
canvas.tag_bind("affp-Button","<Button-1>",affp)
canvas.tag_bind("settings-Button","<Button-1>",settings)

fen1.resizable(width=False, height=False)
fen1.mainloop()

#2ème fenêtre - Paramètres de l'arbre
import tkinter as TK

def ajout(*args):
    print("Ajouter des éléments")
    return
    '''
    def InsererNoeud(racine,cle) :
        while racine != None:
            arbre_courant=T
            if cle <= racine :
                T=T.SAG
            else:
                T=T.SAD
            if (cle <= arbre_courant.Racine) :
                InsererNoeud(cle, T.SAG())
            else:
                InsererNoeud(cle, T.SAD())

    def Inserer_Cle(racine, cle):
        while (racine!=None):
            noeud_courant=racine
            if cle <= racine.get_valeur_noeud():

    '''

def recherche(*args):
    print("Rechercher des éléments")
    return
    '''
    def Recherche_Cle(racine, cle):
        if racine ==None:
            return False
        if(cle==racine.get_valeur_noeud()):
            return True
        else:
            if(cle < racine.get_valeur_noeud()):
                return Recherche_Cle(racine.get_SAG().cle)
            else:
                return Recherche_Cle(racine.get_SAD().cle)
   '''

def creer(*args):
    print("Créer un nouve arbre")
    return

def delete(*args):
    print("Supprimer l'arbre")
    return

fen2 = TK.Tk()
fen2.title("Paramètres de l'arbre")
#fen2.iconbitmap(False, TK.PhotoImage(file='tree.ico'))
canvas=TK.Canvas(fen2,width=600,height=600,background='#B0E0E6')

B2=TK.Canvas.create_rectangle(canvas,430,200,170,240, fill="#6db4bf", tags = "ajout-Button")
B3=TK.Canvas.create_rectangle(canvas,430,260,170,300, fill="#6db4bf", tags = "recherche-Button")
B5=TK.Canvas.create_rectangle(canvas,430,320,170,360, fill="#6db4bf", tags = "creer-Button")
B5=TK.Canvas.create_rectangle(canvas,430,380,170,420, fill="#6db4bf", tags = "delete-Button")

font1=('Calibri',11,'bold')

TK.Canvas.create_text(canvas, 295, 220, text= "Ajouter des éléments",font=font1, fill="white", tags = "ajout-Button")
TK.Canvas.create_text(canvas, 295, 280, text= "Rechercher des éléments",font=font1, fill="white", tags = "recherche-Button")
TK.Canvas.create_text(canvas, 295, 340, text= "Créer un nouvel arbre",font=font1, fill="white", tags = "creer-Button")
TK.Canvas.create_text(canvas, 295, 400, text= "Supprimer l'arbre",font=font1, fill="white", tags = "delete-Button")

canvas.pack()
#Ajout des actions aux boutons
canvas.tag_bind("ajout-Button","<Button-1>",ajout)
canvas.tag_bind("recherche-Button","<Button-1>",recherche)
canvas.tag_bind("creer-Button","<Button-1>",creer)
canvas.tag_bind("delete-Button","<Button-1>",delete)

fen2.resizable(width=False, height=False)
fen2.mainloop()

#3ème fenêtre - Affichage et parcours

import tkinter as TK

def visualiser(*args): #revient à la fonction affichage
    print("Viualiser l'arbre")
    return
    '''
    def affiche_arbre(noeud) :
        if noeud!=None :
            return(noeud.get_valeur_noeud(),affiche_arbre(noeud.get_SAG()),affiche_arbre(noeud.get_SAD()))
    '''

def parcours(*args):
    fen4.mainloop()

fen3 = TK.Tk()
fen3.title("Affichage et parcours")
#fen3.iconbitmap(False, TK.PhotoImage(file='tree.ico'))
canvas=TK.Canvas(fen3,width=600,height=600,background='#B0E0E6')

B2=TK.Canvas.create_rectangle(canvas,390,530,200,490, fill="#6db4bf", tags = "visualiser-Button")
B3=TK.Canvas.create_rectangle(canvas,200,550,390,590, fill="#6db4bf", tags = "parcours-Button")

font1=('Calibri',11,'bold')

TK.Canvas.create_text(canvas, 295, 510, text= "Viualiser l'arbre",font=font1, fill="white", tags = "visualiser-Button")
TK.Canvas.create_text(canvas, 295, 570, text= "Parcours de l'arbre",font=font1, fill="white", tags = "parcours-Button")

canvas.pack()
#Ajout des actions aux boutons
canvas.tag_bind("visualiser-Button","<Button-1>",visualiser)
canvas.tag_bind("parcours-Button","<Button-1>",parcours)

fen3.resizable(width=False, height=False)
fen3.mainloop()

# 4 - fenêtre parcours
import tkinter as TK

def largeur(*args):
    print("Parcours en largeur")
    return
    '''
    def Parcours_Largeur(racine):
        Liste_resultat=[]
        if racine!=None :
            F=[]
            F.append(racine) #La liste F ne contient qu'un seul élément, l'objet racine de la classe noeud
            while(len(F)!=0 #Attention, F!=None ne fonctionne pas
            noeud_courant=F.pop(0) #Pop supprime l'élément d'index 0 d'une liste et le renvoie. Ici, cela n'affecte que le premier attribut de l'objet de la classe Noeud

            #print("\ noeud courant : ", noeud_courant.get_valeur_noeud())
            Liste_resultats.append(noeud_courant.get_valeur_noeud())
            if noeud_courant.get_SAG() !=None :
                F.append(noeud_courant.get_SAG() !=None)
            if noeud_courant.get_SAD() !=None :
                F.append(noeud_courant.get_SAD() !=None)
            print("L résultat :",Liste_resulatts)
        return Liste_resultats
    '''

def infixe(*args):
    print("Parcours infixe")
    return
    '''
    def Parcours_infixe(l,T):
        if T!=None:
            Parcours_infixe(l, T.SAG)
            l.append(T.get_valeur_noeud())
            Parcours_infixe(l, T.SAD)
        return l
    '''

def suffixe(*args):
    print("Parcours suffixe")
    return
    '''
    def Parcours_suffixe(l,T):
        if T!=None:
            Parcours_suffixe(l, T.SAG)
            Parcours_suffixe(l, T.SAD)
            l.append(T.get_valeur_noeud())
        return l
    '''

def postfixe(*args):
    print("Parcours postfixe")
    return
    '''
    def Parcours_prefixe(l,T):
        if T!=None:
            l.append(T.get_valeur_noeud())
            Parcours_prefixe(l, T.SAG)
            Parcours_prefixe(l, T.SAD)
        return l
    '''

fen4 = TK.Tk()
fen4.title("Parcours")
#fen4.iconbitmap(False, TK.PhotoImage(file='tree.ico'))
canvas=TK.Canvas(fen4,width=600,height=600,background='#B0E0E6')

B2=TK.Canvas.create_rectangle(canvas,430,200,170,240, fill="#6db4bf", tags = "largeur-Button")
B3=TK.Canvas.create_rectangle(canvas,430,260,170,300, fill="#6db4bf", tags = "infixe-Button")
B5=TK.Canvas.create_rectangle(canvas,430,320,170,360, fill="#6db4bf", tags = "suffixe-Button")
B5=TK.Canvas.create_rectangle(canvas,430,380,170,420, fill="#6db4bf", tags = "postfixe-Button")

font1=('Calibri',11,'bold')

TK.Canvas.create_text(canvas, 295, 220, text= "Parcours en largeur",font=font1, fill="white", tags = "largeur-Button")
TK.Canvas.create_text(canvas, 295, 280, text= "Parcours infixe",font=font1, fill="white", tags = "infixe-Button")
TK.Canvas.create_text(canvas, 295, 340, text= "Parcours suffixe",font=font1, fill="white", tags = "suffixe-Button")
TK.Canvas.create_text(canvas, 295, 400, text= "Parcours postfixe",font=font1, fill="white", tags = "postfixe-Button")

canvas.pack()
#Ajout des actions aux boutons
canvas.tag_bind("largeur-Button","<Button-1>",largeur)
canvas.tag_bind("infixe-Button","<Button-1>",infixe)
canvas.tag_bind("suffixe-Button","<Button-1>",suffixe)
canvas.tag_bind("postfixe-Button","<Button-1>",postfixe)

fen4.resizable(width=False, height=False)
fen4.mainloop()

### clavier (ne fonctionne pas encore)

from tkinter import *
import tkinter

clavier_app = tkinter.Tk()
clavier_app.title("clavier")
clavier_app.resizable(0, 0)


def select(value):
    if value == "<-":
        entry2 = entry.get()
        pos = entry2.find("")
        pos2 = entry2[pos:]
        entry.delete(pos2, tkinter.END)
    elif value == " ESPACE ":
        entry.insert(tkinter.END, ' ')
    elif value == " Tab ":
        entry.insert(tkinter.END, '   ')
    else:
        entry.insert(tkinter.END,value)

buttons = [

'a','z','e','r','t','y','u','i','o','p','<--','7','8','9','-','q','s','d','f','g','h','j','k','l','m','[',']','4','5','6','+','w','x','c','v','b','n',',',';','_','?','SHIFT','1','2','3','/','ESPACE'
]
label1.Label(clavier_app, text='').grid(row=0, columnspan = 1 entry = Entry(clavier_app, width = 138)
entry.grid(row = 1, columnspan = 20)

varRow = 2
varColumn = 0

for button in buttons:
    command = lambda x=button: select(x)
    if button != ' ESPACE ':
        tkinter.Button(clavier_app, text = button, width = 5,bg ="#000000",fg="#ffffff",activebackground="#ffffff",activeforeground="#000000",relief = 'raised',padx=4, pady=4, bd=4, command=command).grid(row = 6, columnspace=16)

    varColumn+m1
    if varColumns > 14 and varRow ==2:
        varColumns = 0
    if varColumns > 14 and varRow ==3:
        varColumns = 0
        varRow+=1

clavier_app.resizable(width=False, height=False)
clavier_app.mainloop()

### Partie réalisée par un autre camarade

import tkinter
import tkinter.font as tkFont

class Noeud:
    def __init__(self, valeur,nomre,coul):
        self.valeur_noeud = valeur
        self.SAG = None
        self.SAD = None
        self.couleur= coul
        self.nom = nomre
    def insert_dans_SAG(self, valeur,nomre,coul):
        self.SAG = Noeud(valeur,nomre,coul)
    def insert_dans_SAD(self,valeur,nomre,coul):
        self.SAD = Noeud(valeur,nomre,coul)
    def get_valeur_noeud(self):
        return self.valeur_noeud
    def get_SAG(self):
        return self.SAG
    def get_SAD(self):
        return self.SAD
    def get_couleur(self):
        return self.couleur
    def set_couleur(self,val):
        self.couleur = val
    def get_nom(self):
        return self.nom
def affiche_arbre(noeud) :
    if noeud!=None :
        return(noeud.get_valeur_noeud(),affiche_arbre(noeud.get_SAG()),affiche_arbre(noeud.get_SAD()))


"""well"""

fen = tkinter.Tk()
fen.option_add('*Font', '19')
fen.geometry("400x400") #Dimensions de la fenetre
fen.title("Arbres") #Nom de la fenetre. Reference à un jeu de plateau similaire
fen.resizable(False, False) #On empeche de redimensionner la fenetre

#Canvas création
can = tkinter.Canvas(fen, width = 400, height = 400, background = "black")
can.place(x = 0, y = 0)

""" lets try"""
def display_node(noeud):
    if noeud.get_valeur_noeud()!=None:
        c= noeud.get_valeur_noeud()
        x_1= placement[noeud.get_nom()][0]
        y_1= placement[noeud.get_nom()][1]
        lab= tkinter.Label(fen,text=c,bg="black",fg=noeud.get_couleur())
        lab.place(x=x_1,y=y_1)






# This is the definition of all nodes for the manual work
noeud_A=Noeud(90, "A" ,"red")
noeud_A.insert_dans_SAG(80,'B','red')
noeud_A.insert_dans_SAD(100, "C" ,"yellow")
noeud_B=noeud_A.get_SAG()
noeud_C=noeud_A.get_SAD()

noeud_B.insert_dans_SAG(70,"D","pink")
noeud_B.insert_dans_SAD(81,"E","pink")
noeud_D=noeud_B.get_SAG()
noeud_E=noeud_B.get_SAD()


noeud_C.insert_dans_SAG(95,"F","pink")
noeud_C.insert_dans_SAD(105,"G","pink")
noeud_F=noeud_C.get_SAG()
noeud_G=noeud_C.get_SAD()




placement={"A":[200,1],"B":[100,50],"C":[300,50],"D":[50,100],"E":[150,100],"F":[250,100],"G":[350,100]}



display_node(noeud_A)
display_node(noeud_B)
display_node(noeud_C)
display_node(noeud_D)
display_node(noeud_E)
display_node(noeud_F)
display_node(noeud_G)

fen.mainloop()