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

        self.oggettoDato = False
        self.avanzaStoria = False
        self.menuMercante = False
        self.scelta = False

        self.animaSpostamento = False
        self.animazioneFatta = False

        if self.tipo != "Tutorial" and self.tipo != "Nessuno":
            if self.tipo.startswith("Oggetto"):
                self.mantieniSempreASchermo = True
                self.caricaImgOggetto()
                self.aggiornaImgOggetto(avanzamentoStoria)
            else:
                self.mantieniSempreASchermo = False
                self.caricaImgPersonaggio()
                self.girati(direzione)

        self.aggiornaDialogo(avanzamentoStoria)

    def caricaImgOggetto(self):
        self.imgOggetto = []
        numImg = 0
        nomeImgDialogo = ""
        if self.tipo == "OggettoSaraDormiente":
            numImg = 1
            nomeImgDialogo = "OggettoSaraDormienteDialogo"
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
        i = 1
        while i <= numImg:
            img = GlobalVar.loadImage("Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/" + self.tipo + str(i) + ".png")
            img = pygame.transform.smoothscale(img, (GlobalVar.gpx, GlobalVar.gpy))
            self.imgOggetto.append(img)
            i += 1
        imgDialogo = GlobalVar.loadImage("Immagini/Scenari/Stanza" + str(self.stanzaDiAppartenenza) + "/" + nomeImgDialogo + ".png")
        self.imgDialogo = pygame.transform.smoothscale(imgDialogo, (GlobalVar.gpx * 12, GlobalVar.gpy * 9))

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
                self.avanzaStoria = True
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
                self.avanzaStoria = True
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
                self.avanzaStoria = False
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
                self.avanzaStoria = True
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
                dialogo.append(u"Mmh... è giusto...")
                dialogo.append("2+3? ... mi scusi signore ... 2+3? ...")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ho comprato tutto ciò che aveva il mercante")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
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
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Muoviti verso il baule davanti a te e prova ad aprirlo utilizzando il tasto SPAZIO o cliccandoci sopra con il")
                dialogo.append("mouse.")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["aperturaPrimoCofanetto"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Hai trovato una pozione. Puoi usarla dal menu a cui puoi accedere premendo Esc o il tasto centrale del mouse.")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Dal menu potrai anche accedere a \"Equipaggiamento\" dove potrai selezionare armi, protezioni e accessori da")
                dialogo.append("equipaggiarti.")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialUtilizzoOggetti"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Davanti a te c'è un nemico!")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Per vedere le sue informazioni passa alla modalità interazione (premi il tasto E della tastiera o il tasto")
                dialogo.append("destro del mouse) e inquadralo.")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Una volta inquadrato puoi selezionarlo e attaccarlo premendo SPAZIO o il tasto sinistro del mouse (dato che")
                dialogo.append("al momento non hai freccie, puoi attaccarlo solo da vicino).")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialBattaglia"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Fai attenzione a quel pipistrello: è velenoso e attacca a distanza!")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Se vuoi ingaggiarlo assicurati di poterlo attaccare a distanza prima che ti possa vedere.")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("In quel baule potrebbe esserci qualcosa che fa al caso tuo...")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara1"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"È possibile richiudere le porte che sono già state aperte utilizzando la modalità interazione.")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("...")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
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
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Mi sono persa... lo sapevo...")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialMovimento"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Dovrei aprire quel baule prima di andare...?")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialOggettiBattaglia"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ok, Sam dovrebbe essere passato di qua... credo...")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["dialogoSognoSara2"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Perché sono venuta qui...?")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara1"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and self.x == GlobalVar.gpx * 24 and self.y == GlobalVar.gpy * 3 and self.stanzaDiAppartenenza == GlobalVar.dictStanze["casaSamSara1"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non voglio farmi scoprire e se entro il babbo e la mamma si sveglieranno. O forse sono ancora svegli?")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("... Non lo voglio sapere... basta che non mi faccia vedere")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara1"] <= avanzamentoStoria <= GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara2"] and (self.x == GlobalVar.gpx * 16 or self.x == GlobalVar.gpx * 17) and self.y == GlobalVar.gpy * 16 and self.stanzaDiAppartenenza == GlobalVar.dictStanze["casaSamSara1"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Prima devo portare l'acqua a Sara, così si riaddormenterà di nuovo e non si accorgerà che sono uscito")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("...")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
        if self.tipo == "OggettoSaraDormiente":
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
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ehi, hai fatto un brutto sogno?")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No, io stavo... stavo andando... ehm... non lo so, non importa. Perché sei sveglio?")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Stavo andando in bagno, è tutto ok?")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Si, si... mi porteresti un bicchiere d'acqua quando torni?")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Si, ok")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Grazie")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara1"] <= avanzamentoStoria <= GlobalVar.dictAvanzamentoStoria["tutorialChiusuraPorte"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Yaaawn... Sto ancora aspettando la mia acqua")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Si, sto andando")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["OttenutoBicchiere"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Dai Sam... mi hai portato un bicchiere vuoto...")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ah, lo volevi con l'acqua?")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Mmh...")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["OttenutoBicchiereAcqua"]:
                self.oggettoDato = False
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Sara...")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Zzz...")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Si è già addormentata... Posso partire adesso allora, prima che qualcun altro si svegli")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria <= GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("Zzz...")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("...")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
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
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["OttenutoBicchiere"]:
                self.oggettoDato = "Bicchiere con acqua"
                self.avanzaStoria = True
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ok, ho riempito il bicchiere")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non ho più bisogno del lavandino")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non ho bisogno di lavarmi le mani")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
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
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non mi servono altri bicchieri")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non ho bisogno di queste cose")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
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
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non importa, non prenderò queste cose")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            elif GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara2"] <= avanzamentoStoria <= GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Ho messo qua il bicchiere con l'acqua")
                dialogo.append("")
                dialogo.append("")
                dialogo.append("")
                self.partiDialogo.append(dialogo)
            else:
                self.oggettoDato = False
                self.avanzaStoria = False
                self.menuMercante = False
                self.scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non ho bisogno di altre cose")
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
