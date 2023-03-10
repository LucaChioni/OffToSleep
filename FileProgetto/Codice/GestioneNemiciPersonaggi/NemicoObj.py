# -*- coding: utf-8 -*-

import random
import pygame
import copy
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc


class NemicoObj(object):

    def __init__(self, x, y, direzione, tipo, stanza, percorso, numeroMovimento=0, triggerato=False, monetePossedute=-1, nonCaricareImg=False, posizioneOriginale=False, id=False):
        if id:
            self.id = id
            GlobalGameVar.listaIdNemiciUsati.append(id)
        else:
            trovatoId = False
            while not trovatoId:
                GlobalGameVar.idNemico += 1
                if not GlobalGameVar.idNemico in GlobalGameVar.listaIdNemiciUsati:
                    self.id = GlobalGameVar.idNemico
                    GlobalGameVar.listaIdNemiciUsati.append(GlobalGameVar.idNemico)
                    trovatoId = True
        if posizioneOriginale:
            self.posizioneOriginale = posizioneOriginale
        else:
            self.posizioneOriginale = (x, y)
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
        # il vettore "obbiettivo" contiene nome, x, y e path dell'obiettivo
        self.obbiettivo = ["", 0, 0, []]
        self.xPosizioneUltimoBersaglio = False
        self.yPosizioneUltimoBersaglio = False
        self.quadrettoSottoOggettoLanciato = 0
        self.quadrettoSottoArma = 0
        self.ralloParato = False
        self.statoInizioTurno = []
        # il vettore "bersaglioColpito" contiene: bersaglio, danno, statoInflitto e se l'attacco è stato mortale o no
        self.bersaglioColpito = []
        self.caseattactot = []
        self.caselleAttaccabiliAggiornate = False
        self.ultimaPosizioneConCaselleAttaccabiliAggiornate = [0, 0]
        self.direzione = direzione
        self.mosseRimaste = 0
        self.animaSpostamento = False
        self.animaAttacco = False
        self.animaMorte = False
        self.animaDanneggiamento = []
        self.animazioneFatta = False
        self.tipo = tipo

        self.inizializzaStatistiche(monetePossedute)
        self.caricaImg(nonCaricareImg=nonCaricareImg)
        self.girati(direzione)

    def inizializzaStatistiche(self, monetePossedute):
        vitaTotale = 0
        attacco = 0
        difesa = 0
        velocita = 0
        raggioVisivo = 0
        attaccaDaLontano = False
        velenoso = False
        surriscaldante = False
        avvelenabile = True
        denaro = 0
        esp = 0
        ignoraEsche = False

        if self.tipo == "Orco":
            vitaTotale = 10
            attacco = 5
            difesa = 1
            velocita = -1
            raggioVisivo = GlobalHWVar.gpx * 3
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = 0
            esp = 0
        if self.tipo == "Pipistrello":
            vitaTotale = 5
            attacco = 3
            difesa = 0
            velocita = 0
            raggioVisivo = GlobalHWVar.gpx * 3
            attaccaDaLontano = True
            velenoso = True
            surriscaldante = False
            avvelenabile = False
            denaro = 0
            esp = 0

        if self.tipo == "TartarugaVerde":
            vitaTotale = 20
            attacco = 8
            difesa = 3
            velocita = -2
            raggioVisivo = GlobalHWVar.gpx * 2
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 1)
            esp = 1
        if self.tipo == "TartarugaMarrone":
            vitaTotale = 20
            attacco = 10
            difesa = 3
            velocita = -1
            raggioVisivo = GlobalHWVar.gpx * 3
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(0, 2)
            esp = 3
        if self.tipo == "LupoGrigio":
            vitaTotale = 30
            attacco = 17
            difesa = 2
            velocita = 0
            raggioVisivo = GlobalHWVar.gpx * 5
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(1, 4)
            esp = 8
        if self.tipo == "LupoBianco":
            vitaTotale = 50
            attacco = 24
            difesa = 2
            velocita = 0
            raggioVisivo = GlobalHWVar.gpx * 5
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(3, 6)
            esp = 12
        if self.tipo == "LupoNero":
            vitaTotale = 80
            attacco = 30
            difesa = 2
            velocita = 0
            raggioVisivo = GlobalHWVar.gpx * 5
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(5, 8)
            esp = 15
        if self.tipo == "Cinghiale":
            vitaTotale = 200
            attacco = 50
            difesa = 8
            velocita = 0
            raggioVisivo = GlobalHWVar.gpx * 4
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(15, 20)
            esp = 50

        if self.tipo == "Cittadino1":
            vitaTotale = 40
            attacco = GlobalGameVar.dannoMortale
            difesa = 0
            velocita = 1
            raggioVisivo = GlobalHWVar.gpx * 6
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = 0
            esp = 0
            ignoraEsche = True
        if self.tipo == "Cittadino3":
            vitaTotale = 40
            attacco = GlobalGameVar.dannoMortale
            difesa = 0
            velocita = 1
            raggioVisivo = GlobalHWVar.gpx * 6
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = 0
            esp = 0
            ignoraEsche = True

        if self.tipo == "SerpeVerde":
            vitaTotale = 200
            attacco = 45
            difesa = 5
            velocita = 1
            raggioVisivo = GlobalHWVar.gpx * 4
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(8, 12)
            esp = 19
        if self.tipo == "SerpeArancio":
            vitaTotale = 300
            attacco = 55
            difesa = 7
            velocita = 1
            raggioVisivo = GlobalHWVar.gpx * 4
            attaccaDaLontano = False
            velenoso = True
            surriscaldante = False
            avvelenabile = False
            denaro = random.randint(13, 15)
            esp = 36
        if self.tipo == "RagnoNero":
            vitaTotale = 400
            attacco = 70
            difesa = 10
            velocita = 0
            raggioVisivo = GlobalHWVar.gpx * 5
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(8, 12)
            esp = 22
        if self.tipo == "RagnoRosso":
            vitaTotale = 400
            attacco = 60
            difesa = 10
            velocita = 0
            raggioVisivo = GlobalHWVar.gpx * 5
            attaccaDaLontano = True
            velenoso = True
            surriscaldante = False
            avvelenabile = False
            denaro = random.randint(13, 15)
            esp = 34
        if self.tipo == "Scorpione":
            vitaTotale = 1000
            attacco = 80
            difesa = 15
            velocita = 1
            raggioVisivo = GlobalHWVar.gpx * 4
            attaccaDaLontano = False
            velenoso = True
            surriscaldante = False
            avvelenabile = False
            denaro = random.randint(25, 30)
            esp = 120

        if self.tipo == "GufoMarrone":
            vitaTotale = 500
            attacco = 100
            difesa = 15
            velocita = 1
            raggioVisivo = GlobalHWVar.gpx * 6
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(35, 40)
            esp = 82
        if self.tipo == "GufoBianco":
            vitaTotale = 800
            attacco = 140
            difesa = 20
            velocita = 1
            raggioVisivo = GlobalHWVar.gpx * 6
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(55, 60)
            esp = 168
        if self.tipo == "Struzzo":
            vitaTotale = 1000
            attacco = 200
            difesa = 30
            velocita = 0
            raggioVisivo = GlobalHWVar.gpx * 4
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(40, 45)
            esp = 124
        if self.tipo == "Casuario":
            vitaTotale = 1500
            attacco = 180
            difesa = 30
            velocita = 0
            raggioVisivo = GlobalHWVar.gpx * 4
            attaccaDaLontano = False
            velenoso = True
            surriscaldante = False
            avvelenabile = False
            denaro = random.randint(60, 65)
            esp = 236
        if self.tipo == "Falco":
            vitaTotale = 1500
            attacco = 180
            difesa = 25
            velocita = 1
            raggioVisivo = GlobalHWVar.gpx * 7
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(70, 75)
            esp = 277
        if self.tipo == "Aquila":
            vitaTotale = 2000
            attacco = 250
            difesa = 25
            velocita = 1
            raggioVisivo = GlobalHWVar.gpx * 7
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = random.randint(200, 220)
            esp = 1000

        if self.tipo == "ServoSpada":
            vitaTotale = 1500
            attacco = 250
            difesa = 30
            velocita = 0
            raggioVisivo = GlobalHWVar.gpx * 5
            attaccaDaLontano = False
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = 0
            esp = 158
            ignoraEsche = True
        if self.tipo == "ServoArco":
            vitaTotale = 1000
            attacco = 180
            difesa = 30
            velocita = 0
            raggioVisivo = GlobalHWVar.gpx * 6
            attaccaDaLontano = True
            velenoso = False
            surriscaldante = False
            avvelenabile = True
            denaro = 0
            esp = 181
            ignoraEsche = True
        if self.tipo == "ServoLancia":
            vitaTotale = 1500
            attacco = 200
            difesa = 30
            velocita = 0
            raggioVisivo = GlobalHWVar.gpx * 5
            attaccaDaLontano = False
            velenoso = True
            surriscaldante = False
            avvelenabile = True
            denaro = 0
            esp = 203
            ignoraEsche = True

        if self.tipo == "RoboLeggero":
            vitaTotale = 1000
            attacco = 400
            difesa = 60
            velocita = 1
            raggioVisivo = GlobalHWVar.gpx * 3
            attaccaDaLontano = True
            velenoso = False
            surriscaldante = False
            avvelenabile = False
            denaro = 0
            esp = 300
        if self.tipo == "RoboVolante":
            vitaTotale = 1000
            attacco = 300
            difesa = 50
            velocita = 2
            raggioVisivo = GlobalHWVar.gpx * 8
            attaccaDaLontano = True
            velenoso = False
            surriscaldante = False
            avvelenabile = False
            denaro = 0
            esp = 350
        if self.tipo == "RoboPesante":
            vitaTotale = 2000
            attacco = 600
            difesa = 80
            velocita = 0
            raggioVisivo = GlobalHWVar.gpx * 4
            attaccaDaLontano = True
            velenoso = False
            surriscaldante = False
            avvelenabile = False
            denaro = 0
            esp = 500
        if self.tipo == "RoboPesanteVolante":
            vitaTotale = 1500
            attacco = 500
            difesa = 70
            velocita = 1
            raggioVisivo = GlobalHWVar.gpx * 8
            attaccaDaLontano = True
            velenoso = False
            surriscaldante = False
            avvelenabile = False
            denaro = 0
            esp = 550
        if self.tipo == "RoboTorre":
            vitaTotale = 2500
            attacco = 1000
            difesa = 120
            velocita = -1
            raggioVisivo = GlobalHWVar.gpx * 7
            attaccaDaLontano = True
            velenoso = False
            surriscaldante = False
            avvelenabile = False
            denaro = 0
            esp = 5000

        self.vita = vitaTotale
        self.vitaTotale = vitaTotale
        self.esp = esp
        self.raggioVisivo = raggioVisivo
        self.velocita = velocita
        self.attacco = attacco
        self.attaccaDaLontano = attaccaDaLontano
        self.velenoso = velenoso
        self.surriscaldante = surriscaldante
        if monetePossedute != -1:
            self.denaro = monetePossedute
        else:
            self.denaro = denaro
        self.difesa = difesa
        self.avvelenabile = avvelenabile
        self.ignoraEsche = ignoraEsche

    def caricaImg(self, nonCaricareImg=False):
        self.imgW = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgW"]
        self.imgA = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgA"]
        self.imgS = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgS"]
        self.imgD = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgD"]

        self.imgWMov1 = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgWMov1"]
        self.imgWMov2 = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgWMov2"]
        self.imgAMov1 = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgAMov1"]
        self.imgAMov2 = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgAMov2"]
        self.imgSMov1 = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgSMov1"]
        self.imgSMov2 = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgSMov2"]
        self.imgDMov1 = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgDMov1"]
        self.imgDMov2 = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgDMov2"]

        self.imgAvvelenamento = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgAvvelenamento"]
        self.imgAppiccicato = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgAppiccicato"]

        self.imgAttaccoW = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgAttaccoW"]
        self.imgAttaccoA = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgAttaccoA"]
        self.imgAttaccoS = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgAttaccoS"]
        self.imgAttaccoD = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgAttaccoD"]
        if self.attaccaDaLontano:
            self.imgOggettoLanciato = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgOggettoLanciato"]
            self.imgDanneggiamentoOggettoLanciato = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgDanneggiamentoOggettoLanciato"]
        else:
            self.imgOggettoLanciato = 0
            self.imgDanneggiamentoOggettoLanciato = 0

        self.imgDanneggiamentoRallo = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgDanneggiamentoRalloNemico"]
        self.imgDanneggiamentoColco = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgDanneggiamentoColcoNemico"]
        self.posizMorte = random.randint(1, 3)
        if self.tipo.startswith("Servo"):
            self.imgMorte = GlobalImgVar.dictImgPersonaggiOggettoSpecifici["OggettoDictCadavereSoldatoCastello" + str(self.posizMorte)]
        else:
            self.imgMorte = GlobalImgVar.dictImgPersonaggiOggettoSpecifici["OggettoDictCadavere" + self.tipo + str(self.posizMorte)]

        if nonCaricareImg:
            self.imgCampoAttaccabile = False
        else:
            self.imgCampoAttaccabile = GlobalImgVar.dictImgCampiVisiviNemici[str(self.raggioVisivo // GlobalHWVar.gpx)]

    def copiaImgs(self, nemicoDaCopiare):
        self.imgW = nemicoDaCopiare.imgW
        self.imgA = nemicoDaCopiare.imgA
        self.imgS = nemicoDaCopiare.imgS
        self.imgD = nemicoDaCopiare.imgD

        self.imgWMov1 = nemicoDaCopiare.imgWMov1
        self.imgWMov2 = nemicoDaCopiare.imgWMov2
        self.imgAMov1 = nemicoDaCopiare.imgAMov1
        self.imgAMov2 = nemicoDaCopiare.imgAMov2
        self.imgSMov1 = nemicoDaCopiare.imgSMov1
        self.imgSMov2 = nemicoDaCopiare.imgSMov2
        self.imgDMov1 = nemicoDaCopiare.imgDMov1
        self.imgDMov2 = nemicoDaCopiare.imgDMov2

        self.imgAvvelenamento = nemicoDaCopiare.imgAvvelenamento
        self.imgAppiccicato = nemicoDaCopiare.imgAppiccicato

        self.imgAttaccoW = nemicoDaCopiare.imgAttaccoW
        self.imgAttaccoA = nemicoDaCopiare.imgAttaccoA
        self.imgAttaccoS = nemicoDaCopiare.imgAttaccoS
        self.imgAttaccoD = nemicoDaCopiare.imgAttaccoD
        self.imgOggettoLanciato = nemicoDaCopiare.imgOggettoLanciato
        self.imgDanneggiamentoOggettoLanciato = nemicoDaCopiare.imgDanneggiamentoOggettoLanciato

        self.imgDanneggiamentoRallo = nemicoDaCopiare.imgDanneggiamentoRallo
        self.imgDanneggiamentoColco = nemicoDaCopiare.imgDanneggiamentoColco
        self.imgMorte = nemicoDaCopiare.imgMorte

        self.imgCampoAttaccabile = nemicoDaCopiare.imgCampoAttaccabile

    def creaCopia(self):
        copia = NemicoObj(self.x, self.y, self.direzione, self.tipo, self.stanzaDiAppartenenza, self.percorso)
        for variabileOriginaleKey, variabileOriginaleVal in vars(self).items():
            superficiInLista = False
            if type(variabileOriginaleVal) == list:
                for elem in variabileOriginaleVal:
                    if type(elem) == pygame.SurfaceType:
                        superficiInLista = True
                        break
            if type(variabileOriginaleVal) != pygame.SurfaceType and not superficiInLista:
                for variabileCopiaKey, variabileCopiaVal in vars(copia).items():
                    if variabileOriginaleKey == variabileCopiaKey:
                        exec ("copia.%s = copy.deepcopy(self.%s)" % (variabileOriginaleKey, variabileOriginaleKey))
                        break
        return copia

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
        # il vettore "animaDanneggiamento" contiene nome dell'attaccante e un booleano che indica se il colpo è stato mortale o no
        self.animaDanneggiamento.append(attaccante)
        danno = GenericFunc.calcoloDanni(danno, self.difesa)
        self.vita -= danno
        if self.vita <= 0:
            self.animaDanneggiamento.append(True)
            self.vita = 0
        else:
            self.animaDanneggiamento.append(False)

    def aggiornaVista(self, x, y, rx, ry, vettoreEsche, vettoreDenaro, dati, caseviste, forzaAggiornamentoCaselleAttaccabili=False):
        vistoRallo = False

        necessarioTrovareCaselleAttaccabili = False
        if (abs(self.x - x) <= self.raggioVisivo and abs(self.y - y) <= self.raggioVisivo) or (abs(self.x - rx) <= self.raggioVisivo and abs(self.y - ry) <= self.raggioVisivo):
            necessarioTrovareCaselleAttaccabili = True
        if not necessarioTrovareCaselleAttaccabili:
            i = 0
            while i < len(vettoreEsche):
                if abs(self.x - vettoreEsche[i + 2]) <= self.raggioVisivo and abs(self.y - vettoreEsche[i + 3]) <= self.raggioVisivo:
                    necessarioTrovareCaselleAttaccabili = True
                    break
                i += 4
        if not necessarioTrovareCaselleAttaccabili:
            i = 0
            while i < len(vettoreDenaro):
                if abs(self.x - vettoreDenaro[i + 1]) <= self.raggioVisivo and abs(self.y - vettoreDenaro[i + 2]) <= self.raggioVisivo:
                    necessarioTrovareCaselleAttaccabili = True
                    break
                i += 3
        if (necessarioTrovareCaselleAttaccabili and not (self.ultimaPosizioneConCaselleAttaccabiliAggiornate[0] == self.x and self.ultimaPosizioneConCaselleAttaccabiliAggiornate[1] == self.y)) or forzaAggiornamentoCaselleAttaccabili:
            self.caseattactot = GenericFunc.trovacasattaccabili(self.x, self.y, self.raggioVisivo, caseviste)
            self.caselleAttaccabiliAggiornate = True
            self.ultimaPosizioneConCaselleAttaccabiliAggiornate = [self.x, self.y]
        elif self.ultimaPosizioneConCaselleAttaccabiliAggiornate[0] == self.x and self.ultimaPosizioneConCaselleAttaccabiliAggiornate[1] == self.y:
            self.caselleAttaccabiliAggiornate = True
        else:
            self.caselleAttaccabiliAggiornate = False

        if abs(x - self.x) <= self.raggioVisivo and abs(y - self.y) <= self.raggioVisivo and dati[5] > 0:
            j = 0
            while j < len(self.caseattactot):
                if self.caseattactot[j] == x and self.caseattactot[j + 1] == y:
                    if self.caseattactot[j + 2]:
                        vistoRallo = True
                        self.xPosizioneUltimoBersaglio = x
                        self.yPosizioneUltimoBersaglio = y
                    break
                j += 3
        if abs(rx - self.x) <= self.raggioVisivo and abs(ry - self.y) <= self.raggioVisivo and dati[10] > 0:
            j = 0
            while j < len(self.caseattactot):
                if self.caseattactot[j] == rx and self.caseattactot[j + 1] == ry:
                    if self.caseattactot[j + 2]:
                        self.xPosizioneUltimoBersaglio = rx
                        self.yPosizioneUltimoBersaglio = ry
                    break
                j += 3
        if vistoRallo:
            self.visto = True
        else:
            self.visto = False

    def aggiornaBersaglioAttacchiDistanti(self, x, y, rx, ry, attaccoADistanza, listaNemiciAttaccatiADistanzaRobo):
        if self.obbiettivo[0] == "":
            if attaccoADistanza and type(attaccoADistanza) is not str and self.x == attaccoADistanza.x and self.y == attaccoADistanza.y:
                self.triggerato = True
                self.xPosizioneUltimoBersaglio = x
                self.yPosizioneUltimoBersaglio = y
            elif listaNemiciAttaccatiADistanzaRobo:
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    if type(nemico) is not str and self.x == nemico.x and self.y == nemico.y:
                        self.triggerato = True
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

    def settaObbiettivoDalSalvataggio(self, x, y, rx, ry, vettoreEsche, vettoreDenaro, listaNemici, listaPersonaggi, dati, caseviste):
        if self.obbiettivo[1] != 0 and self.obbiettivo[2] != 0:
            vetNemiciSoloConXeY = []
            if dati[10] <= 0:
                vetNemiciSoloConXeY.append(rx)
                vetNemiciSoloConXeY.append(ry)
            for nemico in listaNemici:
                if not (nemico.x == self.x and nemico.y == self.y):
                    vetNemiciSoloConXeY.append(nemico.x)
                    vetNemiciSoloConXeY.append(nemico.y)
            for personaggio in listaPersonaggi:
                vetNemiciSoloConXeY.append(personaggio.x)
                vetNemiciSoloConXeY.append(personaggio.y)
            escaTrovata = False
            i = 0
            while i < len(vettoreEsche):
                if self.obbiettivo[1] == vettoreEsche[i + 2] and self.obbiettivo[2] == vettoreEsche[i + 3] and vettoreEsche[i + 1] > 0:
                    self.obbiettivo[0] = "Esca"
                    self.obbiettivo[3] = GenericFunc.pathFinding(self.x, self.y, vettoreEsche[i + 2], vettoreEsche[i + 3], vetNemiciSoloConXeY, caseviste)
                    escaTrovata = True
                    break
                i += 4
            if not escaTrovata:
                if self.obbiettivo[1] == x and self.obbiettivo[2] == y and dati[5] > 0:
                    self.obbiettivo[0] = "Rallo"
                    self.obbiettivo[3] = GenericFunc.pathFinding(self.x, self.y, x, y, vetNemiciSoloConXeY, caseviste)
                elif self.obbiettivo[1] == rx and self.obbiettivo[2] == ry and dati[10] > 0:
                    self.obbiettivo[0] = "Colco"
                    self.obbiettivo[3] = GenericFunc.pathFinding(self.x, self.y, rx, ry, vetNemiciSoloConXeY, caseviste)
                else:
                    i = 0
                    while i < len(vettoreDenaro):
                        if self.obbiettivo[1] == vettoreDenaro[i + 1] and self.obbiettivo[2] == vettoreDenaro[i + 2]:
                            self.obbiettivo[0] = "Monete"
                            self.obbiettivo[3] = GenericFunc.pathFinding(self.x, self.y, vettoreDenaro[i + 1], vettoreDenaro[i + 2], vetNemiciSoloConXeY, caseviste)
                            break
                        i += 3

    def settaObbiettivo(self, x, y, rx, ry, dati, vettoreDenaro, vettoreEsche, listaPersonaggi, listaNemici, porte, caseviste):
        vistoRallo = False
        vistoRob = False
        vistoesca = False
        escabersaglio = 0
        vistoDenaro = False
        xDenaro = False
        yDenaro = False

        distanzaDaRallo = -1
        pathPerRallo = []
        distanzaDaColco = -1
        pathPerColco = []
        primaesca = True
        distanzaDaEsca = -1
        distMinXEsca = -1
        distMinYEsca = -1
        pathPerEsca = []
        primoDenaro = True
        distanzaDaDenaro = -1
        distMinXDenaro = -1
        distMinYDenaro = -1
        pathPerDenaro = []

        vetNemiciSoloConXeY = []
        if dati[10] <= 0:
            vetNemiciSoloConXeY.append(rx)
            vetNemiciSoloConXeY.append(ry)
        for nemico in listaNemici:
            if not (nemico.x == self.x and nemico.y == self.y) and nemico.vita > 0:
                vetNemiciSoloConXeY.append(nemico.x)
                vetNemiciSoloConXeY.append(nemico.y)
        for personaggio in listaPersonaggi:
            vetNemiciSoloConXeY.append(personaggio.x)
            vetNemiciSoloConXeY.append(personaggio.y)

        # se l'obiettivo precedente è un'esca che esiste ancora, che puoi ancora raggiungere me che non vedi più non cambi bersaglio a meno che non vedi un'altra esca (corregge il caso in cui il nemico vede te o colco e non più l'esca => fa avanti e indietro di continuo)
        escaVecchiaAncoraRaggiungibilie = False
        if self.obbiettivo[0] == "Esca":
            j = 0
            while j < len(self.caseattactot):
                i = 0
                while i < len(vettoreEsche):
                    if self.caseattactot[j] == vettoreEsche[i + 2] and self.caseattactot[j + 1] == vettoreEsche[i + 3] and vettoreEsche[i + 1] > 0:
                        if not self.caseattactot[j + 2] and self.obbiettivo[1] == self.caseattactot[j] and self.obbiettivo[2] == self.caseattactot[j + 1]:
                            # nel caso c'è l'esca aggiungo rallo e colco agli ostacoli
                            vetNemiciSoloConXeY.append(x)
                            vetNemiciSoloConXeY.append(y)
                            vetNemiciSoloConXeY.append(rx)
                            vetNemiciSoloConXeY.append(ry)
                            pathPerEscaVecchia = GenericFunc.pathFinding(self.x, self.y, vettoreEsche[i + 2], vettoreEsche[i + 3], vetNemiciSoloConXeY, caseviste)
                            if pathPerEscaVecchia:
                                self.obbiettivo = ["Esca", vettoreEsche[i + 2], vettoreEsche[i + 3], pathPerEscaVecchia]
                                escaVecchiaAncoraRaggiungibilie = True
                        break
                    i += 4
                j += 3
        # tolgo rallo e colco dagli ostacoli nel caso fossero stati aggiunti durante la ricerca dell'esca vecchia
        i = 0
        while i < len(vetNemiciSoloConXeY):
            if vetNemiciSoloConXeY[i] == x and vetNemiciSoloConXeY[i + 1] == y:
                del vetNemiciSoloConXeY[i + 1]
                del vetNemiciSoloConXeY[i]
            elif vetNemiciSoloConXeY[i] == rx and vetNemiciSoloConXeY[i + 1] == ry and dati[10] > 0:
                del vetNemiciSoloConXeY[i + 1]
                del vetNemiciSoloConXeY[i]
            else:
                i += 2
        # se l'obiettivo precedente è in una casella vicina, non si è spostato e è prioritario rispetto a tutte le cose che vedi => non cerchi altri obiettivi
        inutileCalcolareObbiettivo = False
        if self.obbiettivo[0] != "" and ((self.obbiettivo[1] == self.x + GlobalHWVar.gpx and self.obbiettivo[2] == self.y) or (self.obbiettivo[1] == self.x - GlobalHWVar.gpx and self.obbiettivo[2] == self.y) or (self.obbiettivo[1] == self.x and self.obbiettivo[2] == self.y + GlobalHWVar.gpy) or (self.obbiettivo[1] == self.x and self.obbiettivo[2] == self.y - GlobalHWVar.gpy)):
            if self.obbiettivo[0] == "Esca":
                # controllo se esiste ancora l'obiettivo precedente
                i = 0
                while i < len(vettoreEsche):
                    if self.obbiettivo[1] == vettoreEsche[i + 2] and self.obbiettivo[2] == vettoreEsche[i + 3] and vettoreEsche[i + 1] > 0:
                        inutileCalcolareObbiettivo = True
                        break
                    i += 4
            elif self.obbiettivo[0] == "Colco" or self.obbiettivo[0] == "Rallo":
                # controllo se esiste ancora l'obiettivo precedente
                if self.obbiettivo[0] == "Rallo" and self.obbiettivo[1] == x and self.obbiettivo[2] == y and dati[5] > 0:
                    inutileCalcolareObbiettivo = True
                if self.obbiettivo[0] == "Colco" and self.obbiettivo[1] == rx and self.obbiettivo[2] == ry and dati[10] > 0:
                    inutileCalcolareObbiettivo = True
                # controllo se ci sono altri obiettivi (esche)
                j = 0
                while j < len(self.caseattactot):
                    i = 0
                    while i < len(vettoreEsche):
                        if self.caseattactot[j] == vettoreEsche[i + 2] and self.caseattactot[j + 1] == vettoreEsche[i + 3] and vettoreEsche[i + 1] > 0:
                            if self.caseattactot[j + 2]:
                                inutileCalcolareObbiettivo = False
                                break
                        i += 4
                    j += 3
            elif self.obbiettivo[0] == "Monete":
                # controllo se esiste ancora l'obiettivo precedente
                i = 0
                while i < len(vettoreDenaro):
                    if self.obbiettivo[1] == vettoreDenaro[i + 1] and self.obbiettivo[2] == vettoreDenaro[i + 2]:
                        inutileCalcolareObbiettivo = True
                        break
                    i += 3
                # controllo se ci sono altri obiettivi (esche, rallo o colco)
                j = 0
                while j < len(self.caseattactot):
                    i = 0
                    while i < len(vettoreEsche):
                        if self.caseattactot[j] == vettoreEsche[i + 2] and self.caseattactot[j + 1] == vettoreEsche[i + 3] and vettoreEsche[i + 1] > 0:
                            if self.caseattactot[j + 2]:
                                inutileCalcolareObbiettivo = False
                                break
                        i += 4
                    if not vistoRallo and abs(x - self.x) <= self.raggioVisivo and abs(y - self.y) <= self.raggioVisivo and dati[5] > 0:
                        if self.caseattactot[j] == x and self.caseattactot[j + 1] == y and self.caseattactot[j + 2]:
                            inutileCalcolareObbiettivo = False
                            break
                    if not vistoRob and abs(rx - self.x) <= self.raggioVisivo and abs(ry - self.y) <= self.raggioVisivo and dati[10] > 0:
                        if self.caseattactot[j] == rx and self.caseattactot[j + 1] == ry and self.caseattactot[j + 2]:
                            inutileCalcolareObbiettivo = False
                            break
                    j += 3
        if not inutileCalcolareObbiettivo:
            # cerco il bersaglio più vicino dando priorità a esche, poi colco-rallo, poi monete (se il nemico attacca da lontano non cerco il path più breve)
            if not self.ignoraEsche:
                j = 0
                while j < len(self.caseattactot):
                    i = 0
                    while i < len(vettoreEsche):
                        if self.caseattactot[j] == vettoreEsche[i + 2] and self.caseattactot[j + 1] == vettoreEsche[i + 3] and vettoreEsche[i + 1] > 0:
                            if self.caseattactot[j + 2]:
                                if primaesca:
                                    # nel caso vede un'esca aggiungo rallo e colco agli ostacoli
                                    vetNemiciSoloConXeY.append(x)
                                    vetNemiciSoloConXeY.append(y)
                                    vetNemiciSoloConXeY.append(rx)
                                    vetNemiciSoloConXeY.append(ry)
                                    if not self.attaccaDaLontano:
                                        pathPerEsca = GenericFunc.pathFinding(self.x, self.y, vettoreEsche[i + 2], vettoreEsche[i + 3], vetNemiciSoloConXeY, caseviste)
                                        if pathPerEsca and len(pathPerEsca) > 0:
                                            distanzaDaEsca = len(pathPerEsca) // 2
                                    distMinXEsca = vettoreEsche[i + 2]
                                    distMinYEsca = vettoreEsche[i + 3]
                                    escabersaglio = i
                                    vistoesca = True
                                    primaesca = False
                                else:
                                    pathPerEscaTemp = False
                                    if not self.attaccaDaLontano:
                                        pathPerEscaTemp = GenericFunc.pathFinding(self.x, self.y, vettoreEsche[i + 2], vettoreEsche[i + 3], vetNemiciSoloConXeY, caseviste)
                                    if (pathPerEscaTemp and (len(pathPerEscaTemp) < distanzaDaEsca or distanzaDaEsca == -1)) or (((not pathPerEscaTemp and distanzaDaEsca == -1) or self.attaccaDaLontano) and abs(vettoreEsche[i + 2] - self.x) + abs(vettoreEsche[i + 3] - self.y) < abs(distMinXEsca - self.x) + abs(distMinYEsca - self.y)):
                                        if pathPerEscaTemp and len(pathPerEscaTemp) > 0:
                                            pathPerEsca = pathPerEscaTemp
                                            distanzaDaEsca = len(pathPerEsca) // 2
                                        distMinXEsca = vettoreEsche[i + 2]
                                        distMinYEsca = vettoreEsche[i + 3]
                                        escabersaglio = i
                            break
                        i += 4
                    j += 3
            if not escaVecchiaAncoraRaggiungibilie:
                self.obbiettivo = ["", 0, 0, []]
                if not vistoesca or (vistoesca and distanzaDaEsca == -1 and not self.attaccaDaLontano):
                    # nel caso abbia visto un'esca devo togliere rallo e colco dagli ostacoli
                    if vistoesca:
                        i = 0
                        while i < len(vetNemiciSoloConXeY):
                            if vetNemiciSoloConXeY[i] == x and vetNemiciSoloConXeY[i + 1] == y:
                                del vetNemiciSoloConXeY[i + 1]
                                del vetNemiciSoloConXeY[i]
                            elif vetNemiciSoloConXeY[i] == rx and vetNemiciSoloConXeY[i + 1] == ry and dati[10] > 0:
                                del vetNemiciSoloConXeY[i + 1]
                                del vetNemiciSoloConXeY[i]
                            else:
                                i += 2
                    j = 0
                    while j < len(self.caseattactot):
                        # controllo caselle che si vedono (per controllare se si vedono pers o robo)
                        if not vistoRallo and abs(x - self.x) <= self.raggioVisivo and abs(y - self.y) <= self.raggioVisivo and dati[5] > 0:
                            if self.caseattactot[j] == x and self.caseattactot[j + 1] == y and self.caseattactot[j + 2]:
                                if not self.attaccaDaLontano:
                                    pathPerRallo = GenericFunc.pathFinding(self.x, self.y, x, y, vetNemiciSoloConXeY, caseviste)
                                    if pathPerRallo and len(pathPerRallo) > 0:
                                        distanzaDaRallo = len(pathPerRallo) // 2
                                vistoRallo = True
                        if not vistoRob and abs(rx - self.x) <= self.raggioVisivo and abs(ry - self.y) <= self.raggioVisivo and dati[10] > 0:
                            if self.caseattactot[j] == rx and self.caseattactot[j + 1] == ry and self.caseattactot[j + 2]:
                                if not self.attaccaDaLontano:
                                    pathPerColco = GenericFunc.pathFinding(self.x, self.y, rx, ry, vetNemiciSoloConXeY, caseviste)
                                    if pathPerColco and len(pathPerColco) > 0:
                                        distanzaDaColco = len(pathPerColco) // 2
                                vistoRob = True
                        j += 3
                if (not vistoesca or (vistoesca and distanzaDaEsca == -1 and not self.attaccaDaLontano)) and (not vistoRallo or (vistoRallo and distanzaDaRallo == -1 and not self.attaccaDaLontano)) and (not vistoRob or (vistoRob and distanzaDaColco == -1 and not self.attaccaDaLontano)):
                    j = 0
                    while j < len(self.caseattactot):
                        i = 0
                        while i < len(vettoreDenaro):
                            if self.caseattactot[j] == vettoreDenaro[i + 1] and self.caseattactot[j + 1] == vettoreDenaro[i + 2]:
                                if self.caseattactot[j + 2] and not (x == vettoreDenaro[i + 1] and y == vettoreDenaro[i + 2]) and not (rx == vettoreDenaro[i + 1] and ry == vettoreDenaro[i + 2]):
                                    eliminatoOstocoloSulleMonete = False
                                    k = 0
                                    while k < len(vetNemiciSoloConXeY):
                                        if vetNemiciSoloConXeY[k] == vettoreDenaro[i + 1] and vetNemiciSoloConXeY[k + 1] == vettoreDenaro[i + 2]:
                                            del vetNemiciSoloConXeY[k + 1]
                                            del vetNemiciSoloConXeY[k]
                                            eliminatoOstocoloSulleMonete = True
                                            break
                                        k += 2
                                    if primoDenaro:
                                        pathPerDenaro = GenericFunc.pathFinding(self.x, self.y, vettoreDenaro[i + 1], vettoreDenaro[i + 2], vetNemiciSoloConXeY, caseviste)
                                        if pathPerDenaro and len(pathPerDenaro) > 0:
                                            distanzaDaDenaro = len(pathPerDenaro) // 2
                                        distMinXDenaro = vettoreDenaro[i + 1]
                                        distMinYDenaro = vettoreDenaro[i + 2]
                                        xDenaro = distMinXDenaro
                                        yDenaro = distMinYDenaro
                                        vistoDenaro = True
                                        primoDenaro = False
                                    else:
                                        pathPerDenaroTemp = GenericFunc.pathFinding(self.x, self.y, vettoreDenaro[i + 1], vettoreDenaro[i + 2], vetNemiciSoloConXeY, caseviste)
                                        if (pathPerDenaroTemp and (len(pathPerDenaroTemp) < distanzaDaDenaro or distanzaDaDenaro == -1)) or (not pathPerDenaroTemp and distanzaDaDenaro == -1 and abs(vettoreDenaro[i + 1] - self.x) + abs(vettoreDenaro[i + 2] - self.y) < abs(distMinXDenaro - self.x) + abs(distMinYDenaro - self.y)):
                                            if pathPerDenaroTemp and len(pathPerDenaroTemp) > 0:
                                                pathPerDenaro = pathPerDenaroTemp
                                                distanzaDaDenaro = len(pathPerDenaro) // 2
                                            distMinXDenaro = vettoreDenaro[i + 1]
                                            distMinYDenaro = vettoreDenaro[i + 2]
                                            xDenaro = distMinXDenaro
                                            yDenaro = distMinYDenaro
                                    if eliminatoOstocoloSulleMonete:
                                        vetNemiciSoloConXeY.append(vettoreDenaro[i + 1])
                                        vetNemiciSoloConXeY.append(vettoreDenaro[i + 2])
                                break
                            i += 3
                        j += 3

            if vistoRallo or vistoRob or vistoesca or vistoDenaro:
                if vistoesca and (distanzaDaEsca != -1 or self.attaccaDaLontano):
                    self.obbiettivo = ["Esca", vettoreEsche[escabersaglio + 2], vettoreEsche[escabersaglio + 3], pathPerEsca]
                elif vistoDenaro and not (vistoRallo and distanzaDaRallo != -1) and not (vistoRob and distanzaDaColco != -1):
                    self.obbiettivo = ["Monete", xDenaro, yDenaro, pathPerDenaro]
                elif vistoRallo or vistoRob:
                    if self.attaccaDaLontano:
                        distanzaDaRallo = abs(self.x - x) + abs(self.y - y)
                        distanzaDaColco = abs(self.x - rx) + abs(self.y - ry)
                    if vistoRallo and (not vistoRob or -1 < distanzaDaRallo <= distanzaDaColco or -1 == distanzaDaColco < distanzaDaRallo or distanzaDaRallo == distanzaDaColco):
                        self.obbiettivo = ["Rallo", x, y, pathPerRallo]
                    elif vistoRob:
                        self.obbiettivo = ["Colco", rx, ry, pathPerColco]

        if self.obbiettivo[0] != "":
            self.xPosizioneUltimoBersaglio = self.obbiettivo[1]
            self.yPosizioneUltimoBersaglio = self.obbiettivo[2]
        elif self.xPosizioneUltimoBersaglio and self.yPosizioneUltimoBersaglio:
            if self.x == self.xPosizioneUltimoBersaglio and self.y == self.yPosizioneUltimoBersaglio:
                self.xPosizioneUltimoBersaglio = False
                self.yPosizioneUltimoBersaglio = False
            elif rx == self.xPosizioneUltimoBersaglio and ry == self.yPosizioneUltimoBersaglio and dati[10] <= 0:
                # non cancello PosizioneUltimoBersaglio finché non vede Colco
                vistoRoboMorto = False
                if abs(rx - self.x) <= self.raggioVisivo and abs(ry - self.y) <= self.raggioVisivo:
                    j = 0
                    while j < len(self.caseattactot):
                        if self.caseattactot[j] == rx and self.caseattactot[j + 1] == ry:
                            if self.caseattactot[j + 2]:
                                vistoRoboMorto = True
                            break
                        j += 3
                if vistoRoboMorto:
                    self.xPosizioneUltimoBersaglio = False
                    self.yPosizioneUltimoBersaglio = False
            else:
                for nemico in listaNemici:
                    if not (nemico.x == self.x and nemico.y == self.y) and nemico.x == self.xPosizioneUltimoBersaglio and nemico.y == self.yPosizioneUltimoBersaglio:
                        # non cancello PosizioneUltimoBersaglio finché non vede la casella
                        vistaCasellaOccupata = False
                        if abs(nemico.x - self.x) <= self.raggioVisivo and abs(nemico.y - self.y) <= self.raggioVisivo:
                            j = 0
                            while j < len(self.caseattactot):
                                if self.caseattactot[j] == nemico.x and self.caseattactot[j + 1] == nemico.y:
                                    if self.caseattactot[j + 2]:
                                        vistaCasellaOccupata = True
                                    break
                                j += 3
                        if vistaCasellaOccupata:
                            self.xPosizioneUltimoBersaglio = False
                            self.yPosizioneUltimoBersaglio = False
                        break
                i = 0
                while i < len(porte):
                    if porte[i + 1] == self.xPosizioneUltimoBersaglio and porte[i + 2] == self.yPosizioneUltimoBersaglio:
                        if not porte[i + 3]:
                            self.xPosizioneUltimoBersaglio = False
                            self.yPosizioneUltimoBersaglio = False
                        break
                    i += 4
