# -*- coding: utf-8 -*-

from GenericFunc import *


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
        if self.tipo == "OggettoComodinoLucy":
            numImg = 3
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
        i = 1
        while i <= numImg:
            if nonCaricareImg:
                if not GlobalVar.os.path.exists(GlobalVar.gamePath + "Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Oggetti/" + self.tipo + str(i) + ".png"):
                    raise Exception("Immagine \"" + self.tipo + str(i) + ".png\" non trovata...")
                img = False
                self.imgOggetto.append(img)
            else:
                img = GlobalVar.loadImage("Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Oggetti/" + self.tipo + str(i) + ".png", GlobalVar.gpx, GlobalVar.gpy, True)
                self.imgOggetto.append(img)
            i += 1
        i = 0
        while i < numImgDialogo:
            if nonCaricareImg:
                if not GlobalVar.os.path.exists(GlobalVar.gamePath + "Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Dialoghi/" + nomeImgDialogo[i] + ".png"):
                    raise Exception("Immagine \"" + nomeImgDialogo[i] + ".png\" non trovata...")
                img = False
                self.imgOggettoDialogo.append(img)
            else:
                img = GlobalVar.loadImage("Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Dialoghi/" + nomeImgDialogo[i] + ".png", GlobalVar.gpx * 16, GlobalVar.gpy * 12, False)
                self.imgOggettoDialogo.append(img)
            i += 1

    def aggiornaImgOggetto(self, avanzamentoStoria, primoCaricamento=False):
        refreshSchermo = False

        numImgAttuale = 0
        if self.tipo == "OggettoComodinoLucy":
            if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["dialogoCasaHansLucy2"]:
                numImgAttuale = 1
            if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
                numImgAttuale = 2
        if self.tipo == "OggettoSiepe":
            if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                numImgAttuale = 1
            if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                numImgAttuale = 2
        if self.tipo == "OggettoFuoco":
            if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["inizioUltimoDialogoHans"]:
                numImgAttuale = 1
            if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                numImgAttuale = 2
        if self.tipo == "OggettoCibo":
            if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["trovatoLegna3"]:
                numImgAttuale = 1
            if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                numImgAttuale = 2
        if self.tipo == "OggettoMucchioLegna":
            if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["legnaDepositata"]:
                numImgAttuale = 1
        if self.tipo.startswith("OggettoLegna"):
            if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["trovatoLegna3"] or self.avanzamentoDialogo == 1:
                numImgAttuale = 1
        if self.tipo == "OggettoTombaSam":
            if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
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
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["ottenutoBicchiereAcqua"]:
                numImgAttualeDialogo = 0
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                numImgAttualeDialogo = 1
            else:
                numImgAttualeDialogo = 2
        if self.tipo == "OggettoPersonaCadavereSam":
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["cinghialeUcciso"]:
                numImgAttualeDialogo = 0
            else:
                numImgAttualeDialogo = 1
        self.imgDialogo = self.imgOggettoDialogo[numImgAttualeDialogo]

        if not primoCaricamento:
            return refreshSchermo

    def caricaImgPersonaggio(self, nonCaricareImg=False):
        if nonCaricareImg:
            if not GlobalVar.os.path.exists(GlobalVar.gamePath + "Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "W.png"):
                raise Exception("Immagine \"" + self.tipo + "W.png\" non trovata...")
            self.imgW = False
            if not GlobalVar.os.path.exists(GlobalVar.gamePath + "Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "A.png"):
                raise Exception("Immagine \"" + self.tipo + "A.png\" non trovata...")
            self.imgA = False
            if not GlobalVar.os.path.exists(GlobalVar.gamePath + "Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "S.png"):
                raise Exception("Immagine \"" + self.tipo + "S.png\" non trovata...")
            self.imgS = False
            if not GlobalVar.os.path.exists(GlobalVar.gamePath + "Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "D.png"):
                raise Exception("Immagine \"" + self.tipo + "D.png\" non trovata...")
            self.imgD = False

            if not GlobalVar.os.path.exists(GlobalVar.gamePath + "Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "WMov1.png"):
                raise Exception("Immagine \"" + self.tipo + "WMov1.png\" non trovata...")
            self.imgWMov1 = False
            if not GlobalVar.os.path.exists(GlobalVar.gamePath + "Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "WMov2.png"):
                raise Exception("Immagine \"" + self.tipo + "WMov2.png\" non trovata...")
            self.imgWMov2 = False
            if not GlobalVar.os.path.exists(GlobalVar.gamePath + "Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "AMov1.png"):
                raise Exception("Immagine \"" + self.tipo + "AMov1.png\" non trovata...")
            self.imgAMov1 = False
            if not GlobalVar.os.path.exists(GlobalVar.gamePath + "Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "AMov2.png"):
                raise Exception("Immagine \"" + self.tipo + "AMov2.png\" non trovata...")
            self.imgAMov2 = False
            if not GlobalVar.os.path.exists(GlobalVar.gamePath + "Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "SMov1.png"):
                raise Exception("Immagine \"" + self.tipo + "SMov1.png\" non trovata...")
            self.imgSMov1 = False
            if not GlobalVar.os.path.exists(GlobalVar.gamePath + "Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "SMov2.png"):
                raise Exception("Immagine \"" + self.tipo + "SMov2.png\" non trovata...")
            self.imgSMov2 = False
            if not GlobalVar.os.path.exists(GlobalVar.gamePath + "Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "DMov1.png"):
                raise Exception("Immagine \"" + self.tipo + "DMov1.png\" non trovata...")
            self.imgDMov1 = False
            if not GlobalVar.os.path.exists(GlobalVar.gamePath + "Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "DMov2.png"):
                raise Exception("Immagine \"" + self.tipo + "DMov2.png\" non trovata...")
            self.imgDMov2 = False

            if not GlobalVar.os.path.exists(GlobalVar.gamePath + "Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "Dialogo.png"):
                raise Exception("Immagine \"" + self.tipo + "Dialogo.png\" non trovata...")
            self.imgDialogo = False
        else:
            self.imgW = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "W.png", GlobalVar.gpx, GlobalVar.gpy, True)
            self.imgA = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "A.png", GlobalVar.gpx, GlobalVar.gpy, True)
            self.imgS = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "S.png", GlobalVar.gpx, GlobalVar.gpy, True)
            self.imgD = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "D.png", GlobalVar.gpx, GlobalVar.gpy, True)

            self.imgWMov1 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "WMov1.png", GlobalVar.gpx, GlobalVar.gpy, True)
            self.imgWMov2 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "WMov2.png", GlobalVar.gpx, GlobalVar.gpy, True)
            self.imgAMov1 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "AMov1.png", GlobalVar.gpx, GlobalVar.gpy, True)
            self.imgAMov2 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "AMov2.png", GlobalVar.gpx, GlobalVar.gpy, True)
            self.imgSMov1 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "SMov1.png", GlobalVar.gpx, GlobalVar.gpy, True)
            self.imgSMov2 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "SMov2.png", GlobalVar.gpx, GlobalVar.gpy, True)
            self.imgDMov1 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "DMov1.png", GlobalVar.gpx, GlobalVar.gpy, True)
            self.imgDMov2 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "DMov2.png", GlobalVar.gpx, GlobalVar.gpy, True)

            self.imgDialogo = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "Dialogo.png", GlobalVar.gpx * 16, GlobalVar.gpy * 12, True)

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
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Vattene")
                self.partiDialogo.append(dialogo)
        if self.tipo == "Mercante":
            self.partiDialogo = []
            self.nome = "Bob"
            if avanzamentoStoria != 0:
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

        if self.tipo == "Tutorial":
            self.partiDialogo = []
            self.nome = "Tutorial"
            if avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["dialogoSognoLucy1"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Per muoverti usa i tasti <*>#bold#W<*>, <*>#bold#A<*>, <*>#bold#S<*> e <*>#bold#D<*> della tastiera, la <*>#bold#Croce direzionale<*> del controller oppure, utilizzando il mouse, clicca sulla casella verso cui vuoi spostarti con il tasto <*>#bold#Sinistro<*>.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Muoviti verso il baule davanti a te e prova ad aprirlo utilizzando il tasto <*>#bold#SPAZIO<*> sulla tastiera, la <*>#bold#Croce<*> sul controller oppure cliccandoci sopra con il tasto <*>#bold#Sinistro<*> del mouse.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["aperturaPrimoCofanetto"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Hai trovato una pozione. Puoi usarla dal menu a cui puoi accedere premendo <*>#bold#Esc<*> sulla tastiera, <*>#bold#Start<*> sul controller o il tasto <*>#bold#Centrale<*> del mouse.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Dal menu potrai anche accedere a \"Equipaggiamento\" dove potrai selezionare armi, protezioni e accessori da equipaggiarti.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialUtilizzoOggetti"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Davanti a te c'è un nemico. Per vedere le sue informazioni passa alla modalità interazione (premi il tasto <*>#bold#E<*> della tastiera, <*>#bold#Quadrato<*> del controller o il tasto <*>#bold#Destro<*> del mouse) e inquadralo spostando il puntatore sulla sua casella.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Una volta inquadrato puoi selezionarlo e attaccarlo premendo <*>#bold#SPAZIO<*> sulla tastiera, la <*>#bold#Croce<*> sul controller o il tasto <*>#bold#Sinistro<*> del mouse (dato che al momento non hai frecce, puoi attaccarlo solo da vicino).")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Attenzione: se ci sono dei nemici presenti nella stanza, premendo <*>#bold#Esc<*>, <*>#bold#Start<*> o il tasto <*>#bold#Centrale<*> del mouse, viene aperto un menu rapido che permette di compiere meno operazioni ripetto al menu normale.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialBattaglia"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Fai attenzione a quel pipistrello: è velenoso ed attacca a distanza!")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Se vuoi ingaggiarlo assicurati di poterlo attaccare a distanza prima che ti possa vedere.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("In quel baule potrebbe esserci qualcosa che fa al caso tuo...")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["dialogoCasaHansLucy1"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"È possibile richiudere le porte utilizzando la modalità interazione.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["dialogoCasaHansLucy2"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"In modalità interazione le caselle fuori dal tuo campo visivo vengono oscurate.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Inquadrando un nemico inoltre compaiono delle crocette rosse e nere che contrassegnano le caselle che il nemico non riesce a vedere. Quando un nemico ti vede l'occhio in alto a destra nello schermo si aprirà. Viceversa, quando sei fuori dal campo visivo di tutti i nemici, l'occhio sarà chiuso.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Dato che al momento sei disarmato non ti conviene affrontare i nemici a viso aperto: prova a passare senza farti vedere!")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialCampoVisivo"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"In modalità interazione, cliccando su te stesso assumerai una posizione difensiva che ti permetterà di subire meno danni e di recuperare qualche pv.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Usala anche fuori dal combattimento per evitare di sprecare pozioni!")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("La mappa e il diario si possono aprire dal menu cliccando sulle relative voci.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"È possibile accedere alla mappa anche dal menu rapido di battaglia.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("...")
                self.partiDialogo.append(dialogo)
        if self.tipo == "Nessuno":
            self.partiDialogo = []
            self.nome = "Nessuno"
            if avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["inizio"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Oh cavolo! Dove sono adesso!?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Mi sono persa... lo sapevo...")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialMovimento"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Dovrei aprire quel baule prima di andare... ?")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialOggettiBattaglia"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ok, Hans dovrebbe essere passato di qua... credo...")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["dialogoSognoLucy2"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Perché sono venuta qui...?")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and self.x == GlobalVar.gpx * 24 and self.y == GlobalVar.gpy * 3 and self.stanzaDiAppartenenza == GlobalVar.dictStanze["casaHansLucy1"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non voglio farmi scoprire e se entro il babbo e la mamma si sveglieranno. O forse sono ancora svegli?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("... Non lo voglio sapere... basta che non mi faccia vedere.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["dialogoCasaHansLucy2"] and (self.x == GlobalVar.gpx * 16 or self.x == GlobalVar.gpx * 17) and self.y == GlobalVar.gpy * 16 and self.stanzaDiAppartenenza == GlobalVar.dictStanze["casaHansLucy1"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Prima devo portare l'acqua a Lucy, così si riaddormenterà di nuovo e non si accorgerà che sono uscito.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["ingressoForestaCadetta"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Bene, dall'altra parte della foresta c'è la città.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialDifesa"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Pant pant...<*> non mi sono mai spinto fino a questo punto...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Dovrei essere quasi dall'altra parte.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["quartaStanzaForestaCadetta"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Un attimo, c'è qualcuno più avanti!")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Credo che dovrei parlargli, magari possiamo aiutarci per superare la notte.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["incontroFiglioUfficiale"] and ((self.x == GlobalVar.gpx * 15 and self.y == GlobalVar.gpy * 16) or (self.x == GlobalVar.gpx * 30 and self.y == GlobalVar.gpy * 8)) and self.stanzaDiAppartenenza == GlobalVar.dictStanze["forestaCadetta5"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Prima di procedere potrei chiedere a quel soldato da che parte si trova la città.")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["trovatoLegna1"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["legnaDepositata"] and self.x == GlobalVar.gpx * 16 and self.y == GlobalVar.gpy * 1 and self.stanzaDiAppartenenza == GlobalVar.dictStanze["forestaCadetta5"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non voglio portare la legna che ho raccolto in giro per la foresta!")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and self.x == GlobalVar.gpx * 15 and self.y == GlobalVar.gpy * 16 and self.stanzaDiAppartenenza == GlobalVar.dictStanze["forestaCadetta5"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Meglio prendere la legna e accamparsi qui per la notte.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and self.stanzaDiAppartenenza == GlobalVar.dictStanze["casaHansLucy1"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Mi ha portato l'acqua ma non è tornato a letto...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Dovevo immaginarlo che partiva stanotte... cosa devo fare adesso... ?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Di certo non posso dirlo al babbo: si arrabbierebbe troppo.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Mmh... provo a vedere se è ancora qua fuori da qualche parte.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["monologoRisveglioLucy"] and self.x == GlobalVar.gpx * 6 and self.y == GlobalVar.gpy * 10 and self.stanzaDiAppartenenza == GlobalVar.dictStanze["casaHansLucy1"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Aspetta! Prima di andare devo prendere la mia mappa e il diario.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Dovrei poter documentare qualcosa di interessante.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialMappaDiario"] and self.x == GlobalVar.gpx * 6 and self.y == GlobalVar.gpy * 8 and self.stanzaDiAppartenenza == GlobalVar.dictStanze["casaHansLucy1"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Fuori è troppo pericoloso a quest'ora: devo preparami prima di uscire.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Nel ripostiglio del babbo ci dovrebbe essere qualcosa di utile.")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["armaturaNonnoCompletata"] and (self.x == GlobalVar.gpx * 16 or self.x == GlobalVar.gpx * 17) and self.y == GlobalVar.gpy * 16 and self.stanzaDiAppartenenza == GlobalVar.dictStanze["casaHansLucy1"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Fuori è pericoloso! Devo prepararmi meglio prima di uscire.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Nel ripostiglio del babbo e la mamma ci dovrebbe essere qualcosa di utile.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["monologoIndicazioniArmaturaNonno"] and self.x == GlobalVar.gpx * 26 and self.y == GlobalVar.gpy * 10 and self.stanzaDiAppartenenza == GlobalVar.dictStanze["casaHansLucy1"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"No, merda! Non si apre.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("La chiave deve essere qui da qualche parte.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"] and self.x == GlobalVar.gpx * 26 and self.y == GlobalVar.gpy * 10 and self.stanzaDiAppartenenza == GlobalVar.dictStanze["casaHansLucy1"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Devo trovare la chiave per entrare!")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["armaturaNonno4"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Bene! Quest'armatura mi entra perfettamente.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Sono pronta per andare adesso.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["armaturaNonnoCompletata"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Hans? HAAANS? ... Cavolo! È pieno di bestie selvatiche qui!")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["ingressoForestaCadettaLucy"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ehi, c'è un accampamento qui!")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["accampamentoForestaAnalizzato2"] and ((self.x == GlobalVar.gpx * 15 and self.y == GlobalVar.gpy * 16) or (self.x == GlobalVar.gpx * 30 and self.y == GlobalVar.gpy * 8)) and self.stanzaDiAppartenenza == GlobalVar.dictStanze["forestaCadetta5"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Dovrei guardare bene l'accampamento per capire se Hans è stato qui.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["accampamentoForestaAnalizzato2"] and self.stanzaDiAppartenenza == GlobalVar.dictStanze["forestaCadetta7"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non sarà facile passare qua in mezzo...")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["incontratoBrancoLupiNeri"] and self.stanzaDiAppartenenza == GlobalVar.dictStanze["forestaCadetta7"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"C'è un uomo a terra e... ok, prima di tutto mi devo occupare di quel bestione.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["sotterratoSam"] and self.stanzaDiAppartenenza == GlobalVar.dictStanze["forestaCadetta7"]:
                self.oggettoDato = "Armatura d'acciaio"
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ecco fatto.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Forse non avrei dovuto prendere le sue cose, ma... non credo che gli servissero ancora...")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["monologoDopoTombaSam"] and self.stanzaDiAppartenenza == GlobalVar.dictStanze["forestaCadetta8"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Uff... ma quanto è grande questa foresta!?")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and self.y == GlobalVar.gpy * 1 and (self.x == GlobalVar.gpx * 14 or self.x == GlobalVar.gpx * 15 or self.x == GlobalVar.gpx * 16 or self.x == GlobalVar.gpx * 17) and self.stanzaDiAppartenenza == GlobalVar.dictStanze["casaHansLucy4"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"I miei genitori non se la staranno passando bene, ma non posso tornare finché non scopro dov'è andato Hans.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("...")
                self.partiDialogo.append(dialogo)

        # casa Hans e Lucy interno
        if self.tipo == "OggettoLettoLucy":
            self.partiDialogo = []
            self.nome = "Lucy"
            if avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("... Uh!?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ehi, hai fatto un brutto sogno?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("No, io stavo... stavo andando... ehm... non lo so, non importa.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Perché sei sveglio?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Stavo andando in bagno, è tutto ok?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Si, si... mi porti un bicchiere d'acqua quando torni?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Va bene.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Grazie.")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["dialogoCasaHansLucy1"] <= avanzamentoStoria <= GlobalVar.dictAvanzamentoStoria["tutorialChiusuraPorte"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Yaaawn... Sto ancora aspettando la mia acqua.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Si, sto andando.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["ottenutoBicchiere"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Dai Hans... mi hai portato un bicchiere vuoto...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ah, lo volevi con l'acqua?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Mmh...")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["ottenutoBicchiereAcqua"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Lucy... ?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Zzz...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Si è già riaddormentata... Posso partire adesso allora, prima che qualcun altro si svegli.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Zzz...")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non mi rimetterò a dormire.")
                self.partiDialogo.append(dialogo)
        if self.tipo == "OggettoLavandinoCucina" or self.tipo == "OggettoLavandinoBagno":
            self.partiDialogo = []
            self.nome = "OggettoLavandino"
            if avanzamentoStoria <= GlobalVar.dictAvanzamentoStoria["tutorialChiusuraPorte"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Devo prendere un bicchiere prima.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["ottenutoBicchiere"]:
                self.oggettoDato = "Bicchiere con acqua"
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ok, ho riempito il bicchiere.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non ho più bisogno di acqua.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non ho bisogno di acqua.")
                self.partiDialogo.append(dialogo)
        if self.tipo.startswith("OggettoScaffaleBicchieri"):
            self.partiDialogo = []
            self.nome = "OggettoScaffaleBicchieri"
            if avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialChiusuraPorte"]:
                self.oggettoDato = "Bicchiere"
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ecco un bicchiere, ora devo riempirlo d'acqua.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non mi servono altri bicchieri.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non ho bisogno di queste cose.")
                self.partiDialogo.append(dialogo)
        if self.tipo == "OggettoComodinoLucy":
            self.partiDialogo = []
            self.nome = "OggettoComodinoLucy"
            if avanzamentoStoria <= GlobalVar.dictAvanzamentoStoria["ottenutoBicchiereAcqua"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Questa è la roba di Lucy. C'è il suo diario e... un foglio arrotolato?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non importa, non prenderò queste cose.")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["dialogoCasaHansLucy2"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ho messo qua il bicchiere con l'acqua.")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
                self.oggettoDato = "Mappa e Diario"
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ok, mappa e diario presi.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non c'è nient'altro di importante da prendere qui.")
                self.partiDialogo.append(dialogo)
        if self.tipo == "OggettoComodinoHans":
            self.partiDialogo = []
            self.nome = "OggettoComodinoHans"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non tengo niente di utile qui.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È il comodino di Hans. Non c'è niente di interessante... solo una piccola lanterna.")
                self.partiDialogo.append(dialogo)
        if self.tipo.startswith("OggettoFinestra"):
            self.partiDialogo = []
            self.nome = "OggettoFinestra"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È notte fonda, devo partire adesso.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Hans stava guardando fuori dalla finestra quando mi sono svegliata... spero che sia ancora qua fuori e che ci stia ripensando.")
                self.partiDialogo.append(dialogo)
        if self.tipo == "OggettoLettoHans":
            self.partiDialogo = []
            self.nome = "OggettoLettoHans"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non posso rimettermi a dormire. Non voglio rimandare ancora, sono pronto.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È il letto di Hans e lui non c'è...")
                self.partiDialogo.append(dialogo)
        if self.tipo.startswith("OggettoVasca"):
            self.partiDialogo = []
            self.nome = "OggettoVasca"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È una specie di fontana che abbiamo fatto io e il babbo per poterci lavare senza dover uscire di casa.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"La parte più difficile e faticosa è stata senza dubbio costruire il canale per l'acqua... ma una volta fatto quello abbiamo potuto pensare di fare anche le altre fontanelle.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È la fontana che usiamo per lavarci. È molto comodo averla dentro casa.")
                self.partiDialogo.append(dialogo)
        if self.tipo.startswith("OggettoGabinetto"):
            self.partiDialogo = []
            self.nome = "OggettoGabinetto"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non ho bisogno di usare il gabinetto adesso.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non mi scappa la pipì!")
                self.partiDialogo.append(dialogo)
        if self.tipo.startswith("OggettoCamino"):
            self.partiDialogo = []
            self.nome = "OggettoCamino"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È un camino che usiamo per riscaldare la casa e cucinare.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È il camino che usiamo sempre io e la mamma per cucinare.")
                self.partiDialogo.append(dialogo)
        if self.tipo.startswith("OggettoScaffaleCucina"):
            self.partiDialogo = []
            self.nome = "OggettoScaffaleCucina"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["ottenutoBicchiere"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È lo scaffale dove conserviamo gli alimenti... niente bicchieri qui!")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È lo scaffale dove conserviamo gli alimenti.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non ho bisogno di cibo, non ho fame adesso.")
                self.partiDialogo.append(dialogo)
        if self.tipo == "OggettoTavolinoFiori":
            self.partiDialogo = []
            self.nome = "OggettoTavolinoFiori"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È un tavolino con dei fiori... lo hanno voluto mettere perchè sembrava uno spazio troppo vuoto.")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ci sono dei bellissimi fiori che sarebbero già morti se non ci fossi io ad innaffiarli.")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"]:
                self.oggettoDato = "Chiave ripostiglio"
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Sono i miei bellissimi fiori... ma...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ehi, sotto il vaso c'è una chiave!")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Sotto questo vaso era nascosta la chiave del ripostiglio... come ho fatto a non accorgermene per tutto questo tempo?")
                self.partiDialogo.append(dialogo)
        if self.tipo == "OggettoComodinoMamma":
            self.partiDialogo = []
            self.nome = "OggettoComodinoMamma"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È il comodino della mamma... niente di interessante.")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Niente, la chiave non è qui...")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non c'è niente di utile per me qui.")
                self.partiDialogo.append(dialogo)
        if self.tipo == "OggettoComodinoBabbo":
            self.partiDialogo = []
            self.nome = "OggettoComodinoBabbo"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È il comodino del babbo... niente di interessante qui, solo un po' di roba puzzolente.")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Avrei giurato che la chiave fosse qui... devo cercare in un posto più insolito.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non c'è niente di utile per me qui.")
                self.partiDialogo.append(dialogo)
        if self.tipo.startswith("OggettoLettoGenitori"):
            self.partiDialogo = []
            self.nome = "OggettoLettoGenitori"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Devo fare piano, non voglio svegliarli.")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non credo che tengano la chiave del ripostiglio nel letto!")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Stanno dormento profondamente, non devo fare rumore.")
                self.partiDialogo.append(dialogo)

        # casa Hans e Lucy esterno
        if self.tipo.startswith("OggettoCancellettoCasa"):
            self.partiDialogo = []
            self.nome = "OggettoCancellettoCasa"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non voglio andare nei campi adesso.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non credo che Hans sia andato nei campi a quest'ora.")
                self.partiDialogo.append(dialogo)
        if self.tipo == "CaneCasa":
            self.partiDialogo = []
            self.nome = "Agglomerato"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ciao Agglo, cosa stai cercando in questi cespugli?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Deve aver fiutato qualcosa...")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ehi Agglo, hai visto Hans andare da quella parte?")
                self.partiDialogo.append(dialogo)
        if self.tipo.startswith("OggettoCanaleCasa"):
            self.partiDialogo = []
            self.nome = "OggettoCanaleCasa"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È il canale che abbiamo costruito per portare l'acqua del fiume nelle fontane in casa.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Qua dentro scorre l'acqua del fiume!")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È stata un'idea geniale costruire questo tunnel: adesso possiamo utilizzare l'acqua direttamente in casa!")
                self.partiDialogo.append(dialogo)

        # foresta cadetta
        if self.tipo == "OggettoSiepe":
            self.partiDialogo = []
            self.nome = "OggettoSiepe"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and self.avanzamentoDialogo == 0:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                self.avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"C'è un cinghiale incastrato in questo cespuglio...?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Sta facendo degli strani lamenti e sta perdendo sangue. Cosa stava cercando di fare? Forse inseguiva qualcosa?...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Credo che mi attaccherebbe se lo liberassi, quindi... sono costretta a lasciarlo qui e sperare che riesca a cavarsela in qualche modo.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and self.avanzamentoDialogo == 1:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                self.avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Mi attaccherebbe se lo liberassi, quindi lo lascerò qui sperando che riesca farcela da solo.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                self.avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Questo cinghiale non è riuscito a liberarsi... almeno ha smesso di fare quegli strazianti lamenti...")
                self.partiDialogo.append(dialogo)
        if self.tipo == "OggettoFuoco":
            self.partiDialogo = []
            self.nome = "OggettoFuoco"
            if avanzamentoStoria <= GlobalVar.dictAvanzamentoStoria["quintaStanzaForestaCadetta"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sembra allestito per fare un piccolo falò.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Qui è dove Sam ha intezione di accendere il fuoco per la notte.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Questo falò è stato usato di recente...")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Probabilmente questo accampamento era stato allestito da quel soldato che ho trovato morto in questa foresta.")
                self.partiDialogo.append(dialogo)
        if self.tipo == "OggettoCibo":
            self.partiDialogo = []
            self.nome = "OggettoCibo"
            if avanzamentoStoria <= GlobalVar.dictAvanzamentoStoria["quintaStanzaForestaCadetta"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                self.avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È una tavoletta di legno con una tovaglietta sopra.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["trovatoLegna3"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                self.avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Presumo che Sam voglia mettere qua il cibo che raccoglierà.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                self.avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sam ha raccolto un bel po' di carne.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Mi domando cosa abbia cacciato... le ossa sembrano piccole ma molto robuste...")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["cadavereSamDepredato"] and self.avanzamentoDialogo == 0:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                self.avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Qua sopra c'è della carne fresca. Delle gocce di sangue stanno ancora colando per terra.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ma Hans non sa cacciare... che ci sia qualcun altro nel bosco?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok ok, calma! Starà sicuramente bene.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["cadavereSamDepredato"] and self.avanzamentoDialogo == 1:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                self.avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"C'è della carne su questa tavoletta e non è di Hans...")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                self.avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Credo che sia stato quel soldato ad essersi procurato questa carne.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                self.avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Qualche animale dev'essersi divorato tutto.")
                self.partiDialogo.append(dialogo)
        if self.tipo == "OggettoMucchioLegna":
            self.partiDialogo = []
            self.nome = "OggettoMucchioLegna"
            if avanzamentoStoria <= GlobalVar.dictAvanzamentoStoria["quintaStanzaForestaCadetta"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È un mucchietto di legna.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria <= GlobalVar.dictAvanzamentoStoria["trovatoLegna2"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non c'è ancora abbastanza legna per la notte.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Devo raccoglierne altra.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["trovatoLegna3"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok, ho raccolto abbastanza legna adesso.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È un mucchio di legna da bruciare.")
                self.partiDialogo.append(dialogo)
        if self.tipo == "FiglioUfficiale":
            self.partiDialogo = []
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["incontroFiglioUfficiale"]:
                self.nome = "Sconosciuto"
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ehm... salve...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Uh!?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Stai lontano ragazzo!")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("No, non voglio causarti problemi.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Fai parte dell'esercito cittadino, vero?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Il mio nome è Sam e sto affrontando l'ultima prova per diventare ufficiale dell'esercito cittadino. Non ti conviene provare a derubarmi ragazzo: di solito non mi batto al di fuori degli allenamenti, ma nel caso ti avverto che sono armato e ben addestrato!")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non voglio derubarti, se avessi voluto di certo non mi sarei fatto notare in questo modo!")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Mmh... Cosa ci fai in mezzo alla foresta disarmato a quest'ora?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sto cercando di attraversarla per arrivare alla città e... sono disarmato perché mi aspettavo meno pericoli... e comunque me la posso cavare lo stesso.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Mmh... certo. Senti ragazzo se mi aiuterai a finire di allestire l'accampamento, potrai passare qua la notte e continuare domani il tuo cammino.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non chiamarmi <*>#italic#ragazzo,<*> se stai affrontando questa prova vuol dire che hai più o meno la mia età!")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non è una questione di età <*>#italic#ragazzo<*> ma di esperienza!")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Se vuoi sopravvivere stanotte vai a raccogliere la legna che ho tagliato ad est di qui. Altrimenti, se vuoi andare da solo, procedi verso sud e troverai la città.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Va bene, va bene... vado a prendere la legna.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Allora fai in fretta, tra poco sarà molto più pericoloso! Nel frattempo io mi procurerò del cibo.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["legnaDepositata"]:
                self.nome = "Sam"
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Dove hai detto che posso trovare della legna?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ho già tagliato la legna ad est di qui, devi solo prenderla e metterla accanto al falò.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["legnaDepositata"]:
                self.nome = "Sam"
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ho portato tutta la legna che ho trovato.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Mmh... si, dovrebbe bastare.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Vieni, accendiamo il fuoco e organizziamo i turni per la notte.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["inizioUltimoDialogoHans"]:
                self.nome = "Sam"
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ehm... è buona questa carne... che cos'è?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("... cinghiale...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Cinghiale!?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Voglio dire il sapore è quello ma... queste ossa mi sembrano troppo piccole per un cinghiale!")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Mmh...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ehm ehm... da quanto sei in questa foresta?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Da cinque giorni.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("E quanto ci devi rimanere ancora?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"In totale la prova è di due settimane, quindi... altri nove giorni.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("E cosa succede se torni prima o se non torni affatto?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Beh... non supero la prova.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ah beh certo...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ma, scusa se te lo chiedo: tecnicamente non dovrebbe essere vietato l'aiuto di altre persone?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Mi è concesso sfruttare tutto ciò che mi viene messo a disposizione dalla natura... tu non ne fai parte ragazzo?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Mah... senz'altro <*>#italic#ragazzo<*>...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Mmh... e tu invece perché stai andando tutto solo verso la città?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non lo so... faccio il contadino da tutta la vita e mi ero un po' stufato... e poi... diciamo che vorrei usare il mio tempo per cose più interessanti di ...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Oh CAZZO, ATTENTO!!!")
                self.partiDialogo.append(dialogo)
        if self.tipo.startswith("OggettoLegna"):
            self.partiDialogo = []
            self.nome = "OggettoLegna"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["trovatoLegna1"] and self.avanzamentoDialogo == 0:
                self.oggettoDato = "Legna"
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                self.avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Credo che sia questa la legna tagliata da Sam... di sicuro non basterà per la notte.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Qui intorno ce ne dovrebbe essere dell'altra.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["trovatoLegna2"] and self.avanzamentoDialogo == 0:
                self.oggettoDato = "Legna"
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                self.avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ecco dell'altra legna! Ancora un po' e posso tornare indietro.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["trovatoLegna3"] and self.avanzamentoDialogo == 0:
                self.oggettoDato = "Legna"
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                self.avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ok, ho preso abbastanza legna. Adesso devo portarla all'accampamento.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                self.avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non c'è più legna da prendere qui.")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                self.avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ci sono dei bastoncini di legno per terra.")
                self.partiDialogo.append(dialogo)
        if self.tipo == "OggettoCinghiale":
            self.partiDialogo = []
            self.nome = "Cinghiale"
            self.oggettoDato = False
            self.avanzaStoria = True
            self.menuMercante = False
            self.scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("<*>#italic#GRUNT GRUNT!!!<*>")
            self.partiDialogo.append(dialogo)
        if self.tipo == "OggettoPersonaCadavereSam":
            self.partiDialogo = []
            self.nome = "Soldato"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["cinghialeUcciso"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Devo liberare la zona prima di occuparmi di lui.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["cinghialeUcciso"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Soldat...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ohh... cazzo...")
                self.partiDialogo.append(dialogo)
        if self.tipo == "OggettoTombaSam":
            self.partiDialogo = []
            self.nome = "OggettoTombaSam"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Credo che stesse cercando di scappare da quel cinghiale e...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("... forse stava cacciando... che sia stato lui ad allestire quell'accampamento?")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Qui è dove ho seppellito il figlio di David. Sulla lapide hanno inciso il suo nome: \"Sam\".")
                self.partiDialogo.append(dialogo)

    def spostati(self, x, y, rx, ry, listaNemici, caseviste):
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
