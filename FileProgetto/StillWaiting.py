# -*- coding: utf-8 -*-

# import psutil
import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto
import Codice.GestioneMenu.MenuPrincipali as MenuPrincipali
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche
import Codice.GestioneGrafica.EnvPrint as EnvPrint
import Codice.GestioneGrafica.Animazioni as Animazioni
import Codice.GestioneNemiciPersonaggi.MovNemiciRob as MovNemiciRob
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.FunzioniGeneriche.UtilityOstacoliContenutoCofanetti as UtilityOstacoliContenutoCofanetti
import Codice.SettaggiLivelli.SetNemiciPersonaggiEventi as SetNemiciPersonaggiEventi
import Codice.SettaggiLivelli.SetOstacoliContenutoCofanetti as SetOstacoliContenutoCofanetti
import Codice.SettaggiLivelli.SetPosizioneAudioImpedimenti as SetPosizioneAudioImpedimenti


def gameloop():
    # p = psutil.Process()
    # maxMemoryUsage = 0
    caricaSalvataggio = False
    inizio = True
    gameover = False
    while True:

        # if p.memory_info().rss / 1000000.0 > maxMemoryUsage:
        #     maxMemoryUsage = p.memory_info().rss / 1000000.0
        #     print u"Max RAM usata: " + str(maxMemoryUsage) + " MB"

        if inizio:
            nonMostrarePersonaggio = False
            avanzaIlTurnoSenzaMuoverti = False
            aggiornaImgEquip = True
            turniDaSaltarePerDifesa = 0
            refreshSchermo = True
            impossibileAprirePorta = False
            canzone = False
            sottofondoAmbientale = False
            stanzaCambiata = False
            uscitoDaMenu = 0
            # rumore porte (dipende dalla stanza)
            rumoreAperturaPorte = 0
            rumoreChiusuraPorte = 0
            animaOggetto = [False, 0, 0]
            raffreddamento = False
            ricarica1 = False
            ricarica2 = False
            nemicoInquadrato = False
            spingiColco = False
            apriChiudiPorta = [False, 0, 0]
            apriCofanetto = [False, 0, 0]
            interagisciConPersonaggio = False
            oggettoRicevuto = False
            visualizzaMenuMercante = False
            stanzaVecchia = 0
            tesoro = -1
            apriocchio = False
            sposta = False
            bottoneDown = False
            startf = False
            aumentoliv = 0
            primopasso = True
            xesca = 0
            yesca = 0
            creaesca = False
            attacco = 0
            difesa = 0
            nx = 0
            ny = 0

            dati, tutteporte, tutticofanetti, listaNemiciTotali, vettoreEsche, vettoreDenaro, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco = MenuPrincipali.menu(caricaSalvataggio, gameover)
            print ("Salvataggio: " + str(GlobalGameVar.numSalvataggioCaricato))
            gameover = False
            # controlla se devi cambiare personaggio giocabile
            if dati[0] < GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
                personaggioDaUsare = "Lucy1"
                GenericFunc.cambiaProtagonista(personaggioDaUsare)
                personaggioUsato = personaggioDaUsare
            elif GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= dati[0] < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                personaggioDaUsare = "FratelloMaggiore"
                GenericFunc.cambiaProtagonista(personaggioDaUsare)
                personaggioUsato = personaggioDaUsare
            elif dati[0] < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
                personaggioDaUsare = "Lucy1"
                GenericFunc.cambiaProtagonista(personaggioDaUsare)
                personaggioUsato = personaggioDaUsare
            else:
                personaggioDaUsare = "Lucy2"
                GenericFunc.cambiaProtagonista(personaggioDaUsare)
                personaggioUsato = personaggioDaUsare
            caricaSalvataggio = False
            pers = GlobalImgVar.perss
            robot = GlobalImgVar.robos
            print (dati)

            # vettore porte -> porte[stanza, x, y, True/False, ...]
            porte = []
            # vettore cofanetti -> cofanetti[stanza, x, y, True/False, ...]
            cofanetti = []

            x = dati[2]
            y = dati[3]
            vx = x
            vy = y
            # 1->d , 2->a , 3->w , 4->s
            npers = dati[140]
            rx = dati[134]
            ry = dati[135]
            vrx = rx
            vry = ry
            chiamarob = dati[142]
            caselleAttaccabiliColco = []
            posizioneColcoAggiornamentoCaseAttac = [rx, ry]
            raffredda = dati[136]
            autoRic1 = dati[137]
            autoRic2 = dati[138]
            # 1->d , 2->a , 3->s , 4->w
            nrob = dati[141]
            mosseRimasteRob = dati[139]

            listaPersonaggi = []
            listaNemici = []

            carim = True
            cambiosta = True
            impossibileCliccarePulsanti = True

        # caricare gli oggetti
        if carim:
            # aggiorno le img del personaggio giocabile
            if dati[0] < GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
                personaggioDaUsare = "Lucy1"
            elif GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= dati[0] < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                personaggioDaUsare = "FratelloMaggiore"
            elif dati[0] < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
                personaggioDaUsare = "Lucy1"
            else:
                personaggioDaUsare = "Lucy2"
            if personaggioDaUsare != personaggioUsato:
                GenericFunc.cambiaProtagonista(personaggioDaUsare)
                personaggioUsato = personaggioDaUsare
                npers = 4

            if cambiosta:
                if not inizio:
                    FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False)

                stoppaMusica = SetPosizioneAudioImpedimenti.scriviNomeZona(dati[1], stanzaVecchia)

                canzoneCambiata = False
                sottofondoAmbientaleCambiato = False
                # mi posiziono e setto canzone, sottofondo ambientale e rumore porte
                x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, sottofondoAmbientaleCambiato, canzone, sottofondoAmbientale, bottoneDown = SetPosizioneAudioImpedimenti.settaPosizioneERumoriStanza(x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, sottofondoAmbientaleCambiato, dati[1], stanzaVecchia, canzone, sottofondoAmbientale, inizio, dati[0], bottoneDown)
                if not inizio:
                    vx = x
                    vy = y
                    if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"]:
                        rx = x
                        ry = y
                        vrx = x
                        vry = y
                        # npers: 1=d, 2=a, 3=w, 4=s
                        # nrob: 1=d, 2=a, 3=s, 4=w
                        if npers == 1:
                            nrob = 1
                        if npers == 2:
                            nrob = 2
                        if npers == 3:
                            nrob = 4
                        if npers == 4:
                            nrob = 3

                if canzoneCambiata or sottofondoAmbientaleCambiato:
                    i = GlobalHWVar.volumeCanzoni
                    j = GlobalHWVar.volumeEffetti
                    while i > 0 or j > 0:
                        if canzoneCambiata:
                            GlobalHWVar.canaleSoundCanzone.set_volume(i)
                        if sottofondoAmbientaleCambiato:
                            GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(j)
                        i -= GlobalHWVar.volumeCanzoni / 10
                        j -= GlobalHWVar.volumeEffetti / 10
                        pygame.time.wait(30)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    if canzoneCambiata:
                        GlobalHWVar.canaleSoundCanzone.stop()
                        if canzone and not stoppaMusica:
                            GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
                    if sottofondoAmbientaleCambiato:
                        GlobalHWVar.canaleSoundSottofondoAmbientale.stop()
                        if sottofondoAmbientale:
                            GlobalHWVar.canaleSoundSottofondoAmbientale.play(sottofondoAmbientale, -1)
                    i = 0
                    j = 0
                    while i < GlobalHWVar.volumeCanzoni or j < GlobalHWVar.volumeEffetti:
                        if canzoneCambiata:
                            GlobalHWVar.canaleSoundCanzone.set_volume(i)
                        if sottofondoAmbientaleCambiato:
                            GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(j)
                        i += GlobalHWVar.volumeCanzoni / 10
                        j += GlobalHWVar.volumeEffetti / 10
                        pygame.time.wait(30)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    if canzoneCambiata:
                        GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
                    if sottofondoAmbientaleCambiato:
                        GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti)

                # resetto obbiettivo Colco
                if not inizio:
                    ultimoObbiettivoColco = []
                    obbiettivoCasualeColco = False

                # carico nemici e personaggi nella stanza
                listaNemici, listaPersonaggi, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali, listaAvanzamentoDialoghi = SetNemiciPersonaggiEventi.caricaNemiciEPersonaggi(dati[0], dati[1], stanzaVecchia, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali, listaAvanzamentoDialoghi, listaPersonaggi)
                stanzaVecchia = dati[1]

                # stanza
                nomeStanza = SetPosizioneAudioImpedimenti.settaNomeStanza(dati[0], dati[1])
                imgSfondoStanza = CaricaFileProgetto.loadImage("Risorse/Immagini/Scenari/Stanza" + str(dati[1]) + "/" + nomeStanza + ".png", GlobalHWVar.gsx, GlobalHWVar.gsy, False, canale_alpha=False)
                casellaChiara = CaricaFileProgetto.loadImage("Risorse/Immagini/Scenari/CasellaChiara.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                casellaScura = CaricaFileProgetto.loadImage("Risorse/Immagini/Scenari/CasellaScura.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                casellaOscurata = CaricaFileProgetto.loadImage("Risorse/Immagini/Scenari/CasellaOscurata.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                portaVert = CaricaFileProgetto.loadImage("Risorse/Immagini/Scenari/Stanza" + str(dati[1]) + "/PortaVerticale.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                portaOriz = CaricaFileProgetto.loadImage("Risorse/Immagini/Scenari/Stanza" + str(dati[1]) + "/PortaOrizzontale.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)

                if not inizio:
                    mosseRimasteRob = 0
                nemicoInquadrato = False
                # fermare la camminata dopo il cambio stanza
                bottoneDown = False

                # carica i cofanetti nella stanza (svuoto e riempio il vettore)
                i = 0
                while i < len(cofanetti):
                    del cofanetti[i + 3]
                    del cofanetti[i + 2]
                    del cofanetti[i + 1]
                    del cofanetti[i]
                i = 0
                while i < len(tutticofanetti):
                    if tutticofanetti[i] == dati[1]:
                        cofanetti.append(tutticofanetti[i])
                        cofanetti.append(tutticofanetti[i + 1])
                        cofanetti.append(tutticofanetti[i + 2])
                        cofanetti.append(tutticofanetti[i + 3])
                    i = i + 4

                # carica le porte nella stanza (svuoto e riempio il vettore)
                i = 0
                while i < len(porte):
                    del porte[i + 3]
                    del porte[i + 2]
                    del porte[i + 1]
                    del porte[i]
                i = 0
                while i < len(tutteporte):
                    if tutteporte[i] == dati[1]:
                        porte.append(tutteporte[i])
                        porte.append(tutteporte[i + 1])
                        porte.append(tutteporte[i + 2])
                        porte.append(tutteporte[i + 3])
                    i += 4

                caseviste, casevisteDaRallo, casevisteEntrateIncluse, caselleNonVisibili, casellePercorribili = GenericFunc.creaTuttiIVettoriPerLeCaselleViste(x, y, rx, ry, dati[1], porte, cofanetti, dati[0])
                entrateStanza = SetOstacoliContenutoCofanetti.getEntrateStanze(dati[1], dati[0])

                GlobalHWVar.disegnaImmagineSuSchermo(imgSfondoStanza, (0, 0))

                schermoOriginale = GlobalHWVar.schermo.copy().convert()
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.nero)
                vettoreImgCaselle = []
                i = 0
                while i < len(caseviste):
                    vettoreImgCaselle.append(caseviste[i])
                    vettoreImgCaselle.append(caseviste[i + 1])
                    vettoreImgCaselle.append(schermoOriginale.subsurface(pygame.Rect(caseviste[i], caseviste[i + 1], GlobalHWVar.gpx, GlobalHWVar.gpy)).convert())
                    i += 3

                if not inizio:
                    # eliminare tutte le esche
                    vettoreEsche = []
                    # elimino tutti i sacchetti di denaro
                    vettoreDenaro = []

                if dati[1] in GlobalGameVar.vetStanzePacifiche:
                    dati[2] = x
                    dati[3] = y
                    dati[140] = npers
                    dati[134] = rx
                    dati[135] = ry
                    dati[141] = nrob
                    dati[142] = chiamarob
                    dati[139] = mosseRimasteRob
                    dati[136] = raffredda
                    dati[137] = autoRic1
                    dati[138] = autoRic2
                    GlobalGameVar.vetDatiSalvataggioGameOver = [dati[:], tutteporte[:], tutticofanetti[:], GenericFunc.copiaListaDiOggettiConImmagini(listaNemiciTotali, True), vettoreEsche[:], vettoreDenaro[:], stanzeGiaVisitate[:], GenericFunc.copiaListaDiOggettiConImmagini(listaPersonaggiTotali, False, dati[0]), listaAvanzamentoDialoghi[:], oggettiRimastiAHans[:], ultimoObbiettivoColco[:], GenericFunc.copiaNemico(obbiettivoCasualeColco)]

                stanzaCambiata = True
                impossibileCliccarePulsanti = True

            if aggiornaImgEquip:
                # arma
                armaw = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Spade/Spada%iw.png" % dati[6], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armawMov1 = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Spade/Spada%iwMov1.png" % dati[6], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armawMov2 = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Spade/Spada%iwMov2.png" % dati[6], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armaa = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Spade/Spada%ia.png" % dati[6], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armaaMov1 = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Spade/Spada%iaMov1.png" % dati[6], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armaaMov2 = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Spade/Spada%iaMov2.png" % dati[6], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armas = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Spade/Spada%is.png" % dati[6], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armasMov1 = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Spade/Spada%isMov1.png" % dati[6], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armasMov2 = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Spade/Spada%isMov2.png" % dati[6], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armad = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Spade/Spada%id.png" % dati[6], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armadMov1 = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Spade/Spada%idMov1.png" % dati[6], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armadMov2 = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Spade/Spada%idMov2.png" % dati[6], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armasAttacco = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Spade/Spada%isAttacco.png" % dati[6], GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
                armaaAttacco = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Spade/Spada%iaAttacco.png" % dati[6], GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
                armadAttacco = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Spade/Spada%idAttacco.png" % dati[6], GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
                armawAttacco = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Spade/Spada%iwAttacco.png" % dati[6], GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
                # arco
                arcow = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Archi/Arco%iw.png" % dati[128], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                arcoa = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Archi/Arco%ia.png" % dati[128], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                arcos = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Archi/Arco%is.png" % dati[128], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                arcod = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Archi/Arco%id.png" % dati[128], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                arcosAttacco = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Archi/Arco%isAttacco.png" % dati[128], GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
                arcoaAttacco = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Archi/Arco%iaAttacco.png" % dati[128], GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
                arcodAttacco = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Archi/Arco%idAttacco.png" % dati[128], GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
                arcowAttacco = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Archi/Arco%iwAttacco.png" % dati[128], GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
                # faretra
                faretraw = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Faretre/Faretra%iw.png" % dati[133], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                faretraa = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Faretre/Faretra%ia.png" % dati[133], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                faretras = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Faretre/Faretra%is.png" % dati[133], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                faretrad = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Faretre/Faretra%id.png" % dati[133], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                # armatura
                armaturaw = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Armature/Armatura%iw.png" % dati[8], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armaturaa = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Armature/Armatura%ia.png" % dati[8], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armaturas = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Armature/Armatura%is.png" % dati[8], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armaturad = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Armature/Armatura%id.png" % dati[8], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                # scudo
                scudow = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Scudi/Scudo%iw.png" % dati[7], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                scudoa = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Scudi/Scudo%ia.png" % dati[7], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                scudos = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Scudi/Scudo%is.png" % dati[7], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                scudod = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Scudi/Scudo%id.png" % dati[7], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                scudoDifesa = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Scudi/Scudo%iDifesa.png" % dati[7], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                # guanti
                guantiw = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Guanti/Guanti%iw.png" % dati[129], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                guantiwMov1 = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Guanti/Guanti%iwMov1.png" % dati[129], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                guantiwMov2 = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Guanti/Guanti%iwMov2.png" % dati[129], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                guantia = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Guanti/Guanti%ia.png" % dati[129], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                guantiaMov1 = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Guanti/Guanti%iaMov1.png" % dati[129], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                guantiaMov2 = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Guanti/Guanti%iaMov2.png" % dati[129], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                guantis = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Guanti/Guanti%is.png" % dati[129], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                guantisMov1 = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Guanti/Guanti%isMov1.png" % dati[129], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                guantisMov2 = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Guanti/Guanti%isMov2.png" % dati[129], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                guantid = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Guanti/Guanti%id.png" % dati[129], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                guantidMov1 = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Guanti/Guanti%idMov1.png" % dati[129], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                guantidMov2 = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Guanti/Guanti%idMov2.png" % dati[129], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                guantisAttacco = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Guanti/Guanti%isAttacco.png" % dati[129], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                guantiaAttacco = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Guanti/Guanti%iaAttacco.png" % dati[129], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                guantidAttacco = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Guanti/Guanti%idAttacco.png" % dati[129], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                guantiwAttacco = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Guanti/Guanti%iwAttacco.png" % dati[129], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                guantiDifesa = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Guanti/Guanti%iDifesa.png" % dati[129], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                # collana
                collanaw = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Collane/Collana%iw.png" % dati[130], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                collanaa = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Collane/Collana%ia.png" % dati[130], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                collanas = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Collane/Collana%is.png" % dati[130], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                collanad = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipLucy/Collane/Collana%id.png" % dati[130], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                # armatura robot
                armrobw = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipRobo/Batteria%iw.png" % dati[9], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armroba = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipRobo/Batteria%ia.png" % dati[9], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armrobs = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipRobo/Batteria%is.png" % dati[9], GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                armrobd = CaricaFileProgetto.loadImage("Risorse/Immagini/EquipRobo/Batteria%id.png" % dati[9], GlobalHWVar.gpx, GlobalHWVar.gpy, True)

            if npers == 3:
                pers = GlobalImgVar.persw
                arma = armaw
                armaMov1 = armawMov1
                armaMov2 = armawMov2
                armaAttacco = armawAttacco
                armatura = armaturaw
                scudo = scudow
                arco = arcow
                faretra = faretraw
                arcoAttacco = arcowAttacco
                guanti = guantiw
                guantiMov1 = guantiwMov1
                guantiMov2 = guantiwMov2
                guantiAttacco = guantiwAttacco
                collana = collanaw
            if npers == 2:
                pers = GlobalImgVar.persa
                arma = armaa
                armaMov1 = armaaMov1
                armaMov2 = armaaMov2
                armaAttacco = armaaAttacco
                armatura = armaturaa
                scudo = scudoa
                arco = arcoa
                faretra = faretraa
                arcoAttacco = arcoaAttacco
                guanti = guantia
                guantiMov1 = guantiaMov1
                guantiMov2 = guantiaMov2
                guantiAttacco = guantiaAttacco
                collana = collanaa
            if npers == 4:
                pers = GlobalImgVar.perss
                arma = armas
                armaMov1 = armasMov1
                armaMov2 = armasMov2
                armaAttacco = armasAttacco
                armatura = armaturas
                scudo = scudos
                arco = arcos
                faretra = faretras
                arcoAttacco = arcosAttacco
                guanti = guantis
                guantiMov1 = guantisMov1
                guantiMov2 = guantisMov2
                guantiAttacco = guantisAttacco
                collana = collanas
            if npers == 1:
                pers = GlobalImgVar.persd
                arma = armad
                armaMov1 = armadMov1
                armaMov2 = armadMov2
                armaAttacco = armadAttacco
                armatura = armaturad
                scudo = scudod
                arco = arcod
                faretra = faretrad
                arcoAttacco = arcodAttacco
                guanti = guantid
                guantiMov1 = guantidMov1
                guantiMov2 = guantidMov2
                guantiAttacco = guantidAttacco
                collana = collanad
            if nrob != 0:
                if nrob == 1:
                    robot = GlobalImgVar.robod
                    armrob = armrobd
                if nrob == 2:
                    robot = GlobalImgVar.roboa
                    armrob = armroba
                if nrob == 3:
                    robot = GlobalImgVar.robos
                    armrob = armrobs
                if nrob == 4:
                    robot = GlobalImgVar.robow
                    armrob = armrobw

            # aggiorno inCasellaVista di nemici e personaggi
            listaNemici, listaPersonaggi = GenericFunc.aggiornaInCasellaVistaDiNemiciEPersonaggi(caseviste, listaNemici, listaPersonaggi)
            # aggiorno il campo attaccabile di colco
            if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] and rx == GlobalHWVar.gsx and ry == GlobalHWVar.gsy:
                rx = x
                ry = y
                vrx = rx
                vry = ry
            if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"]:
                caselleAttaccabiliColco = GenericFunc.trovacasattaccabili(rx, ry, GlobalGameVar.vistaRobo * GlobalHWVar.gpx, caseviste)
                posizioneColcoAggiornamentoCaseAttac = [rx, ry]
            # faccio il primo aggiornamento delle caselle attaccabili dei nemici (lo faccio perché queste caselle non vengono aggiornate finché il nemico non si sposta almeno una volta)
            for nemico in listaNemici:
                if inizio:
                    nemico.settaObbiettivoDalSalvataggio(x, y, rx, ry, vettoreEsche, vettoreDenaro, listaNemici, listaPersonaggi, dati, caseviste)
                if nemico.vita > 0 and nemico.inCasellaVista:
                    nemico.aggiornaVista(x, y, rx, ry, dati, caseviste, True)

            # aggiorno dialoghi/img dei personaggi
            for personaggio in listaPersonaggi:
                personaggio.aggiornaDialogo(dati[0])
                if personaggio.tipo.startswith("Oggetto"):
                    imgAggiornata = personaggio.aggiornaImgOggetto(dati[0])
                    if imgAggiornata:
                        refreshSchermo = True

            caricaTutto = True
            cambiosta = False
            carim = False
            aggiornaImgEquip = False

        if inizio:
            if npers != 1 and npers != 2 and npers != 3 and npers != 4:
                arma = armas
                armaMov1 = armasMov1
                armaMov2 = armasMov2
                armaAttacco = armasAttacco
                armatura = armaturas
                scudo = scudos
                arco = arcos
                faretra = faretras
                arcoAttacco = arcosAttacco
                guanti = guantis
                guantiMov1 = guantisMov1
                guantiMov2 = guantisMov2
                guantiAttacco = guantisAttacco
                collana = collanas
            if nrob == 0:
                robot = GlobalImgVar.robos
                armrob = armrobs
            inizio = False

        inquadratoQualcosa = False
        xMouse, yMouse = pygame.mouse.get_pos()
        if GlobalHWVar.mouseVisibile:
            # controlle se il cursore è sul pers in basso a sinistra / nemico in alto a sinistra / telecolco / personaggio / porta / cofanetto / casella vista
            if GlobalHWVar.gsy // 18 * 17 <= yMouse <= GlobalHWVar.gsy and GlobalHWVar.gsx // 32 * 0 <= xMouse <= GlobalHWVar.gsx // 32 * 6:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "start"
            elif ((type(nemicoInquadrato) is str and nemicoInquadrato == "Colco") or (not nemicoInquadrato and dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"])) and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 0 <= xMouse <= GlobalHWVar.gsx // 32 * 4:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 0 <= xMouse <= GlobalHWVar.gsx // 32 * 1:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif nemicoInquadrato and not type(nemicoInquadrato) is str and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 0 <= xMouse <= GlobalHWVar.gsx // 32 * 3:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 1.5 and GlobalHWVar.gsx // 32 * 27.8 < xMouse <= GlobalHWVar.gsx // 32 * 30.2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "telecolco"
            else:
                if not inquadratoQualcosa:
                    i = 0
                    for personaggio in listaPersonaggi:
                        if personaggio.x <= xMouse <= personaggio.x + GlobalHWVar.gpx and personaggio.y <= yMouse <= personaggio.y + GlobalHWVar.gpy:
                            if (personaggio.x == x + GlobalHWVar.gpx and personaggio.y == y) or (personaggio.x == x - GlobalHWVar.gpx and personaggio.y == y) or (personaggio.x == x and personaggio.y == y + GlobalHWVar.gpy) or (personaggio.x == x and personaggio.y == y - GlobalHWVar.gpy):
                                if GlobalHWVar.mouseBloccato:
                                    GlobalHWVar.configuraCursore(False)
                                inquadratoQualcosa = "personaggio:" + str(i)
                            break
                        i += 1
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(porte):
                        if porte[i + 1] <= xMouse <= porte[i + 1] + GlobalHWVar.gpx and porte[i + 2] <= yMouse <= porte[i + 2] + GlobalHWVar.gpy and not porte[i + 3]:
                            if ((porte[i + 1] == x + GlobalHWVar.gpx and porte[i + 2] == y) or (porte[i + 1] == x - GlobalHWVar.gpx and porte[i + 2] == y) or (porte[i + 1] == x and porte[i + 2] == y + GlobalHWVar.gpy) or (porte[i + 1] == x and porte[i + 2] == y - GlobalHWVar.gpy)) and not porte[i + 3]:
                                if GlobalHWVar.mouseBloccato:
                                    GlobalHWVar.configuraCursore(False)
                                inquadratoQualcosa = "porta:" + str(i)
                            break
                        i += 4
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(cofanetti):
                        if cofanetti[i + 1] <= xMouse <= cofanetti[i + 1] + GlobalHWVar.gpx and cofanetti[i + 2] <= yMouse <= cofanetti[i + 2] + GlobalHWVar.gpy and not cofanetti[i + 3]:
                            if ((cofanetti[i + 1] == x + GlobalHWVar.gpx and cofanetti[i + 2] == y) or (cofanetti[i + 1] == x - GlobalHWVar.gpx and cofanetti[i + 2] == y) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y + GlobalHWVar.gpy) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y - GlobalHWVar.gpy)) and not cofanetti[i + 3]:
                                if GlobalHWVar.mouseBloccato:
                                    GlobalHWVar.configuraCursore(False)
                                inquadratoQualcosa = "cofanetto:" + str(i)
                            break
                        i += 4
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(casevisteEntrateIncluse):
                        if casevisteEntrateIncluse[i] <= xMouse <= casevisteEntrateIncluse[i] + GlobalHWVar.gpx and casevisteEntrateIncluse[i + 1] <= yMouse <= casevisteEntrateIncluse[i + 1] + GlobalHWVar.gpy:
                            if casevisteEntrateIncluse[i + 2]:
                                casellaOccupata = False
                                for personaggio in listaPersonaggi:
                                    if casevisteEntrateIncluse[i] == personaggio.x and casevisteEntrateIncluse[i + 1] == personaggio.y:
                                        casellaOccupata = True
                                        break
                                for nemico in listaNemici:
                                    if casevisteEntrateIncluse[i] == nemico.x and casevisteEntrateIncluse[i + 1] == nemico.y:
                                        casellaOccupata = True
                                        break
                                if not casellaOccupata:
                                    if GlobalHWVar.mouseBloccato:
                                        GlobalHWVar.configuraCursore(False)
                                    inquadratoQualcosa = "movimento:" + str(casevisteEntrateIncluse[i]) + ":" + str(casevisteEntrateIncluse[i + 1])
                            break
                        i += 3
        if not inquadratoQualcosa and GlobalHWVar.mouseVisibile:
            if not GlobalHWVar.mouseBloccato:
                GlobalHWVar.configuraCursore(True)

        # controllo se ci sono nemici in movimento per decidere se fare altre animazioni o no
        nemiciInMovimento = False
        for nemico in listaNemici:
            if nemico.mosseRimaste > 0:
                nemiciInMovimento = True
                break

        # gestione degli input
        if not impossibileCliccarePulsanti and not avanzaIlTurnoSenzaMuoverti and mosseRimasteRob <= 0 and not nemiciInMovimento and not startf and not oggettoRicevuto and turniDaSaltarePerDifesa == 0:
            bottoneDown, inutile = GestioneInput.getInput(bottoneDown, False)
        elif startf or oggettoRicevuto or impossibileCliccarePulsanti or avanzaIlTurnoSenzaMuoverti:
            bottoneDown = False
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        if not bottoneDown:
            GlobalHWVar.canaleSoundPassiRallo.stop()
            nx = 0
            ny = 0
        movimentoPerMouse = False
        if mosseRimasteRob <= 0 and not nemiciInMovimento:
            # movimenti personaggio
            if bottoneDown == pygame.K_w or bottoneDown == "padSu":
                refreshSchermo = True
                npers = 3
                pers = GlobalImgVar.persw
                arma = armaw
                armaMov1 = armawMov1
                armaMov2 = armawMov2
                armaAttacco = armawAttacco
                armatura = armaturaw
                scudo = scudow
                arco = arcow
                faretra = faretraw
                arcoAttacco = arcowAttacco
                guanti = guantiw
                guantiMov1 = guantiwMov1
                guantiMov2 = guantiwMov2
                guantiAttacco = guantiwAttacco
                collana = collanaw
                ny = -GlobalHWVar.gpy
                nx = 0
            if bottoneDown == pygame.K_a or bottoneDown == "padSinistra":
                refreshSchermo = True
                npers = 2
                pers = GlobalImgVar.persa
                arma = armaa
                armaMov1 = armaaMov1
                armaMov2 = armaaMov2
                armaAttacco = armaaAttacco
                armatura = armaturaa
                scudo = scudoa
                arco = arcoa
                faretra = faretraa
                arcoAttacco = arcoaAttacco
                guanti = guantia
                guantiMov1 = guantiaMov1
                guantiMov2 = guantiaMov2
                guantiAttacco = guantiaAttacco
                collana = collanaa
                nx = -GlobalHWVar.gpx
                ny = 0
            if bottoneDown == pygame.K_s or bottoneDown == "padGiu":
                refreshSchermo = True
                npers = 4
                pers = GlobalImgVar.perss
                arma = armas
                armaMov1 = armasMov1
                armaMov2 = armasMov2
                armaAttacco = armasAttacco
                armatura = armaturas
                scudo = scudos
                arco = arcos
                faretra = faretras
                arcoAttacco = arcosAttacco
                guanti = guantis
                guantiMov1 = guantisMov1
                guantiMov2 = guantisMov2
                guantiAttacco = guantisAttacco
                collana = collanas
                ny = GlobalHWVar.gpy
                nx = 0
            if bottoneDown == pygame.K_d or bottoneDown == "padDestra":
                refreshSchermo = True
                npers = 1
                pers = GlobalImgVar.persd
                arma = armad
                armaMov1 = armadMov1
                armaMov2 = armadMov2
                armaAttacco = armadAttacco
                armatura = armaturad
                scudo = scudod
                arco = arcod
                faretra = faretrad
                arcoAttacco = arcodAttacco
                guanti = guantid
                guantiMov1 = guantidMov1
                guantiMov2 = guantidMov2
                guantiAttacco = guantidAttacco
                collana = collanad
                nx = GlobalHWVar.gpx
                ny = 0
            # vado in mod. interazione
            if bottoneDown == pygame.K_e or bottoneDown == "padQuadrato":
                GlobalHWVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                attacco = 1
                bottoneDown = False
            # tolgo l'obbiettivo se presente
            if bottoneDown == pygame.K_q or bottoneDown == "padCerchio":
                GlobalHWVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                if nemicoInquadrato:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    nemicoInquadrato = False
                    caricaTutto = True
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                bottoneDown = False
            # attivo / disattivo gambit di Colco
            if bottoneDown == pygame.K_LSHIFT or bottoneDown == pygame.K_RSHIFT or bottoneDown == "padTriangolo":
                GlobalHWVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"]:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoTeleColco)
                    refreshSchermo = True
                    if chiamarob:
                        chiamarob = False
                    else:
                        ultimoObbiettivoColco = []
                        ultimoObbiettivoColco.append("Telecomando")
                        ultimoObbiettivoColco.append(x)
                        ultimoObbiettivoColco.append(y)
                        chiamarob = True
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                bottoneDown = False
            # scorro la selezione dell'obbiettivo
            if bottoneDown == pygame.K_3 or bottoneDown == pygame.K_KP3 or bottoneDown == "padR1":
                GlobalHWVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                listaNemiciVisti = []
                for nemico in listaNemici:
                    if nemico.inCasellaVista:
                        listaNemiciVisti.append(nemico)
                listaEscheViste = []
                i = 0
                while i < len(vettoreEsche):
                    j = 0
                    while j < len(caseviste):
                        if caseviste[j] == vettoreEsche[i + 2] and caseviste[j + 1] == vettoreEsche[i + 3] and caseviste[j + 2]:
                            listaEscheViste.append(vettoreEsche[i])
                            listaEscheViste.append(vettoreEsche[i + 1])
                            listaEscheViste.append(vettoreEsche[i + 2])
                            listaEscheViste.append(vettoreEsche[i + 3])
                        j += 3
                    i += 4
                nemicoInquadrato = GenericFunc.scorriObbiettiviInquadrati(dati[0], nemicoInquadrato, listaNemiciVisti, listaEscheViste, True)
                caricaTutto = True
                bottoneDown = False
            if bottoneDown == pygame.K_2 or bottoneDown == pygame.K_KP2 or bottoneDown == "padL1":
                GlobalHWVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                listaNemiciVisti = []
                for nemico in listaNemici:
                    if nemico.inCasellaVista:
                        listaNemiciVisti.append(nemico)
                listaEscheViste = []
                i = 0
                while i < len(vettoreEsche):
                    j = 0
                    while j < len(caseviste):
                        if caseviste[j] == vettoreEsche[i + 2] and caseviste[j + 1] == vettoreEsche[i + 3] and caseviste[j + 2]:
                            listaEscheViste.append(vettoreEsche[i])
                            listaEscheViste.append(vettoreEsche[i + 1])
                            listaEscheViste.append(vettoreEsche[i + 2])
                            listaEscheViste.append(vettoreEsche[i + 3])
                        j += 3
                    i += 4
                nemicoInquadrato = GenericFunc.scorriObbiettiviInquadrati(dati[0], nemicoInquadrato, listaNemiciVisti, listaEscheViste, False)
                caricaTutto = True
                bottoneDown = False
            # interagisco
            if bottoneDown == pygame.K_SPACE or bottoneDown == "padCroce":
                GlobalHWVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                # apertura porte
                k = 0
                while k < len(porte):
                    if porte[k] == dati[1] and not porte[k + 3] and ((porte[k + 1] == x + GlobalHWVar.gpx and porte[k + 2] == y and npers == 1) or (porte[k + 1] == x - GlobalHWVar.gpx and porte[k + 2] == y and npers == 2) or (porte[k + 1] == x and porte[k + 2] == y + GlobalHWVar.gpy and npers == 4) or (porte[k + 1] == x and porte[k + 2] == y - GlobalHWVar.gpy and npers == 3)):
                        if SetPosizioneAudioImpedimenti.possibileAprirePorta(dati[1], porte[k + 1], porte[k + 2], dati[0]):
                            sposta = True
                            GlobalHWVar.canaleSoundInterazioni.play(rumoreAperturaPorte)
                            porte[k + 3] = True
                            caseviste, casevisteDaRallo, casevisteEntrateIncluse, caselleNonVisibili, casellePercorribili = GenericFunc.creaTuttiIVettoriPerLeCaselleViste(x, y, rx, ry, dati[1], porte, cofanetti, dati[0])
                            caricaTutto = True
                            # aggiornare vettore tutteporte
                            j = 0
                            while j < len(tutteporte):
                                if tutteporte[j] == porte[k] and tutteporte[j + 1] == porte[k + 1] and tutteporte[j + 2] == porte[k + 2]:
                                    tutteporte[j + 3] = True
                                    break
                                j = j + 4
                            # aggiorno inCasellaVista di nemici e personaggi
                            listaNemici, listaPersonaggi = GenericFunc.aggiornaInCasellaVistaDiNemiciEPersonaggi(caseviste, listaNemici, listaPersonaggi)
                            # aggiorno il campo attaccabile di colco
                            if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"]:
                                caselleAttaccabiliColco = GenericFunc.trovacasattaccabili(rx, ry, GlobalGameVar.vistaRobo * GlobalHWVar.gpx, caseviste)
                                posizioneColcoAggiornamentoCaseAttac = [rx, ry]
                            # aggiorno la vista dei nemici
                            for nemico in listaNemici:
                                if nemico.vita > 0 and nemico.inCasellaVista:
                                    nemico.aggiornaVista(x, y, rx, ry, dati, caseviste, True)
                        else:
                            caricaTutto = True
                            impossibileAprirePorta = True
                        break
                    k = k + 4
                # apertura cofanetti
                i = 0
                while i < len(cofanetti):
                    if cofanetti[i] == dati[1] and (
                            (cofanetti[i + 1] == x + GlobalHWVar.gpx and cofanetti[i + 2] == y and npers == 1) or (
                            cofanetti[i + 1] == x - GlobalHWVar.gpx and cofanetti[i + 2] == y and npers == 2) or (
                                    cofanetti[i + 1] == x and cofanetti[i + 2] == y + GlobalHWVar.gpy and npers == 4) or (
                                    cofanetti[i + 1] == x and cofanetti[i + 2] == y - GlobalHWVar.gpy and npers == 3)) and not \
                    cofanetti[i + 3]:
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoaperturacofanetti)
                        sposta = True
                        dati, tesoro, dati[0] = SetOstacoliContenutoCofanetti.aperturacofanetto(cofanetti[i], cofanetti[i + 1], cofanetti[i + 2], dati)
                        if tesoro == -2 or tesoro == -1 or tesoro > 0:
                            cofanetti[i + 3] = True
                        caricaTutto = True
                        # aggiornare vettore tutticofanetti
                        j = 0
                        while j < len(tutticofanetti):
                            if tutticofanetti[j] == cofanetti[i] and tutticofanetti[j + 1] == cofanetti[i + 1] and tutticofanetti[j + 2] == cofanetti[i + 2]:
                                if tesoro == -2 or tesoro == -1 or tesoro > 0:
                                    tutticofanetti[j + 3] = True
                            j = j + 4
                    i = i + 4
                # interazioni con altri personaggi
                for personaggio in listaPersonaggi:
                    if (personaggio.x == x + GlobalHWVar.gpx and personaggio.y == y and npers == 1) or (personaggio.x == x - GlobalHWVar.gpx and personaggio.y == y and npers == 2) or (personaggio.x == x and personaggio.y == y + GlobalHWVar.gpy and npers == 4) or (personaggio.x == x and personaggio.y == y - GlobalHWVar.gpy and npers == 3):
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        sposta = True
                        if npers == 1:
                            personaggio.girati("a")
                        elif npers == 2:
                            personaggio.girati("d")
                        elif npers == 3:
                            personaggio.girati("s")
                        elif npers == 4:
                            personaggio.girati("w")
                        EnvPrint.disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, casellaChiara, casellaScura, casellaOscurata, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, entrateStanza, caselleNonVisibili, dati[0], nonMostrarePersonaggio)
                        dati[0], oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(dati[0], personaggio, listaAvanzamentoDialoghi)
                        caricaTutto = True
                if not sposta:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                bottoneDown = False
            # apro il menu
            if bottoneDown == pygame.K_ESCAPE or bottoneDown == "mouseCentrale" or bottoneDown == "padStart":
                GlobalHWVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                startf = True
                bottoneDown = False
            # comandi mouse
            if bottoneDown == "mouseDestro":
                GlobalHWVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                if inquadratoQualcosa == "battaglia" and nemicoInquadrato:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    nemicoInquadrato = False
                    caricaTutto = True
                else:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                    attacco = 1
                bottoneDown = False
            if bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato:
                if inquadratoQualcosa == "start":
                    GlobalHWVar.canaleSoundPassiRallo.stop()
                    nx = 0
                    ny = 0
                    startf = True
                    bottoneDown = False
                elif inquadratoQualcosa == "battaglia":
                    GlobalHWVar.canaleSoundPassiRallo.stop()
                    nx = 0
                    ny = 0
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                    attacco = 1
                    bottoneDown = False
                elif inquadratoQualcosa == "telecolco":
                    GlobalHWVar.canaleSoundPassiRallo.stop()
                    nx = 0
                    ny = 0
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoTeleColco)
                    refreshSchermo = True
                    if chiamarob:
                        chiamarob = False
                    else:
                        ultimoObbiettivoColco = []
                        ultimoObbiettivoColco.append("Telecomando")
                        ultimoObbiettivoColco.append(x)
                        ultimoObbiettivoColco.append(y)
                        chiamarob = True
                    bottoneDown = False
                elif inquadratoQualcosa and inquadratoQualcosa.startswith("porta"):
                    GlobalHWVar.canaleSoundPassiRallo.stop()
                    nx = 0
                    ny = 0
                    inquadratoQualcosaList = inquadratoQualcosa.split(":")
                    posizPortaInVettore = int(inquadratoQualcosaList[1])
                    if SetPosizioneAudioImpedimenti.possibileAprirePorta(dati[1], porte[posizPortaInVettore + 1], porte[posizPortaInVettore + 2], dati[0]):
                        sposta = True
                        GlobalHWVar.canaleSoundInterazioni.play(rumoreAperturaPorte)
                        porte[posizPortaInVettore + 3] = True
                        caseviste, casevisteDaRallo, casevisteEntrateIncluse, caselleNonVisibili, casellePercorribili = GenericFunc.creaTuttiIVettoriPerLeCaselleViste(x, y, rx, ry, dati[1], porte, cofanetti, dati[0])
                        caricaTutto = True
                        # aggiornare vettore tutteporte
                        j = 0
                        while j < len(tutteporte):
                            if tutteporte[j] == porte[posizPortaInVettore] and tutteporte[j + 1] == porte[posizPortaInVettore + 1] and tutteporte[j + 2] == porte[posizPortaInVettore + 2]:
                                tutteporte[j + 3] = True
                                break
                            j += 4
                        # aggiorno inCasellaVista di nemici e personaggi
                        listaNemici, listaPersonaggi = GenericFunc.aggiornaInCasellaVistaDiNemiciEPersonaggi(caseviste, listaNemici, listaPersonaggi)
                        # aggiorno il campo attaccabile di colco
                        if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"]:
                            caselleAttaccabiliColco = GenericFunc.trovacasattaccabili(rx, ry, GlobalGameVar.vistaRobo * GlobalHWVar.gpx, caseviste)
                            posizioneColcoAggiornamentoCaseAttac = [rx, ry]
                        # aggiorno la vista dei nemici
                        for nemico in listaNemici:
                            if nemico.vita > 0 and nemico.inCasellaVista:
                                nemico.aggiornaVista(x, y, rx, ry, dati, caseviste, True)
                    else:
                        impossibileAprirePorta = True
                        caricaTutto = True
                    # giro il pers verso la porta
                    if porte[posizPortaInVettore + 1] == x + GlobalHWVar.gpx and porte[posizPortaInVettore + 2] == y:
                        npers = 1
                    if porte[posizPortaInVettore + 1] == x - GlobalHWVar.gpx and porte[posizPortaInVettore + 2] == y:
                        npers = 2
                    if porte[posizPortaInVettore + 1] == x and porte[posizPortaInVettore + 2] == y + GlobalHWVar.gpy:
                        npers = 4
                    if porte[posizPortaInVettore + 1] == x and porte[posizPortaInVettore + 2] == y - GlobalHWVar.gpy:
                        npers = 3
                    if npers == 3:
                        pers = GlobalImgVar.persw
                        arma = armaw
                        armaMov1 = armawMov1
                        armaMov2 = armawMov2
                        armaAttacco = armawAttacco
                        armatura = armaturaw
                        scudo = scudow
                        arco = arcow
                        faretra = faretraw
                        arcoAttacco = arcowAttacco
                        guanti = guantiw
                        guantiMov1 = guantiwMov1
                        guantiMov2 = guantiwMov2
                        guantiAttacco = guantiwAttacco
                        collana = collanaw
                    if npers == 2:
                        pers = GlobalImgVar.persa
                        arma = armaa
                        armaMov1 = armaaMov1
                        armaMov2 = armaaMov2
                        armaAttacco = armaaAttacco
                        armatura = armaturaa
                        scudo = scudoa
                        arco = arcoa
                        faretra = faretraa
                        arcoAttacco = arcoaAttacco
                        guanti = guantia
                        guantiMov1 = guantiaMov1
                        guantiMov2 = guantiaMov2
                        guantiAttacco = guantiaAttacco
                        collana = collanaa
                    if npers == 4:
                        pers = GlobalImgVar.perss
                        arma = armas
                        armaMov1 = armasMov1
                        armaMov2 = armasMov2
                        armaAttacco = armasAttacco
                        armatura = armaturas
                        scudo = scudos
                        arco = arcos
                        faretra = faretras
                        arcoAttacco = arcosAttacco
                        guanti = guantis
                        guantiMov1 = guantisMov1
                        guantiMov2 = guantisMov2
                        guantiAttacco = guantisAttacco
                        collana = collanas
                    if npers == 1:
                        pers = GlobalImgVar.persd
                        arma = armad
                        armaMov1 = armadMov1
                        armaMov2 = armadMov2
                        armaAttacco = armadAttacco
                        armatura = armaturad
                        scudo = scudod
                        arco = arcod
                        faretra = faretrad
                        arcoAttacco = arcodAttacco
                        guanti = guantid
                        guantiMov1 = guantidMov1
                        guantiMov2 = guantidMov2
                        guantiAttacco = guantidAttacco
                        collana = collanad
                elif inquadratoQualcosa and inquadratoQualcosa.startswith("cofanetto"):
                    GlobalHWVar.canaleSoundPassiRallo.stop()
                    nx = 0
                    ny = 0
                    inquadratoQualcosaList = inquadratoQualcosa.split(":")
                    posizCofanettoInVettore = int(inquadratoQualcosaList[1])
                    sposta = True
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoaperturacofanetti)
                    dati, tesoro, dati[0] = SetOstacoliContenutoCofanetti.aperturacofanetto(cofanetti[posizCofanettoInVettore], cofanetti[posizCofanettoInVettore + 1], cofanetti[posizCofanettoInVettore + 2], dati)
                    if tesoro == -2 or tesoro == -1 or tesoro > 0:
                        cofanetti[posizCofanettoInVettore + 3] = True
                    caricaTutto = True
                    # aggiornare vettore tutticofanetti
                    j = 0
                    while j < len(tutticofanetti):
                        if tutticofanetti[j] == cofanetti[posizCofanettoInVettore] and tutticofanetti[j + 1] == cofanetti[posizCofanettoInVettore + 1] and tutticofanetti[j + 2] == cofanetti[posizCofanettoInVettore + 2]:
                            if tesoro == -2 or tesoro == -1 or tesoro > 0:
                                tutticofanetti[j + 3] = True
                        j += 4
                    # giro il pers verso il cofanetto
                    if cofanetti[posizCofanettoInVettore + 1] == x + GlobalHWVar.gpx and cofanetti[posizCofanettoInVettore + 2] == y:
                        npers = 1
                    if cofanetti[posizCofanettoInVettore + 1] == x - GlobalHWVar.gpx and cofanetti[posizCofanettoInVettore + 2] == y:
                        npers = 2
                    if cofanetti[posizCofanettoInVettore + 1] == x and cofanetti[posizCofanettoInVettore + 2] == y + GlobalHWVar.gpy:
                        npers = 4
                    if cofanetti[posizCofanettoInVettore + 1] == x and cofanetti[posizCofanettoInVettore + 2] == y - GlobalHWVar.gpy:
                        npers = 3
                    if npers == 3:
                        pers = GlobalImgVar.persw
                        arma = armaw
                        armaMov1 = armawMov1
                        armaMov2 = armawMov2
                        armaAttacco = armawAttacco
                        armatura = armaturaw
                        scudo = scudow
                        arco = arcow
                        faretra = faretraw
                        arcoAttacco = arcowAttacco
                        guanti = guantiw
                        guantiMov1 = guantiwMov1
                        guantiMov2 = guantiwMov2
                        guantiAttacco = guantiwAttacco
                        collana = collanaw
                    if npers == 2:
                        pers = GlobalImgVar.persa
                        arma = armaa
                        armaMov1 = armaaMov1
                        armaMov2 = armaaMov2
                        armaAttacco = armaaAttacco
                        armatura = armaturaa
                        scudo = scudoa
                        arco = arcoa
                        faretra = faretraa
                        arcoAttacco = arcoaAttacco
                        guanti = guantia
                        guantiMov1 = guantiaMov1
                        guantiMov2 = guantiaMov2
                        guantiAttacco = guantiaAttacco
                        collana = collanaa
                    if npers == 4:
                        pers = GlobalImgVar.perss
                        arma = armas
                        armaMov1 = armasMov1
                        armaMov2 = armasMov2
                        armaAttacco = armasAttacco
                        armatura = armaturas
                        scudo = scudos
                        arco = arcos
                        faretra = faretras
                        arcoAttacco = arcosAttacco
                        guanti = guantis
                        guantiMov1 = guantisMov1
                        guantiMov2 = guantisMov2
                        guantiAttacco = guantisAttacco
                        collana = collanas
                    if npers == 1:
                        pers = GlobalImgVar.persd
                        arma = armad
                        armaMov1 = armadMov1
                        armaMov2 = armadMov2
                        armaAttacco = armadAttacco
                        armatura = armaturad
                        scudo = scudod
                        arco = arcod
                        faretra = faretrad
                        arcoAttacco = arcodAttacco
                        guanti = guantid
                        guantiMov1 = guantidMov1
                        guantiMov2 = guantidMov2
                        guantiAttacco = guantidAttacco
                        collana = collanad
                    bottoneDown = False
                elif inquadratoQualcosa and inquadratoQualcosa.startswith("personaggio"):
                    GlobalHWVar.canaleSoundPassiRallo.stop()
                    nx = 0
                    ny = 0
                    inquadratoQualcosaList = inquadratoQualcosa.split(":")
                    posizPersonaggioInVettore = int(inquadratoQualcosaList[1])
                    personaggio = listaPersonaggi[posizPersonaggioInVettore]
                    sposta = True
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    # giro Rallo verso il personaggio e viceversa
                    if personaggio.x == x + GlobalHWVar.gpx and personaggio.y == y:
                        npers = 1
                    if personaggio.x == x - GlobalHWVar.gpx and personaggio.y == y:
                        npers = 2
                    if personaggio.x == x and personaggio.y == y + GlobalHWVar.gpy:
                        npers = 4
                    if personaggio.x == x and personaggio.y == y - GlobalHWVar.gpy:
                        npers = 3
                    if npers == 3:
                        pers = GlobalImgVar.persw
                        arma = armaw
                        armaMov1 = armawMov1
                        armaMov2 = armawMov2
                        armaAttacco = armawAttacco
                        armatura = armaturaw
                        scudo = scudow
                        arco = arcow
                        faretra = faretraw
                        arcoAttacco = arcowAttacco
                        guanti = guantiw
                        guantiMov1 = guantiwMov1
                        guantiMov2 = guantiwMov2
                        guantiAttacco = guantiwAttacco
                        collana = collanaw
                    if npers == 2:
                        pers = GlobalImgVar.persa
                        arma = armaa
                        armaMov1 = armaaMov1
                        armaMov2 = armaaMov2
                        armaAttacco = armaaAttacco
                        armatura = armaturaa
                        scudo = scudoa
                        arco = arcoa
                        faretra = faretraa
                        arcoAttacco = arcoaAttacco
                        guanti = guantia
                        guantiMov1 = guantiaMov1
                        guantiMov2 = guantiaMov2
                        guantiAttacco = guantiaAttacco
                        collana = collanaa
                    if npers == 4:
                        pers = GlobalImgVar.perss
                        arma = armas
                        armaMov1 = armasMov1
                        armaMov2 = armasMov2
                        armaAttacco = armasAttacco
                        armatura = armaturas
                        scudo = scudos
                        arco = arcos
                        faretra = faretras
                        arcoAttacco = arcosAttacco
                        guanti = guantis
                        guantiMov1 = guantisMov1
                        guantiMov2 = guantisMov2
                        guantiAttacco = guantisAttacco
                        collana = collanas
                    if npers == 1:
                        pers = GlobalImgVar.persd
                        arma = armad
                        armaMov1 = armadMov1
                        armaMov2 = armadMov2
                        armaAttacco = armadAttacco
                        armatura = armaturad
                        scudo = scudod
                        arco = arcod
                        faretra = faretrad
                        arcoAttacco = arcodAttacco
                        guanti = guantid
                        guantiMov1 = guantidMov1
                        guantiMov2 = guantidMov2
                        guantiAttacco = guantidAttacco
                        collana = collanad
                    if npers == 1:
                        personaggio.girati("a")
                    elif npers == 2:
                        personaggio.girati("d")
                    elif npers == 3:
                        personaggio.girati("s")
                    elif npers == 4:
                        personaggio.girati("w")
                    EnvPrint.disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, casellaChiara, casellaScura, casellaOscurata, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, entrateStanza, caselleNonVisibili, dati[0], nonMostrarePersonaggio)
                    dati[0], oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(dati[0], personaggio, listaAvanzamentoDialoghi)
                    caricaTutto = True
                    bottoneDown = False
                elif inquadratoQualcosa and inquadratoQualcosa.startswith("movimento"):
                    movimentoPerMouse = True
            elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
                GlobalHWVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                bottoneDown = False

        impossibileCliccarePulsanti = False
        if avanzaIlTurnoSenzaMuoverti:
            sposta = True
        avanzaIlTurnoSenzaMuoverti = False
        # statistiche personaggio e robo
        esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati, difesa)

        # resetta stati/pv al campio personaggio
        if dati[0] == GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] or dati[0] == GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            dati[5] = pvtot
            dati[121] = False

        # ripristina vita e status dopo lv up
        if aumentoliv != 0:
            dati[5] = pvtot
            dati[121] = False
            aumentoliv = 0

        if inquadratoQualcosa and inquadratoQualcosa.startswith("movimento") and movimentoPerMouse and mosseRimasteRob <= 0 and not nemiciInMovimento and not startf:
            nx = 0
            ny = 0
            vetNemiciSoloConXeY = []
            for nemico in listaNemici:
                vetNemiciSoloConXeY.append(nemico.x)
                vetNemiciSoloConXeY.append(nemico.y)
            for personaggio in listaPersonaggi:
                vetNemiciSoloConXeY.append(personaggio.x)
                vetNemiciSoloConXeY.append(personaggio.y)
            inquadratoQualcosaList = inquadratoQualcosa.split(":")
            xObbiettivo = int(inquadratoQualcosaList[1])
            yObbiettivo = int(inquadratoQualcosaList[2])
            bloccato = False
            i = 0
            while i < len(vetNemiciSoloConXeY):
                if xObbiettivo == vetNemiciSoloConXeY[i] and yObbiettivo == vetNemiciSoloConXeY[i + 1]:
                    bloccato = True
                    break
                i += 2
            if not bloccato and not (x == xObbiettivo and y == yObbiettivo):
                if abs(xObbiettivo - x) == GlobalHWVar.gpx and abs(yObbiettivo - y) == 0:
                    if x < xObbiettivo:
                        npers = 1
                    if x > xObbiettivo:
                        npers = 2
                    sposta = True
                elif abs(yObbiettivo - y) == GlobalHWVar.gpy and abs(xObbiettivo - x) == 0:
                    if y < yObbiettivo:
                        npers = 4
                    if y > yObbiettivo:
                        npers = 3
                    sposta = True
                else:
                    percorsoTrovato = GenericFunc.pathFinding(x, y, xObbiettivo, yObbiettivo, vetNemiciSoloConXeY, casevisteEntrateIncluse)
                    if percorsoTrovato and percorsoTrovato != "arrivato" and len(percorsoTrovato) >= 4 and (percorsoTrovato[len(percorsoTrovato) - 4] != x or percorsoTrovato[len(percorsoTrovato) - 3] != y):
                        if percorsoTrovato[len(percorsoTrovato) - 4] > x:
                            npers = 1
                        if percorsoTrovato[len(percorsoTrovato) - 4] < x:
                            npers = 2
                        if percorsoTrovato[len(percorsoTrovato) - 3] > y:
                            npers = 4
                        if percorsoTrovato[len(percorsoTrovato) - 3] < y:
                            npers = 3
                        sposta = True
                    else:
                        print ("Percorso Rallo verso cursore non trovato")
                # cambiare posizione
                if sposta:
                    if npers == 3:
                        ny = -GlobalHWVar.gpy
                        nx = 0
                        pers = GlobalImgVar.persw
                        arma = armaw
                        armaMov1 = armawMov1
                        armaMov2 = armawMov2
                        armaAttacco = armawAttacco
                        armatura = armaturaw
                        scudo = scudow
                        arco = arcow
                        faretra = faretraw
                        arcoAttacco = arcowAttacco
                        guanti = guantiw
                        guantiMov1 = guantiwMov1
                        guantiMov2 = guantiwMov2
                        guantiAttacco = guantiwAttacco
                        collana = collanaw
                    if npers == 2:
                        ny = 0
                        nx = -GlobalHWVar.gpx
                        pers = GlobalImgVar.persa
                        arma = armaa
                        armaMov1 = armaaMov1
                        armaMov2 = armaaMov2
                        armaAttacco = armaaAttacco
                        armatura = armaturaa
                        scudo = scudoa
                        arco = arcoa
                        faretra = faretraa
                        arcoAttacco = arcoaAttacco
                        guanti = guantia
                        guantiMov1 = guantiaMov1
                        guantiMov2 = guantiaMov2
                        guantiAttacco = guantiaAttacco
                        collana = collanaa
                    if npers == 4:
                        ny = GlobalHWVar.gpy
                        nx = 0
                        pers = GlobalImgVar.perss
                        arma = armas
                        armaMov1 = armasMov1
                        armaMov2 = armasMov2
                        armaAttacco = armasAttacco
                        armatura = armaturas
                        scudo = scudos
                        arco = arcos
                        faretra = faretras
                        arcoAttacco = arcosAttacco
                        guanti = guantis
                        guantiMov1 = guantisMov1
                        guantiMov2 = guantisMov2
                        guantiAttacco = guantisAttacco
                        collana = collanas
                    if npers == 1:
                        ny = 0
                        nx = GlobalHWVar.gpx
                        pers = GlobalImgVar.persd
                        arma = armad
                        armaMov1 = armadMov1
                        armaMov2 = armadMov2
                        armaAttacco = armadAttacco
                        armatura = armaturad
                        scudo = scudod
                        arco = arcod
                        faretra = faretrad
                        arcoAttacco = arcodAttacco
                        guanti = guantid
                        guantiMov1 = guantidMov1
                        guantiMov2 = guantidMov2
                        guantiAttacco = guantidAttacco
                        collana = collanad
            if nx == 0 and ny == 0:
                GlobalHWVar.canaleSoundPassiRallo.stop()

        # menu start
        if startf and attacco != 1:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selsta)
            refreshSchermo = True
            dati[2] = x
            dati[3] = y
            dati[140] = npers
            dati[134] = rx
            dati[135] = ry
            dati[141] = nrob
            dati[142] = chiamarob
            dati[139] = mosseRimasteRob
            dati[136] = raffredda
            dati[137] = autoRic1
            dati[138] = autoRic2
            # se c'è un nemico in caselleViste di Rallo => apri il menu di battaglia
            nemicoInCasellaVista = False
            colcoInCasellaVista = False
            i = 0
            while i < len(casevisteDaRallo):
                for nemico in listaNemici:
                    if nemico.x == casevisteDaRallo[i] and nemico.y == casevisteDaRallo[i + 1] and casevisteDaRallo[i + 2]:
                        nemicoInCasellaVista = True
                        break
                if rx == casevisteDaRallo[i] and ry == casevisteDaRallo[i + 1] and casevisteDaRallo[i + 2]:
                    colcoInCasellaVista = True
                i += 3
            if not nemicoInCasellaVista:
                aggiornaImgEquip = True
                dati, inizio, attacco, caricaSalvataggio = MenuPrincipali.start(dati, tutteporte, tutticofanetti, listaNemiciTotali, vettoreEsche, vettoreDenaro, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco, colcoInCasellaVista)
                if caricaSalvataggio:
                    inizio = True
                if attacco == 0:
                    uscitoDaMenu = 2
                if not inizio:
                    FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False, tipoOscuramento=3)
            else:
                dati, attacco, sposta, animaOggetto, npers, inizio = MenuPrincipali.startBattaglia(dati, animaOggetto, x, y, npers, rx, ry, inizio)
                # cambiare posizione dopo l'uso di caricabatterie
                if npers == 3:
                    pers = GlobalImgVar.persw
                    arma = armaw
                    armaMov1 = armawMov1
                    armaMov2 = armawMov2
                    armaAttacco = armawAttacco
                    armatura = armaturaw
                    scudo = scudow
                    arco = arcow
                    faretra = faretraw
                    arcoAttacco = arcowAttacco
                    guanti = guantiw
                    guantiMov1 = guantiwMov1
                    guantiMov2 = guantiwMov2
                    guantiAttacco = guantiwAttacco
                    collana = collanaw
                if npers == 2:
                    pers = GlobalImgVar.persa
                    arma = armaa
                    armaMov1 = armaaMov1
                    armaMov2 = armaaMov2
                    armaAttacco = armaaAttacco
                    armatura = armaturaa
                    scudo = scudoa
                    arco = arcoa
                    faretra = faretraa
                    arcoAttacco = arcoaAttacco
                    guanti = guantia
                    guantiMov1 = guantiaMov1
                    guantiMov2 = guantiaMov2
                    guantiAttacco = guantiaAttacco
                    collana = collanaa
                if npers == 4:
                    pers = GlobalImgVar.perss
                    arma = armas
                    armaMov1 = armasMov1
                    armaMov2 = armasMov2
                    armaAttacco = armasAttacco
                    armatura = armaturas
                    scudo = scudos
                    arco = arcos
                    faretra = faretras
                    arcoAttacco = arcosAttacco
                    guanti = guantis
                    guantiMov1 = guantisMov1
                    guantiMov2 = guantisMov2
                    guantiAttacco = guantisAttacco
                    collana = collanas
                if npers == 1:
                    pers = GlobalImgVar.persd
                    arma = armad
                    armaMov1 = armadMov1
                    armaMov2 = armadMov2
                    armaAttacco = armadAttacco
                    armatura = armaturad
                    scudo = scudod
                    arco = arcod
                    faretra = faretrad
                    arcoAttacco = arcodAttacco
                    guanti = guantid
                    guantiMov1 = guantidMov1
                    guantiMov2 = guantidMov2
                    guantiAttacco = guantidAttacco
                    collana = collanad
                caricaTutto = True
            carim = True
            startf = False

        # morte tua e di robo
        inizio, gameover = FunzioniGraficheGeneriche.controllaMorteRallo(dati[5], inizio, gameover)
        morterob, dati, mosseRimasteRob = GenericFunc.controllaMorteColco(dati, mosseRimasteRob)

        if not inizio:
            # setto stato personaggi all'inizio del turno
            for nemico in listaNemici:
                nemico.statoInizioTurno = []
                nemico.statoInizioTurno.append(nemico.vita)
                nemico.statoInizioTurno.append(nemico.avvelenato)
                nemico.statoInizioTurno.append(nemico.appiccicato)
            statoRalloInizioTurno = []
            statoRalloInizioTurno.append(dati[5])
            statoRalloInizioTurno.append(dati[121])
            statoRalloInizioTurno.append(dati[123])
            statoRalloInizioTurno.append(dati[124])
            statoColcoInizioTurno = []
            statoColcoInizioTurno.append(dati[10])
            statoColcoInizioTurno.append(dati[122])
            statoColcoInizioTurno.append(dati[125])
            statoColcoInizioTurno.append(dati[126])
            statoEscheInizioTurno = []
            i = 0
            while i < len(vettoreEsche):
                statoEscheInizioTurno.append("Esca" + str(vettoreEsche[i]))
                statoEscheInizioTurno.append(vettoreEsche[i + 1])
                i += 4

            # faccio animazione di quando ricevo un oggetto speciale
            if oggettoRicevuto:
                EnvPrint.disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, casellaChiara, casellaScura, casellaOscurata, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, entrateStanza, caselleNonVisibili, dati[0], nonMostrarePersonaggio)
                FunzioniGraficheGeneriche.animaOggettoSpecialeRicevuto(oggettoRicevuto)
                oggettoRicevuto = False
                caricaTutto = True

            # movimento-azioni personaggio
            if (nx != 0 or ny != 0) and not nemiciInMovimento and mosseRimasteRob <= 0:
                vx = x
                vy = y
                stanzaVecchia = dati[1]
                x, y, dati[1], carim, cambiosta = SetOstacoliContenutoCofanetti.controlloOstacoli(x, y, nx, ny, dati[1], carim, porte, cofanetti, dati[0])

                sovrapposto = False
                for nemico in listaNemici:
                    if nemico.x == x and nemico.y == y:
                        sovrapposto = True
                        break
                for personaggio in listaPersonaggi:
                    if personaggio.x == x and personaggio.y == y:
                        sovrapposto = True
                        break
                if sovrapposto:
                    x = vx
                    y = vy
                if x == rx and y == ry and not sovrapposto:
                    spingiColco = True
                if not (vx == x and vy == y):
                    sposta = True
                else:
                    GlobalHWVar.canaleSoundPassiRallo.stop()
            # gestione attacchi
            attaccoADistanza = False
            # attaccoDiRallo [obbiettivo, danno, status(avvelena, appiccica) ... => per ogni nemico colpito]
            attaccoDiRallo = []
            if attacco != 0:
                sposta, creaesca, xesca, yesca, npers, nrob, dati[5], dati[121], dati[10], difesa, apriChiudiPorta, apriCofanetto, listaNemici, attacco, attaccoADistanza, nemicoInquadrato, attaccoDiRallo, chiamarob, ultimoObbiettivoColco, animaOggetto, interagisciConPersonaggio, startf, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac = EnvPrint.attacca(dati, x, y, vx, vy, npers, nrob, rx, ry, obbiettivoCasualeColco, pers, dati[5], pvtot, dif, dati[121], dati[130], dati[123], dati[124], dati[10], entot, difro, dati[122], dati[125], dati[126], imgSfondoStanza, casellaChiara, casellaScura, casellaOscurata, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, attVicino, attLontano, attacco, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, vettoreDenaro, dati[132], nemicoInquadrato, raffredda, autoRic1, autoRic2, ultimoObbiettivoColco, animaOggetto, listaPersonaggi, startf, dati[0], casellePercorribili, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, mosseRimasteRob, nonMostrarePersonaggio)
                refreshSchermo = True
                caricaTutto = True
                # cancello apertura porta se non si può aprire
                if apriChiudiPorta[0] and not SetPosizioneAudioImpedimenti.possibileAprirePorta(dati[1], apriChiudiPorta[1], apriChiudiPorta[2], dati[0]):
                    apriChiudiPorta = [False, 0, 0]
                    sposta = False
                    impossibileAprirePorta = True
                # tolgo una freccia se uso l'attacco a distanza
                if attaccoADistanza:
                    dati[132] -= 1
                # cambiare posizione dopo l'attacco
                if npers == 3:
                    pers = GlobalImgVar.persw
                    arma = armaw
                    armaMov1 = armawMov1
                    armaMov2 = armawMov2
                    armaAttacco = armawAttacco
                    armatura = armaturaw
                    scudo = scudow
                    arco = arcow
                    faretra = faretraw
                    arcoAttacco = arcowAttacco
                    guanti = guantiw
                    guantiMov1 = guantiwMov1
                    guantiMov2 = guantiwMov2
                    guantiAttacco = guantiwAttacco
                    collana = collanaw
                if npers == 2:
                    pers = GlobalImgVar.persa
                    arma = armaa
                    armaMov1 = armaaMov1
                    armaMov2 = armaaMov2
                    armaAttacco = armaaAttacco
                    armatura = armaturaa
                    scudo = scudoa
                    arco = arcoa
                    faretra = faretraa
                    arcoAttacco = arcoaAttacco
                    guanti = guantia
                    guantiMov1 = guantiaMov1
                    guantiMov2 = guantiaMov2
                    guantiAttacco = guantiaAttacco
                    collana = collanaa
                if npers == 4:
                    pers = GlobalImgVar.perss
                    arma = armas
                    armaMov1 = armasMov1
                    armaMov2 = armasMov2
                    armaAttacco = armasAttacco
                    armatura = armaturas
                    scudo = scudos
                    arco = arcos
                    faretra = faretras
                    arcoAttacco = arcosAttacco
                    guanti = guantis
                    guantiMov1 = guantisMov1
                    guantiMov2 = guantisMov2
                    guantiAttacco = guantisAttacco
                    collana = collanas
                if npers == 1:
                    pers = GlobalImgVar.persd
                    arma = armad
                    armaMov1 = armadMov1
                    armaMov2 = armadMov2
                    armaAttacco = armadAttacco
                    armatura = armaturad
                    scudo = scudod
                    arco = arcod
                    faretra = faretrad
                    arcoAttacco = arcodAttacco
                    guanti = guantid
                    guantiMov1 = guantidMov1
                    guantiMov2 = guantidMov2
                    guantiAttacco = guantidAttacco
                    collana = collanad
                # decrementa oggetto utilizzato
                if sposta:
                    # bomba attacco = 2
                    if attacco == 2:
                        dati[36] = dati[36] - 1
                    # bomba veleno attacco = 3
                    if attacco == 3:
                        dati[37] = dati[37] - 1
                    # esca attacco = 4
                    if attacco == 4:
                        dati[38] = dati[38] - 1
                    # bomba appiccicosa attacco = 5
                    if attacco == 5:
                        dati[39] = dati[39] - 1
                    # bomba potenziata attacco = 6
                    if attacco == 6:
                        dati[40] = dati[40] - 1
            # gestione difesa
            if sposta:
                difesa = 0
            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati, difesa)
            if turniDaSaltarePerDifesa > 0 and not sposta:
                turniDaSaltarePerDifesa -= 1
                sposta = True
                if turniDaSaltarePerDifesa == 0:
                    caricaTutto = True
                    uscitoDaMenu = 2
            if difesa == 2 and not sposta:
                difesa = 1
                sposta = True
                riempiTuttaLaVita = True
                turniDaSaltarePerDifesa = 0
                for nemico in listaNemici:
                    if nemico.vita > 0 and nemico.inCasellaVista:
                        riempiTuttaLaVita = False
                        break
                if riempiTuttaLaVita and dati[5] + 3 < pvtot:
                    while dati[5] < pvtot:
                        dati[5] += 3
                        turniDaSaltarePerDifesa += 1
                    turniDaSaltarePerDifesa -= 1
                    dati[5] = pvtot
                    FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False, tipoOscuramento=1)
                else:
                    dati[5] += 3
                    if dati[5] > pvtot:
                        dati[5] = pvtot
            # gestione att+ e dif+
            if dati[123] > 0 and sposta:
                dati[123] = dati[123] - 1
            if dati[124] > 0 and sposta:
                dati[124] = dati[124] - 1
            # veleno
            if dati[121] and sposta and dati[5] > 0:
                dati[5] = dati[5] - 2
                if dati[5] <= 0:
                    dati[5] = 1
            # effetto collana rigenerante
            if dati[130] == 1 and sposta:
                dati[5] = dati[5] + 1
                if dati[5] > pvtot:
                    dati[5] = pvtot
            # apertura/chiusura porte
            if apriChiudiPorta[0]:
                k = 0
                while k < len(porte):
                    if porte[k] == dati[1] and porte[k + 1] == apriChiudiPorta[1] and porte[k + 2] == apriChiudiPorta[2]:
                        if porte[k + 3]:
                            GlobalHWVar.canaleSoundInterazioni.play(rumoreChiusuraPorte)
                            porte[k + 3] = False
                        else:
                            GlobalHWVar.canaleSoundInterazioni.play(rumoreAperturaPorte)
                            porte[k + 3] = True
                        caseviste, casevisteDaRallo, casevisteEntrateIncluse, caselleNonVisibili, casellePercorribili = GenericFunc.creaTuttiIVettoriPerLeCaselleViste(x, y, rx, ry, dati[1], porte, cofanetti, dati[0])
                        # aggiornare vettore tutteporte
                        j = 0
                        while j < len(tutteporte):
                            if tutteporte[j] == porte[k] and tutteporte[j + 1] == porte[k + 1] and tutteporte[j + 2] == porte[k + 2]:
                                tutteporte[j + 3] = porte[k + 3]
                                break
                            j = j + 4
                        # aggiorno inCasellaVista di nemici e personaggi
                        listaNemici, listaPersonaggi = GenericFunc.aggiornaInCasellaVistaDiNemiciEPersonaggi(caseviste, listaNemici, listaPersonaggi)
                        # aggiorno il campo attaccabile di colco
                        if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"]:
                            caselleAttaccabiliColco = GenericFunc.trovacasattaccabili(rx, ry, GlobalGameVar.vistaRobo * GlobalHWVar.gpx, caseviste)
                            posizioneColcoAggiornamentoCaseAttac = [rx, ry]
                        # aggiorno la vista dei nemici
                        for nemico in listaNemici:
                            if nemico.vita > 0 and nemico.inCasellaVista:
                                nemico.aggiornaVista(x, y, rx, ry, dati, caseviste, True)
                        break
                    k = k + 4
                apriChiudiPorta = [False, 0, 0]
                # controllo se devo deselezionare il nemico/esca inquadrato
                if not type(nemicoInquadrato) is str and nemicoInquadrato:
                    i = 0
                    while i < len(caseviste):
                        if not caseviste[i + 2] and caseviste[i] == nemicoInquadrato.x and caseviste[i + 1] == nemicoInquadrato.y:
                            nemicoInquadrato = False
                            break
                        i += 3
                # vita esche selezionate
                elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
                    idEscaInquadrata = int(nemicoInquadrato[4:])
                    i = 0
                    while i < len(vettoreEsche):
                        if idEscaInquadrata == vettoreEsche[i]:
                            j = 0
                            while j < len(caseviste):
                                if caseviste[j] == vettoreEsche[i + 2] and caseviste[j + 1] == vettoreEsche[i + 3] and not caseviste[j + 2]:
                                    nemicoInquadrato = False
                                j += 3
                            break
                        i += 4
            # interazioni con altri personaggi
            if interagisciConPersonaggio:
                for personaggio in listaPersonaggi:
                    if (personaggio.x == x + GlobalHWVar.gpx and personaggio.y == y and npers == 1) or (personaggio.x == x - GlobalHWVar.gpx and personaggio.y == y and npers == 2) or (personaggio.x == x and personaggio.y == y + GlobalHWVar.gpy and npers == 4) or (personaggio.x == x and personaggio.y == y - GlobalHWVar.gpy and npers == 3):
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        if npers == 1:
                            personaggio.girati("a")
                        elif npers == 2:
                            personaggio.girati("d")
                        elif npers == 3:
                            personaggio.girati("s")
                        elif npers == 4:
                            personaggio.girati("w")
                        # aggiorno lo GlobalVarG2.schermo (serve per girare i pers uno verso l'altro e per togliere il campo visivo dell'obiettivo selezionato)
                        EnvPrint.disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, casellaChiara, casellaScura, casellaOscurata, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, entrateStanza, caselleNonVisibili, dati[0], nonMostrarePersonaggio)
                        dati[0], oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(dati[0], personaggio, listaAvanzamentoDialoghi)
                        sposta = True
                        caricaTutto = True
                interagisciConPersonaggio = False
            # menu mercante
            if visualizzaMenuMercante:
                dati = MenuDialoghi.menuMercante(dati)
                visualizzaMenuMercante = False
                uscitoDaMenu = 2
                carim = True
            # apertura cofanetti
            if apriCofanetto[0]:
                i = 0
                while i < len(cofanetti):
                    if cofanetti[i] == dati[1] and cofanetti[i + 1] == apriCofanetto[1] and cofanetti[i + 2] == apriCofanetto[2] and not cofanetti[i + 3]:
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoaperturacofanetti)
                        dati, tesoro, dati[0] = SetOstacoliContenutoCofanetti.aperturacofanetto(cofanetti[i], cofanetti[i + 1], cofanetti[i + 2], dati)
                        if tesoro == -2 or tesoro == -1 or tesoro > 0:
                            cofanetti[i + 3] = True
                        # aggiornare vettore tutticofanetti
                        j = 0
                        while j < len(tutticofanetti):
                            if tutticofanetti[j] == cofanetti[i] and tutticofanetti[j + 1] == cofanetti[i + 1] and tutticofanetti[j + 2] == cofanetti[i + 2]:
                                if tesoro == -2 or tesoro == -1 or tesoro > 0:
                                    tutticofanetti[j + 3] = True
                            j = j + 4
                    i = i + 4
                apriCofanetto = [False, 0, 0]
            # scambia posizione con Colco
            if spingiColco:
                rx = vx
                ry = vy
                vrx = rx
                vry = ry
                if not chiamarob:
                    caselleAttaccabiliColco = GenericFunc.trovacasattaccabili(rx, ry, GlobalGameVar.vistaRobo * GlobalHWVar.gpx, caseviste)
                    posizioneColcoAggiornamentoCaseAttac = [rx, ry]
                spingiColco = False
            # aggiorna la posizione del telecolco se è attivo
            if chiamarob:
                ultimoObbiettivoColco = []
                ultimoObbiettivoColco.append("Telecomando")
                ultimoObbiettivoColco.append(x)
                ultimoObbiettivoColco.append(y)

            # impedisce di andare avanti quando si vuole andare in una zona non ancora sbloccata
            if cambiosta and SetPosizioneAudioImpedimenti.nonPuoiProcedere(dati[0], stanzaVecchia, dati[1]):
                cambiosta = False
                dati[1] = stanzaVecchia
                xPrimaDiCambioStanza = x
                yPrimaDiCambioStanza = y
                x = vx
                y = vy
                sposta = False
                caricaTutto = True
                bottoneDown = False

                EnvPrint.disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, casellaChiara, casellaScura, casellaOscurata, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, entrateStanza, caselleNonVisibili, dati[0], nonMostrarePersonaggio)
                personaggio = PersonaggioObj.PersonaggioObj(xPrimaDiCambioStanza, yPrimaDiCambioStanza, False, "Nessuno", dati[1], dati[0], False)
                dati[0], oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(dati[0], personaggio, listaAvanzamentoDialoghi)

            # lancio esche
            if creaesca:
                contaesca = 0
                if len(vettoreEsche) > 0:
                    contaesca = vettoreEsche[len(vettoreEsche) - 4] + 1
                # id, vita, xesca, yesca
                vettoreEsche.append(contaesca)
                vettoreEsche.append(1000)
                vettoreEsche.append(xesca)
                vettoreEsche.append(yesca)
                creaesca = False
            # riprendere le esche
            i = 1
            while i < len(vettoreEsche):
                if vettoreEsche[i + 1] == x and vettoreEsche[i + 2] == y:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoRaccoltaEsca)
                    # tolgo la GlobalVarG2.selezione dell'esca ripresa
                    if type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and int(nemicoInquadrato[4:]) == vettoreEsche[i - 1]:
                        nemicoInquadrato = False
                        caricaTutto = True
                    del vettoreEsche[i + 2]
                    del vettoreEsche[i + 1]
                    del vettoreEsche[i]
                    del vettoreEsche[i - 1]
                    dati[38] += 1
                i += 4
            i = 0
            while i < len(vettoreEsche):
                if not vettoreEsche[i + 1] in statoEscheInizioTurno:
                    statoEscheInizioTurno.append("Esca" + str(vettoreEsche[i]))
                    statoEscheInizioTurno.append(vettoreEsche[i + 1])
                i += 4

            # movimento-azioni robo
            azioneRobEseguita = False
            if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] and dati[122] > 0 and (dati[125] > 0 or dati[126] > 0):
                # se surriscaldato toglie vel+ e efficienza
                dati[125] = 0
                dati[126] = 0
                refreshSchermo = True
            if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] and sposta and mosseRimasteRob == 0 and not morterob:
                if dati[125] > 0:
                    mosseRimasteRob = 2
                else:
                    mosseRimasteRob = 1
            # effetto di surriscalda / raffreddamento / auto-ricarica / auto-ricarica+
            if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] and sposta:
                # surriscalda
                if dati[122] > 0:
                    dati[122] = dati[122] - 1
                    dati[10] = dati[10] - 3
                # efficienza
                if dati[126] > 0:
                    dati[126] -= 1
                # vel+
                if dati[125] > 0:
                    dati[125] -= 1
                    if dati[125] == 0:
                        dati[122] = 10
                # raffred
                if raffredda >= 0:
                    raffreddamento = False
                    raffredda -= 1
                if raffredda == 0:
                    dati[122] = 0
                # autoric
                if autoRic1 >= 0:
                    ricarica1 = False
                    autoRic1 -= 1
                if autoRic1 == 0:
                    dati[10] += GlobalGameVar.dannoTecniche[6]
                    if dati[10] > entot:
                        dati[10] = entot
                    dati[122] = 10
                # autoric+
                if autoRic2 >= 0:
                    ricarica2 = False
                    autoRic2 -= 1
                if autoRic2 == 0:
                    dati[10] += GlobalGameVar.dannoTecniche[16]
                    if dati[10] > entot:
                        dati[10] = entot
                    dati[122] = 10
            listaNemiciAttaccatiADistanzaRobo = False
            # attaccoDiColco [obbiettivo, danno, status (antidoto, attP, difP, velocizza, efficienza) ... => per ogni nemico colpito (non raffredda perchè deve rimanere per più turni)]
            attaccoDiColco = []
            tecnicaUsata = False
            if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] and mosseRimasteRob > 0 and not morterob and not cambiosta:
                vrx = rx
                vry = ry

                # movimento - gambit
                if raffredda < 0 and autoRic1 < 0 and autoRic2 < 0:
                    rx, ry, nrob, dati, listaNemici, raffreddamento, ricarica1, ricarica2, azioneRobEseguita, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, attaccoDiColco, ultimoObbiettivoColco, obbiettivoCasualeColco, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, vettoreEsche = MovNemiciRob.movrobo(x, y, vx, vy, rx, ry, chiamarob, dati, porte, listaNemici, difesa, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggi, caseviste, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, vettoreEsche, analizzaColco=False)

                if dati[122] > 0 or raffreddamento or ricarica1 or ricarica2:
                    mosseRimasteRob -= 2
                else:
                    mosseRimasteRob -= 1
                if raffreddamento:
                    raffredda = 1
                if ricarica1:
                    autoRic1 = 1
                if ricarica2:
                    autoRic2 = 1

                sovrapposto = False
                for nemico in listaNemici:
                    if nemico.x == rx and nemico.y == ry:
                        sovrapposto = True
                        break
                if sovrapposto:
                    rx = vrx
                    ry = vry
                    nrob = 0
                    azioneRobEseguita = False
                if nrob != 0:
                    if nrob == 1:
                        robot = GlobalImgVar.robod
                        armrob = armrobd
                    if nrob == 2:
                        robot = GlobalImgVar.roboa
                        armrob = armroba
                    if nrob == 3:
                        robot = GlobalImgVar.robos
                        armrob = armrobs
                    if nrob == 4:
                        robot = GlobalImgVar.robow
                        armrob = armrobw
                if (rx != vrx or ry != vry) and not chiamarob:
                    caselleAttaccabiliColco = GenericFunc.trovacasattaccabili(rx, ry, GlobalGameVar.vistaRobo * GlobalHWVar.gpx, caseviste)
                    posizioneColcoAggiornamentoCaseAttac = [rx, ry]
            elif dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] and sposta and mosseRimasteRob < 0 and not morterob:
                mosseRimasteRob += 1
            if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] and morterob:
                robot = GlobalImgVar.robomo
                armrob = GlobalImgVar.armrobmo
            if dati[0] < GlobalGameVar.dictAvanzamentoStoria["incontratoColco"]:
                rx = GlobalHWVar.gsx
                ry = GlobalHWVar.gsy
                vrx = rx
                vry = ry

            # aggiorna vista dei mostri (per mettere l'occhio se ti vedono) e aggiorno xPosizioneUltimoBersaglio e yPosizioneUltimoBersaglio se ci sono attacchi a distanza
            apriocchio = False
            for nemico in listaNemici:
                if nemico.vita > 0 and nemico.inCasellaVista:
                    nemico.aggiornaBersaglioAttacchiDistanti(x, y, rx, ry, attaccoADistanza, listaNemiciAttaccatiADistanzaRobo)
                    nemico.aggiornaVista(x, y, rx, ry, dati, caseviste, False)
                    if nemico.visto:
                        apriocchio = True
                else:
                    nemico.visto = False
            # movimento-azioni mostri
            if len(listaNemici) > 0 and not cambiosta:
                for nemico in listaNemici:
                    if nemico.avvelenato and sposta and nemico.vita > 0:
                        nemico.vita -= 3
                        if nemico.vita <= 0:
                            nemico.vita = 1
                    if nemico.vita > 0 and nemico.inCasellaVista:
                        if sposta and nemico.mosseRimaste == 0:
                            nemico.resettaMosseRimaste()
                        if nemico.mosseRimaste > 0:
                            vetDatiNemici = []
                            for nemicoTemp in listaNemici:
                                if nemicoTemp.vita > 0:
                                    vetDatiNemici.append(nemicoTemp.vita)
                                    vetDatiNemici.append(nemicoTemp.x)
                                    vetDatiNemici.append(nemicoTemp.y)
                                    vetDatiNemici.append(nemicoTemp.vitaTotale)
                            # trovo l'obbiettivo
                            nemico.settaObbiettivo(x, y, rx, ry, dati, vettoreDenaro, vettoreEsche, listaPersonaggi, listaNemici, porte, caseviste)
                            nemico.vx = nemico.x
                            nemico.vy = nemico.y
                            nemico, direzioneMostro, dati, vettoreEsche = MovNemiciRob.movmostro(x, y, rx, ry, nemico, dif, difro, par, dati, vettoreEsche, vetDatiNemici, listaPersonaggi, caseviste, dati[0])
                            if direzioneMostro == 1:
                                nemico.girati("d")
                            elif direzioneMostro == 2:
                                nemico.girati("a")
                            elif direzioneMostro == 3:
                                nemico.girati("s")
                            elif direzioneMostro == 4:
                                nemico.girati("w")
                            i = 0
                            while i < len(vetDatiNemici):
                                if nemico.x == vetDatiNemici[i + 1] and nemico.y == vetDatiNemici[i + 2]:
                                    nemico.x = nemico.vx
                                    nemico.y = nemico.vy
                                    nemico.animaSpostamento = False
                                    break
                                i += 4
                            for personaggio in listaPersonaggi:
                                if nemico.x == personaggio.x and nemico.y == personaggio.y:
                                    nemico.x = nemico.vx
                                    nemico.y = nemico.vy
                                    nemico.animaSpostamento = False
                                    break
                            if (nemico.x == x and nemico.y == y) or (nemico.x == rx and nemico.y == ry):
                                nemico.x = nemico.vx
                                nemico.y = nemico.vy
                                nemico.animaSpostamento = False
                            if nemico.animaSpostamento:
                                if nemico.numeroMovimento < len(nemico.percorso) - 1:
                                    nemico.numeroMovimento += 1
                                else:
                                    nemico.numeroMovimento = 0
                            elif len(nemico.percorso) > 0 and nemico.percorso[nemico.numeroMovimento] == "":
                                nemico.numeroMovimento += 1
                            if nemico.vx != nemico.x or nemico.vy != nemico.y:
                                nemico.aggiornaVista(x, y, rx, ry, dati, caseviste, True)
                            nemico.compiMossa()
                        elif sposta and nemico.mosseRimaste < 0:
                            nemico.mosseRimaste += 1
                    elif nemico.vita <= 0:
                        dati[127] += nemico.esp
                        # effetto apprendimaschera
                        if dati[130] == 3:
                            dati[127] += nemico.esp
                        # metto il suo denaro nella casella in cui è morto (vettore => qta, x, y)
                        denaroDroppato = nemico.denaro
                        # effetto portafortuna
                        if dati[130] == 4:
                            denaroDroppato += int(nemico.denaro * 1.5)
                            if denaroDroppato == 0:
                                denaroDroppato = 1
                        if denaroDroppato > 0:
                            vettoreDenaro.append(denaroDroppato)
                            vettoreDenaro.append(nemico.x)
                            vettoreDenaro.append(nemico.y)
                        nemico.morto = True
                        nemico.animaMorte = True

            # movimento personaggi che sono in una casella vista
            if sposta:
                for personaggio in listaPersonaggi:
                    if personaggio.inCasellaVista and not personaggio.mantieniSempreASchermo:
                        personaggio.spostati(x, y, rx, ry, listaNemici, listaPersonaggi, caseviste)

            # aumentare di livello
            while dati[127] >= esptot and dati[4] < 100:
                dati[4] += 1
                dati[127] -= esptot
                aumentoliv += 1
                esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati, difesa)
                impossibileCliccarePulsanti = True

            # aggiorna i dialoghi e le img di tutti i personaggi in base all'avanzamento nella storia
            for personaggio in listaPersonaggi:
                if personaggio.tipo.startswith("Oggetto"):
                    imgAggiornata = personaggio.aggiornaImgOggetto(dati[0])
                    if imgAggiornata:
                        refreshSchermo = True

            # fai tutte le animazioni del turno e disegni gli sfondi e personaggi
            if caricaTutto and turniDaSaltarePerDifesa == 0:
                refreshSchermo = True
                if aumentoliv != 0:
                    pvtot = GenericFunc.getVitaTotRallo(dati[4] - aumentoliv, dati[129])
                EnvPrint.disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, casellaChiara, casellaScura, casellaOscurata, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, entrateStanza, caselleNonVisibili, dati[0], nonMostrarePersonaggio)
                caricaTutto = False
            if (azioneRobEseguita or nemiciInMovimento or sposta) and not uscitoDaMenu > 0 and turniDaSaltarePerDifesa == 0:
                primopasso, caricaTutto, tesoro, bottoneDown, movimentoPerMouse, robot, armrob = Animazioni.anima(sposta, x, y, vx, vy, rx, ry, vrx, vry, pers, robot, npers, nrob, primopasso, cambiosta, casellaChiara, casellaScura, scudo, armatura, arma, armaMov1, armaMov2, armaAttacco, scudoDifesa, arco, faretra, arcoAttacco, guanti, guantiMov1, guantiMov2, guantiAttacco, guantiDifesa, collana, armas, armaturas, arcos, faretras, collanas, armrob, armrobs, dati, attacco, difesa, bottoneDown, tesoro, aumentoliv, caricaTutto, listaNemici, vettoreEsche, vettoreDenaro, attaccoADistanza, caseviste, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoInquadrato, attaccoDiRallo, attaccoDiColco, statoRalloInizioTurno, statoColcoInizioTurno, statoEscheInizioTurno, raffreddamento, ricarica1, ricarica2, raffredda, autoRic1, autoRic2, animaOggetto, listaPersonaggi, apriocchio, chiamarob, movimentoPerMouse, vettoreImgCaselle, nonMostrarePersonaggio)
            if not carim and (refreshSchermo or azioneRobEseguita or nemiciInMovimento or sposta) and turniDaSaltarePerDifesa == 0:
                refreshSchermo = False
                apriocchio = False
                for nemico in listaNemici:
                    if nemico.vita > 0 and nemico.visto:
                        apriocchio = True
                        break
                pvtot = GenericFunc.getVitaTotRallo(dati[4], dati[129])
                EnvPrint.disegnaAmbiente(x, y, npers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, casellaChiara, casellaScura, casellaOscurata, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, False, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, entrateStanza, caselleNonVisibili, dati[0], nonMostrarePersonaggio)

            # gestisce eventi speciali come i dialoghi del tutorial o dialoghi con nessuno
            if not carim:
                dati[0], cambiosta, dati[1], npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio = SetNemiciPersonaggiEventi.gestisciEventiStoria(dati[0], dati[1], npers, x, y, cambiosta, carim, caricaTutto, bottoneDown, movimentoPerMouse, impossibileAprirePorta, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, stanzeGiaVisitate, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, canzone, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio)
                impossibileAprirePorta = False
                if caricaTutto:
                    impossibileCliccarePulsanti = True

            # cancella definitivamente i mostri morti e resetta vx/vy/anima
            i = len(listaNemici) - 1
            while i >= 0:
                nemico = listaNemici[i]
                nemico.vx = nemico.x
                nemico.vy = nemico.y
                nemico.animaSpostamento = False
                nemico.animaAttacco = False
                nemico.animaMorte = False
                nemico.animaDanneggiamento = []
                nemico.bersaglioColpito = []
                nemico.ralloParato = False
                if not type(nemicoInquadrato) is str and nemicoInquadrato and nemicoInquadrato.morto:
                    nemicoInquadrato = False
                    caricaTutto = True
                if nemico.morto:
                    listaNemici.remove(nemico)
                    listaNemiciTotali.remove(nemico)
                i -= 1
            # morte esche
            i = 1
            while i < len(vettoreEsche):
                if vettoreEsche[i] <= 0:
                    # tolgo la selezione dell'esca morta
                    if type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and int(nemicoInquadrato[4:]) == vettoreEsche[i - 1]:
                        nemicoInquadrato = False
                        caricaTutto = True
                    del vettoreEsche[i + 2]
                    del vettoreEsche[i + 1]
                    del vettoreEsche[i]
                    del vettoreEsche[i - 1]
                else:
                    i += 4

            # aggiorna i dialoghi e le img di tutti i personaggi in base all'avanzamento nella storia
            for personaggio in listaPersonaggi:
                personaggio.aggiornaDialogo(dati[0])
                if personaggio.tipo.startswith("Oggetto"):
                    imgAggiornata = personaggio.aggiornaImgOggetto(dati[0])
                    if imgAggiornata:
                        refreshSchermo = True

            # prendere il denaro da terra
            i = 0
            while i < len(vettoreDenaro):
                denaroPreso = False
                if vettoreDenaro[i + 1] == x and vettoreDenaro[i + 2] == y:
                    dati[131] = UtilityOstacoliContenutoCofanetti.ottieniMonete(dati, vettoreDenaro[i])
                    del vettoreDenaro[i + 2]
                    del vettoreDenaro[i + 1]
                    del vettoreDenaro[i]
                    denaroPreso = True
                if not denaroPreso:
                    for nemico in listaNemici:
                        if vettoreDenaro[i + 1] == nemico.x and vettoreDenaro[i + 2] == nemico.y:
                            nemico.denaro += vettoreDenaro[i]
                            del vettoreDenaro[i + 2]
                            del vettoreDenaro[i + 1]
                            del vettoreDenaro[i]
                            refreshSchermo = True
                            break
                i += 3

            vx = x
            vy = y
            vrx = rx
            vry = ry
            attacco = 0
            animaOggetto = [False, 0, 0]
            stanzaCambiata = False
            uscitoDaMenu -= 1
            sposta = False

        if inizio:
            if not caricaSalvataggio:
                FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False)
            GlobalHWVar.canaleSoundPuntatoreSposta.stop()
            GlobalHWVar.canaleSoundPuntatoreSeleziona.stop()
            GlobalHWVar.canaleSoundPassiRallo.stop()
            GlobalHWVar.canaleSoundPassiColco.stop()
            GlobalHWVar.canaleSoundPassiNemiciPersonaggi.stop()
            GlobalHWVar.canaleSoundMorteNemici.stop()
            GlobalHWVar.canaleSoundLvUp.stop()
            GlobalHWVar.canaleSoundInterazioni.stop()
            GlobalHWVar.canaleSoundAttacco.stop()
            i = GlobalHWVar.volumeCanzoni / 2
            j = GlobalHWVar.volumeEffetti / 2
            while i > 0 or j > 0:
                GlobalHWVar.canaleSoundCanzone.set_volume(i)
                GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(j)
                i -= GlobalHWVar.volumeCanzoni / 10
                j -= GlobalHWVar.volumeEffetti / 10
                pygame.time.wait(30)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.canaleSoundCanzone.stop()
            GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
            GlobalHWVar.canaleSoundSottofondoAmbientale.stop()
            GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti)

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMainLoop.tick(GlobalHWVar.fpsMainLoop)

gameloop()
