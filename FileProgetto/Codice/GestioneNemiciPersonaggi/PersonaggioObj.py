# -*- coding: utf-8 -*-

import os
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.SettaggiLivelli.Dialoghi.DialoghiNessuno as DialoghiNessuno
import Codice.SettaggiLivelli.Dialoghi.DialoghiTutorial as DialoghiTutorial
import Codice.SettaggiLivelli.Dialoghi.DialoghiCasa as DialoghiCasa
import Codice.SettaggiLivelli.Dialoghi.DialoghiForestaCadetta as DialoghiForestaCadetta
import Codice.SettaggiLivelli.Dialoghi.DialoghiStradaPerCitta as DialoghiStradaPerCitta
import Codice.SettaggiLivelli.Dialoghi.DialoghiCasaUfficiale as DialoghiCasaUfficiale


class PersonaggioObj(object):

    def __init__(self, x, y, direzione, tipo, stanza, avanzamentoStoria, percorso, numeroMovimento=0, avanzamentoDialogo=0, nonCaricareImg=False):
        self.tipo = tipo
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
            else:
                self.mantieniSempreASchermo = False
                self.caricaImgPersonaggio(nonCaricareImg=nonCaricareImg)
                self.girati(direzione)

        self.aggiornaDialogo(avanzamentoStoria)

    def caricaImgOggetto(self, nonCaricareImg=False):
        self.imgOggetto = []
        self.imgOggettoDialogo = []
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoLettoLucy":
            numImg = 1
            numImgDialogo = 3
            nomeImgDialogo = ["LucyDormienteDialogo1", "LucyDormienteDialogo2", "Vuota"]
        if self.tipo == "OggettoLettoHans":
            numImg = 2
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoComodinoLucy":
            numImg = 4
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoComodinoHans":
            numImg = 2
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo.startswith("OggettoFinestra"):
            numImg = 2
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoSiepe":
            numImg = 3
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoFuoco":
            numImg = 3
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoCibo":
            numImg = 3
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoMucchioLegna":
            numImg = 2
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo.startswith("OggettoLegna"):
            numImg = 2
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoCinghiale":
            numImg = 1
            numImgDialogo = 1
            nomeImgDialogo = ["CinghialeDialogo"]
        if self.tipo == "OggettoPersonaCadavereSam":
            numImg = 1
            numImgDialogo = 2
            nomeImgDialogo = ["Vuota", "FiglioUfficialeCadavereDialogo"]
        if self.tipo == "OggettoTombaSam":
            numImg = 2
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo.startswith("OggettoCartelloStaccionata"):
            numImg = 2
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        if self.tipo == "OggettoCartelloBloccoStrada":
            numImg = 2
            numImgDialogo = 1
            nomeImgDialogo = ["Vuota"]
        i = 1
        while i <= numImg:
            if nonCaricareImg:
                if not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Oggetti/" + self.tipo + str(i) + ".png"):
                    raise Exception("Immagine \"" + self.tipo + str(i) + ".png\" non trovata...")
                img = False
                self.imgOggetto.append(img)
            else:
                img = GlobalImgVar.loadImage("Risorse/Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Oggetti/" + self.tipo + str(i) + ".png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                self.imgOggetto.append(img)
            i += 1
        i = 0
        while i < numImgDialogo:
            if nonCaricareImg:
                if not os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Dialoghi/" + nomeImgDialogo[i] + ".png"):
                    raise Exception("Immagine \"" + nomeImgDialogo[i] + ".png\" non trovata...")
                img = False
                self.imgOggettoDialogo.append(img)
            else:
                img = GlobalImgVar.loadImage("Risorse/Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Dialoghi/" + nomeImgDialogo[i] + ".png", GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
                self.imgOggettoDialogo.append(img)
            i += 1

    def aggiornaImgOggetto(self, avanzamentoStoria, primoCaricamento=False):
        refreshSchermo = False

        numImgAttuale = 0
        if self.tipo == "OggettoLettoHans":
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                numImgAttuale = 1
        if self.tipo == "OggettoComodinoLucy":
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansLucy2"]:
                numImgAttuale = 1
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                numImgAttuale = 2
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
                numImgAttuale = 3
        if self.tipo == "OggettoComodinoHans":
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                numImgAttuale = 1
        if self.tipo.startswith("OggettoFinestra"):
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                numImgAttuale = 1
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
        if self.tipo.startswith("OggettoCartelloStaccionata"):
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                numImgAttuale = 1
        if self.tipo == "OggettoCartelloBloccoStrada":
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
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
            self.imgW = GlobalImgVar.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "W.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgA = GlobalImgVar.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "A.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgS = GlobalImgVar.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "S.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgD = GlobalImgVar.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "D.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)

            self.imgWMov1 = GlobalImgVar.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "WMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgWMov2 = GlobalImgVar.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "WMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgAMov1 = GlobalImgVar.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "AMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgAMov2 = GlobalImgVar.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "AMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgSMov1 = GlobalImgVar.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "SMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgSMov2 = GlobalImgVar.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "SMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgDMov1 = GlobalImgVar.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "DMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            self.imgDMov2 = GlobalImgVar.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "DMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)

            self.imgDialogo = GlobalImgVar.loadImage("Risorse/Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "Dialogo.png", GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, True)

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
        if self.tipo == "test":
            self.partiDialogo = []
            self.nome = "Bob"
            if avanzamentoStoria == 0:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = True
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Ciao, ecco la merce")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Ecco la merceee")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == 1:
                self.oggettoDato = "oggetto speciale"
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ciao, la merce è finita")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È finita?")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == 2:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = 3
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Ti sto per fare una domanda")
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
                dialogo.append(u"Mmh... è giusto...")
                dialogo.append("2+3? ... mi scusi signore ... 2+3? ...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non ho più merce")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == 3:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = True
                self.scelta = 3
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Ciao, ecco la merce")
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
                dialogo.append(u"Mmh... è giusto...")
                dialogo.append("2+3? ... mi scusi signore ... 2+3? ...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Ecco la merceee")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Vattene")
                self.partiDialogo.append(dialogo)

        if self.tipo == "Nessuno":
            self.partiDialogo, self.nome, self.oggettoDato, self.avanzaStoria, self.menuMercante, self.scelta, self.avanzaColDialogo = DialoghiNessuno.setDialogo(self.tipo, self.x, self.y, avanzamentoStoria, self.stanzaDiAppartenenza, self.avanzamentoDialogo)
        elif self.tipo == "Tutorial":
            self.partiDialogo, self.nome, self.oggettoDato, self.avanzaStoria, self.menuMercante, self.scelta, self.avanzaColDialogo = DialoghiTutorial.setDialogo(self.tipo, self.x, self.y, avanzamentoStoria, self.stanzaDiAppartenenza, self.avanzamentoDialogo)
        elif GlobalGameVar.dictStanze["casaHansLucy1"] <= self.stanzaDiAppartenenza <= GlobalGameVar.dictStanze["casaHansLucy4"]:
            self.partiDialogo, self.nome, self.oggettoDato, self.avanzaStoria, self.menuMercante, self.scelta, self.avanzaColDialogo = DialoghiCasa.setDialogo(self.tipo, self.x, self.y, avanzamentoStoria, self.stanzaDiAppartenenza, self.avanzamentoDialogo)
        elif GlobalGameVar.dictStanze["forestaCadetta1"] <= self.stanzaDiAppartenenza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
            self.partiDialogo, self.nome, self.oggettoDato, self.avanzaStoria, self.menuMercante, self.scelta, self.avanzaColDialogo = DialoghiForestaCadetta.setDialogo(self.tipo, self.x, self.y, avanzamentoStoria, self.stanzaDiAppartenenza, self.avanzamentoDialogo)
        elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= self.stanzaDiAppartenenza <= GlobalGameVar.dictStanze["stradaPerCittà3"]:
            self.partiDialogo, self.nome, self.oggettoDato, self.avanzaStoria, self.menuMercante, self.scelta, self.avanzaColDialogo = DialoghiStradaPerCitta.setDialogo(self.tipo, self.x, self.y, avanzamentoStoria, self.stanzaDiAppartenenza, self.avanzamentoDialogo)
        elif GlobalGameVar.dictStanze["casaDavid1"] <= self.stanzaDiAppartenenza <= GlobalGameVar.dictStanze["casaDavid3"]:
            self.partiDialogo, self.nome, self.oggettoDato, self.avanzaStoria, self.menuMercante, self.scelta, self.avanzaColDialogo = DialoghiCasaUfficiale.setDialogo(self.tipo, self.x, self.y, avanzamentoStoria, self.stanzaDiAppartenenza, self.avanzamentoDialogo)

    def spostati(self, x, y, rx, ry, listaNemici, listaPersonaggi, caseviste):
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

        if not movimentoAnnullato:
            if self.numeroMovimento < len(self.percorso) - 1:
                self.numeroMovimento += 1
            else:
                self.numeroMovimento = 0
