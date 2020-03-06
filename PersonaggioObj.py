# -*- coding: utf-8 -*-

from GenericFuncG2 import *


class PersonaggioObj(object):

    def __init__(self, x, y, direzione, tipo, avanzamentoStoria):
        self.x = x
        self.y = y

        self.tipo = tipo
        self.oggettoDato = False
        self.avanzamentoStoria = False
        self.menuMercante = False

        self.caricaImg()
        self.girati(direzione)
        self.aggiornaDialogo(avanzamentoStoria)

    def caricaImg(self):
        imgW = pygame.image.load("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "W.png")
        self.imgW = pygame.transform.scale(imgW, (gpx, gpy))
        imgA = pygame.image.load("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "A.png")
        self.imgA = pygame.transform.scale(imgA, (gpx, gpy))
        imgS = pygame.image.load("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "S.png")
        self.imgS = pygame.transform.scale(imgS, (gpx, gpy))
        imgD = pygame.image.load("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "D.png")
        self.imgD = pygame.transform.scale(imgD, (gpx, gpy))

    def girati(self, direzione):
        if direzione == "w":
            self.imgAttuale = self.imgW
        elif direzione == "a":
            self.imgAttuale = self.imgA
        elif direzione == "s":
            self.imgAttuale = self.imgS
        elif direzione == "d":
            self.imgAttuale = self.imgD
        self.direzione = direzione

    def aggiornaDialogo(self, avanzamentoStoria):
        if self.tipo == "Mercante":
            self.partiDialogo = []
            self.nome = "Bob"
            if avanzamentoStoria == 0:
                self.oggettoDato = False
                self.avanzamentoStoria = False
                self.menuMercante = True
                dialogo = []
                dialogo.append("Ciao,")
                dialogo.append("ecco la merce")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("Ecco la merceee")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == 1:
                self.oggettoDato = "oggetto speciale"
                self.avanzamentoStoria = True
                self.menuMercante = False
                dialogo = []
                dialogo.append("Ciao,")
                dialogo.append(u"la merce è finita")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append(u"È finitaaa")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzamentoStoria = False
                self.menuMercante = False
                dialogo = []
                dialogo.append("Vattene")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
        if self.tipo == "Tizio":
            self.partiDialogo = []
            self.nome = "Tiz"
            if avanzamentoStoria == 0:
                self.oggettoDato = False
                self.avanzamentoStoria = True
                self.menuMercante = False
                dialogo = []
                dialogo.append(u"Ho compato tutto ciò che aveva il mercante")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzamentoStoria = False
                self.menuMercante = False
                dialogo = []
                dialogo.append("Muhahahaha")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
