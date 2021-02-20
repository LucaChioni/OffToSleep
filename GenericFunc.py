# -*- coding: utf-8 -*-

import random
import copy
import pygame
import GlobalHWVar
import GlobalSndVar
import GlobalImgVar
import GlobalGameVar
import GestioneInput
import SetOstacoliContenutoCofanetti


def messaggio(msg, colore, x, y, gr, largezzaFoglio=-1, spazioTraLeRighe=-1, daDestra=False, centrale=False, lungMax=False):
    x = int(x)
    y = int(y)

    gr = gr - 10
    gr = GlobalHWVar.gpx * gr // 60
    y = y - (GlobalHWVar.gpy // 8)
    font = pygame.font.Font(GlobalHWVar.fontUtilizzato, gr)
    italic = False
    bold = False
    coloreOrig = colore
    xOrig = x

    testoComplesso = False
    if "<*>" in msg or "<br>" in msg or largezzaFoglio != -1 or spazioTraLeRighe != -1:
        testoComplesso = True

    # per mettere parti in italic, bold o colorate: "Premi <*>#bold#un<*> <*>#italic#tasto<*> per <*>#color#100,0,0#continuare<*>..."
    if daDestra:
        testo = font.render(msg, True, colore)
        dimX, dimY = font.size(msg)
        GlobalHWVar.disegnaImmagineSuSchermo(testo, (x - dimX, y))
    elif centrale:
        msgIniziale = msg
        font.render(msg, True, colore)
        dimX, dimY = font.size(msg)
        if lungMax and dimX > lungMax * GlobalHWVar.gpx:
            while dimX > lungMax * GlobalHWVar.gpx:
                msg = msg[:-1]
                font.render(msg + "...", True, colore)
                dimX, dimY = font.size(msg)
        if msgIniziale != msg:
            msg += "..."
        testo = font.render(msg, True, colore)
        dimX, dimY = font.size(msg)
        GlobalHWVar.disegnaImmagineSuSchermo(testo, (x - (dimX // 2), y))
    elif testoComplesso:
        vetMsg = msg.split("<*>")
        for text in vetMsg:
            colore = coloreOrig
            if italic or bold:
                font = pygame.font.Font(GlobalHWVar.fontUtilizzato, gr)
                italic = False
                bold = False
            if text.startswith("#italic#"):
                text = text.replace("#italic#", "")
                font = pygame.font.Font(GlobalHWVar.fontUtilizzatoItalic, gr)
                italic = True
            elif text.startswith("#bold#"):
                text = text.replace("#bold#", "")
                font = pygame.font.Font(GlobalHWVar.fontUtilizzatoBold, gr)
                bold = True
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
                        GlobalHWVar.disegnaImmagineSuSchermo(testo, (x, y))
                        x += dimX
    else:
        testo = font.render(msg, True, colore)
        GlobalHWVar.disegnaImmagineSuSchermo(testo, (x, y))


def getStatistiche(dati, difesa=0, inMenu=False):
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

    if not inMenu:
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


def guardaVideo(listaImg, audio, loop):
    if GlobalHWVar.mouseBloccato:
        GlobalHWVar.configuraCursore(False)
    bottoneDown = False

    # play video
    countdownInizioVideo = 10
    continua = False
    i = 0
    while i < len(listaImg) and not continua:
        if countdownInizioVideo == 0:
            if audio and i == 0:
                GlobalHWVar.canaleSoundCanzone.play(audio)
            GlobalHWVar.disegnaImmagineSuSchermo(listaImg[i], (0, 0))
            GlobalHWVar.aggiornaSchermo()

        # gestione degli input
        bottoneDown, inutile = GestioneInput.getInput(bottoneDown, False)
        if bottoneDown:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
            continua = True
            bottoneDown = False

        pygame.event.pump()
        GlobalHWVar.clockVideo.tick(GlobalHWVar.fpsVideo)
        if countdownInizioVideo > 0:
            countdownInizioVideo -= 1
        else:
            i += 1
            if loop and i == len(listaImg):
                i = 0

    # oscura lo schermo
    # oscuraIlluminaSchermo(illumina=False)


def trovacasattaccabili(x, y, raggio, caseviste):
    if raggio == -1:
        rangeXSinistra = (x // GlobalHWVar.gpx) - 2
        rangeXDestra = (GlobalHWVar.gsx // GlobalHWVar.gpx) - (x // GlobalHWVar.gpx) - 3
        rangeYAlto = (y // GlobalHWVar.gpy) - 2
        rangeYBasso = (GlobalHWVar.gsy // GlobalHWVar.gpy) - (y // GlobalHWVar.gpy) - 3
    else:
        rangeXSinistra = raggio // GlobalHWVar.gpx
        if (x // GlobalHWVar.gpx) - rangeXSinistra < 2:
            rangeXSinistra = (x // GlobalHWVar.gpx) - 2
        rangeXDestra = raggio // GlobalHWVar.gpx
        if (x // GlobalHWVar.gpx) + rangeXDestra > 30:
            rangeXDestra = (GlobalHWVar.gsx // GlobalHWVar.gpx) - (x // GlobalHWVar.gpx) - 3
        rangeYAlto = raggio // GlobalHWVar.gpy
        if (y // GlobalHWVar.gpy) - rangeYAlto < 2:
            rangeYAlto = (y // GlobalHWVar.gpy) - 2
        rangeYBasso = raggio // GlobalHWVar.gpy
        if (y // GlobalHWVar.gpy) + rangeYBasso > 16:
            rangeYBasso = (GlobalHWVar.gsy // GlobalHWVar.gpy) - (y // GlobalHWVar.gpy) - 3

    # il vettore caseattac contiene solo le caselle nel raggio visivo
    caseattac = []
    i = 0
    while i < len(caseviste):
        if caseviste[i] <= x + (rangeXDestra * GlobalHWVar.gpx) and caseviste[i] >= x - (rangeXSinistra * GlobalHWVar.gpx) and caseviste[i + 1] <= y + (rangeYBasso * GlobalHWVar.gpy) and caseviste[i + 1] >= y - (rangeYAlto * GlobalHWVar.gpy):
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
            caseattacbassodestra.append(x + (GlobalHWVar.gpx * n))
            caseattacbassodestra.append(y + (GlobalHWVar.gpy * m))
            caseattacbassodestra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacbassodestra[2] = False
    i = 0
    while i < len(caseattac):
        if caseattac[i] > x and caseattac[i] <= x + (rangeXDestra * GlobalHWVar.gpx) and caseattac[i + 1] > y and caseattac[i + 1] <= y + (rangeYBasso * GlobalHWVar.gpy) and not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a destra dell'ostacolo
            xInizioRetta = (x + (GlobalHWVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalHWVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalHWVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalHWVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalHWVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalHWVar.gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacbassodestra):
                if caseattacbassodestra[j] == caseattac[i] and caseattacbassodestra[j + 1] == caseattac[i + 1]:
                    caseattacbassodestra[j + 2] = False
                elif caseattacbassodestra[j + 2]:
                    xLatoSinistroCasella = caseattacbassodestra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacbassodestra[j] + GlobalHWVar.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacbassodestra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacbassodestra[j + 1] + GlobalHWVar.gpy
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
                                latoSinistro = GlobalHWVar.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalHWVar.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalHWVar.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalHWVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoDestro != 0:
                                area = (GlobalHWVar.gpx * GlobalHWVar.gpy) - ((GlobalHWVar.gpx - latoSuperiore) * (GlobalHWVar.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalHWVar.gpx * GlobalHWVar.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalHWVar.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalHWVar.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalHWVar.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalHWVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoSinistro != 0:
                                area = (GlobalHWVar.gpx * GlobalHWVar.gpy) - ((GlobalHWVar.gpx - latoInferiore) * (GlobalHWVar.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalHWVar.gpx * GlobalHWVar.gpy / 2.0) + margineDiErrore:
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
            caseattacbassosinistra.append(x - (GlobalHWVar.gpx * n))
            caseattacbassosinistra.append(y + (GlobalHWVar.gpy * m))
            caseattacbassosinistra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacbassosinistra[2] = False
    i = 0
    while i < len(caseattac):
        if caseattac[i] < x and caseattac[i] >= x - (rangeXSinistra * GlobalHWVar.gpx) and caseattac[i + 1] > y and caseattac[i + 1] <= y + (rangeYBasso * GlobalHWVar.gpy) and not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalHWVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalHWVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = - deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (GlobalHWVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalHWVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalHWVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalHWVar.gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = - deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacbassosinistra):
                if caseattacbassosinistra[j] == caseattac[i] and caseattacbassosinistra[j + 1] == caseattac[i + 1]:
                    caseattacbassosinistra[j + 2] = False
                elif caseattacbassosinistra[j + 2]:
                    xLatoSinistroCasella = caseattacbassosinistra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacbassosinistra[j] + GlobalHWVar.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacbassosinistra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacbassosinistra[j + 1] + GlobalHWVar.gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacbassosinistra[j + 2] and yLatoSuperioreCasella >= caseattac[i + 1] and xLatoDestroCasella <= caseattac[i] + GlobalHWVar.gpx:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = GlobalHWVar.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalHWVar.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalHWVar.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalHWVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoSinistro != 0:
                                area = (GlobalHWVar.gpx * GlobalHWVar.gpy) - ((GlobalHWVar.gpx - latoSuperiore) * (GlobalHWVar.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalHWVar.gpx * GlobalHWVar.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalHWVar.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalHWVar.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalHWVar.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalHWVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoDestro != 0:
                                area = (GlobalHWVar.gpx * GlobalHWVar.gpy) - ((GlobalHWVar.gpx - latoInferiore) * (GlobalHWVar.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalHWVar.gpx * GlobalHWVar.gpy / 2.0) + margineDiErrore:
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
            caseattacaltosinistra.append(x - (GlobalHWVar.gpx * n))
            caseattacaltosinistra.append(y - (GlobalHWVar.gpy * m))
            caseattacaltosinistra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacaltosinistra[2] = False
    i = 0
    while i < len(caseattac):
        if caseattac[i] < x and caseattac[i] >= x - (rangeXSinistra * GlobalHWVar.gpx) and caseattac[i + 1] < y and caseattac[i + 1] >= y - (rangeYAlto * GlobalHWVar.gpy) and not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a destra dell'ostacolo
            xInizioRetta = (x + (GlobalHWVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalHWVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalHWVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalHWVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalHWVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalHWVar.gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacaltosinistra):
                if caseattacaltosinistra[j] == caseattac[i] and caseattacaltosinistra[j + 1] == caseattac[i + 1]:
                    caseattacaltosinistra[j + 2] = False
                elif caseattacaltosinistra[j + 2]:
                    xLatoSinistroCasella = caseattacaltosinistra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacaltosinistra[j] + GlobalHWVar.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacaltosinistra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacaltosinistra[j + 1] + GlobalHWVar.gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacaltosinistra[j + 2] and yLatoInferioreCasella <= caseattac[i + 1] + GlobalHWVar.gpy and xLatoDestroCasella <= caseattac[i] + GlobalHWVar.gpx:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = GlobalHWVar.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalHWVar.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalHWVar.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalHWVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoDestro != 0:
                                area = (GlobalHWVar.gpx * GlobalHWVar.gpy) - ((GlobalHWVar.gpx - latoSuperiore) * (GlobalHWVar.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalHWVar.gpx * GlobalHWVar.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalHWVar.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalHWVar.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalHWVar.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalHWVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoSinistro != 0:
                                area = (GlobalHWVar.gpx * GlobalHWVar.gpy) - ((GlobalHWVar.gpx - latoInferiore) * (GlobalHWVar.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalHWVar.gpx * GlobalHWVar.gpy / 2.0) + margineDiErrore:
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
            caseattacaltodestra.append(x + (GlobalHWVar.gpx * n))
            caseattacaltodestra.append(y - (GlobalHWVar.gpy * m))
            caseattacaltodestra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacaltodestra[2] = False
    i = 0
    while i < len(caseattac):
        if caseattac[i] > x and caseattac[i] <= x + (rangeXDestra * GlobalHWVar.gpx) and caseattac[i + 1] < y and caseattac[i + 1] >= y - (rangeYAlto * GlobalHWVar.gpy) and not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalHWVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalHWVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = - deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (GlobalHWVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalHWVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalHWVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalHWVar.gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = - deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacaltodestra):
                if caseattacaltodestra[j] == caseattac[i] and caseattacaltodestra[j + 1] == caseattac[i + 1]:
                    caseattacaltodestra[j + 2] = False
                elif caseattacaltodestra[j + 2]:
                    xLatoSinistroCasella = caseattacaltodestra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacaltodestra[j] + GlobalHWVar.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacaltodestra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacaltodestra[j + 1] + GlobalHWVar.gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacaltodestra[j + 2] and yLatoInferioreCasella <= caseattac[i + 1] + GlobalHWVar.gpy and xLatoSinistroCasella >= caseattac[i]:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = GlobalHWVar.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalHWVar.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalHWVar.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalHWVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoSinistro != 0:
                                area = (GlobalHWVar.gpx * GlobalHWVar.gpy) - ((GlobalHWVar.gpx - latoSuperiore) * (GlobalHWVar.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalHWVar.gpx * GlobalHWVar.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalHWVar.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalHWVar.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalHWVar.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalHWVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoDestro != 0:
                                area = (GlobalHWVar.gpx * GlobalHWVar.gpy) - ((GlobalHWVar.gpx - latoInferiore) * (GlobalHWVar.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalHWVar.gpx * GlobalHWVar.gpy / 2.0) + margineDiErrore:
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
            caseattacdestra.append(x + (GlobalHWVar.gpx * n))
            caseattacdestra.append(y - (GlobalHWVar.gpy * m))
            caseattacdestra.append(True)
            m = m + 1
        m = 1
        while m <= rangeYBasso:
            caseattacdestra.append(x + (GlobalHWVar.gpx * n))
            caseattacdestra.append(y + (GlobalHWVar.gpy * m))
            caseattacdestra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacdestra[2] = False
    i = 0
    while i < len(caseattac):
        if caseattac[i] > x and caseattac[i] <= x + (rangeXDestra * GlobalHWVar.gpx) and caseattac[i + 1] == y and not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalHWVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalHWVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = - deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalHWVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalHWVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalHWVar.gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacdestra):
                if caseattacdestra[j] == caseattac[i] and caseattacdestra[j + 1] == caseattac[i + 1]:
                    caseattacdestra[j + 2] = False
                elif caseattacdestra[j + 2]:
                    xLatoSinistroCasella = caseattacdestra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacdestra[j] + GlobalHWVar.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacdestra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacdestra[j + 1] + GlobalHWVar.gpy
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
                                latoSinistro = GlobalHWVar.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalHWVar.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalHWVar.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalHWVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoSinistro != 0:
                                area = (GlobalHWVar.gpx * GlobalHWVar.gpy) - ((GlobalHWVar.gpx - latoSuperiore) * (GlobalHWVar.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalHWVar.gpx * GlobalHWVar.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalHWVar.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalHWVar.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalHWVar.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta2LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalHWVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoSinistro != 0:
                                area = (GlobalHWVar.gpx * GlobalHWVar.gpy) - ((GlobalHWVar.gpx - latoInferiore) * (GlobalHWVar.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalHWVar.gpx * GlobalHWVar.gpy / 2.0) + margineDiErrore:
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
            caseattacsinistra.append(x - (GlobalHWVar.gpx * n))
            caseattacsinistra.append(y - (GlobalHWVar.gpy * m))
            caseattacsinistra.append(True)
            m = m + 1
        m = 1
        while m <= rangeYBasso:
            caseattacsinistra.append(x - (GlobalHWVar.gpx * n))
            caseattacsinistra.append(y + (GlobalHWVar.gpy * m))
            caseattacsinistra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacsinistra[2] = False
    i = 0
    while i < len(caseattac):
        if caseattac[i] < x and caseattac[i] >= x - (rangeXSinistra * GlobalHWVar.gpx) and caseattac[i + 1] == y and not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a destra dell'ostacolo
            xInizioRetta = (x + (GlobalHWVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalHWVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalHWVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (GlobalHWVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalHWVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalHWVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalHWVar.gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = - deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacsinistra):
                if caseattacsinistra[j] == caseattac[i] and caseattacsinistra[j + 1] == caseattac[i + 1]:
                    caseattacsinistra[j + 2] = False
                elif caseattacsinistra[j + 2]:
                    xLatoSinistroCasella = caseattacsinistra[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacsinistra[j] + GlobalHWVar.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacsinistra[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacsinistra[j + 1] + GlobalHWVar.gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacsinistra[j + 2] and xLatoDestroCasella <= caseattac[i] + GlobalHWVar.gpx:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta1
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoSinistroCasella < yLatoSuperioreCasella:
                                latoSinistro = GlobalHWVar.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalHWVar.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalHWVar.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta1LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalHWVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoDestro != 0:
                                area = (GlobalHWVar.gpx * GlobalHWVar.gpy) - ((GlobalHWVar.gpx - latoSuperiore) * (GlobalHWVar.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalHWVar.gpx * GlobalHWVar.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalHWVar.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalHWVar.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalHWVar.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalHWVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoDestro != 0:
                                area = (GlobalHWVar.gpx * GlobalHWVar.gpy) - ((GlobalHWVar.gpx - latoInferiore) * (GlobalHWVar.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalHWVar.gpx * GlobalHWVar.gpy / 2.0) + margineDiErrore:
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
            caseattacalto.append(x + (GlobalHWVar.gpx * m))
            caseattacalto.append(y - (GlobalHWVar.gpy * n))
            caseattacalto.append(True)
            m = m + 1
        m = 1
        while m <= rangeXSinistra:
            caseattacalto.append(x - (GlobalHWVar.gpx * m))
            caseattacalto.append(y - (GlobalHWVar.gpy * n))
            caseattacalto.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacalto[2] = False
    i = 0
    while i < len(caseattac):
        if caseattac[i] == x and caseattac[i + 1] < y and caseattac[i + 1] >= y - (rangeYAlto * GlobalHWVar.gpy) and not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalHWVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalHWVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalHWVar.gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (GlobalHWVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalHWVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalHWVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalHWVar.gpy
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = - deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacalto):
                if caseattacalto[j] == caseattac[i] and caseattacalto[j + 1] == caseattac[i + 1]:
                    caseattacalto[j + 2] = False
                elif caseattacalto[j + 2]:
                    xLatoSinistroCasella = caseattacalto[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacalto[j] + GlobalHWVar.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacalto[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacalto[j + 1] + GlobalHWVar.gpy
                    xRetta1LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoInferioreCasella = (yLatoInferioreCasella - altezzaRetta2) / float(coeffAngolare2)

                    if caseattacalto[j + 2] and yLatoInferioreCasella <= caseattac[i + 1] + GlobalHWVar.gpy:
                        if (yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella) or (yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella) or (xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella) or (xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella):
                            # trovo le misure dei lati interni delle caselle intersecate dalla retta2
                            latoSuperiore = 0
                            latoInferiore = 0
                            latoDestro = 0
                            latoSinistro = 0
                            if yLatoSuperioreCasella <= yRetta1LatoSinistroCasella <= yLatoInferioreCasella:
                                latoSinistro = abs(yRetta1LatoSinistroCasella - yLatoSuperioreCasella)
                            elif yRetta1LatoSinistroCasella > yLatoInferioreCasella:
                                latoSinistro = GlobalHWVar.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta1LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalHWVar.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalHWVar.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalHWVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoSinistro != 0:
                                area = (GlobalHWVar.gpx * GlobalHWVar.gpy) - ((GlobalHWVar.gpx - latoInferiore) * (GlobalHWVar.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalHWVar.gpx * GlobalHWVar.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalHWVar.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoSuperioreCasella)
                            elif yRetta2LatoDestroCasella > yLatoInferioreCasella:
                                latoDestro = GlobalHWVar.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalHWVar.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalHWVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta2
                            if latoInferiore != 0 and latoDestro != 0:
                                area = (GlobalHWVar.gpx * GlobalHWVar.gpy) - ((GlobalHWVar.gpx - latoInferiore) * (GlobalHWVar.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalHWVar.gpx * GlobalHWVar.gpy / 2.0) + margineDiErrore:
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
            caseattacbasso.append(x + (GlobalHWVar.gpx * m))
            caseattacbasso.append(y + (GlobalHWVar.gpy * n))
            caseattacbasso.append(True)
            m = m + 1
        m = 1
        while m <= rangeXSinistra:
            caseattacbasso.append(x - (GlobalHWVar.gpx * m))
            caseattacbasso.append(y + (GlobalHWVar.gpy * n))
            caseattacbasso.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacbasso[2] = False
    i = 0
    while i < len(caseattac):
        if caseattac[i] == x and caseattac[i + 1] > y and caseattac[i + 1] <= y + (rangeYBasso * GlobalHWVar.gpy) and not caseattac[i + 2]:
            # la prima retta va dal personaggio all'angolo in alto a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalHWVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalHWVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare1 = - deltaYRetta / deltaXRetta
            altezzaRetta1 = yInizioRetta - (xInizioRetta * coeffAngolare1)
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in alto a destra dell'ostacolo
            xInizioRetta = (x + (GlobalHWVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalHWVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalHWVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1]
            deltaYRetta = abs(yInizioRetta - yFineRetta)
            coeffAngolare2 = deltaYRetta / deltaXRetta
            altezzaRetta2 = yInizioRetta - (xInizioRetta * coeffAngolare2)
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            j = 0
            while j < len(caseattacbasso):
                if caseattacbasso[j] == caseattac[i] and caseattacbasso[j + 1] == caseattac[i + 1]:
                    caseattacbasso[j + 2] = False
                elif caseattacbasso[j + 2]:
                    xLatoSinistroCasella = caseattacbasso[j]
                    yRetta1LatoSinistroCasella = (coeffAngolare1 * xLatoSinistroCasella) + altezzaRetta1
                    yRetta2LatoSinistroCasella = (coeffAngolare2 * xLatoSinistroCasella) + altezzaRetta2
                    xLatoDestroCasella = caseattacbasso[j] + GlobalHWVar.gpx
                    yRetta1LatoDestroCasella = (coeffAngolare1 * xLatoDestroCasella) + altezzaRetta1
                    yRetta2LatoDestroCasella = (coeffAngolare2 * xLatoDestroCasella) + altezzaRetta2
                    yLatoSuperioreCasella = caseattacbasso[j + 1]
                    xRetta1LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta1) / float(coeffAngolare1)
                    xRetta2LatoSuperioreCasella = (yLatoSuperioreCasella - altezzaRetta2) / float(coeffAngolare2)
                    yLatoInferioreCasella = caseattacbasso[j + 1] + GlobalHWVar.gpy
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
                                latoSinistro = GlobalHWVar.gpy
                            if yLatoSuperioreCasella <= yRetta1LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta1LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta1LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalHWVar.gpy
                            if xLatoSinistroCasella <= xRetta1LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta1LatoSuperioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoSuperioreCasella < xLatoSinistroCasella:
                                latoSuperiore = GlobalHWVar.gpx
                            if xLatoSinistroCasella <= xRetta1LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta1LatoInferioreCasella - xLatoDestroCasella)
                            elif xRetta1LatoInferioreCasella < xLatoSinistroCasella:
                                latoInferiore = GlobalHWVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoSinistro != 0:
                                area = (GlobalHWVar.gpx * GlobalHWVar.gpy) - ((GlobalHWVar.gpx - latoSuperiore) * (GlobalHWVar.gpy - latoSinistro) / 2.0)
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
                            if area > (GlobalHWVar.gpx * GlobalHWVar.gpy / 2.0) + margineDiErrore:
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
                                latoSinistro = GlobalHWVar.gpy
                            if yLatoSuperioreCasella <= yRetta2LatoDestroCasella <= yLatoInferioreCasella:
                                latoDestro = abs(yRetta2LatoDestroCasella - yLatoInferioreCasella)
                            elif yRetta2LatoDestroCasella < yLatoSuperioreCasella:
                                latoDestro = GlobalHWVar.gpy
                            if xLatoSinistroCasella <= xRetta2LatoSuperioreCasella <= xLatoDestroCasella:
                                latoSuperiore = abs(xRetta2LatoSuperioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoSuperioreCasella > xLatoDestroCasella:
                                latoSuperiore = GlobalHWVar.gpx
                            if xLatoSinistroCasella <= xRetta2LatoInferioreCasella <= xLatoDestroCasella:
                                latoInferiore = abs(xRetta2LatoInferioreCasella - xLatoSinistroCasella)
                            elif xRetta2LatoInferioreCasella > xLatoDestroCasella:
                                latoInferiore = GlobalHWVar.gpx
                            # calcolo la parte di area interna di ogni casella intersecata dalla retta1
                            if latoSuperiore != 0 and latoDestro != 0:
                                area = (GlobalHWVar.gpx * GlobalHWVar.gpy) - ((GlobalHWVar.gpx - latoSuperiore) * (GlobalHWVar.gpy - latoDestro) / 2.0)
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
                            if area > (GlobalHWVar.gpx * GlobalHWVar.gpy / 2.0) + margineDiErrore:
                                caseattacbasso[j + 2] = False
                        elif (yLatoSuperioreCasella > yRetta1LatoSinistroCasella and xLatoSinistroCasella > xRetta1LatoSuperioreCasella) and (yLatoSuperioreCasella > yRetta2LatoDestroCasella and xLatoDestroCasella < xRetta2LatoSuperioreCasella):
                            caseattacbasso[j + 2] = False

                j += 3
        i += 3

    caseattactot = caseattacaltodestra + caseattacaltosinistra + caseattacbassodestra + caseattacbassosinistra + caseattacdestra + caseattacsinistra + caseattacalto + caseattacbasso

    # aggiungo le caselle dei bordi
    i = 0
    while i < 32:
        if raggio == -1 or (raggio != -1 and (GlobalHWVar.gpx * i <= x + raggio and 0 <= y + raggio) and (GlobalHWVar.gpx * i >= x - raggio and 0 >= y - raggio)):
            caseattactot.append(GlobalHWVar.gpx * i)
            caseattactot.append(0)
            caseattactot.append(False)
        if raggio == -1 or (raggio != -1 and (GlobalHWVar.gpx * i <= x + raggio and GlobalHWVar.gpy <= y + raggio) and (GlobalHWVar.gpx * i >= x - raggio and GlobalHWVar.gpy >= y - raggio)):
            caseattactot.append(GlobalHWVar.gpx * i)
            caseattactot.append(GlobalHWVar.gpy)
            caseattactot.append(False)
        if raggio == -1 or (raggio != -1 and (GlobalHWVar.gpx * i <= x + raggio and GlobalHWVar.gpy * 16 <= y + raggio) and (GlobalHWVar.gpx * i >= x - raggio and GlobalHWVar.gpy * 16 >= y - raggio)):
            caseattactot.append(GlobalHWVar.gpx * i)
            caseattactot.append(GlobalHWVar.gpy * 16)
            caseattactot.append(False)
        if raggio == -1 or (raggio != -1 and (GlobalHWVar.gpx * i <= x + raggio and GlobalHWVar.gpy * 17 <= y + raggio) and (GlobalHWVar.gpx * i >= x - raggio and GlobalHWVar.gpy * 17 >= y - raggio)):
            caseattactot.append(GlobalHWVar.gpx * i)
            caseattactot.append(GlobalHWVar.gpy * 17)
            caseattactot.append(False)
        i += 1
    i = 2
    while i < 16:
        if raggio == -1 or (raggio != -1 and (0 <= x + raggio and GlobalHWVar.gpy * i <= y + raggio) and (0 >= x - raggio and GlobalHWVar.gpy * i >= y - raggio)):
            caseattactot.append(0)
            caseattactot.append(GlobalHWVar.gpy * i)
            caseattactot.append(False)
        if raggio == -1 or (raggio != -1 and (GlobalHWVar.gpx <= x + raggio and GlobalHWVar.gpy * i <= y + raggio) and (GlobalHWVar.gpx >= x - raggio and GlobalHWVar.gpy * i >= y - raggio)):
            caseattactot.append(GlobalHWVar.gpx)
            caseattactot.append(GlobalHWVar.gpy * i)
            caseattactot.append(False)
        if raggio == -1 or (raggio != -1 and (GlobalHWVar.gpx * 30 <= x + raggio and GlobalHWVar.gpy * i <= y + raggio) and (GlobalHWVar.gpx * 30 >= x - raggio and GlobalHWVar.gpy * i >= y - raggio)):
            caseattactot.append(GlobalHWVar.gpx * 30)
            caseattactot.append(GlobalHWVar.gpy * i)
            caseattactot.append(False)
        if raggio == -1 or (raggio != -1 and (GlobalHWVar.gpx * 31 <= x + raggio and GlobalHWVar.gpy * i <= y + raggio) and (GlobalHWVar.gpx * 31 >= x - raggio and GlobalHWVar.gpy * i >= y - raggio)):
            caseattactot.append(GlobalHWVar.gpx * 31)
            caseattactot.append(GlobalHWVar.gpy * i)
            caseattactot.append(False)
        i += 1

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


def scopriCaselleViste(x, y, rx, ry, numstanza, porte, cofanetti, avanzamentoStoria, escludiOggettiBassi=False, vetPartenze=False):
    escludiPorte = True

    # caseviste[x, y, flag, ... ] -> riempito come se non vedessi niente
    caseviste = []
    n = 0
    while n <= 29:
        m = 0
        while m <= 15:
            caseviste.append(GlobalHWVar.gpx + (GlobalHWVar.gpx * n))
            caseviste.append(GlobalHWVar.gpy + (GlobalHWVar.gpy * m))
            caseviste.append(False)
            m = m + 1
        n = n + 1

    # contiene x e y delle caselle già esplorate
    caselleEsplorate = [x, y]
    # caselle viste da rallo
    j = 0
    while j < len(caselleEsplorate):
        nx, ny, stanza, carim, cambiosta = SetOstacoliContenutoCofanetti.controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -GlobalHWVar.gpy, numstanza, False, porte, cofanetti, avanzamentoStoria, escludiPorte, escludiOggettiBassi)
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
        nx, ny, stanza, carim, cambiosta = SetOstacoliContenutoCofanetti.controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], 0, GlobalHWVar.gpy, numstanza, False, porte, cofanetti, avanzamentoStoria, escludiPorte, escludiOggettiBassi)
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
        nx, ny, stanza, carim, cambiosta = SetOstacoliContenutoCofanetti.controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], -GlobalHWVar.gpx, 0, numstanza, False, porte, cofanetti, avanzamentoStoria, escludiPorte, escludiOggettiBassi)
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
        nx, ny, stanza, carim, cambiosta = SetOstacoliContenutoCofanetti.controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], GlobalHWVar.gpx, 0, numstanza, False, porte, cofanetti, avanzamentoStoria, escludiPorte, escludiOggettiBassi)
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
    incasevistaColco = False
    i = 0
    while i < len(caseviste):
        if caseviste[i] == rx and caseviste[i + 1] == ry:
            if caseviste[i + 2]:
                incasevistaColco = True
            break
        i = i + 3
    if not incasevistaColco and GlobalHWVar.gsx // 32 * 2 <= rx <= GlobalHWVar.gsx // 32 * 29 and GlobalHWVar.gsy // 18 * 2 <= ry <= GlobalHWVar.gsy // 18 * 15:
        caselleEsplorate = [rx, ry]
        j = 0
        while j < len(caselleEsplorate):
            nx, ny, stanza, carim, cambiosta = SetOstacoliContenutoCofanetti.controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -GlobalHWVar.gpy, numstanza, False, porte, cofanetti, avanzamentoStoria, escludiPorte, escludiOggettiBassi)
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
            nx, ny, stanza, carim, cambiosta = SetOstacoliContenutoCofanetti.controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], 0, GlobalHWVar.gpy, numstanza, False, porte, cofanetti, avanzamentoStoria, escludiPorte, escludiOggettiBassi)
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
            nx, ny, stanza, carim, cambiosta = SetOstacoliContenutoCofanetti.controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], -GlobalHWVar.gpx, 0, numstanza, False, porte, cofanetti, avanzamentoStoria, escludiPorte, escludiOggettiBassi)
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
            nx, ny, stanza, carim, cambiosta = SetOstacoliContenutoCofanetti.controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], GlobalHWVar.gpx, 0, numstanza, False, porte, cofanetti, avanzamentoStoria, escludiPorte, escludiOggettiBassi)
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

    # scopro le caselle del vettore vetPartenze se non sono in caselle già viste
    if not vetPartenze:
        vetPartenze = []
    if len(vetPartenze) > 0:
        contatoreVetPartenze = 0
        while contatoreVetPartenze < len(vetPartenze):
            incasevista = False
            i = 0
            while i < len(caseviste):
                if caseviste[i] == vetPartenze[contatoreVetPartenze] and caseviste[i + 1] == vetPartenze[contatoreVetPartenze + 1]:
                    if caseviste[i + 2]:
                        incasevista = True
                    break
                i += 3
            if not incasevista:
                caselleEsplorate = [vetPartenze[contatoreVetPartenze], vetPartenze[contatoreVetPartenze + 1]]
                j = 0
                while j < len(caselleEsplorate):
                    nx, ny, stanza, carim, cambiosta = SetOstacoliContenutoCofanetti.controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -GlobalHWVar.gpy, numstanza, False, porte, cofanetti, avanzamentoStoria, escludiPorte, escludiOggettiBassi)
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
                    nx, ny, stanza, carim, cambiosta = SetOstacoliContenutoCofanetti.controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], 0, GlobalHWVar.gpy, numstanza, False, porte, cofanetti, avanzamentoStoria, escludiPorte, escludiOggettiBassi)
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
                    nx, ny, stanza, carim, cambiosta = SetOstacoliContenutoCofanetti.controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], -GlobalHWVar.gpx, 0, numstanza, False, porte, cofanetti, avanzamentoStoria, escludiPorte, escludiOggettiBassi)
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
                    nx, ny, stanza, carim, cambiosta = SetOstacoliContenutoCofanetti.controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], GlobalHWVar.gpx, 0, numstanza, False, porte, cofanetti, avanzamentoStoria, escludiPorte, escludiOggettiBassi)
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
            contatoreVetPartenze += 5

    return caseviste, incasevistaColco


def pathFinding(xPartenza, yPartenza, xArrivo, yArrivo, vetOstacoli, caseviste):
    # caselleEsplorate contiene x, y e valore delle caselle già esplorate (il valore serve per trovare il percorso più breve)
    valoreCasella = 0
    caselleEsplorate = [xPartenza, yPartenza, valoreCasella]
    percorsoTrovato = []

    impossibileRaggiungere = False
    if (xPartenza == xArrivo and yPartenza == yArrivo + GlobalHWVar.gpy) or (xPartenza == xArrivo and yPartenza == yArrivo - GlobalHWVar.gpy) or (xPartenza == xArrivo + GlobalHWVar.gpx and yPartenza == yArrivo) or (xPartenza == xArrivo and yPartenza - GlobalHWVar.gpx == yArrivo):
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
                if (caselleLibere[i] == caselleEsplorate[j] + GlobalHWVar.gpx and caselleLibere[i + 1] == caselleEsplorate[j + 1]) or (caselleLibere[i] == caselleEsplorate[j] - GlobalHWVar.gpx and caselleLibere[i + 1] == caselleEsplorate[j + 1]) or (caselleLibere[i] == caselleEsplorate[j] and caselleLibere[i + 1] == caselleEsplorate[j + 1] + GlobalHWVar.gpy) or (caselleLibere[i] == caselleEsplorate[j] and caselleLibere[i + 1] == caselleEsplorate[j + 1] - GlobalHWVar.gpy):
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
                    if (xCasellaAttuale == xCasellaAccanto + GlobalHWVar.gpx and yCasellaAttuale == yCasellaAccanto) or (xCasellaAttuale == xCasellaAccanto - GlobalHWVar.gpx and yCasellaAttuale == yCasellaAccanto) or (xCasellaAttuale == xCasellaAccanto and yCasellaAttuale == yCasellaAccanto + GlobalHWVar.gpy) or (xCasellaAttuale == xCasellaAccanto and yCasellaAttuale == yCasellaAccanto - GlobalHWVar.gpy):
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


def controllaMorteRallo(vitaRallo, inizio, gameover):
    if vitaRallo <= 0:
        gameover = True
        if GlobalHWVar.mouseBloccato:
            GlobalHWVar.configuraCursore(False)
        GlobalHWVar.canaleSoundPuntatoreSposta.stop()
        GlobalHWVar.canaleSoundPuntatoreSeleziona.stop()
        GlobalHWVar.canaleSoundPassiRallo.stop()
        GlobalHWVar.canaleSoundPassiColco.stop()
        GlobalHWVar.canaleSoundPassiNemiciPersonaggi.stop()
        GlobalHWVar.canaleSoundMorteNemici.stop()
        GlobalHWVar.canaleSoundLvUp.stop()
        GlobalHWVar.canaleSoundInterazioni.stop()
        GlobalHWVar.canaleSoundAttacco.stop()
        i = GlobalHWVar.volumeCanzoni
        j = GlobalHWVar.volumeEffetti
        while i > 0 or j > 0:
            GlobalHWVar.canaleSoundCanzone.set_volume(i)
            GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(j)
            i -= GlobalHWVar.volumeCanzoni / 10
            j -= GlobalHWVar.volumeEffetti / 10
            pygame.time.wait(30)
        GlobalHWVar.canaleSoundCanzone.stop()
        GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
        GlobalHWVar.canaleSoundSottofondoAmbientale.stop()
        GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti)

        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreMorte)
        oscuraIlluminaSchermo(illumina=False, tipoOscuramento=2)

        # GlobalVarG2.disegnaColoreSuTuttoLoSchermo(GlobalVarG2.grigioscu)
        messaggio("Sei morto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 13, 150)
        GlobalHWVar.aggiornaSchermo()

        bottoneDown = False
        continua = False
        while not continua:
            # gestione degli input
            bottoneDown, inutile = GestioneInput.getInput(bottoneDown, False)
            if bottoneDown:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                continua = True
                bottoneDown = False

            pygame.event.pump()
            GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
        inizio = True

    return inizio, gameover


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
            GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persdmbAttacco, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
        if npers == 2:
            GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persambAttacco, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x - GlobalHWVar.gpx, y))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
        if npers == 3:
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y - GlobalHWVar.gpy))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perswmbAttacco, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
        if npers == 4:
            GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssmbAttacco, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
    else:
        if npers == 1:
            GlobalHWVar.disegnaImmagineSuSchermo(scudo, (x, y))
            if inMovimento:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persdm, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y))
            if attaccoRavvicinato:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persdmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persdmb1, (x, y))
                elif frame == 2:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persdmb2, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persdb, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arma, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
        if npers == 2:
            if attaccoRavvicinato:
                GlobalHWVar.disegnaImmagineSuSchermo(arma, (x - GlobalHWVar.gpx, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(arma, (x, y))
            if inMovimento:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persam, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y))
            if attaccoRavvicinato:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persambAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persamb1, (x, y))
                elif frame == 2:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persamb2, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persab, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(scudo, (x, y))
        if npers == 3:
            if attaccoRavvicinato:
                GlobalHWVar.disegnaImmagineSuSchermo(arma, (x, y - GlobalHWVar.gpy))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(arma, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(scudo, (x, y))
            if attaccoRavvicinato:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perswmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perswmb1, (x, y))
                elif frame == 2:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perswmb2, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perswb, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
            if inMovimento:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perswm, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y))
        if npers == 4:
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            if inMovimento:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssm, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            if attaccoRavvicinato:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssmb1, (x, y))
                elif frame == 2:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssmb2, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssb, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arma, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(scudo, (x, y))


def dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi):
    GlobalHWVar.canaleSoundPassiRallo.stop()
    oggettoRicevuto = False
    menuMercante = False
    sceltaEffettuata = 0
    voceMarcata = 1
    puntatoreSpostato = False
    puntatore = GlobalImgVar.puntatore
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
        imgPersDialogo = GlobalImgVar.imgDialogoLucy1
        nomePersonaggio = "Lucy"
    elif GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
        imgPersDialogo = GlobalImgVar.imgDialogoFraMaggiore
        nomePersonaggio = "Hans"
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
        imgPersDialogo = GlobalImgVar.imgDialogoLucy1
        nomePersonaggio = "Lucy"
    else:
        imgPersDialogo = GlobalImgVar.imgDialogoLucy2
        nomePersonaggio = "Lucy"

    if personaggio.nome != "Tutorial":
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersDialogo, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 3.5))
    if personaggio.nome != "Tutorial" and personaggio.nome != "Nessuno":
        GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgDialogo, (GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 3.5))
    schermo_prima_del_dialogo = GlobalHWVar.schermo.copy().convert()
    background = schermo_prima_del_dialogo.subsurface(pygame.Rect(0, 0, GlobalHWVar.gsx, GlobalHWVar.gsy)).convert()
    dark = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
    dark.fill((0, 0, 0, 150))
    background.blit(dark, (0, 0))
    GlobalHWVar.disegnaImmagineSuSchermo(background, (0, 0))

    schermo_prima_del_dialogo = GlobalHWVar.schermo.copy().convert()
    background = schermo_prima_del_dialogo.subsurface(pygame.Rect(0, GlobalHWVar.gsy // 18 * 3.5, GlobalHWVar.gsx, GlobalHWVar.gsy // 18 * 14.5)).convert()

    primoframe = True
    numeroMessaggiTotali = len(personaggio.partiDialogo)
    numeromessaggioAttuale = 0
    prosegui = True
    fineDialogo = False

    aggiornaInterfacciaPerCambioInput = True
    bottoneDown = False

    GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni / 2)
    GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti / 2)
    while not fineDialogo:
        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        if GlobalHWVar.mouseVisibile:
            if numeromessaggioAttuale < len(personaggio.partiDialogo) and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                if GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 15.1 <= yMouse <= GlobalHWVar.gsy // 18 * 16.2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 1
                elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 16.2 <= yMouse <= GlobalHWVar.gsy // 18 * 17.3:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 2
                elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 31 and GlobalHWVar.gsy // 18 * 15.1 <= yMouse <= GlobalHWVar.gsy // 18 * 16.2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 3
                elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 31 and GlobalHWVar.gsy // 18 * 16.2 <= yMouse <= GlobalHWVar.gsy // 18 * 17.3:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 4
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            else:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
            if voceMarcataVecchia != voceMarcata and not primoframe:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
        primoframe = False

        # gestione degli input
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            fineDialogo = True
            bottoneDown = False
        if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
            puntatoreSpostato = True
            prosegui = True
            if voceMarcata != 1 and voceMarcata != 3:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                voceMarcata -= 1
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
            puntatoreSpostato = True
            prosegui = True
            if voceMarcata != 1 and voceMarcata != 2:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                voceMarcata -= 2
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
            puntatoreSpostato = True
            prosegui = True
            if voceMarcata != 2 and voceMarcata != 4:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                voceMarcata += 1
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
            puntatoreSpostato = True
            prosegui = True
            if voceMarcata != 3 and voceMarcata != 4:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                voceMarcata += 2
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        elif bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
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
                if personaggio.avanzaColDialogo:
                    personaggio.avanzamentoDialogo += 1
                    personaggio.avanzaColDialogo = False
                    i = 0
                    while i < len(listaAvanzamentoDialoghi):
                        if personaggio.tipo == listaAvanzamentoDialoghi[i]:
                            listaAvanzamentoDialoghi[i + 1] = personaggio.avanzamentoDialogo
                            break
                        i += 2
                fineDialogo = True
            else:
                if personaggio.scelta and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                    sceltaEffettuata = voceMarcata
                prosegui = True
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if bottoneDown:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False

        if (prosegui or aggiornaInterfacciaPerCambioInput) and not fineDialogo:
            if aggiornaInterfacciaPerCambioInput and numeromessaggioAttuale != 0:
                numeromessaggioAttuale -= 1
                aggiornaInterfacciaPerCambioInput = False
            if puntatoreSpostato:
                numeromessaggioAttuale -= 1
                puntatoreSpostato = False
            GlobalHWVar.disegnaImmagineSuSchermo(background, (0, GlobalHWVar.gsy // 18 * 3.5))
            if personaggio.nome != "Tutorial":
                if personaggio.partiDialogo[numeromessaggioAttuale][0] == "personaggio" and personaggio.nome != "Nessuno":
                    GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgDialogo, (GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 3.5))
                if personaggio.partiDialogo[numeromessaggioAttuale][0] == "tu" or personaggio.partiDialogo[numeromessaggioAttuale][1] == "???DOMANDA???":
                    GlobalHWVar.disegnaImmagineSuSchermo(imgPersDialogo, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 3.5))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoDialoghi, (0, GlobalHWVar.gsy * 2 // 3))
            if personaggio.partiDialogo[numeromessaggioAttuale][0] == "personaggio":
                messaggio(personaggio.nome + ":", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 4 // 5), 80)
            elif personaggio.partiDialogo[numeromessaggioAttuale][0] == "tu":
                messaggio(nomePersonaggio + ":", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 4 // 5), 80)
            if personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][sceltaEffettuata + 1], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3), 50)
            elif personaggio.partiDialogo[numeromessaggioAttuale][1] == "???DOMANDA???":
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][2], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3), 50)
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][3], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 1.2), 50)
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][4], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 2.2), 50)
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][5], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 1.2), 50)
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][6], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 2.2), 50)
                if voceMarcata == 1:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (GlobalHWVar.gsx // 32 * 1, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 1.2)))
                if voceMarcata == 2:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (GlobalHWVar.gsx // 32 * 1, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 2.2)))
                if voceMarcata == 3:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (GlobalHWVar.gsx // 32 * 16, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 1.2)))
                if voceMarcata == 4:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (GlobalHWVar.gsx // 32 * 16, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 2.2)))
            else:
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][1], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3), 50, GlobalHWVar.gpx * 30, GlobalHWVar.gpy * 4 // 5)
            numeromessaggioAttuale += 1
            prosegui = False
            GlobalHWVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
    GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti)

    return avanzamentoStoria, oggettoRicevuto, menuMercante, listaAvanzamentoDialoghi


def animaOggettoSpecialeRicevuto(oggettoRicevuto):
    if GlobalHWVar.mouseBloccato:
        GlobalHWVar.configuraCursore(False)
    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoRaccoltaMonete)
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfocontcof, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 0))
    messaggio("Hai ottenuto: " + oggettoRicevuto, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
    GlobalHWVar.aggiornaSchermo()
    bottoneDown = False
    risposta = False
    while not risposta:
        # gestione degli input
        bottoneDown, inutile = GestioneInput.getInput(bottoneDown, False)
        if bottoneDown == pygame.K_SPACE or bottoneDown == "mouseSinistro" or bottoneDown == "padCroce":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
            risposta = True
            bottoneDown = False
        if bottoneDown:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False

        pygame.event.pump()
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def cambiaProtagonista(nome):
    GlobalImgVar.persw = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.perswb = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.persa = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.persab = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.perso = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    GlobalImgVar.perss = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.persob = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1b.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    GlobalImgVar.perssb = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.persd = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.persdb = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.perssm = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.perssmb1 = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.perssmb2 = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.persdm = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.persdmb1 = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.persdmb2 = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.persam = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.persamb1 = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.persamb2 = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.perswm = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.perswmb1 = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.perswmb2 = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.perswmbAttacco = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.persambAttacco = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.perssmbAttacco = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.persdmbAttacco = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.persmbDifesa = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/PersonaggiomovbDifesa.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    GlobalImgVar.persAvvele = GlobalImgVar.loadImage('Immagini/Personaggi/' + nome + '/PersonaggioAvvelenato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)


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
                if (personaggio.x + GlobalHWVar.gpx == caseviste[i] and personaggio.y == caseviste[i + 1]) or (personaggio.x - GlobalHWVar.gpx == caseviste[i] and personaggio.y == caseviste[i + 1]) or (personaggio.x == caseviste[i] and personaggio.y + GlobalHWVar.gpy == caseviste[i + 1]) or (personaggio.x == caseviste[i] and personaggio.y - GlobalHWVar.gpy == caseviste[i + 1]):
                    if caseviste[i + 2]:
                        personaggio.vicinoACasellaVista = True
                        break
                i += 3

    return listaNemici, listaPersonaggi


def scorriObbiettiviInquadrati(avanzamentoStoria, nemicoInquadrato, listaNemiciVisti, listaEscheViste, scorriAvanti):
    obbiettivoRichiesto = False
    trovatoNemicoDaInquadrare = False

    if scorriAvanti:
        if not nemicoInquadrato and avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"]:
            obbiettivoRichiesto = "Colco"
        elif not nemicoInquadrato and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoColco"]:
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
                if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"]:
                    nemicoInquadrato = "Colco"
                    trovatoNemicoDaInquadrare = True
                else:
                    obbiettivoRichiesto = "NemicoIniziale"
            cicliDisponibili -= 1
    else:
        if not nemicoInquadrato and avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"]:
            obbiettivoRichiesto = "Colco"
        elif not nemicoInquadrato and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoColco"]:
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
                if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"]:
                    nemicoInquadrato = "Colco"
                    trovatoNemicoDaInquadrare = True
                else:
                    obbiettivoRichiesto = "EscaFinale"
            cicliDisponibili -= 1

    if trovatoNemicoDaInquadrare:
        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selObbiettivo)
    else:
        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
    return nemicoInquadrato


def creaTuttiIVettoriPerLeCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, avanzamentoStoria):
    # scoprire caselle viste
    caseviste, colcoInCasellaVista = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, avanzamentoStoria)
    # scoprire caselle viste solo da Rallo
    if not colcoInCasellaVista and GlobalHWVar.gsx // 32 * 2 <= rx <= GlobalHWVar.gsx // 32 * 29 and GlobalHWVar.gsy // 18 * 2 <= ry <= GlobalHWVar.gsy // 18 * 15:
        casevisteDaRallo, colcoInCasellaVista = scopriCaselleViste(x, y, -1, -1, stanza, porte, cofanetti, avanzamentoStoria)
    else:
        casevisteDaRallo = caseviste[:]

    # casellePercorribili include solo le caselle su cui si può camminare
    casellePercorribili = caseviste[:]
    # sistemo il vettore delle caselle percorribili: togliendo le caselle non viste e scoprendo le caselle delle porte vicine a caselle viste
    i = 0
    while i < len(casellePercorribili):
        if not casellePercorribili[i + 2]:
            del casellePercorribili[i + 2]
            del casellePercorribili[i + 1]
            del casellePercorribili[i]
        else:
            del casellePercorribili[i + 2]
            i += 2
    i = 0
    while i < len(porte):
        if not porte[i + 3]:
            j = 0
            while j < len(casellePercorribili):
                if casellePercorribili[j] - GlobalHWVar.gpx <= porte[i + 1] <= casellePercorribili[j] + GlobalHWVar.gpx and casellePercorribili[j + 1] - GlobalHWVar.gpy <= porte[i + 2] <= casellePercorribili[j + 1] + GlobalHWVar.gpy:
                    casellePercorribili.append(porte[i + 1])
                    casellePercorribili.append(porte[i + 2])
                    break
                j += 2
        i += 4

    # casevisteEntrateIncluse include anche le entrate della stanza
    casevisteEntrateIncluse = caseviste[:]
    vetEntrate = SetOstacoliContenutoCofanetti.getEntrateStanze(stanza, avanzamentoStoria)
    i = 0
    while i < len(vetEntrate):
        j = 0
        while j < len(casevisteEntrateIncluse):
            if vetEntrate[i] == casevisteEntrateIncluse[j] and vetEntrate[i + 1] == casevisteEntrateIncluse[j + 1]:
                if casevisteEntrateIncluse[j + 2]:
                    k = 0
                    while k < len(casevisteEntrateIncluse):
                        if vetEntrate[i] + vetEntrate[i + 2] == casevisteEntrateIncluse[k] and vetEntrate[i + 1] + vetEntrate[i + 3] == casevisteEntrateIncluse[k + 1]:
                            casevisteEntrateIncluse[k + 2] = True
                            break
                        k += 3
                break
            j += 3
        i += 5

    # il vettore delle caselle non visibili serve per tenere conto degli "oggetti bassi"
    caselleNonVisibili, colcoInCasellaVista = scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, avanzamentoStoria, escludiOggettiBassi=True)
    i = 0
    while i < 32:
        caselleNonVisibili.append(GlobalHWVar.gpx * i)
        caselleNonVisibili.append(0)
        caselleNonVisibili.append(False)
        caselleNonVisibili.append(GlobalHWVar.gpx * i)
        caselleNonVisibili.append(GlobalHWVar.gpy * 17)
        caselleNonVisibili.append(False)
        i += 1
    i = 1
    while i < 17:
        caselleNonVisibili.append(0)
        caselleNonVisibili.append(GlobalHWVar.gpx * i)
        caselleNonVisibili.append(False)
        caselleNonVisibili.append(GlobalHWVar.gpx * 31)
        caselleNonVisibili.append(GlobalHWVar.gpy * i)
        caselleNonVisibili.append(False)
        i += 1

    return caseviste, casevisteDaRallo, casevisteEntrateIncluse, caselleNonVisibili, casellePercorribili


def disegnaOmbreggiaturaNellaCasellaSpecifica(x, y, casellaChiara, casellaScura):
    if ((x / GlobalHWVar.gpx) + (y / GlobalHWVar.gpy)) % 2 == 0:
        GlobalHWVar.disegnaImmagineSuSchermo(casellaChiara, (x, y))
    if ((x / GlobalHWVar.gpx) + (y / GlobalHWVar.gpy)) % 2 == 1:
        GlobalHWVar.disegnaImmagineSuSchermo(casellaScura, (x, y))


def oscuraIlluminaSchermo(illumina, tipoOscuramento=1):
    # se "screen" è False oscura lo schermo
    if not illumina:
        rect = pygame.display.get_surface().get_rect()
        image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
        if tipoOscuramento == 1:
            image.fill((0, 0, 0, 100))
            image = image.convert_alpha(GlobalHWVar.schermo)
            i = 0
            while i <= 5:
                GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
                GlobalHWVar.aggiornaSchermo()
                pygame.event.pump()
                GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                i += 1
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.nero)
            GlobalHWVar.aggiornaSchermo()
        elif tipoOscuramento == 2:
            image.fill((0, 0, 0, 8))
            image = image.convert_alpha(GlobalHWVar.schermo)
            i = 0
            while i <= 30:
                if i % 2 == 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
                    GlobalHWVar.aggiornaSchermo()
                pygame.event.pump()
                GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                i += 1
        elif tipoOscuramento == 3:
            image.fill((0, 0, 0, 100))
            image = image.convert_alpha(GlobalHWVar.schermo)
            i = 0
            while i <= 3:
                GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
                GlobalHWVar.aggiornaSchermo()
                pygame.event.pump()
                GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                i += 1
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.nero)
            GlobalHWVar.aggiornaSchermo()
    else:
        screen = GlobalHWVar.schermo.copy().convert()
        rect = pygame.display.get_surface().get_rect()
        vetImg = []
        if illumina == 1:
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 200))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 150))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 100))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 50))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            i = 0
            while i <= 3:
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(vetImg[i], (0, 0))
                GlobalHWVar.aggiornaSchermo()
                pygame.event.pump()
                GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                i += 1
        elif illumina == 2:
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 250))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 200))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 150))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 100))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 60))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 20))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            i = 0
            while i <= 5:
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(vetImg[i], (0, 0))
                GlobalHWVar.aggiornaSchermo()
                pygame.event.pump()
                GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                i += 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        GlobalHWVar.aggiornaSchermo()


def copiaNemico(oggettoNemico, checkErrori=False):
    copia = copy.deepcopy(oggettoNemico)
    if oggettoNemico and not checkErrori:
        copia.caricaImg()
        copia.girati(copia.direzione)

    return copia


def copiaPersonaggio(oggettoPersonaggio, avanzamentoStoria, checkErrori=False):
    copia = copy.deepcopy(oggettoPersonaggio)
    if copia.tipo != "Tutorial" and copia.tipo != "Nessuno" and not checkErrori:
        if copia.tipo.startswith("Oggetto"):
            copia.caricaImgOggetto()
            copia.aggiornaImgOggetto(avanzamentoStoria, True)
        else:
            copia.caricaImgPersonaggio()
            copia.girati(copia.direzione)

    return copia


def copiaListaDiOggettiConImmagini(listaOggetti, nemici, avanzamentoStoria=0, checkErrori=False):
    copiaLista = []
    if nemici:
        for oggetto in listaOggetti:
            copiaLista.append(copiaNemico(oggetto, checkErrori=checkErrori))
    else:
        for oggetto in listaOggetti:
            copiaLista.append(copiaPersonaggio(oggetto, avanzamentoStoria, checkErrori=checkErrori))

    return copiaLista


'''# linea(dove,colore,inizio,fine,spessore)
GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, verde, (0, 0), (GlobalVarG2.gsx, GlobalVarG2.gsy), 10)
# cerchio(dove,colore,centro,raggio,spessore)
pygame.draw.circle(GlobalVarG2.schermo, blu, (300, 100), 5)
# rettangolo(dove,colore,(x,y,larghezza,altezza),spessore)
GlobalVar.disegnaRettangoloSuSchermo(GlobalVarG2.schermo, rosso, (200, 100, 30, 40), 5)'''
