# -*- coding: utf-8 -*-

import random
import copy
import pygame
import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GestioneCanaliAudioAmbiente as GestioneCanaliAudioAmbiente
import Codice.SettaggiLivelli.SetOstacoliContenutoCofanetti as SetOstacoliContenutoCofanetti


def getStatistiche(dati, difesa=0, inMenu=False):
    esptot = 1 + pow(dati[4], 2) + (dati[4] * 2)

    # inizializzo le statistiche con il valore base derivato dal livello
    pvtot = GlobalGameVar.statistichePerLivello[dati[4]-1][0]
    attVicino = GlobalGameVar.statistichePerLivello[dati[4]-1][1]
    attLontano = GlobalGameVar.statistichePerLivello[dati[4]-1][2]
    dif = GlobalGameVar.statistichePerLivello[dati[4]-1][3]
    par = 2

    # effetti armi
    attVicino += GlobalGameVar.statisticheEquipaggiamento["spade"][dati[6]]
    attLontano += GlobalGameVar.statisticheEquipaggiamento["archi"][dati[128]]
    dif += GlobalGameVar.statisticheEquipaggiamento["armature"][dati[8]] + GlobalGameVar.statisticheEquipaggiamento["scudiDif"][dati[7]]
    par += GlobalGameVar.statisticheEquipaggiamento["scudiPar"][dati[7]]
    # effetti accessori
    if dati[129] == 1:
        pvtot += GlobalGameVar.statisticheEquipaggiamento["guanti"][dati[129]]
    if dati[129] == 3:
        attVicino += GlobalGameVar.statisticheEquipaggiamento["guanti"][dati[129]]
        attLontano += GlobalGameVar.statisticheEquipaggiamento["guanti"][dati[129]]
    if dati[129] == 2:
        dif += GlobalGameVar.statisticheEquipaggiamento["guanti"][dati[129]]
    if dati[129] == 4:
        par += GlobalGameVar.statisticheEquipaggiamento["guanti"][dati[129]]
    # effetti tecniche
    if dati[123] > 0:
        attVicino += int(attVicino // 3)
        attLontano += int(attLontano // 3)
    if dati[124] > 0:
        dif += int(dif // 3)
    # effetto difesa
    if difesa != 0:
        par += int(par // 4)
        dif += int(dif // 2)

    entot = GlobalGameVar.statisticheEquipaggiamento["batteriaPe"][dati[9]]
    difro = GlobalGameVar.statisticheEquipaggiamento["batteriaDif"][dati[9]]

    return esptot, pvtot, entot, attVicino, attLontano, dif, difro, par


def getVitaTotRallo(livello, guanti):
    pvtot = GlobalGameVar.statistichePerLivello[livello-1][0]
    if guanti == 1:
        pvtot += GlobalGameVar.statisticheEquipaggiamento["guanti"][1]
    return pvtot


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
            if GlobalHWVar.gpx + (GlobalHWVar.gpx * n) == x and GlobalHWVar.gpy + (GlobalHWVar.gpy * m) == y:
                caseviste.append(True)
            else:
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
        if len(percorsoTrovato) == 0:
            percorsoTrovato = [xArrivo, yArrivo]
        return percorsoTrovato


def controllaMorteColco(dati, mosseRimasteRob,ultimoObbiettivoColco):
    if dati[10] <= 0:
        morterob = True
        mosseRimasteRob = 0
        dati[122] = 0
        dati[125] = 0
        dati[126] = 0
        ultimoObbiettivoColco = []
    else:
        morterob = False
    return morterob, dati, mosseRimasteRob, ultimoObbiettivoColco


def aggiornaInCasellaVistaDiNemiciEPersonaggi(caselleNonVisibili, listaNemici, listaPersonaggi):
    for nemico in listaNemici:
        nemico.inCasellaVista = False
        i = 0
        while i < len(caselleNonVisibili):
            if caselleNonVisibili[i] == nemico.x and caselleNonVisibili[i + 1] == nemico.y:
                if caselleNonVisibili[i + 2]:
                    nemico.inCasellaVista = True
                break
            i += 3

    for personaggio in listaPersonaggi:
        if not personaggio.mantieniSempreASchermo:
            personaggio.inCasellaVista = False
            i = 0
            while i < len(caselleNonVisibili):
                if caselleNonVisibili[i] == personaggio.x and caselleNonVisibili[i + 1] == personaggio.y:
                    if caselleNonVisibili[i + 2]:
                        personaggio.inCasellaVista = True
                    break
                i += 3
        else:
            personaggio.vicinoACasellaVista = False
            i = 0
            while i < len(caselleNonVisibili):
                if (personaggio.x + GlobalHWVar.gpx == caselleNonVisibili[i] and personaggio.y == caselleNonVisibili[i + 1]) or (personaggio.x - GlobalHWVar.gpx == caselleNonVisibili[i] and personaggio.y == caselleNonVisibili[i + 1]) or (personaggio.x == caselleNonVisibili[i] and personaggio.y + GlobalHWVar.gpy == caselleNonVisibili[i + 1]) or (personaggio.x == caselleNonVisibili[i] and personaggio.y - GlobalHWVar.gpy == caselleNonVisibili[i + 1]):
                    if caselleNonVisibili[i + 2]:
                        personaggio.vicinoACasellaVista = True
                        break
                i += 3

    return listaNemici, listaPersonaggi


def scorriObbiettiviInquadrati(avanzamentoStoria, nemicoInquadrato, listaNemiciVisti, listaEscheViste, scorriAvanti):
    obbiettivoRichiesto = False
    trovatoNemicoDaInquadrare = False

    if scorriAvanti:
        if not nemicoInquadrato and GlobalGameVar.impoPresente:
            obbiettivoRichiesto = "Colco"
        elif not nemicoInquadrato and not GlobalGameVar.impoPresente:
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
                if len(listaEscheViste) > 0 and listaEscheViste.index(int(nemicoInquadrato[4:])) + 3 < len(listaEscheViste) - 1:
                    nemicoInquadrato = "Esca" + str(listaEscheViste[listaEscheViste.index(int(nemicoInquadrato[4:])) + 4])
                    trovatoNemicoDaInquadrare = True
                else:
                    obbiettivoRichiesto = "ColcoFinale"
            if obbiettivoRichiesto == "ColcoFinale":
                if GlobalGameVar.impoPresente:
                    nemicoInquadrato = "Colco"
                    trovatoNemicoDaInquadrare = True
                else:
                    obbiettivoRichiesto = "NemicoIniziale"
            cicliDisponibili -= 1
    else:
        if not nemicoInquadrato and GlobalGameVar.impoPresente:
            obbiettivoRichiesto = "Colco"
        elif not nemicoInquadrato and not GlobalGameVar.impoPresente:
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
                    nemicoInquadrato = "Esca" + str(listaEscheViste[listaEscheViste.index(int(nemicoInquadrato[4:])) - 4])
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
                if GlobalGameVar.impoPresente:
                    nemicoInquadrato = "Colco"
                    trovatoNemicoDaInquadrare = True
                else:
                    obbiettivoRichiesto = "EscaFinale"
            cicliDisponibili -= 1

    return trovatoNemicoDaInquadrare, nemicoInquadrato


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
    casevisteEntrateIncluse = casevisteDaRallo[:]
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

    # il vettore delle casellePercorribiliPorteEscluse serve per sapere se le porte non visibili (in caselle che non sono accanto a caselle viste) devono essere disegnate verticalmente o orizzontalmente
    casellePercorribiliPorteEscluse, colcoInCasellaVista = scopriCaselleViste(x, y, rx, ry, stanza, [], cofanetti, avanzamentoStoria, vetPartenze=vetEntrate)

    return caseviste, casevisteDaRallo, casevisteEntrateIncluse, caselleNonVisibili, casellePercorribili, casellePercorribiliPorteEscluse


def copiaNemico(oggettoNemico, checkErrori=False):
    # ho messo una funzione che crea un nuovo oggetto e copia tutti gli attributi al posto del deepcopy
    if oggettoNemico:
        copia = oggettoNemico.creaCopia()
    else:
        copia = copy.deepcopy(oggettoNemico)
    if oggettoNemico and not checkErrori:
        copia.copiaImgs(oggettoNemico)
        copia.girati(copia.direzione)

    return copia


def copiaPersonaggio(oggettoPersonaggio, avanzamentoStoria, checkErrori=False):
    # ho messo una funzione che crea un nuovo oggetto e copia tutti gli attributi al posto del deepcopy
    if oggettoPersonaggio:
        copia = oggettoPersonaggio.creaCopia(avanzamentoStoria)
    else:
        copia = copy.deepcopy(oggettoPersonaggio)
    if copia.tipo != "Tutorial" and copia.tipo != "Nessuno" and not checkErrori:
        if copia.tipo.startswith("Oggetto"):
            copia.copiaImgsOggetto(oggettoPersonaggio)
            copia.aggiornaImgOggetto(avanzamentoStoria, True)
        else:
            copia.copiaImgsPersonaggio(oggettoPersonaggio)
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


def cambiaVolumeCanaliAudio(listaCanali, listaVolumiFinali, daMenu, posizioneCanaleMusica=-1):
    if daMenu:
        tempoPerCiclo = 5
        numeroCicli = 5.0
    else:
        tempoPerCiclo = 30
        numeroCicli = 10.0

    if len(listaCanali) == len(listaVolumiFinali) and len(listaCanali) > 0:
        listaVolumiIniziali = []
        for canale in listaCanali:
            if type(canale) is GestioneCanaliAudioAmbiente.CanaliAudioAmbiente:
                listaVolumiIniziali.append(canale.volume)
            else:
                listaVolumiIniziali.append(canale.get_volume())
        if GlobalGameVar.volumeMusicaDimezzato and posizioneCanaleMusica != -1 and listaVolumiFinali[posizioneCanaleMusica] == GlobalHWVar.volumeCanzoni:
            listaVolumiFinali[posizioneCanaleMusica] /= 2.0
        volumiInvariati = True
        i = 0
        while i < len(listaCanali):
            if listaVolumiFinali[i] != listaVolumiIniziali[i]:
                volumiInvariati = False
                break
            i += 1
        if not volumiInvariati:
            listaVolumiEffettivi = listaVolumiIniziali[:]
            numeroCicloAttuale = 1
            while numeroCicloAttuale <= numeroCicli:
                c = 0
                while c < len(listaCanali):
                    incrementoVolume = (listaVolumiFinali[c] - listaVolumiIniziali[c]) / numeroCicli
                    listaVolumiEffettivi[c] += incrementoVolume
                    if numeroCicloAttuale == numeroCicli:
                        listaVolumiEffettivi[c] = listaVolumiFinali[c]

                    if type(listaCanali[c]) is GestioneCanaliAudioAmbiente.CanaliAudioAmbiente:
                        listaCanali[c].settaVolume(listaVolumiEffettivi[c])
                    else:
                        listaCanali[c].set_volume(listaVolumiEffettivi[c])

                    c += 1
                pygame.time.wait(tempoPerCiclo)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                numeroCicloAttuale += 1
    # elif len(listaCanali) != len(listaVolumiFinali):
        # print ("Errore: il numero dei canali audio non corrisponde al numero dei volumi. NumCanali=" + str(len(listaCanali)) + ", NumVolumi=" + str(len(listaVolumiFinali)))


def sistemaImgPerCambioRisoluzione(dati, tutteporte, tutticofanetti, listaNemiciTotali, vettoreEsche, vettoreDenaro, listaPersonaggiTotali, ultimoObbiettivoColco, obbiettivoCasualeColco, gpxPreCambioRisoluzione, gpyPreCambioRisoluzione):
    # conversione della posizione in caselle
    dati[2] = dati[2] // gpxPreCambioRisoluzione * GlobalHWVar.gpx
    dati[3] = dati[3] // gpyPreCambioRisoluzione * GlobalHWVar.gpy
    dati[134] = dati[134] // gpxPreCambioRisoluzione * GlobalHWVar.gpx
    dati[135] = dati[135] // gpyPreCambioRisoluzione * GlobalHWVar.gpy
    i = 0
    while i < len(tutteporte):
        tutteporte[i + 1] = tutteporte[i + 1] // gpxPreCambioRisoluzione * GlobalHWVar.gpx
        tutteporte[i + 2] = tutteporte[i + 2] // gpyPreCambioRisoluzione * GlobalHWVar.gpy
        i += 4
    i = 0
    while i < len(tutticofanetti):
        tutticofanetti[i + 1] = tutticofanetti[i + 1] // gpxPreCambioRisoluzione * GlobalHWVar.gpx
        tutticofanetti[i + 2] = tutticofanetti[i + 2] // gpyPreCambioRisoluzione * GlobalHWVar.gpy
        i += 4

    for nemico in listaNemiciTotali:
        nemico.x = nemico.x // gpxPreCambioRisoluzione * GlobalHWVar.gpx
        nemico.y = nemico.y // gpyPreCambioRisoluzione * GlobalHWVar.gpy
        nemico.vx = nemico.vx // gpxPreCambioRisoluzione * GlobalHWVar.gpx
        nemico.vy = nemico.vy // gpyPreCambioRisoluzione * GlobalHWVar.gpy
        nemico.obbiettivo[1] = nemico.obbiettivo[1] // gpxPreCambioRisoluzione * GlobalHWVar.gpx
        nemico.obbiettivo[2] = nemico.obbiettivo[2] // gpyPreCambioRisoluzione * GlobalHWVar.gpy
        nemico.xPosizioneUltimoBersaglio = nemico.xPosizioneUltimoBersaglio // gpxPreCambioRisoluzione * GlobalHWVar.gpx
        nemico.yPosizioneUltimoBersaglio = nemico.yPosizioneUltimoBersaglio // gpyPreCambioRisoluzione * GlobalHWVar.gpy
        xOrig, yOrig = nemico.posizioneOriginale
        nemico.posizioneOriginale = (xOrig // gpxPreCambioRisoluzione * GlobalHWVar.gpx, yOrig // gpyPreCambioRisoluzione * GlobalHWVar.gpy)
        nemico.raggioVisivo = nemico.raggioVisivo // gpxPreCambioRisoluzione * GlobalHWVar.gpx
        nemico.caselleAttaccabiliAggiornate = False
        nemico.ultimaPosizioneConCaselleAttaccabiliAggiornate = [0, 0]
    i = 0
    while i < len(vettoreEsche):
        vettoreEsche[i + 2] = vettoreEsche[i + 2] // gpxPreCambioRisoluzione * GlobalHWVar.gpx
        vettoreEsche[i + 3] = vettoreEsche[i + 3] // gpyPreCambioRisoluzione * GlobalHWVar.gpy
        i += 4
    i = 0
    while i < len(vettoreDenaro):
        vettoreDenaro[i + 1] = vettoreDenaro[i + 1] // gpxPreCambioRisoluzione * GlobalHWVar.gpx
        vettoreDenaro[i + 2] = vettoreDenaro[i + 2] // gpyPreCambioRisoluzione * GlobalHWVar.gpy
        i += 4
    for personaggio in listaPersonaggiTotali:
        personaggio.x = personaggio.x // gpxPreCambioRisoluzione * GlobalHWVar.gpx
        personaggio.y = personaggio.y // gpyPreCambioRisoluzione * GlobalHWVar.gpy
        personaggio.vx = personaggio.vx // gpxPreCambioRisoluzione * GlobalHWVar.gpx
        personaggio.vy = personaggio.vy // gpyPreCambioRisoluzione * GlobalHWVar.gpy
    if len(ultimoObbiettivoColco) > 0:
        ultimoObbiettivoColco[1] = ultimoObbiettivoColco[1] // gpxPreCambioRisoluzione * GlobalHWVar.gpx
        ultimoObbiettivoColco[2] = ultimoObbiettivoColco[2] // gpyPreCambioRisoluzione * GlobalHWVar.gpy
    if obbiettivoCasualeColco:
        obbiettivoCasualeColco.x = obbiettivoCasualeColco.x // gpxPreCambioRisoluzione * GlobalHWVar.gpx
        obbiettivoCasualeColco.y = obbiettivoCasualeColco.y // gpyPreCambioRisoluzione * GlobalHWVar.gpy

    return dati, tutteporte, tutticofanetti, listaNemiciTotali, vettoreEsche, vettoreDenaro, listaPersonaggiTotali, ultimoObbiettivoColco, obbiettivoCasualeColco


def calcoloDanni(danno, difesa):
    dannoEffettivo = int((danno - (difesa / 2.0)) / ((difesa / 30.0) + 1))
    if dannoEffettivo < 0:
        dannoEffettivo = 0

    return dannoEffettivo
