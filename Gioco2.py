# -*- coding: utf-8 -*-

from Menu import *
from EnvPrint import *
from Animazioni import *
from SetNemiciPersonaggiEventi import *
from SetPosizioneAudioImpedimenti import *


def gameloop():
    caricaSalvataggio = False
    inizio = True
    gameover = False
    while True:
        if inizio:
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

            dati, porteini, portefin, cofaniini, cofanifin, listaNemiciTotali, vettoreEsche, vettoreDenaro, stanzeGiaVisitate, listaPersonaggiTotali, oggettiRimastiASam, ultimoObbiettivoColco, obbiettivoCasualeColco = menu(caricaSalvataggio, gameover)
            print ("Salvataggio: " + str(GlobalVar.numSalvataggioCaricato))
            gameover = False
            # controlla se devi cambiare personaggio giocabile
            if GlobalVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= dati[0] < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                personaggioDaUsare = "FratelloMaggiore"
                cambiaProtagonista(personaggioDaUsare)
                personaggioUsato = personaggioDaUsare
            else:
                personaggioDaUsare = "Sara"
                cambiaProtagonista(personaggioDaUsare)
                personaggioUsato = personaggioDaUsare
            caricaSalvataggio = False
            pers = GlobalVar.perss
            robot = GlobalVar.robos
            print (dati)

            # creare vettore porte -> porte[stanza, x, y, True/False, ...]
            porte = []
            tutteporte = []
            i = porteini
            while i <= portefin:
                tutteporte.append(dati[i])
                tutteporte.append(dati[i + 1])
                tutteporte.append(dati[i + 2])
                tutteporte.append(dati[i + 3])
                i = i + 4

            # creare vettore cofanetti -> cofanetti[stanza, x, y, True/False, ...]
            cofanetti = []
            tutticofanetti = []
            i = cofaniini
            while i <= cofanifin:
                tutticofanetti.append(dati[i])
                tutticofanetti.append(dati[i + 1])
                tutticofanetti.append(dati[i + 2])
                tutticofanetti.append(dati[i + 3])
                i = i + 4

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
            if GlobalVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= dati[0] < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                personaggioDaUsare = "FratelloMaggiore"
            else:
                personaggioDaUsare = "Sara"
            if personaggioDaUsare != personaggioUsato:
                cambiaProtagonista(personaggioDaUsare)
                personaggioUsato = personaggioDaUsare
                npers = 4

            if cambiosta:
                if not inizio:
                    sprites = pygame.sprite.Group(Fade(0))
                    schermoFadeToBlack = GlobalVar.schermo.copy().convert()
                    oscuraIlluminaSchermo(sprites, schermoFadeToBlack)

                canzoneCambiata = False
                sottofondoAmbientaleCambiato = False
                # mi posiziono e setto canzone, sottofondo ambientale e rumore porte
                x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, sottofondoAmbientaleCambiato, canzone, sottofondoAmbientale = settaPosizioneERumoriStanza(x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, sottofondoAmbientaleCambiato, dati[1], stanzaVecchia, canzone, sottofondoAmbientale, inizio)
                if not inizio:
                    vx = x
                    vy = y
                    if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
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
                    i = GlobalVar.volumeCanzoni
                    j = GlobalVar.volumeEffetti
                    while i > 0 and j > 0:
                        if canzoneCambiata:
                            GlobalVar.canaleSoundCanzone.set_volume(i)
                        if sottofondoAmbientaleCambiato:
                            GlobalVar.canaleSoundSottofondoAmbientale.set_volume(j)
                        i -= GlobalVar.volumeCanzoni / 10
                        j -= GlobalVar.volumeEffetti / 10
                        pygame.time.wait(30)
                    if canzoneCambiata:
                        GlobalVar.canaleSoundCanzone.stop()
                        GlobalVar.canaleSoundCanzone.set_volume(GlobalVar.volumeCanzoni)
                    if sottofondoAmbientaleCambiato:
                        GlobalVar.canaleSoundSottofondoAmbientale.stop()
                        GlobalVar.canaleSoundSottofondoAmbientale.set_volume(GlobalVar.volumeEffetti)
                    if canzone and canzoneCambiata:
                        GlobalVar.canaleSoundCanzone.play(canzone, -1)
                    if sottofondoAmbientale and sottofondoAmbientaleCambiato:
                        GlobalVar.canaleSoundSottofondoAmbientale.play(sottofondoAmbientale, -1)

                # resetto obbiettivo Colco
                if not inizio:
                    ultimoObbiettivoColco = []
                    obbiettivoCasualeColco = False

                # carico nemici e personaggi nella stanza
                listaNemici, listaPersonaggi, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali = caricaNemiciEPersonaggi(dati[0], dati[1], stanzaVecchia, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali)
                stanzaVecchia = dati[1]

                # stanza
                nomeStanza = settaNomeStanza(dati[0], dati[1])
                imgSfondoStanza = GlobalVar.loadImage("Immagini/Scenari/Stanza" + str(dati[1]) + "/" + nomeStanza + ".png", GlobalVar.gsx, GlobalVar.gsy, True, canale_alpha=False)
                casellaChiara = GlobalVar.loadImage("Immagini/Scenari/CasellaChiara.png", GlobalVar.gpx, GlobalVar.gpy, True)
                casellaScura = GlobalVar.loadImage("Immagini/Scenari/CasellaScura.png", GlobalVar.gpx, GlobalVar.gpy, True)
                casellaOscurata = GlobalVar.loadImage("Immagini/Scenari/CasellaOscurata.png", GlobalVar.gpx, GlobalVar.gpy, True)
                portaVert = GlobalVar.loadImage("Immagini/Scenari/Stanza" + str(dati[1]) + "/PortaVerticale.png", GlobalVar.gpx, GlobalVar.gpy, True)
                portaOriz = GlobalVar.loadImage("Immagini/Scenari/Stanza" + str(dati[1]) + "/PortaOrizzontale.png", GlobalVar.gpx, GlobalVar.gpy, True)

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
                    i = i + 4

                caseviste, casevisteDaRallo, casevisteEntrateIncluse, casellePercorribili = creaTuttiIVettoriPerLeCaselleViste(x, y, rx, ry, dati[1], porte, cofanetti)

                GlobalVar.schermo.blit(imgSfondoStanza, (0, 0))
                schermoOriginale = GlobalVar.schermo.copy().convert()
                GlobalVar.schermo.fill(GlobalVar.nero)
                vettoreImgCaselle = []
                i = 0
                while i < len(casellePercorribili):
                    vettoreImgCaselle.append(casellePercorribili[i])
                    vettoreImgCaselle.append(casellePercorribili[i + 1])
                    vettoreImgCaselle.append(schermoOriginale.subsurface(pygame.Rect(casellePercorribili[i], casellePercorribili[i + 1], GlobalVar.gpx, GlobalVar.gpy)))
                    i += 3

                if not inizio:
                    # eliminare tutte le esche
                    vettoreEsche = []
                    # elimino tutti i sacchetti di denaro
                    vettoreDenaro = []

                cambiosta = False
                stanzaCambiata = True
                impossibileCliccarePulsanti = True

            if not cambiosta:
                # arma
                armaw = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%iw.png" % dati[6], GlobalVar.gpx, GlobalVar.gpy, True)
                armawMov1 = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%iwMov1.png" % dati[6], GlobalVar.gpx, GlobalVar.gpy, True)
                armawMov2 = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%iwMov2.png" % dati[6], GlobalVar.gpx, GlobalVar.gpy, True)
                armaa = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%ia.png" % dati[6], GlobalVar.gpx, GlobalVar.gpy, True)
                armaaMov1 = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%iaMov1.png" % dati[6], GlobalVar.gpx, GlobalVar.gpy, True)
                armaaMov2 = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%iaMov2.png" % dati[6], GlobalVar.gpx, GlobalVar.gpy, True)
                armas = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%is.png" % dati[6], GlobalVar.gpx, GlobalVar.gpy, True)
                armasMov1 = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%isMov1.png" % dati[6], GlobalVar.gpx, GlobalVar.gpy, True)
                armasMov2 = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%isMov2.png" % dati[6], GlobalVar.gpx, GlobalVar.gpy, True)
                armad = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%id.png" % dati[6], GlobalVar.gpx, GlobalVar.gpy, True)
                armadMov1 = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%idMov1.png" % dati[6], GlobalVar.gpx, GlobalVar.gpy, True)
                armadMov2 = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%idMov2.png" % dati[6], GlobalVar.gpx, GlobalVar.gpy, True)
                armasAttacco = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%isAttacco.png" % dati[6], GlobalVar.gpx, GlobalVar.gpy * 2, True)
                armaaAttacco = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%iaAttacco.png" % dati[6], GlobalVar.gpx * 2, GlobalVar.gpy, True)
                armadAttacco = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%idAttacco.png" % dati[6], GlobalVar.gpx * 2, GlobalVar.gpy, True)
                armawAttacco = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%iwAttacco.png" % dati[6], GlobalVar.gpx, GlobalVar.gpy * 2, True)
                # arco
                arcow = GlobalVar.loadImage("Immagini/EquipSara/Archi/Arco%iw.png" % dati[128], GlobalVar.gpx, GlobalVar.gpy, True)
                arcoa = GlobalVar.loadImage("Immagini/EquipSara/Archi/Arco%ia.png" % dati[128], GlobalVar.gpx, GlobalVar.gpy, True)
                arcos = GlobalVar.loadImage("Immagini/EquipSara/Archi/Arco%is.png" % dati[128], GlobalVar.gpx, GlobalVar.gpy, True)
                arcod = GlobalVar.loadImage("Immagini/EquipSara/Archi/Arco%id.png" % dati[128], GlobalVar.gpx, GlobalVar.gpy, True)
                arcosAttacco = GlobalVar.loadImage("Immagini/EquipSara/Archi/Arco%isAttacco.png" % dati[128], GlobalVar.gpx, GlobalVar.gpy * 2, True)
                arcoaAttacco = GlobalVar.loadImage("Immagini/EquipSara/Archi/Arco%iaAttacco.png" % dati[128], GlobalVar.gpx * 2, GlobalVar.gpy, True)
                arcodAttacco = GlobalVar.loadImage("Immagini/EquipSara/Archi/Arco%idAttacco.png" % dati[128], GlobalVar.gpx * 2, GlobalVar.gpy, True)
                arcowAttacco = GlobalVar.loadImage("Immagini/EquipSara/Archi/Arco%iwAttacco.png" % dati[128], GlobalVar.gpx, GlobalVar.gpy * 2, True)
                # faretra
                faretraw = GlobalVar.loadImage("Immagini/EquipSara/Faretre/Faretra%iw.png" % dati[133], GlobalVar.gpx, GlobalVar.gpy, True)
                faretraa = GlobalVar.loadImage("Immagini/EquipSara/Faretre/Faretra%ia.png" % dati[133], GlobalVar.gpx, GlobalVar.gpy, True)
                faretras = GlobalVar.loadImage("Immagini/EquipSara/Faretre/Faretra%is.png" % dati[133], GlobalVar.gpx, GlobalVar.gpy, True)
                faretrad = GlobalVar.loadImage("Immagini/EquipSara/Faretre/Faretra%id.png" % dati[133], GlobalVar.gpx, GlobalVar.gpy, True)
                # armatura
                armaturaw = GlobalVar.loadImage("Immagini/EquipSara/Armature/Armatura%iw.png" % dati[8], GlobalVar.gpx, GlobalVar.gpy, True)
                armaturaa = GlobalVar.loadImage("Immagini/EquipSara/Armature/Armatura%ia.png" % dati[8], GlobalVar.gpx, GlobalVar.gpy, True)
                armaturas = GlobalVar.loadImage("Immagini/EquipSara/Armature/Armatura%is.png" % dati[8], GlobalVar.gpx, GlobalVar.gpy, True)
                armaturad = GlobalVar.loadImage("Immagini/EquipSara/Armature/Armatura%id.png" % dati[8], GlobalVar.gpx, GlobalVar.gpy, True)
                # scudo
                scudow = GlobalVar.loadImage("Immagini/EquipSara/Scudi/Scudo%iw.png" % dati[7], GlobalVar.gpx, GlobalVar.gpy, True)
                scudoa = GlobalVar.loadImage("Immagini/EquipSara/Scudi/Scudo%ia.png" % dati[7], GlobalVar.gpx, GlobalVar.gpy, True)
                scudos = GlobalVar.loadImage("Immagini/EquipSara/Scudi/Scudo%is.png" % dati[7], GlobalVar.gpx, GlobalVar.gpy, True)
                scudod = GlobalVar.loadImage("Immagini/EquipSara/Scudi/Scudo%id.png" % dati[7], GlobalVar.gpx, GlobalVar.gpy, True)
                scudoDifesa = GlobalVar.loadImage("Immagini/EquipSara/Scudi/Scudo%iDifesa.png" % dati[7], GlobalVar.gpx, GlobalVar.gpy, True)
                # guanti
                guantiw = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%iw.png" % dati[129], GlobalVar.gpx, GlobalVar.gpy, True)
                guantiwMov1 = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%iwMov1.png" % dati[129], GlobalVar.gpx, GlobalVar.gpy, True)
                guantiwMov2 = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%iwMov2.png" % dati[129], GlobalVar.gpx, GlobalVar.gpy, True)
                guantia = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%ia.png" % dati[129], GlobalVar.gpx, GlobalVar.gpy, True)
                guantiaMov1 = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%iaMov1.png" % dati[129], GlobalVar.gpx, GlobalVar.gpy, True)
                guantiaMov2 = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%iaMov2.png" % dati[129], GlobalVar.gpx, GlobalVar.gpy, True)
                guantis = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%is.png" % dati[129], GlobalVar.gpx, GlobalVar.gpy, True)
                guantisMov1 = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%isMov1.png" % dati[129], GlobalVar.gpx, GlobalVar.gpy, True)
                guantisMov2 = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%isMov2.png" % dati[129], GlobalVar.gpx, GlobalVar.gpy, True)
                guantid = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%id.png" % dati[129], GlobalVar.gpx, GlobalVar.gpy, True)
                guantidMov1 = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%idMov1.png" % dati[129], GlobalVar.gpx, GlobalVar.gpy, True)
                guantidMov2 = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%idMov2.png" % dati[129], GlobalVar.gpx, GlobalVar.gpy, True)
                guantisAttacco = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%isAttacco.png" % dati[129], GlobalVar.gpx, GlobalVar.gpy, True)
                guantiaAttacco = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%iaAttacco.png" % dati[129], GlobalVar.gpx, GlobalVar.gpy, True)
                guantidAttacco = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%idAttacco.png" % dati[129], GlobalVar.gpx, GlobalVar.gpy, True)
                guantiwAttacco = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%iwAttacco.png" % dati[129], GlobalVar.gpx, GlobalVar.gpy, True)
                guantiDifesa = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%iDifesa.png" % dati[129], GlobalVar.gpx, GlobalVar.gpy, True)
                # collana
                collanaw = GlobalVar.loadImage("Immagini/EquipSara/Collane/Collana%iw.png" % dati[130], GlobalVar.gpx, GlobalVar.gpy, True)
                collanaa = GlobalVar.loadImage("Immagini/EquipSara/Collane/Collana%ia.png" % dati[130], GlobalVar.gpx, GlobalVar.gpy, True)
                collanas = GlobalVar.loadImage("Immagini/EquipSara/Collane/Collana%is.png" % dati[130], GlobalVar.gpx, GlobalVar.gpy, True)
                collanad = GlobalVar.loadImage("Immagini/EquipSara/Collane/Collana%id.png" % dati[130], GlobalVar.gpx, GlobalVar.gpy, True)
                # armatura robot
                armrobw = GlobalVar.loadImage("Immagini/EquipRobo/Batteria%iw.png" % dati[9], GlobalVar.gpx, GlobalVar.gpy, True)
                armroba = GlobalVar.loadImage("Immagini/EquipRobo/Batteria%ia.png" % dati[9], GlobalVar.gpx, GlobalVar.gpy, True)
                armrobs = GlobalVar.loadImage("Immagini/EquipRobo/Batteria%is.png" % dati[9], GlobalVar.gpx, GlobalVar.gpy, True)
                armrobd = GlobalVar.loadImage("Immagini/EquipRobo/Batteria%id.png" % dati[9], GlobalVar.gpx, GlobalVar.gpy, True)
            if npers == 3:
                pers = GlobalVar.persw
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
                pers = GlobalVar.persa
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
                pers = GlobalVar.perss
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
                pers = GlobalVar.persd
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
                    robot = GlobalVar.robod
                    armrob = armrobd
                if nrob == 2:
                    robot = GlobalVar.roboa
                    armrob = armroba
                if nrob == 3:
                    robot = GlobalVar.robos
                    armrob = armrobs
                if nrob == 4:
                    robot = GlobalVar.robow
                    armrob = armrobw

            # aggiorno inCasellaVista di nemici e personaggi
            listaNemici, listaPersonaggi = aggiornaInCasellaVistaDiNemiciEPersonaggi(caseviste, listaNemici, listaPersonaggi)
            # aggiorno il campo attaccabile di colco
            if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] and rx == GlobalVar.gsx and ry == GlobalVar.gsy:
                rx = x
                ry = y
                vrx = rx
                vry = ry
            if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
                caselleAttaccabiliColco = trovacasattaccabili(rx, ry, GlobalVar.vistaRobo * GlobalVar.gpx, caseviste)
                posizioneColcoAggiornamentoCaseAttac = [rx, ry]
            # faccio il primo aggiornamento delle caselle attaccabili dei nemici (lo faccio perché queste caselle non vengono aggiornate finché il nemico non si sposta almeno una volta)
            for nemico in listaNemici:
                if inizio:
                    nemico.settaObbiettivoDalSalvataggio(x, y, rx, ry, vettoreEsche, vettoreDenaro, listaNemici, listaPersonaggi, dati, caseviste)
                if nemico.vita > 0 and nemico.inCasellaVista:
                    nemico.aggiornaVista(x, y, rx, ry, dati, caseviste, True)

            if dati[1] in GlobalVar.vetStanzePacifiche:
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
                GlobalVar.vetDatiSalvataggioGameOver = [dati[:], tutteporte[:], tutticofanetti[:], copy.deepcopy(listaNemiciTotali), vettoreEsche[:], vettoreDenaro[:], stanzeGiaVisitate[:], copy.deepcopy(listaPersonaggiTotali), oggettiRimastiASam[:], ultimoObbiettivoColco[:], copy.deepcopy(obbiettivoCasualeColco)]

            caricaTutto = True
            carim = False

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
                robot = GlobalVar.robos
                armrob = armrobs
            inizio = False

        inquadratoQualcosa = False
        xMouse, yMouse = pygame.mouse.get_pos()
        if GlobalVar.mouseVisibile:
            # controlle se il cursore è sul pers in basso a sinistra / nemico in alto a sinistra / telecolco / personaggio / porta / cofanetto / casella vista
            if GlobalVar.gsy // 18 * 17 <= yMouse <= GlobalVar.gsy and GlobalVar.gsx // 32 * 0 <= xMouse <= GlobalVar.gsx // 32 * 6:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                inquadratoQualcosa = "start"
            elif ((type(nemicoInquadrato) is str and nemicoInquadrato == "Colco") or (not nemicoInquadrato and dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"])) and 0 <= yMouse <= GlobalVar.gsy // 18 * 1 and GlobalVar.gsx // 32 * 0 <= xMouse <= GlobalVar.gsx // 32 * 4:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and 0 <= yMouse <= GlobalVar.gsy // 18 * 1 and GlobalVar.gsx // 32 * 0 <= xMouse <= GlobalVar.gsx // 32 * 1:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif nemicoInquadrato and not type(nemicoInquadrato) is str and 0 <= yMouse <= GlobalVar.gsy // 18 * 1 and GlobalVar.gsx // 32 * 0 <= xMouse <= GlobalVar.gsx // 32 * 3:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] and 0 <= yMouse <= GlobalVar.gsy // 18 * 1.5 and GlobalVar.gsx // 32 * 27.8 < xMouse <= GlobalVar.gsx // 32 * 30.2:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                inquadratoQualcosa = "telecolco"
            else:
                if not inquadratoQualcosa:
                    i = 0
                    for personaggio in listaPersonaggi:
                        if personaggio.x <= xMouse <= personaggio.x + GlobalVar.gpx and personaggio.y <= yMouse <= personaggio.y + GlobalVar.gpy:
                            if (personaggio.x == x + GlobalVar.gpx and personaggio.y == y) or (personaggio.x == x - GlobalVar.gpx and personaggio.y == y) or (personaggio.x == x and personaggio.y == y + GlobalVar.gpy) or (personaggio.x == x and personaggio.y == y - GlobalVar.gpy):
                                if GlobalVar.mouseBloccato:
                                    GlobalVar.configuraCursore(False)
                                inquadratoQualcosa = "personaggio:" + str(i)
                            break
                        i += 1
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(porte):
                        if porte[i + 1] <= xMouse <= porte[i + 1] + GlobalVar.gpx and porte[i + 2] <= yMouse <= porte[i + 2] + GlobalVar.gpy and not porte[i + 3]:
                            if ((porte[i + 1] == x + GlobalVar.gpx and porte[i + 2] == y) or (porte[i + 1] == x - GlobalVar.gpx and porte[i + 2] == y) or (porte[i + 1] == x and porte[i + 2] == y + GlobalVar.gpy) or (porte[i + 1] == x and porte[i + 2] == y - GlobalVar.gpy)) and not porte[i + 3]:
                                if GlobalVar.mouseBloccato:
                                    GlobalVar.configuraCursore(False)
                                inquadratoQualcosa = "porta:" + str(i)
                            break
                        i += 4
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(cofanetti):
                        if cofanetti[i + 1] <= xMouse <= cofanetti[i + 1] + GlobalVar.gpx and cofanetti[i + 2] <= yMouse <= cofanetti[i + 2] + GlobalVar.gpy and not cofanetti[i + 3]:
                            if ((cofanetti[i + 1] == x + GlobalVar.gpx and cofanetti[i + 2] == y) or (cofanetti[i + 1] == x - GlobalVar.gpx and cofanetti[i + 2] == y) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y + GlobalVar.gpy) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y - GlobalVar.gpy)) and not cofanetti[i + 3]:
                                if GlobalVar.mouseBloccato:
                                    GlobalVar.configuraCursore(False)
                                inquadratoQualcosa = "cofanetto:" + str(i)
                            break
                        i += 4
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(casevisteEntrateIncluse):
                        if casevisteEntrateIncluse[i] <= xMouse <= casevisteEntrateIncluse[i] + GlobalVar.gpx and casevisteEntrateIncluse[i + 1] <= yMouse <= casevisteEntrateIncluse[i + 1] + GlobalVar.gpy:
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
                                    if GlobalVar.mouseBloccato:
                                        GlobalVar.configuraCursore(False)
                                    inquadratoQualcosa = "movimento:" + str(casevisteEntrateIncluse[i]) + ":" + str(casevisteEntrateIncluse[i + 1])
                            break
                        i += 3
        if not inquadratoQualcosa and GlobalVar.mouseVisibile:
            if not GlobalVar.mouseBloccato:
                GlobalVar.configuraCursore(True)

        # controllo se ci sono nemici in movimento per decidere se fare altre animazioni o no
        nemiciInMovimento = False
        for nemico in listaNemici:
            if nemico.mosseRimaste > 0:
                nemiciInMovimento = True
                break

        # gestione degli input
        if not impossibileCliccarePulsanti and mosseRimasteRob <= 0 and not nemiciInMovimento and not startf and not oggettoRicevuto:
            bottoneDown, aggiornaInterfacciaPerCambioInput = getInput(bottoneDown, False)
        else:
            bottoneDown = False
            pygame.event.pump()
        if not bottoneDown:
            GlobalVar.canaleSoundPassiRallo.stop()
            nx = 0
            ny = 0
        movimentoPerMouse = False
        # movimenti personaggio
        if bottoneDown == pygame.K_w or bottoneDown == "padSu":
            refreshSchermo = True
            npers = 3
            pers = GlobalVar.persw
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
            ny = -GlobalVar.gpy
            nx = 0
        if bottoneDown == pygame.K_a or bottoneDown == "padSinistra":
            refreshSchermo = True
            npers = 2
            pers = GlobalVar.persa
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
            nx = -GlobalVar.gpx
            ny = 0
        if bottoneDown == pygame.K_s or bottoneDown == "padGiu":
            refreshSchermo = True
            npers = 4
            pers = GlobalVar.perss
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
            ny = GlobalVar.gpy
            nx = 0
        if bottoneDown == pygame.K_d or bottoneDown == "padDestra":
            refreshSchermo = True
            npers = 1
            pers = GlobalVar.persd
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
            nx = GlobalVar.gpx
            ny = 0
        # vado in mod. interazione
        if bottoneDown == pygame.K_e or bottoneDown == "padQuadrato":
            GlobalVar.canaleSoundPassiRallo.stop()
            nx = 0
            ny = 0
            GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
            attacco = 1
            bottoneDown = False
        # tolgo l'obbiettivo se presente
        if bottoneDown == pygame.K_q or bottoneDown == "padCerchio":
            GlobalVar.canaleSoundPassiRallo.stop()
            nx = 0
            ny = 0
            if nemicoInquadrato:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                nemicoInquadrato = False
                caricaTutto = True
            else:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
            bottoneDown = False
        # attivo / disattivo gambit di Colco
        if bottoneDown == pygame.K_LSHIFT or bottoneDown == pygame.K_RSHIFT or bottoneDown == "padTriangolo":
            GlobalVar.canaleSoundPassiRallo.stop()
            nx = 0
            ny = 0
            if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
                GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoTeleColco)
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
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
            bottoneDown = False
        # scorro la selezione dell'obbiettivo
        if bottoneDown == pygame.K_3 or bottoneDown == pygame.K_KP3 or bottoneDown == "padR1":
            GlobalVar.canaleSoundPassiRallo.stop()
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
            nemicoInquadrato = scorriObbiettiviInquadrati(dati[0], nemicoInquadrato, listaNemiciVisti, listaEscheViste, True)
            caricaTutto = True
            bottoneDown = False
        if bottoneDown == pygame.K_2 or bottoneDown == pygame.K_KP2 or bottoneDown == "padL1":
            GlobalVar.canaleSoundPassiRallo.stop()
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
            nemicoInquadrato = scorriObbiettiviInquadrati(dati[0], nemicoInquadrato, listaNemiciVisti, listaEscheViste, False)
            caricaTutto = True
            bottoneDown = False
        # interagisco
        if bottoneDown == pygame.K_SPACE or bottoneDown == "padCroce":
            GlobalVar.canaleSoundPassiRallo.stop()
            nx = 0
            ny = 0
            # apertura porte
            k = 0
            while k < len(porte):
                if porte[k] == dati[1] and not porte[k + 3] and ((porte[k + 1] == x + GlobalVar.gpx and porte[k + 2] == y and npers == 1) or (porte[k + 1] == x - GlobalVar.gpx and porte[k + 2] == y and npers == 2) or (porte[k + 1] == x and porte[k + 2] == y + GlobalVar.gpy and npers == 4) or (porte[k + 1] == x and porte[k + 2] == y - GlobalVar.gpy and npers == 3)):
                    if possibileAprirePorta(dati[1], porte[k + 1], porte[k + 2], dati[0]):
                        sposta = True
                        GlobalVar.canaleSoundInterazioni.play(rumoreAperturaPorte)
                        porte[k + 3] = True
                        caseviste, casevisteDaRallo, casevisteEntrateIncluse, casellePercorribili = creaTuttiIVettoriPerLeCaselleViste(x, y, rx, ry, dati[1], porte, cofanetti)
                        caricaTutto = True
                        # aggiornare vettore tutteporte
                        j = 0
                        while j < len(tutteporte):
                            if tutteporte[j] == porte[k] and tutteporte[j + 1] == porte[k + 1] and tutteporte[j + 2] == porte[k + 2]:
                                tutteporte[j + 3] = True
                                break
                            j = j + 4
                        # aggiorno inCasellaVista di nemici e personaggi
                        listaNemici, listaPersonaggi = aggiornaInCasellaVistaDiNemiciEPersonaggi(caseviste, listaNemici, listaPersonaggi)
                        # aggiorno il campo attaccabile di colco
                        if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
                            caselleAttaccabiliColco = trovacasattaccabili(rx, ry, GlobalVar.vistaRobo * GlobalVar.gpx, caseviste)
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
                        (cofanetti[i + 1] == x + GlobalVar.gpx and cofanetti[i + 2] == y and npers == 1) or (
                        cofanetti[i + 1] == x - GlobalVar.gpx and cofanetti[i + 2] == y and npers == 2) or (
                                cofanetti[i + 1] == x and cofanetti[i + 2] == y + GlobalVar.gpy and npers == 4) or (
                                cofanetti[i + 1] == x and cofanetti[i + 2] == y - GlobalVar.gpy and npers == 3)) and not \
                cofanetti[i + 3]:
                    GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoaperturacofanetti)
                    sposta = True
                    dati, tesoro, dati[0] = aperturacofanetto(cofanetti[i], cofanetti[i + 1], cofanetti[i + 2], dati)
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
                if (personaggio.x == x + GlobalVar.gpx and personaggio.y == y and npers == 1) or (personaggio.x == x - GlobalVar.gpx and personaggio.y == y and npers == 2) or (personaggio.x == x and personaggio.y == y + GlobalVar.gpy and npers == 4) or (personaggio.x == x and personaggio.y == y - GlobalVar.gpy and npers == 3):
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                    sposta = True
                    if npers == 1:
                        personaggio.girati("a")
                    elif npers == 2:
                        personaggio.girati("d")
                    elif npers == 3:
                        personaggio.girati("s")
                    elif npers == 4:
                        personaggio.girati("w")
                    disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, casellaChiara, casellaScura, casellaOscurata, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, dati[0])
                    dati[0], oggettoRicevuto, visualizzaMenuMercante = dialoga(dati[0], personaggio)
                    caricaTutto = True
            if not sposta:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
            bottoneDown = False
        # apro il menu
        if bottoneDown == pygame.K_ESCAPE or bottoneDown == "mouseCentrale" or bottoneDown == "padStart":
            GlobalVar.canaleSoundPassiRallo.stop()
            nx = 0
            ny = 0
            startf = True
            bottoneDown = False
        # comandi mouse
        if bottoneDown == "mouseDestro":
            GlobalVar.canaleSoundPassiRallo.stop()
            nx = 0
            ny = 0
            if inquadratoQualcosa == "battaglia" and nemicoInquadrato:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                nemicoInquadrato = False
                caricaTutto = True
            else:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                attacco = 1
            bottoneDown = False
        if bottoneDown == "mouseSinistro" and not GlobalVar.mouseBloccato:
            if inquadratoQualcosa == "start":
                GlobalVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                startf = True
                bottoneDown = False
            elif inquadratoQualcosa == "battaglia":
                GlobalVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                attacco = 1
                bottoneDown = False
            elif inquadratoQualcosa == "telecolco":
                GlobalVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoTeleColco)
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
                GlobalVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                inquadratoQualcosaList = inquadratoQualcosa.split(":")
                posizPortaInVettore = int(inquadratoQualcosaList[1])
                if possibileAprirePorta(dati[1], porte[posizPortaInVettore + 1], porte[posizPortaInVettore + 2], dati[0]):
                    sposta = True
                    GlobalVar.canaleSoundInterazioni.play(rumoreAperturaPorte)
                    porte[posizPortaInVettore + 3] = True
                    caseviste, casevisteDaRallo, casevisteEntrateIncluse, casellePercorribili = creaTuttiIVettoriPerLeCaselleViste(x, y, rx, ry, dati[1], porte, cofanetti)
                    caricaTutto = True
                    # aggiornare vettore tutteporte
                    j = 0
                    while j < len(tutteporte):
                        if tutteporte[j] == porte[posizPortaInVettore] and tutteporte[j + 1] == porte[posizPortaInVettore + 1] and tutteporte[j + 2] == porte[posizPortaInVettore + 2]:
                            tutteporte[j + 3] = True
                            break
                        j += 4
                    # aggiorno inCasellaVista di nemici e personaggi
                    listaNemici, listaPersonaggi = aggiornaInCasellaVistaDiNemiciEPersonaggi(caseviste, listaNemici, listaPersonaggi)
                    # aggiorno il campo attaccabile di colco
                    if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
                        caselleAttaccabiliColco = trovacasattaccabili(rx, ry, GlobalVar.vistaRobo * GlobalVar.gpx, caseviste)
                        posizioneColcoAggiornamentoCaseAttac = [rx, ry]
                    # aggiorno la vista dei nemici
                    for nemico in listaNemici:
                        if nemico.vita > 0 and nemico.inCasellaVista:
                            nemico.aggiornaVista(x, y, rx, ry, dati, caseviste, True)
                else:
                    impossibileAprirePorta = True
                    caricaTutto = True
                # giro il pers verso la porta
                if porte[posizPortaInVettore + 1] == x + GlobalVar.gpx and porte[posizPortaInVettore + 2] == y:
                    npers = 1
                if porte[posizPortaInVettore + 1] == x - GlobalVar.gpx and porte[posizPortaInVettore + 2] == y:
                    npers = 2
                if porte[posizPortaInVettore + 1] == x and porte[posizPortaInVettore + 2] == y + GlobalVar.gpy:
                    npers = 4
                if porte[posizPortaInVettore + 1] == x and porte[posizPortaInVettore + 2] == y - GlobalVar.gpy:
                    npers = 3
                if npers == 3:
                    pers = GlobalVar.persw
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
                    pers = GlobalVar.persa
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
                    pers = GlobalVar.perss
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
                    pers = GlobalVar.persd
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
            elif inquadratoQualcosa and inquadratoQualcosa.startswith("cofanetto"):
                GlobalVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                inquadratoQualcosaList = inquadratoQualcosa.split(":")
                posizCofanettoInVettore = int(inquadratoQualcosaList[1])
                sposta = True
                GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoaperturacofanetti)
                dati, tesoro, dati[0] = aperturacofanetto(cofanetti[posizCofanettoInVettore], cofanetti[posizCofanettoInVettore + 1], cofanetti[posizCofanettoInVettore + 2], dati)
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
                if cofanetti[posizCofanettoInVettore + 1] == x + GlobalVar.gpx and cofanetti[posizCofanettoInVettore + 2] == y:
                    npers = 1
                if cofanetti[posizCofanettoInVettore + 1] == x - GlobalVar.gpx and cofanetti[posizCofanettoInVettore + 2] == y:
                    npers = 2
                if cofanetti[posizCofanettoInVettore + 1] == x and cofanetti[posizCofanettoInVettore + 2] == y + GlobalVar.gpy:
                    npers = 4
                if cofanetti[posizCofanettoInVettore + 1] == x and cofanetti[posizCofanettoInVettore + 2] == y - GlobalVar.gpy:
                    npers = 3
                if npers == 3:
                    pers = GlobalVar.persw
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
                    pers = GlobalVar.persa
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
                    pers = GlobalVar.perss
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
                    pers = GlobalVar.persd
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
                GlobalVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                inquadratoQualcosaList = inquadratoQualcosa.split(":")
                posizPersonaggioInVettore = int(inquadratoQualcosaList[1])
                personaggio = listaPersonaggi[posizPersonaggioInVettore]
                sposta = True
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                # giro Rallo verso il personaggio e viceversa
                if personaggio.x == x + GlobalVar.gpx and personaggio.y == y:
                    npers = 1
                if personaggio.x == x - GlobalVar.gpx and personaggio.y == y:
                    npers = 2
                if personaggio.x == x and personaggio.y == y + GlobalVar.gpy:
                    npers = 4
                if personaggio.x == x and personaggio.y == y - GlobalVar.gpy:
                    npers = 3
                if npers == 3:
                    pers = GlobalVar.persw
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
                    pers = GlobalVar.persa
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
                    pers = GlobalVar.perss
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
                    pers = GlobalVar.persd
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
                disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, casellaChiara, casellaScura, casellaOscurata, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, dati[0])
                dati[0], oggettoRicevuto, visualizzaMenuMercante = dialoga(dati[0], personaggio)
                caricaTutto = True
                bottoneDown = False
            elif inquadratoQualcosa and inquadratoQualcosa.startswith("movimento"):
                movimentoPerMouse = True
        elif bottoneDown == "mouseSinistro" and GlobalVar.mouseBloccato:
            GlobalVar.canaleSoundPassiRallo.stop()
            nx = 0
            ny = 0
            GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
            bottoneDown = False

        impossibileCliccarePulsanti = False
        # statistiche personaggio e robo
        esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati, difesa)

        # resetta stati/pv al campio personaggio
        if dati[0] == GlobalVar.dictAvanzamentoStoria["primoCambioPersonaggio"] or dati[0] == GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
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
                if abs(xObbiettivo - x) == GlobalVar.gpx and abs(yObbiettivo - y) == 0:
                    if x < xObbiettivo:
                        npers = 1
                    if x > xObbiettivo:
                        npers = 2
                    sposta = True
                elif abs(yObbiettivo - y) == GlobalVar.gpy and abs(xObbiettivo - x) == 0:
                    if y < yObbiettivo:
                        npers = 4
                    if y > yObbiettivo:
                        npers = 3
                    sposta = True
                else:
                    percorsoTrovato = pathFinding(x, y, xObbiettivo, yObbiettivo, vetNemiciSoloConXeY, casevisteEntrateIncluse)
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
                        ny = -GlobalVar.gpy
                        nx = 0
                        pers = GlobalVar.persw
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
                        nx = -GlobalVar.gpx
                        pers = GlobalVar.persa
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
                        ny = GlobalVar.gpy
                        nx = 0
                        pers = GlobalVar.perss
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
                        nx = GlobalVar.gpx
                        pers = GlobalVar.persd
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
                GlobalVar.canaleSoundPassiRallo.stop()

        # menu start
        if startf and attacco != 1:
            GlobalVar.canaleSoundInterazioni.play(GlobalVar.selsta)
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
                dati, inizio, attacco, caricaSalvataggio = start(dati, porteini, portefin, cofaniini, cofanifin, tutteporte, tutticofanetti, listaNemiciTotali, vettoreEsche, vettoreDenaro, stanzeGiaVisitate, listaPersonaggiTotali, oggettiRimastiASam, ultimoObbiettivoColco, obbiettivoCasualeColco, colcoInCasellaVista)
                if caricaSalvataggio:
                    inizio = True
                if attacco == 0:
                    uscitoDaMenu = 2
            else:
                dati, attacco, sposta, animaOggetto, npers, inizio = startBattaglia(dati, animaOggetto, x, y, npers, rx, ry, inizio)
                # cambiare posizione dopo l'uso di caricabatterie
                if npers == 3:
                    pers = GlobalVar.persw
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
                    pers = GlobalVar.persa
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
                    pers = GlobalVar.perss
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
                    pers = GlobalVar.persd
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
        inizio, gameover = controllaMorteRallo(dati[5], inizio, gameover)
        morterob, dati, mosseRimasteRob = controllaMorteColco(dati, mosseRimasteRob)

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
                disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, casellaChiara, casellaScura, casellaOscurata, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, dati[0])
                animaOggettoSpecialeRicevuto(oggettoRicevuto)
                oggettoRicevuto = False
                caricaTutto = True

            # movimento-azioni personaggio
            if (nx != 0 or ny != 0) and not nemiciInMovimento and mosseRimasteRob <= 0:
                vx = x
                vy = y
                stanzaVecchia = dati[1]
                x, y, dati[1], carim, cambiosta = controlloOstacoli(x, y, nx, ny, dati[1], carim, False, porte, cofanetti)

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
                    GlobalVar.canaleSoundPassiRallo.stop()
            # gestione attacchi
            attaccoADistanza = False
            # attaccoDiRallo [obbiettivo, danno, status(avvelena, appiccica) ... => per ogni nemico colpito]
            attaccoDiRallo = []
            if attacco != 0:
                sposta, creaesca, xesca, yesca, npers, nrob, dati[5], dati[121], dati[10], difesa, apriChiudiPorta, apriCofanetto, listaNemici, attacco, attaccoADistanza, nemicoInquadrato, attaccoDiRallo, chiamarob, ultimoObbiettivoColco, animaOggetto, interagisciConPersonaggio, startf, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac = attacca(dati, x, y, vx, vy, npers, nrob, rx, ry, obbiettivoCasualeColco, pers, dati[5], pvtot, dif, dati[121], dati[130], dati[123], dati[124], dati[10], entot, difro, dati[122], dati[125], dati[126], imgSfondoStanza, casellaChiara, casellaScura, casellaOscurata, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, attVicino, attLontano, attacco, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, vettoreDenaro, dati[132], nemicoInquadrato, raffredda, autoRic1, autoRic2, ultimoObbiettivoColco, animaOggetto, listaPersonaggi, startf, dati[0], casellePercorribili, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, mosseRimasteRob)
                refreshSchermo = True
                caricaTutto = True
                # cancello apertura porta se non si può aprire
                if apriChiudiPorta[0] and not possibileAprirePorta(dati[1], apriChiudiPorta[1], apriChiudiPorta[2], dati[0]):
                    apriChiudiPorta = [False, 0, 0]
                    sposta = False
                    impossibileAprirePorta = True
                # tolgo una freccia se uso l'attacco a distanza
                if attaccoADistanza:
                    dati[132] -= 1
                # cambiare posizione dopo l'attacco
                if npers == 3:
                    pers = GlobalVar.persw
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
                    pers = GlobalVar.persa
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
                    pers = GlobalVar.perss
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
                    pers = GlobalVar.persd
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
            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati, difesa)
            if difesa == 2 and not sposta:
                difesa = 1
                sposta = True
                dati[5] = dati[5] + 3
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
            if dati[130] == 2 and sposta:
                dati[5] = dati[5] + 1
                if dati[5] > pvtot:
                    dati[5] = pvtot
            # apertura/chiusura porte
            if apriChiudiPorta[0]:
                k = 0
                while k < len(porte):
                    if porte[k] == dati[1] and porte[k + 1] == apriChiudiPorta[1] and porte[k + 2] == apriChiudiPorta[2]:
                        if porte[k + 3]:
                            GlobalVar.canaleSoundInterazioni.play(rumoreChiusuraPorte)
                            porte[k + 3] = False
                        else:
                            GlobalVar.canaleSoundInterazioni.play(rumoreAperturaPorte)
                            porte[k + 3] = True
                        caseviste, casevisteDaRallo, casevisteEntrateIncluse, casellePercorribili = creaTuttiIVettoriPerLeCaselleViste(x, y, rx, ry, dati[1], porte, cofanetti)
                        # aggiornare vettore tutteporte
                        j = 0
                        while j < len(tutteporte):
                            if tutteporte[j] == porte[k] and tutteporte[j + 1] == porte[k + 1] and tutteporte[j + 2] == porte[k + 2]:
                                tutteporte[j + 3] = porte[k + 3]
                                break
                            j = j + 4
                        # aggiorno inCasellaVista di nemici e personaggi
                        listaNemici, listaPersonaggi = aggiornaInCasellaVistaDiNemiciEPersonaggi(caseviste, listaNemici, listaPersonaggi)
                        # aggiorno il campo attaccabile di colco
                        if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
                            caselleAttaccabiliColco = trovacasattaccabili(rx, ry, GlobalVar.vistaRobo * GlobalVar.gpx, caseviste)
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
                    if (personaggio.x == x + GlobalVar.gpx and personaggio.y == y and npers == 1) or (personaggio.x == x - GlobalVar.gpx and personaggio.y == y and npers == 2) or (personaggio.x == x and personaggio.y == y + GlobalVar.gpy and npers == 4) or (personaggio.x == x and personaggio.y == y - GlobalVar.gpy and npers == 3):
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                        if npers == 1:
                            personaggio.girati("a")
                        elif npers == 2:
                            personaggio.girati("d")
                        elif npers == 3:
                            personaggio.girati("s")
                        elif npers == 4:
                            personaggio.girati("w")
                        # aggiorno lo GlobalVarG2.schermo (serve per girare i pers uno verso l'altro e per togliere il campo visivo dell'obiettivo selezionato)
                        disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, casellaChiara, casellaScura, casellaOscurata, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, dati[0])
                        dati[0], oggettoRicevuto, visualizzaMenuMercante = dialoga(dati[0], personaggio)
                        caricaTutto = True
                interagisciConPersonaggio = False
            # menu mercante
            if visualizzaMenuMercante:
                dati = menuMercante(dati)
                visualizzaMenuMercante = False
                uscitoDaMenu = 2
                carim = True
            # apertura cofanetti
            if apriCofanetto[0]:
                i = 0
                while i < len(cofanetti):
                    if cofanetti[i] == dati[1] and cofanetti[i + 1] == apriCofanetto[1] and cofanetti[i + 2] == apriCofanetto[2] and not cofanetti[i + 3]:
                        GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoaperturacofanetti)
                        dati, tesoro, dati[0] = aperturacofanetto(cofanetti[i], cofanetti[i + 1], cofanetti[i + 2], dati)
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
                    caselleAttaccabiliColco = trovacasattaccabili(rx, ry, GlobalVar.vistaRobo * GlobalVar.gpx, caseviste)
                    posizioneColcoAggiornamentoCaseAttac = [rx, ry]
                spingiColco = False
            # aggiorna la posizione del telecolco se è attivo
            if chiamarob:
                ultimoObbiettivoColco = []
                ultimoObbiettivoColco.append("Telecomando")
                ultimoObbiettivoColco.append(x)
                ultimoObbiettivoColco.append(y)

            # impedisce di andare avanti quando si vuole andare in una zona non ancora sbloccata
            if cambiosta and nonPuoiProcedere(dati[0], x, y, stanzaVecchia, dati[1]):
                cambiosta = False
                dati[1] = stanzaVecchia
                x = vx
                y = vy
                sposta = False
                caricaTutto = True
                bottoneDown = False

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
                    GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoRaccoltaEsca)
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
            if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] and dati[122] > 0 and (dati[125] > 0 or dati[126] > 0):
                # se surriscaldato toglie vel+ e efficienza
                dati[125] = 0
                dati[126] = 0
                refreshSchermo = True
            if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] and sposta and mosseRimasteRob == 0 and not morterob:
                if dati[125] > 0:
                    mosseRimasteRob = 2
                else:
                    mosseRimasteRob = 1
            # effetto di surriscalda / raffreddamento / auto-ricarica / auto-ricarica+
            if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] and sposta:
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
                    dati[10] += GlobalVar.dannoTecniche[6]
                    if dati[10] > entot:
                        dati[10] = entot
                    dati[122] = 10
                # autoric+
                if autoRic2 >= 0:
                    ricarica2 = False
                    autoRic2 -= 1
                if autoRic2 == 0:
                    dati[10] += GlobalVar.dannoTecniche[16]
                    if dati[10] > entot:
                        dati[10] = entot
                    dati[122] = 10
            listaNemiciAttaccatiADistanzaRobo = False
            # attaccoDiColco [obbiettivo, danno, status (antidoto, attP, difP, velocizza, efficienza) ... => per ogni nemico colpito (non raffredda perchè deve rimanere per più turni)]
            attaccoDiColco = []
            tecnicaUsata = False
            if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] and mosseRimasteRob > 0 and not morterob and not cambiosta:
                vrx = rx
                vry = ry

                # movimento - gambit
                if raffredda < 0 and autoRic1 < 0 and autoRic2 < 0:
                    rx, ry, nrob, dati, listaNemici, raffreddamento, ricarica1, ricarica2, azioneRobEseguita, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, attaccoDiColco, ultimoObbiettivoColco, obbiettivoCasualeColco, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, vettoreEsche = movrobo(x, y, vx, vy, rx, ry, chiamarob, dati, porte, listaNemici, difesa, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggi, caseviste, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, vettoreEsche, analizzaColco=False)

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
                        robot = GlobalVar.robod
                        armrob = armrobd
                    if nrob == 2:
                        robot = GlobalVar.roboa
                        armrob = armroba
                    if nrob == 3:
                        robot = GlobalVar.robos
                        armrob = armrobs
                    if nrob == 4:
                        robot = GlobalVar.robow
                        armrob = armrobw
                if (rx != vrx or ry != vry) and not chiamarob:
                    caselleAttaccabiliColco = trovacasattaccabili(rx, ry, GlobalVar.vistaRobo * GlobalVar.gpx, caseviste)
                    posizioneColcoAggiornamentoCaseAttac = [rx, ry]
            elif dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] and sposta and mosseRimasteRob < 0 and not morterob:
                mosseRimasteRob += 1
            if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] and morterob:
                robot = GlobalVar.robomo
                armrob = GlobalVar.armrobmo
            if dati[0] < GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
                rx = GlobalVar.gsx
                ry = GlobalVar.gsy
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
                                vetDatiNemici.append(nemicoTemp.vita)
                                vetDatiNemici.append(nemicoTemp.x)
                                vetDatiNemici.append(nemicoTemp.y)
                                vetDatiNemici.append(nemicoTemp.vitaTotale)
                            # trovo l'obbiettivo
                            nemico.settaObbiettivo(x, y, rx, ry, dati, vettoreDenaro, vettoreEsche, listaPersonaggi, listaNemici, porte, caseviste)
                            nemico.vx = nemico.x
                            nemico.vy = nemico.y
                            nemico, direzioneMostro, dati, vettoreEsche = movmostro(x, y, rx, ry, nemico, dif, difro, par, dati, vettoreEsche, vetDatiNemici, listaPersonaggi, caseviste, dati[0])
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
                            if (nemico.x == x and nemico.y == y) or (nemico.x == rx and nemico.y == ry):
                                nemico.x = nemico.vx
                                nemico.y = nemico.vy
                                nemico.animaSpostamento = False
                            if nemico.animaSpostamento:
                                if nemico.numeroMovimento < len(nemico.percorso) - 1:
                                    nemico.numeroMovimento += 1
                                else:
                                    nemico.numeroMovimento = 0
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
                        personaggio.spostati(x, y, rx, ry, listaNemici, caseviste)

            # aumentare di livello
            while dati[127] >= esptot and dati[4] < 100:
                dati[4] += 1
                dati[127] -= esptot
                aumentoliv += 1
                esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati, difesa)
                impossibileCliccarePulsanti = True

            # fai tutte le animazioni del turno e disegni gli sfondi e personaggi
            if caricaTutto:
                refreshSchermo = True
                if aumentoliv != 0:
                    pvtot = getVitaTotRallo(dati[4] - aumentoliv, dati[129])
                disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, casellaChiara, casellaScura, casellaOscurata, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, dati[0])
                caricaTutto = False
            if (azioneRobEseguita or nemiciInMovimento or sposta) and not uscitoDaMenu > 0:
                primopasso, caricaTutto, tesoro, bottoneDown, movimentoPerMouse, robot, armrob = anima(sposta, x, y, vx, vy, rx, ry, vrx, vry, pers, robot, npers, nrob, primopasso, cambiosta, casellaChiara, casellaScura, scudo, armatura, arma, armaMov1, armaMov2, armaAttacco, scudoDifesa, arco, faretra, arcoAttacco, guanti, guantiMov1, guantiMov2, guantiAttacco, guantiDifesa, collana, armas, armaturas, arcos, faretras, collanas, armrob, armrobs, dati, attacco, difesa, bottoneDown, tesoro, aumentoliv, caricaTutto, listaNemici, vettoreEsche, vettoreDenaro, attaccoADistanza, caseviste, porte, cofanetti, portaOriz, portaVert, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoInquadrato, attaccoDiRallo, attaccoDiColco, statoRalloInizioTurno, statoColcoInizioTurno, statoEscheInizioTurno, raffreddamento, ricarica1, ricarica2, raffredda, autoRic1, autoRic2, animaOggetto, listaPersonaggi, apriocchio, chiamarob, movimentoPerMouse, vettoreImgCaselle)
            if not carim and (refreshSchermo or azioneRobEseguita or nemiciInMovimento or sposta):
                refreshSchermo = False
                apriocchio = False
                for nemico in listaNemici:
                    if nemico.visto:
                        apriocchio = True
                        break
                pvtot = getVitaTotRallo(dati[4], dati[129])
                disegnaAmbiente(x, y, npers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, casellaChiara, casellaScura, casellaOscurata, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, False, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, dati[0])

            # gestisce eventi speciali come i dialoghi del tutorial o dialoghi con nessuno
            if not carim:
                dati[0], cambiosta, dati[1], npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaNemiciTotali, dati, oggettiRimastiASam, tutteporte = gestisciEventiStoria(dati[0], dati[1], npers, x, y, cambiosta, carim, caricaTutto, bottoneDown, movimentoPerMouse, impossibileAprirePorta, listaPersonaggi, listaNemici, listaNemiciTotali, dati, oggettiRimastiASam, tutteporte)
                impossibileAprirePorta = False

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

            # aggiorna i dialoghi e le img di tutti i personaggi / oggetti in base all'avanzamento nella storia
            for personaggio in listaPersonaggi:
                personaggio.aggiornaDialogo(dati[0])
                if personaggio.mantieniSempreASchermo:
                    imgAggiornata = personaggio.aggiornaImgOggetto(dati[0])
                    if imgAggiornata:
                        refreshSchermo = True

            # prendere il denaro da terra
            i = 0
            while i < len(vettoreDenaro):
                denaroPreso = False
                if vettoreDenaro[i + 1] == x and vettoreDenaro[i + 2] == y:
                    dati[131] = ottieniMonete(dati, vettoreDenaro[i])
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
                sprites = pygame.sprite.Group(Fade(0))
                schermoFadeToBlack = GlobalVar.schermo.copy().convert()
                oscuraIlluminaSchermo(sprites, schermoFadeToBlack)
            GlobalVar.canaleSoundPuntatore.stop()
            GlobalVar.canaleSoundPassiRallo.stop()
            GlobalVar.canaleSoundPassiColco.stop()
            GlobalVar.canaleSoundPassiNemiciPersonaggi.stop()
            GlobalVar.canaleSoundMorteNemici.stop()
            GlobalVar.canaleSoundLvUp.stop()
            GlobalVar.canaleSoundInterazioni.stop()
            GlobalVar.canaleSoundAttacco.stop()
            i = GlobalVar.volumeCanzoni / 2
            j = GlobalVar.volumeEffetti / 2
            while i > 0 and j > 0:
                GlobalVar.canaleSoundCanzone.set_volume(i)
                GlobalVar.canaleSoundSottofondoAmbientale.set_volume(j)
                i -= GlobalVar.volumeCanzoni / 10
                j -= GlobalVar.volumeEffetti / 10
                pygame.time.wait(30)
            GlobalVar.canaleSoundCanzone.stop()
            GlobalVar.canaleSoundCanzone.set_volume(GlobalVar.volumeCanzoni)
            GlobalVar.canaleSoundSottofondoAmbientale.stop()
            GlobalVar.canaleSoundSottofondoAmbientale.set_volume(GlobalVar.volumeEffetti)

gameloop()
