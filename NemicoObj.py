# -*- coding: utf-8 -*-

from GenericFunc import *


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
        self.caseattactot = []
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
        avvelenabile = True

        if self.tipo == "Orco":
            vitaTotale = 20
            attacco = 20
            difesa = 2
            velocita = -1
            raggioVisivo = GlobalVar.gpx * 3
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = 0
            esp = 1
        if self.tipo == "Pipistrello":
            vitaTotale = 10
            attacco = 15
            difesa = 1
            velocita = 0
            raggioVisivo = GlobalVar.gpx * 3
            attaccaDaLontano = True
            velenoso = True
            surriscaldante = False
            avvelenabile = False
            denaro = 0
            esp = 2

        if self.tipo == "TartarugaVerde":
            vitaTotale = 40
            attacco = 40
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "TartarugaMarrone":
            vitaTotale = 60
            attacco = 40
            difesa = 10
            velocita = -1
            raggioVisivo = GlobalVar.gpx * 3
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "LupoGrigio":
            vitaTotale = 40
            attacco = 45
            difesa = 3
            velocita = 0
            raggioVisivo = GlobalVar.gpx * 5
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "LupoBianco":
            vitaTotale = 60
            attacco = 55
            difesa = 3
            velocita = 0
            raggioVisivo = GlobalVar.gpx * 5
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "LupoNero":
            vitaTotale = 80
            attacco = 60
            difesa = 5
            velocita = 0
            raggioVisivo = GlobalVar.gpx * 5
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "Cinghiale":
            vitaTotale = 80
            attacco = 75
            difesa = 15
            velocita = 0
            raggioVisivo = GlobalVar.gpx * 4
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5

        if self.tipo == "SerpeVerde":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "SerpeArancio":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "Scorpione":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "RagnoNero":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "RagnoRosso":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5

        if self.tipo == "ServoSpada":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "ServoArco":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "ServoLancia":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5

        if self.tipo == "GufoMarrone":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "GufoBianco":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "Falco":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "Aquila":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "Struzzo":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "Casuario":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5

        if self.tipo == "RoboLeggero":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "RoboVolante":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "RoboPesante":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5

        if self.tipo == "RoboPesanteVolante":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5
        if self.tipo == "RoboTorre":
            vitaTotale = 25
            attacco = 20
            difesa = 5
            velocita = -2
            raggioVisivo = GlobalVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 3)
            esp = 5

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
        self.avvelenabile = avvelenabile

    def caricaImg(self):
        self.imgW = GlobalVar.dictionaryImgNemici[self.tipo]["imgW"]
        self.imgA = GlobalVar.dictionaryImgNemici[self.tipo]["imgA"]
        self.imgS = GlobalVar.dictionaryImgNemici[self.tipo]["imgS"]
        self.imgD = GlobalVar.dictionaryImgNemici[self.tipo]["imgD"]

        self.imgWMov1 = GlobalVar.dictionaryImgNemici[self.tipo]["imgWMov1"]
        self.imgWMov2 = GlobalVar.dictionaryImgNemici[self.tipo]["imgWMov2"]
        self.imgAMov1 = GlobalVar.dictionaryImgNemici[self.tipo]["imgAMov1"]
        self.imgAMov2 = GlobalVar.dictionaryImgNemici[self.tipo]["imgAMov2"]
        self.imgSMov1 = GlobalVar.dictionaryImgNemici[self.tipo]["imgSMov1"]
        self.imgSMov2 = GlobalVar.dictionaryImgNemici[self.tipo]["imgSMov2"]
        self.imgDMov1 = GlobalVar.dictionaryImgNemici[self.tipo]["imgDMov1"]
        self.imgDMov2 = GlobalVar.dictionaryImgNemici[self.tipo]["imgDMov2"]

        self.imgAvvelenamento = GlobalVar.dictionaryImgNemici[self.tipo]["imgAvvelenamento"]
        self.imgAppiccicato = GlobalVar.dictionaryImgNemici[self.tipo]["imgAppiccicato"]

        self.imgAttaccoW = GlobalVar.dictionaryImgNemici[self.tipo]["imgAttaccoW"]
        self.imgAttaccoA = GlobalVar.dictionaryImgNemici[self.tipo]["imgAttaccoA"]
        self.imgAttaccoS = GlobalVar.dictionaryImgNemici[self.tipo]["imgAttaccoS"]
        self.imgAttaccoD = GlobalVar.dictionaryImgNemici[self.tipo]["imgAttaccoD"]
        if self.attaccaDaLontano:
            self.imgOggettoLanciato = GlobalVar.dictionaryImgNemici[self.tipo]["imgOggettoLanciato"]
            self.imgDanneggiamentoOggettoLanciato = GlobalVar.dictionaryImgNemici[self.tipo]["imgDanneggiamentoOggettoLanciato"]
        else:
            self.imgOggettoLanciato = 0
            self.imgDanneggiamentoOggettoLanciato = 0

        self.imgDanneggiamentoRallo = GlobalVar.dictionaryImgNemici[self.tipo]["imgDanneggiamentoRalloNemico"]
        self.imgDanneggiamentoColco = GlobalVar.dictionaryImgNemici[self.tipo]["imgDanneggiamentoColcoNemico"]

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

    def aggiornaVista(self, x, y, rx, ry, stanza, porte, cofanetti, listaPersonaggi, dati):
        vistoRallo = False
        vistoRob = False
        self.caseattactot = trovacasattaccabili(self.x, self.y, stanza, porte, cofanetti, listaPersonaggi, self.raggioVisivo)
        if abs(x - self.x) <= self.raggioVisivo and abs(y - self.y) <= self.raggioVisivo and dati[5] > 0:
            j = 0
            while j < len(self.caseattactot):
                if self.caseattactot[j] == x and self.caseattactot[j + 1] == y:
                    if not self.caseattactot[j + 2]:
                        vistoRallo = False
                    else:
                        vistoRallo = True
                        self.xPosizioneUltimoBersaglio = x
                        self.yPosizioneUltimoBersaglio = y
                    break
                j = j + 3
        if abs(rx - self.x) <= self.raggioVisivo and abs(ry - self.y) <= self.raggioVisivo and dati[10] > 0:
            j = 0
            while j < len(self.caseattactot):
                if self.caseattactot[j] == rx and self.caseattactot[j + 1] == ry:
                    if not self.caseattactot[j + 2]:
                        vistoRob = False
                    else:
                        vistoRob = True
                        self.xPosizioneUltimoBersaglio = rx
                        self.yPosizioneUltimoBersaglio = ry
                    break
                j = j + 3
        if vistoRallo or vistoRob:
            self.visto = True
        else:
            self.visto = False

    def aggiornaBersaglioAttacchiDistanti (self, x, y, rx, ry, attaccoADistanza, listaNemiciAttaccatiADistanzaRobo):
        if not self.xObbiettivo and not self.yObbiettivo:
            if attaccoADistanza and self.x == attaccoADistanza.x and self.y == attaccoADistanza.y:
                self.xPosizioneUltimoBersaglio = x
                self.yPosizioneUltimoBersaglio = y
            elif listaNemiciAttaccatiADistanzaRobo:
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    if self.x == nemico.x and self.y == nemico.y:
                        self.xPosizioneUltimoBersaglio = rx
                        self.yPosizioneUltimoBersaglio = ry
                        break

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

    def settaObbiettivo(self, x, y, rx, ry, dati, vettoreDenaro, vitaesca):
        vistoRallo = False
        vistoRob = False
        vistoesca = False
        escabersaglio = 0
        vistoDenaro = False
        xDenaro = 0
        yDenaro = 0

        primaesca = True
        distMinXEsca = -1
        distMinYEsca = -1
        primoDenaro = True
        distMinXDenaro = -1
        distMinYDenaro = -1
        j = 0
        while j < len(self.caseattactot):
            i = 0
            while i < len(vitaesca):
                if self.caseattactot[j] == vitaesca[i + 2] and self.caseattactot[j + 1] == vitaesca[i + 3]:
                    if self.caseattactot[j + 2]:
                        if primaesca:
                            distMinXEsca = vitaesca[i + 2]
                            distMinYEsca = vitaesca[i + 3]
                            escabersaglio = i
                            vistoesca = True
                            primaesca = False
                        elif abs(vitaesca[i + 2] - self.x) + abs(vitaesca[i + 3] - self.y) < abs(distMinXEsca - self.x) + abs(distMinYEsca - self.y):
                            distMinXEsca = vitaesca[i + 2]
                            distMinYEsca = vitaesca[i + 3]
                            escabersaglio = i
                    break
                i += 4

            if not vistoesca:
                # controllo caselle che si vedono (per controllare se si vedono pers o robo)
                if not vistoRallo and abs(x - self.x) <= self.raggioVisivo and abs(y - self.y) <= self.raggioVisivo and dati[5] > 0:
                    if self.caseattactot[j] == x and self.caseattactot[j + 1] == y and self.caseattactot[j + 2]:
                        vistoRallo = True
                if not vistoRob and abs(rx - self.x) <= self.raggioVisivo and abs(ry - self.y) <= self.raggioVisivo and dati[10] > 0:
                    if self.caseattactot[j] == rx and self.caseattactot[j + 1] == ry and self.caseattactot[j + 2]:
                        vistoRob = True
                i = 0
                while i < len(vettoreDenaro):
                    if self.caseattactot[j] == vettoreDenaro[i + 1] and self.caseattactot[j + 1] == vettoreDenaro[i + 2]:
                        if self.caseattactot[j + 2] and not (x == vettoreDenaro[i + 1] and y == vettoreDenaro[i + 2]) and not (rx == vettoreDenaro[i + 1] and ry == vettoreDenaro[i + 2]):
                            if primoDenaro:
                                distMinXDenaro = vettoreDenaro[i + 1]
                                distMinYDenaro = vettoreDenaro[i + 2]
                                xDenaro = distMinXDenaro
                                yDenaro = distMinYDenaro
                                vistoDenaro = True
                                primoDenaro = False
                            elif abs(vettoreDenaro[i + 1] - self.x) + abs(vettoreDenaro[i + 2] - self.y) < abs(distMinXDenaro - self.x) + abs(distMinYDenaro - self.y):
                                distMinXDenaro = vettoreDenaro[i + 1]
                                distMinYDenaro = vettoreDenaro[i + 2]
                                xDenaro = distMinXDenaro
                                yDenaro = distMinYDenaro
                        break
                    i += 3
            j += 3

        self.xObbiettivo = False
        self.yObbiettivo = False
        attrobo = False
        if vistoRallo or vistoRob or vistoesca or vistoDenaro:
            distanzaDaRallo = abs(x - self.x) + abs(y - self.y)
            distanzaDaColco = abs(rx - self.x) + abs(ry - self.y)
            distanzaDaDenaro = abs(xDenaro - self.x) + abs(yDenaro - self.y)
            if vistoesca:
                self.xObbiettivo = vitaesca[escabersaglio + 2]
                self.yObbiettivo = vitaesca[escabersaglio + 3]
            elif vistoRallo and (not vistoRob or distanzaDaRallo <= distanzaDaColco):
                self.xObbiettivo = x
                self.yObbiettivo = y
            elif vistoRob and (not vistoDenaro or distanzaDaColco <= distanzaDaDenaro):
                self.xObbiettivo = rx
                self.yObbiettivo = ry
                attrobo = True
            elif vistoDenaro:
                self.xObbiettivo = xDenaro
                self.yObbiettivo = yDenaro

        if self.xObbiettivo and self.yObbiettivo:
            self.xPosizioneUltimoBersaglio = self.xObbiettivo
            self.yPosizioneUltimoBersaglio = self.yObbiettivo
        elif self.x == self.xPosizioneUltimoBersaglio and self.y == self.yPosizioneUltimoBersaglio:
            self.xPosizioneUltimoBersaglio = False
            self.yPosizioneUltimoBersaglio = False

        return vistoRallo, vistoRob, vistoesca, escabersaglio, vistoDenaro, xDenaro, yDenaro, attrobo
