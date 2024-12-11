from tkiteasy1 import *
from cooking import Pokemon
from IAautiste1 import Debile
from Code import IAPOKEBETE
from IAminmax import Minmax
from playsound import playsound
import threading

dimMorpion = 800

class Morpion :

    def __init__(self):
        threading.Thread(target=self.play_music_loop, daemon=True).start()
        self.g = ouvrirFenetre(1532,800)
        self.niveauIA = 1
        self.modeJeu = 1
        self.minmax = Minmax(self,self.g)
        self.cooking = Pokemon(self,self.g)
        self.IABETE = Debile(self,self.g)
        self.pokebete = IAPOKEBETE(self,self.g)
        self.nbp = 64
        self.menu()

    def play_music_loop(self):
        # Boucle de lecture infinie avec playsound
        while True:
            playsound("./theme.mp3")


    def menu(self):
        menu = self.g.afficherImage(0, 0, "./MenuPokemon.png")
        #testjeusolo = self.g.dessinerRectangle(950,645,470,55,"white")
        #settings = self.g.afficherImage(1300, 700, "./Settings.png",150,75)
        while True:
            cliquesouris = self.g.attendreClic()
            if 950<cliquesouris.x<1420  and 645 <cliquesouris.y<700:
                self.g.supprimerTout()
                if self.niveauIA==1 and self.modeJeu==2:
                    self.IABETE.Jeuautiste()
                if self.niveauIA == 1 and self.modeJeu == 1:
                    self.pokebete.JeuPoke(self.nbp)
                if self.niveauIA == 2:
                    self.minmax.Jeumin()

            if 950 < cliquesouris.x < 1420 and 585 < cliquesouris.y < 635:
                self.g.supprimerTout()
                if self.modeJeu == 1:
                    self.cooking.JeuPoke(self.nbp)
                else:
                    self.Jeu()

            if 950 < cliquesouris.x<1420 and 710<cliquesouris.y<765:
                self.g.supprimerTout()
                self.settings()

    def choixmode(self):
        if self.modeJeu == 1:
            texte = "Avec Pokémon"
        else:
            texte = "Sans Pokémon"
        if self.niveauIA == 1:
            texteIA = "Niveau de l'IA : Facile"
        else:
            texteIA = "Niveau de l'IA : Difficile"
        return texte,texteIA

    def settings(self):
        texte = self.choixmode()[0]
        texteIA = self.choixmode()[1]
        settings = self.g.afficherImage(0, 0, "./MenuSettings.png")
        choimode = self.g.afficherTexte(texte,770,310,col="darkblue",sizefont=25)
        choilvlIA = self.g.afficherTexte(texteIA,770,510,col="beige",sizefont=25)
        nombrepokemon = self.g.afficherTexte(f"Nombre de Pokémon : {self.nbp}",770,410,col="beige",sizefont=25)
        self.g.dessinerRectangle(1000,295,35,35,col="darkblue")
        self.g.dessinerRectangle(505,295,35,35,col="darkblue")
        self.g.dessinerRectangle(505,395,35,35,col="beige")
        self.g.dessinerRectangle(1000,395,35,35,col="beige")
        self.g.dessinerRectangle(1000,495,35,35,col="beige")
        self.g.dessinerRectangle(505, 495, 35, 35, col="beige")
        while True:

            cliquesouris = self.g.attendreClic()
            if 505<cliquesouris.x<540 and 495<cliquesouris.y<530:
                self.niveauIA = 3-self.niveauIA
                texteIA = self.choixmode()[1]
                self.g.changerTexte(choilvlIA,texteIA)

            if 1000<cliquesouris.x<1035 and 495<cliquesouris.y<530:
                self.niveauIA = 3-self.niveauIA
                texteIA = self.choixmode()[1]
                self.g.changerTexte(choilvlIA,texteIA)

            if 14 < cliquesouris.x<75 and 629<cliquesouris.y<689:
                self.g.supprimerTout()
                self.menu()

            if 1000<cliquesouris.x<1035 and 295<cliquesouris.y<330:
                self.modeJeu = 3-self.modeJeu
                texte = self.choixmode()[0]
                self.g.changerTexte(choimode,texte)

            if 505<cliquesouris.x<540 and 295<cliquesouris.y<330:
                self.modeJeu = 3-self.modeJeu
                texte = self.choixmode()[0]
                self.g.changerTexte(choimode,texte)

            if 505<cliquesouris.x<540 and 395<cliquesouris.y<430 :
                self.nbp -= 1
                if self.nbp==41:
                    self.nbp=800
                self.g.changerTexte(nombrepokemon,f"Nombre de Pokémon : {self.nbp}")

            if 1000<cliquesouris.x<1035 and 395<cliquesouris.y<430:
                self.nbp+=1
                if self.nbp == 801:
                    self.nbp = 42
                self.g.changerTexte(nombrepokemon,f"Nombre de Pokémon : {self.nbp}")


    def Jeu(self):
        self.g.dessinerDisque(1345,74,26,"white")
        self.g.afficherImage(1300,30,"./Home.png",90,90)
        self.joueur = self.g.afficherImage(1000,150,"./Joueur 1.png")
        self.j = self.g.afficherImage(1532-435,325,"./Tortank.png")
        #j2 = self.g.afficherImage(dimMorpion+5,325,"./dracaufeu.png")
        self.l1 = [0 for _ in range(9)]
        self.l2 = [0 for _ in range(9)]
        self.l3 = [0 for _ in range(9)]
        self.l4 = [0 for _ in range(9)]
        self.l5 = [0 for _ in range(9)]
        self.l6 = [0 for _ in range(9)]
        self.l7 = [0 for _ in range(9)]
        self.l8 = [0 for _ in range(9)]
        self.l9 = [0 for _ in range(9)]
        # Dictionnaire pour associer les grandes cases aux listes
        self.lists = {
            1: self.l1,
            2: self.l2,
            3: self.l3,
            4: self.l4,
            5: self.l5,
            6: self.l6,
            7: self.l7,
            8: self.l8,
            9: self.l9
        }
        self.ban = {}
        self.win = {}
        self.victoire = {}
        self.MegaGrille = [0 for _ in range(9)]

        for i in range(1,3):
            self.g.placerAuDessous(self.g.dessinerLigne(i * dimMorpion/3, 0, i * dimMorpion/3, dimMorpion , "white",ep=5))
            self.g.placerAuDessous(self.g.dessinerLigne(0,dimMorpion/3 * i, dimMorpion, dimMorpion/3 * i, "white",ep=5))
        for i in range(3):
            for j in range(3):
                self.g.placerAuDessous(self.dessinerPetiteGrille(i, j))
        self.g.placerAuDessous(self.g.dessinerLigne(dimMorpion,0,dimMorpion,dimMorpion,"white",ep=5))
        self.g.placerAuDessous(self.g.dessinerLigne(0,dimMorpion,dimMorpion,dimMorpion,"white",ep=5))
        self.g.placerAuDessous(self.g.dessinerLigne(0,0,0,dimMorpion,"white",ep=5))
        self.g.placerAuDessous(self.g.dessinerLigne(0,0,dimMorpion,0,"white",ep=5))
        encadre = None
        joueur = 1
        cliquable = None

        while True:


            clic = self.g.attendreClic()
            self.win = {}

            if (((clic.x - 1345)) ** 2 + ((clic.y - 74)) ** 2) ** 0.5 <= 26:
                self.g.supprimerTout()
                self.menu()

            if 0 < clic.x < dimMorpion and 0 < clic.y < dimMorpion:


                grande_case, petite_case = self.determinerCase(clic.x, clic.y)
                if grande_case in self.ban:
                    print(f"Vous devez jouer dans une autre grande case. La grande case {grande_case} est bannie.")
                    continue

                if (grande_case == cliquable and encadre!=None):
                    if self.lists[grande_case][petite_case-1]==0:

                        self.g.supprimer(encadre)
                        encadre = None


                if cliquable is not None and grande_case != cliquable :
                    print(f"Vous devez jouer dans la grande case {cliquable}.")

                    continue

                if self.RemplirGrille(grande_case, petite_case, joueur):
                    self.Regle(grande_case, joueur)
                    cliquable = self.Transfert(grande_case,petite_case)
                    joueur = 3 - joueur
                    self.alterner(joueur)


                    if cliquable is not None :
                        xc,yc = self.dessinerEncadrement(cliquable)
                        encadre = self.g.dessinerRectangle(xc,yc,dimMorpion/3,dimMorpion/3,col="purple")
                        self.g.placerAuDessous(encadre)


    def alterner(self,joueur):
        if joueur == 1:
            self.g.supprimer(self.j)
            self.g.supprimer(self.joueur)
            self.j = self.g.afficherImage(1532-435,325,"./Tortank.png")
            self.joueur = self.g.afficherImage(1000,150,"./Joueur 1.png")
        else:
            self.g.supprimer(self.joueur)
            self.g.supprimer(self.j)
            self.j = self.g.afficherImage(dimMorpion+5,325,"./dracaufeu.png")
            self.joueur = self.g.afficherImage(1000,150,"./Joueur 2.png")

    def Regle(self,grande_case,joueur):
        x = None
        if joueur == 1 :
            x =1
        else :
            joueur = 2
        liste = self.lists[grande_case]
        if ((liste[0] == liste[1] == liste[2]) and liste[0]!=0 ) or ((liste[3] == liste[4] == liste[5]) and liste[3]!=0 ) or ((liste[6] == liste[7] == liste[8]) and liste[6]!=0 ) or ((liste[0] == liste[4] == liste[8]) and liste[0]!=0 ) or ((liste[0] == liste[3] == liste[6]) and liste[0]!=0 ) or ((liste[1] == liste[4] == liste[7]) and liste[1]!=0) or ((liste[2] == liste[5] == liste[8]) and liste[2]!=0) or ((liste[6] == liste[4] == liste[2]) and liste[6]!=0)  :
            self.MegaGrille[grande_case-1] = joueur
            self.ban[grande_case] = self.lists[grande_case]
            self.win[grande_case] = self.lists[grande_case]
            self.victoire[grande_case] = joueur
            print(self.ban)
            self.dessinerCroix(grande_case, joueur)
            self.Finale(joueur)

    def ecranvictoire(self,joueur):

        self.g.afficherImage(0,0,"./fondviictoire.png")
        if joueur == 1:
            self.g.afficherImage(600,150,"./Joueur 1.png")
        else:
            self.g.afficherImage(600,150,"./Joueur 2.png")
        self.g.afficherImage(600,300,"./gagne.png")

    def ecrangalite(self):
        self.g.afficherImage(0,0,"./fondviictoire.png")
        self.g.afficherImage(600,300,"./egalite.png")

    def Finale(self,joueur):
        if ((self.MegaGrille[0] == self.MegaGrille[1] == self.MegaGrille[2]) and self.MegaGrille[0]!=0 ) or ((self.MegaGrille[3] == self.MegaGrille[4] == self.MegaGrille[5]) and self.MegaGrille[3]!=0 ) or ((self.MegaGrille[6] == self.MegaGrille[7] == self.MegaGrille[8]) and self.MegaGrille[6]!=0 ) or ((self.MegaGrille[0] == self.MegaGrille[4] == self.MegaGrille[8]) and self.MegaGrille[0]!=0 ) or ((self.MegaGrille[0] == self.MegaGrille[3] == self.MegaGrille[6]) and self.MegaGrille[0]!=0 ) or ((self.MegaGrille[1] == self.MegaGrille[4] == self.MegaGrille[7]) and self.MegaGrille[1]!=0) or ((self.MegaGrille[2] == self.MegaGrille[5] == self.MegaGrille[8]) and self.MegaGrille[2]!=0) or ((self.MegaGrille[6] == self.MegaGrille[4] == self.MegaGrille[2]) and self.MegaGrille[6]!=0) :

            self.g.supprimerTout()
            self.ecranvictoire(joueur)
            self.g.attendreClic()
            self.g.supprimerTout()
            self.menu()

        if all(i!=0 for i in self.MegaGrille):
            self.ecrangalite()
            self.g.attendreClic()
            self.g.supprimerTout()
            self.menu()


    def dessinerCroix(self, grande_case, joueur):
        taille = dimMorpion / 3
        colonne = (grande_case -1) % 3
        ligne = (grande_case -1)  // 3
        x = (taille * colonne )
        y = (taille* ligne )
        x1 = x+taille
        y1 = y+taille
        yc= (y1+y)/2
        xc = (x1 + x) / 2
        couleur = "royalblue" if joueur == 1 else "tomato"
        forme = "x" if joueur ==1 else "o"
        self.g.dessinerRectangle(x+3,y+3,taille-5,taille-5, couleur)
        self.g.afficherTexte(forme,xc,yc-(taille/8),"white",sizefont = int(taille))


    def dessinerEncadrement(self, grande_case):
        TaillGC = dimMorpion / 3
        colonne_grande = (grande_case - 1) % 3
        ligne_grande = (grande_case - 1) // 3
        x0 = colonne_grande * TaillGC
        y0 = ligne_grande * TaillGC
        return x0,y0


    def Affichage(self,grande_case,petite_case, joueur):
        taille_grande_case = dimMorpion / 3
        taille_petite_case = taille_grande_case / 3
        # Indices de la grande case
        ligne_grande = (grande_case - 1) // 3
        colonne_grande = (grande_case - 1) % 3
        # Indices de la petite case
        ligne_petite = (petite_case - 1) // 3
        colonne_petite = (petite_case - 1) % 3
        # Calcul des coordonnées du centre
        x = (colonne_grande * taille_grande_case + colonne_petite * taille_petite_case
             + taille_petite_case / 2)
        y = (ligne_grande * taille_grande_case + ligne_petite * taille_petite_case
             + taille_petite_case / 2)
        xc = x - taille_petite_case/2
        yc = y - taille_petite_case/2
        if joueur == 1 :
            self.g.afficherTexte("X",x,y, "white",sizefont = int(taille_petite_case/2))
            self.g.placerAuDessous(self.g.dessinerRectangle(xc,yc,taille_petite_case,taille_petite_case,"royalblue"))
        if joueur == 2 :
            self.g.afficherTexte("O",x,y, "white",sizefont = int(taille_petite_case/2))
            self.g.placerAuDessous(self.g.dessinerRectangle(xc,yc,taille_petite_case,taille_petite_case,"tomato"))

    def Transfert(self,grande_case, petite_case):
        liste = self.lists[petite_case]
        if petite_case in self.ban:
            return None
        if grande_case in self.win:
            return petite_case
        if grande_case in self.ban:
            return None
        if all(i != 0 for i in liste) :
            return None
        else :
            return petite_case

    def RemplirGrille(self,grande_case, petite_case,joueur):
        print(joueur)
        J = None
        if joueur % 2 == 0:
            J = 2
        else :
            J=1        #Verification
        if self.lists[grande_case][petite_case-1] == 0:
            self.lists[grande_case][petite_case-1] = joueur
            self.Affichage(grande_case,petite_case, joueur)
            return True
        else:
            print(f"Case {petite_case} dans la grande case {grande_case} déjà occupée !")
            return False


    def dessinerPetiteGrille(self, i, j):
        x0 = j * dimMorpion / 3
        y0 = i * dimMorpion / 3
        x1 = x0 + dimMorpion / 3
        y1 = y0 + dimMorpion / 3

        for k in range(1, 3):
            self.g.dessinerLigne(x0 + k * (dimMorpion / 9), y0, x0 + k * (dimMorpion / 9), y1, "white")
            self.g.dessinerLigne(x0, y0 + k * (dimMorpion / 9), x1, y0 + k * (dimMorpion / 9), "white")



    def determinerCase(self, x, y):
        taille_case_grande_x = dimMorpion / 3
        taille_case_grande_y = dimMorpion / 3
        taille_case_petite_x = dimMorpion / 9
        taille_case_petite_y = dimMorpion / 9

        # Trouver la grande case
        colonne_grande = int(x // taille_case_grande_x)
        ligne_grande = int(y // taille_case_grande_y)
        numero_grande_case = ligne_grande * 3 + colonne_grande + 1

        # Trouver la petite case dans la grande case
        x_relative = x % taille_case_grande_x
        y_relative = y % taille_case_grande_y
        colonne_petite = int(x_relative // taille_case_petite_x)
        ligne_petite = int(y_relative // taille_case_petite_y)
        numero_petite_case = ligne_petite * 3 + colonne_petite + 1

        return numero_grande_case, numero_petite_case





Morpion()