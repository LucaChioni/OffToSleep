# -*- coding: utf-8 -*-

import random
from GestioneInput import *
from SetOstacoliContenutoCofanetti import *


def messaggio(msg, colore, x, y, gr, largezzaFoglio=-1, spazioTraLeRighe=-1, daDestra=False, centrale=False, lungMax=False):
    x = int(x)
    y = int(y)

    gr = gr - 10
    gr = GlobalVar.gpx * gr // 60
    y = y - (GlobalVar.gpy // 8)
    carattere = "Liberation Serif"
    font = pygame.font.SysFont(carattere, gr)
    coloreOrig = colore
    xOrig = x

    testoComplesso = False
    if "<*>" in msg or "<br>" in msg or largezzaFoglio != -1 or spazioTraLeRighe != -1:
        testoComplesso = True

    # per mettere parti in italic, bold o colorate: "Premi <*>#bold#un<*> <*>#italic#tasto<*> per <*>#color#100,0,0#continuare<*>..."
    if daDestra:
        testo = font.render(msg, True, colore)
        dimX, dimY = font.size(msg)
        GlobalVar.disegnaImmagineSuSchermo(testo, (x - dimX, y))
    elif centrale:
        msgIniziale = msg
        font.render(msg, True, colore)
        dimX, dimY = font.size(msg)
        if lungMax and dimX > lungMax * GlobalVar.gpx:
            while dimX > lungMax * GlobalVar.gpx:
                msg = msg[:-1]
                font.render(msg + "...", True, colore)
                dimX, dimY = font.size(msg)
        if msgIniziale != msg:
            msg += "..."
        testo = font.render(msg, True, colore)
        dimX, dimY = font.size(msg)
        GlobalVar.disegnaImmagineSuSchermo(testo, (x - (dimX // 2), y))
    elif testoComplesso:
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
                        GlobalVar.disegnaImmagineSuSchermo(testo, (x, y))
                        x += dimX
    else:
        testo = font.render(msg, True, colore)
        GlobalVar.disegnaImmagineSuSchermo(testo, (x, y))


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
    if GlobalVar.mouseBloccato:
        GlobalVar.configuraCursore(False)
    GlobalVar.disegnaColoreSuTuttoLoSchermo(GlobalVar.grigioscu)
    oscuraIlluminaSchermo(illumina=2)
    GlobalVar.aggiornaSchermo()
    bottoneDown = False

    # play video
    countdownInizioVideo = 10
    continua = False
    i = 0
    while i < len(listaImg) and not continua:
        if countdownInizioVideo == 0:
            if i == 0:
                GlobalVar.canaleSoundSottofondoAmbientale.play(audio)
            GlobalVar.disegnaImmagineSuSchermo(listaImg[i], (0, 0))
            GlobalVar.aggiornaSchermo()

        # gestione degli input
        bottoneDown, inutile = getInput(bottoneDown, False)
        if bottoneDown:
            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
            continua = True
            bottoneDown = False

        pygame.event.pump()
        GlobalVar.clockVideo.tick(GlobalVar.fpsVideo)
        if countdownInizioVideo > 0:
            countdownInizioVideo -= 1
        else:
            i += 1
            if loop and i == len(listaImg):
                i = 0

    # oscura lo schermo
    oscuraIlluminaSchermo(illumina=False)
    i = GlobalVar.volumeEffetti
    while i > 0:
        GlobalVar.canaleSoundSottofondoAmbientale.set_volume(i)
        i -= GlobalVar.volumeEffetti / 10
        pygame.time.wait(30)
    GlobalVar.canaleSoundSottofondoAmbientale.stop()
    GlobalVar.canaleSoundSottofondoAmbientale.set_volume(GlobalVar.volumeEffetti)


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
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVar.gpy
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
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVar.gpy
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
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVar.gpy
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
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVar.gpy
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
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a sinistra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i]
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVar.gpy
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
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVar.gpy
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
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in basso a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
            yFineRetta = caseattac[i + 1] + GlobalVar.gpy
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
            #GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, rosso, (xInizioRetta, yInizioRetta), (xFineRetta, yFineRetta), 1)
            # la seconda retta va dal personaggio all'angolo in alto a destra dell'ostacolo
            xInizioRetta = (x + (GlobalVar.gpx / 2.0))
            xFineRetta = caseattac[i] + GlobalVar.gpx
            deltaXRetta = abs(xInizioRetta - xFineRetta)
            yInizioRetta = (y + (GlobalVar.gpy / 2.0))
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


def scopriCaselleViste(x, y, rx, ry, vetPartenze, numstanza, porte, cofanetti, escludiPorte=True):
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

    # contiene x e y delle caselle già esplorate
    caselleEsplorate = [x, y]
    # caselle viste da rallo
    j = 0
    while j < len(caselleEsplorate):
        nx, ny, stanza, carim, cambiosta = controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -GlobalVar.gpy, numstanza, False, escludiPorte, porte, cofanetti)
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
        nx, ny, stanza, carim, cambiosta = controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], 0, GlobalVar.gpy, numstanza, False, escludiPorte, porte, cofanetti)
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
        nx, ny, stanza, carim, cambiosta = controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], -GlobalVar.gpx, 0, numstanza, False, escludiPorte, porte, cofanetti)
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
        nx, ny, stanza, carim, cambiosta = controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], GlobalVar.gpx, 0, numstanza, False, escludiPorte, porte, cofanetti)
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
    if not incasevista and GlobalVar.gsx // 32 * 2 <= rx <= GlobalVar.gsx // 32 * 29 and GlobalVar.gsy // 18 * 2 <= ry <= GlobalVar.gsy // 18 * 15:
        caselleEsplorate = [rx, ry]
        j = 0
        while j < len(caselleEsplorate):
            nx, ny, stanza, carim, cambiosta = controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -GlobalVar.gpy, numstanza, False, escludiPorte, porte, cofanetti)
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
            nx, ny, stanza, carim, cambiosta = controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], 0, GlobalVar.gpy, numstanza, False, escludiPorte, porte, cofanetti)
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
            nx, ny, stanza, carim, cambiosta = controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], -GlobalVar.gpx, 0, numstanza, False, escludiPorte, porte, cofanetti)
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
            nx, ny, stanza, carim, cambiosta = controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], GlobalVar.gpx, 0, numstanza, False, escludiPorte, porte, cofanetti)
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
                    nx, ny, stanza, carim, cambiosta = controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -GlobalVar.gpy, numstanza, False, escludiPorte, porte, cofanetti)
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
                    nx, ny, stanza, carim, cambiosta = controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], 0, GlobalVar.gpy, numstanza, False, escludiPorte, porte, cofanetti)
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
                    nx, ny, stanza, carim, cambiosta = controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], -GlobalVar.gpx, 0, numstanza, False, escludiPorte, porte, cofanetti)
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
                    nx, ny, stanza, carim, cambiosta = controlloOstacoli(caselleEsplorate[j], caselleEsplorate[j + 1], GlobalVar.gpx, 0, numstanza, False, escludiPorte, porte, cofanetti)
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


def controllaMorteRallo(vitaRallo, inizio, gameover):
    if vitaRallo <= 0:
        gameover = True
        if GlobalVar.mouseBloccato:
            GlobalVar.configuraCursore(False)
        GlobalVar.canaleSoundPuntatoreSposta.stop()
        GlobalVar.canaleSoundPuntatoreSeleziona.stop()
        GlobalVar.canaleSoundPassiRallo.stop()
        GlobalVar.canaleSoundPassiColco.stop()
        GlobalVar.canaleSoundPassiNemiciPersonaggi.stop()
        GlobalVar.canaleSoundMorteNemici.stop()
        GlobalVar.canaleSoundLvUp.stop()
        GlobalVar.canaleSoundInterazioni.stop()
        GlobalVar.canaleSoundAttacco.stop()
        i = GlobalVar.volumeCanzoni
        j = GlobalVar.volumeEffetti
        while i > 0 or j > 0:
            GlobalVar.canaleSoundCanzone.set_volume(i)
            GlobalVar.canaleSoundSottofondoAmbientale.set_volume(j)
            i -= GlobalVar.volumeCanzoni / 10
            j -= GlobalVar.volumeEffetti / 10
            pygame.time.wait(30)
        GlobalVar.canaleSoundCanzone.stop()
        GlobalVar.canaleSoundCanzone.set_volume(GlobalVar.volumeCanzoni)
        GlobalVar.canaleSoundSottofondoAmbientale.stop()
        GlobalVar.canaleSoundSottofondoAmbientale.set_volume(GlobalVar.volumeEffetti)

        GlobalVar.canaleSoundInterazioni.play(GlobalVar.rumoreMorte)
        oscuraIlluminaSchermo(illumina=False, tipoOscuramento=2)

        # GlobalVarG2.disegnaColoreSuTuttoLoSchermo(GlobalVarG2.grigioscu)
        messaggio("Sei morto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 13, 150)
        GlobalVar.aggiornaSchermo()

        bottoneDown = False
        continua = False
        while not continua:
            # gestione degli input
            bottoneDown, inutile = getInput(bottoneDown, False)
            if bottoneDown:
                GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selind)
                continua = True
                bottoneDown = False
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
            GlobalVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persAvvele, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persdmbAttacco, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(arco, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(guanti, (x, y))
        if npers == 2:
            GlobalVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persAvvele, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persambAttacco, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(arco, (x - GlobalVar.gpx, y))
            GlobalVar.disegnaImmagineSuSchermo(guanti, (x, y))
        if npers == 3:
            GlobalVar.disegnaImmagineSuSchermo(arco, (x, y - GlobalVar.gpy))
            GlobalVar.disegnaImmagineSuSchermo(GlobalVar.perswmbAttacco, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(guanti, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persAvvele, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(faretra, (x, y))
        if npers == 4:
            GlobalVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persAvvele, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(GlobalVar.perssmbAttacco, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(arco, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(guanti, (x, y))
    else:
        if npers == 1:
            GlobalVar.disegnaImmagineSuSchermo(scudo, (x, y))
            if inMovimento:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persdm, (x, y))
            else:
                GlobalVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persAvvele, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(arco, (x, y))
            if attaccoRavvicinato:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persdmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persdmb1, (x, y))
                elif frame == 2:
                    GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persdmb2, (x, y))
            else:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persdb, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(arma, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(guanti, (x, y))
        if npers == 2:
            if attaccoRavvicinato:
                GlobalVar.disegnaImmagineSuSchermo(arma, (x - GlobalVar.gpx, y))
            else:
                GlobalVar.disegnaImmagineSuSchermo(arma, (x, y))
            if inMovimento:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persam, (x, y))
            else:
                GlobalVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persAvvele, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(arco, (x, y))
            if attaccoRavvicinato:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persambAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persamb1, (x, y))
                elif frame == 2:
                    GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persamb2, (x, y))
            else:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persab, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(guanti, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(scudo, (x, y))
        if npers == 3:
            if attaccoRavvicinato:
                GlobalVar.disegnaImmagineSuSchermo(arma, (x, y - GlobalVar.gpy))
            else:
                GlobalVar.disegnaImmagineSuSchermo(arma, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(scudo, (x, y))
            if attaccoRavvicinato:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.perswmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalVar.disegnaImmagineSuSchermo(GlobalVar.perswmb1, (x, y))
                elif frame == 2:
                    GlobalVar.disegnaImmagineSuSchermo(GlobalVar.perswmb2, (x, y))
            else:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.perswb, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(guanti, (x, y))
            if inMovimento:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.perswm, (x, y))
            else:
                GlobalVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persAvvele, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(arco, (x, y))
        if npers == 4:
            GlobalVar.disegnaImmagineSuSchermo(arco, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(faretra, (x, y))
            if inMovimento:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.perssm, (x, y))
            else:
                GlobalVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.persAvvele, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(collana, (x, y))
            if attaccoRavvicinato:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.perssmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalVar.disegnaImmagineSuSchermo(GlobalVar.perssmb1, (x, y))
                elif frame == 2:
                    GlobalVar.disegnaImmagineSuSchermo(GlobalVar.perssmb2, (x, y))
            else:
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.perssb, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(arma, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(guanti, (x, y))
            GlobalVar.disegnaImmagineSuSchermo(scudo, (x, y))


def dialoga(avanzamentoStoria, personaggio):
    GlobalVar.canaleSoundPassiRallo.stop()
    oggettoRicevuto = False
    menuMercante = False
    sceltaEffettuata = 0
    voceMarcata = 1
    puntatoreSpostato = False
    puntatore = GlobalVar.puntatore
    if GlobalVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
        imgPersDialogo = GlobalVar.imgDialogoFraMaggiore
        nomePersonaggio = "Sam"
    else:
        imgPersDialogo = GlobalVar.imgDialogoSara
        nomePersonaggio = "Sara"

    if personaggio.nome != "Tutorial":
        GlobalVar.disegnaImmagineSuSchermo(imgPersDialogo, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 3.5))
    if personaggio.nome != "Tutorial" and personaggio.nome != "Nessuno":
        GlobalVar.disegnaImmagineSuSchermo(personaggio.imgDialogo, (GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 3.5))
    schermo_prima_del_dialogo = GlobalVar.schermo.copy().convert()
    background = schermo_prima_del_dialogo.subsurface(pygame.Rect(0, 0, GlobalVar.gsx, GlobalVar.gsy))
    dark = pygame.Surface((GlobalVar.gsx, GlobalVar.gsy), flags=pygame.SRCALPHA)
    dark.fill((0, 0, 0, 150))
    background.blit(dark, (0, 0))
    GlobalVar.disegnaImmagineSuSchermo(background, (0, 0))

    schermo_prima_del_dialogo = GlobalVar.schermo.copy().convert()
    background = schermo_prima_del_dialogo.subsurface(pygame.Rect(0, GlobalVar.gsy // 18 * 3.5, GlobalVar.gsx, GlobalVar.gsy // 18 * 14.5))

    primoframe = True
    numeroMessaggiTotali = len(personaggio.partiDialogo)
    numeromessaggioAttuale = 0
    prosegui = True
    fineDialogo = False

    aggiornaInterfacciaPerCambioInput = True
    bottoneDown = False

    GlobalVar.canaleSoundCanzone.set_volume(GlobalVar.volumeCanzoni / 2)
    GlobalVar.canaleSoundSottofondoAmbientale.set_volume(GlobalVar.volumeEffetti / 2)
    while not fineDialogo:
        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
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
                aggiornaInterfacciaPerCambioInput = True
                GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
        primoframe = False

        # gestione degli input
        bottoneDown, aggiornaInterfacciaPerCambioInput = getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selind)
            fineDialogo = True
            bottoneDown = False
        if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
            puntatoreSpostato = True
            prosegui = True
            if voceMarcata != 1 and voceMarcata != 3:
                GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                voceMarcata -= 1
            else:
                GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
            bottoneDown = False
        if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
            puntatoreSpostato = True
            prosegui = True
            if voceMarcata != 1 and voceMarcata != 2:
                GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                voceMarcata -= 2
            else:
                GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
            bottoneDown = False
        if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
            puntatoreSpostato = True
            prosegui = True
            if voceMarcata != 2 and voceMarcata != 4:
                GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                voceMarcata += 1
            else:
                GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
            bottoneDown = False
        if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
            puntatoreSpostato = True
            prosegui = True
            if voceMarcata != 3 and voceMarcata != 4:
                GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                voceMarcata += 2
            else:
                GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
            bottoneDown = False
        elif bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalVar.mouseBloccato) or bottoneDown == "padCroce":
            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
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
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalVar.mouseBloccato:
            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
            bottoneDown = False
        if bottoneDown:
            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
            bottoneDown = False

        if (prosegui or aggiornaInterfacciaPerCambioInput) and not fineDialogo:
            if aggiornaInterfacciaPerCambioInput and numeromessaggioAttuale != 0:
                numeromessaggioAttuale -= 1
                aggiornaInterfacciaPerCambioInput = False
            if puntatoreSpostato:
                numeromessaggioAttuale -= 1
                puntatoreSpostato = False
            GlobalVar.disegnaImmagineSuSchermo(background, (0, GlobalVar.gsy // 18 * 3.5))
            if personaggio.nome != "Tutorial":
                if personaggio.partiDialogo[numeromessaggioAttuale][0] == "personaggio" and personaggio.nome != "Nessuno":
                    GlobalVar.disegnaImmagineSuSchermo(personaggio.imgDialogo, (GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 3.5))
                if personaggio.partiDialogo[numeromessaggioAttuale][0] == "tu" or personaggio.partiDialogo[numeromessaggioAttuale][1] == "???DOMANDA???":
                    GlobalVar.disegnaImmagineSuSchermo(imgPersDialogo, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 3.5))
            GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoDialoghi, (0, GlobalVar.gsy * 2 // 3))
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
                if voceMarcata == 1:
                    GlobalVar.disegnaImmagineSuSchermo(puntatore, (GlobalVar.gsx // 32 * 1, ((GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3)) + int(GlobalVar.gpy * 1.2)))
                if voceMarcata == 2:
                    GlobalVar.disegnaImmagineSuSchermo(puntatore, (GlobalVar.gsx // 32 * 1, ((GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3)) + int(GlobalVar.gpy * 2.2)))
                if voceMarcata == 3:
                    GlobalVar.disegnaImmagineSuSchermo(puntatore, (GlobalVar.gsx // 32 * 16, ((GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3)) + int(GlobalVar.gpy * 1.2)))
                if voceMarcata == 4:
                    GlobalVar.disegnaImmagineSuSchermo(puntatore, (GlobalVar.gsx // 32 * 16, ((GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3)) + int(GlobalVar.gpy * 2.2)))
            else:
                messaggio(personaggio.partiDialogo[numeromessaggioAttuale][1], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, (GlobalVar.gsy * 2 // 3) + (GlobalVar.gpy * 7 // 3), 50, GlobalVar.gpx * 30, GlobalVar.gpy * 4 // 5)
            numeromessaggioAttuale += 1
            prosegui = False
            GlobalVar.aggiornaSchermo()
    GlobalVar.canaleSoundCanzone.set_volume(GlobalVar.volumeCanzoni)
    GlobalVar.canaleSoundSottofondoAmbientale.set_volume(GlobalVar.volumeEffetti)

    return avanzamentoStoria, oggettoRicevuto, menuMercante


def animaOggettoSpecialeRicevuto(oggettoRicevuto):
    if GlobalVar.mouseBloccato:
        GlobalVar.configuraCursore(False)
    GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoRaccoltaMonete)
    GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfocontcof, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 0))
    messaggio("Hai ottenuto: " + oggettoRicevuto, GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
    GlobalVar.aggiornaSchermo()
    bottoneDown = False
    risposta = False
    while not risposta:
        # gestione degli input
        bottoneDown, inutile = getInput(bottoneDown, False)
        if bottoneDown == pygame.K_SPACE or bottoneDown == "mouseSinistro" or bottoneDown == "padCroce":
            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
            risposta = True
            bottoneDown = False
        if bottoneDown:
            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
            bottoneDown = False


def cambiaProtagonista(nome):
    GlobalVar.persw = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.perswb = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4b.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.persa = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.persab = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3b.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.perso = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1.png', GlobalVar.gpx * 5, GlobalVar.gpy * 5, True)
    GlobalVar.perss = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.persob = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1b.png', GlobalVar.gpx * 5, GlobalVar.gpy * 5, True)
    GlobalVar.perssb = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1b.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.persd = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.persdb = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2b.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.perssm = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1mov.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.perssmb1 = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1movb1.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.perssmb2 = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1movb2.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.persdm = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2mov.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.persdmb1 = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2movb1.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.persdmb2 = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2movb2.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.persam = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3mov.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.persamb1 = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3movb1.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.persamb2 = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3movb2.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.perswm = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4mov.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.perswmb1 = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4movb1.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.perswmb2 = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4movb2.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.perswmbAttacco = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio4movbAttacco.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.persambAttacco = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio3movbAttacco.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.perssmbAttacco = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio1movbAttacco.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.persdmbAttacco = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/Personaggio2movbAttacco.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.persmbDifesa = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/PersonaggiomovbDifesa.png', GlobalVar.gpx, GlobalVar.gpy, True)
    GlobalVar.persAvvele = GlobalVar.loadImage('Immagini/Personaggi/' + nome + '/PersonaggioAvvelenato.png', GlobalVar.gpx, GlobalVar.gpy, True)


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
        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selObbiettivo)
    else:
        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
    return nemicoInquadrato


def creaTuttiIVettoriPerLeCaselleViste(x, y, rx, ry, stanza, porte, cofanetti):
    # scoprire caselle viste
    caseviste = scopriCaselleViste(x, y, rx, ry, [], stanza, porte, cofanetti)
    # scoprire caselle viste solo da Rallo
    casevisteDaRallo = scopriCaselleViste(x, y, -1, -1, [], stanza, porte, cofanetti)
    # casevisteEntrateIncluse include anche le entrate della stanza
    casevisteEntrateIncluse = scopriCaselleViste(x, y, rx, ry, [], stanza, porte, cofanetti, False)
    # casellePercorribili include solo le caselle su cui si può camminare
    vetPartenze = getEntrateStanze(stanza)
    casellePercorribili = scopriCaselleViste(x, y, rx, ry, vetPartenze, stanza, [], [])

    # sistemo il vettore delle caselle percorribili: togliendo le caselle-ostacolo, coprendo le caselle non viste, scoprendo le caselle delle porte vicine a caselle viste
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

    return caseviste, casevisteDaRallo, casevisteEntrateIncluse, casellePercorribili


def disegnaOmbreggiaturaNellaCasellaSpecifica(x, y, casellaChiara, casellaScura):
    if ((x / GlobalVar.gpx) + (y / GlobalVar.gpy)) % 2 == 0:
        GlobalVar.disegnaImmagineSuSchermo(casellaChiara, (x, y))
    if ((x / GlobalVar.gpx) + (y / GlobalVar.gpy)) % 2 == 1:
        GlobalVar.disegnaImmagineSuSchermo(casellaScura, (x, y))


def oscuraIlluminaSchermo(illumina, tipoOscuramento=1):
    # se "screen" è False oscura lo schermo
    if not illumina:
        rect = pygame.display.get_surface().get_rect()
        image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
        if tipoOscuramento == 1:
            image.fill((0, 0, 0, 100))
            image = image.convert_alpha(GlobalVar.schermo)
            i = 0
            while i <= 5:
                GlobalVar.disegnaImmagineSuSchermo(image, (0, 0))
                GlobalVar.aggiornaSchermo()
                pygame.event.pump()
                GlobalVar.clockFadeToBlack.tick(GlobalVar.fpsFadeToBlack)
                i += 1
            GlobalVar.disegnaColoreSuTuttoLoSchermo(GlobalVar.nero)
            GlobalVar.aggiornaSchermo()
        elif tipoOscuramento == 2:
            image.fill((0, 0, 0, 5))
            image = image.convert_alpha(GlobalVar.schermo)
            i = 0
            while i <= 35:
                GlobalVar.disegnaImmagineSuSchermo(image, (0, 0))
                GlobalVar.aggiornaSchermo()
                pygame.event.pump()
                GlobalVar.clockFadeToBlack.tick(GlobalVar.fpsFadeToBlack)
                i += 1
        elif tipoOscuramento == 3:
            image.fill((0, 0, 0, 100))
            image = image.convert_alpha(GlobalVar.schermo)
            i = 0
            while i <= 3:
                GlobalVar.disegnaImmagineSuSchermo(image, (0, 0))
                GlobalVar.aggiornaSchermo()
                pygame.event.pump()
                GlobalVar.clockFadeToBlack.tick(GlobalVar.fpsFadeToBlack)
                i += 1
            GlobalVar.disegnaColoreSuTuttoLoSchermo(GlobalVar.nero)
            GlobalVar.aggiornaSchermo()
    else:
        screen = GlobalVar.schermo.copy().convert()
        rect = pygame.display.get_surface().get_rect()
        vetImg = []
        if illumina == 1:
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 200))
            vetImg.append(image.convert_alpha(GlobalVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 150))
            vetImg.append(image.convert_alpha(GlobalVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 100))
            vetImg.append(image.convert_alpha(GlobalVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 50))
            vetImg.append(image.convert_alpha(GlobalVar.schermo))
            i = 0
            while i <= 3:
                GlobalVar.disegnaImmagineSuSchermo(screen, (0, 0))
                GlobalVar.disegnaImmagineSuSchermo(vetImg[i], (0, 0))
                GlobalVar.aggiornaSchermo()
                pygame.event.pump()
                GlobalVar.clockFadeToBlack.tick(GlobalVar.fpsFadeToBlack)
                i += 1
        elif illumina == 2:
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 250))
            vetImg.append(image.convert_alpha(GlobalVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 200))
            vetImg.append(image.convert_alpha(GlobalVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 150))
            vetImg.append(image.convert_alpha(GlobalVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 100))
            vetImg.append(image.convert_alpha(GlobalVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 60))
            vetImg.append(image.convert_alpha(GlobalVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 20))
            vetImg.append(image.convert_alpha(GlobalVar.schermo))
            i = 0
            while i <= 5:
                GlobalVar.disegnaImmagineSuSchermo(screen, (0, 0))
                GlobalVar.disegnaImmagineSuSchermo(vetImg[i], (0, 0))
                GlobalVar.aggiornaSchermo()
                pygame.event.pump()
                GlobalVar.clockFadeToBlack.tick(GlobalVar.fpsFadeToBlack)
                i += 1
        GlobalVar.disegnaImmagineSuSchermo(screen, (0, 0))
        GlobalVar.aggiornaSchermo()


'''# linea(dove,colore,inizio,fine,spessore)
GlobalVar.disegnaLineaSuSchermo(GlobalVarG2.schermo, verde, (0, 0), (GlobalVarG2.gsx, GlobalVarG2.gsy), 10)
# cerchio(dove,colore,centro,raggio,spessore)
pygame.draw.circle(GlobalVarG2.schermo, blu, (300, 100), 5)
# rettangolo(dove,colore,(x,y,larghezza,altezza),spessore)
GlobalVar.disegnaRettangoloSuSchermo(GlobalVarG2.schermo, rosso, (200, 100, 30, 40), 5)'''
