# -*- coding: utf-8 -*-

import os
import pygame
import copy
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto
import Codice.SettaggiLivelli.SetDialoghiPersonaggi as SetDialoghiPersonaggi
import Codice.SettaggiLivelli.SetImgOggettiMappaPersonaggi as SetImgOggettiMappaPersonaggi


class PersonaggioObj(object):

    def __init__(self, x, y, direzione, tipoId, stanza, avanzamentoStoria, percorso, numeroMovimento=0, avanzamentoDialogo=0, nonCaricareImg=False):
        self.tipoId = tipoId

        self.tipo = tipoId.split("-")[0]
        self.x = x
        self.y = y
        self.vx = x
        self.vy = y
        self.direzione = direzione
        self.stanzaDiAppartenenza = stanza
        self.percorso = percorso
        self.numeroMovimento = numeroMovimento
        self.inCasellaVista = False
        self.vicinoACasellaVista = False
        self.oggettoEnigma = False

        self.oggettoDato = False
        self.avanzaStoria = False
        self.menuMercante = False
        self.scelta = False

        self.animaSpostamento = False
        self.animazioneFatta = False

        self.imgAggiornata = True
        # le variabili "self.avanzamentoDialogo" e "self.avanzaColDialogo" servono per cambiare dialogo e/o immagine quando l'avanzamento della storia non è abbastanza per definire l'evento che fa scatenare queste modifiche
        self.avanzamentoDialogo = avanzamentoDialogo
        self.avanzaColDialogo = False
        self.idDialogoCorrente = False

        if self.tipo in GlobalImgVar.vettoreNomiNemici and self.tipo != "ServoLancia" and self.tipo != "ServoSpada" and self.tipo != "ServoArco":
            self.mantieniSempreASchermo = False
            self.caricaImgNemico()
            self.girati(direzione)
        elif self.tipo != "Tutorial" and self.tipo != "Nessuno":
            if self.tipo.startswith("Oggetto"):
                if self.tipo.startswith("OggettoPersona"):
                    self.mantieniSempreASchermo = False
                else:
                    self.mantieniSempreASchermo = True
                self.caricaImgOggetto(nonCaricareImg=nonCaricareImg)
                self.aggiornaImgOggetto(avanzamentoStoria, True)
                if self.tipo.startswith("OggettoEnigma"):
                    self.oggettoEnigma = True
            else:
                self.mantieniSempreASchermo = False
                self.caricaImgPersonaggio()
                self.girati(direzione)
        else:
            self.imgAttuale = False
            self.imgDialogo = False

        self.aggiornaDialogo(avanzamentoStoria)
        self.gender = SetDialoghiPersonaggi.setGender(self.tipo)

    def caricaImgOggetto(self, nonCaricareImg=False):
        self.imgOggetto = []
        self.imgOggettoDialogo = []

        disegnaImg, numImg, numImgDialogo, nomeImgDialogo = SetImgOggettiMappaPersonaggi.definisciImgOggetti(self.tipo)

        i = 1
        while i <= numImg:
            if nonCaricareImg:
                if disegnaImg and not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Oggetti/" + self.tipo + str(i) + ".png") and not self.tipo.startswith("OggettoDict"):
                    raise Exception("Immagine \"" + self.tipo + str(i) + ".png\" non trovata...")
                img = False
                self.imgOggetto.append(img)
            else:
                if disegnaImg:
                    if self.tipo.startswith("OggettoDict"):
                        img = GlobalImgVar.dictImgPersonaggiOggettoSpecifici[self.tipo]
                    else:
                        img = CaricaFileProgetto.loadImage("Risorse/Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Oggetti/" + self.tipo + str(i) + ".png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)

                else:
                    img = False
                self.imgOggetto.append(img)
            i += 1
        i = 0
        while i < numImgDialogo:
            if nonCaricareImg:
                if nomeImgDialogo[i] != "Vuota" and not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Dialoghi/" + nomeImgDialogo[i] + ".png") and not nomeImgDialogo[i].startswith("OggettoDict"):
                    raise Exception("Immagine \"" + nomeImgDialogo[i] + ".png\" non trovata...")
                img = False
                self.imgOggettoDialogo.append(img)
            else:
                if nomeImgDialogo[i] != "Vuota":
                    if nomeImgDialogo[i].startswith("OggettoDict"):
                        img = GlobalImgVar.dictImgDialoghiPersonaggiOggettoSpecifici[nomeImgDialogo[i]]
                    else:
                        img = CaricaFileProgetto.loadImage("Risorse/Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Dialoghi/" + nomeImgDialogo[i] + ".png", GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
                else:
                    img = False
                self.imgOggettoDialogo.append(img)
            i += 1

    def aggiornaImgOggetto(self, avanzamentoStoria, primoCaricamento=False):
        refreshSchermo = False

        numImgAttuale = SetImgOggettiMappaPersonaggi.impostaImgOggettoDaUsare(self.tipo, avanzamentoStoria, self.avanzamentoDialogo)
        if primoCaricamento or self.imgAttuale != self.imgOggetto[numImgAttuale]:
            refreshSchermo = True
            self.imgAttuale = self.imgOggetto[numImgAttuale]
            self.imgW = self.imgAttuale
            self.imgA = self.imgAttuale
            self.imgS = self.imgAttuale
            self.imgD = self.imgAttuale
            self.imgAggiornata = True

        numImgAttualeDialogo = SetImgOggettiMappaPersonaggi.impostaImgOggettoDialogoDaUsare(self.tipo, avanzamentoStoria, self.avanzamentoDialogo)
        self.imgDialogo = self.imgOggettoDialogo[numImgAttualeDialogo]

        if not primoCaricamento:
            return refreshSchermo

    def caricaImgPersonaggio(self):
        self.imgW = GlobalImgVar.dictionaryImgPersonaggi[self.tipo]["imgW"]
        self.imgA = GlobalImgVar.dictionaryImgPersonaggi[self.tipo]["imgA"]
        self.imgS = GlobalImgVar.dictionaryImgPersonaggi[self.tipo]["imgS"]
        self.imgD = GlobalImgVar.dictionaryImgPersonaggi[self.tipo]["imgD"]

        self.imgWMov1 = GlobalImgVar.dictionaryImgPersonaggi[self.tipo]["imgWMov1"]
        self.imgWMov2 = GlobalImgVar.dictionaryImgPersonaggi[self.tipo]["imgWMov2"]
        self.imgAMov1 = GlobalImgVar.dictionaryImgPersonaggi[self.tipo]["imgAMov1"]
        self.imgAMov2 = GlobalImgVar.dictionaryImgPersonaggi[self.tipo]["imgAMov2"]
        self.imgSMov1 = GlobalImgVar.dictionaryImgPersonaggi[self.tipo]["imgSMov1"]
        self.imgSMov2 = GlobalImgVar.dictionaryImgPersonaggi[self.tipo]["imgSMov2"]
        self.imgDMov1 = GlobalImgVar.dictionaryImgPersonaggi[self.tipo]["imgDMov1"]
        self.imgDMov2 = GlobalImgVar.dictionaryImgPersonaggi[self.tipo]["imgDMov2"]

        self.imgDialogo = GlobalImgVar.dictionaryImgPersonaggi[self.tipo]["imgDialogo"]

    def caricaImgNemico(self):
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

        self.imgDialogo = GlobalImgVar.dictionaryImgNemici[self.tipo]["imgDialogo"]

    def copiaImgsPersonaggio(self, personaggioDaCopiare):
        self.imgW = personaggioDaCopiare.imgW
        self.imgA = personaggioDaCopiare.imgA
        self.imgS = personaggioDaCopiare.imgS
        self.imgD = personaggioDaCopiare.imgD

        self.imgWMov1 = personaggioDaCopiare.imgWMov1
        self.imgWMov2 = personaggioDaCopiare.imgWMov2
        self.imgAMov1 = personaggioDaCopiare.imgAMov1
        self.imgAMov2 = personaggioDaCopiare.imgAMov2
        self.imgSMov1 = personaggioDaCopiare.imgSMov1
        self.imgSMov2 = personaggioDaCopiare.imgSMov2
        self.imgDMov1 = personaggioDaCopiare.imgDMov1
        self.imgDMov2 = personaggioDaCopiare.imgDMov2

        self.imgDialogo = personaggioDaCopiare.imgDialogo

    def copiaImgsOggetto(self, oggettoDaCopiare):
        self.imgOggetto = oggettoDaCopiare.imgOggetto
        self.imgOggettoDialogo = oggettoDaCopiare.imgOggettoDialogo

    def creaCopia(self, avanzamentoStoria):
        copia = PersonaggioObj(self.x, self.y, self.direzione, self.tipoId, self.stanzaDiAppartenenza, avanzamentoStoria, self.percorso)
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

    def girati(self, direzione, perDialogo=False):
        if not perDialogo or (perDialogo and not (self.tipo == "ServoLancia" or self.tipo == "ServoSpada" or self.tipo == "ServoArco")):
            if direzione == "w":
                self.imgAttuale = self.imgW
            elif direzione == "a":
                self.imgAttuale = self.imgA
            elif direzione == "s":
                self.imgAttuale = self.imgS
            elif direzione == "d":
                self.imgAttuale = self.imgD

            if direzione != "" and direzione != "fermati" and direzione != "mantieniPosizione":
                self.direzione = direzione

    def aggiornaDialogo(self, avanzamentoStoria, monetePossedute=0):
        self.partiDialogoTradotte, self.nome, self.oggettoDato, self.avanzaStoria, self.menuMercante, self.scelta, self.avanzaColDialogo, self.idDialogoCorrente = SetDialoghiPersonaggi.caricaDialogo(self.tipoId, self.x, self.y, avanzamentoStoria, self.stanzaDiAppartenenza, self.avanzamentoDialogo, monetePossedute)

    def spostati(self, x, y, rx, ry, listaNemici, listaPersonaggi, caseviste):
        self.vx = self.x
        self.vy = self.y
        self.animaSpostamento = True
        movimentoAnnullato = False

        if len(self.percorso) > 0 and self.percorso[self.numeroMovimento] != "fermati" and self.percorso[self.numeroMovimento] != "mantieniPosizione":
            if self.percorso[self.numeroMovimento].endswith("Gira"):
                direzione = ""
                self.girati(self.percorso[self.numeroMovimento][0])
            else:
                direzione = self.percorso[self.numeroMovimento]
                self.girati(direzione)
        elif len(self.percorso) > 0 and self.percorso[self.numeroMovimento] == "mantieniPosizione":
            direzione = ""
            self.girati(self.percorso[self.numeroMovimento - 1][0])
        else:
            direzione = ""
        if direzione == "w":
            self.y -= GlobalHWVar.gpy
        elif direzione == "a":
            self.x -= GlobalHWVar.gpx
        elif direzione == "s":
            self.y += GlobalHWVar.gpy
        elif direzione == "d":
            self.x += GlobalHWVar.gpx
        else:
            self.animaSpostamento = False

        for nemico in listaNemici:
            if self.x == nemico.x and self.y == nemico.y:
                self.x = self.vx
                self.y = self.vy
                self.animaSpostamento = False
                movimentoAnnullato = True
                break
        for personaggio in listaPersonaggi:
            if self.tipo != personaggio.tipo and self.x == personaggio.x and self.y == personaggio.y:
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
        i = 0
        while i < len(caseviste):
            if caseviste[i] == self.x and caseviste[i + 1] == self.y:
                if not caseviste[i + 2]:
                    self.x = self.vx
                    self.y = self.vy
                    self.animaSpostamento = False
                    movimentoAnnullato = True
                break
            i += 3

        if not movimentoAnnullato and len(self.percorso) > 0 and self.percorso[self.numeroMovimento] != "fermati" and self.percorso[self.numeroMovimento] != "mantieniPosizione":
            if self.numeroMovimento < len(self.percorso) - 1:
                self.numeroMovimento += 1
            else:
                self.numeroMovimento = 0
