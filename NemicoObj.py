# -*- coding: utf-8 -*-

from GenericFuncA import *


class NemicoObj(object):

    def __init__(self, x, y, direzione, tipo, stanza, percorso, numeroMovimento=0, triggerato=False):
        self.x = x
        self.y = y
        self.vx = x
        self.vy = y
        self.avvelenato = False
        self.appiccicato = False
        self.visto = False
        self.stanzaDiAppartenenza = stanza
        self.morto = False
        self.inCasellaVista = False
        self.triggerato = triggerato
        self.percorso = percorso
        self.numeroMovimento = numeroMovimento
        self.xObbiettivo = False
        self.yObbiettivo = False
        self.xPosizioneUltimoBersaglio = False
        self.yPosizioneUltimoBersaglio = False
        self.quadrettoSottoOggettoLanciato = 0
        self.quadrettoSottoArma = 0
        self.ralloParato = False
        self.statoInizioTurno = []
        self.bersaglioColpito = []
        self.direzione = direzione
        self.mosseRimaste = 0
        self.animaSpostamento = False
        self.animaAttacco = False
        self.animaMorte = False
        self.animaDanneggiamento = False
        self.animazioneFatta = False
        self.tipo = tipo

        self.inizializzaStatistiche()
        self.caricaImg()
        self.girati(direzione)

    def inizializzaStatistiche(self):
        vitaTotale = 0
        esp = 0
        raggioVisivo = 0
        velocita = 0
        attacco = 0
        attaccaDaLontano = False
        velenoso = False
        surriscaldante = False
        denaro = 0
        difesa = 0
        if self.tipo == "Orco":
            vitaTotale = 3000
            esp = 10
            raggioVisivo = GlobalVar.gpx * 4
            velocita = -1
            attacco = 50
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            denaro = random.randint(3, 7)
            difesa = 2
        if self.tipo == "Pipistrello":
            vitaTotale = 20
            esp = 5
            raggioVisivo = GlobalVar.gpx * 6
            velocita = 1
            attacco = 20
            attaccaDaLontano = True
            velenoso = True
            surriscaldante = False
            denaro = random.randint(0, 3)
            difesa = 0
        if self.tipo == "TartarugaVerde":
            vitaTotale = 20
            esp = 5
            raggioVisivo = GlobalVar.gpx * 2
            velocita = -2
            attacco = 20
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            denaro = random.randint(0, 3)
            difesa = 5
        if self.tipo == "TartarugaMarrone":
            vitaTotale = 20
            esp = 5
            raggioVisivo = GlobalVar.gpx * 2
            velocita = -2
            attacco = 20
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            denaro = random.randint(0, 3)
            difesa = 5
        if self.tipo == "Cinghiale":
            vitaTotale = 20
            esp = 5
            raggioVisivo = GlobalVar.gpx * 2
            velocita = -2
            attacco = 20
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            denaro = random.randint(0, 3)
            difesa = 5
        if self.tipo == "LupoGrigio":
            vitaTotale = 20
            esp = 5
            raggioVisivo = GlobalVar.gpx * 2
            velocita = -2
            attacco = 20
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            denaro = random.randint(0, 3)
            difesa = 5
        if self.tipo == "LupoNero":
            vitaTotale = 20
            esp = 5
            raggioVisivo = GlobalVar.gpx * 2
            velocita = -2
            attacco = 20
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            denaro = random.randint(0, 3)
            difesa = 5
        if self.tipo == "LupoBianco":
            vitaTotale = 20
            esp = 5
            raggioVisivo = GlobalVar.gpx * 2
            velocita = -2
            attacco = 20
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            denaro = random.randint(0, 3)
            difesa = 1
        if self.tipo == "SerpeVerde":
            vitaTotale = 20
            esp = 5
            raggioVisivo = GlobalVar.gpx * 2
            velocita = -2
            attacco = 20
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            denaro = random.randint(0, 3)
            difesa = 1
        if self.tipo == "SerpeArancio":
            vitaTotale = 20
            esp = 5
            raggioVisivo = GlobalVar.gpx * 2
            velocita = -2
            attacco = 20
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            denaro = random.randint(0, 3)
            difesa = 1
        if self.tipo == "Scorpione":
            vitaTotale = 20
            esp = 5
            raggioVisivo = GlobalVar.gpx * 2
            velocita = -2
            attacco = 20
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            denaro = random.randint(0, 3)
            difesa = 1
        if self.tipo == "RagnoNero":
            vitaTotale = 20
            esp = 5
            raggioVisivo = GlobalVar.gpx * 2
            velocita = -2
            attacco = 20
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            denaro = random.randint(0, 3)
            difesa = 1
        if self.tipo == "RagnoRosso":
            vitaTotale = 20
            esp = 5
            raggioVisivo = GlobalVar.gpx * 2
            velocita = -2
            attacco = 20
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            denaro = random.randint(0, 3)
            difesa = 1
        if self.tipo == "GufoMarrone":
            vitaTotale = 20
            esp = 5
            raggioVisivo = GlobalVar.gpx * 2
            velocita = -2
            attacco = 20
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            denaro = random.randint(0, 3)
            difesa = 1
        if self.tipo == "GufoBianco":
            vitaTotale = 20
            esp = 5
            raggioVisivo = GlobalVar.gpx * 2
            velocita = -2
            attacco = 20
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            denaro = random.randint(0, 3)
            difesa = 1
        if self.tipo == "Falco":
            vitaTotale = 20
            esp = 5
            raggioVisivo = GlobalVar.gpx * 2
            velocita = -2
            attacco = 20
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            denaro = random.randint(0, 3)
            difesa = 1
        if self.tipo == "Aquila":
            vitaTotale = 20
            esp = 5
            raggioVisivo = GlobalVar.gpx * 2
            velocita = -2
            attacco = 20
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            denaro = random.randint(0, 3)
            difesa = 1
        self.vita = vitaTotale
        self.vitaTotale = vitaTotale
        self.esp = esp
        self.raggioVisivo = raggioVisivo
        self.velocita = velocita
        self.attacco = attacco
        self.attaccaDaLontano = attaccaDaLontano
        self.velenoso = velenoso
        self.surriscaldante = surriscaldante
        self.denaro = denaro
        self.difesa = difesa

    def caricaImg(self):
        imgW = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "w.png")
        self.imgW = pygame.transform.smoothscale(imgW, (GlobalVar.gpx, GlobalVar.gpy))
        imgA = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "a.png")
        self.imgA = pygame.transform.smoothscale(imgA, (GlobalVar.gpx, GlobalVar.gpy))
        imgS = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "s.png")
        self.imgS = pygame.transform.smoothscale(imgS, (GlobalVar.gpx, GlobalVar.gpy))
        imgD = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "d.png")
        self.imgD = pygame.transform.smoothscale(imgD, (GlobalVar.gpx, GlobalVar.gpy))

        imgWMov1 = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "wMov1.png")
        self.imgWMov1 = pygame.transform.smoothscale(imgWMov1, (GlobalVar.gpx, GlobalVar.gpy))
        imgWMov2 = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "wMov2.png")
        self.imgWMov2 = pygame.transform.smoothscale(imgWMov2, (GlobalVar.gpx, GlobalVar.gpy))
        imgAMov1 = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "aMov1.png")
        self.imgAMov1 = pygame.transform.smoothscale(imgAMov1, (GlobalVar.gpx, GlobalVar.gpy))
        imgAMov2 = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "aMov2.png")
        self.imgAMov2 = pygame.transform.smoothscale(imgAMov2, (GlobalVar.gpx, GlobalVar.gpy))
        imgSMov1 = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "sMov1.png")
        self.imgSMov1 = pygame.transform.smoothscale(imgSMov1, (GlobalVar.gpx, GlobalVar.gpy))
        imgSMov2 = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "sMov2.png")
        self.imgSMov2 = pygame.transform.smoothscale(imgSMov2, (GlobalVar.gpx, GlobalVar.gpy))
        imgDMov1 = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "dMov1.png")
        self.imgDMov1 = pygame.transform.smoothscale(imgDMov1, (GlobalVar.gpx, GlobalVar.gpy))
        imgDMov2 = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "dMov2.png")
        self.imgDMov2 = pygame.transform.smoothscale(imgDMov2, (GlobalVar.gpx, GlobalVar.gpy))

        imgAvvelenamento = GlobalVar.loadImage("Immagini/Nemici/NemicoAvvelenato.png")
        self.imgAvvelenamento = pygame.transform.smoothscale(imgAvvelenamento, (GlobalVar.gpx, GlobalVar.gpy))
        imgAppiccicato = GlobalVar.loadImage("Immagini/Nemici/NemicoAppiccicato.png")
        self.imgAppiccicato = pygame.transform.smoothscale(imgAppiccicato, (GlobalVar.gpx, GlobalVar.gpy))

        imgAttaccoW = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "wAttacco.png")
        self.imgAttaccoW = pygame.transform.smoothscale(imgAttaccoW, (GlobalVar.gpx, GlobalVar.gpy * 2))
        imgAttaccoA = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "aAttacco.png")
        self.imgAttaccoA = pygame.transform.smoothscale(imgAttaccoA, (GlobalVar.gpx * 2, GlobalVar.gpy))
        imgAttaccoS = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "sAttacco.png")
        self.imgAttaccoS = pygame.transform.smoothscale(imgAttaccoS, (GlobalVar.gpx, GlobalVar.gpy * 2))
        imgAttaccoD = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "dAttacco.png")
        self.imgAttaccoD = pygame.transform.smoothscale(imgAttaccoD, (GlobalVar.gpx * 2, GlobalVar.gpy))
        if self.attaccaDaLontano:
            imgOggettoLanciato = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "OggettoLanciato.png")
            self.imgOggettoLanciato = pygame.transform.smoothscale(imgOggettoLanciato, (GlobalVar.gpx, GlobalVar.gpy))
            imgDanneggiamentoOggettoLanciato = GlobalVar.loadImage("Immagini/Nemici/" + self.tipo + "/" + self.tipo + "DanneggiamentoOggettoLanciato.png")
            self.imgDanneggiamentoOggettoLanciato = pygame.transform.smoothscale(imgDanneggiamentoOggettoLanciato, (GlobalVar.gpx, GlobalVar.gpy))
        else:
            self.imgOggettoLanciato = 0
            self.imgDanneggiamentoOggettoLanciato = 0

        imgDanneggiamentoRallo = GlobalVar.loadImage("Immagini/Nemici/DannoRallo.png")
        self.imgDanneggiamentoRallo = pygame.transform.smoothscale(imgDanneggiamentoRallo, (GlobalVar.gpx, GlobalVar.gpy))
        imgDanneggiamentoColco = GlobalVar.loadImage("Immagini/Nemici/DannoColco.png")
        self.imgDanneggiamentoColco = pygame.transform.smoothscale(imgDanneggiamentoColco, (GlobalVar.gpx, GlobalVar.gpy))

    def girati(self, direzione):
        self.imgAttuale = self.imgS
        if direzione == "w":
            self.imgAttuale = self.imgW
        elif direzione == "a":
            self.imgAttuale = self.imgA
        elif direzione == "s":
            self.imgAttuale = self.imgS
        elif direzione == "d":
            self.imgAttuale = self.imgD
        self.direzione = direzione

    def danneggia(self, danno, attaccante):
        self.animaDanneggiamento = attaccante
        danno -= self.difesa
        if danno < 0:
            danno = 0
        self.vita -= danno
        if self.vita < 0:
            self.vita = 0

    def aggiornaVista(self, x, y, rx, ry, stanza, porte, cofanetti, dati):
        vistoRallo = False
        vistoRob = False
        caseattactot = trovacasattaccabili(self.x, self.y, stanza, porte, cofanetti, self.raggioVisivo)
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

    def settaObbiettivo(self, x, y, rx, ry, dati, stanza, porte, cofanetti, vettoreDenaro, vitaesca, attaccoADistanza, listaNemiciAttaccatiADistanzaRobo):
        vistoRallo = False
        vistoRob = False
        vistoesca = False
        escabersaglio = 0
        vistoDenaro = False
        xDenaro = 0
        yDenaro = 0

        caseattactot = trovacasattaccabili(self.x, self.y, stanza, porte, cofanetti, self.raggioVisivo)

        distminx = 0
        distminy = 0
        primoSacchetto = True
        i = 0
        while i < len(vettoreDenaro):
            j = 0
            while j < len(caseattactot):
                if caseattactot[j] == vettoreDenaro[i + 1] and caseattactot[j + 1] == vettoreDenaro[i + 2] and caseattactot[j + 2] and not (x == vettoreDenaro[i + 1] and y == vettoreDenaro[i + 2]) and not (rx == vettoreDenaro[i + 1] and ry == vettoreDenaro[i + 2]):
                    if primoSacchetto:
                        distminx = vettoreDenaro[i + 1]
                        distminy = vettoreDenaro[i + 2]
                        xDenaro = distminx
                        yDenaro = distminy
                        vistoDenaro = True
                        primoSacchetto = False
                    elif abs(vettoreDenaro[i + 1] - self.x) + abs(vettoreDenaro[i + 2] - self.y) < abs(distminx - self.x) + abs(distminy - self.y):
                        distminx = vettoreDenaro[i + 1]
                        distminy = vettoreDenaro[i + 2]
                        xDenaro = distminx
                        yDenaro = distminy
                    break
                j += 3
            i += 3
        primaesca = True
        i = 0
        while i < len(vitaesca):
            j = 0
            while j < len(caseattactot):
                if caseattactot[j] == vitaesca[i + 2] and caseattactot[j + 1] == vitaesca[i + 3] and caseattactot[j + 2]:
                    if primaesca:
                        distminx = vitaesca[i + 2]
                        distminy = vitaesca[i + 3]
                        escabersaglio = i
                        vistoesca = True
                        primaesca = False
                    elif abs(vitaesca[i + 2] - self.x) + abs(vitaesca[i + 3] - self.y) < abs(
                            distminx - self.x) + abs(distminy - self.y):
                        distminx = vitaesca[i + 2]
                        distminy = vitaesca[i + 3]
                        escabersaglio = i
                    break
                j += 3
            i += 4
        if not vistoesca:
            # controllo caselle che si vedono (per controllare se si vedono pers o robo)
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

        self.xObbiettivo = False
        self.yObbiettivo = False
        attrobo = False
        if vistoRallo or vistoRob or vistoesca:
            self.xObbiettivo = x
            self.yObbiettivo = y
            if ((abs(rx - self.x) + abs(ry - self.y)) < (abs(x - self.x) + abs(y - self.y)) or not vistoRallo) and vistoRob and dati[10] > 0 and not vistoesca:
                self.xObbiettivo = rx
                self.yObbiettivo = ry
                attrobo = True
            if vistoDenaro and (abs(xDenaro - self.x) + abs(yDenaro - self.y)) <= (abs(self.xObbiettivo - self.x) + abs(self.yObbiettivo - self.y)):
                self.xObbiettivo = xDenaro
                self.yObbiettivo = yDenaro
            if vistoesca:
                self.xObbiettivo = vitaesca[escabersaglio + 2]
                self.yObbiettivo = vitaesca[escabersaglio + 3]

        if self.xObbiettivo and self.yObbiettivo:
            self.xPosizioneUltimoBersaglio = self.xObbiettivo
            self.yPosizioneUltimoBersaglio = self.yObbiettivo
        elif self.x == self.xPosizioneUltimoBersaglio and self.y == self.yPosizioneUltimoBersaglio:
            self.xPosizioneUltimoBersaglio = False
            self.yPosizioneUltimoBersaglio = False

        if not self.xObbiettivo and not self.yObbiettivo:
            if self == attaccoADistanza:
                self.xPosizioneUltimoBersaglio = x
                self.yPosizioneUltimoBersaglio = y
            elif listaNemiciAttaccatiADistanzaRobo:
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    if self == nemico:
                        self.xPosizioneUltimoBersaglio = rx
                        self.yPosizioneUltimoBersaglio = ry
                        break

        return vistoRallo, vistoRob, vistoesca, escabersaglio, vistoDenaro, xDenaro, yDenaro, attrobo
