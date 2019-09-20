# -*- coding: utf-8 -*-

import copy

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
            primopas = False
            tastotemp = 5
            tastop = 0
            startf = False
            aumentoliv = False
            primopasso = True
            contaesca = 0
            xesca = 0
            yesca = 0
            creaesca = False
            vitaesca = []
            premuti = 0
            contattogg = 0
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

        # caricare gli oggetti
        if carim:
            premuti = 0
            contattogg = 0
            if pers == persw:
                agg = 1
            if pers == persa:
                agg = 2
            if pers == perss:
                agg = 3
            if pers == persd:
                agg = 4
            # stanza
            stanzaa = pygame.image.load("Immagini\Paesaggi\Stanza%ia.png" % dati[1]).convert()
            stanzaa = pygame.transform.scale(stanzaa, (gsx, gsy))
            sfondinoa = pygame.image.load("Immagini\Paesaggi\Sfondino%ia.png" % dati[1]).convert()
            sfondinoa = pygame.transform.scale(sfondinoa, (gpx, gpy))
            sfondinob = pygame.image.load("Immagini\Paesaggi\Sfondino%ib.png" % dati[1]).convert()
            sfondinob = pygame.transform.scale(sfondinob, (gpx, gpy))
            sfondinoc = pygame.image.load("Immagini\Paesaggi\Sfondino%ic.png" % dati[1]).convert()
            sfondinoc = pygame.transform.scale(sfondinoc, (gpx, gpy))
            portaVert = pygame.image.load("Immagini\Paesaggi\PortaV%i.png" % dati[1])
            portaVert = pygame.transform.scale(portaVert, (gpx, gpy))
            portaOriz = pygame.image.load("Immagini\Paesaggi\PortaO%i.png" % dati[1])
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

                muovirob = 0

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

                muovirob = 0

            if cambiosta:
                stanza = dati[1]
                # fermare la camminata dopo il cambio stanza
                nx = 0
                ny = 0
                primopas = False
                tastop = 0
                # per inizializzare i mostri

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
                i = 1
                while i < len(vitaesca):
                    del vitaesca[i + 2]
                    del vitaesca[i + 1]
                    del vitaesca[i]
                    del vitaesca[i - 1]

                # cambiosta viene cambiato sopra !!!!!!!!!!!!
                cambiosta = False

            # arma
            armaw = pygame.image.load("Immagini\Armi\Arma%iw.png" % dati[6])
            armaw = pygame.transform.scale(armaw, (gpx, gpy))
            armaa = pygame.image.load("Immagini\Armi\Arma%ia.png" % dati[6])
            armaa = pygame.transform.scale(armaa, (gpx, gpy))
            armas = pygame.image.load("Immagini\Armi\Arma%is.png" % dati[6])
            armas = pygame.transform.scale(armas, (gpx, gpy))
            armad = pygame.image.load("Immagini\Armi\Arma%id.png" % dati[6])
            armad = pygame.transform.scale(armad, (gpx, gpy))
            # armatura
            armaturaw = pygame.image.load("Immagini\Armature\Armatura%iw.png" % dati[8])
            armaturaw = pygame.transform.scale(armaturaw, (gpx, gpy))
            armaturaa = pygame.image.load("Immagini\Armature\Armatura%ia.png" % dati[8])
            armaturaa = pygame.transform.scale(armaturaa, (gpx, gpy))
            armaturas = pygame.image.load("Immagini\Armature\Armatura%is.png" % dati[8])
            armaturas = pygame.transform.scale(armaturas, (gpx, gpy))
            armaturad = pygame.image.load("Immagini\Armature\Armatura%id.png" % dati[8])
            armaturad = pygame.transform.scale(armaturad, (gpx, gpy))
            # scudo
            scudow = pygame.image.load("Immagini\Scudi\Scudo%iw.png" % dati[7])
            scudow = pygame.transform.scale(scudow, (gpx, gpy))
            scudoa = pygame.image.load("Immagini\Scudi\Scudo%ia.png" % dati[7])
            scudoa = pygame.transform.scale(scudoa, (gpx, gpy))
            scudos = pygame.image.load("Immagini\Scudi\Scudo%is.png" % dati[7])
            scudos = pygame.transform.scale(scudos, (gpx, gpy))
            scudod = pygame.image.load("Immagini\Scudi\Scudo%id.png" % dati[7])
            scudod = pygame.transform.scale(scudod, (gpx, gpy))
            # armatura robot
            armrobw = pygame.image.load("Immagini\Armrobs\Armrob%iw.png" % dati[9])
            armrobw = pygame.transform.scale(armrobw, (gpx, gpy))
            armroba = pygame.image.load("Immagini\Armrobs\Armrob%ia.png" % dati[9])
            armroba = pygame.transform.scale(armroba, (gpx, gpy))
            armrobs = pygame.image.load("Immagini\Armrobs\Armrob%is.png" % dati[9])
            armrobs = pygame.transform.scale(armrobs, (gpx, gpy))
            armrobd = pygame.image.load("Immagini\Armrobs\Armrob%id.png" % dati[9])
            armrobd = pygame.transform.scale(armrobd, (gpx, gpy))
            if agg == 1:
                arma = armaw
                armatura = armaturaw
                scudo = scudow
            if agg == 2:
                arma = armaa
                armatura = armaturaa
                scudo = scudoa
            if agg == 3:
                arma = armas
                armatura = armaturas
                scudo = scudos
            if agg == 4:
                arma = armad
                armatura = armaturad
                scudo = scudod
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

            caricaini = True
            carim = False
            tastotemp = 10

        if inizio:
            arma = armas
            armatura = armaturas
            scudo = scudos
            robot = robos
            armrob = armrobs
            inizio = False

        # rallenta per i 30 fps
        '''if not primopas and tastotempfps != 0 and premuti >= 1:
            tastotempfps = tastotempfps - 1
            nx = 0
            ny = 0
        if not primopas and tastotempfps == 0 and premuti >= 1:
            if tastop == pygame.K_w:
                ny = -gpy
            if tastop == pygame.K_a:
                nx = -gpx
            if tastop == pygame.K_s:
                ny = gpy
            if tastop == pygame.K_d:
                nx = gpx
            tastotempfps = 5'''

        # controllo primo passo
        if primopas and tastotemp != 0 and premuti >= 1:
            tastotemp = tastotemp - 1
            nx = 0
            ny = 0
        if primopas and tastotemp == 0 and premuti >= 1:
            if tastop == pygame.K_w:
                ny = -gpy
            if tastop == pygame.K_a:
                nx = -gpx
            if tastop == pygame.K_s:
                ny = gpy
            if tastop == pygame.K_d:
                nx = gpx
            primopas = False
            tastotemp = 5

        tastoTrovato = False
        # catturare gli eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN and not aumentoliv:
                # movimanti
                tastop = event.key
                # movimenti personaggio
                if event.key == pygame.K_w and not tastoTrovato:
                    tastoTrovato = True
                    premuti += 1
                    npers = 3
                    pers = persw
                    arma = armaw
                    armatura = armaturaw
                    scudo = scudow
                    ny = -gpy
                    nx = 0
                    primopas = True
                if event.key == pygame.K_a and not tastoTrovato:
                    tastoTrovato = True
                    premuti += 1
                    npers = 2
                    pers = persa
                    arma = armaa
                    armatura = armaturaa
                    scudo = scudoa
                    nx = -gpx
                    ny = 0
                    primopas = True
                if event.key == pygame.K_s and not tastoTrovato:
                    tastoTrovato = True
                    premuti += 1
                    npers = 4
                    pers = perss
                    arma = armas
                    armatura = armaturas
                    scudo = scudos
                    ny = gpy
                    nx = 0
                    primopas = True
                if event.key == pygame.K_d and not tastoTrovato:
                    tastoTrovato = True
                    premuti += 1
                    npers = 1
                    pers = persd
                    arma = armad
                    armatura = armaturad
                    scudo = scudod
                    nx = gpx
                    ny = 0
                    primopas = True

                nemicoInMovimento = False
                for nemico in listaNemici:
                    if nemico.mosseRimaste > 0:
                        nemicoInMovimento = True
                        break

                if event.key == pygame.K_e and not tastoTrovato and muovirob <= 0 and not nemicoInMovimento:
                    tastoTrovato = True
                    nx = 0
                    ny = 0
                    attacco = 1
                if event.key == pygame.K_x and not tastoTrovato and muovirob <= 0 and not nemicoInMovimento:
                    tastoTrovato = True
                    nx = 0
                    ny = 0
                    if chiamarob:
                        chiamarob = False
                    else:
                        chiamarob = True

                if event.key == pygame.K_SPACE and not tastoTrovato and muovirob <= 0 and not nemicoInMovimento:
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
                            suonoaperturacopo.play()
                            porte[k + 3] = True
                            # scoprire caselle viste
                            caseviste = scopriCaselleViste(x, y, rx, ry, numstanza, porte, cofanetti, caseviste)
                            caricaini = True
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
                            suonoaperturacopo.play()
                            sposta = True
                            dati, tesoro = aperturacofanetto(cofanetti[i], cofanetti[i + 1], cofanetti[i + 2], dati)
                            cofanetti[i + 3] = True
                            caricaini = True
                            # aggiornare vettore tutticofanetti
                            j = 0
                            while j < len(tutticofanetti):
                                if tutticofanetti[j] == cofanetti[i] and tutticofanetti[j + 1] == cofanetti[i + 1] and \
                                        tutticofanetti[j + 2] == cofanetti[i + 2]:
                                    tutticofanetti[j + 3] = True
                                j = j + 4
                        i = i + 4

                if event.key == pygame.K_ESCAPE and not tastoTrovato and muovirob <= 0 and not nemicoInMovimento:
                    tastoTrovato = True
                    startf = True

            if event.type == pygame.KEYUP:
                if tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d:
                    premuti -= 1
                    if event.key == tastop:
                        premuti = 0
                else:
                    premuti = 0
                if premuti == 0:
                    nx = 0
                    ny = 0
                    primopas = False
                    tastotemp = 5
                    tastotempfps = 5
                    tastop = 0

        # statistiche personaggio e robo (liv + arm + scu)
        # se modifichi -> modifica anche equip, equiprobo e ovunque si presenta pvtot
        esptot, pvtot, entot, att, dif, difro, par = getStatistiche(dati, difesa)

        # ripristina vita e status dopo lv up
        if aumentoliv:
            dati[5] = pvtot
            dati[121] = False
            aumentoliv = False

        # menu start
        if startf and attacco != 1:
            selsta.play()
            dati[2] = x
            dati[3] = y
            if not apriocchio:
                dati, inizio, attacco = start(dati, nmost, porteini, portefin, cofaniini, cofanifin, tutteporte, tutticofanetti, apriocchio)
            else:
                dati, attacco, sposta = startBattaglia(dati)
            if attacco != 0:
                contattogg = 1
            carim = True
            startf = False

        # morte tua e di robo
        inizio = controllaMorteRallo(dati[5], inizio)
        morterob, dati, muovirob = controllaMorteColco(dati, muovirob)

        # movimento-azioni personaggio
        nemiciInMovimento = False
        for nemico in listaNemici:
            if nemico.mosseRimaste > 0:
                nemiciInMovimento = True
                break
        if (nx != 0 or ny != 0) and not nemiciInMovimento:
            # progresso - stanza - x - y - liv - pv - arma - scudo - armatura - armrob - energiarob - tecniche(20) - oggetti(50) - condizioni(20) - gambit(20) - veleno - surriscalda // dimensione: 0-122
            vx = x
            vy = y
            sposta = True
            stanzaVecchia = dati[1]
            x, y, dati[1], carim, inutile, cambiosta = muri_porte(x, y, nx, ny, dati[1], carim, 0, False, False, porte, cofanetti)

            sovrapposto = False
            for nemico in listaNemici:
                if nemico.x == x and nemico.y == y:
                    sovrapposto = True
                    break
            if (x == rx and y == ry) or sovrapposto:
                x = vx
                y = vy
        # gestione attacchi
        if attacco != 0 and attacco <= 6 and contattogg == 0:
            sposta, creaesca, xesca, yesca, npers, nrob, difesa, apriChiudiPorta, apriCofanetto, spingiColco, listaNemici = attacca(x, y, npers, nrob, rx, ry, pers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126], stanzaa, dati[1], sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, robot, armrob, att, attacco, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici)
            caricaini = True
            # cambiare posizione dopo l'attacco
            if npers == 3:
                pers = persw
                arma = armaw
                armatura = armaturaw
                scudo = scudow
            if npers == 2:
                pers = persa
                arma = armaa
                armatura = armaturaa
                scudo = scudoa
            if npers == 4:
                pers = perss
                arma = armas
                armatura = armaturas
                scudo = scudos
            if npers == 1:
                pers = persd
                arma = armad
                armatura = armaturad
                scudo = scudod
            # decrementa oggetto utilizzato
            if sposta:
                # bomba attacco = 2
                if attacco == 2:
                    dati[33] = dati[33] - 1
                # bomba veleno attacco = 3
                if attacco == 3:
                    dati[35] = dati[35] - 1
                # esca attacco = 4
                if attacco == 4:
                    dati[36] = dati[36] - 1
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
            sposta = False
            esptot, pvtot, entot, att, dif, difro, par = getStatistiche(dati, difesa)
            if difesa == 2:
                difesa = 1
                sposta = True
                dati[5] = dati[5] + 3
                if dati[5] > pvtot:
                    dati[5] = pvtot
        # gestione att+ e dif+
        if dati[123] > 0:
            att = att + att // 4
            if sposta:
                dati[123] = dati[123] - 1
        if dati[124] > 0:
            dif = dif + dif // 4
            if sposta:
                dati[124] = dati[124] - 1
        # veleno
        if dati[121] and sposta:
            dati[5] = dati[5] - 3
            if dati[5] < 0:
                dati[5] = 0
        # apertura/chiusura porte
        if apriChiudiPorta[0]:
            k = 0
            while k < len(porte):
                if porte[k] == dati[1] and porte[k + 1] == apriChiudiPorta[1] and porte[k + 2] == apriChiudiPorta[2]:
                    suonoaperturacopo.play()
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
        # apertura cofanetti
        if apriCofanetto[0]:
            i = 0
            while i < len(cofanetti):
                if cofanetti[i] == dati[1] and cofanetti[i + 1] == apriCofanetto[1] and cofanetti[i + 2] == apriCofanetto[2] and not cofanetti[i + 3]:
                    suonoaperturacopo.play()
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
                n = 0
                while n < 32:
                    if vitaesca[i + 1] == gpx * n:
                        m = 0
                        while m < 18:
                            if vitaesca[i + 2] == gpy * m:
                                if (n + m) % 2 == 0:
                                    schermo.blit(sfondinoa, (vitaesca[i + 1], vitaesca[i + 2]))
                                if (n + m) % 2 != 0:
                                    schermo.blit(sfondinob, (vitaesca[i + 1], vitaesca[i + 2]))
                            m = m + 1
                    n = n + 1
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
                dati[36] = dati[36] + 1
            i = i + 4

        # movimento-azioni robo
        if dati[122] > 0:
            # se surriscaldato toglie vel+ e efficienza
            dati[125] = 0
            dati[126] = 0
        if ((sposta and muovirob <= 0) or muovirob > 0) and not morterob and not cambiosta:
            vrx = rx
            vry = ry

            # surriscalda
            if dati[122] > 0:
                dati[122] = dati[122] - 1
                dati[10] = dati[10] - 3
                if muovirob == 0:
                    muovirob = -2

            # efficienza
            if dati[126] > 0:
                if dati[125] > 0:
                    if muovirob == 1 or muovirob == -1:
                        dati[126] = dati[126] - 1
                else:
                    dati[126] = dati[126] - 1

            # vel+
            if dati[125] > 0:
                if muovirob == 1 or muovirob == -1:
                    dati[125] = dati[125] - 1
                if dati[125] == 0:
                    dati[122] = 10
                if muovirob == 0:
                    muovirob = 2

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
            rx, ry, muovirob, nrob, dati, vetDatiNemici, raffreddamento, ricarica1, ricarica2 = movrobo(x, y, vx, vy, rx, ry, dati[1], muovirob, chiamarob, dati, porte, cofanetti, vetDatiNemici, nmost, difesa)
            i = 0
            for nemico in listaNemici:
                nemico.vita = vetDatiNemici[i]
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

            # effetto di raffreddamento
            if True:
                if raffreddamento:
                    muovirob = -2
                    raffredda = 1
                if raffredda == 0:
                    dati[122] = 0
                if raffredda >= 0:
                    raffredda -= 1
            # effetto auto-ricarica
            if True:
                if ricarica1:
                    muovirob = -2
                    autoRic1 = 1
                if autoRic1 == 0:
                    dati[10] += dannoTecniche[6]
                    if dati[10] > entot:
                        dati[10] = entot
                    dati[122] = 10
                if autoRic1 >= 0:
                    autoRic1 -= 1
            # effetto auto-ricarica+
            if True:
                if ricarica2:
                    muovirob = -2
                    autoRic2 = 1
                if autoRic2 == 0:
                    dati[10] += dannoTecniche[16]
                    if dati[10] > entot:
                        dati[10] = entot
                    dati[122] = 10
                if autoRic2 >= 0:
                    autoRic2 -= 1

            sovrapposto = False
            for nemico in listaNemici:
                if nemico.x == rx and nemico.y == ry:
                    sovrapposto = True
                    break
            if (rx == x and ry == y) or sovrapposto or muovirob < 0:
                rx = vrx
                ry = vry
                nrob = 0
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
        # gestione tecniche
        if attacco != 0 and attacco > 6 and contattogg == 0:
            caricaini = True
            # cambiare posizione dopo l'attacco
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
        if morterob:
            robot = robomo
            armrob = armrobmo

        # movimento-azioni mostri
        if nmost > 0 and not cambiosta:
            vetDatiNemici = []
            for nemico in listaNemici:
                vetDatiNemici.append(nemico.vita)
                vetDatiNemici.append(nemico.x)
                vetDatiNemici.append(nemico.y)
                vetDatiNemici.append(nemico.vitaTotale)
            for nemico in listaNemici:
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
                    if nemico.mosseRimaste > 0:
                        nemico.vx = nemico.x
                        nemico.vy = nemico.y
                        nemico, direzioneMostro, dati, vitaesca = movmostro(x, y, rx, ry, nemico, dati[1], dif, difro, par, dati, vitaesca, porte, cofanetti, vetDatiNemici)
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
                    elif sposta and nemico.mosseRimaste == 0:
                        nemico.resettaMosseRimaste()
                    elif sposta and nemico.mosseRimaste < 0:
                        nemico.mosseRimaste += 1
                elif nemico.vita <= 0:
                    nmost -= 1
                    dati[127] += nemico.esp
                    nemico.morto = True
                    listaNemici.remove(nemico)

        # aumentare di livello
        if dati[127] >= esptot and dati[4] < 100 and not carim and not inizio:
            dati[4] = dati[4] + 1
            dati[127] = dati[127] - esptot
            aumentoliv = True

        # aggiorna vista dei mostri e metti l'occhio se ti vedono
        apriocchio = False
        for nemico in listaNemici:
            nemico.aggiornaVista(x, y, rx, ry, dati[1], porte, cofanetti, dati)
            if nemico.visto:
                apriocchio = True
                break

        # fai tutte le animazioni del turno e disegnare gli sfondi e personaggi
        if not inizio:
            primopasso, caricaini, tesoro = anima(sposta, x, y, vx, vy, rx, ry, vrx, vry, pers, robot, npers, nrob, primopasso, cambiosta, sfondinoa, sfondinob, scudo, armatura, arma, armrob, dati, attacco, difesa, tastop, tesoro, sfondinoc, aumentoliv, carim, caricaini, listaNemici, listaNemiciTotali)
            if not carim:
                ambiente_movimento(x, y, npers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126], vx, vy, rx, ry, vrx, vry, pers, stanzaa, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, robot, armrob, caricaini, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza, listaNemici)

        # calncella deinitivamente i mostri morti
        for nemico in listaNemiciTotali:
            if nemico.morto:
                listaNemiciTotali.remove(nemico)

        if not aumentoliv:
            caricaini = False

        vx = x
        vy = y
        vrx = rx
        vry = ry
        if contattogg != 1:
            attacco = 0

        sposta = False

        # mostra il framerate
        #if clock.get_fps() < 27:
        #    print (clock.get_fps())

        pygame.display.update()
        clock.tick(fps)

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
c1 = pygame.mixer.Sound("Audio\Canzone11.wav")
c1.play(-1))'''
