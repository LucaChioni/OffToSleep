# -*- coding: utf-8 -*-

from MenuG2 import *
from EnvPrintG2 import *
from MovNemiciRobG2 import *
from AnimazioniG2 import *
from NemicoObj import *


# freccetta invisibile
pygame.mouse.set_visible(False)


def gameloop():
    inizio = True
    while True:
        if inizio:
            nemicoInquadrato = False
            raffredda = -1
            autoRic1 = -1
            autoRic2 = -1
            spingiColco = False
            apriChiudiPorta = [False, 0, 0]
            apriCofanetto = [False, 0, 0]
            stanzaVecchia = 0
            chiamarob = True
            tesoro = -1
            apriocchio = False
            sposta = False
            nmost = 0
            agg = 0
            tastop = 0
            startf = False
            aumentoliv = False
            primopasso = True
            contaesca = 0
            xesca = 0
            yesca = 0
            creaesca = False
            vitaesca = []
            vettoreDenaro = []
            attacco = 0
            # difesa e' grigio perche' viene impostato a ogni ciclo
            difesa = 0
            # 1->d , 2->a , 3->w , 4->s
            npers = 4
            # 1->d , 2->a , 3->s , 4->w
            nrob = 3
            nx = 0
            ny = 0
            pers = perss
            robot = robos
            dati, porteini, portefin, cofaniini, cofanifin = menu()
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
            rx = x
            ry = y
            vrx = vx
            vry = vy

            stanzeGiaVisitate = []
            listaNemici = []
            listaNemiciTotali = []

            carim = True
            cambiosta = True
            impossibileCliccarePulsanti = True

        # caricare gli oggetti
        if carim:
            if pers == persw:
                agg = 1
            if pers == persa:
                agg = 2
            if pers == perss:
                agg = 3
            if pers == persd:
                agg = 4
            # stanza
            imgSfondoStanza = pygame.image.load("Immagini/Paesaggi/Stanza%ia.png" % dati[1]).convert()
            imgSfondoStanza = pygame.transform.scale(imgSfondoStanza, (gsx, gsy))
            sfondinoa = pygame.image.load("Immagini/Paesaggi/Sfondino%ia.png" % dati[1]).convert()
            sfondinoa = pygame.transform.scale(sfondinoa, (gpx, gpy))
            sfondinob = pygame.image.load("Immagini/Paesaggi/Sfondino%ib.png" % dati[1]).convert()
            sfondinob = pygame.transform.scale(sfondinob, (gpx, gpy))
            sfondinoc = pygame.image.load("Immagini/Paesaggi/Sfondino%ic.png" % dati[1]).convert()
            sfondinoc = pygame.transform.scale(sfondinoc, (gpx, gpy))
            portaVert = pygame.image.load("Immagini/Paesaggi/PortaV%i.png" % dati[1])
            portaVert = pygame.transform.scale(portaVert, (gpx, gpy))
            portaOriz = pygame.image.load("Immagini/Paesaggi/PortaO%i.png" % dati[1])
            portaOriz = pygame.transform.scale(portaOriz, (gpx, gpy))

            # mostri
            if dati[1] == 1 and cambiosta:
                # posizione personaggio e robot al cambio stanza
                if not inizio:
                    if stanzaVecchia == 2:
                        npers = 4
                        nrob = 3
                        x = gsx // 32 * 6
                        y = gsy // 18 * 2
                        pers = perss
                        robot = robos
                        agg = 3
                    vx = x
                    vy = y
                    rx = x
                    ry = y
                    vrx = x
                    vry = y

                listaNemici = []
                if not dati[1] in stanzeGiaVisitate:
                    stanzeGiaVisitate.append(dati[1])
                    nemico = NemicoObj(gsx // 32 * 29, gsy // 18 * 15, "w", "Orco", dati[1])
                    listaNemiciTotali.append(nemico)
                    listaNemici.append(nemico)
                    nemico = NemicoObj(gsx // 32 * 3, gsy // 18 * 3, "a", "Orco", dati[1])
                    listaNemiciTotali.append(nemico)
                    listaNemici.append(nemico)
                    nemico = NemicoObj(gsx // 32 * 8, gsy // 18 * 7, "s", "Pipistrello", dati[1])
                    listaNemiciTotali.append(nemico)
                    listaNemici.append(nemico)
                    nemico = NemicoObj(gsx // 32 * 15, gsy // 18 * 14, "d", "Orco", dati[1])
                    listaNemiciTotali.append(nemico)
                    listaNemici.append(nemico)
                    nemico = NemicoObj(gsx // 32 * 23, gsy // 18 * 4, "s", "Pipistrello", dati[1])
                    listaNemiciTotali.append(nemico)
                    listaNemici.append(nemico)
                else:
                    for nemico in listaNemiciTotali:
                        if nemico.stanzaDiAppartenenza == dati[1]:
                            listaNemici.append(nemico)
                nmost = len(listaNemici)

            if dati[1] == 2 and cambiosta:
                # posizione personaggio e robot al cambio stanza
                if not inizio:
                    if stanzaVecchia == 1:
                        npers = 4
                        nrob = 3
                        x = gsx // 32 * 6
                        y = gsy // 18 * 2
                        pers = perss
                        robot = robos
                        agg = 3
                    vx = x
                    vy = y
                    rx = x
                    ry = y
                    vrx = x
                    vry = y

                listaNemici = []
                if not dati[1] in stanzeGiaVisitate:
                    stanzeGiaVisitate.append(dati[1])
                    nemico = NemicoObj(gsx // 32 * 29, gsy // 18 * 15, "w", "Orco", dati[1])
                    listaNemiciTotali.append(nemico)
                    listaNemici.append(nemico)
                else:
                    for nemico in listaNemiciTotali:
                        if nemico.stanzaDiAppartenenza == dati[1]:
                            listaNemici.append(nemico)
                nmost = len(listaNemici)

            if cambiosta:
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
                numstanza = dati[1]
                caseviste = []
                n = 1
                while n <= 28:
                    m = 1
                    while m <= 14:
                        caseviste.append(gpx + (gpx * n))
                        caseviste.append(gpy + (gpy * m))
                        caseviste.append(False)
                        m = m + 1
                    n = n + 1
                # scoprire caselle viste
                caseviste = scopriCaselleViste(x, y, rx, ry, numstanza, porte, cofanetti, caseviste)

                # eliminare tutte le esche
                vitaesca = []
                # elimino tutti i sacchetti di denaro
                vettoreDenaro = []

                # cambiosta viene cambiato sopra !!!!!!!!!!!!
                cambiosta = False
                impossibileCliccarePulsanti = True

            # arma
            armaw = pygame.image.load("Immagini/EquipRallo/Spade/Spada%iw.png" % dati[6])
            armaw = pygame.transform.scale(armaw, (gpx, gpy))
            armawMov1 = pygame.image.load("Immagini/EquipRallo/Spade/Spada%iwMov1.png" % dati[6])
            armawMov1 = pygame.transform.scale(armawMov1, (gpx, gpy))
            armawMov2 = pygame.image.load("Immagini/EquipRallo/Spade/Spada%iwMov2.png" % dati[6])
            armawMov2 = pygame.transform.scale(armawMov2, (gpx, gpy))
            armaa = pygame.image.load("Immagini/EquipRallo/Spade/Spada%ia.png" % dati[6])
            armaa = pygame.transform.scale(armaa, (gpx, gpy))
            armaaMov1 = pygame.image.load("Immagini/EquipRallo/Spade/Spada%iaMov1.png" % dati[6])
            armaaMov1 = pygame.transform.scale(armaaMov1, (gpx, gpy))
            armaaMov2 = pygame.image.load("Immagini/EquipRallo/Spade/Spada%iaMov2.png" % dati[6])
            armaaMov2 = pygame.transform.scale(armaaMov2, (gpx, gpy))
            armas = pygame.image.load("Immagini/EquipRallo/Spade/Spada%is.png" % dati[6])
            armas = pygame.transform.scale(armas, (gpx, gpy))
            armasMov1 = pygame.image.load("Immagini/EquipRallo/Spade/Spada%isMov1.png" % dati[6])
            armasMov1 = pygame.transform.scale(armasMov1, (gpx, gpy))
            armasMov2 = pygame.image.load("Immagini/EquipRallo/Spade/Spada%isMov2.png" % dati[6])
            armasMov2 = pygame.transform.scale(armasMov2, (gpx, gpy))
            armad = pygame.image.load("Immagini/EquipRallo/Spade/Spada%id.png" % dati[6])
            armad = pygame.transform.scale(armad, (gpx, gpy))
            armadMov1 = pygame.image.load("Immagini/EquipRallo/Spade/Spada%idMov1.png" % dati[6])
            armadMov1 = pygame.transform.scale(armadMov1, (gpx, gpy))
            armadMov2 = pygame.image.load("Immagini/EquipRallo/Spade/Spada%idMov2.png" % dati[6])
            armadMov2 = pygame.transform.scale(armadMov2, (gpx, gpy))
            armasAttacco = pygame.image.load("Immagini/EquipRallo/Spade/Spada%isAttacco.png" % dati[6])
            armasAttacco = pygame.transform.scale(armasAttacco, (gpx, gpy * 2))
            armaaAttacco = pygame.image.load("Immagini/EquipRallo/Spade/Spada%iaAttacco.png" % dati[6])
            armaaAttacco = pygame.transform.scale(armaaAttacco, (gpx * 2, gpy))
            armadAttacco = pygame.image.load("Immagini/EquipRallo/Spade/Spada%idAttacco.png" % dati[6])
            armadAttacco = pygame.transform.scale(armadAttacco, (gpx * 2, gpy))
            armawAttacco = pygame.image.load("Immagini/EquipRallo/Spade/Spada%iwAttacco.png" % dati[6])
            armawAttacco = pygame.transform.scale(armawAttacco, (gpx, gpy * 2))
            # arco
            arcow = pygame.image.load("Immagini/EquipRallo/Archi/Arco%iw.png" % dati[128])
            arcow = pygame.transform.scale(arcow, (gpx, gpy))
            arcoa = pygame.image.load("Immagini/EquipRallo/Archi/Arco%ia.png" % dati[128])
            arcoa = pygame.transform.scale(arcoa, (gpx, gpy))
            arcos = pygame.image.load("Immagini/EquipRallo/Archi/Arco%is.png" % dati[128])
            arcos = pygame.transform.scale(arcos, (gpx, gpy))
            arcod = pygame.image.load("Immagini/EquipRallo/Archi/Arco%id.png" % dati[128])
            arcod = pygame.transform.scale(arcod, (gpx, gpy))
            arcosAttacco = pygame.image.load("Immagini/EquipRallo/Archi/Arco%isAttacco.png" % dati[128])
            arcosAttacco = pygame.transform.scale(arcosAttacco, (gpx, gpy * 2))
            arcoaAttacco = pygame.image.load("Immagini/EquipRallo/Archi/Arco%iaAttacco.png" % dati[128])
            arcoaAttacco = pygame.transform.scale(arcoaAttacco, (gpx * 2, gpy))
            arcodAttacco = pygame.image.load("Immagini/EquipRallo/Archi/Arco%idAttacco.png" % dati[128])
            arcodAttacco = pygame.transform.scale(arcodAttacco, (gpx * 2, gpy))
            arcowAttacco = pygame.image.load("Immagini/EquipRallo/Archi/Arco%iwAttacco.png" % dati[128])
            arcowAttacco = pygame.transform.scale(arcowAttacco, (gpx, gpy * 2))
            # faretra
            faretraw = pygame.image.load("Immagini/EquipRallo/Faretre/Faretra%iw.png" % dati[133])
            faretraw = pygame.transform.scale(faretraw, (gpx, gpy))
            faretraa = pygame.image.load("Immagini/EquipRallo/Faretre/Faretra%ia.png" % dati[133])
            faretraa = pygame.transform.scale(faretraa, (gpx, gpy))
            faretras = pygame.image.load("Immagini/EquipRallo/Faretre/Faretra%is.png" % dati[133])
            faretras = pygame.transform.scale(faretras, (gpx, gpy))
            faretrad = pygame.image.load("Immagini/EquipRallo/Faretre/Faretra%id.png" % dati[133])
            faretrad = pygame.transform.scale(faretrad, (gpx, gpy))
            # armatura
            armaturaw = pygame.image.load("Immagini/EquipRallo/Armature/Armatura%iw.png" % dati[8])
            armaturaw = pygame.transform.scale(armaturaw, (gpx, gpy))
            armaturaa = pygame.image.load("Immagini/EquipRallo/Armature/Armatura%ia.png" % dati[8])
            armaturaa = pygame.transform.scale(armaturaa, (gpx, gpy))
            armaturas = pygame.image.load("Immagini/EquipRallo/Armature/Armatura%is.png" % dati[8])
            armaturas = pygame.transform.scale(armaturas, (gpx, gpy))
            armaturad = pygame.image.load("Immagini/EquipRallo/Armature/Armatura%id.png" % dati[8])
            armaturad = pygame.transform.scale(armaturad, (gpx, gpy))
            # scudo
            scudow = pygame.image.load("Immagini/EquipRallo/Scudi/Scudo%iw.png" % dati[7])
            scudow = pygame.transform.scale(scudow, (gpx, gpy))
            scudoa = pygame.image.load("Immagini/EquipRallo/Scudi/Scudo%ia.png" % dati[7])
            scudoa = pygame.transform.scale(scudoa, (gpx, gpy))
            scudos = pygame.image.load("Immagini/EquipRallo/Scudi/Scudo%is.png" % dati[7])
            scudos = pygame.transform.scale(scudos, (gpx, gpy))
            scudod = pygame.image.load("Immagini/EquipRallo/Scudi/Scudo%id.png" % dati[7])
            scudod = pygame.transform.scale(scudod, (gpx, gpy))
            scudoDifesa = pygame.image.load("Immagini/EquipRallo/Scudi/Scudo%iDifesa.png" % dati[7])
            scudoDifesa = pygame.transform.scale(scudoDifesa, (gpx, gpy))
            # guanti
            guantiw = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%iw.png" % dati[129])
            guantiw = pygame.transform.scale(guantiw, (gpx, gpy))
            guantiwMov1 = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%iwMov1.png" % dati[129])
            guantiwMov1 = pygame.transform.scale(guantiwMov1, (gpx, gpy))
            guantiwMov2 = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%iwMov2.png" % dati[129])
            guantiwMov2 = pygame.transform.scale(guantiwMov2, (gpx, gpy))
            guantia = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%ia.png" % dati[129])
            guantia = pygame.transform.scale(guantia, (gpx, gpy))
            guantiaMov1 = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%iaMov1.png" % dati[129])
            guantiaMov1 = pygame.transform.scale(guantiaMov1, (gpx, gpy))
            guantiaMov2 = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%iaMov2.png" % dati[129])
            guantiaMov2 = pygame.transform.scale(guantiaMov2, (gpx, gpy))
            guantis = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%is.png" % dati[129])
            guantis = pygame.transform.scale(guantis, (gpx, gpy))
            guantisMov1 = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%isMov1.png" % dati[129])
            guantisMov1 = pygame.transform.scale(guantisMov1, (gpx, gpy))
            guantisMov2 = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%isMov2.png" % dati[129])
            guantisMov2 = pygame.transform.scale(guantisMov2, (gpx, gpy))
            guantid = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%id.png" % dati[129])
            guantid = pygame.transform.scale(guantid, (gpx, gpy))
            guantidMov1 = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%idMov1.png" % dati[129])
            guantidMov1 = pygame.transform.scale(guantidMov1, (gpx, gpy))
            guantidMov2 = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%idMov2.png" % dati[129])
            guantidMov2 = pygame.transform.scale(guantidMov2, (gpx, gpy))
            guantisAttacco = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%isAttacco.png" % dati[129])
            guantisAttacco = pygame.transform.scale(guantisAttacco, (gpx, gpy))
            guantiaAttacco = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%iaAttacco.png" % dati[129])
            guantiaAttacco = pygame.transform.scale(guantiaAttacco, (gpx, gpy))
            guantidAttacco = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%idAttacco.png" % dati[129])
            guantidAttacco = pygame.transform.scale(guantidAttacco, (gpx, gpy))
            guantiwAttacco = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%iwAttacco.png" % dati[129])
            guantiwAttacco = pygame.transform.scale(guantiwAttacco, (gpx, gpy))
            guantiDifesa = pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%iDifesa.png" % dati[129])
            guantiDifesa = pygame.transform.scale(guantiDifesa, (gpx, gpy))
            # collana
            collanaw = pygame.image.load("Immagini/EquipRallo/Collane/Collana%iw.png" % dati[130])
            collanaw = pygame.transform.scale(collanaw, (gpx, gpy))
            collanaa = pygame.image.load("Immagini/EquipRallo/Collane/Collana%ia.png" % dati[130])
            collanaa = pygame.transform.scale(collanaa, (gpx, gpy))
            collanas = pygame.image.load("Immagini/EquipRallo/Collane/Collana%is.png" % dati[130])
            collanas = pygame.transform.scale(collanas, (gpx, gpy))
            collanad = pygame.image.load("Immagini/EquipRallo/Collane/Collana%id.png" % dati[130])
            collanad = pygame.transform.scale(collanad, (gpx, gpy))
            # armatura robot
            armrobw = pygame.image.load("Immagini/EquipRobo/Batteria%iw.png" % dati[9])
            armrobw = pygame.transform.scale(armrobw, (gpx, gpy))
            armroba = pygame.image.load("Immagini/EquipRobo/Batteria%ia.png" % dati[9])
            armroba = pygame.transform.scale(armroba, (gpx, gpy))
            armrobs = pygame.image.load("Immagini/EquipRobo/Batteria%is.png" % dati[9])
            armrobs = pygame.transform.scale(armrobs, (gpx, gpy))
            armrobd = pygame.image.load("Immagini/EquipRobo/Batteria%id.png" % dati[9])
            armrobd = pygame.transform.scale(armrobd, (gpx, gpy))
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
                    robot = robod
                    armrob = armrobd
                if nrob == 2:
                    robot = roboa
                    armrob = armroba
                if nrob == 3:
                    robot = robos
                    armrob = armrobs
                if nrob == 4:
                    robot = robow
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
            robot = robos
            armrob = armrobs
            inizio = False
        if tastop == 0:
            nx = 0
            ny = 0

        tastoTrovato = False
        # catturare gli eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN and not impossibileCliccarePulsanti and not tastoTrovato:
                # movimanti
                tastop = event.key
                # movimenti personaggio
                if event.key == pygame.K_w and not tastoTrovato:
                    tastoTrovato = True
                    npers = 3
                    pers = persw
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
                    ny = -gpy
                    nx = 0
                if event.key == pygame.K_a and not tastoTrovato:
                    tastoTrovato = True
                    npers = 2
                    pers = persa
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
                    nx = -gpx
                    ny = 0
                if event.key == pygame.K_s and not tastoTrovato:
                    tastoTrovato = True
                    npers = 4
                    pers = perss
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
                    ny = gpy
                    nx = 0
                if event.key == pygame.K_d and not tastoTrovato:
                    tastoTrovato = True
                    npers = 1
                    pers = persd
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
                    nx = gpx
                    ny = 0

                nemiciInMovimento = False
                for nemico in listaNemici:
                    if nemico.mosseRimaste > 0:
                        nemiciInMovimento = True
                        break

                if event.key == pygame.K_e and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento:
                    tastoTrovato = True
                    nx = 0
                    ny = 0
                    attacco = 1
                if event.key == pygame.K_x and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento:
                    tastoTrovato = True
                    nx = 0
                    ny = 0
                    if chiamarob:
                        chiamarob = False
                    else:
                        chiamarob = True
                if event.key == pygame.K_q and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento and nemicoInquadrato:
                    canaleSoundPuntatore.play(selind)
                    nemicoInquadrato = False
                    caricaTutto = True

                if event.key == pygame.K_SPACE and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento:
                    tastoTrovato = True
                    # apertura porte
                    k = 0
                    while k < len(porte):
                        if porte[k] == dati[1] and ((porte[k + 1] == x + gpx and porte[k + 2] == y and npers == 1) or (
                                porte[k + 1] == x - gpx and porte[k + 2] == y and npers == 2) or (
                                                            porte[k + 1] == x and porte[
                                                        k + 2] == y + gpy and npers == 4) or (
                                                            porte[k + 1] == x and porte[
                                                        k + 2] == y - gpy and npers == 3)) and not porte[k + 3]:
                            sposta = True
                            canaleSoundInterazioni.play(suonoaperturaporte)
                            porte[k + 3] = True
                            # scoprire caselle viste
                            caseviste = scopriCaselleViste(x, y, rx, ry, numstanza, porte, cofanetti, caseviste)
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
                                (cofanetti[i + 1] == x + gpx and cofanetti[i + 2] == y and npers == 1) or (
                                cofanetti[i + 1] == x - gpx and cofanetti[i + 2] == y and npers == 2) or (
                                        cofanetti[i + 1] == x and cofanetti[i + 2] == y + gpy and npers == 4) or (
                                        cofanetti[i + 1] == x and cofanetti[i + 2] == y - gpy and npers == 3)) and not \
                        cofanetti[i + 3]:
                            canaleSoundInterazioni.play(suonoaperturacofanetti)
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

                if event.key == pygame.K_ESCAPE and not tastoTrovato and mosseRimasteRob <= 0 and not nemiciInMovimento:
                    tastoTrovato = True
                    startf = True

            if event.type == pygame.KEYUP:
                if tastop == event.key:
                    canaleSoundPassiRallo.stop()
                    nx = 0
                    ny = 0
                    tastop = 0

        impossibileCliccarePulsanti = False

        # statistiche personaggio e robo
        esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati, difesa)

        # ripristina vita e status dopo lv up
        if aumentoliv:
            dati[5] = pvtot
            dati[121] = False
            aumentoliv = False

        # menu start
        if startf and attacco != 1:
            canaleSoundInterazioni.play(selsta)
            dati[2] = x
            dati[3] = y
            if not apriocchio:
                dati, inizio, attacco = start(dati, nmost, porteini, portefin, cofaniini, cofanifin, tutteporte, tutticofanetti, apriocchio)
            else:
                dati, attacco, sposta = startBattaglia(dati)
                caricaTutto = True
            carim = True
            startf = False

        # morte tua e di robo
        inizio = controllaMorteRallo(dati[5], inizio)
        morterob, dati, mosseRimasteRob = controllaMorteColco(dati, mosseRimasteRob)

        # controllo se ci sono nemici in movimento per decidere se fare animazioni o no
        nemiciInMovimento = False
        for nemico in listaNemici:
            if nemico.mosseRimaste > 0:
                nemiciInMovimento = True
                break

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
            if (x == rx and y == ry) or sovrapposto:
                x = vx
                y = vy
        # gestione attacchi
        attaccoADistanza = False
        if attacco != 0:
            sposta, creaesca, xesca, yesca, npers, nrob, difesa, apriChiudiPorta, apriCofanetto, spingiColco, listaNemici, attacco, attaccoADistanza, nemicoInquadrato = attacca(x, y, npers, nrob, rx, ry, pers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126], imgSfondoStanza, dati[1], sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, attVicino, attLontano, attacco, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, vettoreDenaro, dati[132], nemicoInquadrato)
            # tolgo una freccia se uso l'attacco a distanza
            if attaccoADistanza:
                dati[132] -= 1
            caricaTutto = True
            # cambiare posizione dopo l'attacco
            if npers == 3:
                pers = persw
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
                pers = persa
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
                pers = perss
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
                pers = persd
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
        if dati[123] > 0:
            attVicino = attVicino + attVicino // 4
            if sposta:
                dati[123] = dati[123] - 1
        if dati[124] > 0:
            dif = dif + dif // 4
            if sposta:
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
                    canaleSoundInterazioni.play(suonoaperturaporte)
                    if porte[k + 3]:
                        porte[k + 3] = False
                    else:
                        porte[k + 3] = True
                    # scoprire caselle viste
                    caseviste = scopriCaselleViste(x, y, rx, ry, numstanza, porte, cofanetti, caseviste)
                    # aggiornare vettore tutteporte
                    j = 0
                    while j < len(tutteporte):
                        if tutteporte[j] == porte[k] and tutteporte[j + 1] == porte[k + 1] and tutteporte[j + 2] == porte[k + 2]:
                            tutteporte[j + 3] = porte[k + 3]
                        j = j + 4
                k = k + 4
            apriChiudiPorta = [False, 0, 0]
            # controllo se devo deselezionare il nemico / esca / colco inquadrato
            vettoreVuoto = []
            # vita colco selezionato
            if nemicoInquadrato == "Colco":
                raggiungibile = pathFinding(x, y, rx, ry, numstanza, porte, cofanetti, vettoreVuoto)
                if not raggiungibile:
                    nemicoInquadrato = False
            # vita nemico selezionato
            elif not type(nemicoInquadrato) is str and nemicoInquadrato:
                raggiungibile = pathFinding(x, y, nemicoInquadrato.x, nemicoInquadrato.y, numstanza, porte, cofanetti, vettoreVuoto)
                if not raggiungibile:
                    nemicoInquadrato = False
            # vita esche selezionate
            elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
                idEscaInquadrata = int(nemicoInquadrato[4:])
                i = 0
                while i < len(vitaesca):
                    if idEscaInquadrata == vitaesca[i]:
                        raggiungibile = pathFinding(x, y, vitaesca[i + 2], vitaesca[i + 3], numstanza, porte, cofanetti, vettoreVuoto)
                        if not raggiungibile:
                            nemicoInquadrato = False
                        break
                    i += 4
        # apertura cofanetti
        if apriCofanetto[0]:
            i = 0
            while i < len(cofanetti):
                if cofanetti[i] == dati[1] and cofanetti[i + 1] == apriCofanetto[1] and cofanetti[i + 2] == apriCofanetto[2] and not cofanetti[i + 3]:
                    canaleSoundInterazioni.play(suonoaperturacofanetti)
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

        # lancio esche
        if creaesca:
            contaesca = contaesca + 1
            # id, vita, xesca, yesca
            vitaesca.append(contaesca)
            vitaesca.append(100)
            vitaesca.append(xesca)
            vitaesca.append(yesca)
            creaesca = False
        # morte esca
        i = 1
        while i < len(vitaesca):
            cancellata = False
            if vitaesca[i] <= 0:
                if ((vitaesca[i + 1] / gpx) + (vitaesca[i + 2] / gpy)) % 2 == 0:
                    schermo.blit(sfondinoa, (vitaesca[i + 1], vitaesca[i + 2]))
                if ((vitaesca[i + 1] / gpx) + (vitaesca[i + 2] / gpy)) % 2 == 1:
                    schermo.blit(sfondinob, (vitaesca[i + 1], vitaesca[i + 2]))
                # tolgo la selezione dell'esca morta
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
                del vitaesca[i + 2]
                del vitaesca[i + 1]
                del vitaesca[i]
                del vitaesca[i - 1]
                dati[38] += 1
            i = i + 4

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
        if mosseRimasteRob > 0 and not morterob and not cambiosta:
            vrx = rx
            vry = ry

            # surriscalda
            if dati[122] > 0:
                dati[122] = dati[122] - 1
                dati[10] = dati[10] - 3

            # efficienza
            if dati[126] > 0:
                if dati[125] > 0:
                    if mosseRimasteRob == 1:
                        dati[126] -= 1
                else:
                    dati[126] -= 1

            # vel+
            if dati[125] > 0:
                if mosseRimasteRob == 1:
                    dati[125] -= 1
                if dati[125] == 0:
                    dati[122] = 10

            # movimento - gambit
            vetDatiNemici = []
            for nemico in listaNemici:
                vetDatiNemici.append(nemico.vita)
                vetDatiNemici.append(nemico.x)
                vetDatiNemici.append(nemico.y)
                vetDatiNemici.append(nemico.vitaTotale)
                if not nemico.avvelenato and not nemico.appiccicato:
                    vetDatiNemici.append(0)
                elif nemico.avvelenato and not nemico.appiccicato:
                    vetDatiNemici.append(1)
                elif not nemico.avvelenato and nemico.appiccicato:
                    vetDatiNemici.append(2)
                elif nemico.avvelenato and nemico.appiccicato:
                    vetDatiNemici.append(3)
            rx, ry, nrob, dati, vetDatiNemici, raffreddamento, ricarica1, ricarica2, azioneRobEseguita = movrobo(x, y, vx, vy, rx, ry, dati[1], chiamarob, dati, porte, cofanetti, vetDatiNemici, nmost, difesa)
            i = 0
            for nemico in listaNemici:
                if nemico.vita != vetDatiNemici[i]:
                    nemico.danneggia(nemico.vita - vetDatiNemici[i], "Colco")
                statom = vetDatiNemici[i + 4]
                if statom == 0:
                    nemico.avvelenato = False
                    nemico.appiccicato = False
                elif statom == 1:
                    nemico.avvelenato = True
                    nemico.appiccicato = False
                elif statom == 2:
                    nemico.avvelenato = False
                    nemico.appiccicato = True
                elif statom == 3:
                    nemico.avvelenato = True
                    nemico.appiccicato = True
                i += 5

            if dati[122] > 0:
                mosseRimasteRob -= 2
            else:
                mosseRimasteRob -= 1

            if raffreddamento:
                mosseRimasteRob = -1
                raffredda = 1
            if ricarica1:
                mosseRimasteRob = -1
                autoRic1 = 1
            if ricarica2:
                mosseRimasteRob = -1
                autoRic2 = 1

            sovrapposto = False
            for nemico in listaNemici:
                if nemico.x == rx and nemico.y == ry:
                    sovrapposto = True
                    break
            if (rx == x and ry == y) or sovrapposto:
                rx = vrx
                ry = vry
                nrob = 0
                azioneRobEseguita = False
            if nrob != 0:
                if nrob == 1:
                    robot = robod
                    armrob = armrobd
                if nrob == 2:
                    robot = roboa
                    armrob = armroba
                if nrob == 3:
                    robot = robos
                    armrob = armrobs
                if nrob == 4:
                    robot = robow
                    armrob = armrobw
        elif sposta and mosseRimasteRob < 0 and not morterob:
            mosseRimasteRob += 1
        # effetto di raffreddamento / auto-ricarica / auto-ricarica+
        if mosseRimasteRob >= 0:
            if raffredda == 0:
                dati[122] = 0
            if raffredda >= 0:
                raffredda -= 1

            if autoRic1 == 0:
                dati[10] += dannoTecniche[6]
                if dati[10] > entot:
                    dati[10] = entot
                dati[122] = 10
            if autoRic1 >= 0:
                autoRic1 -= 1

            if autoRic2 == 0:
                dati[10] += dannoTecniche[16]
                if dati[10] > entot:
                    dati[10] = entot
                dati[122] = 10
            if autoRic2 >= 0:
                autoRic2 -= 1
        if morterob:
            robot = robomo
            armrob = armrobmo

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
                    if sposta and nemico.mosseRimaste == 0:
                        nemico.resettaMosseRimaste()
                    if nemico.mosseRimaste > 0:
                        nemico.vx = nemico.x
                        nemico.vy = nemico.y
                        nemico, direzioneMostro, dati, vitaesca = movmostro(x, y, rx, ry, nemico, dati[1], dif, difro, par, dati, vitaesca, porte, cofanetti, vetDatiNemici, vettoreDenaro)
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
                                break
                            i += 4
                        if (nemico.x == x and nemico.y == y) or (nemico.x == rx and nemico.y == ry):
                            nemico.x = nemico.vx
                            nemico.y = nemico.vy
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

        # aumentare di livello
        if dati[127] >= esptot and dati[4] < 100 and not carim and not inizio:
            dati[4] = dati[4] + 1
            dati[127] = dati[127] - esptot
            aumentoliv = True
            impossibileCliccarePulsanti = True

        # aggiorna vista dei mostri e metti l'occhio se ti vedono
        apriocchio = False
        for nemico in listaNemici:
            if (abs(x - nemico.x) <= nemico.raggioVisivo and abs(y - nemico.y) <= nemico.raggioVisivo) or (abs(rx - nemico.x) <= nemico.raggioVisivo and abs(ry - nemico.y) <= nemico.raggioVisivo):
                incasevista = False
                i = 0
                while i < len(caseviste):
                    if caseviste[i + 2] and caseviste[i] == nemico.x and caseviste[i + 1] == nemico.y:
                        incasevista = True
                        break
                    i += 3
                if nemico.vita > 0 and incasevista:
                    nemico.aggiornaVista(x, y, rx, ry, dati[1], porte, cofanetti, dati)
                    if nemico.visto:
                        apriocchio = True
                        break

        # fai tutte le animazioni del turno e disegnare gli sfondi e personaggi
        if not inizio:
            if caricaTutto:
                disegnaAmbiente(x, y, npers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato)
                caricaTutto = False
            if azioneRobEseguita or nemiciInMovimento or sposta:
                primopasso, caricaTutto, tesoro, tastop = anima(sposta, x, y, vx, vy, rx, ry, vrx, vry, pers, robot, npers, nrob, primopasso, cambiosta, sfondinoa, sfondinob, scudo, armatura, arma, armaMov1, armaMov2, armaAttacco, scudoDifesa, arco, faretra, arcoAttacco, guanti, guantiMov1, guantiMov2, guantiAttacco, guantiDifesa, collana, armas, armaturas, arcos, faretras, guantis, collanas, armrob, dati, attacco, difesa, tastop, tesoro, sfondinoc, aumentoliv, carim, caricaTutto, listaNemici, vitaesca, vettoreDenaro, attaccoADistanza, caseviste, porte, cofanetti, portaOriz, portaVert, stanza)
            elif not sposta:
                canaleSoundPassiRallo.stop()
            if not carim:
                disegnaAmbiente(x, y, npers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza, listaNemici, caricaTutto, vettoreDenaro, dati[132], nemicoInquadrato)

        if not aumentoliv:
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
            if not type(nemicoInquadrato) is str and nemicoInquadrato and nemicoInquadrato.morto:
                nemicoInquadrato = False
            if nemico.morto:
                caricaTutto = True
                listaNemici.remove(nemico)
                listaNemiciTotali.remove(nemico)
            i -= 1

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

        sposta = False

gameloop()

'''pygame.draw.rect(schermo, grigioscu, (gsx // 32 * 0, gsy // 18 * 0, gpx * 16, gpy * 3))
                    messaggio("Aumento Lv: Pv +", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
                    messaggio("Aumento Lv: Attacco +", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
                    messaggio("Aumento Lv: Difesa +", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
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
                                    selezione.play()
                                    risposta = True
                    caricaini = True
                    tesoro = -1'''

'''if esc:
    schermo.fill(grigioscu)
    messaggio("Fine", grigiochi, gsx // 32 * 14, gsy // 18 * 8, 150)
    pygame.display.update()
    pygame.time.wait(500)
    pygame.quit()
    quit()'''
'''# linea(dove,colore,inizio,fine,spessore)
pygame.draw.line(schermo, verde, (0, 0), (gsx, gsy), 10)
# cerchio(dove,colore,centro,raggio,spessore)
pygame.draw.circle(schermo, blu, (300, 100), 5)
# rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
pygame.draw.rect(schermo, rosso, (200, 100, 30, 40), 5)'''
'''# canzone
c1 = pygame.mixer.Sound("Audio/Canzone11.wav")
c1.play(-1))'''
