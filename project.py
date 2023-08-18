import tkinter as TK
from tkinter import * #Pour importer l'ensemble de la bibliothèque
from PIL import Image, ImageTk
import time as tm
from random import randint
import random
import os
from tkinter import messagebox

domino=['domino/domino-0_0.PNG','domino/domino-1_0.PNG','domino/domino-2_0.PNG','domino/domino-3_0.PNG','domino/domino-4_0.PNG','domino/domino-5_0.PNG',
'domino/domino-6_0.PNG','domino/domino-1_1.PNG','domino/domino-1_2.PNG','domino/domino-1_3.PNG','domino/domino-1_4.PNG','domino/domino-1_5.PNG',
'domino/domino-1_6.PNG','domino/domino-2_2.PNG','domino/domino-2_3.PNG','domino/domino-2_4.PNG','domino/domino-2_5.PNG','domino/domino-2_6.PNG',
'domino/domino-3_3.PNG','domino/domino-3_4.PNG','domino/domino-3_5.PNG','domino/domino-3_6.PNG','domino/domino-4_4.PNG','domino/domino-4_5.PNG',
'domino/domino-4_6.PNG','domino/domino-5_5.PNG','domino/domino-5_6.PNG','domino/domino-6_6.PNG']
domino_list = [ x for x in range(0,28) ]

class joueur():
    def __init__(self,nom):
        self.nom = nom
        self.dominoes = []
        self.image_dominoes = [ ]
        self.score = 0
        self.score_canvas = None

pairs = [ 27, 25, 22, 18, 13, 7, 0 ]
dominos_dict = { 27:"6/6", 26:"5/6", 25:"5/5", 24:"4/6", 23:"4/5", 22:"4/4", 21:"3/6", 20:"3/5", 19:"3/4", 18:"3/3", 17:"2/6", 16:"2/5", 15:"2/4", 14:"2/3", 
13:"2/2", 12:"1/6", 11:"1/5", 10:"1/4", 9:"1/3", 8:"1/2", 7:"1/1", 6:"0/6", 5:"0/5", 4:"0/4", 3:"0/3", 2:"0/2", 1:"0/1", 0:"0/0" }

U1 = []
U2 = []
Rnd= []

def pioche():
    global domino_list
    idx = random.choice(domino_list)
    domino_list.remove(idx)
    return idx

def password(event):
    if e1.get() != "jeudomino":
        print("Mot de passe incorrect ! \nVeuillez saisir à nouveau le mot de passe")
        e1.delete(0, 'end')
    else:
        print("Lancement du jeu...")
        joueurs()



def my_show():
    if c_v1.get() == 1:
        e1.config(show="")  # mot de passe visible
    else:
        e1.config(show="*")  # mot de passe caché


def START(event, joueur_1, joueur_2):
    global fen
    global canvas,imgs,joue_deroule,image_tk
    if joue_deroule == True:
        messagebox.showerror("Erreur","Un jeu est déjà lancé.")
        return
    joue_deroule = True
    print(event)
    print("START")

    imgs = []
    for j in range(7):
        idx = pioche()
        joueur_1.dominoes.append(idx)
        image_defaut = Image.open(domino[idx]).resize((39,79), Image.ANTIALIAS )
        position = [ 50, 160+(j*50) ]
        image = image_defaut.rotate(90, expand = True)
        imageTK = ImageTk.PhotoImage(image)
        #print("position 50 x",str(160+(j*50)),"pour le domino",domino[idx],sep=' ')
        image_id = canvas.create_image(50,160+(j*50), image=imageTK)
        joueur_1.image_dominoes.append( [position,image_id,image_defaut,image] )
        imgs.append(imageTK)

    for j in range(7):
        idx = pioche()
        joueur_2.dominoes.append(idx)
        image_defaut=Image.open(domino[idx]).resize((39,79), Image.ANTIALIAS )
        position = [ 550, 160+(j*50) ]
        image = image_defaut.rotate(90, expand = True)
        imageTK = ImageTk.PhotoImage(image)
        #print("position 550 x",str(160+(j*50)),"pour le domino",domino[idx],sep=' ')
        image_id = canvas.create_image(550,160+(j*50), image=imageTK)
        joueur_2.image_dominoes.append( [position,image_id,image_defaut,image] )
        imgs.append(imageTK)
    premier_joueur = None
    premier_piece = None
    for i in range( len(pairs) ):
        if pairs[i] in joueur_1.dominoes:
            premier_joueur = joueur_1
            premier_piece = pairs[i]
            print("Le plus grand pair trouvé",dominos_dict[pairs[i]],"pour le joueur", joueur_1.nom)
            break
        elif pairs[i] in joueur_2.dominoes:
            premier_joueur = joueur_2
            premier_piece = pairs[i]
            print("Le plus grand pair trouvé",dominos_dict[pairs[i]],"pour le joueur", joueur_2.nom)
            break
    if premier_joueur == None:
        print("Aucun pair trouvée. On cherche le plus grand nombre...")
        if max(joueur_1.dominoes) > max(joueur_2.dominoes):
            print("Le plus grand nombre trouvé",max(joueur_1.dominoes),"pour le joueur",joueur_1.nom)
            premier_piece = max(joueur_1.dominoes)
            premier_joueur = joueur_1
        elif max(joueur_2.dominoes) > max(joueur_1.dominoes):
            premier_joueur = joueur_2
            print("Le plus grand nombre trouvé",max(joueur_2.dominoes),"pour le joueur",joueur_1.nom)
            premier_piece = max(joueur_2.dominoes)
        else:
            print("Premier joueur choisi au hazard...")
            premier_joueur = random.choice( [ joueur_1, joueur_2] )
            premier_piece = random.choice( joueur_1.dominoes + joueur_2.dominoes )
    #print("joueur_1.dominoes = ",joueur_1.dominoes)
    #print("joueur_2.dominoes = ",joueur_2.dominoes)
    print("premier piece a jouer = ", dominos_dict[premier_piece] )
    image_tk = ImageTk.PhotoImage( premier_joueur.image_dominoes[ premier_joueur.dominoes.index(premier_piece) ][2] )
    image_id = premier_joueur.image_dominoes[ premier_joueur.dominoes.index(premier_piece) ][1]
    canvas.delete(image_id)
    canvas.create_image(300,300, image = image_tk, anchor = 'center' )
    print("premier joueur est",premier_joueur.nom)
    print("Placement direct de le plus grand pair au milieu")
    jouer(joueur_1, joueur_2, premier_joueur)

def jouer(joueur_1, joueur_2, premier_joueur):
    global joueur_courant
    if premier_joueur == joueur_1:
        print(joueur_1.nom,"a terminé son tour. Maintenant, c'est au tour de", joueur_2.nom )
        joueur_prochaine = joueur_2
    else:
        print(joueur_2.nom,"a terminé son tour. Maintenant, c'est au tour de", joueur_1.nom )
        joueur_prochaine = joueur_1
    joueur_courant = joueur_prochaine
    print( f"{joueur_prochaine.nom}, faites glisser votre domino à l'emplacement préféré.")
    canvas.bind('<Button 1>', lambda e, joueur_prochaine = joueur_prochaine: select_domino(e,joueur_prochaine,premier_joueur) )
    fen.bind("<Left>", deplace_gauche )
    fen.bind("<Right>", deplace_droit )
    fen.bind("<Up>", deplace_haut )
    fen.bind("<Down>", deplace_bas )

def deplace_gauche(e):
    global domino_princip, posdomino_mouve
    try:
        canvas.move(domino_princip, -5, 0)
        posdomino_mouve[0] -= 5
    except:
        print("Aucun Domino sélectionné")

def deplace_droit(e):
    global domino_princip, posdomino_mouve
    try:
        canvas.move(domino_princip, 5, 0)
        posdomino_mouve[0] += 5
    except:
        print("Aucun Domino sélectionné")

def deplace_haut(e):
    global domino_princip, posdomino_mouve
    try:
        canvas.move(domino_princip, 0, -5)
        posdomino_mouve[1] -= 5
    except:
        print("Aucun Domino sélectionné")

def deplace_bas(e):
    global domino_princip, posdomino_mouve
    try:
        canvas.move(domino_princip, 0, 5)
        posdomino_mouve[1] += 5
    except:
        print("Aucun Domino sélectionné")

def select_domino(e,joueur_prochaine,premier_joueur):
    global domino_princip, posdomino_mouve, joueur_courant
    i = 0
    for element in joueur_prochaine.image_dominoes:
        pos = element[0]
        if abs( pos[0] - e.x ) <= 50 and abs( pos[1] - e.y ) <= 20:
            print(premier_joueur.nom,"a terminé son tour. Maintenant, c'est au tour de", joueur_prochaine.nom,":")
            print("Domino sélectionné")
            posdomino_mouve = [ pos[0], pos[1] ]
            domino_princip = element[1]
            joueur_courant = joueur_prochaine
            fen.bind('r', lambda e, joueur_prochaine = joueur_prochaine, i = i: rotate_domino(e,joueur_prochaine,i) )
        i += 1
    i = 0
    for element in premier_joueur.image_dominoes:
        pos = element[0]
        if abs( pos[0] - e.x ) <= 50 and abs( pos[1] - e.y ) <= 20:
            print(joueur_prochaine.nom,"a terminé son tour. Maintenant, c'est au tour de", premier_joueur.nom,":")
            print("Domino sélectionné")
            posdomino_mouve = [ pos[0], pos[1] ]
            domino_princip = element[1]
            joueur_courant = premier_joueur
            fen.bind('r', lambda e, premier_joueur = premier_joueur, i = i:rotate_domino(e,premier_joueur,i) )
        i += 1
    #print( e.x, e.y )

def rotate_domino(e,joueur,i):
    global posdomino_mouve,img, domino_princip
    print("posdomino_mouve = ",posdomino_mouve)
    img = joueur.image_dominoes[i][3].rotate(90, expand = True)
    joueur.image_dominoes[i][3] = img
    img = ImageTk.PhotoImage( img )
    joueur.image_dominoes[i][2] = img
    canvas.delete(joueur.image_dominoes[i][1])
    joueur.image_dominoes[i][1] = canvas.create_image(posdomino_mouve[0],posdomino_mouve[1],image=img,anchor='center')
    domino_princip = joueur.image_dominoes[i][1]

def ABANDON(e, joueur_1, joueur_2 ):
    global joueur_courant
    try:
        if messagebox.askyesno("abandon", f"{joueur_courant.nom}, voulez-vous rendre?"):
            if joueur_1 == joueur_courant:
                mise_score( joueur_2 )
            else:
                mise_score( joueur_1 )
    except:
        messagebox.showerror("Erreur","pas de match trouvé. Veuillez d'abord en commencer un.")

def mise_score( gagnant ):
    win = Toplevel( bg = '#B0E0E6')
    win.geometry("600x200+500+300")
    win.overrideredirect(True)
    Label(win, text = f"Félicitations {gagnant.nom},\nvous avez gagné le match!", font = ('Times',18,'bold'), fg = '#517369' ).pack(expand = True, fill = 'both', side = 'top')
    frm = Frame(win, bg = '#B0E0E6' )
    frm.pack( expand = True, fill = 'both', side = 'bottom')
    lbl = Label(frm, text = f"Combien de points {gagnant.nom} a-t-il gagné:", bg = '#B0E0E6', fg = '#517369', font = ('Times',12,'bold') )
    lbl.pack(side = 'left', padx = 20)
    en = Entry(frm )
    en.pack(side = 'left', expand = True, fill = 'x',padx = 20)
    btn = Button(frm, text = 'Confirmer', command = lambda: refraichir_score(en.get(), gagnant, win), bg = "#6db4bf", fg = "white" )
    btn.pack( side = 'left', expand = True, fill = 'x', padx = 20)
    # win.after(3000, lambda e = None, win = win: detruire_splash(e,win) )

def refraichir_score(score_ajout,gagnant, win):
    gagnant.score += int(score_ajout)
    canvas.itemconfigure(gagnant.score_canvas, text = str(gagnant.score) )
    win.destroy()

def detruire_splash(e,win):
    win.destroy()

def PIOCHER(e):
    global domino_list, joueur_courant, imageTK
    if domino_list == []:
        messagebox.showinfo("Vide","Il n'y a plus de dominos à dessiner!")
        return
    try:
        idx = random.choice(domino_list)
        domino_list.remove(idx)
        image_defaut = Image.open(domino[idx]).resize((39,79), Image.ANTIALIAS )
        image = image_defaut.rotate(90, expand = True )
        imageTK = ImageTk.PhotoImage(image)
        image_id = canvas.create_image(300,500, image=imageTK)
        position = [ 300, 500 ]
        joueur_courant.image_dominoes.append( [position,image_id,image_defaut,image] )
        print( f"Domino {dominos_dict[idx]} a été tiré pour le joueur {joueur_courant.nom}." )
    except:
        canvas.delete(image_id)
        messagebox.showerror("Erreur","Aucun match détecté. Veuillez commencer un match en premier.")

def REJOUER(e,joueur_1,joueur_2):
    global joue_deroule, imgs, domino_list
    if not messagebox.askyesno("Rejouer","Êtes-vous sûr de vouloir recommencer depuis le début ?"):
        return
    joue_deroule = False
    joueur_1.score = joueur_2.score = 0
    canvas.itemconfigure( joueur_1.score_canvas, text = str(joueur_1.score) )
    canvas.itemconfigure( joueur_2.score_canvas, text = str(joueur_2.score) )
    joueur_1.dominoes.clear()
    joueur_2.dominoes.clear()
    for image in joueur_1.image_dominoes:
        canvas.delete(image[1])
    for image in joueur_2.image_dominoes:
        canvas.delete(image[1])
    joueur_1.image_dominoes.clear()
    joueur_2.image_dominoes.clear()
    imgs.clear()
    domino_list = [ x for x in range(0,28) ]
    START(e,joueur_1,joueur_2)

def QUITTER(e,fen):
    fen.destroy()

def fen_detruire():
    exit()

def show(Nom_du_joueur,noms,app):
    nom = Nom_du_joueur.get()
    noms.append(nom)
    #print(p)
    app.destroy()

def joueurs():
    noms=[]
    fen.destroy()
    for joueurs in range(2):
        app = TK.Tk()
        app.iconbitmap("lib/domino.ico")
        app.title("Saisie nom des joueurs")
        app.geometry('400x400')
        canvas=TK.Canvas(background="#B0E0E6",height=300,width=300)
        img0=TK.PhotoImage(file="lib/joueur_image.PNG")
        canvas.create_image(150,150,image=img0)
        canvas.pack()
        Nom_du_joueur = TK.StringVar()
        nomEntry = TK.Entry(app, textvariable=Nom_du_joueur).pack()
        sumbmit = TK.Button(app, text='Saisir le nom des joueurs',command=lambda Nom_du_joueur = Nom_du_joueur, app = app:show(Nom_du_joueur,noms,app)).pack()
        app.mainloop()

    print(noms)
    application(noms)

def application(noms):
    global canvas, fen
    fen = TK.Tk()
    fen.title("Jeu de Domino")
    fen.iconbitmap("lib/domino.ico")
    canvas=Canvas(fen,width=600,height=600,background='#B0E0E6')

    #1ère ligne du quadrillage
    c11=Canvas.create_rectangle(canvas,100,100,140,140, fill="white")
    c12=Canvas.create_rectangle(canvas,140,100,180,140, fill="white")
    c13=Canvas.create_rectangle(canvas,180,100,220,140, fill="white")
    c14=Canvas.create_rectangle(canvas,220,100,260,140, fill="white")
    c15=Canvas.create_rectangle(canvas,260,100,300,140, fill="white")
    c16=Canvas.create_rectangle(canvas,300,100,340,140, fill="white")
    c17=Canvas.create_rectangle(canvas,340,100,380,140, fill="white")
    c18=Canvas.create_rectangle(canvas,380,100,420,140, fill="white")
    c19=Canvas.create_rectangle(canvas,420,100,460,140, fill="white")
    c1A=Canvas.create_rectangle(canvas,460,100,500,140, fill="white")

    #2ème ligne
    c21=Canvas.create_rectangle(canvas,100,140,140,180, fill="white")
    c22=Canvas.create_rectangle(canvas,140,140,180,180, fill="white")
    c23=Canvas.create_rectangle(canvas,180,140,220,180, fill="white")
    c24=Canvas.create_rectangle(canvas,220,140,260,180, fill="white")
    c25=Canvas.create_rectangle(canvas,260,140,300,180, fill="white")
    c26=Canvas.create_rectangle(canvas,300,140,340,180, fill="white")
    c27=Canvas.create_rectangle(canvas,340,140,380,180, fill="white")
    c28=Canvas.create_rectangle(canvas,380,140,420,180, fill="white")
    c29=Canvas.create_rectangle(canvas,420,140,460,180, fill="white")
    c2A=Canvas.create_rectangle(canvas,460,140,500,180, fill="white")

    #3ème ligne
    c31=Canvas.create_rectangle(canvas,100,180,140,220, fill="white")
    c32=Canvas.create_rectangle(canvas,140,180,180,220, fill="white")
    c33=Canvas.create_rectangle(canvas,180,180,220,220, fill="white")
    c34=Canvas.create_rectangle(canvas,220,180,260,220, fill="white")
    c35=Canvas.create_rectangle(canvas,260,180,300,220, fill="white")
    c36=Canvas.create_rectangle(canvas,300,180,340,220, fill="white")
    c37=Canvas.create_rectangle(canvas,340,180,380,220, fill="white")
    c38=Canvas.create_rectangle(canvas,380,180,420,220, fill="white")
    c39=Canvas.create_rectangle(canvas,420,180,460,220, fill="white")
    c3A=Canvas.create_rectangle(canvas,460,180,500,220, fill="white")

    #4ème ligne
    c41=Canvas.create_rectangle(canvas,100,220,140,260, fill="white")
    c42=Canvas.create_rectangle(canvas,140,220,180,260, fill="white")
    c43=Canvas.create_rectangle(canvas,180,220,220,260, fill="white")
    c44=Canvas.create_rectangle(canvas,220,220,260,260, fill="white")
    c45=Canvas.create_rectangle(canvas,260,220,300,260, fill="white")
    c46=Canvas.create_rectangle(canvas,300,220,340,260, fill="white")
    c47=Canvas.create_rectangle(canvas,340,220,380,260, fill="white")
    c48=Canvas.create_rectangle(canvas,380,220,420,260, fill="white")
    c49=Canvas.create_rectangle(canvas,420,220,460,260, fill="white")
    c4A=Canvas.create_rectangle(canvas,460,220,500,260, fill="white")

    #5ème ligne
    c51=Canvas.create_rectangle(canvas,100,260,140,300, fill="white")
    c52=Canvas.create_rectangle(canvas,140,260,180,300, fill="white")
    c53=Canvas.create_rectangle(canvas,180,260,220,300, fill="white")
    c54=Canvas.create_rectangle(canvas,220,260,260,300, fill="white")
    c55=Canvas.create_rectangle(canvas,260,260,300,300, fill="white")
    c56=Canvas.create_rectangle(canvas,300,260,340,300, fill="white")
    c57=Canvas.create_rectangle(canvas,340,260,380,300, fill="white")
    c58=Canvas.create_rectangle(canvas,380,260,420,300, fill="white")
    c59=Canvas.create_rectangle(canvas,420,260,460,300, fill="white")
    c5A=Canvas.create_rectangle(canvas,460,260,500,300, fill="white")

    #6ème ligne
    c61=Canvas.create_rectangle(canvas,100,300,140,340, fill="white")
    c62=Canvas.create_rectangle(canvas,140,300,180,340, fill="white")
    c63=Canvas.create_rectangle(canvas,180,300,220,340, fill="white")
    c64=Canvas.create_rectangle(canvas,220,300,260,340, fill="white")
    c65=Canvas.create_rectangle(canvas,260,300,300,340, fill="white")
    c66=Canvas.create_rectangle(canvas,300,300,340,340, fill="white")
    c67=Canvas.create_rectangle(canvas,340,300,380,340, fill="white")
    c68=Canvas.create_rectangle(canvas,380,300,420,340, fill="white")
    c69=Canvas.create_rectangle(canvas,420,300,460,340, fill="white")
    c6A=Canvas.create_rectangle(canvas,460,300,500,340, fill="white")

    #7ème ligne
    c71=Canvas.create_rectangle(canvas,100,340,140,380, fill="white")
    c72=Canvas.create_rectangle(canvas,140,340,180,380, fill="white")
    c73=Canvas.create_rectangle(canvas,180,340,220,380, fill="white")
    c74=Canvas.create_rectangle(canvas,220,340,260,380, fill="white")
    c75=Canvas.create_rectangle(canvas,260,340,300,380, fill="white")
    c76=Canvas.create_rectangle(canvas,300,340,340,380, fill="white")
    c77=Canvas.create_rectangle(canvas,340,340,380,380, fill="white")
    c78=Canvas.create_rectangle(canvas,380,340,420,380, fill="white")
    c79=Canvas.create_rectangle(canvas,420,340,460,380, fill="white")
    c7A=Canvas.create_rectangle(canvas,460,340,500,380, fill="white")

    #8ème ligne
    c81=Canvas.create_rectangle(canvas,100,380,140,420, fill="white")
    c82=Canvas.create_rectangle(canvas,140,380,180,420, fill="white")
    c83=Canvas.create_rectangle(canvas,180,380,220,420, fill="white")
    c84=Canvas.create_rectangle(canvas,220,380,260,420, fill="white")
    c85=Canvas.create_rectangle(canvas,260,380,300,420, fill="white")
    c86=Canvas.create_rectangle(canvas,300,380,340,420, fill="white")
    c87=Canvas.create_rectangle(canvas,340,380,380,420, fill="white")
    c88=Canvas.create_rectangle(canvas,380,380,420,420, fill="white")
    c89=Canvas.create_rectangle(canvas,420,380,460,420, fill="white")
    c8A=Canvas.create_rectangle(canvas,460,380,500,420, fill="white")

    #9ème ligne
    c91=Canvas.create_rectangle(canvas,100,420,140,460, fill="white")
    c92=Canvas.create_rectangle(canvas,140,420,180,460, fill="white")
    c93=Canvas.create_rectangle(canvas,180,420,220,460, fill="white")
    c94=Canvas.create_rectangle(canvas,220,420,260,460, fill="white")
    c95=Canvas.create_rectangle(canvas,260,420,300,460, fill="white")
    c96=Canvas.create_rectangle(canvas,300,420,340,460, fill="white")
    c97=Canvas.create_rectangle(canvas,340,420,380,460, fill="white")
    c98=Canvas.create_rectangle(canvas,380,420,420,460, fill="white")
    c99=Canvas.create_rectangle(canvas,420,420,460,460, fill="white")
    c9A=Canvas.create_rectangle(canvas,460,420,500,460, fill="white")


    #dernière ligne
    cA1=Canvas.create_rectangle(canvas,100,460,140,500, fill="white")
    cA2=Canvas.create_rectangle(canvas,140,460,180,500, fill="white")
    cA3=Canvas.create_rectangle(canvas,180,460,220,500, fill="white")
    cA4=Canvas.create_rectangle(canvas,220,460,260,500, fill="white")
    cA5=Canvas.create_rectangle(canvas,260,460,300,500, fill="white")
    cA6=Canvas.create_rectangle(canvas,300,460,340,500, fill="white")
    cA7=Canvas.create_rectangle(canvas,340,460,380,500, fill="white")
    cA8=Canvas.create_rectangle(canvas,380,460,420,500, fill="white")
    cA9=Canvas.create_rectangle(canvas,420,460,460,500, fill="white")
    cAA=Canvas.create_rectangle(canvas,460,460,500,500, fill="white")

    font3=('Times',30,'bold')
    if len( noms ) < 1:
        noms = [ 'defaut', 'defaut' ]
    elif len( noms ) < 2:
        noms.append( 'defaut' )
    joueur_1 = joueur(noms[0])
    joueur_2 = joueur(noms[1])
    Canvas.create_text(canvas, 300, 55, text="SCORE", font=font3, fill="#517369")
    joueur_1.score_canvas = Canvas.create_text(canvas, 50, 55, text= str(joueur_1.score), font=font3, fill="#517369" )
    joueur_2.score_canvas = Canvas.create_text(canvas, 550, 55, text= str(joueur_2.score), font=font3, fill="#517369")
    Canvas.create_text(canvas, 50, 105, text=noms[0])
    Canvas.create_text(canvas, 550, 105, text=noms[1])

    """
    #file="C:\\Users\\leila\\OneDrive\\Bureau\\joueur_image.PNG")

    img9=TK.PhotoImage(file = "domino/domino-5_6.png")
    canvas.create_image((120,140),image = img9)

    img7=TK.PhotoImage(file = "domino/domino-6_6.png")
    canvas.create_image((120,220),image = img7)
    """


    d11=canvas.create_rectangle(10,140,90,180, fill="white")
    d12=canvas.create_rectangle(10,190,90,230, fill="white")
    d13=canvas.create_rectangle(10,240,90,280, fill="white")
    d14=canvas.create_rectangle(10,290,90,330, fill="white")
    d15=canvas.create_rectangle(10,340,90,380, fill="white")
    d16=canvas.create_rectangle(10,390,90,430, fill="white")
    d17=canvas.create_rectangle(10,440,90,480, fill="white")

    d21=canvas.create_rectangle(510,140,590,180, fill="white")
    d22=canvas.create_rectangle(510,190,590,230, fill="white")
    d23=canvas.create_rectangle(510,240,590,280, fill="white")
    d24=canvas.create_rectangle(510,290,590,330, fill="white")
    d25=canvas.create_rectangle(510,340,590,380, fill="white")
    d26=canvas.create_rectangle(510,390,590,430, fill="white")
    d27=canvas.create_rectangle(510,440,590,480, fill="white")

    #Ajouter le bouton start
    B1=Canvas.create_rectangle(canvas,60,530,130,580, fill="#6db4bf", tags = "START-Button")
    B2=Canvas.create_rectangle(canvas,160,530,230,580, fill="#6db4bf", tags = "ABANDON-Button")
    B3=Canvas.create_oval(canvas,250,520,340,590, fill="#6db4bf", tags = "PIOCHER-Button")
    B4=Canvas.create_rectangle(canvas,360,530,430,580, fill="#6db4bf", tags = "REJOUER-Button")
    B5=Canvas.create_rectangle(canvas,460,530,530,580, fill="#6db4bf", tags = "QUITTER-Button")

    font1=('Calibri',11,'bold')

    #Ajouter le nom de chaque bouton

    Canvas.create_text(canvas, 95, 555, text= "START",font=font1, fill="white", tags = "START-Button")
    Canvas.create_text(canvas, 195, 555, text= "ABANDON",font=font1, fill="white", tags = "ABANDON-Button")
    Canvas.create_text(canvas, 295, 555, text= "PIOCHER",font=font1, fill="white", tags = "PIOCHER-Button")
    Canvas.create_text(canvas, 395, 555, text= "REJOUER",font=font1, fill="white", tags = "REJOUER-Button")
    Canvas.create_text(canvas, 495, 555, text= "QUITTER",font=font1, fill="white", tags = "QUITTER-Button")
    canvas.pack()


    #Ajout des actions aux boutons
    canvas.tag_bind("START-Button","<Button-1>", lambda e, joueur_1 = joueur_1, joueur_2 = joueur_2: START(e,joueur_1,joueur_2))
    canvas.tag_bind("ABANDON-Button","<Button-1>", lambda e, joueur_1 = joueur_1, joueur_2 = joueur_2: ABANDON(e,joueur_1,joueur_2))
    canvas.tag_bind("PIOCHER-Button","<Button-1>",PIOCHER)
    canvas.tag_bind("REJOUER-Button","<Button-1>", lambda e, joueur_1 = joueur_1, joueur_2 = joueur_2:REJOUER(e,joueur_1,joueur_2))
    canvas.tag_bind("QUITTER-Button","<Button-1>",lambda e, fen = fen:QUITTER(e,fen))


    #canvas.pack()

    fen.mainloop()

joue_deroule = False
if __name__=='__main__':
    rundir= os.getcwd()
    print(rundir)

    fen = TK.Tk()
    fen.iconbitmap("lib/domino.ico")
    fen.title("login")
    fen.geometry("350x100")
    fen.configure(bg="#B0E0E6")
    fen.protocol( "WM_DELETE_WINDOW" , fen_detruire )
    font2 = ("Times", 16, "bold")
    l1 = TK.Label(fen, text="Mot de passe :", font=font2, bg="#B0E0E6")
    l1.grid(row=1, column=1, padx=10, pady=10)
    e1 = TK.Entry(fen, font=font2, width=15, show="*")
    e1.grid(row=1, column=2, padx=5, pady=5)
    e1.bind("<Return>", password)
    c_v1 = IntVar(value=0)
    c1 = TK.Checkbutton(fen, text="Afficher", variable=c_v1, onvalue=1, offvalue=0, command=my_show, bg="#B0E0E6")
    c1.grid(row=2, column=1)
    fen.mainloop()