# -*- coding: utf-8 -*-

import os
import random
from GlobalVarG2 import *


def messaggio(msg, colore, x, y, gr):
    gr = gr - 10
    gr = gpx * gr // 60
    y = y - (gpy // 8)
    carattere = "Gentium Book Basic"
    font = pygame.font.SysFont(carattere, gr)
    testo = font.render(msg, True, colore)
    schermo.blit(testo, (x, y))


def getStatistiche(dati, difesa=0):
    esptot = 1 + pow(dati[4], 2) + (dati[4] * 2)
    pvtot = 50
    if dati[129] == 1:
        pvtot += 50
    attVicino = 6 + ((dati[6] * dati[6]) * 10)
    attLontano = 4 + ((dati[128] * dati[128]) * 10)
    if dati[129] == 3:
        attVicino += 20
        attLontano += 20
    dif = 7 + ((dati[8] * dati[8]) * 10) + 5 + ((dati[7] * dati[7]) * 5)
    if dati[129] == 2:
        dif += 30
    par = 2 + ((dati[7] * dati[7]) * 3)
    if dati[129] == 4:
        par += 10
    if difesa != 0:
        par = par * 2
        dif = dif + dif // 2

    if dati[4] >= 1:
        i = 1
        while i <= 100:
            if dati[4] <= i + 2:
                pvtot += (i * 5)
                break
            i += 3

    if dati[4] >= 2:
        i = 2
        while i <= 100:
            if dati[4] <= i + 2:
                attVicino += (i * 3)
                attLontano += (i * 2)
                break
            i += 3

    if dati[4] >= 3:
        i = 3
        while i <= 100:
            if dati[4] <= i + 2:
                dif += (i * 2)
                break
            i += 3

    entot = 220 + (dati[9] * dati[9] * 80)
    difro = 20 + (dati[9] * dati[9] * 30)

    return esptot, pvtot, entot, attVicino, attLontano, dif, difro, par


def getVitaTotRallo(livello, guanti):
    pvtot = 50
    if guanti == 1:
        pvtot += 50
    if livello >= 1:
        i = 1
        while i <= 100:
            if livello <= i + 2:
                pvtot += (i * 5)
                break
            i += 3
    return pvtot


def guardaVideo(path, audio=0):
    schermo.fill(grigioscu)
    pygame.display.update()
    listaImg = []
    # load all the images
    for i in os.listdir(path):
        img = pygame.image.load(path + '/' + i).convert()
        img = pygame.transform.scale(img, (gsx, gsy))
        listaImg.append(img)
    if audio != 0:
        canaleSoundCanzone.play(audio)
    # play video
    i = 0
    while i < len(listaImg) + 10:
        if i >= 10:
            schermo.blit(listaImg[i - 10], (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    canaleSoundPuntatore.play(selezione)
                    if audio != 0:
                        canaleSoundCanzone.stop()
                    return True
        pygame.event.pump()
        clockVideo.tick(fpsVideo)
        i += 1
    if audio != 0:
        canaleSoundCanzone.stop()
    return False


def salvataggio(n, dati, porteini, portefin, cofaniini, cofanifin, porte, cofanetti):
    scrivi = open("Salvataggi/Salvataggio%i.txt" % n, "w")
    # conversione della posizione in caselle
    dati[2] = dati[2] // gpx
    dati[3] = dati[3] // gpy
    i = porteini
    while i <= portefin:
        j = 0
        while j < len(porte):
            if dati[i] == porte[j] and dati[i + 1] == porte[j + 1] and dati[i + 2] == porte[j + 2]:
                dati[i + 3] = porte[j + 3]
            j = j + 4
        dati[i + 1] = dati[i + 1] // gpx
        dati[i + 2] = dati[i + 2] // gpy
        i = i + 4
    i = cofaniini
    while i <= cofanifin:
        j = 0
        while j < len(cofanetti):
            if dati[i] == cofanetti[j] and dati[i + 1] == cofanetti[j + 1] and dati[i + 2] == cofanetti[j + 2]:
                dati[i + 3] = cofanetti[j + 3]
            j = j + 4
        dati[i + 1] = dati[i + 1] // gpx
        dati[i + 2] = dati[i + 2] // gpy
        i = i + 4

    for i in range(0, len(dati)):
        scrivi.write("%i_" % dati[i])
    scrivi.close()

    # conversione della posizione in pixel
    dati[2] = dati[2] * gpx
    dati[3] = dati[3] * gpy
    i = porteini
    while i <= portefin:
        dati[i + 1] = dati[i + 1] * gpx
        dati[i + 2] = dati[i + 2] * gpy
        i = i + 4
    i = cofaniini
    while i <= cofanifin:
        dati[i + 1] = dati[i + 1] * gpx
        dati[i + 2] = dati[i + 2] * gpy
        i = i + 4


def oggetto(x, y, dimx, dimy, px, py, nx, ny):
    a = x
    b = y
    dimx = dimx + x
    dimy = dimy + y
    while x < dimx:
        if (ny == -gpy and py == dimy and px == x) or (ny == gpy and py == y - gpy and px == x):
            return True
        x = x + gpx
    x = a
    y = b
    while y < dimy:
        if (nx == -gpx and px == dimx and py == y) or (nx == gpx and px == x - gpx and py == y):
            return True
        y = y + gpy


def muri_porte(x, y, nx, ny, stanza, carim, mostro, robo, porte, cofanetti):
    cambiosta = False
    # prima stanza
    if (stanza == 1) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if ny == -gpy and x == gsx // 32 * 6 and y == gsy // 18 * 2 and not mostro and not robo:
            stanza = 2
            cambiosta = True
            carim = True
        else:
            # bordi stanza
            if nx == -gpx and x <= gpx * 2:
                nx = 0
            if nx == gpx and x >= gsx - (gpx * 3):
                nx = 0
            if ny == -gpy and y <= gpy * 2:
                ny = 0
            if ny == gpy and y >= gsy - (gpy * 3):
                ny = 0
        # controllo muri-oggetti
        #          posizione x    posizione y     dim x    dim y   px py  nx  ny
        if oggetto(gsx // 32 * 7, gsy // 18 * 11, gpx * 1, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 18, gsy // 18 * 7, gpx * 2, gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 21, gsy // 18 * 11, gpx * 4, gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        # controllo se le porte sono chiuse o aperte
        i = 0
        while i < len(porte):
            if not porte[i + 3]:
                if oggetto(porte[i + 1], porte[i + 2], gpx * 1, gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
            i = i + 4
        # controllo cofanetti
        i = 0
        while i < len(cofanetti):
            if oggetto(cofanetti[i + 1], cofanetti[i + 2], gpx * 1, gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            i = i + 4
    # seconda stanza
    if (stanza == 2) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if ny == -gpy and x == gsx // 32 * 6 and y == gsy // 18 * 2 and not mostro and not robo:
            stanza = 1
            cambiosta = True
            carim = True
        else:
            # bordi stanza
            if nx == -gpx and x <= gpx * 2:
                nx = 0
            if nx == gpx and x >= gsx - (gpx * 3):
                nx = 0
            if ny == -gpy and y <= gpy * 2:
                ny = 0
            if ny == gpy and y >= gsy - (gpy * 3):
                ny = 0
        # controllo muri-oggetti
        #          posizione x    posizione y    dim x    dim y    px py nx  ny
        if oggetto(gsx // 32 * 9, gsy // 18 * 2, gpx * 1, gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 2, gsy // 18 * 7, gpx * 1, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 4, gsy // 18 * 7, gpx * 12, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 2, gsy // 18 * 11, gpx * 6, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 7, gsy // 18 * 13, gpx * 5, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 9, gsy // 18 * 13, gpx * 1, gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 11, gsy // 18 * 11, gpx * 1, gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 13, gsy // 18 * 11, gpx * 3, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 15, gsy // 18 * 10, gpx * 1, gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 15, gsy // 18 * 4, gpx * 1, gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 15, gsy // 18 * 2, gpx * 1, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 15, gsy // 18 * 6, gpx * 9, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 23, gsy // 18 * 4, gpx * 4, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 23, gsy // 18 * 6, gpx * 1, gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 23, gsy // 18 * 13, gpx * 1, gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 26, gsy // 18 * 4, gpx * 1, gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 26, gsy // 18 * 6, gpx * 4, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        # controllo se le porte sono chiuse o aperte
        i = 0
        while i < len(porte):
            if not porte[i + 3]:
                if oggetto(porte[i + 1], porte[i + 2], gpx * 1, gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
            i = i + 4
        # controllo cofanetti
        i = 0
        while i < len(cofanetti):
            if oggetto(cofanetti[i + 1], cofanetti[i + 2], gpx * 1, gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            i = i + 4

    # movimento personaggio
    x = x + nx
    y = y + ny

    return x, y, stanza, carim, cambiosta


def trovacasattaccabili(x, y, stanza, porte, cofanetti, raggio):
    if raggio == -1:
        rangeXSinistra = (x // gpx) - 2
        rangeXDestra = (gsx // gpx) - (x // gpx) - 3
        rangeYAlto = (y // gpy) - 2
        rangeYBasso = (gsy // gpy) - (y // gpy) - 3
    else:
        rangeXSinistra = raggio // gpx
        if (x // gpx) - rangeXSinistra < 2:
            rangeXSinistra = (x // gpx) - 2
        rangeXDestra = raggio // gpx
        if (x // gpx) + rangeXDestra > 30:
            rangeXDestra = (gsx // gpx) - (x // gpx) - 3
        rangeYAlto = raggio // gpy
        if (y // gpy) - rangeYAlto < 2:
            rangeYAlto = (y // gpy) - 2
        rangeYBasso = raggio // gpy
        if (y // gpy) + rangeYBasso > 16:
            rangeYBasso = (gsy // gpy) - (y // gpy) - 3

    margineDiErrore = 1
    base1 = 0
    base2 = 0
    altezza = 0

    # caseattac[x, y, flag, ... ] -> per trovare gli ostacoli in basso a destra
    caseattac = []
    n = 0
    while n < rangeXDestra:
        m = 1
        while m <= rangeYBasso:
            murx = x + (gpx * n)
            mury = y + (gpy * m)
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, gpx, 0, stanza, False, True, False, porte, cofanetti)
            if murx != nmurx:
                caseattac.append(nmurx)
                caseattac.append(nmury)
                caseattac.append(True)
            else:
                caseattac.append(nmurx + gpx)
                caseattac.append(nmury)
                caseattac.append(False)
            m = m + 1
        n = n + 1
    n = 0
    while n < rangeYBasso:
        m = 1
        while m <= rangeXDestra:
            murx = x + (gpx * m)
            mury = y + (gpy * n)
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, 0, gpy, stanza, False, True, False, porte, cofanetti)
            if mury == nmury:
                i = 0
                while i < len(caseattac):
                    if caseattac[i] == nmurx and caseattac[i + 1] == nmury + gpy:
                        caseattac[i + 2] = False
                        break
                    i = i + 3
            m = m + 1
        n = n + 1
    #  caseattacbassodestra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli in basso a destra
    caseattacbassodestra = []
    # riempio caseattacbassodestra come se tutto il campo in basso a destra fosse libero
    n = 0
    while n <= rangeXDestra:
        m = 0
        while m <= rangeYBasso:
            caseattacbassodestra.append(x + (gpx * n))
            caseattacbassodestra.append(y + (gpy * m))
            caseattacbassodestra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacbassodestra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a destra dell'ostacolo
            xInizioRetta = (x + (gpx / 2.0))
            xFineRetta = caseattac[i] + gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (gpy / 2.0))
            yFineRetta = caseattac[i + 1] + gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #pygame.draw.line(schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacbassodestra):
                if caseattacbassodestra[j] == caseattac[i] and caseattacbassodestra[j + 1] == caseattac[i + 1]:
                    caseattacbassodestra[j + 2] = False
                elif caseattacbassodestra[j + 2]:
                    xLatoSinistroCasella = caseattacbassodestra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacbassodestra[j] + gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacbassodestra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacbassodestra[j + 1] + gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacbassodestra[j + 2] and yLatoSuperioreCasella >= caseattac[i + 1] and xLatoSinistroCasella >= caseattac[i]:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoDestro != 0:
                                area = (gpx * gpy) - ((gpx - latoSuperiore) * (gpy - latoDestro) / 2.0)
                            else:
                                if latoSuperiore == 0 and latoDestro != 0:
                                    altezza = latoInferiore
                                    base1 = latoSinistro
                                    base2 = latoDestro
                                elif latoDestro == 0 and latoSuperiore != 0:
                                    altezza = latoSinistro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                elif latoDestro == 0 and latoSuperiore == 0:
                                    altezza = latoSinistro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                area = (base1 + base2) * altezza / 2.0
                            if area > (gpx * gpy / 2.0) + margineDiErrore:
                                caseattacbassodestra[j + 2] = False
                        elif (yLatoSuperioreCasella <= yRetta2LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta2
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta2LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta2LatoSinistroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoSinistroCasella > yLatoInferioreCasella:
                                latoSinistro = gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoSinistro != 0:
                                area = (gpx * gpy) - ((gpx - latoInferiore) * (gpy - latoSinistro) / 2.0)
                            else:
                                if latoInferiore == 0 and latoSinistro != 0:
                                    altezza = latoSuperiore
                                    base1 = latoSinistro
                                    base2 = latoDestro
                                elif latoSinistro == 0 and latoInferiore != 0:
                                    altezza = latoDestro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                elif latoInferiore == 0 and latoSinistro == 0:
                                    altezza = latoDestro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                area = (base1 + base2) * altezza / 2.0
                            if area > (gpx * gpy / 2.0) + margineDiErrore:
                                caseattacbassodestra[j + 2] = False
                        elif (yLatoSuperioreCasella > yRetta1LatoDestroCasella and xLatoDestroCasella < xRetta1LatoSuperioreCasella) and (yLatoInferioreCasella < yRetta2LatoSinistroCasella and xLatoSinistroCasella > xRetta2LatoInferioreCasella):
                            caseattacbassodestra[j + 2] = False

                j += 3
        i += 3

    # caseattac[x, y, flag, ... ] -> per trovare gli ostacoli in basso a sinistra
    caseattac = []
    n = 0
    while n < rangeXSinistra:
        m = 1
        while m <= rangeYBasso:
            murx = x - (gpx * n)
            mury = y + (gpy * m)
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, -gpx, 0, stanza, False, True, False, porte, cofanetti)
            if murx != nmurx:
                caseattac.append(nmurx)
                caseattac.append(nmury)
                caseattac.append(True)
            else:
                caseattac.append(nmurx - gpx)
                caseattac.append(nmury)
                caseattac.append(False)
            m = m + 1
        n = n + 1
    n = 0
    while n < rangeYBasso:
        m = 1
        while m <= rangeXSinistra:
            murx = x - (gpx * m)
            mury = y + (gpy * n)
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, 0, gpy, stanza, False, True, False, porte, cofanetti)
            if mury == nmury:
                i = 0
                while i < len(caseattac):
                    if caseattac[i] == nmurx and caseattac[i + 1] == nmury + gpy:
                        caseattac[i + 2] = False
                        break
                    i = i + 3
            m = m + 1
        n = n + 1
    #  caseattacbassosinistra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli in basso a sinistra
    caseattacbassosinistra = []
    # riempio caseattacbassosinistra come se tutto il campo in basso a sinistra fosse libero
    n = 0
    while n <= rangeXSinistra:
        m = 0
        while m <= rangeYBasso:
            caseattacbassosinistra.append(x - (gpx * n))
            caseattacbassosinistra.append(y + (gpy * m))
            caseattacbassosinistra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacbassosinistra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a sinistra dell'ostacolo
            xInizioRetta = (x + (gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = - deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (gpx / 2.0))
            xFineRetta = caseattac[i] + gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (gpy / 2.0))
            yFineRetta = caseattac[i + 1] + gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = - deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #pygame.draw.line(schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacbassosinistra):
                if caseattacbassosinistra[j] == caseattac[i] and caseattacbassosinistra[j + 1] == caseattac[i + 1]:
                    caseattacbassosinistra[j + 2] = False
                elif caseattacbassosinistra[j + 2]:
                    xLatoSinistroCasella = caseattacbassosinistra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacbassosinistra[j] + gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacbassosinistra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacbassosinistra[j + 1] + gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacbassosinistra[j + 2] and yLatoSuperioreCasella >= caseattac[i + 1] and xLatoDestroCasella <= caseattac[i] + gpx:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoSinistro != 0:
                                area = (gpx * gpy) - ((gpx - latoSuperiore) * (gpy - latoSinistro) / 2.0)
                            else:
                                if latoSuperiore == 0 and latoSinistro != 0:
                                    altezza = latoInferiore
                                    base1 = latoSinistro
                                    base2 = latoDestro
                                elif latoSinistro == 0 and latoSuperiore != 0:
                                    altezza = latoDestro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                elif latoSinistro == 0 and latoSuperiore == 0:
                                    altezza = latoDestro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                area = (base1 + base2) * altezza / 2.0
                            if area > (gpx * gpy / 2.0) + margineDiErrore:
                                caseattacbassosinistra[j + 2] = False
                        elif (yLatoSuperioreCasella <= yRetta2LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta2
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta2LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta2LatoSinistroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoSinistroCasella > yLatoInferioreCasella:
                                latoSinistro = gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoDestro != 0:
                                area = (gpx * gpy) - ((gpx - latoInferiore) * (gpy - latoDestro) / 2.0)
                            else:
                                if latoInferiore == 0 and latoDestro != 0:
                                    altezza = latoSuperiore
                                    base1 = latoSinistro
                                    base2 = latoDestro
                                elif latoDestro == 0 and latoInferiore != 0:
                                    altezza = latoSinistro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                elif latoInferiore == 0 and latoDestro == 0:
                                    altezza = latoSinistro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                area = (base1 + base2) * altezza / 2.0
                            if area > (gpx * gpy / 2.0) + margineDiErrore:
                                caseattacbassosinistra[j + 2] = False
                        elif (yLatoSuperioreCasella > yRetta1LatoSinistroCasella and xLatoSinistroCasella > xRetta1LatoSuperioreCasella) and (yLatoInferioreCasella < yRetta2LatoDestroCasella and xLatoDestroCasella < xRetta2LatoInferioreCasella):
                            caseattacbassosinistra[j + 2] = False

                j += 3
        i += 3

    # caseattac[x, y, flag, ... ] -> per trovare gli ostacoli in alto a sinistra
    caseattac = []
    n = 0
    while n < rangeXSinistra:
        m = 1
        while m <= rangeYAlto:
            murx = x - (gpx * n)
            mury = y - (gpy * m)
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, -gpx, 0, stanza, False, True, False, porte, cofanetti)
            if murx != nmurx:
                caseattac.append(nmurx)
                caseattac.append(nmury)
                caseattac.append(True)
            else:
                caseattac.append(nmurx - gpx)
                caseattac.append(nmury)
                caseattac.append(False)
            m = m + 1
        n = n + 1
    n = 0
    while n < rangeYAlto:
        m = 1
        while m <= rangeXSinistra:
            murx = x - (gpx * m)
            mury = y - (gpy * n)
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, 0, -gpy, stanza, False, True, False, porte, cofanetti)
            if mury == nmury:
                i = 0
                while i < len(caseattac):
                    if caseattac[i] == nmurx and caseattac[i + 1] == nmury - gpy:
                        caseattac[i + 2] = False
                        break
                    i = i + 3
            m = m + 1
        n = n + 1
    # caseattacaltosinistra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli in alto a sinistra
    caseattacaltosinistra = []
    # riempio caseattacaltosinistra come se tutto il campo in alto a sinistra fosse libero
    n = 0
    while n <= rangeXSinistra:
        m = 0
        while m <= rangeYAlto:
            caseattacaltosinistra.append(x - (gpx * n))
            caseattacaltosinistra.append(y - (gpy * m))
            caseattacaltosinistra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacaltosinistra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a destra dell'ostacolo
            xInizioRetta = (x + (gpx / 2.0))
            xFineRetta = caseattac[i] + gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (gpy / 2.0))
            yFineRetta = caseattac[i + 1] + gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #pygame.draw.line(schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacaltosinistra):
                if caseattacaltosinistra[j] == caseattac[i] and caseattacaltosinistra[j + 1] == caseattac[i + 1]:
                    caseattacaltosinistra[j + 2] = False
                elif caseattacaltosinistra[j + 2]:
                    xLatoSinistroCasella = caseattacaltosinistra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacaltosinistra[j] + gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacaltosinistra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacaltosinistra[j + 1] + gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacaltosinistra[j + 2] and yLatoInferioreCasella <= caseattac[i + 1] + gpy and xLatoDestroCasella <= caseattac[i] + gpx:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoDestro != 0:
                                area = (gpx * gpy) - ((gpx - latoSuperiore) * (gpy - latoDestro) / 2.0)
                            else:
                                if latoSuperiore == 0 and latoDestro != 0:
                                    altezza = latoInferiore
                                    base1 = latoSinistro
                                    base2 = latoDestro
                                elif latoDestro == 0 and latoSuperiore != 0:
                                    altezza = latoSinistro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                elif latoDestro == 0 and latoSuperiore == 0:
                                    altezza = latoSinistro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                area = (base1 + base2) * altezza / 2.0
                            if area > (gpx * gpy / 2.0) + margineDiErrore:
                                caseattacaltosinistra[j + 2] = False
                        elif (yLatoSuperioreCasella <= yRetta2LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta2
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta2LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta2LatoSinistroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoSinistroCasella > yLatoInferioreCasella:
                                latoSinistro = gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoSinistro != 0:
                                area = (gpx * gpy) - ((gpx - latoInferiore) * (gpy - latoSinistro) / 2.0)
                            else:
                                if latoInferiore == 0 and latoSinistro != 0:
                                    altezza = latoSuperiore
                                    base1 = latoSinistro
                                    base2 = latoDestro
                                elif latoSinistro == 0 and latoInferiore != 0:
                                    altezza = latoDestro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                elif latoInferiore == 0 and latoSinistro == 0:
                                    altezza = latoDestro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                area = (base1 + base2) * altezza / 2.0
                            if area > (gpx * gpy / 2.0) + margineDiErrore:
                                caseattacaltosinistra[j + 2] = False
                        elif (yLatoSuperioreCasella > yRetta1LatoDestroCasella and xLatoDestroCasella < xRetta1LatoSuperioreCasella) and (yLatoInferioreCasella < yRetta2LatoSinistroCasella and xLatoSinistroCasella > xRetta2LatoInferioreCasella):
                            caseattacaltosinistra[j + 2] = False

                j += 3
        i += 3

    # caseattac[x, y, flag, ... ] -> per trovare gli ostacoli in alto a destra
    caseattac = []
    n = 0
    while n < rangeXDestra:
        m = 1
        while m <= rangeYAlto:
            murx = x + (gpx * n)
            mury = y - (gpy * m)
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, gpx, 0, stanza, False, True, False, porte, cofanetti)
            if murx != nmurx:
                caseattac.append(nmurx)
                caseattac.append(nmury)
                caseattac.append(True)
            else:
                caseattac.append(nmurx + gpx)
                caseattac.append(nmury)
                caseattac.append(False)
            m = m + 1
        n = n + 1
    n = 0
    while n < rangeYAlto:
        m = 1
        while m <= rangeXDestra:
            murx = x + (gpx * m)
            mury = y - (gpy * n)
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, 0, -gpy, stanza, False, True, False, porte, cofanetti)
            if mury == nmury:
                i = 0
                while i < len(caseattac):
                    if caseattac[i] == nmurx and caseattac[i + 1] == nmury - gpy:
                        caseattac[i + 2] = False
                        break
                    i = i + 3
            m = m + 1
        n = n + 1
    # caseattacaltodestra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli in alto a destra
    caseattacaltodestra = []
    # riempio caseattacaltodestra come se tutto il campo in alto a destra fosse libero
    n = 0
    while n <= rangeXDestra:
        m = 0
        while m <= rangeYAlto:
            caseattacaltodestra.append(x + (gpx * n))
            caseattacaltodestra.append(y - (gpy * m))
            caseattacaltodestra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacaltodestra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a sinistra dell'ostacolo
            xInizioRetta = (x + (gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = - deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (gpx / 2.0))
            xFineRetta = caseattac[i] + gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (gpy / 2.0))
            yFineRetta = caseattac[i + 1] + gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = - deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #pygame.draw.line(schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacaltodestra):
                if caseattacaltodestra[j] == caseattac[i] and caseattacaltodestra[j + 1] == caseattac[i + 1]:
                    caseattacaltodestra[j + 2] = False
                elif caseattacaltodestra[j + 2]:
                    xLatoSinistroCasella = caseattacaltodestra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacaltodestra[j] + gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacaltodestra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacaltodestra[j + 1] + gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacaltodestra[j + 2] and yLatoInferioreCasella <= caseattac[i + 1] + gpy and xLatoSinistroCasella >= caseattac[i]:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoSinistro != 0:
                                area = (gpx * gpy) - ((gpx - latoSuperiore) * (gpy - latoSinistro) / 2.0)
                            else:
                                if latoSuperiore == 0 and latoSinistro != 0:
                                    altezza = latoInferiore
                                    base1 = latoSinistro
                                    base2 = latoDestro
                                elif latoSinistro == 0 and latoSuperiore != 0:
                                    altezza = latoDestro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                elif latoSinistro == 0 and latoSuperiore == 0:
                                    altezza = latoDestro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                area = (base1 + base2) * altezza / 2.0
                            if area > (gpx * gpy / 2.0) + margineDiErrore:
                                caseattacaltodestra[j + 2] = False
                        elif (yLatoSuperioreCasella <= yRetta2LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta2
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta2LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta2LatoSinistroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoSinistroCasella > yLatoInferioreCasella:
                                latoSinistro = gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoDestro != 0:
                                area = (gpx * gpy) - ((gpx - latoInferiore) * (gpy - latoDestro) / 2.0)
                            else:
                                if latoInferiore == 0 and latoDestro != 0:
                                    altezza = latoSuperiore
                                    base1 = latoSinistro
                                    base2 = latoDestro
                                elif latoDestro == 0 and latoInferiore != 0:
                                    altezza = latoSinistro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                elif latoInferiore == 0 and latoDestro == 0:
                                    altezza = latoSinistro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                area = (base1 + base2) * altezza / 2.0
                            if area > (gpx * gpy / 2.0) + margineDiErrore:
                                caseattacaltodestra[j + 2] = False
                        elif (yLatoSuperioreCasella > yRetta1LatoSinistroCasella and xLatoSinistroCasella > xRetta1LatoSuperioreCasella) and (yLatoInferioreCasella < yRetta2LatoDestroCasella and xLatoDestroCasella < xRetta2LatoInferioreCasella):
                            caseattacaltodestra[j + 2] = False

                j += 3
        i += 3

    # caselle a destra del personaggio
    caseattac = []
    n = 0
    while n <= rangeXDestra:
        murx = x + (gpx * n)
        mury = y
        nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, gpx, 0, stanza, False, True, False, porte, cofanetti)
        if murx != nmurx:
            caseattac.append(nmurx)
            caseattac.append(nmury)
            caseattac.append(True)
        else:
            caseattac.append(nmurx + gpx)
            caseattac.append(nmury)
            caseattac.append(False)
        n += 1
    # caseattacdestra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli a destra
    caseattacdestra = []
    # riempio caseattacdestra come se tutto il campo a destra fosse libero
    n = 0
    while n <= rangeXDestra:
        m = 0
        while m <= rangeYAlto:
            caseattacdestra.append(x + (gpx * n))
            caseattacdestra.append(y - (gpy * m))
            caseattacdestra.append(True)
            m = m + 1
        m = 1
        while m <= rangeYBasso:
            caseattacdestra.append(x + (gpx * n))
            caseattacdestra.append(y + (gpy * m))
            caseattacdestra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacdestra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a sinistra dell'ostacolo
            xInizioRetta = (x + (gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = - deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (gpy / 2.0))
            yFineRetta = caseattac[i + 1] + gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #pygame.draw.line(schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacdestra):
                if caseattacdestra[j] == caseattac[i] and caseattacdestra[j + 1] == caseattac[i + 1]:
                    caseattacdestra[j + 2] = False
                elif caseattacdestra[j + 2]:
                    xLatoSinistroCasella = caseattacdestra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacdestra[j] + gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacdestra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacdestra[j + 1] + gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacdestra[j + 2] and xLatoSinistroCasella >= caseattac[i]:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoSinistro != 0:
                                area = (gpx * gpy) - ((gpx - latoSuperiore) * (gpy - latoSinistro) / 2.0)
                            else:
                                if latoSuperiore == 0 and latoSinistro != 0:
                                    altezza = latoInferiore
                                    base1 = latoSinistro
                                    base2 = latoDestro
                                elif latoSinistro == 0 and latoSuperiore != 0:
                                    altezza = latoDestro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                elif latoSinistro == 0 and latoSuperiore == 0:
                                    altezza = latoDestro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                area = (base1 + base2) * altezza / 2.0
                            if area > (gpx * gpy / 2.0) + margineDiErrore:
                                caseattacdestra[j + 2] = False
                        elif (yLatoSuperioreCasella <= yRetta2LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta2
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta2LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta2LatoSinistroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoSinistroCasella > yLatoInferioreCasella:
                                latoSinistro = gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoSinistro != 0:
                                area = (gpx * gpy) - ((gpx - latoInferiore) * (gpy - latoSinistro) / 2.0)
                            else:
                                if latoInferiore == 0 and latoSinistro != 0:
                                    altezza = latoSuperiore
                                    base1 = latoSinistro
                                    base2 = latoDestro
                                elif latoSinistro == 0 and latoInferiore != 0:
                                    altezza = latoDestro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                elif latoInferiore == 0 and latoSinistro == 0:
                                    altezza = latoDestro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                area = (base1 + base2) * altezza / 2.0
                            if area > (gpx * gpy / 2.0) + margineDiErrore:
                                caseattacdestra[j + 2] = False
                        elif (yLatoSuperioreCasella > yRetta1LatoSinistroCasella and xLatoSinistroCasella > xRetta1LatoSuperioreCasella) and (yLatoInferioreCasella < yRetta2LatoSinistroCasella and xLatoSinistroCasella > xRetta2LatoInferioreCasella):
                            caseattacdestra[j + 2] = False

                j += 3
        i += 3

    # caselle a sinistra del personaggio
    caseattac = []
    n = 0
    while n <= rangeXSinistra:
        murx = x - (gpx * n)
        mury = y
        nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, -gpx, 0, stanza, False, True, False, porte, cofanetti)
        if murx != nmurx:
            caseattac.append(nmurx)
            caseattac.append(nmury)
            caseattac.append(True)
        else:
            caseattac.append(nmurx - gpx)
            caseattac.append(nmury)
            caseattac.append(False)
        n += 1
    # caseattacsinistra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli a sinistra
    caseattacsinistra = []
    # riempio caseattacsinistra come se tutto il campo a sinistra fosse libero
    n = 0
    while n <= rangeXSinistra:
        m = 0
        while m <= rangeYAlto:
            caseattacsinistra.append(x - (gpx * n))
            caseattacsinistra.append(y - (gpy * m))
            caseattacsinistra.append(True)
            m = m + 1
        m = 1
        while m <= rangeYBasso:
            caseattacsinistra.append(x - (gpx * n))
            caseattacsinistra.append(y + (gpy * m))
            caseattacsinistra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacsinistra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a destra dell'ostacolo
            xInizioRetta = (x + (gpx / 2.0))
            xFineRetta = caseattac[i] + gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (gpx / 2.0))
            xFineRetta = caseattac[i] + gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (gpy / 2.0))
            yFineRetta = caseattac[i + 1] + gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = - deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #pygame.draw.line(schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacsinistra):
                if caseattacsinistra[j] == caseattac[i] and caseattacsinistra[j + 1] == caseattac[i + 1]:
                    caseattacsinistra[j + 2] = False
                elif caseattacsinistra[j + 2]:
                    xLatoSinistroCasella = caseattacsinistra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacsinistra[j] + gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacsinistra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacsinistra[j + 1] + gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacsinistra[j + 2] and xLatoDestroCasella <= caseattac[i] + gpx:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoDestro != 0:
                                area = (gpx * gpy) - ((gpx - latoSuperiore) * (gpy - latoDestro) / 2.0)
                            else:
                                if latoSuperiore == 0 and latoDestro != 0:
                                    altezza = latoInferiore
                                    base1 = latoSinistro
                                    base2 = latoDestro
                                elif latoDestro == 0 and latoSuperiore != 0:
                                    altezza = latoSinistro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                elif latoDestro == 0 and latoSuperiore == 0:
                                    altezza = latoSinistro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                area = (base1 + base2) * altezza / 2.0
                            if area > (gpx * gpy / 2.0) + margineDiErrore:
                                caseattacsinistra[j + 2] = False
                        elif (yLatoSuperioreCasella <= yRetta2LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta2
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta2LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta2LatoSinistroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoSinistroCasella > yLatoInferioreCasella:
                                latoSinistro = gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoDestro != 0:
                                area = (gpx * gpy) - ((gpx - latoInferiore) * (gpy - latoDestro) / 2.0)
                            else:
                                if latoInferiore == 0 and latoDestro != 0:
                                    altezza = latoSuperiore
                                    base1 = latoSinistro
                                    base2 = latoDestro
                                elif latoDestro == 0 and latoInferiore != 0:
                                    altezza = latoSinistro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                elif latoInferiore == 0 and latoDestro == 0:
                                    altezza = latoSinistro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                area = (base1 + base2) * altezza / 2.0
                            if area > (gpx * gpy / 2.0) + margineDiErrore:
                                caseattacsinistra[j + 2] = False
                        elif (yLatoSuperioreCasella > yRetta1LatoDestroCasella and xLatoDestroCasella < xRetta1LatoSuperioreCasella) and (yLatoInferioreCasella < yRetta2LatoDestroCasella and xLatoDestroCasella < xRetta2LatoInferioreCasella):
                            caseattacsinistra[j + 2] = False

                j += 3
        i += 3

    # caselle sopra il personaggio
    caseattac = []
    n = 0
    while n <= rangeYAlto:
        murx = x
        mury = y - (gpy * n)
        nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, 0, -gpy, stanza, False, True, False, porte, cofanetti)
        if mury != nmury:
            caseattac.append(nmurx)
            caseattac.append(nmury)
            caseattac.append(True)
        else:
            caseattac.append(nmurx)
            caseattac.append(nmury - gpy)
            caseattac.append(False)
        n += 1
    # caseattacalto[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli sopra
    caseattacalto = []
    # riempio caseattacalto come se tutto il campo sopra fosse libero
    n = 0
    while n <= rangeYAlto:
        m = 0
        while m <= rangeXDestra:
            caseattacalto.append(x + (gpx * m))
            caseattacalto.append(y - (gpy * n))
            caseattacalto.append(True)
            m = m + 1
        m = 1
        while m <= rangeXSinistra:
            caseattacalto.append(x - (gpx * m))
            caseattacalto.append(y - (gpy * n))
            caseattacalto.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacalto[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (gpy / 2.0))
            yFineRetta = caseattac[i + 1] + gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (gpx / 2.0))
            xFineRetta = caseattac[i] + gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (gpy / 2.0))
            yFineRetta = caseattac[i + 1] + gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = - deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #pygame.draw.line(schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacalto):
                if caseattacalto[j] == caseattac[i] and caseattacalto[j + 1] == caseattac[i + 1]:
                    caseattacalto[j + 2] = False
                elif caseattacalto[j + 2]:
                    xLatoSinistroCasella = caseattacalto[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacalto[j] + gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacalto[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacalto[j + 1] + gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacalto[j + 2] and yLatoInferioreCasella <= caseattac[i + 1] + gpy:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta2
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoSuperioreCasella)
                            elif yRetta1LatoSinistroCasella > yLatoInferioreCasella:
                                latoSinistro = gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta1LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoSinistro != 0:
                                area = (gpx * gpy) - ((gpx - latoInferiore) * (gpy - latoSinistro) / 2.0)
                            else:
                                if latoInferiore == 0 and latoSinistro != 0:
                                    altezza = latoSuperiore
                                    base1 = latoSinistro
                                    base2 = latoDestro
                                elif latoSinistro == 0 and latoInferiore != 0:
                                    altezza = latoDestro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                elif latoInferiore == 0 and latoSinistro == 0:
                                    altezza = latoDestro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                area = (base1 + base2) * altezza / 2.0
                            if area > (gpx * gpy / 2.0) + margineDiErrore:
                                caseattacalto[j + 2] = False
                        elif (yLatoSuperioreCasella <= yRetta2LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta2
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta2LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta2LatoSinistroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoSinistroCasella > yLatoInferioreCasella:
                                latoSinistro = gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoDestro != 0:
                                area = (gpx * gpy) - ((gpx - latoInferiore) * (gpy - latoDestro) / 2.0)
                            else:
                                if latoInferiore == 0 and latoDestro != 0:
                                    altezza = latoSuperiore
                                    base1 = latoSinistro
                                    base2 = latoDestro
                                elif latoDestro == 0 and latoInferiore != 0:
                                    altezza = latoSinistro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                elif latoInferiore == 0 and latoDestro == 0:
                                    altezza = latoSinistro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                area = (base1 + base2) * altezza / 2.0
                            if area > (gpx * gpy / 2.0) + margineDiErrore:
                                caseattacalto[j + 2] = False
                        elif (yLatoInferioreCasella < yRetta1LatoSinistroCasella and xLatoSinistroCasella > xRetta1LatoInferioreCasella) and (yLatoInferioreCasella < yRetta2LatoDestroCasella and xLatoDestroCasella < xRetta2LatoInferioreCasella):
                            caseattacalto[j + 2] = False

                j += 3
        i += 3

    # caselle sotto il personaggio
    caseattac = []
    n = 0
    while n <= rangeYBasso:
        murx = x
        mury = y + (gpy * n)
        nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, 0, gpy, stanza, False, True, False, porte, cofanetti)
        if mury != nmury:
            caseattac.append(nmurx)
            caseattac.append(nmury)
            caseattac.append(True)
        else:
            caseattac.append(nmurx)
            caseattac.append(nmury + gpy)
            caseattac.append(False)
        n += 1
    # caseattacbasso[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli a destra
    caseattacbasso = []
    # riempio caseattacbasso come se tutto il campo a destra fosse libero
    n = 0
    while n <= rangeYBasso:
        m = 0
        while m <= rangeXDestra:
            caseattacbasso.append(x + (gpx * m))
            caseattacbasso.append(y + (gpy * n))
            caseattacbasso.append(True)
            m = m + 1
        m = 1
        while m <= rangeXSinistra:
            caseattacbasso.append(x - (gpx * m))
            caseattacbasso.append(y + (gpy * n))
            caseattacbasso.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacbasso[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a sinistra dell'ostacolo
            xInizioRetta = (x + (gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = - deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in alto a destra dell'ostacolo
            xInizioRetta = (x + (gpx / 2.0))
            xFineRetta = caseattac[i] + gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #pygame.draw.line(schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacbasso):
                if caseattacbasso[j] == caseattac[i] and caseattacbasso[j + 1] == caseattac[i + 1]:
                    caseattacbasso[j + 2] = False
                elif caseattacbasso[j + 2]:
                    xLatoSinistroCasella = caseattacbasso[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacbasso[j] + gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacbasso[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacbasso[j + 1] + gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacbasso[j + 2] and yLatoSuperioreCasella >= caseattac[i + 1]:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoSinistro != 0:
                                area = (gpx * gpy) - ((gpx - latoSuperiore) * (gpy - latoSinistro) / 2.0)
                            else:
                                if latoSuperiore == 0 and latoSinistro != 0:
                                    altezza = latoInferiore
                                    base1 = latoSinistro
                                    base2 = latoDestro
                                elif latoSinistro == 0 and latoSuperiore != 0:
                                    altezza = latoDestro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                elif latoSinistro == 0 and latoSuperiore == 0:
                                    altezza = latoDestro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                area = (base1 + base2) * altezza / 2.0
                            if area > (gpx * gpy / 2.0) + margineDiErrore:
                                caseattacbasso[j + 2] = False
                        elif (yLatoSuperioreCasella <= yRetta2LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta2LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta2LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta2LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta2LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoDestro != 0:
                                area = (gpx * gpy) - ((gpx - latoSuperiore) * (gpy - latoDestro) / 2.0)
                            else:
                                if latoSuperiore == 0 and latoDestro != 0:
                                    altezza = latoInferiore
                                    base1 = latoSinistro
                                    base2 = latoDestro
                                elif latoDestro == 0 and latoSuperiore != 0:
                                    altezza = latoSinistro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                elif latoDestro == 0 and latoSuperiore == 0:
                                    altezza = latoSinistro
                                    base1 = latoInferiore
                                    base2 = latoSuperiore
                                area = (base1 + base2) * altezza / 2.0
                            if area > (gpx * gpy / 2.0) + margineDiErrore:
                                caseattacbasso[j + 2] = False
                        elif (yLatoSuperioreCasella > yRetta1LatoSinistroCasella and xLatoSinistroCasella > xRetta1LatoSuperioreCasella) and (yLatoSuperioreCasella > yRetta2LatoDestroCasella and xLatoDestroCasella < xRetta2LatoSuperioreCasella):
                            caseattacbasso[j + 2] = False

                j += 3
        i += 3

    caseattactot = caseattacaltodestra + caseattacaltosinistra + caseattacbassodestra + caseattacbassosinistra + caseattacdestra + caseattacsinistra + caseattacalto + caseattacbasso
    # tolgo le caselle duplicate
    i = 0
    while i < len(caseattactot):
        j = i + 3
        while j < len(caseattactot):
            if caseattactot[i] == caseattactot[j] and caseattactot[i + 1] == caseattactot[j + 1]:
                if not caseattactot[i + 2] or not caseattactot[j + 2]:
                    caseattactot[i + 2] = False
                del caseattactot[j + 2]
                del caseattactot[j + 1]
                del caseattactot[j]
            else:
                j += 3
        i += 3
    return caseattactot


def aperturacofanetto(stanza, cx, cy, dati):
    tesoro = -1
    # 11-30 -> tecniche(20) / 31-40 -> oggetti(10) / 41-70 -> armi(30) / 71-75 -> batterie(10) / 81-100 -> condizioni(20) / 101-120 -> gambit (=celle di memoria)(20) / 131 -> monete / 132 frecce
    if stanza == 1:
        if cx == gpx * 3 and cy == gpy * 7:
            tesoro = 31
        if cx == gpx * 7 and cy == gpy * 12:
            c = 0
            i = 101
            while i <= 120:
                if dati[i] == -1:
                    tesoro = i
                    break
                if c == 0:
                    c = 1
                    i = i + 10
                elif c == 1:
                    c = 0
                    i = i - 9
            if tesoro == -1:
                tesoro = -2
        if cx == gpx * 12 and cy == gpy * 11:
            c = 0
            i = 101
            while i <= 120:
                if dati[i] == -1:
                    tesoro = i
                    break
                if c == 0:
                    c = 1
                    i = i + 10
                elif c == 1:
                    c = 0
                    i = i - 9
            if tesoro == -1:
                tesoro = -2
    if stanza == 2:
        if cx == gpx * 3 and cy == gpy * 5:
            c = 0
            i = 101
            while i <= 120:
                if dati[i] == -1:
                    tesoro = i
                    break
                if c == 0:
                    c = 1
                    i = i + 10
                elif c == 1:
                    c = 0
                    i = i - 9
            if tesoro == -1:
                tesoro = -2
        if cx == gpx * 5 and cy == gpy * 10:
            tesoro = 11
        if cx == gpx * 10 and cy == gpy * 9:
            tesoro = 81

    # assegna oggetto ottenuto
    if tesoro != -1 and tesoro != -2:
        if tesoro >= 11 and tesoro <= 30:
            dati, tesoro = ottieniTecnica(dati, tesoro)
        elif tesoro >= 31 and tesoro <= 40:
            dati, tesoro = ottieniOggetto(dati, tesoro, 1)
        elif tesoro >= 41 and tesoro <= 75:
            dati, tesoro = ottieniArmaBatteria(dati, tesoro)
        elif tesoro >= 81 and tesoro <= 100:
            dati, tesoro = ottieniCondizione(dati, tesoro)
        elif tesoro >= 101 and tesoro <= 120:
            dati = ottieniCellaDiMemoria(dati, tesoro)
        elif tesoro == 131:
            dati[tesoro] = ottieniMonete(dati, 50)
        elif tesoro == 132:
            dati[tesoro] = ottieniFrecce(dati, 5)
        else:
            tesoro = -2
    return dati, tesoro


def scopriCaselleViste(x, y, rx, ry, numstanza, porte, cofanetti, caseviste):
    # contiene x e y delle caselle già esplorate
    caselleEsplorate = [x, y]

    # imposto tutte le caselle come non viste in caseviste
    i = 0
    while i < len(caseviste):
        caseviste[i + 2] = False
        i = i + 3

    # caselle viste da rallo
    j = 0
    while j < len(caselleEsplorate):
        nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -gpy, numstanza, False, True, False, porte, cofanetti)
        if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
            giaVisitata = False
            k = 0
            while k < len(caselleEsplorate):
                if caselleEsplorate[k] == nx and caselleEsplorate[k + 1] == ny:
                    giaVisitata = True
                    break
                k += 2
            if not giaVisitata:
                caselleEsplorate.append(nx)
                caselleEsplorate.append(ny)
            i = 0
            while i < len(caseviste):
                if caseviste[i] == nx and caseviste[i + 1] == ny:
                    caseviste[i + 2] = True
                    break
                i += 3
        nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, gpy, numstanza, False, True, False, porte, cofanetti)
        if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
            giaVisitata = False
            k = 0
            while k < len(caselleEsplorate):
                if caselleEsplorate[k] == nx and caselleEsplorate[k + 1] == ny:
                    giaVisitata = True
                    break
                k += 2
            if not giaVisitata:
                caselleEsplorate.append(nx)
                caselleEsplorate.append(ny)
            i = 0
            while i < len(caseviste):
                if caseviste[i] == nx and caseviste[i + 1] == ny:
                    caseviste[i + 2] = True
                    break
                i += 3
        nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], -gpx, 0, numstanza, False, True, False, porte, cofanetti)
        if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
            giaVisitata = False
            k = 0
            while k < len(caselleEsplorate):
                if caselleEsplorate[k] == nx and caselleEsplorate[k + 1] == ny:
                    giaVisitata = True
                    break
                k += 2
            if not giaVisitata:
                caselleEsplorate.append(nx)
                caselleEsplorate.append(ny)
            i = 0
            while i < len(caseviste):
                if caseviste[i] == nx and caseviste[i + 1] == ny:
                    caseviste[i + 2] = True
                    break
                i += 3
        nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], gpx, 0, numstanza, False, True, False, porte, cofanetti)
        if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
            giaVisitata = False
            k = 0
            while k < len(caselleEsplorate):
                if caselleEsplorate[k] == nx and caselleEsplorate[k + 1] == ny:
                    giaVisitata = True
                    break
                k += 2
            if not giaVisitata:
                caselleEsplorate.append(nx)
                caselleEsplorate.append(ny)
            i = 0
            while i < len(caseviste):
                if caseviste[i] == nx and caseviste[i + 1] == ny:
                    caseviste[i + 2] = True
                    break
                i += 3
        j += 2

    # se colco non è in una casella vista scopri il campo visto da colco
    incasevista = False
    i = 0
    while i < len(caseviste):
        if caseviste[i + 2] and caseviste[i] == rx and caseviste[i + 1] == ry:
            incasevista = True
            break
        i = i + 3
    if not incasevista:
        caselleEsplorate = [rx, ry]
        j = 0
        while j < len(caselleEsplorate):
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -gpy, numstanza, False, True, False, porte, cofanetti)
            if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                giaVisitata = False
                k = 0
                while k < len(caselleEsplorate):
                    if caselleEsplorate[k] == nx and caselleEsplorate[k + 1] == ny:
                        giaVisitata = True
                        break
                    k += 2
                if not giaVisitata:
                    caselleEsplorate.append(nx)
                    caselleEsplorate.append(ny)
                i = 0
                while i < len(caseviste):
                    if caseviste[i] == nx and caseviste[i + 1] == ny:
                        caseviste[i + 2] = True
                        break
                    i += 3
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, gpy, numstanza, False, True, False, porte, cofanetti)
            if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                giaVisitata = False
                k = 0
                while k < len(caselleEsplorate):
                    if caselleEsplorate[k] == nx and caselleEsplorate[k + 1] == ny:
                        giaVisitata = True
                        break
                    k += 2
                if not giaVisitata:
                    caselleEsplorate.append(nx)
                    caselleEsplorate.append(ny)
                i = 0
                while i < len(caseviste):
                    if caseviste[i] == nx and caseviste[i + 1] == ny:
                        caseviste[i + 2] = True
                        break
                    i += 3
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], -gpx, 0, numstanza, False, True, False, porte, cofanetti)
            if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                giaVisitata = False
                k = 0
                while k < len(caselleEsplorate):
                    if caselleEsplorate[k] == nx and caselleEsplorate[k + 1] == ny:
                        giaVisitata = True
                        break
                    k += 2
                if not giaVisitata:
                    caselleEsplorate.append(nx)
                    caselleEsplorate.append(ny)
                i = 0
                while i < len(caseviste):
                    if caseviste[i] == nx and caseviste[i + 1] == ny:
                        caseviste[i + 2] = True
                        break
                    i += 3
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], gpx, 0, numstanza, False, True, False, porte, cofanetti)
            if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                giaVisitata = False
                k = 0
                while k < len(caselleEsplorate):
                    if caselleEsplorate[k] == nx and caselleEsplorate[k + 1] == ny:
                        giaVisitata = True
                        break
                    k += 2
                if not giaVisitata:
                    caselleEsplorate.append(nx)
                    caselleEsplorate.append(ny)
                i = 0
                while i < len(caseviste):
                    if caseviste[i] == nx and caseviste[i + 1] == ny:
                        caseviste[i + 2] = True
                        break
                    i += 3
            j += 2

    return caseviste


def pathFinding(xPartenza, yPartenza, xArrivo, yArrivo, numstanza, porte, cofanetti, vetnemici):
    # caselleEsplorate contiene x, y e valore delle caselle già esplorate (il valore serve per trovare il percorso più breve)
    valoreCasella = 0
    caselleEsplorate = [xPartenza, yPartenza, valoreCasella]

    valorePiuBasso = 0
    xProssimaCasella = 0
    yProssimaCasella = 0
    percorsoTrovato = []

    impossibileRaggiungere = False
    if (xPartenza == xArrivo and yPartenza == yArrivo + gpy) or (xPartenza == xArrivo and yPartenza == yArrivo - gpy) or (xPartenza == xArrivo + gpx and yPartenza == yArrivo) or (xPartenza == xArrivo and yPartenza - gpx == yArrivo):
        k = 0
        while k < len(vetnemici):
            if xArrivo == vetnemici[k] and yArrivo == vetnemici[k + 1]:
                impossibileRaggiungere = True
            k += 2
    if xPartenza == xArrivo and yPartenza == yArrivo and not impossibileRaggiungere:
        percorsoTrovato = "arrivato"
    elif not impossibileRaggiungere:
        # caselle viste da Colco
        arrivato = False
        j = 0
        while j < len(caselleEsplorate):
            valoreCasella += 1
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -gpy, numstanza, False, True, False, porte, cofanetti)
            if nx == xArrivo and ny == yArrivo:
                caselleEsplorate.append(nx)
                caselleEsplorate.append(ny)
                caselleEsplorate.append(valoreCasella)
                arrivato = True
                break
            k = 0
            while k < len(vetnemici):
                if nx == vetnemici[k] and ny == vetnemici[k + 1]:
                    nx = caselleEsplorate[j]
                    ny = caselleEsplorate[j + 1]
                k += 2
            if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                giaVisitata = False
                k = 0
                while k < len(caselleEsplorate):
                    if caselleEsplorate[k] == nx and caselleEsplorate[k + 1] == ny:
                        giaVisitata = True
                        break
                    k += 3
                if not giaVisitata:
                    caselleEsplorate.append(nx)
                    caselleEsplorate.append(ny)
                    caselleEsplorate.append(valoreCasella)
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, gpy, numstanza, False, True, False, porte, cofanetti)
            if nx == xArrivo and ny == yArrivo:
                caselleEsplorate.append(nx)
                caselleEsplorate.append(ny)
                caselleEsplorate.append(valoreCasella)
                arrivato = True
                break
            k = 0
            while k < len(vetnemici):
                if nx == vetnemici[k] and ny == vetnemici[k + 1]:
                    nx = caselleEsplorate[j]
                    ny = caselleEsplorate[j + 1]
                k += 2
            if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                giaVisitata = False
                k = 0
                while k < len(caselleEsplorate):
                    if caselleEsplorate[k] == nx and caselleEsplorate[k + 1] == ny:
                        giaVisitata = True
                        break
                    k += 3
                if not giaVisitata:
                    caselleEsplorate.append(nx)
                    caselleEsplorate.append(ny)
                    caselleEsplorate.append(valoreCasella)
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], -gpx, 0, numstanza, False, True, False, porte, cofanetti)
            if nx == xArrivo and ny == yArrivo:
                caselleEsplorate.append(nx)
                caselleEsplorate.append(ny)
                caselleEsplorate.append(valoreCasella)
                arrivato = True
                break
            k = 0
            while k < len(vetnemici):
                if nx == vetnemici[k] and ny == vetnemici[k + 1]:
                    nx = caselleEsplorate[j]
                    ny = caselleEsplorate[j + 1]
                k += 2
            if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                giaVisitata = False
                k = 0
                while k < len(caselleEsplorate):
                    if caselleEsplorate[k] == nx and caselleEsplorate[k + 1] == ny:
                        giaVisitata = True
                        break
                    k += 3
                if not giaVisitata:
                    caselleEsplorate.append(nx)
                    caselleEsplorate.append(ny)
                    caselleEsplorate.append(valoreCasella)
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], gpx, 0, numstanza, False, True, False, porte, cofanetti)
            if nx == xArrivo and ny == yArrivo:
                caselleEsplorate.append(nx)
                caselleEsplorate.append(ny)
                caselleEsplorate.append(valoreCasella)
                arrivato = True
                break
            k = 0
            while k < len(vetnemici):
                if nx == vetnemici[k] and ny == vetnemici[k + 1]:
                    nx = caselleEsplorate[j]
                    ny = caselleEsplorate[j + 1]
                k += 2
            if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                giaVisitata = False
                k = 0
                while k < len(caselleEsplorate):
                    if caselleEsplorate[k] == nx and caselleEsplorate[k + 1] == ny:
                        giaVisitata = True
                        break
                    k += 3
                if not giaVisitata:
                    caselleEsplorate.append(nx)
                    caselleEsplorate.append(ny)
                    caselleEsplorate.append(valoreCasella)
            j += 3

        if arrivato:
            # percorsoTrovato contiene x e y per ogni casella del percorso da restituire
            percorsoTrovato = []
            finito = False
            j = len(caselleEsplorate) - 3
            while not finito and not impossibileRaggiungere:
                valoreCasella1 = -1
                valoreCasella2 = -1
                valoreCasella3 = -1
                valoreCasella4 = -1
                xCasella1 = 0
                yCasella1 = 0
                xCasella2 = 0
                yCasella2 = 0
                xCasella3 = 0
                yCasella3 = 0
                xCasella4 = 0
                yCasella4 = 0
                nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -gpy, numstanza, False, True, False, porte, cofanetti)
                k = 0
                while k < len(vetnemici):
                    if nx == vetnemici[k] and ny == vetnemici[k + 1]:
                        nx = caselleEsplorate[j]
                        ny = caselleEsplorate[j + 1]
                    k += 2
                if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                    i = 0
                    while i < len(caselleEsplorate):
                        if caselleEsplorate[i] == nx and caselleEsplorate[i + 1] == ny:
                            valoreCasella1 = caselleEsplorate[i + 2]
                            xCasella1 = nx
                            yCasella1 = ny
                            break
                        i += 3
                nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, gpy, numstanza, False, True, False, porte, cofanetti)
                k = 0
                while k < len(vetnemici):
                    if nx == vetnemici[k] and ny == vetnemici[k + 1]:
                        nx = caselleEsplorate[j]
                        ny = caselleEsplorate[j + 1]
                    k += 2
                if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                    i = 0
                    while i < len(caselleEsplorate):
                        if caselleEsplorate[i] == nx and caselleEsplorate[i + 1] == ny:
                            valoreCasella2 = caselleEsplorate[i + 2]
                            xCasella2 = nx
                            yCasella2 = ny
                            break
                        i += 3
                nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], -gpx, 0, numstanza, False, True, False, porte, cofanetti)
                k = 0
                while k < len(vetnemici):
                    if nx == vetnemici[k] and ny == vetnemici[k + 1]:
                        nx = caselleEsplorate[j]
                        ny = caselleEsplorate[j + 1]
                    k += 2
                if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                    i = 0
                    while i < len(caselleEsplorate):
                        if caselleEsplorate[i] == nx and caselleEsplorate[i + 1] == ny:
                            valoreCasella3 = caselleEsplorate[i + 2]
                            xCasella3 = nx
                            yCasella3 = ny
                            break
                        i += 3
                nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], gpx, 0, numstanza, False, True, False, porte, cofanetti)
                k = 0
                while k < len(vetnemici):
                    if nx == vetnemici[k] and ny == vetnemici[k + 1]:
                        nx = caselleEsplorate[j]
                        ny = caselleEsplorate[j + 1]
                    k += 2
                if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                    i = 0
                    while i < len(caselleEsplorate):
                        if caselleEsplorate[i] == nx and caselleEsplorate[i + 1] == ny:
                            valoreCasella4 = caselleEsplorate[i + 2]
                            xCasella4 = nx
                            yCasella4 = ny
                            break
                        i += 3

                if valoreCasella1 == -1 and valoreCasella2 == -1 and valoreCasella3 == -1 and valoreCasella4 == -1:
                    impossibileRaggiungere = True
                else:
                    if valoreCasella1 != -1:
                        valorePiuBasso = valoreCasella1
                        xProssimaCasella = xCasella1
                        yProssimaCasella = yCasella1
                    elif valoreCasella2 != -1:
                        valorePiuBasso = valoreCasella2
                        xProssimaCasella = xCasella2
                        yProssimaCasella = yCasella2
                    elif valoreCasella3 != -1:
                        valorePiuBasso = valoreCasella3
                        xProssimaCasella = xCasella3
                        yProssimaCasella = yCasella3
                    elif valoreCasella4 != -1:
                        valorePiuBasso = valoreCasella4
                        xProssimaCasella = xCasella4
                        yProssimaCasella = yCasella4
                    if valoreCasella2 != -1 and valoreCasella2 < valorePiuBasso:
                        valorePiuBasso = valoreCasella2
                        xProssimaCasella = xCasella2
                        yProssimaCasella = yCasella2
                    elif valoreCasella2 == valorePiuBasso and random.randint(1, 2) == 1:
                        xProssimaCasella = xCasella2
                        yProssimaCasella = yCasella2
                    if valoreCasella3 != -1 and valoreCasella3 < valorePiuBasso:
                        valorePiuBasso = valoreCasella3
                        xProssimaCasella = xCasella3
                        yProssimaCasella = yCasella3
                    elif valoreCasella3 == valorePiuBasso and random.randint(1, 2) == 1:
                        xProssimaCasella = xCasella3
                        yProssimaCasella = yCasella3
                    if valoreCasella4 != -1 and valoreCasella4 < valorePiuBasso:
                        valorePiuBasso = valoreCasella4
                        xProssimaCasella = xCasella4
                        yProssimaCasella = yCasella4
                    elif valoreCasella4 == valorePiuBasso and random.randint(1, 2) == 1:
                        xProssimaCasella = xCasella4
                        yProssimaCasella = yCasella4
                    percorsoTrovato.append(xProssimaCasella)
                    percorsoTrovato.append(yProssimaCasella)
                i = 0
                while i < len(caselleEsplorate):
                    if caselleEsplorate[i] == xProssimaCasella and caselleEsplorate[i + 1] == yProssimaCasella:
                        j = i
                        break
                    i += 3
                if xProssimaCasella == xPartenza and yProssimaCasella == yPartenza:
                    finito = True
        else:
            impossibileRaggiungere = True

    if impossibileRaggiungere:
        return False
    else:
        return percorsoTrovato


def controllaMorteRallo(vitaRallo, inizio):
    if vitaRallo <= 0:
        canaleSoundCanzone.stop()
        canaleSoundPuntatore.stop()
        canaleSoundPassiRallo.stop()
        canaleSoundPassiColco.stop()
        canaleSoundPassiNemico.stop()
        canaleSoundLvUp.stop()
        canaleSoundInterazioni.stop()
        canaleSoundAttacco.stop()
        schermo.fill(grigioscu)
        messaggio("Sei morto", grigiochi, gsx // 32 * 3, gsy // 18 * 13, 150)
        pygame.display.update()
        continua = False
        while not continua:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    canaleSoundPuntatore.play(selind)
                    continua = True
        inizio = True
    return inizio


def controllaMorteColco(dati, mosseRimasteRob):
    if dati[10] <= 0:
        morterob = True
        mosseRimasteRob = 0
        dati[122] = 0
        dati[125] = 0
        dati[126] = 0
    else:
        morterob = False
    return morterob, dati, mosseRimasteRob


def disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti, inMovimento=False, frame=False, attaccoRavvicinato=False, attaccoDaLontano=False):
    # personaggio: 1=d, 2=a, 3=w, 4=s
    if attaccoDaLontano:
        if npers == 1:
            schermo.blit(pers, (x, y))
            if avvele:
                schermo.blit(persAvvele, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(collana, (x, y))
            schermo.blit(faretra, (x, y))
            schermo.blit(persdmbAttacco, (x, y))
            schermo.blit(arco, (x, y))
            schermo.blit(guanti, (x, y))
        if npers == 2:
            schermo.blit(pers, (x, y))
            if avvele:
                schermo.blit(persAvvele, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(collana, (x, y))
            schermo.blit(faretra, (x, y))
            schermo.blit(persambAttacco, (x, y))
            schermo.blit(arco, (x - gpx, y))
            schermo.blit(guanti, (x, y))
        if npers == 3:
            schermo.blit(arco, (x, y - gpy))
            schermo.blit(perswmbAttacco, (x, y))
            schermo.blit(guanti, (x, y))
            schermo.blit(pers, (x, y))
            if avvele:
                schermo.blit(persAvvele, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(collana, (x, y))
            schermo.blit(faretra, (x, y))
        if npers == 4:
            schermo.blit(faretra, (x, y))
            schermo.blit(pers, (x, y))
            if avvele:
                schermo.blit(persAvvele, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(collana, (x, y))
            schermo.blit(perssmbAttacco, (x, y))
            schermo.blit(arco, (x, y))
            schermo.blit(guanti, (x, y))
    else:
        if npers == 1:
            schermo.blit(scudo, (x, y))
            if inMovimento:
                schermo.blit(persdm, (x, y))
            else:
                schermo.blit(pers, (x, y))
            if avvele:
                schermo.blit(persAvvele, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(collana, (x, y))
            schermo.blit(faretra, (x, y))
            schermo.blit(arco, (x, y))
            if attaccoRavvicinato:
                schermo.blit(persdmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    schermo.blit(persdmb1, (x, y))
                elif frame == 2:
                    schermo.blit(persdmb2, (x, y))
            else:
                schermo.blit(persdb, (x, y))
            schermo.blit(arma, (x, y))
            schermo.blit(guanti, (x, y))
        if npers == 2:
            if attaccoRavvicinato:
                schermo.blit(arma, (x - gpx, y))
            else:
                schermo.blit(arma, (x, y))
            if inMovimento:
                schermo.blit(persam, (x, y))
            else:
                schermo.blit(pers, (x, y))
            if avvele:
                schermo.blit(persAvvele, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(collana, (x, y))
            schermo.blit(faretra, (x, y))
            schermo.blit(arco, (x, y))
            if attaccoRavvicinato:
                schermo.blit(persambAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    schermo.blit(persamb1, (x, y))
                elif frame == 2:
                    schermo.blit(persamb2, (x, y))
            else:
                schermo.blit(persab, (x, y))
            schermo.blit(guanti, (x, y))
            schermo.blit(scudo, (x, y))
        if npers == 3:
            if attaccoRavvicinato:
                schermo.blit(arma, (x, y - gpy))
            else:
                schermo.blit(arma, (x, y))
            if attaccoRavvicinato:
                schermo.blit(perswmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    schermo.blit(perswmb1, (x, y))
                elif frame == 2:
                    schermo.blit(perswmb2, (x, y))
            else:
                schermo.blit(perswb, (x, y))
            schermo.blit(guanti, (x, y))
            schermo.blit(scudo, (x, y))
            if inMovimento:
                schermo.blit(perswm, (x, y))
            else:
                schermo.blit(pers, (x, y))
            if avvele:
                schermo.blit(persAvvele, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(collana, (x, y))
            schermo.blit(faretra, (x, y))
            schermo.blit(arco, (x, y))
        if npers == 4:
            schermo.blit(arco, (x, y))
            schermo.blit(faretra, (x, y))
            if inMovimento:
                schermo.blit(perssm, (x, y))
            else:
                schermo.blit(pers, (x, y))
            if avvele:
                schermo.blit(persAvvele, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(collana, (x, y))
            if attaccoRavvicinato:
                schermo.blit(perssmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    schermo.blit(perssmb1, (x, y))
                elif frame == 2:
                    schermo.blit(perssmb2, (x, y))
            else:
                schermo.blit(perssb, (x, y))
            schermo.blit(arma, (x, y))
            schermo.blit(guanti, (x, y))
            schermo.blit(scudo, (x, y))


def ottieniMonete(dati, moneteOttenute):
    moneteTot = dati[131] + moneteOttenute
    # effetto portafortuna
    if dati[130] == 4:
        moneteTot += moneteOttenute
    if moneteTot > 9999:
        moneteTot = 9999
    return moneteTot


def ottieniFrecce(dati, frecceOttenute):
    FrecceTot = dati[132] + frecceOttenute
    if dati[133] == 0:
        maxFrecce = 1
    elif dati[133] == 1:
        maxFrecce = 5
    elif dati[133] == 2:
        maxFrecce = 10
    elif dati[133] == 3:
        maxFrecce = 60
    else:
        maxFrecce = 0
    if FrecceTot > maxFrecce:
        FrecceTot = maxFrecce
    return FrecceTot


def ottieniOggetto(dati, numOggetto, qta):
    if dati[numOggetto] <= -1:
        dati[numOggetto] += 1
        dati[numOggetto] += qta
    elif dati[numOggetto] < 99:
        dati[numOggetto] += qta
    else:
        numOggetto = -2
    return dati, numOggetto


def ottieniCellaDiMemoria(dati, numCella):
    dati[numCella] += 1
    dati[numCella + 10] += 1
    return dati


def ottieniTecnica(dati, tecnica):
    if dati[tecnica] <= 0:
        dati[tecnica] = 1
    else:
        tecnica = -2
    return dati, tecnica


def ottieniArmaBatteria(dati, armaBatteria):
    if dati[armaBatteria] <= 0:
        dati[armaBatteria] = 1
    else:
        armaBatteria = -2
    return dati, armaBatteria


def ottieniCondizione(dati, condizione):
    if dati[condizione] <= 0:
        dati[condizione] = 1
    else:
        condizione = -2
    return dati, condizione


"""# rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
pygame.draw.rect(schermo, blu, (nx, ny, gpx, gpy))
pygame.display.update()"""
