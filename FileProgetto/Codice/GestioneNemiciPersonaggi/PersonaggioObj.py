# -*- coding: utf-8 -*-

import os
import pygame
import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto
import Codice.SettaggiLivelli.SetDialoghiPersonaggi as SetDialoghiPersonaggi


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

        if self.tipo != "Tutorial" and self.tipo != "Nessuno":
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
                self.caricaImgPersonaggio(nonCaricareImg=nonCaricareImg)
                self.girati(direzione)

        self.aggiornaDialogo(avanzamentoStoria)

    def caricaImgOggetto(self, nonCaricareImg=False):
        self.imgOggetto = []
        self.imgOggettoDialogo = []
        disegnaImg = False
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoLettoLucy":
            disegnaImg = False
            numImg = 1
            numImgDialogo = 3
            nomeImgDialogo = ["LucyDormienteDialogo1", "LucyDormienteDialogo2", "Vuota"]
        if self.tipo == "OggettoComodinoLucy":
            disegnaImg = True
            numImg = 4
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoSiepe":
            disegnaImg = True
            numImg = 3
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoFuoco":
            disegnaImg = True
            numImg = 3
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoCibo":
            disegnaImg = True
            numImg = 3
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoMucchioLegna":
            disegnaImg = True
            numImg = 2
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo.startswith("OggettoLegna"):
            disegnaImg = True
            numImg = 2
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoCinghiale":
            disegnaImg = False
            numImg = 1
            numImgDialogo = 1
            nomeImgDialogo = ["CinghialeDialogo"]
        if self.tipo == "OggettoPersonaCadavereSam":
            disegnaImg = True
            numImg = 1
            numImgDialogo = 2
            nomeImgDialogo = ["Vuota", "FiglioUfficialeCadavereDialogo"]
        if self.tipo == "OggettoTombaSam":
            disegnaImg = True
            numImg = 2
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoMadreUfficialeSeduta":
            disegnaImg = True
            numImg = 1
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoPadreUfficialeSeduto":
            disegnaImg = True
            numImg = 1
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoPersonaCittadino3Cadavere":
            disegnaImg = True
            numImg = 1
            numImgDialogo = 1
            nomeImgDialogo = ["Cittadino3CadavereDialogo"]
        if self.tipo == "OggettoPersonaCittadino1Cadavere":
            disegnaImg = True
            numImg = 1
            numImgDialogo = 1
            nomeImgDialogo = ["Cittadino1CadavereDialogo"]
        if self.tipo == "OggettoAssistBiblioteca":
            disegnaImg = False
            numImg = 1
            numImgDialogo = 1
            nomeImgDialogo = ["AssistBibliotecaDialogo"]
        if self.tipo == "OggettoLibreriaRegistri":
            disegnaImg = True
            numImg = 2
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoRegistroBiblioteca":
            disegnaImg = True
            numImg = 2
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoVomito":
            disegnaImg = True
            numImg = 2
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoMocio":
            disegnaImg = True
            numImg = 1
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoLucySeduta":
            disegnaImg = True
            numImg = 1
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]

        i = 1
        while i <= numImg:
            if nonCaricareImg:
                if disegnaImg and not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Oggetti/" + self.tipo + str(i) + ".png"):
                    raise Exception("Immagine \"" + self.tipo + str(i) + ".png\" non trovata...")
                img = False
                self.imgOggetto.append(img)
            else:
                if disegnaImg:
                    img = CaricaFileProgetto.loadImage("Risorse/Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Oggetti/" + self.tipo + str(i) + ".png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                else:
                    img = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
                self.imgOggetto.append(img)
            i += 1
        i = 0
        while i < numImgDialogo:
            if nonCaricareImg:
                if nomeImgDialogo[i] != "Vuota" and not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Dialoghi/" + nomeImgDialogo[i] + ".png"):
                    raise Exception("Immagine \"" + nomeImgDialogo[i] + ".png\" non trovata...")
                img = False
                self.imgOggettoDialogo.append(img)
            else:
                if nomeImgDialogo[i] != "Vuota":
                    img = CaricaFileProgetto.loadImage("Risorse/Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Dialoghi/" + nomeImgDialogo[i] + ".png", GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
                else:
                    img = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
                self.imgOggettoDialogo.append(img)
            i += 1

    def aggiornaImgOggetto(self, avanzamentoStoria, primoCaricamento=False):
        refreshSchermo = False

        numImgAttuale = 0
        if self.tipo == "OggettoComodinoLucy":
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansLucy2"]:
                numImgAttuale = 1
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                numImgAttuale = 2
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
                numImgAttuale = 3
        if self.tipo == "OggettoSiepe":
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                numImgAttuale = 1
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                numImgAttuale = 2
        if self.tipo == "OggettoFuoco":
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioUltimoDialogoHans"]:
                numImgAttuale = 1
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                numImgAttuale = 2
        if self.tipo == "OggettoCibo":
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["trovatoLegna3"]:
                numImgAttuale = 1
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                numImgAttuale = 2
        if self.tipo == "OggettoMucchioLegna":
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["legnaDepositata"]:
                numImgAttuale = 1
        if self.tipo.startswith("OggettoLegna"):
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["trovatoLegna3"] or self.avanzamentoDialogo == 1:
                numImgAttuale = 1
        if self.tipo == "OggettoTombaSam":
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                numImgAttuale = 1
        if self.tipo == "OggettoLibreriaRegistri":
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["toltoRegistroBibliotecaDallaLibreria"]:
                numImgAttuale = 1
        if self.tipo == "OggettoRegistroBiblioteca":
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["messoRegistroBibliotecaSullaScrivania"]:
                numImgAttuale = 1
        if self.tipo == "OggettoVomito":
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["vomitatoInBiblioteca"]:
                numImgAttuale = 1

        if primoCaricamento or self.imgAttuale != self.imgOggetto[numImgAttuale]:
            refreshSchermo = True
            self.imgAttuale = self.imgOggetto[numImgAttuale]
            self.imgW = self.imgAttuale
            self.imgA = self.imgAttuale
            self.imgS = self.imgAttuale
            self.imgD = self.imgAttuale
            self.imgAggiornata = True

        numImgAttualeDialogo = 0
        if self.tipo == "OggettoLettoLucy":
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ottenutoBicchiereAcqua"]:
                numImgAttualeDialogo = 0
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                numImgAttualeDialogo = 1
            else:
                numImgAttualeDialogo = 2
        if self.tipo == "OggettoPersonaCadavereSam":
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cinghialeUcciso"]:
                numImgAttualeDialogo = 0
            else:
                numImgAttualeDialogo = 1
        self.imgDialogo = self.imgOggettoDialogo[numImgAttualeDialogo]

        if not primoCaricamento:
            return refreshSchermo

    def caricaImgPersonaggio(self, nonCaricareImg=False):
        if nonCaricareImg:
            if not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "W.png"):
                raise Exception("Immagine \"" + self.tipo + "W.png\" non trovata...")
            self.imgW = False
            if not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "A.png"):
                raise Exception("Immagine \"" + self.tipo + "A.png\" non trovata...")
            self.imgA = False
            if not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "S.png"):
                raise Exception("Immagine \"" + self.tipo + "S.png\" non trovata...")
            self.imgS = False
            if not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "D.png"):
                raise Exception("Immagine \"" + self.tipo + "D.png\" non trovata...")
            self.imgD = False

            if not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "WMov1.png"):
                raise Exception("Immagine \"" + self.tipo + "WMov1.png\" non trovata...")
            self.imgWMov1 = False
            if not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "WMov2.png"):
                raise Exception("Immagine \"" + self.tipo + "WMov2.png\" non trovata...")
            self.imgWMov2 = False
            if not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "AMov1.png"):
                raise Exception("Immagine \"" + self.tipo + "AMov1.png\" non trovata...")
            self.imgAMov1 = False
            if not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "AMov2.png"):
                raise Exception("Immagine \"" + self.tipo + "AMov2.png\" non trovata...")
            self.imgAMov2 = False
            if not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "SMov1.png"):
                raise Exception("Immagine \"" + self.tipo + "SMov1.png\" non trovata...")
            self.imgSMov1 = False
            if not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "SMov2.png"):
                raise Exception("Immagine \"" + self.tipo + "SMov2.png\" non trovata...")
            self.imgSMov2 = False
            if not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "DMov1.png"):
                raise Exception("Immagine \"" + self.tipo + "DMov1.png\" non trovata...")
            self.imgDMov1 = False
            if not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "DMov2.png"):
                raise Exception("Immagine \"" + self.tipo + "DMov2.png\" non trovata...")
            self.imgDMov2 = False

            if not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "Dialogo.png"):
                raise Exception("Immagine \"" + self.tipo + "Dialogo.png\" non trovata...")
            self.imgDialogo = False
        else:
            self.imgW = CaricaFileProgetto.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "W.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgA = CaricaFileProgetto.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "A.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgS = CaricaFileProgetto.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "S.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgD = CaricaFileProgetto.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "D.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)

            self.imgWMov1 = CaricaFileProgetto.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "WMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgWMov2 = CaricaFileProgetto.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "WMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgAMov1 = CaricaFileProgetto.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "AMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgAMov2 = CaricaFileProgetto.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "AMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgSMov1 = CaricaFileProgetto.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "SMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgSMov2 = CaricaFileProgetto.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "SMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgDMov1 = CaricaFileProgetto.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "DMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgDMov2 = CaricaFileProgetto.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "DMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)

            self.imgDialogo = CaricaFileProgetto.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "Dialogo.png", GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, True)

    def girati(self, direzione):
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
        self.partiDialogo, self.nome, self.oggettoDato, self.avanzaStoria, self.menuMercante, self.scelta, self.avanzaColDialogo = SetDialoghiPersonaggi.caricaDialogo(self.tipoId, self.x, self.y, avanzamentoStoria, self.stanzaDiAppartenenza, self.avanzamentoDialogo, monetePossedute)

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
