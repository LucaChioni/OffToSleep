# -*- coding: utf-8 -*-

import os
import random
from FadeToBlackClass import *
from SetOstacoliContenutoCofanetti import *


def messaggio(msg, colore, x, y, gr, largezzaFoglio=-1, spazioTraLeRighe=-1):
    gr = gr - 10
    gr = GlobalVar.gpx * gr // 60
    y = y - (GlobalVar.gpy // 8)
    carattere = "Liberation Serif"
    font = pygame.font.SysFont(carattere, gr)
    coloreOrig = colore
    xOrig = x

    # per mettere parti in italic, bold o colorate: "Premi <*>#bold#un<*> <*>#italic#tasto<*> per <*>#color#100,0,0#continuare<*>..."
    vetMsg = msg.split("<*>")
    for text in vetMsg:
        colore = coloreOrig
        font.set_italic(False)
        font.set_bold(False)
        if text.startswith("#italic#"):
            text = text.replace("#italic#", "")
            font.set_italic(True)
        elif text.startswith("#bold#"):
            text = text.replace("#bold#", "")
            font.set_bold(True)
        elif text.startswith("#color#"):
            text = text.replace("#color#", "")
            coloreRgb = text.split("#")[0]
            text = text.split("#")[1]
            colore = (int(coloreRgb.split(",")[0]), int(coloreRgb.split(",")[1]), int(coloreRgb.split(",")[2]))
        vetParole = text.split(" ")
        for parola in vetParole:
            if parola != "":
                if parola == "<br>":
                    x = xOrig
                    y += spazioTraLeRighe
                else:
                    testo = font.render(parola, True, colore)
                    dimX, dimY = font.size(parola + " ")
                    if largezzaFoglio != -1 and x + dimX > xOrig + largezzaFoglio:
                        x = xOrig
                        if spazioTraLeRighe != 1:
                            y += spazioTraLeRighe
                        else:
                            y += dimY
                    GlobalVar.schermo.blit(testo, (x, y))
                    x += dimX


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
    if GlobalVar.mouseBloccato:
        GlobalVar.configuraCursore(False)
    GlobalVar.schermo.fill(GlobalVar.grigioscu)
    pygame.display.update()
    listaImg = []
    # load all the images
    for i in os.listdir(GlobalVar.gamePath + path):
        img = GlobalVar.loadImage(path + '/' + i, False, convert=True)
        img = pygame.transform.smoothscale(img, (GlobalVar.gsx, GlobalVar.gsy))
        listaImg.append(img)
    if audio != 0:
        GlobalVar.canaleSoundCanzone.play(audio)
    # play video
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
    i = 0
    while i < len(listaImg) + 10:
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVar.mouseVisibile:
            pygame.mouse.set_visible(True)
            GlobalVar.mouseVisibile = True
        if i >= 10:
            GlobalVar.schermo.blit(listaImg[i - 10], (0, 0))
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
                    GlobalVar.quit()
                if event.type == pygame.KEYDOWN or (event.type == pygame.MOUSEBUTTONDOWN and (sinistroMouse or centraleMouse or destroMouse) and not rotellaConCentralePremuto):
                    if event.type == pygame.KEYDOWN:
                        if GlobalVar.mouseVisibile:
                            pygame.mouse.set_visible(False)
                            GlobalVar.mouseVisibile = False
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                    if audio != 0:
                        GlobalVar.canaleSoundCanzone.stop()
                    return True
        pygame.event.pump()
        GlobalVar.clockVideo.tick(GlobalVar.fpsVideo)
        i += 1
    if audio != 0:
        GlobalVar.canaleSoundCanzone.stop()
    return False


def trovacasattaccabili(x, y, raggio, caseviste):
    if raggio == -1:
        rangeXSinistra = (x // GlobalVar.gpx) - 2
        rangeXDestra = (GlobalVar.gsx // GlobalVar.gpx) - (x // GlobalVar.gpx) - 3
        rangeYAlto = (y // GlobalVar.gpy) - 2
        rangeYBasso = (GlobalVar.gsy // GlobalVar.gpy) - (y // GlobalVar.gpy) - 3
    else:
        rangeXSinistra = raggio // GlobalVar.gpx
        if (x // GlobalVar.gpx) - rangeXSinistra < 2:
            rangeXSinistra = (x // GlobalVar.gpx) - 2
        rangeXDestra = raggio // GlobalVar.gpx
        if (x // GlobalVar.gpx) + rangeXDestra > 30:
            rangeXDestra = (GlobalVar.gsx // GlobalVar.gpx) - (x // GlobalVar.gpx) - 3
        rangeYAlto = raggio // GlobalVar.gpy
        if (y // GlobalVar.gpy) - rangeYAlto < 2:
            rangeYAlto = (y // GlobalVar.gpy) - 2
        rangeYBasso = raggio // GlobalVar.gpy
        if (y // GlobalVar.gpy) + rangeYBasso > 16:
            rangeYBasso = (GlobalVar.gsy // GlobalVar.gpy) - (y // GlobalVar.gpy) - 3

    # il vettore caseattac contiene solo le caselle nel raggio visivo
    caseattac = []
    i = 0
    while i < len(caseviste):
        if caseviste[i] <= x + (rangeXDestra * GlobalVar.gpx) and caseviste[i] >= x - (rangeXSinistra * GlobalVar.gpx) and caseviste[i + 1] <= y + (rangeYBasso * GlobalVar.gpy) and caseviste[i + 1] >= y - (rangeYAlto * GlobalVar.gpy):
            caseattac.append(caseviste[i])
            caseattac.append(caseviste[i + 1])
            caseattac.append(caseviste[i + 2])
        i += 3

    margineDiErrore = 1
    base1 = 0
    base2 = 0
    altezza = 0

    # caseattacbassodestra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli in basso a destra
    caseattacbassodestra = []
    # riempio caseattacbassodestra come se tutto il campo in basso a destra fosse libero
    n = 0
    while n <= rangeXDestra:
        m = 0
        while m <= rangeYBasso:
            caseattacbassodestra.append(x + (GlobalVar.gpx * n))
            caseattacbassodestra.append(y + (GlobalVar.gpy * m))
            caseattacbassodestra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacbassodestra[2] = False
    i = 0
    while i < len(caseattac):
        if caseattac[i] > x and caseattac[i] <= x + (rangeXDestra * GlobalVar.gpx) and caseattac[i + 1] > y and caseattac[i + 1] <= y + (rangeYBasso * GlobalVar.gpy) and not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVar.gpy
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
                    xLatoDestroCasella = caseattacbassodestra[j] + GlobalVar.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacbassodestra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacbassodestra[j + 1] + GlobalVar.gpy
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
                                latoSinistro = GlobalVar.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalVar.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalVar.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoDestro != 0:
                                area = (GlobalVar.gpx * GlobalVar.gpy) - ((GlobalVar.gpx - latoSuperiore) * (GlobalVar.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalVar.gpx * GlobalVar.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalVar.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalVar.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalVar.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoSinistro != 0:
                                area = (GlobalVar.gpx * GlobalVar.gpy) - ((GlobalVar.gpx - latoInferiore) * (GlobalVar.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalVar.gpx * GlobalVar.gpy / 2.0) + margineDiErrore:
                                caseattacbassodestra[j + 2] = False
                        elif (yLatoSuperioreCasella > yRetta1LatoDestroCasella and xLatoDestroCasella < xRetta1LatoSuperioreCasella) and (yLatoInferioreCasella < yRetta2LatoSinistroCasella and xLatoSinistroCasella > xRetta2LatoInferioreCasella):
                            caseattacbassodestra[j + 2] = False

                j += 3
        i += 3

    # caseattacbassosinistra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli in basso a sinistra
    caseattacbassosinistra = []
    # riempio caseattacbassosinistra come se tutto il campo in basso a sinistra fosse libero
    n = 0
    while n <= rangeXSinistra:
        m = 0
        while m <= rangeYBasso:
            caseattacbassosinistra.append(x - (GlobalVar.gpx * n))
            caseattacbassosinistra.append(y + (GlobalVar.gpy * m))
            caseattacbassosinistra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacbassosinistra[2] = False
    i = 0
    while i < len(caseattac):
        if caseattac[i] < x and caseattac[i] >= x - (rangeXSinistra * GlobalVar.gpx) and caseattac[i + 1] > y and caseattac[i + 1] <= y + (rangeYBasso * GlobalVar.gpy) and not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = - deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVar.gpy
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
                    xLatoDestroCasella = caseattacbassosinistra[j] + GlobalVar.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacbassosinistra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacbassosinistra[j + 1] + GlobalVar.gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacbassosinistra[j + 2] and yLatoSuperioreCasella >= caseattac[i + 1] and xLatoDestroCasella <= caseattac[i] + GlobalVar.gpx:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = GlobalVar.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalVar.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalVar.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoSinistro != 0:
                                area = (GlobalVar.gpx * GlobalVar.gpy) - ((GlobalVar.gpx - latoSuperiore) * (GlobalVar.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalVar.gpx * GlobalVar.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalVar.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalVar.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalVar.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoDestro != 0:
                                area = (GlobalVar.gpx * GlobalVar.gpy) - ((GlobalVar.gpx - latoInferiore) * (GlobalVar.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalVar.gpx * GlobalVar.gpy / 2.0) + margineDiErrore:
                                caseattacbassosinistra[j + 2] = False
                        elif (yLatoSuperioreCasella > yRetta1LatoSinistroCasella and xLatoSinistroCasella > xRetta1LatoSuperioreCasella) and (yLatoInferioreCasella < yRetta2LatoDestroCasella and xLatoDestroCasella < xRetta2LatoInferioreCasella):
                            caseattacbassosinistra[j + 2] = False

                j += 3
        i += 3

    # caseattacaltosinistra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli in alto a sinistra
    caseattacaltosinistra = []
    # riempio caseattacaltosinistra come se tutto il campo in alto a sinistra fosse libero
    n = 0
    while n <= rangeXSinistra:
        m = 0
        while m <= rangeYAlto:
            caseattacaltosinistra.append(x - (GlobalVar.gpx * n))
            caseattacaltosinistra.append(y - (GlobalVar.gpy * m))
            caseattacaltosinistra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacaltosinistra[2] = False
    i = 0
    while i < len(caseattac):
        if caseattac[i] < x and caseattac[i] >= x - (rangeXSinistra * GlobalVar.gpx) and caseattac[i + 1] < y and caseattac[i + 1] >= y - (rangeYAlto * GlobalVar.gpy) and not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVar.gpy
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
                    xLatoDestroCasella = caseattacaltosinistra[j] + GlobalVar.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacaltosinistra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacaltosinistra[j + 1] + GlobalVar.gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacaltosinistra[j + 2] and yLatoInferioreCasella <= caseattac[i + 1] + GlobalVar.gpy and xLatoDestroCasella <= caseattac[i] + GlobalVar.gpx:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = GlobalVar.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalVar.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalVar.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoDestro != 0:
                                area = (GlobalVar.gpx * GlobalVar.gpy) - ((GlobalVar.gpx - latoSuperiore) * (GlobalVar.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalVar.gpx * GlobalVar.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalVar.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalVar.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalVar.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoSinistro != 0:
                                area = (GlobalVar.gpx * GlobalVar.gpy) - ((GlobalVar.gpx - latoInferiore) * (GlobalVar.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalVar.gpx * GlobalVar.gpy / 2.0) + margineDiErrore:
                                caseattacaltosinistra[j + 2] = False
                        elif (yLatoSuperioreCasella > yRetta1LatoDestroCasella and xLatoDestroCasella < xRetta1LatoSuperioreCasella) and (yLatoInferioreCasella < yRetta2LatoSinistroCasella and xLatoSinistroCasella > xRetta2LatoInferioreCasella):
                            caseattacaltosinistra[j + 2] = False

                j += 3
        i += 3

    # caseattacaltodestra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli in alto a destra
    caseattacaltodestra = []
    # riempio caseattacaltodestra come se tutto il campo in alto a destra fosse libero
    n = 0
    while n <= rangeXDestra:
        m = 0
        while m <= rangeYAlto:
            caseattacaltodestra.append(x + (GlobalVar.gpx * n))
            caseattacaltodestra.append(y - (GlobalVar.gpy * m))
            caseattacaltodestra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacaltodestra[2] = False
    i = 0
    while i < len(caseattac):
        if caseattac[i] > x and caseattac[i] <= x + (rangeXDestra * GlobalVar.gpx) and caseattac[i + 1] < y and caseattac[i + 1] >= y - (rangeYAlto * GlobalVar.gpy) and not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = - deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVar.gpy
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
                    xLatoDestroCasella = caseattacaltodestra[j] + GlobalVar.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacaltodestra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacaltodestra[j + 1] + GlobalVar.gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacaltodestra[j + 2] and yLatoInferioreCasella <= caseattac[i + 1] + GlobalVar.gpy and xLatoSinistroCasella >= caseattac[i]:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = GlobalVar.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalVar.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalVar.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoSinistro != 0:
                                area = (GlobalVar.gpx * GlobalVar.gpy) - ((GlobalVar.gpx - latoSuperiore) * (GlobalVar.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalVar.gpx * GlobalVar.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalVar.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalVar.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalVar.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoDestro != 0:
                                area = (GlobalVar.gpx * GlobalVar.gpy) - ((GlobalVar.gpx - latoInferiore) * (GlobalVar.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalVar.gpx * GlobalVar.gpy / 2.0) + margineDiErrore:
                                caseattacaltodestra[j + 2] = False
                        elif (yLatoSuperioreCasella > yRetta1LatoSinistroCasella and xLatoSinistroCasella > xRetta1LatoSuperioreCasella) and (yLatoInferioreCasella < yRetta2LatoDestroCasella and xLatoDestroCasella < xRetta2LatoInferioreCasella):
                            caseattacaltodestra[j + 2] = False

                j += 3
        i += 3

    # caseattacdestra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli a destra
    caseattacdestra = []
    # riempio caseattacdestra come se tutto il campo a destra fosse libero
    n = 0
    while n <= rangeXDestra:
        m = 0
        while m <= rangeYAlto:
            caseattacdestra.append(x + (GlobalVar.gpx * n))
            caseattacdestra.append(y - (GlobalVar.gpy * m))
            caseattacdestra.append(True)
            m = m + 1
        m = 1
        while m <= rangeYBasso:
            caseattacdestra.append(x + (GlobalVar.gpx * n))
            caseattacdestra.append(y + (GlobalVar.gpy * m))
            caseattacdestra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacdestra[2] = False
    i = 0
    while i < len(caseattac):
        if caseattac[i] > x and caseattac[i] <= x + (rangeXDestra * GlobalVar.gpx) and caseattac[i + 1] == y and not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = - deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVar.gpy
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
                    xLatoDestroCasella = caseattacdestra[j] + GlobalVar.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacdestra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacdestra[j + 1] + GlobalVar.gpy
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
                                latoSinistro = GlobalVar.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalVar.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalVar.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoSinistro != 0:
                                area = (GlobalVar.gpx * GlobalVar.gpy) - ((GlobalVar.gpx - latoSuperiore) * (GlobalVar.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalVar.gpx * GlobalVar.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalVar.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalVar.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalVar.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoSinistro != 0:
                                area = (GlobalVar.gpx * GlobalVar.gpy) - ((GlobalVar.gpx - latoInferiore) * (GlobalVar.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalVar.gpx * GlobalVar.gpy / 2.0) + margineDiErrore:
                                caseattacdestra[j + 2] = False
                        elif (yLatoSuperioreCasella > yRetta1LatoSinistroCasella and xLatoSinistroCasella > xRetta1LatoSuperioreCasella) and (yLatoInferioreCasella < yRetta2LatoSinistroCasella and xLatoSinistroCasella > xRetta2LatoInferioreCasella):
                            caseattacdestra[j + 2] = False

                j += 3
        i += 3

    # caseattacsinistra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli a sinistra
    caseattacsinistra = []
    # riempio caseattacsinistra come se tutto il campo a sinistra fosse libero
    n = 0
    while n <= rangeXSinistra:
        m = 0
        while m <= rangeYAlto:
            caseattacsinistra.append(x - (GlobalVar.gpx * n))
            caseattacsinistra.append(y - (GlobalVar.gpy * m))
            caseattacsinistra.append(True)
            m = m + 1
        m = 1
        while m <= rangeYBasso:
            caseattacsinistra.append(x - (GlobalVar.gpx * n))
            caseattacsinistra.append(y + (GlobalVar.gpy * m))
            caseattacsinistra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacsinistra[2] = False
    i = 0
    while i < len(caseattac):
        if caseattac[i] < x and caseattac[i] >= x - (rangeXSinistra * GlobalVar.gpx) and caseattac[i + 1] == y and not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVar.gpy
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
                    xLatoDestroCasella = caseattacsinistra[j] + GlobalVar.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacsinistra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacsinistra[j + 1] + GlobalVar.gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacsinistra[j + 2] and xLatoDestroCasella <= caseattac[i] + GlobalVar.gpx:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = GlobalVar.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalVar.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalVar.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoDestro != 0:
                                area = (GlobalVar.gpx * GlobalVar.gpy) - ((GlobalVar.gpx - latoSuperiore) * (GlobalVar.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalVar.gpx * GlobalVar.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalVar.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalVar.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalVar.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoDestro != 0:
                                area = (GlobalVar.gpx * GlobalVar.gpy) - ((GlobalVar.gpx - latoInferiore) * (GlobalVar.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalVar.gpx * GlobalVar.gpy / 2.0) + margineDiErrore:
                                caseattacsinistra[j + 2] = False
                        elif (yLatoSuperioreCasella > yRetta1LatoDestroCasella and xLatoDestroCasella < xRetta1LatoSuperioreCasella) and (yLatoInferioreCasella < yRetta2LatoDestroCasella and xLatoDestroCasella < xRetta2LatoInferioreCasella):
                            caseattacsinistra[j + 2] = False

                j += 3
        i += 3

    # caseattacalto[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli sopra
    caseattacalto = []
    # riempio caseattacalto come se tutto il campo sopra fosse libero
    n = 0
    while n <= rangeYAlto:
        m = 0
        while m <= rangeXDestra:
            caseattacalto.append(x + (GlobalVar.gpx * m))
            caseattacalto.append(y - (GlobalVar.gpy * n))
            caseattacalto.append(True)
            m = m + 1
        m = 1
        while m <= rangeXSinistra:
            caseattacalto.append(x - (GlobalVar.gpx * m))
            caseattacalto.append(y - (GlobalVar.gpy * n))
            caseattacalto.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacalto[2] = False
    i = 0
    while i < len(caseattac):
        if caseattac[i] == x and caseattac[i + 1] < y and caseattac[i + 1] >= y - (rangeYAlto * GlobalVar.gpy) and not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVar.gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVar.gpy
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
                    xLatoDestroCasella = caseattacalto[j] + GlobalVar.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacalto[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacalto[j + 1] + GlobalVar.gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacalto[j + 2] and yLatoInferioreCasella <= caseattac[i + 1] + GlobalVar.gpy:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta2
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoSuperioreCasella)
                            elif yRetta1LatoSinistroCasella > yLatoInferioreCasella:
                                latoSinistro = GlobalVar.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta1LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalVar.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalVar.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoSinistro != 0:
                                area = (GlobalVar.gpx * GlobalVar.gpy) - ((GlobalVar.gpx - latoInferiore) * (GlobalVar.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalVar.gpx * GlobalVar.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalVar.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalVar.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalVar.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoDestro != 0:
                                area = (GlobalVar.gpx * GlobalVar.gpy) - ((GlobalVar.gpx - latoInferiore) * (GlobalVar.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalVar.gpx * GlobalVar.gpy / 2.0) + margineDiErrore:
                                caseattacalto[j + 2] = False
                        elif (yLatoInferioreCasella < yRetta1LatoSinistroCasella and xLatoSinistroCasella > xRetta1LatoInferioreCasella) and (yLatoInferioreCasella < yRetta2LatoDestroCasella and xLatoDestroCasella < xRetta2LatoInferioreCasella):
                            caseattacalto[j + 2] = False

                j += 3
        i += 3

    # caseattacbasso[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli sotto
    caseattacbasso = []
    # riempio caseattacbasso come se tutto il campo sotto fosse libero
    n = 0
    while n <= rangeYBasso:
        m = 0
        while m <= rangeXDestra:
            caseattacbasso.append(x + (GlobalVar.gpx * m))
            caseattacbasso.append(y + (GlobalVar.gpy * n))
            caseattacbasso.append(True)
            m = m + 1
        m = 1
        while m <= rangeXSinistra:
            caseattacbasso.append(x - (GlobalVar.gpx * m))
            caseattacbasso.append(y + (GlobalVar.gpy * n))
            caseattacbasso.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacbasso[2] = False
    i = 0
    while i < len(caseattac):
        if caseattac[i] == x and caseattac[i + 1] > y and caseattac[i + 1] <= y + (rangeYBasso * GlobalVar.gpy) and not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = - deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #pygame.draw.line(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in alto a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
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
                    xLatoDestroCasella = caseattacbasso[j] + GlobalVar.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacbasso[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacbasso[j + 1] + GlobalVar.gpy
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
                                latoSinistro = GlobalVar.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalVar.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalVar.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoSinistro != 0:
                                area = (GlobalVar.gpx * GlobalVar.gpy) - ((GlobalVar.gpx - latoSuperiore) * (GlobalVar.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalVar.gpx * GlobalVar.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalVar.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta2LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalVar.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalVar.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoDestro != 0:
                                area = (GlobalVar.gpx * GlobalVar.gpy) - ((GlobalVar.gpx - latoSuperiore) * (GlobalVar.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalVar.gpx * GlobalVar.gpy / 2.0) + margineDiErrore:
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

    # aggiungo le caselle dei bordi
    i = 0
    while i < 32:
        if raggio == -1 or (raggio != -1 and (GlobalVar.gpx * i <= x + raggio and 0 <= y + raggio) and (GlobalVar.gpx * i >= x - raggio and 0 >= y - raggio)):
            caseattactot.append(GlobalVar.gpx * i)
            caseattactot.append(0)
            caseattactot.append(False)
        if raggio == -1 or (raggio != -1 and (GlobalVar.gpx * i <= x + raggio and GlobalVar.gpy <= y + raggio) and (GlobalVar.gpx * i >= x - raggio and GlobalVar.gpy >= y - raggio)):
            caseattactot.append(GlobalVar.gpx * i)
            caseattactot.append(GlobalVar.gpy)
            caseattactot.append(False)
        if raggio == -1 or (raggio != -1 and (GlobalVar.gpx * i <= x + raggio and GlobalVar.gpy * 16 <= y + raggio) and (GlobalVar.gpx * i >= x - raggio and GlobalVar.gpy * 16 >= y - raggio)):
            caseattactot.append(GlobalVar.gpx * i)
            caseattactot.append(GlobalVar.gpy * 16)
            caseattactot.append(False)
        if raggio == -1 or (raggio != -1 and (GlobalVar.gpx * i <= x + raggio and GlobalVar.gpy * 17 <= y + raggio) and (GlobalVar.gpx * i >= x - raggio and GlobalVar.gpy * 17 >= y - raggio)):
            caseattactot.append(GlobalVar.gpx * i)
            caseattactot.append(GlobalVar.gpy * 17)
            caseattactot.append(False)
        i += 1
    i = 2
    while i < 16:
        if raggio == -1 or (raggio != -1 and (0 <= x + raggio and GlobalVar.gpy * i <= y + raggio) and (0 >= x - raggio and GlobalVar.gpy * i >= y - raggio)):
            caseattactot.append(0)
            caseattactot.append(GlobalVar.gpy * i)
            caseattactot.append(False)
        if raggio == -1 or (raggio != -1 and (GlobalVar.gpx <= x + raggio and GlobalVar.gpy * i <= y + raggio) and (GlobalVar.gpx >= x - raggio and GlobalVar.gpy * i >= y - raggio)):
            caseattactot.append(GlobalVar.gpx)
            caseattactot.append(GlobalVar.gpy * i)
            caseattactot.append(False)
        if raggio == -1 or (raggio != -1 and (GlobalVar.gpx * 30 <= x + raggio and GlobalVar.gpy * i <= y + raggio) and (GlobalVar.gpx * 30 >= x - raggio and GlobalVar.gpy * i >= y - raggio)):
            caseattactot.append(GlobalVar.gpx * 30)
            caseattactot.append(GlobalVar.gpy * i)
            caseattactot.append(False)
        if raggio == -1 or (raggio != -1 and (GlobalVar.gpx * 31 <= x + raggio and GlobalVar.gpy * i <= y + raggio) and (GlobalVar.gpx * 31 >= x - raggio and GlobalVar.gpy * i >= y - raggio)):
            caseattactot.append(GlobalVar.gpx * 31)
            caseattactot.append(GlobalVar.gpy * i)
            caseattactot.append(False)
        i += 1

    return caseattactot


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
        nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -GlobalVar.gpy, numstanza, False, escludiPorte, porte, cofanetti)
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
        nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, GlobalVar.gpy, numstanza, False, escludiPorte, porte, cofanetti)
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
        nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], -GlobalVar.gpx, 0, numstanza, False, escludiPorte, porte, cofanetti)
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
        nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], GlobalVar.gpx, 0, numstanza, False, escludiPorte, porte, cofanetti)
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
        if caseviste[i] == rx and caseviste[i + 1] == ry:
            if caseviste[i + 2]:
                incasevista = True
            break
        i = i + 3
    if not incasevista:
        caselleEsplorate = [rx, ry]
        j = 0
        while j < len(caselleEsplorate):
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -GlobalVar.gpy, numstanza, False, escludiPorte, porte, cofanetti)
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
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, GlobalVar.gpy, numstanza, False, escludiPorte, porte, cofanetti)
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
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], -GlobalVar.gpx, 0, numstanza, False, escludiPorte, porte, cofanetti)
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
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], GlobalVar.gpx, 0, numstanza, False, escludiPorte, porte, cofanetti)
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


def pathFinding(xPartenza, yPartenza, xArrivo, yArrivo, vetOstacoli, caseviste):
    # caselleEsplorate contiene x, y e valore delle caselle già esplorate (il valore serve per trovare il percorso più breve)
    valoreCasella = 0
    caselleEsplorate = [xPartenza, yPartenza, valoreCasella]
    percorsoTrovato = []

    impossibileRaggiungere = False
    if (xPartenza == xArrivo and yPartenza == yArrivo + GlobalVar.gpy) or (xPartenza == xArrivo and yPartenza == yArrivo - GlobalVar.gpy) or (xPartenza == xArrivo + GlobalVar.gpx and yPartenza == yArrivo) or (xPartenza == xArrivo and yPartenza - GlobalVar.gpx == yArrivo):
        k = 0
        while k < len(vetOstacoli):
            if xArrivo == vetOstacoli[k] and yArrivo == vetOstacoli[k + 1]:
                impossibileRaggiungere = True
            k += 2
    if xPartenza == xArrivo and yPartenza == yArrivo and not impossibileRaggiungere:
        percorsoTrovato = "arrivato"
    elif not impossibileRaggiungere:
        caselleLibere = []
        i = 0
        while i < len(caseviste):
            if caseviste[i + 2]:
                ostacolato = False
                k = 0
                while k < len(vetOstacoli):
                    if caseviste[i] == vetOstacoli[k] and caseviste[i + 1] == vetOstacoli[k + 1]:
                        ostacolato = True
                        break
                    k += 2
                if not ostacolato and not (caseviste[i] == xPartenza and caseviste[i + 1] == yPartenza):
                    caselleLibere.append(caseviste[i])
                    caselleLibere.append(caseviste[i + 1])
            i += 3

        arrivato = False
        countCaselleDiPartenza = 1
        countCaselleFeudo = 0
        countCaselleDiPartenzaEsaminate = 0
        j = 0
        while j < len(caselleEsplorate) and not arrivato:
            caselleAccantoTrovate = 0
            if countCaselleFeudo == 0:
                valoreCasella += 1

            i = 0
            while i < len(caselleLibere) and caselleAccantoTrovate < 4:
                casellaCancellata = False
                if (caselleLibere[i] == caselleEsplorate[j] + GlobalVar.gpx and caselleLibere[i + 1] == caselleEsplorate[j + 1]) or (caselleLibere[i] == caselleEsplorate[j] - GlobalVar.gpx and caselleLibere[i + 1] == caselleEsplorate[j + 1]) or (caselleLibere[i] == caselleEsplorate[j] and caselleLibere[i + 1] == caselleEsplorate[j + 1] + GlobalVar.gpy) or (caselleLibere[i] == caselleEsplorate[j] and caselleLibere[i + 1] == caselleEsplorate[j + 1] - GlobalVar.gpy):
                    caselleAccantoTrovate += 1
                    caselleEsplorate.append(caselleLibere[i])
                    caselleEsplorate.append(caselleLibere[i + 1])
                    caselleEsplorate.append(valoreCasella)
                    if caselleLibere[i] == xArrivo and caselleLibere[i + 1] == yArrivo:
                        arrivato = True
                        break
                    casellaCancellata = True
                    del caselleLibere[i + 1]
                    del caselleLibere[i]
                if not casellaCancellata:
                    i += 2
            countCaselleFeudo += caselleAccantoTrovate
            countCaselleDiPartenzaEsaminate += 1
            if countCaselleDiPartenza == countCaselleDiPartenzaEsaminate:
                countCaselleDiPartenza = countCaselleFeudo
                countCaselleDiPartenzaEsaminate = 0
                countCaselleFeudo = 0
            j += 3

        if arrivato:
            # percorsoTrovato contiene x e y per ogni casella del percorso da restituire
            percorsoTrovato = []
            finito = False
            xCasellaAttuale = caselleEsplorate[len(caselleEsplorate) - 3]
            yCasellaAttuale = caselleEsplorate[len(caselleEsplorate) - 2]
            while not finito:
                valoriCaselleAccanto = []
                i = len(caselleEsplorate) - 3
                while i >= 0:
                    xCasellaAccanto = caselleEsplorate[i]
                    yCasellaAccanto = caselleEsplorate[i + 1]
                    if (xCasellaAttuale == xCasellaAccanto + GlobalVar.gpx and yCasellaAttuale == yCasellaAccanto) or (xCasellaAttuale == xCasellaAccanto - GlobalVar.gpx and yCasellaAttuale == yCasellaAccanto) or (xCasellaAttuale == xCasellaAccanto and yCasellaAttuale == yCasellaAccanto + GlobalVar.gpy) or (xCasellaAttuale == xCasellaAccanto and yCasellaAttuale == yCasellaAccanto - GlobalVar.gpy):
                        valoriCaselleAccanto.append(caselleEsplorate[i])
                        valoriCaselleAccanto.append(caselleEsplorate[i + 1])
                        valoriCaselleAccanto.append(caselleEsplorate[i + 2])
                    i -= 3
                if len(valoriCaselleAccanto) > 0:
                    xCasellaMin = valoriCaselleAccanto[0]
                    yCasellaMin = valoriCaselleAccanto[1]
                    valCasellaMin = valoriCaselleAccanto[2]
                    i = 0
                    while i < len(valoriCaselleAccanto):
                        if valoriCaselleAccanto[i + 2] < valCasellaMin:
                            xCasellaMin = valoriCaselleAccanto[i]
                            yCasellaMin = valoriCaselleAccanto[i + 1]
                            valCasellaMin = valoriCaselleAccanto[i + 2]
                        elif valoriCaselleAccanto[i + 2] == valCasellaMin and ((abs(xPartenza - xArrivo) > abs(yPartenza - yArrivo) and abs(xArrivo - valoriCaselleAccanto[i]) < abs(xArrivo - xCasellaMin)) or (abs(yPartenza - yArrivo) > abs(xPartenza - xArrivo) and abs(yArrivo - valoriCaselleAccanto[i + 1]) < abs(yArrivo - yCasellaMin)) or (abs(yPartenza - yArrivo) == abs(xPartenza - xArrivo) and random.randint(0, 1) == 0)):
                            xCasellaMin = valoriCaselleAccanto[i]
                            yCasellaMin = valoriCaselleAccanto[i + 1]
                            valCasellaMin = valoriCaselleAccanto[i + 2]
                        i += 3
                    percorsoTrovato.append(xCasellaMin)
                    percorsoTrovato.append(yCasellaMin)
                    if valCasellaMin == 0:
                        finito = True
                xCasellaAttuale = percorsoTrovato[len(percorsoTrovato) - 2]
                yCasellaAttuale = percorsoTrovato[len(percorsoTrovato) - 1]
        else:
            impossibileRaggiungere = True

    if impossibileRaggiungere:
        return False
    else:
        return percorsoTrovato


def controllaMorteRallo(vitaRallo, inizio):
    if vitaRallo <= 0:
        if GlobalVar.mouseBloccato:
            GlobalVar.configuraCursore(False)
        GlobalVar.canaleSoundCanzone.stop()
        GlobalVar.canaleSoundPuntatore.stop()
        GlobalVar.canaleSoundPassiRallo.stop()
        GlobalVar.canaleSoundPassiColco.stop()
        GlobalVar.canaleSoundPassiNemiciPersonaggi.stop()
        GlobalVar.canaleSoundMorteNemici.stop()
        GlobalVar.canaleSoundLvUp.stop()
        GlobalVar.canaleSoundInterazioni.stop()
        GlobalVar.canaleSoundAttacco.stop()
        pygame.time.wait(500)
        GlobalVar.canaleSoundInterazioni.play(GlobalVar.rumoreMorte)
        sprites = pygame.sprite.Group(Fade(3))
        schermoFadeToBlack = GlobalVar.schermo.copy()
        i = 1
        while i <= 35:
            sprites.update()
            GlobalVar.schermo.blit(schermoFadeToBlack, (0, 0))
            sprites.draw(GlobalVar.schermo)
            pygame.display.update()
            GlobalVar.clockFadeToBlack.tick(GlobalVar.fpsFadeToBlack)
            i += 1

        # GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
        messaggio("Sei morto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 13, 150)
        pygame.display.update()
        continua = False
        sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
        while not continua:
            deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
            if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVar.mouseVisibile:
                pygame.mouse.set_visible(True)
                GlobalVar.mouseVisibile = True
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
                if event.type == pygame.KEYDOWN or (event.type == pygame.MOUSEBUTTONDOWN and (sinistroMouse or centraleMouse or destroMouse) and not rotellaConCentralePremuto):
                    if event.type == pygame.KEYDOWN:
                        if GlobalVar.mouseVisibile:
                            pygame.mouse.set_visible(False)
                            GlobalVar.mouseVisibile = False
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
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
            GlobalVar.schermo.blit(pers, (x, y))
            if avvele:
                GlobalVar.schermo.blit(GlobalVar.persAvvele, (x, y))
            GlobalVar.schermo.blit(armatura, (x, y))
            GlobalVar.schermo.blit(collana, (x, y))
            GlobalVar.schermo.blit(faretra, (x, y))
            GlobalVar.schermo.blit(GlobalVar.persdmbAttacco, (x, y))
            GlobalVar.schermo.blit(arco, (x, y))
            GlobalVar.schermo.blit(guanti, (x, y))
        if npers == 2:
            GlobalVar.schermo.blit(pers, (x, y))
            if avvele:
                GlobalVar.schermo.blit(GlobalVar.persAvvele, (x, y))
            GlobalVar.schermo.blit(armatura, (x, y))
            GlobalVar.schermo.blit(collana, (x, y))
            GlobalVar.schermo.blit(faretra, (x, y))
            GlobalVar.schermo.blit(GlobalVar.persambAttacco, (x, y))
            GlobalVar.schermo.blit(arco, (x - GlobalVar.gpx, y))
            GlobalVar.schermo.blit(guanti, (x, y))
        if npers == 3:
            GlobalVar.schermo.blit(arco, (x, y - GlobalVar.gpy))
            GlobalVar.schermo.blit(GlobalVar.perswmbAttacco, (x, y))
            GlobalVar.schermo.blit(guanti, (x, y))
            GlobalVar.schermo.blit(pers, (x, y))
            if avvele:
                GlobalVar.schermo.blit(GlobalVar.persAvvele, (x, y))
            GlobalVar.schermo.blit(armatura, (x, y))
            GlobalVar.schermo.blit(collana, (x, y))
            GlobalVar.schermo.blit(faretra, (x, y))
        if npers == 4:
            GlobalVar.schermo.blit(faretra, (x, y))
            GlobalVar.schermo.blit(pers, (x, y))
            if avvele:
                GlobalVar.schermo.blit(GlobalVar.persAvvele, (x, y))
            GlobalVar.schermo.blit(armatura, (x, y))
            GlobalVar.schermo.blit(collana, (x, y))
            GlobalVar.schermo.blit(GlobalVar.perssmbAttacco, (x, y))
            GlobalVar.schermo.blit(arco, (x, y))
            GlobalVar.schermo.blit(guanti, (x, y))
    else:
        if npers == 1:
            GlobalVar.schermo.blit(scudo, (x, y))
            if inMovimento:
                GlobalVar.schermo.blit(GlobalVar.persdm, (x, y))
            else:
                GlobalVar.schermo.blit(pers, (x, y))
            if avvele:
                GlobalVar.schermo.blit(GlobalVar.persAvvele, (x, y))
            GlobalVar.schermo.blit(armatura, (x, y))
            GlobalVar.schermo.blit(collana, (x, y))
            GlobalVar.schermo.blit(faretra, (x, y))
            GlobalVar.schermo.blit(arco, (x, y))
            if attaccoRavvicinato:
                GlobalVar.schermo.blit(GlobalVar.persdmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalVar.schermo.blit(GlobalVar.persdmb1, (x, y))
                elif frame == 2:
                    GlobalVar.schermo.blit(GlobalVar.persdmb2, (x, y))
            else:
                GlobalVar.schermo.blit(GlobalVar.persdb, (x, y))
            GlobalVar.schermo.blit(arma, (x, y))
            GlobalVar.schermo.blit(guanti, (x, y))
        if npers == 2:
            if attaccoRavvicinato:
                GlobalVar.schermo.blit(arma, (x - GlobalVar.gpx, y))
            else:
                GlobalVar.schermo.blit(arma, (x, y))
            if inMovimento:
                GlobalVar.schermo.blit(GlobalVar.persam, (x, y))
            else:
                GlobalVar.schermo.blit(pers, (x, y))
            if avvele:
                GlobalVar.schermo.blit(GlobalVar.persAvvele, (x, y))
            GlobalVar.schermo.blit(armatura, (x, y))
            GlobalVar.schermo.blit(collana, (x, y))
            GlobalVar.schermo.blit(faretra, (x, y))
            GlobalVar.schermo.blit(arco, (x, y))
            if attaccoRavvicinato:
                GlobalVar.schermo.blit(GlobalVar.persambAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalVar.schermo.blit(GlobalVar.persamb1, (x, y))
                elif frame == 2:
                    GlobalVar.schermo.blit(GlobalVar.persamb2, (x, y))
            else:
                GlobalVar.schermo.blit(GlobalVar.persab, (x, y))
            GlobalVar.schermo.blit(guanti, (x, y))
            GlobalVar.schermo.blit(scudo, (x, y))
        if npers == 3:
            if attaccoRavvicinato:
                GlobalVar.schermo.blit(arma, (x, y - GlobalVar.gpy))
            else:
                GlobalVar.schermo.blit(arma, (x, y))
            GlobalVar.schermo.blit(scudo, (x, y))
            if attaccoRavvicinato:
                GlobalVar.schermo.blit(GlobalVar.perswmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalVar.schermo.blit(GlobalVar.perswmb1, (x, y))
                elif frame == 2:
                    GlobalVar.schermo.blit(GlobalVar.perswmb2, (x, y))
            else:
                GlobalVar.schermo.blit(GlobalVar.perswb, (x, y))
            GlobalVar.schermo.blit(guanti, (x, y))
            if inMovimento:
                GlobalVar.schermo.blit(GlobalVar.perswm, (x, y))
            else:
                GlobalVar.schermo.blit(pers, (x, y))
            if avvele:
                GlobalVar.schermo.blit(GlobalVar.persAvvele, (x, y))
            GlobalVar.schermo.blit(armatura, (x, y))
            GlobalVar.schermo.blit(collana, (x, y))
            GlobalVar.schermo.blit(faretra, (x, y))
            GlobalVar.schermo.blit(arco, (x, y))
        if npers == 4:
            GlobalVar.schermo.blit(arco, (x, y))
            GlobalVar.schermo.blit(faretra, (x, y))
            if inMovimento:
                GlobalVar.schermo.blit(GlobalVar.perssm, (x, y))
            else:
                GlobalVar.schermo.blit(pers, (x, y))
            if avvele:
                GlobalVar.schermo.blit(GlobalVar.persAvvele, (x, y))
            GlobalVar.schermo.blit(armatura, (x, y))
            GlobalVar.schermo.blit(collana, (x, y))
            if attaccoRavvicinato:
                GlobalVar.schermo.blit(GlobalVar.perssmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalVar.schermo.blit(GlobalVar.perssmb1, (x, y))
                elif frame == 2:
                    GlobalVar.schermo.blit(GlobalVar.perssmb2, (x, y))
            else:
                GlobalVar.schermo.blit(GlobalVar.perssb, (x, y))
            GlobalVar.schermo.blit(arma, (x, y))
            GlobalVar.schermo.blit(guanti, (x, y))
            GlobalVar.schermo.blit(scudo, (x, y))


def dialoga(avanzamentoStoria, personaggio, canzone):
    if GlobalVar.canaleSoundPassiRallo.get_busy():
        GlobalVar.canaleSoundPassiRallo.stop()
    oggettoRicevuto = False
    menuMercante = False
    sceltaEffettuata = 0
    voceMarcata = 1
    puntatoreSpostato = False
    puntatore = GlobalVar.puntatore
    if GlobalVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
        imgPersDialogo = pygame.transform.smoothscale(GlobalVar.imgDialogoFraMaggiore, (GlobalVar.gpx * 16, GlobalVar.gpy * 12))
        nomePersonaggio = "Sam"
    else:
        imgPersDialogo = pygame.transform.smoothscale(GlobalVar.imgDialogoSara, (GlobalVar.gpx * 16, GlobalVar.gpy * 12))
        nomePersonaggio = "Sara"

    if personaggio.nome != "Tutorial":
        GlobalVar.schermo.blit(imgPersDialogo, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 3.5))
    if personaggio.nome != "Tutorial" and personaggio.nome != "Nessuno":
        GlobalVar.schermo.blit(personaggio.imgDialogo, (GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 3.5))
    schermo_prima_del_dialogo = GlobalVar.schermo.copy()
    background = schermo_prima_del_dialogo.subsurface(pygame.Rect(0, 0, GlobalVar.gsx, GlobalVar.gsy))
    dark = pygame.Surface((GlobalVar.gsx, GlobalVar.gsy), flags=pygame.SRCALPHA)
    dark.fill((0, 0, 0, 150))
    background.blit(dark, (0, 0))
    GlobalVar.schermo.blit(background, (0, 0))

    schermo_prima_del_dialogo = GlobalVar.schermo.copy()
    background = schermo_prima_del_dialogo.subsurface(pygame.Rect(0, GlobalVar.gsy // 18 * 3.5, GlobalVar.gsx, GlobalVar.gsy // 18 * 14.5))

    primoframe = True
    aggiornaInterfacciaPerMouse = False
    numeroMessaggiTotali = len(personaggio.partiDialogo)
    numeromessaggioAttuale = 0
    prosegui = True
    fineDialogo = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    GlobalVar.canaleSoundCanzone.set_volume(GlobalVar.volumeCanzoni / 2)
    while not fineDialogo:
        if canzone and not GlobalVar.canaleSoundCanzone.get_busy():
            GlobalVar.canaleSoundCanzone.play(canzone)

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVar.mouseVisibile:
            aggiornaInterfacciaPerMouse = True
            pygame.mouse.set_visible(True)
            GlobalVar.mouseVisibile = True
        if GlobalVar.mouseVisibile:
            if numeromessaggioAttuale < len(personaggio.partiDialogo) and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                if GlobalVar.gsx // 32 * 1 <= xMouse <= GlobalVar.gsx // 32 * 16 and GlobalVar.gsy // 18 * 15.1 <= yMouse <= GlobalVar.gsy // 18 * 16.2:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 1
                elif GlobalVar.gsx // 32 * 1 <= xMouse <= GlobalVar.gsx // 32 * 16 and GlobalVar.gsy // 18 * 16.2 <= yMouse <= GlobalVar.gsy // 18 * 17.3:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 2
                elif GlobalVar.gsx // 32 * 16 <= xMouse <= GlobalVar.gsx // 32 * 31 and GlobalVar.gsy // 18 * 15.1 <= yMouse <= GlobalVar.gsy // 18 * 16.2:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 3
                elif GlobalVar.gsx // 32 * 16 <= xMouse <= GlobalVar.gsx // 32 * 31 and GlobalVar.gsy // 18 * 16.2 <= yMouse <= GlobalVar.gsy // 18 * 17.3:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 4
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            else:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
            if voceMarcataVecchia != voceMarcata and not primoframe:
                aggiornaInterfacciaPerMouse = True
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
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
                GlobalVar.quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato and voceMarcataVecchia == voceMarcata:
                if GlobalVar.mouseVisibile:
                    aggiornaInterfacciaPerMouse = True
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if event.key == pygame.K_q and not tastoTrovato:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    tastoTrovato = True
                    fineDialogo = True
                if event.key == pygame.K_w and not tastoTrovato and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                    tastoTrovato = True
                    puntatoreSpostato = True
                    prosegui = True
                    if voceMarcata != 1 and voceMarcata != 3:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        voceMarcata -= 1
                if event.key == pygame.K_a and not tastoTrovato and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                    tastoTrovato = True
                    puntatoreSpostato = True
                    prosegui = True
                    if voceMarcata != 1 and voceMarcata != 2:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        voceMarcata -= 2
                if event.key == pygame.K_s and not tastoTrovato and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                    tastoTrovato = True
                    puntatoreSpostato = True
                    prosegui = True
                    if voceMarcata != 2 and voceMarcata != 4:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        voceMarcata += 1
                if event.key == pygame.K_d and not tastoTrovato and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                    tastoTrovato = True
                    puntatoreSpostato = True
                    prosegui = True
                    if voceMarcata != 3 and voceMarcata != 4:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        voceMarcata += 2
            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse and not rotellaConCentralePremuto:
                aggiornaInterfacciaPerMouse = False
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                tastoTrovato = True
                fineDialogo = True
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and not GlobalVar.mouseBloccato):
                aggiornaInterfacciaPerMouse = False
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                tastoTrovato = True
                if sceltaEffettuata != 0 and sceltaEffettuata != personaggio.scelta:
                    fineDialogo = True
                elif numeromessaggioAttuale == numeroMessaggiTotali:
                    if not personaggio.scelta or (personaggio.scelta and personaggio.scelta == sceltaEffettuata):
                        if personaggio.avanzaStoria:
                            avanzamentoStoria = avanzamentoStoria + 1
                        if personaggio.oggettoDato:
                            oggettoRicevuto = personaggio.oggettoDato
                        if personaggio.menuMercante:
                            menuMercante = personaggio.menuMercante
                    if personaggio.cambiaImg:
                        personaggio.imgCambiata += 1
                        personaggio.cambiaImg = False
                    fineDialogo = True
                else:
                    if personaggio.scelta and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                        sceltaEffettuata = voceMarcata
                    prosegui = True
            elif GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and GlobalVar.mouseBloccato:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
            if (sinistroMouse or centraleMouse or destroMouse) and not rotellaConCentralePremuto and not GlobalVar.mouseVisibile:
                aggiornaInterfacciaPerMouse = True
                pygame.mouse.set_visible(True)
                GlobalVar.mouseVisibile = True
        if (prosegui or aggiornaInterfacciaPerMouse) and not fineDialogo:
            if aggiornaInterfacciaPerMouse and numeromessaggioAttuale != 0:
                numeromessaggioAttuale -= 1
                aggiornaInterfacciaPerMouse = False
            if puntatoreSpostato:
                numeromessaggioAttuale -= 1
                puntatoreSpostato = False
            GlobalVar.schermo.blit(background, (0, GlobalVar.gsy // 18 * 3.5))
            if personaggio.nome != "Tutorial":
                if personaggio.partiDialogo[numeromessaggioAttuale][0] == "personaggio" and personaggio.nome != "Nessuno":
                    GlobalVar.schermo.blit(personaggio.imgDialogo, (GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 3.5))
                if personaggio.partiDialogo[numeromessaggioAttuale][0] == "tu" or personaggio.partiDialogo[numeromessaggioAttuale][1] == "???DOMANDA???":
                    GlobalVar.schermo.blit(imgPersDialogo, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 3.5))
            GlobalVar.schermo.blit(GlobalVar.sfondoDialoghi, (0, GlobalVar.gsy * 2 // 3))
            if personaggio.partiDialogo[numeromessaggioAttuale][0] == "personaggio":
                messaggio(personaggio.nome + ":", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, (GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 4 // 5), 80)
            elif personaggio.partiDialogo[numeromessaggioAttuale][0] == "tu":
                messaggio(nomePersonaggio + ":", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, (GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 4 // 5), 80)
            if personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][sceltaEffettuata + 1], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, (GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3), 50)
            elif personaggio.partiDialogo[numeromessaggioAttuale][1] == "???DOMANDA???":
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][2], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, (GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3), 50)
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][3], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, ((GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3)) + int(GlobalVar.gpy * 1.2), 50)
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][4], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, ((GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3)) + int(GlobalVar.gpy * 2.2), 50)
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][5], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 17, ((GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3)) + int(GlobalVar.gpy * 1.2), 50)
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][6], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 17, ((GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3)) + int(GlobalVar.gpy * 2.2), 50)
                pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, ((GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3)) + int(GlobalVar.gpy * 1.2), GlobalVar.gpx, GlobalVar.gpy))
                pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, ((GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3)) + int(GlobalVar.gpy * 2.2), GlobalVar.gpx, GlobalVar.gpy))
                pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 16, ((GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3)) + int(GlobalVar.gpy * 1.2), GlobalVar.gpx, GlobalVar.gpy))
                pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 16, ((GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3)) + int(GlobalVar.gpy * 2.2), GlobalVar.gpx, GlobalVar.gpy))
                if voceMarcata == 1:
                    GlobalVar.schermo.blit(puntatore, (GlobalVar.gsx // 32 * 1, ((GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3)) + int(GlobalVar.gpy * 1.2)))
                if voceMarcata == 2:
                    GlobalVar.schermo.blit(puntatore, (GlobalVar.gsx // 32 * 1, ((GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3)) + int(GlobalVar.gpy * 2.2)))
                if voceMarcata == 3:
                    GlobalVar.schermo.blit(puntatore, (GlobalVar.gsx // 32 * 16, ((GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3)) + int(GlobalVar.gpy * 1.2)))
                if voceMarcata == 4:
                    GlobalVar.schermo.blit(puntatore, (GlobalVar.gsx // 32 * 16, ((GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3)) + int(GlobalVar.gpy * 2.2)))
            else:
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][1], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, (GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3), 50, GlobalVar.gpx * 30, GlobalVar.gpy * 4 // 5)
            numeromessaggioAttuale += 1
            prosegui = False
            pygame.display.update()
    GlobalVar.canaleSoundCanzone.set_volume(GlobalVar.volumeCanzoni)

    return avanzamentoStoria, oggettoRicevuto, menuMercante


def animaOggettoSpecialeRicevuto(oggettoRicevuto, canzone):
    if GlobalVar.canaleSoundPassiRallo.get_busy():
        GlobalVar.canaleSoundPassiRallo.stop()
    if GlobalVar.mouseBloccato:
        GlobalVar.configuraCursore(False)
    GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoRaccoltaMonete)
    GlobalVar.schermo.blit(GlobalVar.sfocontcof, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 0))
    messaggio("Hai ottenuto: " + oggettoRicevuto, GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
    pygame.display.update()
    risposta = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
    while not risposta:
        if canzone and not GlobalVar.canaleSoundCanzone.get_busy():
            GlobalVar.canaleSoundCanzone.play(canzone)
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVar.mouseVisibile:
            pygame.mouse.set_visible(True)
            GlobalVar.mouseVisibile = True
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
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto):
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                risposta = True
            if event.type == pygame.KEYDOWN:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False


def cambiaProtagonista(nome):
    persw = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4.png', True)
    GlobalVar.persw = pygame.transform.smoothscale(persw, (GlobalVar.gpx, GlobalVar.gpy))
    perswb = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4b.png', True)
    GlobalVar.perswb = pygame.transform.smoothscale(perswb, (GlobalVar.gpx, GlobalVar.gpy))
    persa = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3.png', True)
    GlobalVar.persa = pygame.transform.smoothscale(persa, (GlobalVar.gpx, GlobalVar.gpy))
    persab = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3b.png', True)
    GlobalVar.persab = pygame.transform.smoothscale(persab, (GlobalVar.gpx, GlobalVar.gpy))
    GlobalVar.perso = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1.png', True)
    GlobalVar.perss = pygame.transform.smoothscale(GlobalVar.perso, (GlobalVar.gpx, GlobalVar.gpy))
    persob = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1b.png', True)
    GlobalVar.perssb = pygame.transform.smoothscale(persob, (GlobalVar.gpx, GlobalVar.gpy))
    persd = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2.png', True)
    GlobalVar.persd = pygame.transform.smoothscale(persd, (GlobalVar.gpx, GlobalVar.gpy))
    persdb = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2b.png', True)
    GlobalVar.persdb = pygame.transform.smoothscale(persdb, (GlobalVar.gpx, GlobalVar.gpy))
    perssm = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1mov.png', True)
    GlobalVar.perssm = pygame.transform.smoothscale(perssm, (GlobalVar.gpx, GlobalVar.gpy))
    perssmb1 = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1movb1.png', True)
    GlobalVar.perssmb1 = pygame.transform.smoothscale(perssmb1, (GlobalVar.gpx, GlobalVar.gpy))
    perssmb2 = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1movb2.png', True)
    GlobalVar.perssmb2 = pygame.transform.smoothscale(perssmb2, (GlobalVar.gpx, GlobalVar.gpy))
    persdm = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2mov.png', True)
    GlobalVar.persdm = pygame.transform.smoothscale(persdm, (GlobalVar.gpx, GlobalVar.gpy))
    persdmb1 = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2movb1.png', True)
    GlobalVar.persdmb1 = pygame.transform.smoothscale(persdmb1, (GlobalVar.gpx, GlobalVar.gpy))
    persdmb2 = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2movb2.png', True)
    GlobalVar.persdmb2 = pygame.transform.smoothscale(persdmb2, (GlobalVar.gpx, GlobalVar.gpy))
    persam = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3mov.png', True)
    GlobalVar.persam = pygame.transform.smoothscale(persam, (GlobalVar.gpx, GlobalVar.gpy))
    persamb1 = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3movb1.png', True)
    GlobalVar.persamb1 = pygame.transform.smoothscale(persamb1, (GlobalVar.gpx, GlobalVar.gpy))
    persamb2 = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3movb2.png', True)
    GlobalVar.persamb2 = pygame.transform.smoothscale(persamb2, (GlobalVar.gpx, GlobalVar.gpy))
    perswm = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4mov.png', True)
    GlobalVar.perswm = pygame.transform.smoothscale(perswm, (GlobalVar.gpx, GlobalVar.gpy))
    perswmb1 = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4movb1.png', True)
    GlobalVar.perswmb1 = pygame.transform.smoothscale(perswmb1, (GlobalVar.gpx, GlobalVar.gpy))
    perswmb2 = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4movb2.png', True)
    GlobalVar.perswmb2 = pygame.transform.smoothscale(perswmb2, (GlobalVar.gpx, GlobalVar.gpy))
    perswmbAttacco = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4movbAttacco.png', True)
    GlobalVar.perswmbAttacco = pygame.transform.smoothscale(perswmbAttacco, (GlobalVar.gpx, GlobalVar.gpy))
    persambAttacco = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3movbAttacco.png', True)
    GlobalVar.persambAttacco = pygame.transform.smoothscale(persambAttacco, (GlobalVar.gpx, GlobalVar.gpy))
    perssmbAttacco = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1movbAttacco.png', True)
    GlobalVar.perssmbAttacco = pygame.transform.smoothscale(perssmbAttacco, (GlobalVar.gpx, GlobalVar.gpy))
    persdmbAttacco = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2movbAttacco.png', True)
    GlobalVar.persdmbAttacco = pygame.transform.smoothscale(persdmbAttacco, (GlobalVar.gpx, GlobalVar.gpy))
    persmbDifesa = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/PersonaggiomovbDifesa.png', True)
    GlobalVar.persmbDifesa = pygame.transform.smoothscale(persmbDifesa, (GlobalVar.gpx, GlobalVar.gpy))
    persAvvele = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/PersonaggioAvvelenato.png', True)
    GlobalVar.persAvvele = pygame.transform.smoothscale(persAvvele, (GlobalVar.gpx, GlobalVar.gpy))


def aggiornaInCasellaVistaDiNemiciEPersonaggi(caseviste, listaNemici, listaPersonaggi):
    for nemico in listaNemici:
        nemico.inCasellaVista = False
        i = 0
        while i < len(caseviste):
            if caseviste[i] == nemico.x and caseviste[i + 1] == nemico.y:
                if caseviste[i + 2]:
                    nemico.inCasellaVista = True
                break
            i += 3

    for personaggio in listaPersonaggi:
        if not personaggio.mantieniSempreASchermo:
            personaggio.inCasellaVista = False
            i = 0
            while i < len(caseviste):
                if caseviste[i] == personaggio.x and caseviste[i + 1] == personaggio.y:
                    if caseviste[i + 2]:
                        personaggio.inCasellaVista = True
                    break
                i += 3
        else:
            personaggio.vicinoACasellaVista = False
            i = 0
            while i < len(caseviste):
                if (personaggio.x + GlobalVar.gpx == caseviste[i] and personaggio.y == caseviste[i + 1]) or (personaggio.x - GlobalVar.gpx == caseviste[i] and personaggio.y == caseviste[i + 1]) or (personaggio.x == caseviste[i] and personaggio.y + GlobalVar.gpy == caseviste[i + 1]) or (personaggio.x == caseviste[i] and personaggio.y - GlobalVar.gpy == caseviste[i + 1]):
                    if caseviste[i + 2]:
                        personaggio.vicinoACasellaVista = True
                        break
                i += 3

    return listaNemici, listaPersonaggi


def scorriObbiettiviInquadrati(avanzamentoStoria, nemicoInquadrato, listaNemiciVisti, listaEscheViste, scorriAvanti):
    obbiettivoRichiesto = False
    trovatoNemicoDaInquadrare = False

    if scorriAvanti:
        if not nemicoInquadrato and avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
            obbiettivoRichiesto = "Colco"
        elif not nemicoInquadrato and avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
            obbiettivoRichiesto = "NemicoIniziale"
        elif type(nemicoInquadrato) is str and nemicoInquadrato == "Colco":
            obbiettivoRichiesto = "NemicoIniziale"
        elif not type(nemicoInquadrato) is str and nemicoInquadrato:
            obbiettivoRichiesto = "NemicoSuccessivo"
        elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
            obbiettivoRichiesto = "EscaSuccessiva"
        cicliDisponibili = 2
        while obbiettivoRichiesto and not trovatoNemicoDaInquadrare and cicliDisponibili > 0:
            if obbiettivoRichiesto == "Colco":
                nemicoInquadrato = "Colco"
                trovatoNemicoDaInquadrare = True
            if obbiettivoRichiesto == "NemicoIniziale":
                if len(listaNemiciVisti) > 0:
                    nemicoInquadrato = listaNemiciVisti[0]
                    trovatoNemicoDaInquadrare = True
                else:
                    obbiettivoRichiesto = "EscaIniziale"
            if obbiettivoRichiesto == "NemicoSuccessivo":
                if len(listaNemiciVisti) > 0 and listaNemiciVisti.index(nemicoInquadrato) < len(listaNemiciVisti) - 1:
                    nemicoInquadrato = listaNemiciVisti[listaNemiciVisti.index(nemicoInquadrato) + 1]
                    trovatoNemicoDaInquadrare = True
                else:
                    obbiettivoRichiesto = "EscaIniziale"
            if obbiettivoRichiesto == "EscaIniziale":
                if len(listaEscheViste) > 0:
                    nemicoInquadrato = "Esca" + str(listaEscheViste[0])
                    trovatoNemicoDaInquadrare = True
                else:
                    obbiettivoRichiesto = "ColcoFinale"
            if obbiettivoRichiesto == "EscaSuccessiva":
                if len(listaEscheViste) > 0 and listaEscheViste.index(int(nemicoInquadrato[4:])) + 3 < len(
                        listaEscheViste) - 1:
                    nemicoInquadrato = "Esca" + str(listaEscheViste[listaEscheViste.index(int(nemicoInquadrato[4:])) + 4])
                    trovatoNemicoDaInquadrare = True
                else:
                    obbiettivoRichiesto = "ColcoFinale"
            if obbiettivoRichiesto == "ColcoFinale":
                if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
                    nemicoInquadrato = "Colco"
                    trovatoNemicoDaInquadrare = True
                else:
                    obbiettivoRichiesto = "NemicoIniziale"
            cicliDisponibili -= 1
    else:
        if not nemicoInquadrato and avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
            obbiettivoRichiesto = "Colco"
        elif not nemicoInquadrato and avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
            obbiettivoRichiesto = "EscaFinale"
        elif type(nemicoInquadrato) is str and nemicoInquadrato == "Colco":
            obbiettivoRichiesto = "EscaFinale"
        elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
            obbiettivoRichiesto = "EscaPrecedente"
        elif not type(nemicoInquadrato) is str and nemicoInquadrato:
            obbiettivoRichiesto = "NemicoPrecedente"
        trovatoNemicoDaInquadrare = False
        cicliDisponibili = 2
        while cicliDisponibili > 0 and not trovatoNemicoDaInquadrare:
            if obbiettivoRichiesto == "Colco":
                nemicoInquadrato = "Colco"
                trovatoNemicoDaInquadrare = True
            if obbiettivoRichiesto == "EscaFinale":
                if len(listaEscheViste) > 0:
                    nemicoInquadrato = "Esca" + str(listaEscheViste[len(listaEscheViste) - 4])
                    trovatoNemicoDaInquadrare = True
                else:
                    obbiettivoRichiesto = "NemicoFinale"
            if obbiettivoRichiesto == "EscaPrecedente":
                if len(listaEscheViste) > 0 and listaEscheViste.index(int(nemicoInquadrato[4:])) != 0:
                    nemicoInquadrato = "Esca" + str(
                        listaEscheViste[listaEscheViste.index(int(nemicoInquadrato[4:])) - 4])
                    trovatoNemicoDaInquadrare = True
                else:
                    obbiettivoRichiesto = "NemicoFinale"
            if obbiettivoRichiesto == "NemicoFinale":
                if len(listaNemiciVisti) > 0:
                    nemicoInquadrato = listaNemiciVisti[len(listaNemiciVisti) - 1]
                    trovatoNemicoDaInquadrare = True
                else:
                    obbiettivoRichiesto = "ColcoFinale"
            if obbiettivoRichiesto == "NemicoPrecedente":
                if len(listaNemiciVisti) > 0 and listaNemiciVisti.index(nemicoInquadrato) != 0:
                    nemicoInquadrato = listaNemiciVisti[listaNemiciVisti.index(nemicoInquadrato) - 1]
                    trovatoNemicoDaInquadrare = True
                else:
                    obbiettivoRichiesto = "ColcoFinale"
            if obbiettivoRichiesto == "ColcoFinale":
                if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
                    nemicoInquadrato = "Colco"
                    trovatoNemicoDaInquadrare = True
                else:
                    obbiettivoRichiesto = "EscaFinale"
            cicliDisponibili -= 1

    if trovatoNemicoDaInquadrare:
        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selObbiettivo)
    else:
        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
    return nemicoInquadrato


def creaTuttiIVettoriPerLeCaselleViste(x, y, rx, ry, stanza, porte, cofanetti):
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
    caseviste = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, caseviste)
    # casevisteEntrateIncluse include anche le entrate della stanza
    casevisteEntrateIncluse = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, caseviste[:], False)
    # casellePercorribili include solo le caselle su cui si può camminare
    casellePercorribili = scopriCaselleViste(x, y, rx, ry, stanza, [], [], caseviste[:])
    i = 0
    while i < len(casellePercorribili):
        if not casellePercorribili[i + 2]:
            del casellePercorribili[i + 2]
            del casellePercorribili[i + 1]
            del casellePercorribili[i]
        else:
            i += 3
    i = 0
    while i < len(caseviste):
        j = 0
        while j < len(casellePercorribili):
            if caseviste[i] == casellePercorribili[j] and caseviste[i + 1] == casellePercorribili[j + 1]:
                if not caseviste[i + 2]:
                    casellePercorribili[j + 2] = False
                break
            j += 3
        i += 3
    # scopro le caselle delle porte vicine a una casella vista
    vetPorteViste = []
    i = 0
    while i < len(porte):
        if not porte[i + 3]:
            j = 0
            while j < len(casellePercorribili):
                if casellePercorribili[j + 2] and ((porte[i + 1] == casellePercorribili[j] + GlobalVar.gpx and porte[i + 2] == casellePercorribili[j + 1]) or (porte[i + 1] == casellePercorribili[j] - GlobalVar.gpx and porte[i + 2] == casellePercorribili[j + 1]) or (porte[i + 1] == casellePercorribili[j] and porte[i + 2] == casellePercorribili[j + 1] + GlobalVar.gpy) or (porte[i + 1] == casellePercorribili[j] and porte[i + 2] == casellePercorribili[j + 1] - GlobalVar.gpy)):
                    vetPorteViste.append(porte[i + 1])
                    vetPorteViste.append(porte[i + 2])
                    break
                j += 3
        i += 4
    i = 0
    while i < len(casellePercorribili):
        j = 0
        while j < len(vetPorteViste):
            if casellePercorribili[i] == vetPorteViste[j] and casellePercorribili[i + 1] == vetPorteViste[j + 1]:
                casellePercorribili[i + 2] = True
                break
            j += 2
        i += 3

    return caseviste, casevisteEntrateIncluse, casellePercorribili


def disegnaOmbreggiaturaNellaCasellaSpecifica(x, y, casellaChiara, casellaScura):
    if ((x / GlobalVar.gpx) + (y / GlobalVar.gpy)) % 2 == 0:
        GlobalVar.schermo.blit(casellaChiara, (x, y))
    if ((x / GlobalVar.gpx) + (y / GlobalVar.gpy)) % 2 == 1:
        GlobalVar.schermo.blit(casellaScura, (x, y))


'''# linea(dove,colore,inizio,fine,spessore)
pygame.draw.line(GlobalVarG2.schermo, verde, (0, 0), (GlobalVarG2.gsx, GlobalVarG2.gsy), 10)
# cerchio(dove,colore,centro,raggio,spessore)
pygame.draw.circle(GlobalVarG2.schermo, blu, (300, 100), 5)
# rettangolo(dove,colore,(x,y,larghezza,altezza),spessore)
pygame.draw.rect(GlobalVarG2.schermo, rosso, (200, 100, 30, 40), 5)'''
