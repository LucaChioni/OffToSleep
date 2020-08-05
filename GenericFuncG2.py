# -*- coding: utf-8 -*-

import os
import random
import GlobalVarG2
from FadeToBlackClass import *


def messaggio(msg, colore, x, y, gr):
    gr = gr - 10
    gr = GlobalVarG2.gpx * gr // 60
    y = y - (GlobalVarG2.gpy // 8)
    carattere = "Gentium Book Basic"
    font = pygame.font.SysFont(carattere, gr)
    testo = font.render(msg, True, colore)
    GlobalVarG2.schermo.blit(testo, (x, y))


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

    if dati[123] > 0:
        attVicino += attVicino // 4
        attLontano += attLontano // 4
    if dati[124] > 0:
        dif += dif // 4

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
    if GlobalVarG2.mouseBloccato:
        GlobalVarG2.configuraCursore(False)
    GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
    pygame.display.update()
    listaImg = []
    # load all the images
    for i in os.listdir(path):
        img = pygame.image.load(path + '/' + i).convert()
        img = pygame.transform.scale(img, (GlobalVarG2.gsx, GlobalVarG2.gsy))
        listaImg.append(img)
    if audio != 0:
        GlobalVarG2.canaleSoundCanzone.play(audio)
    # play video
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
    i = 0
    while i < len(listaImg) + 10:
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVarG2.mouseVisibile:
            pygame.mouse.set_visible(True)
            GlobalVarG2.mouseVisibile = True
        if i >= 10:
            GlobalVarG2.schermo.blit(listaImg[i - 10], (0, 0))
            pygame.display.update()
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
                if event.type == pygame.KEYDOWN or (event.type == pygame.MOUSEBUTTONDOWN and (sinistroMouse or centraleMouse or destroMouse) and not rotellaConCentralePremuto):
                    if event.type == pygame.KEYDOWN:
                        if GlobalVarG2.mouseVisibile:
                            pygame.mouse.set_visible(False)
                            GlobalVarG2.mouseVisibile = False
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                    if audio != 0:
                        GlobalVarG2.canaleSoundCanzone.stop()
                    return True
        pygame.event.pump()
        GlobalVarG2.clockVideo.tick(GlobalVarG2.fpsVideo)
        i += 1
    if audio != 0:
        GlobalVarG2.canaleSoundCanzone.stop()
    return False


def oggetto(x, y, dimx, dimy, px, py, nx, ny):
    a = x
    b = y
    dimx = dimx + x
    dimy = dimy + y
    while x < dimx:
        if (ny == -GlobalVarG2.gpy and py == dimy and px == x) or (ny == GlobalVarG2.gpy and py == y - GlobalVarG2.gpy and px == x):
            return True
        x = x + GlobalVarG2.gpx
    x = a
    y = b
    while y < dimy:
        if (nx == -GlobalVarG2.gpx and px == dimx and py == y) or (nx == GlobalVarG2.gpx and px == x - GlobalVarG2.gpx and py == y):
            return True
        y = y + GlobalVarG2.gpy


def muri_porte(x, y, nx, ny, stanza, carim, mostro, robo, porte, cofanetti):
    cambiosta = False

    if x < 0 or y < 0 or x >= GlobalVarG2.gsx or y >= GlobalVarG2.gsy:
        return x, y, stanza, carim, cambiosta

    # prima stanza
    if (stanza == 1) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if ny == -GlobalVarG2.gpy and x == GlobalVarG2.gsx // 32 * 6 and y == GlobalVarG2.gsy // 18 * 2 and not mostro and not robo:
            stanza = 2
            cambiosta = True
            carim = True
        elif ny == -GlobalVarG2.gpy and x == GlobalVarG2.gsx // 32 * 6 and y == GlobalVarG2.gsy // 18 * 1 and not mostro and not robo:
            ny = 0
        elif nx == GlobalVarG2.gpx and x == GlobalVarG2.gsx // 32 * 6 and y == GlobalVarG2.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
        elif nx == -GlobalVarG2.gpx and x == GlobalVarG2.gsx // 32 * 6 and y == GlobalVarG2.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
        else:
            # bordi stanza
            if nx == -GlobalVarG2.gpx and x <= GlobalVarG2.gpx * 2:
                nx = 0
            if nx == GlobalVarG2.gpx and x >= GlobalVarG2.gsx - (GlobalVarG2.gpx * 3):
                nx = 0
            if ny == -GlobalVarG2.gpy and y <= GlobalVarG2.gpy * 2:
                ny = 0
            if ny == GlobalVarG2.gpy and y >= GlobalVarG2.gsy - (GlobalVarG2.gpy * 3):
                ny = 0
        # controllo muri-oggetti
        #          posizione x    posizione y     dim x    dim y   px py  nx  ny
        if oggetto(GlobalVarG2.gsx // 32 * 7, GlobalVarG2.gsy // 18 * 11, GlobalVarG2.gpx * 1, GlobalVarG2.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 7, GlobalVarG2.gpx * 2, GlobalVarG2.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 21, GlobalVarG2.gsy // 18 * 11, GlobalVarG2.gpx * 4, GlobalVarG2.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        # controllo se le porte sono chiuse o aperte
        i = 0
        while i < len(porte):
            if not porte[i + 3]:
                if oggetto(porte[i + 1], porte[i + 2], GlobalVarG2.gpx * 1, GlobalVarG2.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
            i = i + 4
        # controllo cofanetti
        i = 0
        while i < len(cofanetti):
            if oggetto(cofanetti[i + 1], cofanetti[i + 2], GlobalVarG2.gpx * 1, GlobalVarG2.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            i = i + 4
    # seconda stanza
    if (stanza == 2) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if ny == -GlobalVarG2.gpy and x == GlobalVarG2.gsx // 32 * 6 and y == GlobalVarG2.gsy // 18 * 2 and not mostro and not robo:
            stanza = 1
            cambiosta = True
            carim = True
        elif ny == -GlobalVarG2.gpy and x == GlobalVarG2.gsx // 32 * 6 and y == GlobalVarG2.gsy // 18 * 1 and not mostro and not robo:
            ny = 0
        elif nx == GlobalVarG2.gpx and x == GlobalVarG2.gsx // 32 * 6 and y == GlobalVarG2.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
        elif nx == -GlobalVarG2.gpx and x == GlobalVarG2.gsx // 32 * 6 and y == GlobalVarG2.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
        else:
            # bordi stanza
            if nx == -GlobalVarG2.gpx and x <= GlobalVarG2.gpx * 2:
                nx = 0
            if nx == GlobalVarG2.gpx and x >= GlobalVarG2.gsx - (GlobalVarG2.gpx * 3):
                nx = 0
            if ny == -GlobalVarG2.gpy and y <= GlobalVarG2.gpy * 2:
                ny = 0
            if ny == GlobalVarG2.gpy and y >= GlobalVarG2.gsy - (GlobalVarG2.gpy * 3):
                ny = 0
        # controllo muri-oggetti
        #          posizione x    posizione y    dim x    dim y    px py nx  ny
        if oggetto(GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 2, GlobalVarG2.gpx * 1, GlobalVarG2.gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7, GlobalVarG2.gpx * 1, GlobalVarG2.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 7, GlobalVarG2.gpx * 12, GlobalVarG2.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11, GlobalVarG2.gpx * 6, GlobalVarG2.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 7, GlobalVarG2.gsy // 18 * 13, GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 13, GlobalVarG2.gpx * 1, GlobalVarG2.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 11, GlobalVarG2.gpx * 1, GlobalVarG2.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 13, GlobalVarG2.gsy // 18 * 11, GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 10, GlobalVarG2.gpx * 1, GlobalVarG2.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gpx * 1, GlobalVarG2.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 2, GlobalVarG2.gpx * 1, GlobalVarG2.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 6, GlobalVarG2.gpx * 9, GlobalVarG2.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gpx * 4, GlobalVarG2.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 6, GlobalVarG2.gpx * 1, GlobalVarG2.gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 13, GlobalVarG2.gpx * 1, GlobalVarG2.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 26, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gpx * 1, GlobalVarG2.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(GlobalVarG2.gsx // 32 * 26, GlobalVarG2.gsy // 18 * 6, GlobalVarG2.gpx * 4, GlobalVarG2.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        # controllo se le porte sono chiuse o aperte
        i = 0
        while i < len(porte):
            if not porte[i + 3]:
                if oggetto(porte[i + 1], porte[i + 2], GlobalVarG2.gpx * 1, GlobalVarG2.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
            i = i + 4
        # controllo cofanetti
        i = 0
        while i < len(cofanetti):
            if oggetto(cofanetti[i + 1], cofanetti[i + 2], GlobalVarG2.gpx * 1, GlobalVarG2.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            i = i + 4

    # movimento personaggio
    x = x + nx
    y = y + ny

    return x, y, stanza, carim, cambiosta


def trovacasattaccabili(x, y, stanza, porte, cofanetti, raggio):
    if raggio == -1:
        rangeXSinistra = (x // GlobalVarG2.gpx) - 2
        rangeXDestra = (GlobalVarG2.gsx // GlobalVarG2.gpx) - (x // GlobalVarG2.gpx) - 3
        rangeYAlto = (y // GlobalVarG2.gpy) - 2
        rangeYBasso = (GlobalVarG2.gsy // GlobalVarG2.gpy) - (y // GlobalVarG2.gpy) - 3
    else:
        rangeXSinistra = raggio // GlobalVarG2.gpx
        if (x // GlobalVarG2.gpx) - rangeXSinistra < 2:
            rangeXSinistra = (x // GlobalVarG2.gpx) - 2
        rangeXDestra = raggio // GlobalVarG2.gpx
        if (x // GlobalVarG2.gpx) + rangeXDestra > 30:
            rangeXDestra = (GlobalVarG2.gsx // GlobalVarG2.gpx) - (x // GlobalVarG2.gpx) - 3
        rangeYAlto = raggio // GlobalVarG2.gpy
        if (y // GlobalVarG2.gpy) - rangeYAlto < 2:
            rangeYAlto = (y // GlobalVarG2.gpy) - 2
        rangeYBasso = raggio // GlobalVarG2.gpy
        if (y // GlobalVarG2.gpy) + rangeYBasso > 16:
            rangeYBasso = (GlobalVarG2.gsy // GlobalVarG2.gpy) - (y // GlobalVarG2.gpy) - 3

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
            murx = x + (GlobalVarG2.gpx * n)
            mury = y + (GlobalVarG2.gpy * m)
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, GlobalVarG2.gpx, 0, stanza, False, True, False, porte, cofanetti)
            if murx != nmurx:
                caseattac.append(nmurx)
                caseattac.append(nmury)
                caseattac.append(True)
            else:
                caseattac.append(nmurx + GlobalVarG2.gpx)
                caseattac.append(nmury)
                caseattac.append(False)
            m = m + 1
        n = n + 1
    n = 0
    while n < rangeYBasso:
        m = 1
        while m <= rangeXDestra:
            murx = x + (GlobalVarG2.gpx * m)
            mury = y + (GlobalVarG2.gpy * n)
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, 0, GlobalVarG2.gpy, stanza, False, True, False, porte, cofanetti)
            if mury == nmury:
                i = 0
                while i < len(caseattac):
                    if caseattac[i] == nmurx and caseattac[i + 1] == nmury + GlobalVarG2.gpy:
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
            caseattacbassodestra.append(x + (GlobalVarG2.gpx * n))
            caseattacbassodestra.append(y + (GlobalVarG2.gpy * m))
            caseattacbassodestra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacbassodestra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVarG2.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVarG2.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVarG2.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVarG2.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVarG2.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVarG2.gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacbassodestra):
                if caseattacbassodestra[j] == caseattac[i] and caseattacbassodestra[j + 1] == caseattac[i + 1]:
                    caseattacbassodestra[j + 2] = False
                elif caseattacbassodestra[j + 2]:
                    xLatoSinistroCasella = caseattacbassodestra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacbassodestra[j] + GlobalVarG2.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacbassodestra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacbassodestra[j + 1] + GlobalVarG2.gpy
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
                                latoSinistro = GlobalVarG2.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalVarG2.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalVarG2.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalVarG2.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoDestro != 0:
                                area = (GlobalVarG2.gpx * GlobalVarG2.gpy) - ((GlobalVarG2.gpx - latoSuperiore) * (GlobalVarG2.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalVarG2.gpx * GlobalVarG2.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalVarG2.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalVarG2.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalVarG2.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalVarG2.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoSinistro != 0:
                                area = (GlobalVarG2.gpx * GlobalVarG2.gpy) - ((GlobalVarG2.gpx - latoInferiore) * (GlobalVarG2.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalVarG2.gpx * GlobalVarG2.gpy / 2.0) + margineDiErrore:
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
            murx = x - (GlobalVarG2.gpx * n)
            mury = y + (GlobalVarG2.gpy * m)
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, -GlobalVarG2.gpx, 0, stanza, False, True, False, porte, cofanetti)
            if murx != nmurx:
                caseattac.append(nmurx)
                caseattac.append(nmury)
                caseattac.append(True)
            else:
                caseattac.append(nmurx - GlobalVarG2.gpx)
                caseattac.append(nmury)
                caseattac.append(False)
            m = m + 1
        n = n + 1
    n = 0
    while n < rangeYBasso:
        m = 1
        while m <= rangeXSinistra:
            murx = x - (GlobalVarG2.gpx * m)
            mury = y + (GlobalVarG2.gpy * n)
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, 0, GlobalVarG2.gpy, stanza, False, True, False, porte, cofanetti)
            if mury == nmury:
                i = 0
                while i < len(caseattac):
                    if caseattac[i] == nmurx and caseattac[i + 1] == nmury + GlobalVarG2.gpy:
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
            caseattacbassosinistra.append(x - (GlobalVarG2.gpx * n))
            caseattacbassosinistra.append(y + (GlobalVarG2.gpy * m))
            caseattacbassosinistra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacbassosinistra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVarG2.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVarG2.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = - deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVarG2.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVarG2.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVarG2.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVarG2.gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = - deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacbassosinistra):
                if caseattacbassosinistra[j] == caseattac[i] and caseattacbassosinistra[j + 1] == caseattac[i + 1]:
                    caseattacbassosinistra[j + 2] = False
                elif caseattacbassosinistra[j + 2]:
                    xLatoSinistroCasella = caseattacbassosinistra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacbassosinistra[j] + GlobalVarG2.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacbassosinistra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacbassosinistra[j + 1] + GlobalVarG2.gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacbassosinistra[j + 2] and yLatoSuperioreCasella >= caseattac[i + 1] and xLatoDestroCasella <= caseattac[i] + GlobalVarG2.gpx:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = GlobalVarG2.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalVarG2.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalVarG2.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalVarG2.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoSinistro != 0:
                                area = (GlobalVarG2.gpx * GlobalVarG2.gpy) - ((GlobalVarG2.gpx - latoSuperiore) * (GlobalVarG2.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalVarG2.gpx * GlobalVarG2.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalVarG2.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalVarG2.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalVarG2.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalVarG2.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoDestro != 0:
                                area = (GlobalVarG2.gpx * GlobalVarG2.gpy) - ((GlobalVarG2.gpx - latoInferiore) * (GlobalVarG2.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalVarG2.gpx * GlobalVarG2.gpy / 2.0) + margineDiErrore:
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
            murx = x - (GlobalVarG2.gpx * n)
            mury = y - (GlobalVarG2.gpy * m)
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, -GlobalVarG2.gpx, 0, stanza, False, True, False, porte, cofanetti)
            if murx != nmurx:
                caseattac.append(nmurx)
                caseattac.append(nmury)
                caseattac.append(True)
            else:
                caseattac.append(nmurx - GlobalVarG2.gpx)
                caseattac.append(nmury)
                caseattac.append(False)
            m = m + 1
        n = n + 1
    n = 0
    while n < rangeYAlto:
        m = 1
        while m <= rangeXSinistra:
            murx = x - (GlobalVarG2.gpx * m)
            mury = y - (GlobalVarG2.gpy * n)
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, 0, -GlobalVarG2.gpy, stanza, False, True, False, porte, cofanetti)
            if mury == nmury:
                i = 0
                while i < len(caseattac):
                    if caseattac[i] == nmurx and caseattac[i + 1] == nmury - GlobalVarG2.gpy:
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
            caseattacaltosinistra.append(x - (GlobalVarG2.gpx * n))
            caseattacaltosinistra.append(y - (GlobalVarG2.gpy * m))
            caseattacaltosinistra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacaltosinistra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVarG2.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVarG2.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVarG2.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVarG2.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVarG2.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVarG2.gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacaltosinistra):
                if caseattacaltosinistra[j] == caseattac[i] and caseattacaltosinistra[j + 1] == caseattac[i + 1]:
                    caseattacaltosinistra[j + 2] = False
                elif caseattacaltosinistra[j + 2]:
                    xLatoSinistroCasella = caseattacaltosinistra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacaltosinistra[j] + GlobalVarG2.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacaltosinistra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacaltosinistra[j + 1] + GlobalVarG2.gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacaltosinistra[j + 2] and yLatoInferioreCasella <= caseattac[i + 1] + GlobalVarG2.gpy and xLatoDestroCasella <= caseattac[i] + GlobalVarG2.gpx:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = GlobalVarG2.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalVarG2.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalVarG2.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalVarG2.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoDestro != 0:
                                area = (GlobalVarG2.gpx * GlobalVarG2.gpy) - ((GlobalVarG2.gpx - latoSuperiore) * (GlobalVarG2.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalVarG2.gpx * GlobalVarG2.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalVarG2.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalVarG2.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalVarG2.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalVarG2.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoSinistro != 0:
                                area = (GlobalVarG2.gpx * GlobalVarG2.gpy) - ((GlobalVarG2.gpx - latoInferiore) * (GlobalVarG2.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalVarG2.gpx * GlobalVarG2.gpy / 2.0) + margineDiErrore:
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
            murx = x + (GlobalVarG2.gpx * n)
            mury = y - (GlobalVarG2.gpy * m)
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, GlobalVarG2.gpx, 0, stanza, False, True, False, porte, cofanetti)
            if murx != nmurx:
                caseattac.append(nmurx)
                caseattac.append(nmury)
                caseattac.append(True)
            else:
                caseattac.append(nmurx + GlobalVarG2.gpx)
                caseattac.append(nmury)
                caseattac.append(False)
            m = m + 1
        n = n + 1
    n = 0
    while n < rangeYAlto:
        m = 1
        while m <= rangeXDestra:
            murx = x + (GlobalVarG2.gpx * m)
            mury = y - (GlobalVarG2.gpy * n)
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, 0, -GlobalVarG2.gpy, stanza, False, True, False, porte, cofanetti)
            if mury == nmury:
                i = 0
                while i < len(caseattac):
                    if caseattac[i] == nmurx and caseattac[i + 1] == nmury - GlobalVarG2.gpy:
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
            caseattacaltodestra.append(x + (GlobalVarG2.gpx * n))
            caseattacaltodestra.append(y - (GlobalVarG2.gpy * m))
            caseattacaltodestra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacaltodestra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVarG2.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVarG2.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = - deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVarG2.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVarG2.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVarG2.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVarG2.gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = - deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacaltodestra):
                if caseattacaltodestra[j] == caseattac[i] and caseattacaltodestra[j + 1] == caseattac[i + 1]:
                    caseattacaltodestra[j + 2] = False
                elif caseattacaltodestra[j + 2]:
                    xLatoSinistroCasella = caseattacaltodestra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacaltodestra[j] + GlobalVarG2.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacaltodestra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacaltodestra[j + 1] + GlobalVarG2.gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacaltodestra[j + 2] and yLatoInferioreCasella <= caseattac[i + 1] + GlobalVarG2.gpy and xLatoSinistroCasella >= caseattac[i]:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = GlobalVarG2.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalVarG2.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalVarG2.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalVarG2.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoSinistro != 0:
                                area = (GlobalVarG2.gpx * GlobalVarG2.gpy) - ((GlobalVarG2.gpx - latoSuperiore) * (GlobalVarG2.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalVarG2.gpx * GlobalVarG2.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalVarG2.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalVarG2.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalVarG2.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalVarG2.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoDestro != 0:
                                area = (GlobalVarG2.gpx * GlobalVarG2.gpy) - ((GlobalVarG2.gpx - latoInferiore) * (GlobalVarG2.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalVarG2.gpx * GlobalVarG2.gpy / 2.0) + margineDiErrore:
                                caseattacaltodestra[j + 2] = False
                        elif (yLatoSuperioreCasella > yRetta1LatoSinistroCasella and xLatoSinistroCasella > xRetta1LatoSuperioreCasella) and (yLatoInferioreCasella < yRetta2LatoDestroCasella and xLatoDestroCasella < xRetta2LatoInferioreCasella):
                            caseattacaltodestra[j + 2] = False

                j += 3
        i += 3

    # caselle a destra del personaggio
    caseattac = []
    n = 0
    while n <= rangeXDestra:
        murx = x + (GlobalVarG2.gpx * n)
        mury = y
        nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, GlobalVarG2.gpx, 0, stanza, False, True, False, porte, cofanetti)
        if murx != nmurx:
            caseattac.append(nmurx)
            caseattac.append(nmury)
            caseattac.append(True)
        else:
            caseattac.append(nmurx + GlobalVarG2.gpx)
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
            caseattacdestra.append(x + (GlobalVarG2.gpx * n))
            caseattacdestra.append(y - (GlobalVarG2.gpy * m))
            caseattacdestra.append(True)
            m = m + 1
        m = 1
        while m <= rangeYBasso:
            caseattacdestra.append(x + (GlobalVarG2.gpx * n))
            caseattacdestra.append(y + (GlobalVarG2.gpy * m))
            caseattacdestra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacdestra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVarG2.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVarG2.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = - deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVarG2.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVarG2.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVarG2.gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacdestra):
                if caseattacdestra[j] == caseattac[i] and caseattacdestra[j + 1] == caseattac[i + 1]:
                    caseattacdestra[j + 2] = False
                elif caseattacdestra[j + 2]:
                    xLatoSinistroCasella = caseattacdestra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacdestra[j] + GlobalVarG2.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacdestra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacdestra[j + 1] + GlobalVarG2.gpy
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
                                latoSinistro = GlobalVarG2.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalVarG2.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalVarG2.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalVarG2.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoSinistro != 0:
                                area = (GlobalVarG2.gpx * GlobalVarG2.gpy) - ((GlobalVarG2.gpx - latoSuperiore) * (GlobalVarG2.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalVarG2.gpx * GlobalVarG2.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalVarG2.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalVarG2.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalVarG2.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalVarG2.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoSinistro != 0:
                                area = (GlobalVarG2.gpx * GlobalVarG2.gpy) - ((GlobalVarG2.gpx - latoInferiore) * (GlobalVarG2.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalVarG2.gpx * GlobalVarG2.gpy / 2.0) + margineDiErrore:
                                caseattacdestra[j + 2] = False
                        elif (yLatoSuperioreCasella > yRetta1LatoSinistroCasella and xLatoSinistroCasella > xRetta1LatoSuperioreCasella) and (yLatoInferioreCasella < yRetta2LatoSinistroCasella and xLatoSinistroCasella > xRetta2LatoInferioreCasella):
                            caseattacdestra[j + 2] = False

                j += 3
        i += 3

    # caselle a sinistra del personaggio
    caseattac = []
    n = 0
    while n <= rangeXSinistra:
        murx = x - (GlobalVarG2.gpx * n)
        mury = y
        nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, -GlobalVarG2.gpx, 0, stanza, False, True, False, porte, cofanetti)
        if murx != nmurx:
            caseattac.append(nmurx)
            caseattac.append(nmury)
            caseattac.append(True)
        else:
            caseattac.append(nmurx - GlobalVarG2.gpx)
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
            caseattacsinistra.append(x - (GlobalVarG2.gpx * n))
            caseattacsinistra.append(y - (GlobalVarG2.gpy * m))
            caseattacsinistra.append(True)
            m = m + 1
        m = 1
        while m <= rangeYBasso:
            caseattacsinistra.append(x - (GlobalVarG2.gpx * n))
            caseattacsinistra.append(y + (GlobalVarG2.gpy * m))
            caseattacsinistra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacsinistra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVarG2.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVarG2.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVarG2.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVarG2.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVarG2.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVarG2.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVarG2.gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = - deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacsinistra):
                if caseattacsinistra[j] == caseattac[i] and caseattacsinistra[j + 1] == caseattac[i + 1]:
                    caseattacsinistra[j + 2] = False
                elif caseattacsinistra[j + 2]:
                    xLatoSinistroCasella = caseattacsinistra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacsinistra[j] + GlobalVarG2.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacsinistra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacsinistra[j + 1] + GlobalVarG2.gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacsinistra[j + 2] and xLatoDestroCasella <= caseattac[i] + GlobalVarG2.gpx:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = GlobalVarG2.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalVarG2.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalVarG2.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalVarG2.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoDestro != 0:
                                area = (GlobalVarG2.gpx * GlobalVarG2.gpy) - ((GlobalVarG2.gpx - latoSuperiore) * (GlobalVarG2.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalVarG2.gpx * GlobalVarG2.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalVarG2.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalVarG2.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalVarG2.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalVarG2.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoDestro != 0:
                                area = (GlobalVarG2.gpx * GlobalVarG2.gpy) - ((GlobalVarG2.gpx - latoInferiore) * (GlobalVarG2.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalVarG2.gpx * GlobalVarG2.gpy / 2.0) + margineDiErrore:
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
        mury = y - (GlobalVarG2.gpy * n)
        nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, 0, -GlobalVarG2.gpy, stanza, False, True, False, porte, cofanetti)
        if mury != nmury:
            caseattac.append(nmurx)
            caseattac.append(nmury)
            caseattac.append(True)
        else:
            caseattac.append(nmurx)
            caseattac.append(nmury - GlobalVarG2.gpy)
            caseattac.append(False)
        n += 1
    # caseattacalto[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli sopra
    caseattacalto = []
    # riempio caseattacalto come se tutto il campo sopra fosse libero
    n = 0
    while n <= rangeYAlto:
        m = 0
        while m <= rangeXDestra:
            caseattacalto.append(x + (GlobalVarG2.gpx * m))
            caseattacalto.append(y - (GlobalVarG2.gpy * n))
            caseattacalto.append(True)
            m = m + 1
        m = 1
        while m <= rangeXSinistra:
            caseattacalto.append(x - (GlobalVarG2.gpx * m))
            caseattacalto.append(y - (GlobalVarG2.gpy * n))
            caseattacalto.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacalto[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVarG2.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVarG2.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVarG2.gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVarG2.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVarG2.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVarG2.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVarG2.gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = - deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacalto):
                if caseattacalto[j] == caseattac[i] and caseattacalto[j + 1] == caseattac[i + 1]:
                    caseattacalto[j + 2] = False
                elif caseattacalto[j + 2]:
                    xLatoSinistroCasella = caseattacalto[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacalto[j] + GlobalVarG2.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacalto[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacalto[j + 1] + GlobalVarG2.gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacalto[j + 2] and yLatoInferioreCasella <= caseattac[i + 1] + GlobalVarG2.gpy:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta2
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoSuperioreCasella)
                            elif yRetta1LatoSinistroCasella > yLatoInferioreCasella:
                                latoSinistro = GlobalVarG2.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta1LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalVarG2.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalVarG2.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalVarG2.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoSinistro != 0:
                                area = (GlobalVarG2.gpx * GlobalVarG2.gpy) - ((GlobalVarG2.gpx - latoInferiore) * (GlobalVarG2.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalVarG2.gpx * GlobalVarG2.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalVarG2.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalVarG2.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalVarG2.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalVarG2.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoDestro != 0:
                                area = (GlobalVarG2.gpx * GlobalVarG2.gpy) - ((GlobalVarG2.gpx - latoInferiore) * (GlobalVarG2.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalVarG2.gpx * GlobalVarG2.gpy / 2.0) + margineDiErrore:
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
        mury = y + (GlobalVarG2.gpy * n)
        nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, 0, GlobalVarG2.gpy, stanza, False, True, False, porte, cofanetti)
        if mury != nmury:
            caseattac.append(nmurx)
            caseattac.append(nmury)
            caseattac.append(True)
        else:
            caseattac.append(nmurx)
            caseattac.append(nmury + GlobalVarG2.gpy)
            caseattac.append(False)
        n += 1
    # caseattacbasso[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli a destra
    caseattacbasso = []
    # riempio caseattacbasso come se tutto il campo a destra fosse libero
    n = 0
    while n <= rangeYBasso:
        m = 0
        while m <= rangeXDestra:
            caseattacbasso.append(x + (GlobalVarG2.gpx * m))
            caseattacbasso.append(y + (GlobalVarG2.gpy * n))
            caseattacbasso.append(True)
            m = m + 1
        m = 1
        while m <= rangeXSinistra:
            caseattacbasso.append(x - (GlobalVarG2.gpx * m))
            caseattacbasso.append(y + (GlobalVarG2.gpy * n))
            caseattacbasso.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacbasso[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVarG2.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVarG2.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = - deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in alto a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVarG2.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVarG2.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVarG2.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacbasso):
                if caseattacbasso[j] == caseattac[i] and caseattacbasso[j + 1] == caseattac[i + 1]:
                    caseattacbasso[j + 2] = False
                elif caseattacbasso[j + 2]:
                    xLatoSinistroCasella = caseattacbasso[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacbasso[j] + GlobalVarG2.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacbasso[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacbasso[j + 1] + GlobalVarG2.gpy
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
                                latoSinistro = GlobalVarG2.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalVarG2.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalVarG2.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalVarG2.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoSinistro != 0:
                                area = (GlobalVarG2.gpx * GlobalVarG2.gpy) - ((GlobalVarG2.gpx - latoSuperiore) * (GlobalVarG2.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalVarG2.gpx * GlobalVarG2.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalVarG2.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta2LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalVarG2.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalVarG2.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalVarG2.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoDestro != 0:
                                area = (GlobalVarG2.gpx * GlobalVarG2.gpy) - ((GlobalVarG2.gpx - latoSuperiore) * (GlobalVarG2.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalVarG2.gpx * GlobalVarG2.gpy / 2.0) + margineDiErrore:
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
        if cx == GlobalVarG2.gpx * 3 and cy == GlobalVarG2.gpy * 7:
            tesoro = 31
        if cx == GlobalVarG2.gpx * 7 and cy == GlobalVarG2.gpy * 12:
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
        if cx == GlobalVarG2.gpx * 12 and cy == GlobalVarG2.gpy * 11:
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
        if cx == GlobalVarG2.gpx * 3 and cy == GlobalVarG2.gpy * 5:
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
        if cx == GlobalVarG2.gpx * 5 and cy == GlobalVarG2.gpy * 10:
            tesoro = 11
        if cx == GlobalVarG2.gpx * 10 and cy == GlobalVarG2.gpy * 9:
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


def scopriCaselleViste(x, y, rx, ry, numstanza, porte, cofanetti, caseviste, escludiPorte=True):
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
        nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -GlobalVarG2.gpy, numstanza, False, escludiPorte, False, porte, cofanetti)
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
        nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, GlobalVarG2.gpy, numstanza, False, escludiPorte, False, porte, cofanetti)
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
        nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], -GlobalVarG2.gpx, 0, numstanza, False, escludiPorte, False, porte, cofanetti)
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
        nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], GlobalVarG2.gpx, 0, numstanza, False, escludiPorte, False, porte, cofanetti)
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
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -GlobalVarG2.gpy, numstanza, False, escludiPorte, False, porte, cofanetti)
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
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, GlobalVarG2.gpy, numstanza, False, escludiPorte, False, porte, cofanetti)
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
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], -GlobalVarG2.gpx, 0, numstanza, False, escludiPorte, False, porte, cofanetti)
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
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], GlobalVarG2.gpx, 0, numstanza, False, escludiPorte, False, porte, cofanetti)
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


def pathFinding(xPartenza, yPartenza, xArrivo, yArrivo, numstanza, porte, cofanetti, vetnemici, escludiPorte=True):
    # caselleEsplorate contiene x, y e valore delle caselle già esplorate (il valore serve per trovare il percorso più breve)
    valoreCasella = 0
    caselleEsplorate = [xPartenza, yPartenza, valoreCasella]

    valorePiuBasso = 0
    xProssimaCasella = 0
    yProssimaCasella = 0
    percorsoTrovato = []

    impossibileRaggiungere = False
    if (xPartenza == xArrivo and yPartenza == yArrivo + GlobalVarG2.gpy) or (xPartenza == xArrivo and yPartenza == yArrivo - GlobalVarG2.gpy) or (xPartenza == xArrivo + GlobalVarG2.gpx and yPartenza == yArrivo) or (xPartenza == xArrivo and yPartenza - GlobalVarG2.gpx == yArrivo):
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
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -GlobalVarG2.gpy, numstanza, False, escludiPorte, False, porte, cofanetti)
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
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, GlobalVarG2.gpy, numstanza, False, escludiPorte, False, porte, cofanetti)
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
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], -GlobalVarG2.gpx, 0, numstanza, False, escludiPorte, False, porte, cofanetti)
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
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], GlobalVarG2.gpx, 0, numstanza, False, escludiPorte, False, porte, cofanetti)
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
                nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -GlobalVarG2.gpy, numstanza, False, escludiPorte, False, porte, cofanetti)
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
                nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, GlobalVarG2.gpy, numstanza, False, escludiPorte, False, porte, cofanetti)
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
                nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], -GlobalVarG2.gpx, 0, numstanza, False, escludiPorte, False, porte, cofanetti)
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
                nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], GlobalVarG2.gpx, 0, numstanza, False, escludiPorte, False, porte, cofanetti)
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
        if GlobalVarG2.mouseBloccato:
            GlobalVarG2.configuraCursore(False)
        GlobalVarG2.canaleSoundCanzone.stop()
        GlobalVarG2.canaleSoundPuntatore.stop()
        GlobalVarG2.canaleSoundPassiRallo.stop()
        GlobalVarG2.canaleSoundPassiColco.stop()
        GlobalVarG2.canaleSoundPassiNemico.stop()
        GlobalVarG2.canaleSoundLvUp.stop()
        # GlobalVarG2.canaleSoundInterazioni.stop()
        # GlobalVarG2.canaleSoundAttacco.stop()
        pygame.time.wait(500)
        GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.rumoreMorte)
        sprites = pygame.sprite.Group(Fade(3))
        schermoFadeToBlack = GlobalVarG2.schermo.copy()
        i = 1
        while i <= 46:
            sprites.update()
            GlobalVarG2.schermo.blit(schermoFadeToBlack, (0, 0))
            sprites.draw(GlobalVarG2.schermo)
            pygame.display.update()
            GlobalVarG2.clockFadeToBlack.tick(GlobalVarG2.fpsFadeToBlack)
            i += 1

        # GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
        messaggio("Sei morto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 3, GlobalVarG2.gsy // 18 * 13, 150)
        pygame.display.update()
        continua = False
        sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
        while not continua:
            deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
            if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVarG2.mouseVisibile:
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True
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
                if event.type == pygame.KEYDOWN or (event.type == pygame.MOUSEBUTTONDOWN and (sinistroMouse or centraleMouse or destroMouse) and not rotellaConCentralePremuto):
                    if event.type == pygame.KEYDOWN:
                        if GlobalVarG2.mouseVisibile:
                            pygame.mouse.set_visible(False)
                            GlobalVarG2.mouseVisibile = False
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
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
            GlobalVarG2.schermo.blit(pers, (x, y))
            if avvele:
                GlobalVarG2.schermo.blit(GlobalVarG2.persAvvele, (x, y))
            GlobalVarG2.schermo.blit(armatura, (x, y))
            GlobalVarG2.schermo.blit(collana, (x, y))
            GlobalVarG2.schermo.blit(faretra, (x, y))
            GlobalVarG2.schermo.blit(GlobalVarG2.persdmbAttacco, (x, y))
            GlobalVarG2.schermo.blit(arco, (x, y))
            GlobalVarG2.schermo.blit(guanti, (x, y))
        if npers == 2:
            GlobalVarG2.schermo.blit(pers, (x, y))
            if avvele:
                GlobalVarG2.schermo.blit(GlobalVarG2.persAvvele, (x, y))
            GlobalVarG2.schermo.blit(armatura, (x, y))
            GlobalVarG2.schermo.blit(collana, (x, y))
            GlobalVarG2.schermo.blit(faretra, (x, y))
            GlobalVarG2.schermo.blit(GlobalVarG2.persambAttacco, (x, y))
            GlobalVarG2.schermo.blit(arco, (x - GlobalVarG2.gpx, y))
            GlobalVarG2.schermo.blit(guanti, (x, y))
        if npers == 3:
            GlobalVarG2.schermo.blit(arco, (x, y - GlobalVarG2.gpy))
            GlobalVarG2.schermo.blit(GlobalVarG2.perswmbAttacco, (x, y))
            GlobalVarG2.schermo.blit(guanti, (x, y))
            GlobalVarG2.schermo.blit(pers, (x, y))
            if avvele:
                GlobalVarG2.schermo.blit(GlobalVarG2.persAvvele, (x, y))
            GlobalVarG2.schermo.blit(armatura, (x, y))
            GlobalVarG2.schermo.blit(collana, (x, y))
            GlobalVarG2.schermo.blit(faretra, (x, y))
        if npers == 4:
            GlobalVarG2.schermo.blit(faretra, (x, y))
            GlobalVarG2.schermo.blit(pers, (x, y))
            if avvele:
                GlobalVarG2.schermo.blit(GlobalVarG2.persAvvele, (x, y))
            GlobalVarG2.schermo.blit(armatura, (x, y))
            GlobalVarG2.schermo.blit(collana, (x, y))
            GlobalVarG2.schermo.blit(GlobalVarG2.perssmbAttacco, (x, y))
            GlobalVarG2.schermo.blit(arco, (x, y))
            GlobalVarG2.schermo.blit(guanti, (x, y))
    else:
        if npers == 1:
            GlobalVarG2.schermo.blit(scudo, (x, y))
            if inMovimento:
                GlobalVarG2.schermo.blit(GlobalVarG2.persdm, (x, y))
            else:
                GlobalVarG2.schermo.blit(pers, (x, y))
            if avvele:
                GlobalVarG2.schermo.blit(GlobalVarG2.persAvvele, (x, y))
            GlobalVarG2.schermo.blit(armatura, (x, y))
            GlobalVarG2.schermo.blit(collana, (x, y))
            GlobalVarG2.schermo.blit(faretra, (x, y))
            GlobalVarG2.schermo.blit(arco, (x, y))
            if attaccoRavvicinato:
                GlobalVarG2.schermo.blit(GlobalVarG2.persdmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalVarG2.schermo.blit(GlobalVarG2.persdmb1, (x, y))
                elif frame == 2:
                    GlobalVarG2.schermo.blit(GlobalVarG2.persdmb2, (x, y))
            else:
                GlobalVarG2.schermo.blit(GlobalVarG2.persdb, (x, y))
            GlobalVarG2.schermo.blit(arma, (x, y))
            GlobalVarG2.schermo.blit(guanti, (x, y))
        if npers == 2:
            if attaccoRavvicinato:
                GlobalVarG2.schermo.blit(arma, (x - GlobalVarG2.gpx, y))
            else:
                GlobalVarG2.schermo.blit(arma, (x, y))
            if inMovimento:
                GlobalVarG2.schermo.blit(GlobalVarG2.persam, (x, y))
            else:
                GlobalVarG2.schermo.blit(pers, (x, y))
            if avvele:
                GlobalVarG2.schermo.blit(GlobalVarG2.persAvvele, (x, y))
            GlobalVarG2.schermo.blit(armatura, (x, y))
            GlobalVarG2.schermo.blit(collana, (x, y))
            GlobalVarG2.schermo.blit(faretra, (x, y))
            GlobalVarG2.schermo.blit(arco, (x, y))
            if attaccoRavvicinato:
                GlobalVarG2.schermo.blit(GlobalVarG2.persambAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalVarG2.schermo.blit(GlobalVarG2.persamb1, (x, y))
                elif frame == 2:
                    GlobalVarG2.schermo.blit(GlobalVarG2.persamb2, (x, y))
            else:
                GlobalVarG2.schermo.blit(GlobalVarG2.persab, (x, y))
            GlobalVarG2.schermo.blit(guanti, (x, y))
            GlobalVarG2.schermo.blit(scudo, (x, y))
        if npers == 3:
            if attaccoRavvicinato:
                GlobalVarG2.schermo.blit(arma, (x, y - GlobalVarG2.gpy))
            else:
                GlobalVarG2.schermo.blit(arma, (x, y))
            GlobalVarG2.schermo.blit(scudo, (x, y))
            if attaccoRavvicinato:
                GlobalVarG2.schermo.blit(GlobalVarG2.perswmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalVarG2.schermo.blit(GlobalVarG2.perswmb1, (x, y))
                elif frame == 2:
                    GlobalVarG2.schermo.blit(GlobalVarG2.perswmb2, (x, y))
            else:
                GlobalVarG2.schermo.blit(GlobalVarG2.perswb, (x, y))
            GlobalVarG2.schermo.blit(guanti, (x, y))
            if inMovimento:
                GlobalVarG2.schermo.blit(GlobalVarG2.perswm, (x, y))
            else:
                GlobalVarG2.schermo.blit(pers, (x, y))
            if avvele:
                GlobalVarG2.schermo.blit(GlobalVarG2.persAvvele, (x, y))
            GlobalVarG2.schermo.blit(armatura, (x, y))
            GlobalVarG2.schermo.blit(collana, (x, y))
            GlobalVarG2.schermo.blit(faretra, (x, y))
            GlobalVarG2.schermo.blit(arco, (x, y))
        if npers == 4:
            GlobalVarG2.schermo.blit(arco, (x, y))
            GlobalVarG2.schermo.blit(faretra, (x, y))
            if inMovimento:
                GlobalVarG2.schermo.blit(GlobalVarG2.perssm, (x, y))
            else:
                GlobalVarG2.schermo.blit(pers, (x, y))
            if avvele:
                GlobalVarG2.schermo.blit(GlobalVarG2.persAvvele, (x, y))
            GlobalVarG2.schermo.blit(armatura, (x, y))
            GlobalVarG2.schermo.blit(collana, (x, y))
            if attaccoRavvicinato:
                GlobalVarG2.schermo.blit(GlobalVarG2.perssmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalVarG2.schermo.blit(GlobalVarG2.perssmb1, (x, y))
                elif frame == 2:
                    GlobalVarG2.schermo.blit(GlobalVarG2.perssmb2, (x, y))
            else:
                GlobalVarG2.schermo.blit(GlobalVarG2.perssb, (x, y))
            GlobalVarG2.schermo.blit(arma, (x, y))
            GlobalVarG2.schermo.blit(guanti, (x, y))
            GlobalVarG2.schermo.blit(scudo, (x, y))


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
    if dati[numOggetto] > 99:
        dati[numOggetto] = 99
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


def dialoga(avanzamentoStoria, personaggio):
    if GlobalVarG2.canaleSoundPassiRallo.get_busy():
        GlobalVarG2.canaleSoundPassiRallo.stop()
    oggettoRicevuto = False
    menuMercante = False
    sceltaEffettuata = 0
    voceMarcata = 1
    puntatoreSpostato = False
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    if avanzamentoStoria < GlobalVarG2.avanzamentoStoriaCambioPersonaggio:
        imgPersDialogo = pygame.transform.scale(GlobalVarG2.imgDialogoFraMaggiore, (GlobalVarG2.gpx * 12, GlobalVarG2.gpy * 9))
        nomePersonaggio = "Sam"
    else:
        imgPersDialogo = pygame.transform.scale(GlobalVarG2.imgDialogoSara, (GlobalVarG2.gpx * 12, GlobalVarG2.gpy * 9))
        nomePersonaggio = "Sara"

    GlobalVarG2.schermo.blit(imgPersDialogo, (GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 4))
    GlobalVarG2.schermo.blit(personaggio.imgDialogo, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
    schermo_prima_del_dialogo = GlobalVarG2.schermo.copy()
    background = schermo_prima_del_dialogo.subsurface(pygame.Rect(0, 0, GlobalVarG2.gsx, GlobalVarG2.gsy))
    dark = pygame.Surface((GlobalVarG2.gsx, GlobalVarG2.gsy), flags=pygame.SRCALPHA)
    dark.fill((0, 0, 0, 150))
    background.blit(dark, (0, 0))
    GlobalVarG2.schermo.blit(background, (0, 0))

    primoframe = True
    aggiornaInterfacciaPerMouse = False
    numeroMessaggiTotali = len(personaggio.partiDialogo)
    numeromessaggioAttuale = 0
    prosegui = True
    fineDialogo = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
    while not fineDialogo:
        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVarG2.mouseVisibile:
            aggiornaInterfacciaPerMouse = True
            pygame.mouse.set_visible(True)
            GlobalVarG2.mouseVisibile = True
        if GlobalVarG2.mouseVisibile:
            if numeromessaggioAttuale < len(personaggio.partiDialogo) and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                if GlobalVarG2.gsx // 32 * 1 <= xMouse <= GlobalVarG2.gsx // 32 * 16 and GlobalVarG2.gsy // 18 * 15.1 <= yMouse <= GlobalVarG2.gsy // 18 * 16.2:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 1
                elif GlobalVarG2.gsx // 32 * 1 <= xMouse <= GlobalVarG2.gsx // 32 * 16 and GlobalVarG2.gsy // 18 * 16.2 <= yMouse <= GlobalVarG2.gsy // 18 * 17.3:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 2
                elif GlobalVarG2.gsx // 32 * 16 <= xMouse <= GlobalVarG2.gsx // 32 * 31 and GlobalVarG2.gsy // 18 * 15.1 <= yMouse <= GlobalVarG2.gsy // 18 * 16.2:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 3
                elif GlobalVarG2.gsx // 32 * 16 <= xMouse <= GlobalVarG2.gsx // 32 * 31 and GlobalVarG2.gsy // 18 * 16.2 <= yMouse <= GlobalVarG2.gsy // 18 * 17.3:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 4
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            else:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
            if voceMarcataVecchia != voceMarcata and not primoframe:
                aggiornaInterfacciaPerMouse = True
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
        primoframe = False

        tastoTrovato = False
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
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato and voceMarcataVecchia == voceMarcata:
                if GlobalVarG2.mouseVisibile:
                    aggiornaInterfacciaPerMouse = True
                    pygame.mouse.set_visible(False)
                    GlobalVarG2.mouseVisibile = False
                if event.key == pygame.K_q and not tastoTrovato:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    tastoTrovato = True
                    fineDialogo = True
                if event.key == pygame.K_w and not tastoTrovato and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                    tastoTrovato = True
                    puntatoreSpostato = True
                    prosegui = True
                    if voceMarcata != 1 and voceMarcata != 3:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        voceMarcata -= 1
                if event.key == pygame.K_a and not tastoTrovato and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                    tastoTrovato = True
                    puntatoreSpostato = True
                    prosegui = True
                    if voceMarcata != 1 and voceMarcata != 2:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        voceMarcata -= 2
                if event.key == pygame.K_s and not tastoTrovato and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                    tastoTrovato = True
                    puntatoreSpostato = True
                    prosegui = True
                    if voceMarcata != 2 and voceMarcata != 4:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        voceMarcata += 1
                if event.key == pygame.K_d and not tastoTrovato and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                    tastoTrovato = True
                    puntatoreSpostato = True
                    prosegui = True
                    if voceMarcata != 3 and voceMarcata != 4:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        voceMarcata += 2
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse and not rotellaConCentralePremuto:
                aggiornaInterfacciaPerMouse = False
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                tastoTrovato = True
                fineDialogo = True
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and not GlobalVarG2.mouseBloccato):
                aggiornaInterfacciaPerMouse = False
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                tastoTrovato = True
                if sceltaEffettuata != 0 and sceltaEffettuata != personaggio.scelta:
                    fineDialogo = True
                elif numeromessaggioAttuale == numeroMessaggiTotali:
                    if not personaggio.scelta or (personaggio.scelta and personaggio.scelta == sceltaEffettuata):
                        if personaggio.avanzamentoStoria:
                            avanzamentoStoria = avanzamentoStoria + 1
                        if personaggio.oggettoDato:
                            oggettoRicevuto = personaggio.oggettoDato
                        if personaggio.menuMercante:
                            menuMercante = personaggio.menuMercante
                    fineDialogo = True
                else:
                    if personaggio.scelta and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                        sceltaEffettuata = voceMarcata
                    prosegui = True
            elif GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and GlobalVarG2.mouseBloccato:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if (sinistroMouse or centraleMouse or destroMouse) and not rotellaConCentralePremuto and not GlobalVarG2.mouseVisibile:
                aggiornaInterfacciaPerMouse = True
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True
        if (prosegui or aggiornaInterfacciaPerMouse) and not fineDialogo:
            if aggiornaInterfacciaPerMouse and numeromessaggioAttuale != 0:
                numeromessaggioAttuale -= 1
                aggiornaInterfacciaPerMouse = False
            if puntatoreSpostato:
                numeromessaggioAttuale -= 1
                puntatoreSpostato = False
            GlobalVarG2.schermo.blit(background, (0, 0))
            if personaggio.partiDialogo[numeromessaggioAttuale][0] == "personaggio":
                GlobalVarG2.schermo.blit(personaggio.imgDialogo, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
            if personaggio.partiDialogo[numeromessaggioAttuale][0] == "tu" or personaggio.partiDialogo[numeromessaggioAttuale][1] == "???DOMANDA???":
                GlobalVarG2.schermo.blit(imgPersDialogo, (GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoDialoghi, (0, GlobalVarG2.gsy * 2 // 3))
            if personaggio.partiDialogo[numeromessaggioAttuale][0] == "personaggio":
                messaggio(personaggio.nome + ":", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, (GlobalVarG2.gsy * 2 // 3) + (GlobalVarG2.gpy * 4 // 5), 80)
            elif personaggio.partiDialogo[numeromessaggioAttuale][0] == "tu":
                messaggio(nomePersonaggio + ":", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, (GlobalVarG2.gsy * 2 // 3) + (GlobalVarG2.gpy * 4 // 5), 80)
            if personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][sceltaEffettuata + 1], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, (GlobalVarG2.gsy * 2 // 3) + (GlobalVarG2.gpy * 7 // 3), 50)
            elif personaggio.partiDialogo[numeromessaggioAttuale][1] == "???DOMANDA???":
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][2], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, (GlobalVarG2.gsy * 2 // 3) + (GlobalVarG2.gpy * 7 // 3), 50)
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][3], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, ((GlobalVarG2.gsy * 2 // 3) + (GlobalVarG2.gpy * 7 // 3)) + int(GlobalVarG2.gpy * 1.2), 50)
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][4], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, ((GlobalVarG2.gsy * 2 // 3) + (GlobalVarG2.gpy * 7 // 3)) + int(GlobalVarG2.gpy * 2.2), 50)
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][5], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17, ((GlobalVarG2.gsy * 2 // 3) + (GlobalVarG2.gpy * 7 // 3)) + int(GlobalVarG2.gpy * 1.2), 50)
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][6], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17, ((GlobalVarG2.gsy * 2 // 3) + (GlobalVarG2.gpy * 7 // 3)) + int(GlobalVarG2.gpy * 2.2), 50)
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, ((GlobalVarG2.gsy * 2 // 3) + (GlobalVarG2.gpy * 7 // 3)) + int(GlobalVarG2.gpy * 1.2), GlobalVarG2.gpx, GlobalVarG2.gpy))
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, ((GlobalVarG2.gsy * 2 // 3) + (GlobalVarG2.gpy * 7 // 3)) + int(GlobalVarG2.gpy * 2.2), GlobalVarG2.gpx, GlobalVarG2.gpy))
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 16, ((GlobalVarG2.gsy * 2 // 3) + (GlobalVarG2.gpy * 7 // 3)) + int(GlobalVarG2.gpy * 1.2), GlobalVarG2.gpx, GlobalVarG2.gpy))
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 16, ((GlobalVarG2.gsy * 2 // 3) + (GlobalVarG2.gpy * 7 // 3)) + int(GlobalVarG2.gpy * 2.2), GlobalVarG2.gpx, GlobalVarG2.gpy))
                if voceMarcata == 1:
                    GlobalVarG2.schermo.blit(puntatore, (GlobalVarG2.gsx // 32 * 1, ((GlobalVarG2.gsy * 2 // 3) + (GlobalVarG2.gpy * 7 // 3)) + int(GlobalVarG2.gpy * 1.2)))
                if voceMarcata == 2:
                    GlobalVarG2.schermo.blit(puntatore, (GlobalVarG2.gsx // 32 * 1, ((GlobalVarG2.gsy * 2 // 3) + (GlobalVarG2.gpy * 7 // 3)) + int(GlobalVarG2.gpy * 2.2)))
                if voceMarcata == 3:
                    GlobalVarG2.schermo.blit(puntatore, (GlobalVarG2.gsx // 32 * 16, ((GlobalVarG2.gsy * 2 // 3) + (GlobalVarG2.gpy * 7 // 3)) + int(GlobalVarG2.gpy * 1.2)))
                if voceMarcata == 4:
                    GlobalVarG2.schermo.blit(puntatore, (GlobalVarG2.gsx // 32 * 16, ((GlobalVarG2.gsy * 2 // 3) + (GlobalVarG2.gpy * 7 // 3)) + int(GlobalVarG2.gpy * 2.2)))
            else:
                riga = -1
                for frase in personaggio.partiDialogo[numeromessaggioAttuale]:
                    if riga == -1:
                        riga = 0
                    else:
                        messaggio(frase, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, ((GlobalVarG2.gsy * 2 // 3) + (GlobalVarG2.gpy * 7 // 3)) + riga, 50)
                        riga += GlobalVarG2.gpy * 4 // 5
            numeromessaggioAttuale += 1
            prosegui = False
            pygame.display.update()
    return avanzamentoStoria, oggettoRicevuto, menuMercante


def animaOggettoSpecialeRicevuto(oggettoRicevuto):
    if GlobalVarG2.canaleSoundPassiRallo.get_busy():
        GlobalVarG2.canaleSoundPassiRallo.stop()
    if GlobalVarG2.mouseBloccato:
        GlobalVarG2.configuraCursore(False)
    GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.suonoRaccoltaMonete)
    GlobalVarG2.schermo.blit(GlobalVarG2.sfocontcof, (GlobalVarG2.gsx // 32 * 0, GlobalVarG2.gsy // 18 * 0))
    messaggio("Hai ottenuto: " + oggettoRicevuto, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
    pygame.display.update()
    risposta = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
    while not risposta:
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVarG2.mouseVisibile:
            pygame.mouse.set_visible(True)
            GlobalVarG2.mouseVisibile = True
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
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto):
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                risposta = True
            if event.type == pygame.KEYDOWN:
                if GlobalVarG2.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVarG2.mouseVisibile = False


def cambiaProtagonista(nome):
    persw = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio4.png')
    GlobalVarG2.persw = pygame.transform.scale(persw, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    perswb = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio4b.png')
    GlobalVarG2.perswb = pygame.transform.scale(perswb, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    persa = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio3.png')
    GlobalVarG2.persa = pygame.transform.scale(persa, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    persab = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio3b.png')
    GlobalVarG2.persab = pygame.transform.scale(persab, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    GlobalVarG2.perso = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio1.png')
    GlobalVarG2.perss = pygame.transform.scale(GlobalVarG2.perso, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    persob = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio1b.png')
    GlobalVarG2.perssb = pygame.transform.scale(persob, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    persd = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio2.png')
    GlobalVarG2.persd = pygame.transform.scale(persd, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    persdb = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio2b.png')
    GlobalVarG2.persdb = pygame.transform.scale(persdb, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    perssm = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio1mov.png')
    GlobalVarG2.perssm = pygame.transform.scale(perssm, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    perssmb1 = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio1movb1.png')
    GlobalVarG2.perssmb1 = pygame.transform.scale(perssmb1, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    perssmb2 = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio1movb2.png')
    GlobalVarG2.perssmb2 = pygame.transform.scale(perssmb2, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    persdm = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio2mov.png')
    GlobalVarG2.persdm = pygame.transform.scale(persdm, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    persdmb1 = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio2movb1.png')
    GlobalVarG2.persdmb1 = pygame.transform.scale(persdmb1, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    persdmb2 = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio2movb2.png')
    GlobalVarG2.persdmb2 = pygame.transform.scale(persdmb2, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    persam = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio3mov.png')
    GlobalVarG2.persam = pygame.transform.scale(persam, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    persamb1 = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio3movb1.png')
    GlobalVarG2.persamb1 = pygame.transform.scale(persamb1, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    persamb2 = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio3movb2.png')
    GlobalVarG2.persamb2 = pygame.transform.scale(persamb2, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    perswm = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio4mov.png')
    GlobalVarG2.perswm = pygame.transform.scale(perswm, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    perswmb1 = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio4movb1.png')
    GlobalVarG2.perswmb1 = pygame.transform.scale(perswmb1, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    perswmb2 = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio4movb2.png')
    GlobalVarG2.perswmb2 = pygame.transform.scale(perswmb2, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    perswmbAttacco = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio4movbAttacco.png')
    GlobalVarG2.perswmbAttacco = pygame.transform.scale(perswmbAttacco, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    persambAttacco = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio3movbAttacco.png')
    GlobalVarG2.persambAttacco = pygame.transform.scale(persambAttacco, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    perssmbAttacco = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio1movbAttacco.png')
    GlobalVarG2.perssmbAttacco = pygame.transform.scale(perssmbAttacco, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    persdmbAttacco = pygame.image.load('Immagini/Personaggi/' + nome + '/Personaggio2movbAttacco.png')
    GlobalVarG2.persdmbAttacco = pygame.transform.scale(persdmbAttacco, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    persmbDifesa = pygame.image.load('Immagini/Personaggi/' + nome + '/PersonaggiomovbDifesa.png')
    GlobalVarG2.persmbDifesa = pygame.transform.scale(persmbDifesa, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    persAvvele = pygame.image.load('Immagini/Personaggi/' + nome + '/PersonaggioAvvelenato.png')
    GlobalVarG2.persAvvele = pygame.transform.scale(persAvvele, (GlobalVarG2.gpx, GlobalVarG2.gpy))


"""# rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
pygame.draw.rect(GlobalVarG2.schermo, blu, (nx, ny, GlobalVarG2.gpx, GlobalVarG2.gpy))
pygame.display.update()"""
