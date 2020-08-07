# -*- coding: utf-8 -*-

from Menu import *
from EnvPrint import *
from MovNemiciRob import *
from Animazioni import *
from PersonaggioObj import *
from GenericFuncB import *


def gameloop():
    caricaSalvataggio = False
    inizio = True
    while True:
        if inizio:
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
            agg = 0
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
            if dati[0] < GlobalVar.avanzamentoStoriaCambioPersonaggio:
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
            if dati[0] < GlobalVar.avanzamentoStoriaCambioPersonaggio:
                personaggioDaUsare = "FratelloMaggiore"
            else:
                personaggioDaUsare = "Sara"
            if personaggioDaUsare != personaggioUsato:
                cambiaProtagonista(personaggioDaUsare)
                personaggioUsato = personaggioDaUsare
                agg = 3

            if cambiosta:
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

            if pers == GlobalVar.persw:
                agg = 1
            if pers == GlobalVar.persa:
                agg = 2
            if pers == GlobalVar.perss:
                agg = 3
            if pers == GlobalVar.persd:
                agg = 4

            # mostri - personaggi
            if dati[1] == 1 and cambiosta:
                # rumore porte
                rumoreAperturaPorte = GlobalVar.suonoaperturaporte1
                rumoreChiusuraPorte = GlobalVar.suonochiusuraporte1

                # posizione personaggio e robot al cambio stanza
                if not inizio:
                    if stanzaVecchia == 2:
                        npers = 4
                        nrob = 3
                        x = GlobalVar.gsx // 32 * 6
                        y = GlobalVar.gsy // 18 * 2
                        pers = GlobalVar.perss
                        robot = GlobalVar.robos
                        agg = 3
                    vx = x
                    vy = y
                    rx = x
                    ry = y
                    vrx = x
                    vry = y

            if dati[1] == 2 and cambiosta:
                # rumore porte
                rumoreAperturaPorte = GlobalVar.suonoaperturaporte2
                rumoreChiusuraPorte = GlobalVar.suonochiusuraporte2

                # posizione personaggio e robot al cambio stanza
                if not inizio:
                    if stanzaVecchia == 1:
                        npers = 4
                        nrob = 3
                        x = GlobalVar.gsx // 32 * 6
                        y = GlobalVar.gsy // 18 * 2
                        pers = GlobalVar.perss
                        robot = GlobalVar.robos
                        agg = 3
                    vx = x
                    vy = y
                    rx = x
                    ry = y
                    vrx = x
                    vry = y

            if cambiosta:
                nmost, listaNemici, listaPersonaggi, listaNemiciTotali, listaPersonaggiTotali = caricaNemiciNellaStanza(dati[0], dati[1], stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali)

                # stanza
                imgSfondoStanza = pygame.image.load("Immagini/Paesaggi/Stanza%ia.png" % dati[1]).convert()
                imgSfondoStanza = pygame.transform.scale(imgSfondoStanza, (GlobalVar.gsx, GlobalVar.gsy))
                sfondinoa = pygame.image.load("Immagini/Paesaggi/Sfondino%ia.png" % dati[1]).convert()
                sfondinoa = pygame.transform.scale(sfondinoa, (GlobalVar.gpx, GlobalVar.gpy))
                sfondinob = pygame.image.load("Immagini/Paesaggi/Sfondino%ib.png" % dati[1]).convert()
                sfondinob = pygame.transform.scale(sfondinob, (GlobalVar.gpx, GlobalVar.gpy))
                sfondinoc = pygame.image.load("Immagini/Paesaggi/Sfondino%ic.png" % dati[1]).convert()
                sfondinoc = pygame.transform.scale(sfondinoc, (GlobalVar.gpx, GlobalVar.gpy))
                portaVert = pygame.image.load("Immagini/Paesaggi/PortaV%i.png" % dati[1])
                portaVert = pygame.transform.scale(portaVert, (GlobalVar.gpx, GlobalVar.gpy))
                portaOriz = pygame.image.load("Immagini/Paesaggi/PortaO%i.png" % dati[1])
                portaOriz = pygame.transform.scale(portaOriz, (GlobalVar.gpx, GlobalVar.gpy))

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
                casevistePorteIncluse = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, caseviste, False)
                casevistePorteIncluse = casevistePorteIncluse[:]
                caseviste = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, caseviste)

                if not inizio:
                    # eliminare tutte le esche
                    vitaesca = []
                    # elimino tutti i sacchetti di denaro
                    vettoreDenaro = []

                # cambiosta viene cambiato sopra !!!!!!!!!!!!
                cambiosta = False
                stanzaCambiata = True
                impossibileCliccarePulsanti = True

            if not cambiosta:
                # arma
                armaw = pygame.image.load("Immagini/EquipSara/Spade/Spada%iw.png" % dati[6])
                armaw = pygame.transform.scale(armaw, (GlobalVar.gpx, GlobalVar.gpy))
                armawMov1 = pygame.image.load("Immagini/EquipSara/Spade/Spada%iwMov1.png" % dati[6])
                armawMov1 = pygame.transform.scale(armawMov1, (GlobalVar.gpx, GlobalVar.gpy))
                armawMov2 = pygame.image.load("Immagini/EquipSara/Spade/Spada%iwMov2.png" % dati[6])
                armawMov2 = pygame.transform.scale(armawMov2, (GlobalVar.gpx, GlobalVar.gpy))
                armaa = pygame.image.load("Immagini/EquipSara/Spade/Spada%ia.png" % dati[6])
                armaa = pygame.transform.scale(armaa, (GlobalVar.gpx, GlobalVar.gpy))
                armaaMov1 = pygame.image.load("Immagini/EquipSara/Spade/Spada%iaMov1.png" % dati[6])
                armaaMov1 = pygame.transform.scale(armaaMov1, (GlobalVar.gpx, GlobalVar.gpy))
                armaaMov2 = pygame.image.load("Immagini/EquipSara/Spade/Spada%iaMov2.png" % dati[6])
                armaaMov2 = pygame.transform.scale(armaaMov2, (GlobalVar.gpx, GlobalVar.gpy))
                armas = pygame.image.load("Immagini/EquipSara/Spade/Spada%is.png" % dati[6])
                armas = pygame.transform.scale(armas, (GlobalVar.gpx, GlobalVar.gpy))
                armasMov1 = pygame.image.load("Immagini/EquipSara/Spade/Spada%isMov1.png" % dati[6])
                armasMov1 = pygame.transform.scale(armasMov1, (GlobalVar.gpx, GlobalVar.gpy))
                armasMov2 = pygame.image.load("Immagini/EquipSara/Spade/Spada%isMov2.png" % dati[6])
                armasMov2 = pygame.transform.scale(armasMov2, (GlobalVar.gpx, GlobalVar.gpy))
                armad = pygame.image.load("Immagini/EquipSara/Spade/Spada%id.png" % dati[6])
                armad = pygame.transform.scale(armad, (GlobalVar.gpx, GlobalVar.gpy))
                armadMov1 = pygame.image.load("Immagini/EquipSara/Spade/Spada%idMov1.png" % dati[6])
                armadMov1 = pygame.transform.scale(armadMov1, (GlobalVar.gpx, GlobalVar.gpy))
                armadMov2 = pygame.image.load("Immagini/EquipSara/Spade/Spada%idMov2.png" % dati[6])
                armadMov2 = pygame.transform.scale(armadMov2, (GlobalVar.gpx, GlobalVar.gpy))
                armasAttacco = pygame.image.load("Immagini/EquipSara/Spade/Spada%isAttacco.png" % dati[6])
                armasAttacco = pygame.transform.scale(armasAttacco, (GlobalVar.gpx, GlobalVar.gpy * 2))
                armaaAttacco = pygame.image.load("Immagini/EquipSara/Spade/Spada%iaAttacco.png" % dati[6])
                armaaAttacco = pygame.transform.scale(armaaAttacco, (GlobalVar.gpx * 2, GlobalVar.gpy))
                armadAttacco = pygame.image.load("Immagini/EquipSara/Spade/Spada%idAttacco.png" % dati[6])
                armadAttacco = pygame.transform.scale(armadAttacco, (GlobalVar.gpx * 2, GlobalVar.gpy))
                armawAttacco = pygame.image.load("Immagini/EquipSara/Spade/Spada%iwAttacco.png" % dati[6])
                armawAttacco = pygame.transform.scale(armawAttacco, (GlobalVar.gpx, GlobalVar.gpy * 2))
                # arco
                arcow = pygame.image.load("Immagini/EquipSara/Archi/Arco%iw.png" % dati[128])
                arcow = pygame.transform.scale(arcow, (GlobalVar.gpx, GlobalVar.gpy))
                arcoa = pygame.image.load("Immagini/EquipSara/Archi/Arco%ia.png" % dati[128])
                arcoa = pygame.transform.scale(arcoa, (GlobalVar.gpx, GlobalVar.gpy))
                arcos = pygame.image.load("Immagini/EquipSara/Archi/Arco%is.png" % dati[128])
                arcos = pygame.transform.scale(arcos, (GlobalVar.gpx, GlobalVar.gpy))
                arcod = pygame.image.load("Immagini/EquipSara/Archi/Arco%id.png" % dati[128])
                arcod = pygame.transform.scale(arcod, (GlobalVar.gpx, GlobalVar.gpy))
                arcosAttacco = pygame.image.load("Immagini/EquipSara/Archi/Arco%isAttacco.png" % dati[128])
                arcosAttacco = pygame.transform.scale(arcosAttacco, (GlobalVar.gpx, GlobalVar.gpy * 2))
                arcoaAttacco = pygame.image.load("Immagini/EquipSara/Archi/Arco%iaAttacco.png" % dati[128])
                arcoaAttacco = pygame.transform.scale(arcoaAttacco, (GlobalVar.gpx * 2, GlobalVar.gpy))
                arcodAttacco = pygame.image.load("Immagini/EquipSara/Archi/Arco%idAttacco.png" % dati[128])
                arcodAttacco = pygame.transform.scale(arcodAttacco, (GlobalVar.gpx * 2, GlobalVar.gpy))
                arcowAttacco = pygame.image.load("Immagini/EquipSara/Archi/Arco%iwAttacco.png" % dati[128])
                arcowAttacco = pygame.transform.scale(arcowAttacco, (GlobalVar.gpx, GlobalVar.gpy * 2))
                # faretra
                faretraw = pygame.image.load("Immagini/EquipSara/Faretre/Faretra%iw.png" % dati[133])
                faretraw = pygame.transform.scale(faretraw, (GlobalVar.gpx, GlobalVar.gpy))
                faretraa = pygame.image.load("Immagini/EquipSara/Faretre/Faretra%ia.png" % dati[133])
                faretraa = pygame.transform.scale(faretraa, (GlobalVar.gpx, GlobalVar.gpy))
                faretras = pygame.image.load("Immagini/EquipSara/Faretre/Faretra%is.png" % dati[133])
                faretras = pygame.transform.scale(faretras, (GlobalVar.gpx, GlobalVar.gpy))
                faretrad = pygame.image.load("Immagini/EquipSara/Faretre/Faretra%id.png" % dati[133])
                faretrad = pygame.transform.scale(faretrad, (GlobalVar.gpx, GlobalVar.gpy))
                # armatura
                armaturaw = pygame.image.load("Immagini/EquipSara/Armature/Armatura%iw.png" % dati[8])
                armaturaw = pygame.transform.scale(armaturaw, (GlobalVar.gpx, GlobalVar.gpy))
                armaturaa = pygame.image.load("Immagini/EquipSara/Armature/Armatura%ia.png" % dati[8])
                armaturaa = pygame.transform.scale(armaturaa, (GlobalVar.gpx, GlobalVar.gpy))
                armaturas = pygame.image.load("Immagini/EquipSara/Armature/Armatura%is.png" % dati[8])
                armaturas = pygame.transform.scale(armaturas, (GlobalVar.gpx, GlobalVar.gpy))
                armaturad = pygame.image.load("Immagini/EquipSara/Armature/Armatura%id.png" % dati[8])
                armaturad = pygame.transform.scale(armaturad, (GlobalVar.gpx, GlobalVar.gpy))
                # scudo
                scudow = pygame.image.load("Immagini/EquipSara/Scudi/Scudo%iw.png" % dati[7])
                scudow = pygame.transform.scale(scudow, (GlobalVar.gpx, GlobalVar.gpy))
                scudoa = pygame.image.load("Immagini/EquipSara/Scudi/Scudo%ia.png" % dati[7])
                scudoa = pygame.transform.scale(scudoa, (GlobalVar.gpx, GlobalVar.gpy))
                scudos = pygame.image.load("Immagini/EquipSara/Scudi/Scudo%is.png" % dati[7])
                scudos = pygame.transform.scale(scudos, (GlobalVar.gpx, GlobalVar.gpy))
                scudod = pygame.image.load("Immagini/EquipSara/Scudi/Scudo%id.png" % dati[7])
                scudod = pygame.transform.scale(scudod, (GlobalVar.gpx, GlobalVar.gpy))
                scudoDifesa = pygame.image.load("Immagini/EquipSara/Scudi/Scudo%iDifesa.png" % dati[7])
                scudoDifesa = pygame.transform.scale(scudoDifesa, (GlobalVar.gpx, GlobalVar.gpy))
                # guanti
                guantiw = pygame.image.load("Immagini/EquipSara/Guanti/Guanti%iw.png" % dati[129])
                guantiw = pygame.transform.scale(guantiw, (GlobalVar.gpx, GlobalVar.gpy))
                guantiwMov1 = pygame.image.load("Immagini/EquipSara/Guanti/Guanti%iwMov1.png" % dati[129])
                guantiwMov1 = pygame.transform.scale(guantiwMov1, (GlobalVar.gpx, GlobalVar.gpy))
                guantiwMov2 = pygame.image.load("Immagini/EquipSara/Guanti/Guanti%iwMov2.png" % dati[129])
                guantiwMov2 = pygame.transform.scale(guantiwMov2, (GlobalVar.gpx, GlobalVar.gpy))
                guantia = pygame.image.load("Immagini/EquipSara/Guanti/Guanti%ia.png" % dati[129])
                guantia = pygame.transform.scale(guantia, (GlobalVar.gpx, GlobalVar.gpy))
                guantiaMov1 = pygame.image.load("Immagini/EquipSara/Guanti/Guanti%iaMov1.png" % dati[129])
                guantiaMov1 = pygame.transform.scale(guantiaMov1, (GlobalVar.gpx, GlobalVar.gpy))
                guantiaMov2 = pygame.image.load("Immagini/EquipSara/Guanti/Guanti%iaMov2.png" % dati[129])
                guantiaMov2 = pygame.transform.scale(guantiaMov2, (GlobalVar.gpx, GlobalVar.gpy))
                guantis = pygame.image.load("Immagini/EquipSara/Guanti/Guanti%is.png" % dati[129])
                guantis = pygame.transform.scale(guantis, (GlobalVar.gpx, GlobalVar.gpy))
                guantisMov1 = pygame.image.load("Immagini/EquipSara/Guanti/Guanti%isMov1.png" % dati[129])
                guantisMov1 = pygame.transform.scale(guantisMov1, (GlobalVar.gpx, GlobalVar.gpy))
                guantisMov2 = pygame.image.load("Immagini/EquipSara/Guanti/Guanti%isMov2.png" % dati[129])
                guantisMov2 = pygame.transform.scale(guantisMov2, (GlobalVar.gpx, GlobalVar.gpy))
                guantid = pygame.image.load("Immagini/EquipSara/Guanti/Guanti%id.png" % dati[129])
                guantid = pygame.transform.scale(guantid, (GlobalVar.gpx, GlobalVar.gpy))
                guantidMov1 = pygame.image.load("Immagini/EquipSara/Guanti/Guanti%idMov1.png" % dati[129])
                guantidMov1 = pygame.transform.scale(guantidMov1, (GlobalVar.gpx, GlobalVar.gpy))
                guantidMov2 = pygame.image.load("Immagini/EquipSara/Guanti/Guanti%idMov2.png" % dati[129])
                guantidMov2 = pygame.transform.scale(guantidMov2, (GlobalVar.gpx, GlobalVar.gpy))
                guantisAttacco = pygame.image.load("Immagini/EquipSara/Guanti/Guanti%isAttacco.png" % dati[129])
                guantisAttacco = pygame.transform.scale(guantisAttacco, (GlobalVar.gpx, GlobalVar.gpy))
                guantiaAttacco = pygame.image.load("Immagini/EquipSara/Guanti/Guanti%iaAttacco.png" % dati[129])
                guantiaAttacco = pygame.transform.scale(guantiaAttacco, (GlobalVar.gpx, GlobalVar.gpy))
                guantidAttacco = pygame.image.load("Immagini/EquipSara/Guanti/Guanti%idAttacco.png" % dati[129])
                guantidAttacco = pygame.transform.scale(guantidAttacco, (GlobalVar.gpx, GlobalVar.gpy))
                guantiwAttacco = pygame.image.load("Immagini/EquipSara/Guanti/Guanti%iwAttacco.png" % dati[129])
                guantiwAttacco = pygame.transform.scale(guantiwAttacco, (GlobalVar.gpx, GlobalVar.gpy))
                guantiDifesa = pygame.image.load("Immagini/EquipSara/Guanti/Guanti%iDifesa.png" % dati[129])
                guantiDifesa = pygame.transform.scale(guantiDifesa, (GlobalVar.gpx, GlobalVar.gpy))
                # collana
                collanaw = pygame.image.load("Immagini/EquipSara/Collane/Collana%iw.png" % dati[130])
                collanaw = pygame.transform.scale(collanaw, (GlobalVar.gpx, GlobalVar.gpy))
                collanaa = pygame.image.load("Immagini/EquipSara/Collane/Collana%ia.png" % dati[130])
                collanaa = pygame.transform.scale(collanaa, (GlobalVar.gpx, GlobalVar.gpy))
                collanas = pygame.image.load("Immagini/EquipSara/Collane/Collana%is.png" % dati[130])
                collanas = pygame.transform.scale(collanas, (GlobalVar.gpx, GlobalVar.gpy))
                collanad = pygame.image.load("Immagini/EquipSara/Collane/Collana%id.png" % dati[130])
                collanad = pygame.transform.scale(collanad, (GlobalVar.gpx, GlobalVar.gpy))
                # armatura robot
                armrobw = pygame.image.load("Immagini/EquipRobo/Batteria%iw.png" % dati[9])
                armrobw = pygame.transform.scale(armrobw, (GlobalVar.gpx, GlobalVar.gpy))
                armroba = pygame.image.load("Immagini/EquipRobo/Batteria%ia.png" % dati[9])
                armroba = pygame.transform.scale(armroba, (GlobalVar.gpx, GlobalVar.gpy))
                armrobs = pygame.image.load("Immagini/EquipRobo/Batteria%is.png" % dati[9])
                armrobs = pygame.transform.scale(armrobs, (GlobalVar.gpx, GlobalVar.gpy))
                armrobd = pygame.image.load("Immagini/EquipRobo/Batteria%id.png" % dati[9])
                armrobd = pygame.transform.scale(armrobd, (GlobalVar.gpx, GlobalVar.gpy))
            if agg == 1:
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
            if agg == 2:
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
            if agg == 3:
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
            if agg == 4:
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
            elif ((type(nemicoInquadrato) is str and nemicoInquadrato == "Colco") or (not nemicoInquadrato and dati[0] >= GlobalVar.avanzamentoStoriaIncontroColco)) and 0 <= yMouse <= GlobalVar.gsy // 18 * 1 and GlobalVar.gsx // 32 * 0 <= xMouse <= GlobalVar.gsx // 32 * 4:
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
            elif dati[0] >= GlobalVar.avanzamentoStoriaIncontroColco and 0 <= yMouse <= GlobalVar.gsy // 18 * 1.5 and GlobalVar.gsx // 32 * 27.8 < xMouse <= GlobalVar.gsx // 32 * 30.2:
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
        if not inquadratoQualcosa and GlobalVar.mouseVisibile:
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
                quit()

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
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selObbiettivo)
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
                    tastoTrovato = True
                    if not nemicoInquadrato:
                        nemicoInquadrato = "Colco"
                    elif type(nemicoInquadrato) is str and nemicoInquadrato == "Colco":
                        if len(listaNemiciVisti) > 0:
                            nemicoInquadrato = listaNemiciVisti[0]
                        elif len(listaEscheViste) > 0:
                            nemicoInquadrato = "Esca" + str(listaEscheViste[0])
                        else:
                            nemicoInquadrato = "Colco"
                    elif not type(nemicoInquadrato) is str and nemicoInquadrato:
                        if len(listaNemiciVisti) > 0 and listaNemiciVisti.index(nemicoInquadrato) < len(listaNemiciVisti) - 1:
                            nemicoInquadrato = listaNemiciVisti[listaNemiciVisti.index(nemicoInquadrato) + 1]
                        elif len(listaEscheViste) > 0:
                            nemicoInquadrato = "Esca" + str(listaEscheViste[0])
                        else:
                            nemicoInquadrato = "Colco"
                    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
                        if len(listaEscheViste) > 0 and listaEscheViste.index(int(nemicoInquadrato[4:])) + 3 < len(listaEscheViste) - 1:
                            nemicoInquadrato = "Esca" + str(listaEscheViste[listaEscheViste.index(int(nemicoInquadrato[4:])) + 4])
                        else:
                            nemicoInquadrato = "Colco"
                    caricaTutto = True
                if (event.key == pygame.K_2 or event.key == pygame.K_KP2) and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selObbiettivo)
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
                    tastoTrovato = True
                    if not nemicoInquadrato:
                        nemicoInquadrato = "Colco"
                    elif type(nemicoInquadrato) is str and nemicoInquadrato == "Colco":
                        if len(listaEscheViste) > 0:
                            nemicoInquadrato = "Esca" + str(listaEscheViste[len(listaEscheViste) - 4])
                        elif len(listaNemiciVisti) > 0:
                            nemicoInquadrato = listaNemiciVisti[len(listaNemiciVisti) - 1]
                        else:
                            nemicoInquadrato = "Colco"
                    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
                        if len(listaEscheViste) > 0 and listaEscheViste.index(int(nemicoInquadrato[4:])) != 0:
                            nemicoInquadrato = "Esca" + str(listaEscheViste[listaEscheViste.index(int(nemicoInquadrato[4:])) - 4])
                        elif len(listaNemiciVisti) > 0:
                            nemicoInquadrato = listaNemiciVisti[len(listaNemiciVisti) - 1]
                        else:
                            nemicoInquadrato = "Colco"
                    elif not type(nemicoInquadrato) is str and nemicoInquadrato:
                        if len(listaNemiciVisti) > 0 and listaNemiciVisti.index(nemicoInquadrato) != 0:
                            nemicoInquadrato = listaNemiciVisti[listaNemiciVisti.index(nemicoInquadrato) - 1]
                        else:
                            nemicoInquadrato = "Colco"
                    caricaTutto = True
                if event.key == pygame.K_SPACE and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento:
                    tastoTrovato = True
                    nx = 0
                    ny = 0
                    # apertura porte
                    k = 0
                    while k < len(porte):
                        if porte[k] == dati[1] and ((porte[k + 1] == x + GlobalVar.gpx and porte[k + 2] == y and npers == 1) or (
                                porte[k + 1] == x - GlobalVar.gpx and porte[k + 2] == y and npers == 2) or (
                                                            porte[k + 1] == x and porte[
                                                        k + 2] == y + GlobalVar.gpy and npers == 4) or (
                                                            porte[k + 1] == x and porte[
                                                        k + 2] == y - GlobalVar.gpy and npers == 3)) and not porte[k + 3]:
                            sposta = True
                            GlobalVar.canaleSoundInterazioni.play(rumoreAperturaPorte)
                            porte[k + 3] = True
                            # scoprire caselle viste
                            casevistePorteIncluse = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, caseviste, False)
                            casevistePorteIncluse = casevistePorteIncluse[:]
                            caseviste = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, caseviste)
                            caricaTutto = True
                            # aggiornare vettore tutteporte
                            j = 0
                            while j < len(tutteporte):
                                if tutteporte[j] == porte[k] and tutteporte[j + 1] == porte[k + 1] and tutteporte[
                                    j + 2] == porte[k + 2]:
                                    tutteporte[j + 3] = True
                                j = j + 4
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
                            dati, tesoro = aperturacofanetto(cofanetti[i], cofanetti[i + 1], cofanetti[i + 2], dati)
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
                            dati[0], oggettoRicevuto, visualizzaMenuMercante = dialoga(dati[0], personaggio)
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
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                nx = 0
                ny = 0
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
                    sposta = True
                    GlobalVar.canaleSoundInterazioni.play(rumoreAperturaPorte)
                    porte[posizPortaInVettore + 3] = True
                    # scoprire caselle viste
                    casevistePorteIncluse = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, caseviste, False)
                    casevistePorteIncluse = casevistePorteIncluse[:]
                    caseviste = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, caseviste)
                    caricaTutto = True
                    # aggiornare vettore tutteporte
                    j = 0
                    while j < len(tutteporte):
                        if tutteporte[j] == porte[posizPortaInVettore] and tutteporte[j + 1] == porte[posizPortaInVettore + 1] and tutteporte[j + 2] == porte[posizPortaInVettore + 2]:
                            tutteporte[j + 3] = True
                        j += 4
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
                    dati, tesoro = aperturacofanetto(cofanetti[posizCofanettoInVettore], cofanetti[posizCofanettoInVettore + 1], cofanetti[posizCofanettoInVettore + 2], dati)
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
                    dati[0], oggettoRicevuto, visualizzaMenuMercante = dialoga(dati[0], personaggio)
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

        # ripristina vita e status dopo lv up
        if aumentoliv != 0:
            dati[5] = pvtot
            dati[121] = False
            aumentoliv = 0

        if inquadratoQualcosa and (inquadratoQualcosa.startswith("movimento") or inquadratoQualcosa.startswith("personaggio")) and movimentoPerMouse and mosseRimasteRob <= 0 and not nemiciInMovimento and not impossibileCliccarePulsanti and not startf:
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
            if inquadratoQualcosa.startswith("movimento"):
                inquadratoQualcosaList = inquadratoQualcosa.split(":")
                xObbiettivo = int(inquadratoQualcosaList[1])
                yObbiettivo = int(inquadratoQualcosaList[2])
            elif inquadratoQualcosa.startswith("personaggio"):
                inquadratoQualcosaList = inquadratoQualcosa.split(":")
                xObbiettivo = listaPersonaggi[int(inquadratoQualcosaList[1])].x
                yObbiettivo = listaPersonaggi[int(inquadratoQualcosaList[1])].y
            if x == xObbiettivo and y == yObbiettivo:
                GlobalVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
            else:
                percorsoTrovato = pathFinding(x, y, xObbiettivo, yObbiettivo, dati[1], porte, cofanetti, vetNemiciSoloConXeY, False)
                if percorsoTrovato:
                    if len(percorsoTrovato) >= 4:
                        if percorsoTrovato[len(percorsoTrovato) - 4] != x or percorsoTrovato[len(percorsoTrovato) - 3] != y:
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
                    if abs(xObbiettivo - x) > abs(yObbiettivo - y):
                        if x < xObbiettivo:
                            npers = 1
                        if x > xObbiettivo:
                            npers = 2
                        sposta = True
                    if abs(yObbiettivo - y) > abs(xObbiettivo - x):
                        if y < yObbiettivo:
                            npers = 4
                        if y > yObbiettivo:
                            npers = 3
                        sposta = True
                    if (abs(xObbiettivo - x) == abs(yObbiettivo - y)) and (xObbiettivo != x) and (yObbiettivo != y):
                        c = random.randint(1, 2)
                        if x < xObbiettivo and c == 1:
                            npers = 1
                        if x > xObbiettivo and c == 1:
                            npers = 2
                        if y < yObbiettivo and c == 2:
                            npers = 4
                        if y > yObbiettivo and c == 2:
                            npers = 3
                        sposta = True
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
                # cambiare posizione
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
            dati[134] = rx
            dati[135] = ry
            if not apriocchio:
                dati, inizio, attacco, caricaSalvataggio = start(dati, porteini, portefin, cofaniini, cofanifin, tutteporte, tutticofanetti, listaNemiciTotali, vitaesca, vettoreDenaro, stanzeGiaVisitate, listaPersonaggiTotali)
                if caricaSalvataggio:
                    inizio = True
                if attacco == 0:
                    uscitoDaMenu = 2
            else:
                dati, attacco, sposta, animaOggetto, npers, caricaSalvataggio, inizio = startBattaglia(dati, animaOggetto, x, y, npers, rx, ry, inizio)
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
                animaOggettoSpecialeRicevuto(oggettoRicevuto)
                oggettoRicevuto = False
                caricaTutto = True

            # movimento-azioni personaggio
            if (nx != 0 or ny != 0) and not nemiciInMovimento and mosseRimasteRob <= 0:
                vx = x
                vy = y
                sposta = True
                stanzaVecchia = dati[1]
                x, y, dati[1], carim, cambiosta = muri_porte(x, y, nx, ny, dati[1], carim, False, False, porte, cofanetti)

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
                sposta, creaesca, xesca, yesca, npers, nrob, difesa, apriChiudiPorta, apriCofanetto, spingiColco, listaNemici, attacco, attaccoADistanza, nemicoInquadrato, attaccoDiRallo, chiamarob, ultimoObbiettivoColco, animaOggetto, interagisciConPersonaggio, startf = attacca(x, y, npers, nrob, rx, ry, pers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126], imgSfondoStanza, dati[1], sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, attVicino, attLontano, attacco, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, vettoreDenaro, dati[132], nemicoInquadrato, raffredda, autoRic1, autoRic2, ultimoObbiettivoColco, animaOggetto, listaPersonaggi, startf, dati[0])
                tastop = 0
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
                dati[5] = dati[5] - 5
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
                        casevistePorteIncluse = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, caseviste, False)
                        casevistePorteIncluse = casevistePorteIncluse[:]
                        caseviste = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, caseviste)
                        # aggiornare vettore tutteporte
                        j = 0
                        while j < len(tutteporte):
                            if tutteporte[j] == porte[k] and tutteporte[j + 1] == porte[k + 1] and tutteporte[j + 2] == porte[k + 2]:
                                tutteporte[j + 3] = porte[k + 3]
                            j = j + 4
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
                        dati[0], oggettoRicevuto, visualizzaMenuMercante = dialoga(dati[0], personaggio)
                        caricaTutto = True
                interagisciConPersonaggio = False
            # menu mercante
            if visualizzaMenuMercante:
                dati = menuMercante(dati)
                visualizzaMenuMercante = False
                uscitoDaMenu = 1
            # apertura cofanetti
            if apriCofanetto[0]:
                i = 0
                while i < len(cofanetti):
                    if cofanetti[i] == dati[1] and cofanetti[i + 1] == apriCofanetto[1] and cofanetti[i + 2] == apriCofanetto[2] and not cofanetti[i + 3]:
                        GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoaperturacofanetti)
                        dati, tesoro = aperturacofanetto(cofanetti[i], cofanetti[i + 1], cofanetti[i + 2], dati)
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
            if dati[0] >= GlobalVar.avanzamentoStoriaIncontroColco and rx == GlobalVar.gsx and ry == GlobalVar.gsy:
                rx = x
                ry = y
                vrx = rx
                vry = ry
            azioneRobEseguita = False
            if dati[0] >= GlobalVar.avanzamentoStoriaIncontroColco and dati[122] > 0:
                # se surriscaldato toglie vel+ e efficienza
                dati[125] = 0
                dati[126] = 0
            if dati[0] >= GlobalVar.avanzamentoStoriaIncontroColco and sposta and mosseRimasteRob == 0 and not morterob:
                if dati[125] > 0:
                    mosseRimasteRob = 2
                else:
                    mosseRimasteRob = 1
            # effetto di surriscalda / raffreddamento / auto-ricarica / auto-ricarica+
            if dati[0] >= GlobalVar.avanzamentoStoriaIncontroColco and sposta:
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
            if dati[0] >= GlobalVar.avanzamentoStoriaIncontroColco and mosseRimasteRob > 0 and not morterob and not cambiosta:
                vrx = rx
                vry = ry

                # movimento - gambit
                if raffredda < 0 and autoRic1 < 0 and autoRic2 < 0:
                    rx, ry, nrob, dati, listaNemici, raffreddamento, ricarica1, ricarica2, azioneRobEseguita, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, attaccoDiColco, ultimoObbiettivoColco, obbiettivoCasualeColco = movrobo(x, y, vx, vy, rx, ry, dati[1], chiamarob, dati, porte, cofanetti, listaNemici, nmost, difesa, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggi)

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
            elif dati[0] >= GlobalVar.avanzamentoStoriaIncontroColco and sposta and mosseRimasteRob < 0 and not morterob:
                mosseRimasteRob += 1
            if dati[0] >= GlobalVar.avanzamentoStoriaIncontroColco and morterob:
                robot = GlobalVar.robomo
                armrob = GlobalVar.armrobmo
            if dati[0] < GlobalVar.avanzamentoStoriaIncontroColco:
                rx = GlobalVar.gsx
                ry = GlobalVar.gsy
                vrx = rx
                vry = ry

            # movimento-azioni mostri
            if nmost > 0 and not cambiosta:
                for nemico in listaNemici:
                    vetDatiNemici = []
                    for nemicoTemp in listaNemici:
                        vetDatiNemici.append(nemicoTemp.vita)
                        vetDatiNemici.append(nemicoTemp.x)
                        vetDatiNemici.append(nemicoTemp.y)
                        vetDatiNemici.append(nemicoTemp.vitaTotale)
                    if nemico.avvelenato and sposta:
                        nemico.vita -= 3
                    incasevista = False
                    i = 0
                    while i < len(caseviste):
                        if caseviste[i + 2] and caseviste[i] == nemico.x and caseviste[i + 1] == nemico.y:
                            incasevista = True
                            break
                        i += 3
                    if nemico.vita > 0 and incasevista:
                        # trovo l'obbiettivo
                        nemicoVistoRallo, nemicoVistoRob, nemicoVistoesca, nemicoEscabersaglio, nemicoVistoDenaro, nemicoXDenaro, nemicoYDenaro, attrobo = nemico.settaObbiettivo(x, y, rx, ry, dati, stanza, porte, cofanetti, vettoreDenaro, vitaesca, attaccoADistanza, listaNemiciAttaccatiADistanzaRobo)
                        if sposta and nemico.mosseRimaste == 0:
                            nemico.resettaMosseRimaste()
                        if nemico.mosseRimaste > 0:
                            nemico.vx = nemico.x
                            nemico.vy = nemico.y
                            nemico, direzioneMostro, dati, vitaesca = movmostro(x, y, rx, ry, nemico, dati[1], dif, difro, par, dati, vitaesca, porte, cofanetti, vetDatiNemici, nemicoVistoRallo, nemicoVistoRob, nemicoVistoesca, nemicoEscabersaglio, nemicoVistoDenaro, nemicoXDenaro, nemicoYDenaro, attrobo, listaPersonaggi)
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
                    # controllo se il personaggio è in una casella vista
                    personaggio.inCasellaVista = False
                    i = 0
                    while i < len(caseviste):
                        if caseviste[i + 2] and caseviste[i] == personaggio.x and caseviste[i + 1] == personaggio.y:
                            personaggio.inCasellaVista = True
                            break
                        i += 3
                    if personaggio.inCasellaVista:
                        personaggio.spostati(x, y, rx, ry, listaNemici)

            # aumentare di livello
            if not carim:
                while dati[127] >= esptot and dati[4] < 100:
                    dati[4] += 1
                    dati[127] -= esptot
                    aumentoliv += 1
                    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati, difesa)
                    impossibileCliccarePulsanti = True

            # aggiorna vista dei mostri e metti l'occhio se ti vedono + aggiorna nemico.inCasellaVista
            apriocchio = False
            for nemico in listaNemici:
                nemico.inCasellaVista = False
                i = 0
                while i < len(caseviste):
                    if caseviste[i + 2] and caseviste[i] == nemico.x and caseviste[i + 1] == nemico.y:
                        nemico.inCasellaVista = True
                        break
                    i += 3
                if (abs(x - nemico.x) <= nemico.raggioVisivo and abs(y - nemico.y) <= nemico.raggioVisivo) or (abs(rx - nemico.x) <= nemico.raggioVisivo and abs(ry - nemico.y) <= nemico.raggioVisivo):
                    if nemico.vita > 0 and nemico.inCasellaVista:
                        nemico.aggiornaVista(x, y, rx, ry, dati[1], porte, cofanetti, dati)
                        if nemico.visto:
                            apriocchio = True

            # fai tutte le animazioni del turno e disegni gli sfondi e personaggi
            if caricaTutto:
                if aumentoliv != 0:
                    pvtot = getVitaTotRallo(dati[4] - aumentoliv, dati[129])
                disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, eschePrimaDelTurno, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, dati[0])
                caricaTutto = False
            if azioneRobEseguita or nemiciInMovimento or sposta:
                primopasso, caricaTutto, tesoro, tastop, movimentoPerMouse = anima(sposta, x, y, vx, vy, rx, ry, vrx, vry, pers, robot, npers, nrob, primopasso, cambiosta, sfondinoa, sfondinob, scudo, armatura, arma, armaMov1, armaMov2, armaAttacco, scudoDifesa, arco, faretra, arcoAttacco, guanti, guantiMov1, guantiMov2, guantiAttacco, guantiDifesa, collana, armas, armaturas, arcos, faretras, collanas, armrob, armrobs, dati, attacco, difesa, tastop, tesoro, sfondinoc, aumentoliv, carim, caricaTutto, listaNemici, vitaesca, vettoreDenaro, attaccoADistanza, caseviste, porte, cofanetti, portaOriz, portaVert, stanza, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoInquadrato, attaccoDiRallo, attaccoDiColco, statoRalloInizioTurno, statoColcoInizioTurno, statoEscheInizioTurno, raffreddamento, ricarica1, ricarica2, raffredda, autoRic1, autoRic2, animaOggetto, eschePrimaDelTurno, listaPersonaggi, movimentoPerMouse)
            if not carim:
                pvtot = getVitaTotRallo(dati[4], dati[129])
                disegnaAmbiente(x, y, npers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, eschePrimaDelTurno, listaPersonaggi, False, stanzaCambiata, uscitoDaMenu, dati[0])

            if aumentoliv == 0:
                caricaTutto = False

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

            # aggiorna i dialoghi di tutti i personaggi in base all'avanzamento nella storia
            for personaggio in listaPersonaggi:
                personaggio.aggiornaDialogo(dati[0])

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
