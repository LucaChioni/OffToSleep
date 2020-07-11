# -*- coding: utf-8 -*-

from MenuG2 import *
from EnvPrintG2 import *
from MovNemiciRobG2 import *
from AnimazioniG2 import *
from PersonaggioObj import *


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
            dati, porteini, portefin, cofaniini, cofanifin, listaNemiciTotali, vitaesca, vettoreDenaro, stanzeGiaVisitate, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggiTotali = menu(caricaSalvataggio)
            caricaSalvataggio = False
            pers = GlobalVarG2.perss
            robot = GlobalVarG2.robos
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
            if cambiosta:
                sprites = pygame.sprite.Group(Fade(0))
                schermoFadeToBlack = GlobalVarG2.schermo.copy()
                i = 0
                while i <= 6:
                    sprites.update()
                    GlobalVarG2.schermo.blit(schermoFadeToBlack, (0, 0))
                    sprites.draw(GlobalVarG2.schermo)
                    pygame.display.update()
                    GlobalVarG2.clockFadeToBlack.tick(GlobalVarG2.fpsFadeToBlack)
                    i += 1

            if pers == GlobalVarG2.persw:
                agg = 1
            if pers == GlobalVarG2.persa:
                agg = 2
            if pers == GlobalVarG2.perss:
                agg = 3
            if pers == GlobalVarG2.persd:
                agg = 4

            # mostri - personaggi
            if dati[1] == 1 and cambiosta:
                # rumore porte
                rumoreAperturaPorte = GlobalVarG2.suonoaperturaporte1
                rumoreChiusuraPorte = GlobalVarG2.suonochiusuraporte1

                # posizione personaggio e robot al cambio stanza
                if not inizio:
                    if stanzaVecchia == 2:
                        npers = 4
                        nrob = 3
                        x = GlobalVarG2.gsx // 32 * 6
                        y = GlobalVarG2.gsy // 18 * 2
                        pers = GlobalVarG2.perss
                        robot = GlobalVarG2.robos
                        agg = 3
                    vx = x
                    vy = y
                    rx = x
                    ry = y
                    vrx = x
                    vry = y

                listaNemici = []
                if not dati[1] in stanzeGiaVisitate:
                    percorsoNemico = ["w", "a", "a", "s", "d", "d"]
                    nemico = NemicoObj(GlobalVarG2.gsx // 32 * 29, GlobalVarG2.gsy // 18 * 15, "w", "Orco", dati[1], percorsoNemico)
                    listaNemiciTotali.append(nemico)
                    listaNemici.append(nemico)
                    percorsoNemico = ["w", "a", "a", "s", "d", "d"]
                    nemico = NemicoObj(GlobalVarG2.gsx // 32 * 3, GlobalVarG2.gsy // 18 * 3, "a", "Orco", dati[1], percorsoNemico)
                    listaNemiciTotali.append(nemico)
                    listaNemici.append(nemico)
                    percorsoNemico = ["w", "a", "a", "s", "d", "d"]
                    nemico = NemicoObj(GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 7, "s", "Pipistrello", dati[1], percorsoNemico)
                    listaNemiciTotali.append(nemico)
                    listaNemici.append(nemico)
                    percorsoNemico = ["w", "a", "a", "s", "d", "d"]
                    nemico = NemicoObj(GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 14, "d", "Orco", dati[1], percorsoNemico)
                    listaNemiciTotali.append(nemico)
                    listaNemici.append(nemico)
                    percorsoNemico = ["w", "a", "a", "s", "d", "d"]
                    nemico = NemicoObj(GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4, "s", "Pipistrello", dati[1], percorsoNemico)
                    listaNemiciTotali.append(nemico)
                    listaNemici.append(nemico)
                else:
                    for nemico in listaNemiciTotali:
                        if nemico.stanzaDiAppartenenza == dati[1]:
                            listaNemici.append(nemico)
                nmost = len(listaNemici)

                listaPersonaggi = []
                if not dati[1] in stanzeGiaVisitate:
                    percorsoPersonaggio = ["w", "a", "a", "s", "d", "d"]
                    personaggio = PersonaggioObj(GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 4, "d", "Mercante", dati[1], dati[0], percorsoPersonaggio)
                    listaPersonaggiTotali.append(personaggio)
                    listaPersonaggi.append(personaggio)
                else:
                    for personaggio in listaPersonaggiTotali:
                        if personaggio.stanzaDiAppartenenza == dati[1]:
                            listaPersonaggi.append(personaggio)

                if not dati[1] in stanzeGiaVisitate:
                    stanzeGiaVisitate.append(dati[1])

            if dati[1] == 2 and cambiosta:
                # rumore porte
                rumoreAperturaPorte = GlobalVarG2.suonoaperturaporte2
                rumoreChiusuraPorte = GlobalVarG2.suonochiusuraporte2

                # posizione personaggio e robot al cambio stanza
                if not inizio:
                    if stanzaVecchia == 1:
                        npers = 4
                        nrob = 3
                        x = GlobalVarG2.gsx // 32 * 6
                        y = GlobalVarG2.gsy // 18 * 2
                        pers = GlobalVarG2.perss
                        robot = GlobalVarG2.robos
                        agg = 3
                    vx = x
                    vy = y
                    rx = x
                    ry = y
                    vrx = x
                    vry = y

                listaNemici = []
                if not dati[1] in stanzeGiaVisitate:
                    percorsoNemico = ["w", "a", "a", "s", "d", "d"]
                    nemico = NemicoObj(GlobalVarG2.gsx // 32 * 29, GlobalVarG2.gsy // 18 * 15, "w", "Orco", dati[1], percorsoNemico)
                    listaNemiciTotali.append(nemico)
                    listaNemici.append(nemico)
                else:
                    for nemico in listaNemiciTotali:
                        if nemico.stanzaDiAppartenenza == dati[1]:
                            listaNemici.append(nemico)
                nmost = len(listaNemici)

                listaPersonaggi = []
                if not dati[1] in stanzeGiaVisitate:
                    percorsoPersonaggio = ["w", "", "d", "s", "a"]
                    personaggio = PersonaggioObj(GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 4, "d", "Mercante", dati[1], dati[0], percorsoPersonaggio)
                    listaPersonaggi.append(personaggio)
                    listaPersonaggiTotali.append(personaggio)
                    percorsoPersonaggio = []
                    personaggio = PersonaggioObj(GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 3, "a", "FiglioUfficiale", dati[1], dati[0], percorsoPersonaggio)
                    listaPersonaggi.append(personaggio)
                    listaPersonaggiTotali.append(personaggio)
                else:
                    for personaggio in listaPersonaggiTotali:
                        if personaggio.stanzaDiAppartenenza == dati[1]:
                            listaPersonaggi.append(personaggio)

                if not dati[1] in stanzeGiaVisitate:
                    stanzeGiaVisitate.append(dati[1])

            if cambiosta:
                # stanza
                imgSfondoStanza = pygame.image.load("Immagini/Paesaggi/Stanza%ia.png" % dati[1]).convert()
                imgSfondoStanza = pygame.transform.scale(imgSfondoStanza, (GlobalVarG2.gsx, GlobalVarG2.gsy))
                sfondinoa = pygame.image.load("Immagini/Paesaggi/Sfondino%ia.png" % dati[1]).convert()
                sfondinoa = pygame.transform.scale(sfondinoa, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                sfondinob = pygame.image.load("Immagini/Paesaggi/Sfondino%ib.png" % dati[1]).convert()
                sfondinob = pygame.transform.scale(sfondinob, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                sfondinoc = pygame.image.load("Immagini/Paesaggi/Sfondino%ic.png" % dati[1]).convert()
                sfondinoc = pygame.transform.scale(sfondinoc, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                portaVert = pygame.image.load("Immagini/Paesaggi/PortaV%i.png" % dati[1])
                portaVert = pygame.transform.scale(portaVert, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                portaOriz = pygame.image.load("Immagini/Paesaggi/PortaO%i.png" % dati[1])
                portaOriz = pygame.transform.scale(portaOriz, (GlobalVarG2.gpx, GlobalVarG2.gpy))

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
                        caseviste.append(GlobalVarG2.gpx + (GlobalVarG2.gpx * n))
                        caseviste.append(GlobalVarG2.gpy + (GlobalVarG2.gpy * m))
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
                armaw = pygame.image.load("Immagini/EquipRallo/Spade/Spada%iw.png" % dati[6])
                armaw = pygame.transform.scale(armaw, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armawMov1 = pygame.image.load("Immagini/EquipRallo/Spade/Spada%iwMov1.png" % dati[6])
                armawMov1 = pygame.transform.scale(armawMov1, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armawMov2 = pygame.image.load("Immagini/EquipRallo/Spade/Spada%iwMov2.png" % dati[6])
                armawMov2 = pygame.transform.scale(armawMov2, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armaa = pygame.image.load("Immagini/EquipRallo/Spade/Spada%ia.png" % dati[6])
                armaa = pygame.transform.scale(armaa, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armaaMov1 = pygame.image.load("Immagini/EquipRallo/Spade/Spada%iaMov1.png" % dati[6])
                armaaMov1 = pygame.transform.scale(armaaMov1, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armaaMov2 = pygame.image.load("Immagini/EquipRallo/Spade/Spada%iaMov2.png" % dati[6])
                armaaMov2 = pygame.transform.scale(armaaMov2, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armas = pygame.image.load("Immagini/EquipRallo/Spade/Spada%is.png" % dati[6])
                armas = pygame.transform.scale(armas, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armasMov1 = pygame.image.load("Immagini/EquipRallo/Spade/Spada%isMov1.png" % dati[6])
                armasMov1 = pygame.transform.scale(armasMov1, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armasMov2 = pygame.image.load("Immagini/EquipRallo/Spade/Spada%isMov2.png" % dati[6])
                armasMov2 = pygame.transform.scale(armasMov2, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armad = pygame.image.load("Immagini/EquipRallo/Spade/Spada%id.png" % dati[6])
                armad = pygame.transform.scale(armad, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armadMov1 = pygame.image.load("Immagini/EquipRallo/Spade/Spada%idMov1.png" % dati[6])
                armadMov1 = pygame.transform.scale(armadMov1, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armadMov2 = pygame.image.load("Immagini/EquipRallo/Spade/Spada%idMov2.png" % dati[6])
                armadMov2 = pygame.transform.scale(armadMov2, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armasAttacco = pygame.image.load("Immagini/EquipRallo/Spade/Spada%isAttacco.png" % dati[6])
                armasAttacco = pygame.transform.scale(armasAttacco, (GlobalVarG2.gpx, GlobalVarG2.gpy * 2))
                armaaAttacco = pygame.image.load("Immagini/EquipRallo/Spade/Spada%iaAttacco.png" % dati[6])
                armaaAttacco = pygame.transform.scale(armaaAttacco, (GlobalVarG2.gpx * 2, GlobalVarG2.gpy))
                armadAttacco = pygame.image.load("Immagini/EquipRallo/Spade/Spada%idAttacco.png" % dati[6])
                armadAttacco = pygame.transform.scale(armadAttacco, (GlobalVarG2.gpx * 2, GlobalVarG2.gpy))
                armawAttacco = pygame.image.load("Immagini/EquipRallo/Spade/Spada%iwAttacco.png" % dati[6])
                armawAttacco = pygame.transform.scale(armawAttacco, (GlobalVarG2.gpx, GlobalVarG2.gpy * 2))
                # arco
                arcow = pygame.image.load("Immagini/EquipRallo/Archi/Arco%iw.png" % dati[128])
                arcow = pygame.transform.scale(arcow, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                arcoa = pygame.image.load("Immagini/EquipRallo/Archi/Arco%ia.png" % dati[128])
                arcoa = pygame.transform.scale(arcoa, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                arcos = pygame.image.load("Immagini/EquipRallo/Archi/Arco%is.png" % dati[128])
                arcos = pygame.transform.scale(arcos, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                arcod = pygame.image.load("Immagini/EquipRallo/Archi/Arco%id.png" % dati[128])
                arcod = pygame.transform.scale(arcod, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                arcosAttacco = pygame.image.load("Immagini/EquipRallo/Archi/Arco%isAttacco.png" % dati[128])
                arcosAttacco = pygame.transform.scale(arcosAttacco, (GlobalVarG2.gpx, GlobalVarG2.gpy * 2))
                arcoaAttacco = pygame.image.load("Immagini/EquipRallo/Archi/Arco%iaAttacco.png" % dati[128])
                arcoaAttacco = pygame.transform.scale(arcoaAttacco, (GlobalVarG2.gpx * 2, GlobalVarG2.gpy))
                arcodAttacco = pygame.image.load("Immagini/EquipRallo/Archi/Arco%idAttacco.png" % dati[128])
                arcodAttacco = pygame.transform.scale(arcodAttacco, (GlobalVarG2.gpx * 2, GlobalVarG2.gpy))
                arcowAttacco = pygame.image.load("Immagini/EquipRallo/Archi/Arco%iwAttacco.png" % dati[128])
                arcowAttacco = pygame.transform.scale(arcowAttacco, (GlobalVarG2.gpx, GlobalVarG2.gpy * 2))
                # faretra
                faretraw = pygame.image.load("Immagini/EquipRallo/Faretre/Faretra%iw.png" % dati[133])
                faretraw = pygame.transform.scale(faretraw, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                faretraa = pygame.image.load("Immagini/EquipRallo/Faretre/Faretra%ia.png" % dati[133])
                faretraa = pygame.transform.scale(faretraa, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                faretras = pygame.image.load("Immagini/EquipRallo/Faretre/Faretra%is.png" % dati[133])
                faretras = pygame.transform.scale(faretras, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                faretrad = pygame.image.load("Immagini/EquipRallo/Faretre/Faretra%id.png" % dati[133])
                faretrad = pygame.transform.scale(faretrad, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                # armatura
                armaturaw = pygame.image.load("Immagini/EquipRallo/Armature/Armatura%iw.png" % dati[8])
                armaturaw = pygame.transform.scale(armaturaw, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armaturaa = pygame.image.load("Immagini/EquipRallo/Armature/Armatura%ia.png" % dati[8])
                armaturaa = pygame.transform.scale(armaturaa, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armaturas = pygame.image.load("Immagini/EquipRallo/Armature/Armatura%is.png" % dati[8])
                armaturas = pygame.transform.scale(armaturas, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armaturad = pygame.image.load("Immagini/EquipRallo/Armature/Armatura%id.png" % dati[8])
                armaturad = pygame.transform.scale(armaturad, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                # scudo
                scudow = pygame.image.load("Immagini/EquipRallo/Scudi/Scudo%iw.png" % dati[7])
                scudow = pygame.transform.scale(scudow, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                scudoa = pygame.image.load("Immagini/EquipRallo/Scudi/Scudo%ia.png" % dati[7])
                scudoa = pygame.transform.scale(scudoa, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                scudos = pygame.image.load("Immagini/EquipRallo/Scudi/Scudo%is.png" % dati[7])
                scudos = pygame.transform.scale(scudos, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                scudod = pygame.image.load("Immagini/EquipRallo/Scudi/Scudo%id.png" % dati[7])
                scudod = pygame.transform.scale(scudod, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                scudoDifesa = pygame.image.load("Immagini/EquipRallo/Scudi/Scudo%iDifesa.png" % dati[7])
                scudoDifesa = pygame.transform.scale(scudoDifesa, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                # guanti
                guantiw = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%iw.png" % dati[129])
                guantiw = pygame.transform.scale(guantiw, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                guantiwMov1 = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%iwMov1.png" % dati[129])
                guantiwMov1 = pygame.transform.scale(guantiwMov1, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                guantiwMov2 = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%iwMov2.png" % dati[129])
                guantiwMov2 = pygame.transform.scale(guantiwMov2, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                guantia = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%ia.png" % dati[129])
                guantia = pygame.transform.scale(guantia, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                guantiaMov1 = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%iaMov1.png" % dati[129])
                guantiaMov1 = pygame.transform.scale(guantiaMov1, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                guantiaMov2 = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%iaMov2.png" % dati[129])
                guantiaMov2 = pygame.transform.scale(guantiaMov2, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                guantis = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%is.png" % dati[129])
                guantis = pygame.transform.scale(guantis, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                guantisMov1 = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%isMov1.png" % dati[129])
                guantisMov1 = pygame.transform.scale(guantisMov1, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                guantisMov2 = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%isMov2.png" % dati[129])
                guantisMov2 = pygame.transform.scale(guantisMov2, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                guantid = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%id.png" % dati[129])
                guantid = pygame.transform.scale(guantid, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                guantidMov1 = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%idMov1.png" % dati[129])
                guantidMov1 = pygame.transform.scale(guantidMov1, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                guantidMov2 = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%idMov2.png" % dati[129])
                guantidMov2 = pygame.transform.scale(guantidMov2, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                guantisAttacco = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%isAttacco.png" % dati[129])
                guantisAttacco = pygame.transform.scale(guantisAttacco, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                guantiaAttacco = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%iaAttacco.png" % dati[129])
                guantiaAttacco = pygame.transform.scale(guantiaAttacco, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                guantidAttacco = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%idAttacco.png" % dati[129])
                guantidAttacco = pygame.transform.scale(guantidAttacco, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                guantiwAttacco = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%iwAttacco.png" % dati[129])
                guantiwAttacco = pygame.transform.scale(guantiwAttacco, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                guantiDifesa = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%iDifesa.png" % dati[129])
                guantiDifesa = pygame.transform.scale(guantiDifesa, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                # collana
                collanaw = pygame.image.load("Immagini/EquipRallo/Collane/Collana%iw.png" % dati[130])
                collanaw = pygame.transform.scale(collanaw, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                collanaa = pygame.image.load("Immagini/EquipRallo/Collane/Collana%ia.png" % dati[130])
                collanaa = pygame.transform.scale(collanaa, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                collanas = pygame.image.load("Immagini/EquipRallo/Collane/Collana%is.png" % dati[130])
                collanas = pygame.transform.scale(collanas, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                collanad = pygame.image.load("Immagini/EquipRallo/Collane/Collana%id.png" % dati[130])
                collanad = pygame.transform.scale(collanad, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                # armatura robot
                armrobw = pygame.image.load("Immagini/EquipRobo/Batteria%iw.png" % dati[9])
                armrobw = pygame.transform.scale(armrobw, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armroba = pygame.image.load("Immagini/EquipRobo/Batteria%ia.png" % dati[9])
                armroba = pygame.transform.scale(armroba, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armrobs = pygame.image.load("Immagini/EquipRobo/Batteria%is.png" % dati[9])
                armrobs = pygame.transform.scale(armrobs, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                armrobd = pygame.image.load("Immagini/EquipRobo/Batteria%id.png" % dati[9])
                armrobd = pygame.transform.scale(armrobd, (GlobalVarG2.gpx, GlobalVarG2.gpy))
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
                    robot = GlobalVarG2.robod
                    armrob = armrobd
                if nrob == 2:
                    robot = GlobalVarG2.roboa
                    armrob = armroba
                if nrob == 3:
                    robot = GlobalVarG2.robos
                    armrob = armrobs
                if nrob == 4:
                    robot = GlobalVarG2.robow
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
            robot = GlobalVarG2.robos
            armrob = armrobs
            inizio = False

        if nmost == -1:
            listaNemiciTotali = []
            stanzeGiaVisitate = []
            ultimoObbiettivoColco = []
            obbiettivoCasualeColco = False

        if tastop == 0:
            GlobalVarG2.canaleSoundPassiRallo.stop()
            nx = 0
            ny = 0

        inquadratoQualcosa = False
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVarG2.mouseVisibile:
            pygame.mouse.set_visible(True)
            GlobalVarG2.mouseVisibile = True
        if GlobalVarG2.mouseVisibile:
            # controlle se il cursore è sul pers in basso a sinistra / nemico in alto a sinistra / telecolco / personaggio / porta / cofanetto / casella vista
            if GlobalVarG2.gsy // 18 * 17 <= yMouse <= GlobalVarG2.gsy and GlobalVarG2.gsx // 32 * 0 <= xMouse <= GlobalVarG2.gsx // 32 * 6:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                inquadratoQualcosa = "start"
            elif ((type(nemicoInquadrato) is str and nemicoInquadrato == "Colco") or not nemicoInquadrato) and 0 <= yMouse <= GlobalVarG2.gsy // 18 * 1 and GlobalVarG2.gsx // 32 * 0 <= xMouse <= GlobalVarG2.gsx // 32 * 4:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and 0 <= yMouse <= GlobalVarG2.gsy // 18 * 1 and GlobalVarG2.gsx // 32 * 0 <= xMouse <= GlobalVarG2.gsx // 32 * 1:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif nemicoInquadrato and not type(nemicoInquadrato) is str and 0 <= yMouse <= GlobalVarG2.gsy // 18 * 1 and GlobalVarG2.gsx // 32 * 0 <= xMouse <= GlobalVarG2.gsx // 32 * 3:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif 0 <= yMouse <= GlobalVarG2.gsy // 18 * 1.5 and GlobalVarG2.gsx // 32 * 27.8 < xMouse <= GlobalVarG2.gsx // 32 * 30.2:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                inquadratoQualcosa = "telecolco"
            else:
                if not inquadratoQualcosa:
                    i = 0
                    for personaggio in listaPersonaggi:
                        if personaggio.x <= xMouse <= personaggio.x + GlobalVarG2.gpx and personaggio.y <= yMouse <= personaggio.y + GlobalVarG2.gpy:
                            if (personaggio.x == x + GlobalVarG2.gpx and personaggio.y == y) or (personaggio.x == x - GlobalVarG2.gpx and personaggio.y == y) or (personaggio.x == x and personaggio.y == y + GlobalVarG2.gpy) or (personaggio.x == x and personaggio.y == y - GlobalVarG2.gpy):
                                if GlobalVarG2.mouseBloccato:
                                    GlobalVarG2.configuraCursore(False)
                                inquadratoQualcosa = "personaggio:" + str(i)
                            break
                        i += 1
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(porte):
                        if porte[i + 1] <= xMouse <= porte[i + 1] + GlobalVarG2.gpx and porte[i + 2] <= yMouse <= porte[i + 2] + GlobalVarG2.gpy and not porte[i + 3]:
                            if ((porte[i + 1] == x + GlobalVarG2.gpx and porte[i + 2] == y) or (porte[i + 1] == x - GlobalVarG2.gpx and porte[i + 2] == y) or (porte[i + 1] == x and porte[i + 2] == y + GlobalVarG2.gpy) or (porte[i + 1] == x and porte[i + 2] == y - GlobalVarG2.gpy)) and not porte[i + 3]:
                                if GlobalVarG2.mouseBloccato:
                                    GlobalVarG2.configuraCursore(False)
                                inquadratoQualcosa = "porta:" + str(i)
                            break
                        i += 4
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(cofanetti):
                        if cofanetti[i + 1] <= xMouse <= cofanetti[i + 1] + GlobalVarG2.gpx and cofanetti[i + 2] <= yMouse <= cofanetti[i + 2] + GlobalVarG2.gpy and not cofanetti[i + 3]:
                            if ((cofanetti[i + 1] == x + GlobalVarG2.gpx and cofanetti[i + 2] == y) or (cofanetti[i + 1] == x - GlobalVarG2.gpx and cofanetti[i + 2] == y) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y + GlobalVarG2.gpy) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y - GlobalVarG2.gpy)) and not cofanetti[i + 3]:
                                if GlobalVarG2.mouseBloccato:
                                    GlobalVarG2.configuraCursore(False)
                                inquadratoQualcosa = "cofanetto:" + str(i)
                            break
                        i += 4
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(casevistePorteIncluse):
                        if casevistePorteIncluse[i] <= xMouse <= casevistePorteIncluse[i] + GlobalVarG2.gpx and casevistePorteIncluse[i + 1] <= yMouse <= casevistePorteIncluse[i + 1] + GlobalVarG2.gpy and casevistePorteIncluse[i + 2]:
                            if GlobalVarG2.mouseBloccato:
                                GlobalVarG2.configuraCursore(False)
                            inquadratoQualcosa = "movimento:" + str(casevistePorteIncluse[i]) + ":" + str(casevistePorteIncluse[i + 1])
                            break
                        i += 3
        if not inquadratoQualcosa and GlobalVarG2.mouseVisibile:
            GlobalVarG2.canaleSoundPassiRallo.stop()
            nx = 0
            ny = 0
            if not GlobalVarG2.mouseBloccato:
                GlobalVarG2.configuraCursore(True)

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
                if GlobalVarG2.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVarG2.mouseVisibile = False
                movimentoPerMouse = False
                tastop = event.key
                # movimenti personaggio
                if event.key == pygame.K_w and not tastoTrovato:
                    tastoTrovato = True
                    npers = 3
                    pers = GlobalVarG2.persw
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
                    ny = -GlobalVarG2.gpy
                    nx = 0
                if event.key == pygame.K_a and not tastoTrovato:
                    tastoTrovato = True
                    npers = 2
                    pers = GlobalVarG2.persa
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
                    nx = -GlobalVarG2.gpx
                    ny = 0
                if event.key == pygame.K_s and not tastoTrovato:
                    tastoTrovato = True
                    npers = 4
                    pers = GlobalVarG2.perss
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
                    ny = GlobalVarG2.gpy
                    nx = 0
                if event.key == pygame.K_d and not tastoTrovato:
                    tastoTrovato = True
                    npers = 1
                    pers = GlobalVarG2.persd
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
                    nx = GlobalVarG2.gpx
                    ny = 0

                if event.key == pygame.K_e and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostaPunBattaglia)
                    tastoTrovato = True
                    nx = 0
                    ny = 0
                    attacco = 1
                if event.key == pygame.K_q and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento and nemicoInquadrato:
                    tastoTrovato = True
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    nx = 0
                    ny = 0
                    nemicoInquadrato = False
                    caricaTutto = True
                if (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT) and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento:
                    GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.suonoTeleColco)
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
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selObbiettivo)
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
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selObbiettivo)
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
                        if porte[k] == dati[1] and ((porte[k + 1] == x + GlobalVarG2.gpx and porte[k + 2] == y and npers == 1) or (
                                porte[k + 1] == x - GlobalVarG2.gpx and porte[k + 2] == y and npers == 2) or (
                                                            porte[k + 1] == x and porte[
                                                        k + 2] == y + GlobalVarG2.gpy and npers == 4) or (
                                                            porte[k + 1] == x and porte[
                                                        k + 2] == y - GlobalVarG2.gpy and npers == 3)) and not porte[k + 3]:
                            sposta = True
                            GlobalVarG2.canaleSoundInterazioni.play(rumoreAperturaPorte)
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
                                (cofanetti[i + 1] == x + GlobalVarG2.gpx and cofanetti[i + 2] == y and npers == 1) or (
                                cofanetti[i + 1] == x - GlobalVarG2.gpx and cofanetti[i + 2] == y and npers == 2) or (
                                        cofanetti[i + 1] == x and cofanetti[i + 2] == y + GlobalVarG2.gpy and npers == 4) or (
                                        cofanetti[i + 1] == x and cofanetti[i + 2] == y - GlobalVarG2.gpy and npers == 3)) and not \
                        cofanetti[i + 3]:
                            GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.suonoaperturacofanetti)
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
                        if (personaggio.x == x + GlobalVarG2.gpx and personaggio.y == y and npers == 1) or (personaggio.x == x - GlobalVarG2.gpx and personaggio.y == y and npers == 2) or (personaggio.x == x and personaggio.y == y + GlobalVarG2.gpy and npers == 4) or (personaggio.x == x and personaggio.y == y - GlobalVarG2.gpy and npers == 3):
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            if npers == 1:
                                personaggio.girati("a")
                            elif npers == 2:
                                personaggio.girati("d")
                            elif npers == 3:
                                personaggio.girati("s")
                            elif npers == 4:
                                personaggio.girati("w")
                            disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, eschePrimaDelTurno, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu)
                            dati[0], oggettoRicevuto, visualizzaMenuMercante = dialoga(dati[0], personaggio)
                            caricaTutto = True
                if event.key == pygame.K_ESCAPE and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento:
                    tastoTrovato = True
                    nx = 0
                    ny = 0
                    startf = True

            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and centraleMouse and not impossibileCliccarePulsanti and not startf and mosseRimasteRob <= 0 and not nemiciInMovimento:
                movimentoPerMouse = False
                tastop = "mouseCentrale"
                tastoTrovato = True
                nx = 0
                ny = 0
                startf = True
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse and not impossibileCliccarePulsanti and not startf and mosseRimasteRob <= 0 and not nemiciInMovimento:
                movimentoPerMouse = False
                tastop = "mouseDestro"
                tastoTrovato = True
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostaPunBattaglia)
                nx = 0
                ny = 0
                attacco = 1
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato and not impossibileCliccarePulsanti and not startf and mosseRimasteRob <= 0 and not nemiciInMovimento:
                tastop = "mouseSinistro"
                tastoTrovato = True
                nx = 0
                ny = 0
                if inquadratoQualcosa == "start":
                    movimentoPerMouse = False
                    startf = True
                elif inquadratoQualcosa == "battaglia":
                    movimentoPerMouse = False
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostaPunBattaglia)
                    attacco = 1
                elif inquadratoQualcosa == "telecolco":
                    movimentoPerMouse = False
                    GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.suonoTeleColco)
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
                    GlobalVarG2.canaleSoundInterazioni.play(rumoreAperturaPorte)
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
                    if porte[posizPortaInVettore + 1] == x + GlobalVarG2.gpx and porte[posizPortaInVettore + 2] == y:
                        npers = 1
                    if porte[posizPortaInVettore + 1] == x - GlobalVarG2.gpx and porte[posizPortaInVettore + 2] == y:
                        npers = 2
                    if porte[posizPortaInVettore + 1] == x and porte[posizPortaInVettore + 2] == y + GlobalVarG2.gpy:
                        npers = 4
                    if porte[posizPortaInVettore + 1] == x and porte[posizPortaInVettore + 2] == y - GlobalVarG2.gpy:
                        npers = 3
                    if npers == 3:
                        pers = GlobalVarG2.persw
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
                        pers = GlobalVarG2.persa
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
                        pers = GlobalVarG2.perss
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
                        pers = GlobalVarG2.persd
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
                    GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.suonoaperturacofanetti)
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
                    if cofanetti[posizCofanettoInVettore + 1] == x + GlobalVarG2.gpx and cofanetti[posizCofanettoInVettore + 2] == y:
                        npers = 1
                    if cofanetti[posizCofanettoInVettore + 1] == x - GlobalVarG2.gpx and cofanetti[posizCofanettoInVettore + 2] == y:
                        npers = 2
                    if cofanetti[posizCofanettoInVettore + 1] == x and cofanetti[posizCofanettoInVettore + 2] == y + GlobalVarG2.gpy:
                        npers = 4
                    if cofanetti[posizCofanettoInVettore + 1] == x and cofanetti[posizCofanettoInVettore + 2] == y - GlobalVarG2.gpy:
                        npers = 3
                    if npers == 3:
                        pers = GlobalVarG2.persw
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
                        pers = GlobalVarG2.persa
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
                        pers = GlobalVarG2.perss
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
                        pers = GlobalVarG2.persd
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
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                    # giro il Rallo verso il personaggio e viceversa
                    if personaggio.x == x + GlobalVarG2.gpx and personaggio.y == y:
                        npers = 1
                    if personaggio.x == x - GlobalVarG2.gpx and personaggio.y == y:
                        npers = 2
                    if personaggio.x == x and personaggio.y == y + GlobalVarG2.gpy:
                        npers = 4
                    if personaggio.x == x and personaggio.y == y - GlobalVarG2.gpy:
                        npers = 3
                    if npers == 3:
                        pers = GlobalVarG2.persw
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
                        pers = GlobalVarG2.persa
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
                        pers = GlobalVarG2.perss
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
                        pers = GlobalVarG2.persd
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
                    disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, eschePrimaDelTurno, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu)
                    dati[0], oggettoRicevuto, visualizzaMenuMercante = dialoga(dati[0], personaggio)
                    caricaTutto = True
                elif inquadratoQualcosa.startswith("movimento"):
                    movimentoPerMouse = True
            elif GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and GlobalVarG2.mouseBloccato and mosseRimasteRob <= 0 and not nemiciInMovimento:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if (sinistroMouse or centraleMouse or destroMouse) and not GlobalVarG2.mouseVisibile:
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True

            if event.type == pygame.KEYUP:
                if tastop == event.key:
                    GlobalVarG2.canaleSoundPassiRallo.stop()
                    nx = 0
                    ny = 0
                    tastop = 0
            if event.type == pygame.MOUSEBUTTONUP:
                movimentoPerMouse = False
                GlobalVarG2.canaleSoundPassiRallo.stop()
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
                GlobalVarG2.canaleSoundPassiRallo.stop()
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
                if abs(xObbiettivo - x) == GlobalVarG2.gpx and abs(yObbiettivo - y) == 0:
                    if x < xObbiettivo:
                        npers = 1
                    if x > xObbiettivo:
                        npers = 2
                    sposta = True
                elif abs(yObbiettivo - y) == GlobalVarG2.gpy and abs(xObbiettivo - x) == 0:
                    if y < yObbiettivo:
                        npers = 4
                    if y > yObbiettivo:
                        npers = 3
                    sposta = True
                # cambiare posizione
                if npers == 3:
                    ny = -GlobalVarG2.gpy
                    nx = 0
                    pers = GlobalVarG2.persw
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
                    nx = -GlobalVarG2.gpx
                    pers = GlobalVarG2.persa
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
                    ny = GlobalVarG2.gpy
                    nx = 0
                    pers = GlobalVarG2.perss
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
                    nx = GlobalVarG2.gpx
                    pers = GlobalVarG2.persd
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
            GlobalVarG2.canaleSoundPassiRallo.stop()
            GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.selsta)
            dati[2] = x
            dati[3] = y
            dati[134] = rx
            dati[135] = ry
            if not apriocchio:
                dati, inizio, attacco, caricaSalvataggio = start(dati, porteini, portefin, cofaniini, cofanifin, tutteporte, tutticofanetti, listaNemiciTotali, vitaesca, vettoreDenaro, stanzeGiaVisitate, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggiTotali)
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
                        pers = GlobalVarG2.persw
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
                        pers = GlobalVarG2.persa
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
                        pers = GlobalVarG2.perss
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
                        pers = GlobalVarG2.persd
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
            disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, eschePrimaDelTurno, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu)
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
            GlobalVarG2.canaleSoundPassiRallo.stop()
            sposta, creaesca, xesca, yesca, npers, nrob, difesa, apriChiudiPorta, apriCofanetto, spingiColco, listaNemici, attacco, attaccoADistanza, nemicoInquadrato, attaccoDiRallo, chiamarob, ultimoObbiettivoColco, animaOggetto, interagisciConPersonaggio, startf = attacca(x, y, npers, nrob, rx, ry, pers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126], imgSfondoStanza, dati[1], sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, attVicino, attLontano, attacco, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, vettoreDenaro, dati[132], nemicoInquadrato, raffredda, autoRic1, autoRic2, ultimoObbiettivoColco, animaOggetto, listaPersonaggi, startf)
            tastop = 0
            # tolgo una freccia se uso l'attacco a distanza
            if attaccoADistanza:
                dati[132] -= 1
            caricaTutto = True
            # cambiare posizione dopo l'attacco
            if npers == 3:
                pers = GlobalVarG2.persw
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
                pers = GlobalVarG2.persa
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
                pers = GlobalVarG2.perss
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
                pers = GlobalVarG2.persd
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
                        GlobalVarG2.canaleSoundInterazioni.play(rumoreChiusuraPorte)
                        porte[k + 3] = False
                    else:
                        GlobalVarG2.canaleSoundInterazioni.play(rumoreAperturaPorte)
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
            if not type(nemicoInquadrato) is str and nemicoInquadrato and not nemicoInquadrato.inCasellaVista:
                nemicoInquadrato = False
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
                if (personaggio.x == x + GlobalVarG2.gpx and personaggio.y == y and npers == 1) or (personaggio.x == x - GlobalVarG2.gpx and personaggio.y == y and npers == 2) or (personaggio.x == x and personaggio.y == y + GlobalVarG2.gpy and npers == 4) or (personaggio.x == x and personaggio.y == y - GlobalVarG2.gpy and npers == 3):
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                    if npers == 1:
                        personaggio.girati("a")
                    elif npers == 2:
                        personaggio.girati("d")
                    elif npers == 3:
                        personaggio.girati("s")
                    elif npers == 4:
                        personaggio.girati("w")
                    # aggiorno lo GlobalVarG2.schermo (serve per girare i pers uno verso l'altro e per togliere il campo visivo dell'obiettivo selezionato)
                    disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, eschePrimaDelTurno, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu)
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
                    GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.suonoaperturacofanetti)
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
                if ((vitaesca[i + 1] / GlobalVarG2.gpx) + (vitaesca[i + 2] / GlobalVarG2.gpy)) % 2 == 0:
                    GlobalVarG2.schermo.blit(sfondinoa, (vitaesca[i + 1], vitaesca[i + 2]))
                if ((vitaesca[i + 1] / GlobalVarG2.gpx) + (vitaesca[i + 2] / GlobalVarG2.gpy)) % 2 == 1:
                    GlobalVarG2.schermo.blit(sfondinob, (vitaesca[i + 1], vitaesca[i + 2]))
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
                GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.suonoRaccoltaEsca)
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
        azioneRobEseguita = False
        if dati[122] > 0:
            # se surriscaldato toglie vel+ e efficienza
            dati[125] = 0
            dati[126] = 0
        if sposta and mosseRimasteRob == 0 and not morterob:
            if dati[125] > 0:
                mosseRimasteRob = 2
            else:
                mosseRimasteRob = 1
        # effetto di surriscalda / raffreddamento / auto-ricarica / auto-ricarica+
        if sposta:
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
                dati[10] += GlobalVarG2.dannoTecniche[6]
                if dati[10] > entot:
                    dati[10] = entot
                dati[122] = 10
            # autoric+
            if autoRic2 >= 0:
                ricarica2 = False
                autoRic2 -= 1
            if autoRic2 == 0:
                dati[10] += GlobalVarG2.dannoTecniche[16]
                if dati[10] > entot:
                    dati[10] = entot
                dati[122] = 10
        listaNemiciAttaccatiADistanzaRobo = False
        # attaccoDiColco [obbiettivo, danno, status (antidoto, attP, difP, velocizza, efficienza) ... => per ogni nemico colpito (non raffredda perchè deve rimanere per più turni)]
        attaccoDiColco = []
        tecnicaUsata = False
        if mosseRimasteRob > 0 and not morterob and not cambiosta:
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
                    robot = GlobalVarG2.robod
                    armrob = armrobd
                if nrob == 2:
                    robot = GlobalVarG2.roboa
                    armrob = armroba
                if nrob == 3:
                    robot = GlobalVarG2.robos
                    armrob = armrobs
                if nrob == 4:
                    robot = GlobalVarG2.robow
                    armrob = armrobw
        elif sposta and mosseRimasteRob < 0 and not morterob:
            mosseRimasteRob += 1
        if morterob:
            robot = GlobalVarG2.robomo
            armrob = GlobalVarG2.armrobmo

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
        if not carim and not inizio:
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
        if not inizio:
            if caricaTutto:
                if aumentoliv != 0:
                    pvtot = getVitaTotRallo(dati[4] - aumentoliv, dati[129])
                disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, eschePrimaDelTurno, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu)
                caricaTutto = False
            if azioneRobEseguita or nemiciInMovimento or sposta:
                primopasso, caricaTutto, tesoro, tastop, movimentoPerMouse = anima(sposta, x, y, vx, vy, rx, ry, vrx, vry, pers, robot, npers, nrob, primopasso, cambiosta, sfondinoa, sfondinob, scudo, armatura, arma, armaMov1, armaMov2, armaAttacco, scudoDifesa, arco, faretra, arcoAttacco, guanti, guantiMov1, guantiMov2, guantiAttacco, guantiDifesa, collana, armas, armaturas, arcos, faretras, collanas, armrob, armrobs, dati, attacco, difesa, tastop, tesoro, sfondinoc, aumentoliv, carim, caricaTutto, listaNemici, vitaesca, vettoreDenaro, attaccoADistanza, caseviste, porte, cofanetti, portaOriz, portaVert, stanza, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoInquadrato, attaccoDiRallo, attaccoDiColco, statoRalloInizioTurno, statoColcoInizioTurno, statoEscheInizioTurno, raffreddamento, ricarica1, ricarica2, raffredda, autoRic1, autoRic2, animaOggetto, eschePrimaDelTurno, listaPersonaggi, movimentoPerMouse)
            if not carim:
                pvtot = getVitaTotRallo(dati[4], dati[129])
                disegnaAmbiente(x, y, npers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, eschePrimaDelTurno, listaPersonaggi, False, stanzaCambiata, uscitoDaMenu)

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

'''pygame.draw.rect(GlobalVarG2.schermo, grigioscu, (GlobalVarG2.gsx // 32 * 0, GlobalVarG2.gsy // 18 * 0, GlobalVarG2.gpx * 16, GlobalVarG2.gpy * 3))
                    messaggio("Aumento Lv: Pv +", grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
                    messaggio("Aumento Lv: Attacco +", grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
                    messaggio("Aumento Lv: Difesa +", grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
                    pygame.display.update()
                    pygame.time.wait(500)
                    risposta = False
                    while not risposta:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    GlobalVarG2.selezione.play()
                                    risposta = True
                    caricaini = True
                    tesoro = -1'''

'''if esc:
    GlobalVarG2.schermo.fill(grigioscu)
    messaggio("Fine", grigiochi, GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 8, 150)
    pygame.display.update()
    pygame.time.wait(500)
    pygame.quit()
    quit()'''
'''# linea(dove,colore,inizio,fine,spessore)
pygame.draw.line(GlobalVarG2.schermo, verde, (0, 0), (GlobalVarG2.gsx, GlobalVarG2.gsy), 10)
# cerchio(dove,colore,centro,raggio,spessore)
pygame.draw.circle(GlobalVarG2.schermo, blu, (300, 100), 5)
# rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
pygame.draw.rect(GlobalVarG2.schermo, rosso, (200, 100, 30, 40), 5)'''
'''# canzone
c1 = pygame.mixer.Sound("Audio/Canzone11.wav")
c1.play(-1))'''
