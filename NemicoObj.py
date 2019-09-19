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
        muovimostro = 0
        attacco = 0
        attaccaDaLontano = False
        if self.tipo == "Orco":
            vitaTotale = 50
            esp = 10
            raggioVisivo = gpx * 4
            muovimostro = -2
            attacco = 50
            attaccaDaLontano = False
        if self.tipo == "Pipistrello":
            vitaTotale = 20
            esp = 5
            raggioVisivo = gpx * 6
            muovimostro = 2
            attacco = 20
            attaccaDaLontano = True
        self.vita = vitaTotale
        self.vitaTotale = vitaTotale
        self.esp = esp
        self.raggioVisivo = raggioVisivo
        self.muoviMostroDefault = muovimostro
        self.muoviMostro = 0
        self.attacco = attacco
        self.attaccaDaLontano = attaccaDaLontano

        imgW = pygame.image.load("Immagini\Mostri\\" + tipo + "w.png")
        self.imgW = pygame.transform.scale(imgW, (gpx, gpy))
        imgA = pygame.image.load("Immagini\Mostri\\" + tipo + "a.png")
        self.imgA = pygame.transform.scale(imgA, (gpx, gpy))
        imgS = pygame.image.load("Immagini\Mostri\\" + tipo + "s.png")
        self.imgS = pygame.transform.scale(imgS, (gpx, gpy))
        imgD = pygame.image.load("Immagini\Mostri\\" + tipo + "d.png")
        self.imgD = pygame.transform.scale(imgD, (gpx, gpy))
        self.girati(direzione)

    def girati(self, direzione):
        if direzione == "w":
            self.imgAttuale = self.imgW
        elif direzione == "a":
            self.imgAttuale = self.imgA
        elif direzione == "s":
            self.imgAttuale = self.imgS
        elif direzione == "d":
            self.imgAttuale = self.imgD

    def resettaMuoviMostro(self):
        if self.appiccicato:
            self.muoviMostro = self.muoviMostroDefault - 1
            if abs(self.muoviMostro) == 1:
                self.muoviMostro -= 1
        else:
            self.muoviMostro = self.muoviMostroDefault

    def danneggia(self, danno):
        self.vita -= danno
        if self.vita <= 0:
            self.vita = 0

    def aggiornaVista(self, x, y, rx, ry, stanza, porte, cofanetti, dati):
        vistoprov1 = False
        vistoprov2 = False
        caseattactot = trovacasattaccabili(self.x, self.y, stanza, porte, cofanetti)
        if abs(x - self.x) <= self.raggioVisivo and abs(y - self.y) <= self.raggioVisivo and dati[5] > 0:
            j = 0
            while j < len(caseattactot):
                if caseattactot[j] == x and caseattactot[j + 1] == y:
                    if not caseattactot[j + 2]:
                        vistoprov1 = False
                    else:
                        vistoprov1 = True
                    break
                j = j + 3
        if abs(rx - self.x) <= self.raggioVisivo and abs(ry - self.y) <= self.raggioVisivo and dati[10] > 0:
            j = 0
            while j < len(caseattactot):
                if caseattactot[j] == rx and caseattactot[j + 1] == ry:
                    if not caseattactot[j + 2]:
                        vistoprov2 = False
                    else:
                        vistoprov2 = True
                    break
                j = j + 3
            if dati[10] <= 0:
                vistoprov2 = False
        if vistoprov1 or vistoprov2:
            self.visto = True
