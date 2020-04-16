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
        self.scelta = False

        self.caricaImg()
        self.girati(direzione)
        self.aggiornaDialogo(avanzamentoStoria)

    def caricaImg(self):
        imgW = pygame.image.load("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "W.png")
        self.imgW = pygame.transform.scale(imgW, (GlobalVarG2.gpx, GlobalVarG2.gpy))
        imgA = pygame.image.load("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "A.png")
        self.imgA = pygame.transform.scale(imgA, (GlobalVarG2.gpx, GlobalVarG2.gpy))
        imgS = pygame.image.load("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "S.png")
        self.imgS = pygame.transform.scale(imgS, (GlobalVarG2.gpx, GlobalVarG2.gpy))
        imgD = pygame.image.load("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "D.png")
        self.imgD = pygame.transform.scale(imgD, (GlobalVarG2.gpx, GlobalVarG2.gpy))

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
        # se c'è una scelta la variabile self.scelta conterrà il numero corrispondente a quella giusta (se ce n'è più di una giusta, la variabile conterrà i nueri di queste una dopo l'altra (es. 12, 134))
        # i dialoghi che iniziano con "???DOMANDA???" contengono 6 frasi in totale (ossia => "???DOMANDA???", la domanda posta, opzione 1, opzione 2, opzione 3, opzione 4)
        # i dialoghi che iniziano con "!!!RISPOSTA!!!" contengono 5 frasi in totale (ossia => "!!!RISPOSTA!!!", risposta opzione 1, risposta opzione 2, risposta opzione 3, risposta opzione 4)
        if self.tipo == "Mercante":
            self.partiDialogo = []
            self.nome = "Bob"
            if avanzamentoStoria == 0:
                self.oggettoDato = False
                self.avanzamentoStoria = False
                self.menuMercante = True
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Ciao,")
                dialogo.append("ecco la merce")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Ecco la merceee")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == 1:
                self.oggettoDato = "oggetto speciale"
                self.avanzamentoStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Ciao,")
                dialogo.append(u"la merce è finita")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È finita?")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzamentoStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
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
                self.scelta = 3
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Ti sto per fare una domanda")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("???DOMANDA???")
                dialogo.append("Quanto fa 2+3?")
                dialogo.append("Che schifo di domanda!")
                dialogo.append("(cambia discorso parlando di carote)")
                dialogo.append("Almeno 3")
                dialogo.append("(mettilo a disagio fingendo di non aver sentito)")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("!!!RISPOSTA!!!")
                dialogo.append("Scusa...")
                dialogo.append("Scusa, non mi interessano le carote")
                dialogo.append("Non mi pare... ma te la do per buona")
                dialogo.append("2+3? ... mi scusi signore ... 2+3? ...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ho compato tutto ciò che aveva il mercante")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzamentoStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Muhahahaha")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Fai schifo")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
