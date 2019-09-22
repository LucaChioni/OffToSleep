# -*- coding: utf-8 -*-

from GenericFuncG2 import *

class NemicoObj(object):

    def __init__(self, x, y, direzione, tipo, stanza):
        self.x = x
        self.y = y
        self.vx = x
        self.vy = y
        self.avvelenato = False
        self.appiccicato = False
        self.visto = False
        self.stanzaDiAppartenenza = stanza
        self.morto = False

        self.tipo = tipo
        vitaTotale = 0
        esp = 0
        raggioVisivo = 0
        velocita = 0
        attacco = 0
        attaccaDaLontano = False
        if self.tipo == "Orco":
            vitaTotale = 50
            esp = 10
            raggioVisivo = gpx * 4
            velocita = -1
            attacco = 50
            attaccaDaLontano = False
        if self.tipo == "Pipistrello":
            vitaTotale = 20
            esp = 5
            raggioVisivo = gpx * 6
            velocita = 1
            attacco = 20
            attaccaDaLontano = False
        self.vita = vitaTotale
        self.vitaTotale = vitaTotale
        self.esp = esp
        self.raggioVisivo = raggioVisivo
        self.velocita = velocita
        self.mosseRimaste = 0
        self.attacco = attacco
        self.attaccaDaLontano = attaccaDaLontano
        self.anima = False

        imgW = pygame.image.load("Immagini\Mostri\\" + tipo + "w.png")
        self.imgW = pygame.transform.scale(imgW, (gpx, gpy))
        imgA = pygame.image.load("Immagini\Mostri\\" + tipo + "a.png")
        self.imgA = pygame.transform.scale(imgA, (gpx, gpy))
        imgS = pygame.image.load("Immagini\Mostri\\" + tipo + "s.png")
        self.imgS = pygame.transform.scale(imgS, (gpx, gpy))
        imgD = pygame.image.load("Immagini\Mostri\\" + tipo + "d.png")
        self.imgD = pygame.transform.scale(imgD, (gpx, gpy))
        self.girati(direzione)
        self.direzione = direzione

        imgWMov1 = pygame.image.load("Immagini\Mostri\\" + tipo + "wMov1.png")
        self.imgWMov1 = pygame.transform.scale(imgWMov1, (gpx, gpy))
        imgWMov2 = pygame.image.load("Immagini\Mostri\\" + tipo + "wMov2.png")
        self.imgWMov2 = pygame.transform.scale(imgWMov2, (gpx, gpy))
        imgAMov1 = pygame.image.load("Immagini\Mostri\\" + tipo + "aMov1.png")
        self.imgAMov1 = pygame.transform.scale(imgAMov1, (gpx, gpy))
        imgAMov2 = pygame.image.load("Immagini\Mostri\\" + tipo + "aMov2.png")
        self.imgAMov2 = pygame.transform.scale(imgAMov2, (gpx, gpy))
        imgSMov1 = pygame.image.load("Immagini\Mostri\\" + tipo + "sMov1.png")
        self.imgSMov1 = pygame.transform.scale(imgSMov1, (gpx, gpy))
        imgSMov2 = pygame.image.load("Immagini\Mostri\\" + tipo + "sMov2.png")
        self.imgSMov2 = pygame.transform.scale(imgSMov2, (gpx, gpy))
        imgDMov1 = pygame.image.load("Immagini\Mostri\\" + tipo + "dMov1.png")
        self.imgDMov1 = pygame.transform.scale(imgDMov1, (gpx, gpy))
        imgDMov2 = pygame.image.load("Immagini\Mostri\\" + tipo + "dMov2.png")
        self.imgDMov2 = pygame.transform.scale(imgDMov2, (gpx, gpy))

        imgAvvelenamento = pygame.image.load("Immagini\Mostri\\" + tipo + "Avvele.png")
        self.imgAvvelenamento = pygame.transform.scale(imgAvvelenamento, (gpx, gpy))
        imgAppiccicato = pygame.image.load("Immagini\Mostri\\" + tipo + "Appicc.png")
        self.imgAppiccicato = pygame.transform.scale(imgAppiccicato, (gpx, gpy))

    def girati(self, direzione):
        if direzione == "w":
            self.imgAttuale = self.imgW
        elif direzione == "a":
            self.imgAttuale = self.imgA
        elif direzione == "s":
            self.imgAttuale = self.imgS
        elif direzione == "d":
            self.imgAttuale = self.imgD

    def danneggia(self, danno):
        self.vita -= danno
        if self.vita <= 0:
            self.vita = 0

    def aggiornaVista(self, x, y, rx, ry, stanza, porte, cofanetti, dati):
        vistoRallo = False
        vistoRob = False
        caseattactot = trovacasattaccabili(self.x, self.y, stanza, porte, cofanetti)
        if abs(x - self.x) <= self.raggioVisivo and abs(y - self.y) <= self.raggioVisivo and dati[5] > 0:
            j = 0
            while j < len(caseattactot):
                if caseattactot[j] == x and caseattactot[j + 1] == y:
                    if not caseattactot[j + 2]:
                        vistoRallo = False
                    else:
                        vistoRallo = True
                    break
                j = j + 3
        if abs(rx - self.x) <= self.raggioVisivo and abs(ry - self.y) <= self.raggioVisivo and dati[10] > 0:
            j = 0
            while j < len(caseattactot):
                if caseattactot[j] == rx and caseattactot[j + 1] == ry:
                    if not caseattactot[j + 2]:
                        vistoRob = False
                    else:
                        vistoRob = True
                    break
                j = j + 3
            if dati[10] <= 0:
                vistoRob = False
        if vistoRallo or vistoRob:
            self.visto = True
        else:
            self.visto = False

    def resettaMosseRimaste(self):
        if self.velocita >= 0:
            self.mosseRimaste = 1 + self.velocita
        elif self.velocita < 0:
            self.mosseRimaste = 1

    def compiMossa(self):
        if self.appiccicato:
            if self.velocita >= 0:
                self.mosseRimaste -= 2
            elif self.velocita < 0:
                self.mosseRimaste = self.mosseRimaste - 2 + self.velocita
        else:
            if self.velocita >= 0:
                self.mosseRimaste -= 1
            elif self.velocita < 0:
                self.mosseRimaste = self.mosseRimaste - 1 + self.velocita
