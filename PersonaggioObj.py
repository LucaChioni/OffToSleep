# -*- coding: utf-8 -*-

from GenericFuncA import *


class PersonaggioObj(object):

    def __init__(self, x, y, direzione, tipo, stanza, avanzamentoStoria, percorso, numeroMovimento=0):
        self.x = x
        self.y = y
        self.vx = x
        self.vy = y

        self.tipo = tipo
        self.stanzaDiAppartenenza = stanza
        self.oggettoDato = False
        self.avanzamentoStoria = False
        self.menuMercante = False
        self.scelta = False
        self.percorso = percorso
        self.numeroMovimento = numeroMovimento
        self.inCasellaVista = False
        self.animaSpostamento = False
        self.animazioneFatta = False

        self.caricaImg()
        self.girati(direzione)
        self.aggiornaDialogo(avanzamentoStoria)

    def caricaImg(self):
        imgW = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "W.png")
        self.imgW = pygame.transform.smoothscale(imgW, (GlobalVar.gpx, GlobalVar.gpy))
        imgA = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "A.png")
        self.imgA = pygame.transform.smoothscale(imgA, (GlobalVar.gpx, GlobalVar.gpy))
        imgS = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "S.png")
        self.imgS = pygame.transform.smoothscale(imgS, (GlobalVar.gpx, GlobalVar.gpy))
        imgD = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "D.png")
        self.imgD = pygame.transform.smoothscale(imgD, (GlobalVar.gpx, GlobalVar.gpy))

        imgWMov1 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "WMov1.png")
        self.imgWMov1 = pygame.transform.smoothscale(imgWMov1, (GlobalVar.gpx, GlobalVar.gpy))
        imgWMov2 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "WMov2.png")
        self.imgWMov2 = pygame.transform.smoothscale(imgWMov2, (GlobalVar.gpx, GlobalVar.gpy))
        imgAMov1 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "AMov1.png")
        self.imgAMov1 = pygame.transform.smoothscale(imgAMov1, (GlobalVar.gpx, GlobalVar.gpy))
        imgAMov2 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "AMov2.png")
        self.imgAMov2 = pygame.transform.smoothscale(imgAMov2, (GlobalVar.gpx, GlobalVar.gpy))
        imgSMov1 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "SMov1.png")
        self.imgSMov1 = pygame.transform.smoothscale(imgSMov1, (GlobalVar.gpx, GlobalVar.gpy))
        imgSMov2 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "SMov2.png")
        self.imgSMov2 = pygame.transform.smoothscale(imgSMov2, (GlobalVar.gpx, GlobalVar.gpy))
        imgDMov1 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "DMov1.png")
        self.imgDMov1 = pygame.transform.smoothscale(imgDMov1, (GlobalVar.gpx, GlobalVar.gpy))
        imgDMov2 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "DMov2.png")
        self.imgDMov2 = pygame.transform.smoothscale(imgDMov2, (GlobalVar.gpx, GlobalVar.gpy))

        imgDialogo = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "Dialogo.png")
        self.imgDialogo = pygame.transform.smoothscale(imgDialogo, (GlobalVar.gpx * 12, GlobalVar.gpy * 9))

    def girati(self, direzione):
        if direzione == "w":
            self.imgAttuale = self.imgW
        elif direzione == "a":
            self.imgAttuale = self.imgA
        elif direzione == "s":
            self.imgAttuale = self.imgS
        elif direzione == "d":
            self.imgAttuale = self.imgD

        if direzione != "":
            self.direzione = direzione

    def aggiornaDialogo(self, avanzamentoStoria):
        # se c'è una scelta la variabile self.scelta conterrà il numero corrispondente a quella giusta (se ce n'è più di una giusta, la variabile conterrà i numeri di queste una dopo l'altra (es. 12, 134))
        # i dialoghi che iniziano con "???DOMANDA???" contengono 6 frasi in totale (ossia => "???DOMANDA???", la domanda posta, opzione 1, opzione 2, opzione 3, opzione 4)
        # i dialoghi che iniziano con "!!!RISPOSTA!!!" contengono 5 frasi in totale (ossia => "!!!RISPOSTA!!!", risposta opzione 1, risposta opzione 2, risposta opzione 3, risposta opzione 4)
        if self.tipo == "Mercante":
            self.partiDialogo = []
            self.nome = "Bob"
            if avanzamentoStoria == 0:
                self.oggettoDato = False
                self.avanzamentoStoria = True
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

    def spostati(self, x, y, rx, ry, listaNemici):
        self.vx = self.x
        self.vy = self.y
        self.animaSpostamento = True
        movimentoAnnullato = False

        if len(self.percorso) > 0:
            direzione = self.percorso[self.numeroMovimento]
            self.girati(direzione)
        else:
            direzione = ""
        if direzione == "w":
            self.y -= GlobalVar.gpy
        elif direzione == "a":
            self.x -= GlobalVar.gpx
        elif direzione == "s":
            self.y += GlobalVar.gpy
        elif direzione == "d":
            self.x += GlobalVar.gpx
        else:
            self.animaSpostamento = False

        for nemico in listaNemici:
            if self.x == nemico.x and self.y == nemico.y:
                self.x = self.vx
                self.y = self.vy
                self.animaSpostamento = False
                movimentoAnnullato = True
                break
        if (self.x == x and self.y == y) or (self.x == rx and self.y == ry):
            self.x = self.vx
            self.y = self.vy
            self.animaSpostamento = False
            movimentoAnnullato = True

        if not movimentoAnnullato:
            if self.numeroMovimento < len(self.percorso) - 1:
                self.numeroMovimento += 1
            else:
                self.numeroMovimento = 0
