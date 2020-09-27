# -*- coding: utf-8 -*-

from GenericFuncA import *


class PersonaggioObj(object):

    def __init__(self, x, y, direzione, tipo, stanza, avanzamentoStoria, percorso, numeroMovimento=0):
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

        if self.tipo != "Tutorial" and self.tipo != "Nessuno":
            if self.tipo.startswith("Oggetto"):
                self.mantieniSempreASchermo = True
                self.caricaImgOggetto(avanzamentoStoria)
                self.aggiornaImgOggetto(avanzamentoStoria)
            else:
                self.mantieniSempreASchermo = False
                self.caricaImgPersonaggio()
                self.girati(direzione)

        self.aggiornaDialogo(avanzamentoStoria)

    def caricaImgOggetto(self, avanzamentoStoria):
        self.imgOggetto = []
        numImg = 1
        nomeImgDialogo = "Vuota"
        if self.tipo == "OggettoLettoSara":
            numImg = 1
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                nomeImgDialogo = "SaraDormienteDialogo"
            else:
                nomeImgDialogo = "Vuota"
        if self.tipo == "OggettoLavandinoCucina":
            numImg = 1
            nomeImgDialogo = "Vuota"
        if self.tipo == "OggettoLavandinoBagno":
            numImg = 1
            nomeImgDialogo = "Vuota"
        if self.tipo.startswith("OggettoScaffaleBicchieri"):
            numImg = 1
            nomeImgDialogo = "Vuota"
        if self.tipo == "OggettoComodinoSara":
            numImg = 3
            nomeImgDialogo = "Vuota"
        if self.tipo.startswith("OggettoFinestra"):
            numImg = 1
            nomeImgDialogo = "Vuota"
        if self.tipo == "OggettoLettoSam":
            numImg = 1
            nomeImgDialogo = "Vuota"
        if self.tipo.startswith("OggettoDoccia"):
            numImg = 1
            nomeImgDialogo = "Vuota"
        if self.tipo.startswith("OggettoGabinetto"):
            numImg = 1
            nomeImgDialogo = "Vuota"
        if self.tipo.startswith("OggettoCamino"):
            numImg = 1
            nomeImgDialogo = "Vuota"
        if self.tipo.startswith("OggettoScaffaleCucina"):
            numImg = 1
            nomeImgDialogo = "Vuota"
        i = 1
        while i <= numImg:
            img = GlobalVar.loadImage("Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Oggetti/" + self.tipo + str(i) + ".png", True)
            img = pygame.transform.smoothscale(img, (GlobalVar.gpx, GlobalVar.gpy))
            self.imgOggetto.append(img)
            i += 1
        imgDialogo = GlobalVar.loadImage("Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/Dialoghi/" + nomeImgDialogo + ".png", False)
        self.imgDialogo = pygame.transform.smoothscale(imgDialogo, (GlobalVar.gpx * 16, GlobalVar.gpy * 12))

    def aggiornaImgOggetto(self, avanzamentoStoria):
        numImgAttuale = 0
        if self.tipo == "OggettoComodinoSara":
            if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara2"]:
                numImgAttuale = 1
        self.imgAttuale = self.imgOggetto[numImgAttuale]
        self.imgW = self.imgAttuale
        self.imgA = self.imgAttuale
        self.imgS = self.imgAttuale
        self.imgD = self.imgAttuale

    def caricaImgPersonaggio(self):
        imgW = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "W.png", True)
        self.imgW = pygame.transform.smoothscale(imgW, (GlobalVar.gpx, GlobalVar.gpy))
        imgA = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "A.png", True)
        self.imgA = pygame.transform.smoothscale(imgA, (GlobalVar.gpx, GlobalVar.gpy))
        imgS = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "S.png", True)
        self.imgS = pygame.transform.smoothscale(imgS, (GlobalVar.gpx, GlobalVar.gpy))
        imgD = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "D.png", True)
        self.imgD = pygame.transform.smoothscale(imgD, (GlobalVar.gpx, GlobalVar.gpy))

        imgWMov1 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "WMov1.png", True)
        self.imgWMov1 = pygame.transform.smoothscale(imgWMov1, (GlobalVar.gpx, GlobalVar.gpy))
        imgWMov2 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "WMov2.png", True)
        self.imgWMov2 = pygame.transform.smoothscale(imgWMov2, (GlobalVar.gpx, GlobalVar.gpy))
        imgAMov1 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "AMov1.png", True)
        self.imgAMov1 = pygame.transform.smoothscale(imgAMov1, (GlobalVar.gpx, GlobalVar.gpy))
        imgAMov2 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "AMov2.png", True)
        self.imgAMov2 = pygame.transform.smoothscale(imgAMov2, (GlobalVar.gpx, GlobalVar.gpy))
        imgSMov1 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "SMov1.png", True)
        self.imgSMov1 = pygame.transform.smoothscale(imgSMov1, (GlobalVar.gpx, GlobalVar.gpy))
        imgSMov2 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "SMov2.png", True)
        self.imgSMov2 = pygame.transform.smoothscale(imgSMov2, (GlobalVar.gpx, GlobalVar.gpy))
        imgDMov1 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "DMov1.png", True)
        self.imgDMov1 = pygame.transform.smoothscale(imgDMov1, (GlobalVar.gpx, GlobalVar.gpy))
        imgDMov2 = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "DMov2.png", True)
        self.imgDMov2 = pygame.transform.smoothscale(imgDMov2, (GlobalVar.gpx, GlobalVar.gpy))

        imgDialogo = GlobalVar.loadImage("Immagini/Personaggi/" + self.tipo + "/" + self.tipo + "Dialogo.png", True)
        self.imgDialogo = pygame.transform.smoothscale(imgDialogo, (GlobalVar.gpx * 16, GlobalVar.gpy * 12))

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
            if avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["dialogoSognoSara1"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = True
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Per muoverti usa i tasti W, A, S e D della tastiera o clicca con il mouse sulla casella verso cui vuoi spostarti.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Muoviti verso il baule davanti a te e prova ad aprirlo utilizzando il tasto SPAZIO o cliccandoci sopra con il mouse.")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["aperturaPrimoCofanetto"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Hai trovato una pozione. Puoi usarla dal menu a cui puoi accedere premendo Esc o il tasto centrale del mouse.")
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
                dialogo.append(u"Davanti a te c'è un nemico!")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Per vedere le sue informazioni passa alla modalità interazione (premi il tasto E della tastiera o il tasto destro del mouse) e inquadralo.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Una volta inquadrato puoi selezionarlo e attaccarlo premendo SPAZIO o il tasto sinistro del mouse (dato che al momento non hai freccie, puoi attaccarlo solo da vicino).")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialBattaglia"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Fai attenzione a quel pipistrello: è velenoso e attacca a distanza!")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Se vuoi ingaggiarlo assicurati di poterlo attaccare a distanza prima che ti possa vedere.")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("In quel baule potrebbe esserci qualcosa che fa al caso tuo...")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara1"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"È possibile richiudere le porte che sono già state aperte utilizzando la modalità interazione.")
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
                dialogo.append("Oh cazzo! Dove sono adesso!?")
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
                dialogo.append("Dovrei aprire quel baule prima di andare...?")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialOggettiBattaglia"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ok, Sam dovrebbe essere passato di qua... credo...")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["dialogoSognoSara2"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Perché sono venuta qui...?")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara1"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and self.x == GlobalVar.gpx * 24 and self.y == GlobalVar.gpy * 3 and self.stanzaDiAppartenenza == GlobalVar.dictStanze["casaSamSara1"]:
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
                dialogo.append("... Non lo voglio sapere... basta che non mi faccia vedere")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara1"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara2"] and (self.x == GlobalVar.gpx * 16 or self.x == GlobalVar.gpx * 17) and self.y == GlobalVar.gpy * 16 and self.stanzaDiAppartenenza == GlobalVar.dictStanze["casaSamSara1"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Prima devo portare l'acqua a Sara, così si riaddormenterà di nuovo e non si accorgerà che sono uscito")
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

        # casa Sam e Sara
        if self.tipo == "OggettoLettoSara":
            self.partiDialogo = []
            self.nome = "Sara"
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
                dialogo.append(u"No, io stavo... stavo andando... ehm... non lo so, non importa. Perché sei sveglio?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Stavo andando in bagno, è tutto ok?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Si, si... mi porteresti un bicchiere d'acqua quando torni?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Si, ok")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Grazie")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara1"] <= avanzamentoStoria <= GlobalVar.dictAvanzamentoStoria["tutorialChiusuraPorte"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Yaaawn... Sto ancora aspettando la mia acqua")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Si, sto andando")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["OttenutoBicchiere"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Dai Sam... mi hai portato un bicchiere vuoto...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ah, lo volevi con l'acqua?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Mmh...")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["OttenutoBicchiereAcqua"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Sara...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Zzz...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Si è già addormentata... Posso partire adesso allora, prima che qualcun altro si svegli")
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
                dialogo.append("...")
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
                dialogo.append("Devo prendere un bicchiere prima")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["OttenutoBicchiere"]:
                self.oggettoDato = "Bicchiere con acqua"
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ok, ho riempito il bicchiere")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non ho più bisogno di acqua")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non ho bisogno di acqua")
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
                dialogo.append("Ecco un bicchiere, ora devo riempirlo d'acqua")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non mi servono altri bicchieri")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non ho bisogno di queste cose")
                self.partiDialogo.append(dialogo)
        if self.tipo == "OggettoComodinoSara":
            self.partiDialogo = []
            self.nome = "OggettoComodinoSara"
            if avanzamentoStoria <= GlobalVar.dictAvanzamentoStoria["OttenutoBicchiereAcqua"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Questa è la roba di Sara. C'è il suo diario e... un foglio arrotolato?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non importa, non prenderò queste cose")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara2"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ho messo qua il bicchiere con l'acqua")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non ho bisogno di altre cose")
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
                dialogo.append(u"È notte fonda, devo partire adesso")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Sam stava guardando fuori dalla finestra quando mi sono svegliata")
                self.partiDialogo.append(dialogo)
        if self.tipo == "OggettoLettoSam":
            self.partiDialogo = []
            self.nome = "OggettoLettoSam"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non posso rimettermi a dormire. Non voglio rimandare ancora, sono pronto")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È il letto di Sam e lui non c'è")
                self.partiDialogo.append(dialogo)
        if self.tipo.startswith("OggettoDoccia"):
            self.partiDialogo = []
            self.nome = "OggettoDoccia"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È una specie di fontana che abbiamo fatto io e il babbo per poterci lavare senza dover uscire di casa")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Noi non la trovavamo molto necessaria ma la mamma continuava a pensare che lo fosse soprattutto per lavare i panni. Così abbiamo deciso di fargli la sorpresa")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"La parte più difficile e faticosa è stata senza dubbio costruire il canale per l'acqua... ma una volta fatto quello abbiamo potuto pensare a fare anche le altre fontanelle")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È la fontana che usiamo per lavarci. È comodo averla dentro casa")
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
                dialogo.append("Non ho bisogno di usare il gabinetto adesso")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non mi scappa la pipì")
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
                dialogo.append(u"È un camino che usiamo per riscaldare la casa e cucinare")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Lo usiamo sempre io e la mamma per cucinare")
                self.partiDialogo.append(dialogo)
        if self.tipo.startswith("OggettoScaffaleCucina"):
            self.partiDialogo = []
            self.nome = "OggettoScaffaleCucina"
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["OttenutoBicchiere"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È lo scaffale dove conserviamo gli alimenti... niente bicchieri qui")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È lo scaffale dove conserviamo gli alimenti")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non ho bisogno di cibo, non ho fame")
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
                dialogo.append("Deve aver fiutato un gatto o uno scoiattolo...")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ehi Agglo, hai vito Sam andare da quella parte?")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("... Mmmh...")
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
