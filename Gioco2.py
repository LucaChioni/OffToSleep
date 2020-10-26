# -*- coding: utf-8 -*-

from Menu import *
from EnvPrint import *
from MovNemiciRob import *
from Animazioni import *
from SetNemiciPersonaggiEventi import *


def gameloop():
    caricaSalvataggio = False
    inizio = True
    while True:
        if inizio:
            impossibileAprirePorta = False
            canzoneCambiata = False
            canzone = False
            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
            movimentoPerMouse = False
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
            chiamarob = True
            tesoro = -1
            apriocchio = False
            sposta = False
            nmost = 0
            tastop = 0
            startf = False
            aumentoliv = 0
            primopasso = True
            contaesca = 0
            xesca = 0
            yesca = 0
            creaesca = False
            attacco = 0
            difesa = 0
            nx = 0
            ny = 0
            ultimoObbiettivoColco = []
            obbiettivoCasualeColco = False
            dati, porteini, portefin, cofaniini, cofanifin, listaNemiciTotali, vitaesca, vettoreDenaro, stanzeGiaVisitate, listaPersonaggiTotali = menu(caricaSalvataggio)
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
                movimentoPerMouse = False
                sprites = pygame.sprite.Group(Fade(0))
                schermoFadeToBlack = GlobalVar.schermo.copy()
                i = 0
                while i <= 6:
                    sprites.update()
                    GlobalVar.schermo.blit(schermoFadeToBlack, (0, 0))
                    sprites.draw(GlobalVar.schermo)
                    pygame.display.update()
                    GlobalVar.clockFadeToBlack.tick(GlobalVar.fpsFadeToBlack)
                    i += 1

                canzoneCambiata = False
                # mi posiziono e setto canzone e rumore porte
                x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, canzone = settaPosizioneERumoriStanza(x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata,dati[1], stanzaVecchia, canzone, inizio)
                if not inizio:
                    vx = x
                    vy = y
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

                if canzoneCambiata:
                    i = GlobalVar.volumeCanzoni
                    while i > 0:
                        GlobalVar.canaleSoundCanzone.set_volume(i)
                        i = i - (GlobalVar.volumeCanzoni / 10)
                        pygame.time.wait(30)
                    GlobalVar.canaleSoundCanzone.stop()
                    GlobalVar.canaleSoundCanzone.set_volume(GlobalVar.volumeCanzoni)
                    if canzone:
                        GlobalVar.canaleSoundCanzone.play(canzone)

                # carico nemici e personaggi nella stanza
                nmost, listaNemici, listaPersonaggi, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali = caricaNemiciEPersonaggi(dati[0], dati[1], stanzaVecchia, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali)

                # stanza
                imgSfondoStanza = GlobalVar.loadImage("Immagini/Scenari/Stanza" + str(dati[1]) + "/Stanza.png", True, convert=True)
                imgSfondoStanza = pygame.transform.smoothscale(imgSfondoStanza, (GlobalVar.gsx, GlobalVar.gsy))
                sfondinoa = GlobalVar.loadImage("Immagini/Scenari/Stanza" + str(dati[1]) + "/SfondinoA.png", True, convert=True)
                sfondinoa = pygame.transform.smoothscale(sfondinoa, (GlobalVar.gpx, GlobalVar.gpy))
                sfondinob = GlobalVar.loadImage("Immagini/Scenari/Stanza" + str(dati[1]) + "/SfondinoB.png", True, convert=True)
                sfondinob = pygame.transform.smoothscale(sfondinob, (GlobalVar.gpx, GlobalVar.gpy))
                sfondinoc = GlobalVar.loadImage("Immagini/Scenari/Stanza" + str(dati[1]) + "/SfondinoC.png", True, convert=True)
                sfondinoc = pygame.transform.smoothscale(sfondinoc, (GlobalVar.gpx, GlobalVar.gpy))
                portaVert = GlobalVar.loadImage("Immagini/Scenari/Stanza" + str(dati[1]) + "/PortaVerticale.png", True)
                portaVert = pygame.transform.smoothscale(portaVert, (GlobalVar.gpx, GlobalVar.gpy))
                portaOriz = GlobalVar.loadImage("Immagini/Scenari/Stanza" + str(dati[1]) + "/PortaOrizzontale.png", True)
                portaOriz = pygame.transform.smoothscale(portaOriz, (GlobalVar.gpx, GlobalVar.gpy))

                if not inizio:
                    mosseRimasteRob = 0
                nemicoInquadrato = False
                stanza = dati[1]
                # fermare la camminata dopo il cambio stanza
                nx = 0
                ny = 0
                tastop = 0

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

                # fai vedere caselle viste
                # caseviste[x, y, flag, ... ] -> riempito come se non vedessi niente
                caseviste = []
                n = 0
                while n <= 29:
                    m = 0
                    while m <= 15:
                        caseviste.append(GlobalVar.gpx + (GlobalVar.gpx * n))
                        caseviste.append(GlobalVar.gpy + (GlobalVar.gpy * m))
                        caseviste.append(False)
                        m = m + 1
                    n = n + 1
                # scoprire caselle viste
                casevistePorteIncluse = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, listaPersonaggi, caseviste, False)
                casevistePorteIncluse = casevistePorteIncluse[:]
                caseviste = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, listaPersonaggi, caseviste)

                if not inizio:
                    # eliminare tutte le esche
                    vitaesca = []
                    # elimino tutti i sacchetti di denaro
                    vettoreDenaro = []

                cambiosta = False
                stanzaCambiata = True
                impossibileCliccarePulsanti = True

            if not cambiosta:
                # arma
                armaw = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%iw.png" % dati[6], True)
                armaw = pygame.transform.smoothscale(armaw, (GlobalVar.gpx, GlobalVar.gpy))
                armawMov1 = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%iwMov1.png" % dati[6], True)
                armawMov1 = pygame.transform.smoothscale(armawMov1, (GlobalVar.gpx, GlobalVar.gpy))
                armawMov2 = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%iwMov2.png" % dati[6], True)
                armawMov2 = pygame.transform.smoothscale(armawMov2, (GlobalVar.gpx, GlobalVar.gpy))
                armaa = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%ia.png" % dati[6], True)
                armaa = pygame.transform.smoothscale(armaa, (GlobalVar.gpx, GlobalVar.gpy))
                armaaMov1 = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%iaMov1.png" % dati[6], True)
                armaaMov1 = pygame.transform.smoothscale(armaaMov1, (GlobalVar.gpx, GlobalVar.gpy))
                armaaMov2 = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%iaMov2.png" % dati[6], True)
                armaaMov2 = pygame.transform.smoothscale(armaaMov2, (GlobalVar.gpx, GlobalVar.gpy))
                armas = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%is.png" % dati[6], True)
                armas = pygame.transform.smoothscale(armas, (GlobalVar.gpx, GlobalVar.gpy))
                armasMov1 = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%isMov1.png" % dati[6], True)
                armasMov1 = pygame.transform.smoothscale(armasMov1, (GlobalVar.gpx, GlobalVar.gpy))
                armasMov2 = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%isMov2.png" % dati[6], True)
                armasMov2 = pygame.transform.smoothscale(armasMov2, (GlobalVar.gpx, GlobalVar.gpy))
                armad = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%id.png" % dati[6], True)
                armad = pygame.transform.smoothscale(armad, (GlobalVar.gpx, GlobalVar.gpy))
                armadMov1 = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%idMov1.png" % dati[6], True)
                armadMov1 = pygame.transform.smoothscale(armadMov1, (GlobalVar.gpx, GlobalVar.gpy))
                armadMov2 = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%idMov2.png" % dati[6], True)
                armadMov2 = pygame.transform.smoothscale(armadMov2, (GlobalVar.gpx, GlobalVar.gpy))
                armasAttacco = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%isAttacco.png" % dati[6], True)
                armasAttacco = pygame.transform.smoothscale(armasAttacco, (GlobalVar.gpx, GlobalVar.gpy * 2))
                armaaAttacco = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%iaAttacco.png" % dati[6], True)
                armaaAttacco = pygame.transform.smoothscale(armaaAttacco, (GlobalVar.gpx * 2, GlobalVar.gpy))
                armadAttacco = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%idAttacco.png" % dati[6], True)
                armadAttacco = pygame.transform.smoothscale(armadAttacco, (GlobalVar.gpx * 2, GlobalVar.gpy))
                armawAttacco = GlobalVar.loadImage("Immagini/EquipSara/Spade/Spada%iwAttacco.png" % dati[6], True)
                armawAttacco = pygame.transform.smoothscale(armawAttacco, (GlobalVar.gpx, GlobalVar.gpy * 2))
                # arco
                arcow = GlobalVar.loadImage("Immagini/EquipSara/Archi/Arco%iw.png" % dati[128], True)
                arcow = pygame.transform.smoothscale(arcow, (GlobalVar.gpx, GlobalVar.gpy))
                arcoa = GlobalVar.loadImage("Immagini/EquipSara/Archi/Arco%ia.png" % dati[128], True)
                arcoa = pygame.transform.smoothscale(arcoa, (GlobalVar.gpx, GlobalVar.gpy))
                arcos = GlobalVar.loadImage("Immagini/EquipSara/Archi/Arco%is.png" % dati[128], True)
                arcos = pygame.transform.smoothscale(arcos, (GlobalVar.gpx, GlobalVar.gpy))
                arcod = GlobalVar.loadImage("Immagini/EquipSara/Archi/Arco%id.png" % dati[128], True)
                arcod = pygame.transform.smoothscale(arcod, (GlobalVar.gpx, GlobalVar.gpy))
                arcosAttacco = GlobalVar.loadImage("Immagini/EquipSara/Archi/Arco%isAttacco.png" % dati[128], True)
                arcosAttacco = pygame.transform.smoothscale(arcosAttacco, (GlobalVar.gpx, GlobalVar.gpy * 2))
                arcoaAttacco = GlobalVar.loadImage("Immagini/EquipSara/Archi/Arco%iaAttacco.png" % dati[128], True)
                arcoaAttacco = pygame.transform.smoothscale(arcoaAttacco, (GlobalVar.gpx * 2, GlobalVar.gpy))
                arcodAttacco = GlobalVar.loadImage("Immagini/EquipSara/Archi/Arco%idAttacco.png" % dati[128], True)
                arcodAttacco = pygame.transform.smoothscale(arcodAttacco, (GlobalVar.gpx * 2, GlobalVar.gpy))
                arcowAttacco = GlobalVar.loadImage("Immagini/EquipSara/Archi/Arco%iwAttacco.png" % dati[128], True)
                arcowAttacco = pygame.transform.smoothscale(arcowAttacco, (GlobalVar.gpx, GlobalVar.gpy * 2))
                # faretra
                faretraw = GlobalVar.loadImage("Immagini/EquipSara/Faretre/Faretra%iw.png" % dati[133], True)
                faretraw = pygame.transform.smoothscale(faretraw, (GlobalVar.gpx, GlobalVar.gpy))
                faretraa = GlobalVar.loadImage("Immagini/EquipSara/Faretre/Faretra%ia.png" % dati[133], True)
                faretraa = pygame.transform.smoothscale(faretraa, (GlobalVar.gpx, GlobalVar.gpy))
                faretras = GlobalVar.loadImage("Immagini/EquipSara/Faretre/Faretra%is.png" % dati[133], True)
                faretras = pygame.transform.smoothscale(faretras, (GlobalVar.gpx, GlobalVar.gpy))
                faretrad = GlobalVar.loadImage("Immagini/EquipSara/Faretre/Faretra%id.png" % dati[133], True)
                faretrad = pygame.transform.smoothscale(faretrad, (GlobalVar.gpx, GlobalVar.gpy))
                # armatura
                armaturaw = GlobalVar.loadImage("Immagini/EquipSara/Armature/Armatura%iw.png" % dati[8], True)
                armaturaw = pygame.transform.smoothscale(armaturaw, (GlobalVar.gpx, GlobalVar.gpy))
                armaturaa = GlobalVar.loadImage("Immagini/EquipSara/Armature/Armatura%ia.png" % dati[8], True)
                armaturaa = pygame.transform.smoothscale(armaturaa, (GlobalVar.gpx, GlobalVar.gpy))
                armaturas = GlobalVar.loadImage("Immagini/EquipSara/Armature/Armatura%is.png" % dati[8], True)
                armaturas = pygame.transform.smoothscale(armaturas, (GlobalVar.gpx, GlobalVar.gpy))
                armaturad = GlobalVar.loadImage("Immagini/EquipSara/Armature/Armatura%id.png" % dati[8], True)
                armaturad = pygame.transform.smoothscale(armaturad, (GlobalVar.gpx, GlobalVar.gpy))
                # scudo
                scudow = GlobalVar.loadImage("Immagini/EquipSara/Scudi/Scudo%iw.png" % dati[7], True)
                scudow = pygame.transform.smoothscale(scudow, (GlobalVar.gpx, GlobalVar.gpy))
                scudoa = GlobalVar.loadImage("Immagini/EquipSara/Scudi/Scudo%ia.png" % dati[7], True)
                scudoa = pygame.transform.smoothscale(scudoa, (GlobalVar.gpx, GlobalVar.gpy))
                scudos = GlobalVar.loadImage("Immagini/EquipSara/Scudi/Scudo%is.png" % dati[7], True)
                scudos = pygame.transform.smoothscale(scudos, (GlobalVar.gpx, GlobalVar.gpy))
                scudod = GlobalVar.loadImage("Immagini/EquipSara/Scudi/Scudo%id.png" % dati[7], True)
                scudod = pygame.transform.smoothscale(scudod, (GlobalVar.gpx, GlobalVar.gpy))
                scudoDifesa = GlobalVar.loadImage("Immagini/EquipSara/Scudi/Scudo%iDifesa.png" % dati[7], True)
                scudoDifesa = pygame.transform.smoothscale(scudoDifesa, (GlobalVar.gpx, GlobalVar.gpy))
                # guanti
                guantiw = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%iw.png" % dati[129], True)
                guantiw = pygame.transform.smoothscale(guantiw, (GlobalVar.gpx, GlobalVar.gpy))
                guantiwMov1 = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%iwMov1.png" % dati[129], True)
                guantiwMov1 = pygame.transform.smoothscale(guantiwMov1, (GlobalVar.gpx, GlobalVar.gpy))
                guantiwMov2 = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%iwMov2.png" % dati[129], True)
                guantiwMov2 = pygame.transform.smoothscale(guantiwMov2, (GlobalVar.gpx, GlobalVar.gpy))
                guantia = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%ia.png" % dati[129], True)
                guantia = pygame.transform.smoothscale(guantia, (GlobalVar.gpx, GlobalVar.gpy))
                guantiaMov1 = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%iaMov1.png" % dati[129], True)
                guantiaMov1 = pygame.transform.smoothscale(guantiaMov1, (GlobalVar.gpx, GlobalVar.gpy))
                guantiaMov2 = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%iaMov2.png" % dati[129], True)
                guantiaMov2 = pygame.transform.smoothscale(guantiaMov2, (GlobalVar.gpx, GlobalVar.gpy))
                guantis = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%is.png" % dati[129], True)
                guantis = pygame.transform.smoothscale(guantis, (GlobalVar.gpx, GlobalVar.gpy))
                guantisMov1 = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%isMov1.png" % dati[129], True)
                guantisMov1 = pygame.transform.smoothscale(guantisMov1, (GlobalVar.gpx, GlobalVar.gpy))
                guantisMov2 = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%isMov2.png" % dati[129], True)
                guantisMov2 = pygame.transform.smoothscale(guantisMov2, (GlobalVar.gpx, GlobalVar.gpy))
                guantid = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%id.png" % dati[129], True)
                guantid = pygame.transform.smoothscale(guantid, (GlobalVar.gpx, GlobalVar.gpy))
                guantidMov1 = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%idMov1.png" % dati[129], True)
                guantidMov1 = pygame.transform.smoothscale(guantidMov1, (GlobalVar.gpx, GlobalVar.gpy))
                guantidMov2 = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%idMov2.png" % dati[129], True)
                guantidMov2 = pygame.transform.smoothscale(guantidMov2, (GlobalVar.gpx, GlobalVar.gpy))
                guantisAttacco = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%isAttacco.png" % dati[129], True)
                guantisAttacco = pygame.transform.smoothscale(guantisAttacco, (GlobalVar.gpx, GlobalVar.gpy))
                guantiaAttacco = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%iaAttacco.png" % dati[129], True)
                guantiaAttacco = pygame.transform.smoothscale(guantiaAttacco, (GlobalVar.gpx, GlobalVar.gpy))
                guantidAttacco = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%idAttacco.png" % dati[129], True)
                guantidAttacco = pygame.transform.smoothscale(guantidAttacco, (GlobalVar.gpx, GlobalVar.gpy))
                guantiwAttacco = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%iwAttacco.png" % dati[129], True)
                guantiwAttacco = pygame.transform.smoothscale(guantiwAttacco, (GlobalVar.gpx, GlobalVar.gpy))
                guantiDifesa = GlobalVar.loadImage("Immagini/EquipSara/Guanti/Guanti%iDifesa.png" % dati[129], True)
                guantiDifesa = pygame.transform.smoothscale(guantiDifesa, (GlobalVar.gpx, GlobalVar.gpy))
                # collana
                collanaw = GlobalVar.loadImage("Immagini/EquipSara/Collane/Collana%iw.png" % dati[130], True)
                collanaw = pygame.transform.smoothscale(collanaw, (GlobalVar.gpx, GlobalVar.gpy))
                collanaa = GlobalVar.loadImage("Immagini/EquipSara/Collane/Collana%ia.png" % dati[130], True)
                collanaa = pygame.transform.smoothscale(collanaa, (GlobalVar.gpx, GlobalVar.gpy))
                collanas = GlobalVar.loadImage("Immagini/EquipSara/Collane/Collana%is.png" % dati[130], True)
                collanas = pygame.transform.smoothscale(collanas, (GlobalVar.gpx, GlobalVar.gpy))
                collanad = GlobalVar.loadImage("Immagini/EquipSara/Collane/Collana%id.png" % dati[130], True)
                collanad = pygame.transform.smoothscale(collanad, (GlobalVar.gpx, GlobalVar.gpy))
                # armatura robot
                armrobw = GlobalVar.loadImage("Immagini/EquipRobo/Batteria%iw.png" % dati[9], True)
                armrobw = pygame.transform.smoothscale(armrobw, (GlobalVar.gpx, GlobalVar.gpy))
                armroba = GlobalVar.loadImage("Immagini/EquipRobo/Batteria%ia.png" % dati[9], True)
                armroba = pygame.transform.smoothscale(armroba, (GlobalVar.gpx, GlobalVar.gpy))
                armrobs = GlobalVar.loadImage("Immagini/EquipRobo/Batteria%is.png" % dati[9], True)
                armrobs = pygame.transform.smoothscale(armrobs, (GlobalVar.gpx, GlobalVar.gpy))
                armrobd = GlobalVar.loadImage("Immagini/EquipRobo/Batteria%id.png" % dati[9], True)
                armrobd = pygame.transform.smoothscale(armrobd, (GlobalVar.gpx, GlobalVar.gpy))
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

            caricaTutto = True
            carim = False

        if inizio:
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

        if nmost == -1:
            listaNemiciTotali = []
            stanzeGiaVisitate = []
            ultimoObbiettivoColco = []
            obbiettivoCasualeColco = False

        if tastop == 0:
            GlobalVar.canaleSoundPassiRallo.stop()
            nx = 0
            ny = 0

        if canzone and not GlobalVar.canaleSoundCanzone.get_busy():
            GlobalVar.canaleSoundCanzone.play(canzone)

        inquadratoQualcosa = False
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVar.mouseVisibile:
            pygame.mouse.set_visible(True)
            GlobalVar.mouseVisibile = True
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
                    while i < len(casevistePorteIncluse):
                        if casevistePorteIncluse[i] <= xMouse <= casevistePorteIncluse[i] + GlobalVar.gpx and casevistePorteIncluse[i + 1] <= yMouse <= casevistePorteIncluse[i + 1] + GlobalVar.gpy and casevistePorteIncluse[i + 2]:
                            if GlobalVar.mouseBloccato:
                                GlobalVar.configuraCursore(False)
                            inquadratoQualcosa = "movimento:" + str(casevistePorteIncluse[i]) + ":" + str(casevistePorteIncluse[i + 1])
                            break
                        i += 3
        if inquadratoQualcosa and not inquadratoQualcosa.startswith("movimento"):
            GlobalVar.canaleSoundPassiRallo.stop()
            nx = 0
            ny = 0
        elif not inquadratoQualcosa and GlobalVar.mouseVisibile:
            GlobalVar.canaleSoundPassiRallo.stop()
            nx = 0
            ny = 0
            if not GlobalVar.mouseBloccato:
                GlobalVar.configuraCursore(True)

        # controllo se ci sono nemici in movimento per decidere se fare altre animazioni o no
        nemiciInMovimento = False
        for nemico in listaNemici:
            if nemico.mosseRimaste > 0:
                nemiciInMovimento = True
                break

        tastoTrovato = False
        # catturare gli eventi
        for event in pygame.event.get():
            sinistroMouseVecchio = sinistroMouse
            centraleMouseVecchio = centraleMouse
            destroMouseVecchio = destroMouse
            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
            rotellaConCentralePremuto = False
            if centraleMouseVecchio and centraleMouse:
                rotellaConCentralePremuto = True
            if not sinistroMouseVecchio and sinistroMouse:
                centraleMouse = False
                destroMouse = False
            elif not centraleMouseVecchio and centraleMouse:
                sinistroMouse = False
                destroMouse = False
            elif not destroMouseVecchio and destroMouse:
                sinistroMouse = False
                centraleMouse = False

            if event.type == pygame.QUIT:
                pygame.quit()
                GlobalVar.quit()

            if event.type == pygame.KEYDOWN and not impossibileCliccarePulsanti and not tastoTrovato and not startf:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                movimentoPerMouse = False
                tastop = event.key
                # movimenti personaggio
                if event.key == pygame.K_w and not tastoTrovato:
                    tastoTrovato = True
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
                if event.key == pygame.K_a and not tastoTrovato:
                    tastoTrovato = True
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
                if event.key == pygame.K_s and not tastoTrovato:
                    tastoTrovato = True
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
                if event.key == pygame.K_d and not tastoTrovato:
                    tastoTrovato = True
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

                if event.key == pygame.K_e and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                    tastoTrovato = True
                    nx = 0
                    ny = 0
                    attacco = 1
                if event.key == pygame.K_q and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento and nemicoInquadrato:
                    tastoTrovato = True
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    nx = 0
                    ny = 0
                    nemicoInquadrato = False
                    caricaTutto = True
                if (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT) and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento:
                    GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoTeleColco)
                    tastoTrovato = True
                    nx = 0
                    ny = 0
                    if chiamarob:
                        chiamarob = False
                    else:
                        ultimoObbiettivoColco = []
                        ultimoObbiettivoColco.append("Telecomando")
                        ultimoObbiettivoColco.append(x)
                        ultimoObbiettivoColco.append(y)
                        chiamarob = True
                if (event.key == pygame.K_3 or event.key == pygame.K_KP3) and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento:
                    tastoTrovato = True
                    nx = 0
                    ny = 0
                    listaNemiciVisti = []
                    for nemico in listaNemici:
                        if nemico.inCasellaVista:
                            listaNemiciVisti.append(nemico)
                    listaEscheViste = []
                    i = 0
                    while i < len(vitaesca):
                        j = 0
                        while j < len(caseviste):
                            if caseviste[j] == vitaesca[i + 2] and caseviste[j + 1] == vitaesca[i + 3] and caseviste[j + 2]:
                                listaEscheViste.append(vitaesca[i])
                                listaEscheViste.append(vitaesca[i + 1])
                                listaEscheViste.append(vitaesca[i + 2])
                                listaEscheViste.append(vitaesca[i + 3])
                            j += 3
                        i += 4
                    nemicoInquadrato = scorriObbiettiviInquadrati(dati[0], nemicoInquadrato, listaNemiciVisti, listaEscheViste, True)
                    caricaTutto = True
                if (event.key == pygame.K_2 or event.key == pygame.K_KP2) and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento:
                    tastoTrovato = True
                    nx = 0
                    ny = 0
                    listaNemiciVisti = []
                    for nemico in listaNemici:
                        if nemico.inCasellaVista:
                            listaNemiciVisti.append(nemico)
                    listaEscheViste = []
                    i = 0
                    while i < len(vitaesca):
                        j = 0
                        while j < len(caseviste):
                            if caseviste[j] == vitaesca[i + 2] and caseviste[j + 1] == vitaesca[i + 3] and caseviste[j + 2]:
                                listaEscheViste.append(vitaesca[i])
                                listaEscheViste.append(vitaesca[i + 1])
                                listaEscheViste.append(vitaesca[i + 2])
                                listaEscheViste.append(vitaesca[i + 3])
                            j += 3
                        i += 4
                    nemicoInquadrato = scorriObbiettiviInquadrati(dati[0], nemicoInquadrato, listaNemiciVisti, listaEscheViste, False)
                    caricaTutto = True
                if event.key == pygame.K_SPACE and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento:
                    tastoTrovato = True
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
                                # scoprire caselle viste
                                casevistePorteIncluse = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, listaPersonaggi, caseviste, False)
                                casevistePorteIncluse = casevistePorteIncluse[:]
                                caseviste = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, listaPersonaggi, caseviste)
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
                            cofanetti[i + 3] = True
                            caricaTutto = True
                            # aggiornare vettore tutticofanetti
                            j = 0
                            while j < len(tutticofanetti):
                                if tutticofanetti[j] == cofanetti[i] and tutticofanetti[j + 1] == cofanetti[i + 1] and \
                                        tutticofanetti[j + 2] == cofanetti[i + 2]:
                                    tutticofanetti[j + 3] = True
                                j = j + 4
                        i = i + 4
                    # interazioni con altri personaggi
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
                            disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, eschePrimaDelTurno, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, dati[0])
                            dati[0], oggettoRicevuto, visualizzaMenuMercante = dialoga(dati[0], personaggio, canzone)
                            caricaTutto = True
                if event.key == pygame.K_ESCAPE and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento:
                    tastoTrovato = True
                    nx = 0
                    ny = 0
                    startf = True

            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and centraleMouse and not rotellaConCentralePremuto and not impossibileCliccarePulsanti and not startf and mosseRimasteRob <= 0 and not nemiciInMovimento:
                movimentoPerMouse = False
                tastop = "mouseCentrale"
                tastoTrovato = True
                nx = 0
                ny = 0
                startf = True
            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse and not rotellaConCentralePremuto and not impossibileCliccarePulsanti and not startf and mosseRimasteRob <= 0 and not nemiciInMovimento:
                movimentoPerMouse = False
                tastop = "mouseDestro"
                tastoTrovato = True
                nx = 0
                ny = 0
                if inquadratoQualcosa == "battaglia" and nemicoInquadrato:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    nemicoInquadrato = False
                    caricaTutto = True
                else:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                    attacco = 1
            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and not GlobalVar.mouseBloccato and not impossibileCliccarePulsanti and not startf and mosseRimasteRob <= 0 and not nemiciInMovimento:
                tastop = "mouseSinistro"
                tastoTrovato = True
                nx = 0
                ny = 0
                if inquadratoQualcosa == "start":
                    movimentoPerMouse = False
                    startf = True
                elif inquadratoQualcosa == "battaglia":
                    movimentoPerMouse = False
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                    attacco = 1
                elif inquadratoQualcosa == "telecolco":
                    movimentoPerMouse = False
                    GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoTeleColco)
                    if chiamarob:
                        chiamarob = False
                    else:
                        ultimoObbiettivoColco = []
                        ultimoObbiettivoColco.append("Telecomando")
                        ultimoObbiettivoColco.append(x)
                        ultimoObbiettivoColco.append(y)
                        chiamarob = True
                elif inquadratoQualcosa.startswith("porta"):
                    movimentoPerMouse = False
                    inquadratoQualcosaList = inquadratoQualcosa.split(":")
                    posizPortaInVettore = int(inquadratoQualcosaList[1])
                    if possibileAprirePorta(dati[1], porte[posizPortaInVettore + 1], porte[posizPortaInVettore + 2], dati[0]):
                        sposta = True
                        GlobalVar.canaleSoundInterazioni.play(rumoreAperturaPorte)
                        porte[posizPortaInVettore + 3] = True
                        # scoprire caselle viste
                        casevistePorteIncluse = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, listaPersonaggi, caseviste, False)
                        casevistePorteIncluse = casevistePorteIncluse[:]
                        caseviste = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, listaPersonaggi, caseviste)
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
                elif inquadratoQualcosa.startswith("cofanetto"):
                    movimentoPerMouse = False
                    inquadratoQualcosaList = inquadratoQualcosa.split(":")
                    posizCofanettoInVettore = int(inquadratoQualcosaList[1])
                    sposta = True
                    GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoaperturacofanetti)
                    dati, tesoro, dati[0] = aperturacofanetto(cofanetti[posizCofanettoInVettore], cofanetti[posizCofanettoInVettore + 1], cofanetti[posizCofanettoInVettore + 2], dati)
                    cofanetti[posizCofanettoInVettore + 3] = True
                    caricaTutto = True
                    # aggiornare vettore tutticofanetti
                    j = 0
                    while j < len(tutticofanetti):
                        if tutticofanetti[j] == cofanetti[posizCofanettoInVettore] and tutticofanetti[j + 1] == cofanetti[posizCofanettoInVettore + 1] and tutticofanetti[j + 2] == cofanetti[posizCofanettoInVettore + 2]:
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
                elif inquadratoQualcosa.startswith("personaggio"):
                    movimentoPerMouse = False
                    inquadratoQualcosaList = inquadratoQualcosa.split(":")
                    posizPersonaggioInVettore = int(inquadratoQualcosaList[1])
                    personaggio = listaPersonaggi[posizPersonaggioInVettore]
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
                    disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, eschePrimaDelTurno, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, dati[0])
                    dati[0], oggettoRicevuto, visualizzaMenuMercante = dialoga(dati[0], personaggio, canzone)
                    caricaTutto = True
                elif inquadratoQualcosa.startswith("movimento"):
                    movimentoPerMouse = True
            elif GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and GlobalVar.mouseBloccato and mosseRimasteRob <= 0 and not nemiciInMovimento:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
            if (sinistroMouse or centraleMouse or destroMouse) and not rotellaConCentralePremuto and not GlobalVar.mouseVisibile:
                pygame.mouse.set_visible(True)
                GlobalVar.mouseVisibile = True

            if event.type == pygame.KEYUP:
                if tastop == event.key:
                    GlobalVar.canaleSoundPassiRallo.stop()
                    nx = 0
                    ny = 0
                    tastop = 0
            if event.type == pygame.MOUSEBUTTONUP:
                movimentoPerMouse = False
                GlobalVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                tastop = 0

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

        if inquadratoQualcosa and inquadratoQualcosa.startswith("movimento") and movimentoPerMouse and mosseRimasteRob <= 0 and not nemiciInMovimento and not impossibileCliccarePulsanti and not startf:
            vetNemiciSoloConXeY = []
            if not (x == rx and y == ry):
                vetNemiciSoloConXeY.append(rx)
                vetNemiciSoloConXeY.append(ry)
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
            if bloccato or (x == xObbiettivo and y == yObbiettivo):
                GlobalVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
            else:
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
                    percorsoTrovato = pathFinding(x, y, xObbiettivo, yObbiettivo, vetNemiciSoloConXeY, casevistePorteIncluse)
                    if percorsoTrovato:
                        if len(percorsoTrovato) >= 4 and percorsoTrovato[len(percorsoTrovato) - 4] != x or percorsoTrovato[len(percorsoTrovato) - 3] != y:
                            if percorsoTrovato[len(percorsoTrovato) - 4] > x:
                                npers = 1
                            if percorsoTrovato[len(percorsoTrovato) - 4] < x:
                                npers = 2
                            if percorsoTrovato[len(percorsoTrovato) - 3] > y:
                                npers = 4
                            if percorsoTrovato[len(percorsoTrovato) - 3] < y:
                                npers = 3
                            sposta = True
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

        # menu start
        if startf and attacco != 1:
            GlobalVar.canaleSoundPassiRallo.stop()
            GlobalVar.canaleSoundInterazioni.play(GlobalVar.selsta)
            dati[2] = x
            dati[3] = y
            dati[140] = npers
            dati[134] = rx
            dati[135] = ry
            dati[141] = nrob
            dati[139] = mosseRimasteRob
            dati[136] = raffredda
            dati[137] = autoRic1
            dati[138] = autoRic2
            if not apriocchio:
                dati, inizio, attacco, caricaSalvataggio = start(dati, porteini, portefin, cofaniini, cofanifin, tutteporte, tutticofanetti, listaNemiciTotali, vitaesca, vettoreDenaro, stanzeGiaVisitate, listaPersonaggiTotali, canzone)
                if caricaSalvataggio:
                    inizio = True
                if attacco == 0:
                    uscitoDaMenu = 2
            else:
                dati, attacco, sposta, animaOggetto, npers, caricaSalvataggio, inizio = startBattaglia(dati, animaOggetto, x, y, npers, rx, ry, inizio, canzone)
                if caricaSalvataggio:
                    inizio = True
                else:
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
        inizio = controllaMorteRallo(dati[5], inizio)
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

            # faccio animazione di quando ricevo un oggetto speciale
            if oggettoRicevuto:
                disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, eschePrimaDelTurno, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, dati[0])
                animaOggettoSpecialeRicevuto(oggettoRicevuto, canzone)
                oggettoRicevuto = False
                caricaTutto = True

            # movimento-azioni personaggio
            if (nx != 0 or ny != 0) and not nemiciInMovimento and mosseRimasteRob <= 0:
                vx = x
                vy = y
                sposta = True
                stanzaVecchia = dati[1]
                x, y, dati[1], carim, cambiosta = muri_porte(x, y, nx, ny, dati[1], carim, False, False, porte, cofanetti, listaPersonaggi)

                sovrapposto = False
                for nemico in listaNemici:
                    if nemico.x == x and nemico.y == y:
                        sovrapposto = True
                        break
                for personaggio in listaPersonaggi:
                    if personaggio.x == x and personaggio.y == y:
                        sovrapposto = True
                        break
                if (x == rx and y == ry) or sovrapposto:
                    x = vx
                    y = vy
            # gestione attacchi
            attaccoADistanza = False
            # attaccoDiRallo [obbiettivo, danno, status(avvelena, appiccica) ... => per ogni nemico colpito]
            attaccoDiRallo = []
            if attacco != 0:
                GlobalVar.canaleSoundPassiRallo.stop()
                sposta, creaesca, xesca, yesca, npers, nrob, difesa, apriChiudiPorta, apriCofanetto, spingiColco, listaNemici, attacco, attaccoADistanza, nemicoInquadrato, attaccoDiRallo, chiamarob, ultimoObbiettivoColco, animaOggetto, interagisciConPersonaggio, startf = attacca(x, y, npers, nrob, rx, ry, pers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126], imgSfondoStanza, dati[1], sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, attVicino, attLontano, attacco, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, vettoreDenaro, dati[132], nemicoInquadrato, raffredda, autoRic1, autoRic2, ultimoObbiettivoColco, animaOggetto, listaPersonaggi, startf, dati[0], canzone)
                tastop = 0
                # cancello apertura porta se non si può aprire
                if apriChiudiPorta[0] and not possibileAprirePorta(dati[1], apriChiudiPorta[1], apriChiudiPorta[2], dati[0]):
                    apriChiudiPorta = [False, 0, 0]
                    caricaTutto = True
                    sposta = False
                    impossibileAprirePorta = True
                # tolgo una freccia se uso l'attacco a distanza
                if attaccoADistanza:
                    dati[132] -= 1
                caricaTutto = True
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
            if difesa != 0 and not sposta:
                esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati, difesa)
                if difesa == 2:
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
            if dati[121] and sposta:
                dati[5] = dati[5] - 2
                if dati[5] < 0:
                    dati[5] = 0
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
                        # scoprire caselle viste
                        casevistePorteIncluse = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, listaPersonaggi, caseviste, False)
                        casevistePorteIncluse = casevistePorteIncluse[:]
                        caseviste = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, listaPersonaggi, caseviste)
                        # aggiornare vettore tutteporte
                        j = 0
                        while j < len(tutteporte):
                            if tutteporte[j] == porte[k] and tutteporte[j + 1] == porte[k + 1] and tutteporte[j + 2] == porte[k + 2]:
                                tutteporte[j + 3] = porte[k + 3]
                                break
                            j = j + 4
                        # aggiorno inCasellaVista di nemici e personaggi
                        listaNemici, listaPersonaggi = aggiornaInCasellaVistaDiNemiciEPersonaggi(caseviste, listaNemici, listaPersonaggi)
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
                    while i < len(vitaesca):
                        if idEscaInquadrata == vitaesca[i]:
                            j = 0
                            while j < len(caseviste):
                                if caseviste[j] == vitaesca[i + 2] and caseviste[j + 1] == vitaesca[i + 3] and not caseviste[j + 2]:
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
                        disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, eschePrimaDelTurno, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, dati[0])
                        dati[0], oggettoRicevuto, visualizzaMenuMercante = dialoga(dati[0], personaggio, canzone)
                        caricaTutto = True
                interagisciConPersonaggio = False
            # menu mercante
            if visualizzaMenuMercante:
                dati = menuMercante(dati, canzone)
                visualizzaMenuMercante = False
                uscitoDaMenu = 1
            # apertura cofanetti
            if apriCofanetto[0]:
                i = 0
                while i < len(cofanetti):
                    if cofanetti[i] == dati[1] and cofanetti[i + 1] == apriCofanetto[1] and cofanetti[i + 2] == apriCofanetto[2] and not cofanetti[i + 3]:
                        GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoaperturacofanetti)
                        dati, tesoro, dati[0] = aperturacofanetto(cofanetti[i], cofanetti[i + 1], cofanetti[i + 2], dati)
                        cofanetti[i + 3] = True
                        # aggiornare vettore tutticofanetti
                        j = 0
                        while j < len(tutticofanetti):
                            if tutticofanetti[j] == cofanetti[i] and tutticofanetti[j + 1] == cofanetti[i + 1] and tutticofanetti[j + 2] == cofanetti[i + 2]:
                                tutticofanetti[j + 3] = True
                            j = j + 4
                    i = i + 4
                apriCofanetto = [False, 0, 0]
            # scambia posizione con Colco
            if spingiColco:
                xProv = x
                yProv = y
                x = rx
                y = ry
                rx = xProv
                ry = yProv
                spingiColco = False

            # impedisce di andare avanti quando si vuole andare in una zona non ancora sbloccata
            if cambiosta and nonPuoiProcedere(dati[0], x, y, stanzaVecchia, dati[1], canzone):
                cambiosta = False
                dati[1] = stanzaVecchia
                x = vx
                y = vy
                sposta = False
                caricaTutto = True
                movimentoPerMouse = False
                tastop = 0

            # esche prima del turno
            eschePrimaDelTurno = []
            i = 0
            while i < len(vitaesca):
                eschePrimaDelTurno.append(vitaesca[i])
                i += 4
            # lancio esche
            if creaesca:
                contaesca = contaesca + 1
                # id, vita, xesca, yesca
                vitaesca.append(contaesca)
                vitaesca.append(1000)
                vitaesca.append(xesca)
                vitaesca.append(yesca)
                creaesca = False
            # morte esca
            i = 1
            while i < len(vitaesca):
                cancellata = False
                if vitaesca[i] <= 0:
                    if ((vitaesca[i + 1] / GlobalVar.gpx) + (vitaesca[i + 2] / GlobalVar.gpy)) % 2 == 0:
                        GlobalVar.schermo.blit(sfondinoa, (vitaesca[i + 1], vitaesca[i + 2]))
                    if ((vitaesca[i + 1] / GlobalVar.gpx) + (vitaesca[i + 2] / GlobalVar.gpy)) % 2 == 1:
                        GlobalVar.schermo.blit(sfondinob, (vitaesca[i + 1], vitaesca[i + 2]))
                    # tolgo la GlobalVarG2.selezione dell'esca morta
                    if type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and int(nemicoInquadrato[4:]) == vitaesca[i - 1]:
                        nemicoInquadrato = False
                        caricaTutto = True
                    del vitaesca[i + 2]
                    del vitaesca[i + 1]
                    del vitaesca[i]
                    del vitaesca[i - 1]
                    cancellata = True
                if not cancellata:
                    i = i + 4
            # riprendere le esche
            i = 1
            while i < len(vitaesca):
                if vitaesca[i + 1] == x and vitaesca[i + 2] == y:
                    GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoRaccoltaEsca)
                    # tolgo la GlobalVarG2.selezione dell'esca ripresa
                    if type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and int(nemicoInquadrato[4:]) == vitaesca[i - 1]:
                        nemicoInquadrato = False
                        caricaTutto = True
                    del vitaesca[i + 2]
                    del vitaesca[i + 1]
                    del vitaesca[i]
                    del vitaesca[i - 1]
                    dati[38] += 1
                i = i + 4
            # statoEscheInizioTurno["Esca"+id1, pv1, "Esca"+id2, pv2, ...]
            statoEscheInizioTurno = []
            i = 0
            while i < len(vitaesca):
                statoEscheInizioTurno.append("Esca" + str(vitaesca[i]))
                statoEscheInizioTurno.append(vitaesca[i + 1])
                i += 4

            # movimento-azioni robo
            if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] and rx == GlobalVar.gsx and ry == GlobalVar.gsy:
                rx = x
                ry = y
                vrx = rx
                vry = ry
            azioneRobEseguita = False
            if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] and dati[122] > 0:
                # se surriscaldato toglie vel+ e efficienza
                dati[125] = 0
                dati[126] = 0
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
                    rx, ry, nrob, dati, listaNemici, raffreddamento, ricarica1, ricarica2, azioneRobEseguita, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, attaccoDiColco, ultimoObbiettivoColco, obbiettivoCasualeColco = movrobo(x, y, vx, vy, rx, ry, dati[1], chiamarob, dati, porte, cofanetti, listaNemici, nmost, difesa, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggi, caseviste)

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

            # movimento-azioni mostri
            if nmost > 0 and not cambiosta:
                for nemico in listaNemici:
                    if nemico.avvelenato and sposta:
                        nemico.vita -= 3
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
                            nemicoVistoRallo, nemicoVistoRob, nemicoVistoesca, nemicoEscabersaglio, nemicoVistoDenaro, nemicoXDenaro, nemicoYDenaro, attrobo = nemico.settaObbiettivo(x, y, rx, ry, dati, stanza, porte, cofanetti, listaPersonaggi, vettoreDenaro, vitaesca, attaccoADistanza, listaNemiciAttaccatiADistanzaRobo)
                            nemico.vx = nemico.x
                            nemico.vy = nemico.y
                            nemico, direzioneMostro, dati, vitaesca = movmostro(x, y, rx, ry, nemico, dati[1], dif, difro, par, dati, vitaesca, porte, cofanetti, vetDatiNemici, nemicoVistoRallo, nemicoVistoRob, nemicoVistoesca, nemicoEscabersaglio, nemicoVistoDenaro, nemicoXDenaro, nemicoYDenaro, attrobo, listaPersonaggi, caseviste)
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
                            nemico.compiMossa()
                        elif sposta and nemico.mosseRimaste < 0:
                            nemico.mosseRimaste += 1
                    elif nemico.vita <= 0:
                        nmost -= 1
                        dati[127] += nemico.esp
                        # effetto apprendimaschera
                        if dati[130] == 3:
                            dati[127] += nemico.esp
                        # metto il suo denaro nella casella in cui è morto (vettore => qta, x, y)
                        if nemico.denaro > 0:
                            vettoreDenaro.append(nemico.denaro)
                            vettoreDenaro.append(nemico.x)
                            vettoreDenaro.append(nemico.y)
                        nemico.morto = True
                        nemico.animaMorte = True

            # movimento personaggi che sono in una casella vista
            if sposta:
                for personaggio in listaPersonaggi:
                    if personaggio.inCasellaVista and not personaggio.mantieniSempreASchermo:
                        personaggio.spostati(x, y, rx, ry, listaNemici)

            # aumentare di livello
            while dati[127] >= esptot and dati[4] < 100:
                dati[4] += 1
                dati[127] -= esptot
                aumentoliv += 1
                esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati, difesa)
                impossibileCliccarePulsanti = True

            # aggiorna vista dei mostri e metti l'occhio se ti vedono
            apriocchio = False
            for nemico in listaNemici:
                if nemico.vita > 0 and nemico.inCasellaVista and ((abs(x - nemico.x) <= nemico.raggioVisivo and abs(y - nemico.y) <= nemico.raggioVisivo) or (abs(rx - nemico.x) <= nemico.raggioVisivo and abs(ry - nemico.y) <= nemico.raggioVisivo)):
                    nemico.aggiornaVista(x, y, rx, ry, dati[1], porte, cofanetti, listaPersonaggi, dati)
                    if nemico.visto:
                        apriocchio = True

            # fai tutte le animazioni del turno e disegni gli sfondi e personaggi
            if caricaTutto:
                if aumentoliv != 0:
                    pvtot = getVitaTotRallo(dati[4] - aumentoliv, dati[129])
                disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, eschePrimaDelTurno, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, dati[0])
                caricaTutto = False
            if azioneRobEseguita or nemiciInMovimento or sposta:
                primopasso, caricaTutto, tesoro, tastop, movimentoPerMouse = anima(sposta, x, y, vx, vy, rx, ry, vrx, vry, pers, robot, npers, nrob, primopasso, cambiosta, sfondinoa, sfondinob, scudo, armatura, arma, armaMov1, armaMov2, armaAttacco, scudoDifesa, arco, faretra, arcoAttacco, guanti, guantiMov1, guantiMov2, guantiAttacco, guantiDifesa, collana, armas, armaturas, arcos, faretras, collanas, armrob, armrobs, dati, attacco, difesa, tastop, tesoro, sfondinoc, aumentoliv, carim, caricaTutto, listaNemici, vitaesca, vettoreDenaro, attaccoADistanza, caseviste, porte, cofanetti, portaOriz, portaVert, stanza, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoInquadrato, attaccoDiRallo, attaccoDiColco, statoRalloInizioTurno, statoColcoInizioTurno, statoEscheInizioTurno, raffreddamento, ricarica1, ricarica2, raffredda, autoRic1, autoRic2, animaOggetto, eschePrimaDelTurno, listaPersonaggi, movimentoPerMouse, canzone)
            if not carim:
                pvtot = getVitaTotRallo(dati[4], dati[129])
                disegnaAmbiente(x, y, npers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, eschePrimaDelTurno, listaPersonaggi, False, stanzaCambiata, uscitoDaMenu, dati[0])

            if aumentoliv == 0:
                caricaTutto = False

            # gestisce eventi speciali come i dialoghi del tutorial o dialoghi con nessuno
            if not carim:
                dati[0], cambiosta, dati[1], carim, caricaTutto, tastop, movimentoPerMouse = gestisciEventiStoria(dati[0], dati[1], x, y, cambiosta, carim, caricaTutto, tastop, movimentoPerMouse, impossibileAprirePorta, canzone)
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
                nemico.animaDanneggiamento = False
                nemico.bersaglioColpito = []
                nemico.ralloParato = False
                if not type(nemicoInquadrato) is str and nemicoInquadrato and nemicoInquadrato.morto:
                    nemicoInquadrato = False
                    caricaTutto = True
                if nemico.morto:
                    listaNemici.remove(nemico)
                    listaNemiciTotali.remove(nemico)
                i -= 1

            # aggiorna i dialoghi e le img di tutti i personaggi / oggetti in base all'avanzamento nella storia
            for personaggio in listaPersonaggi:
                personaggio.aggiornaDialogo(dati[0])
                if personaggio.mantieniSempreASchermo:
                    personaggio.aggiornaImgOggetto(dati[0])

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

gameloop()
