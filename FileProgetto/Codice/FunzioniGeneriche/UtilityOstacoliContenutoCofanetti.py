# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar


def oggetto(xInizio, yInizio, dimx, dimy, px, py, nx, ny):
    xFine = xInizio + dimx - GlobalHWVar.gpx
    yFine = yInizio + dimy - GlobalHWVar.gpy
    if xInizio <= px <= xFine:
        if (ny == -GlobalHWVar.gpy and py == yFine + GlobalHWVar.gpy) or (ny == GlobalHWVar.gpy and py == yInizio - GlobalHWVar.gpy):
            return True
    if yInizio <= py <= yFine:
        if (nx == -GlobalHWVar.gpx and px == xFine + GlobalHWVar.gpx) or (nx == GlobalHWVar.gpx and px == xInizio - GlobalHWVar.gpx):
            return True


def ottieniMonete(dati, moneteOttenute):
    moneteTot = dati[131] + moneteOttenute
    if moneteTot > GlobalGameVar.maxMonete:
        moneteTot = GlobalGameVar.maxMonete
    return moneteTot


def ottieniFrecce(dati, frecceOttenute, tesoro):
    maxFrecce = GlobalGameVar.frecceMaxPerFaretra[dati[133]]
    if dati[132] == maxFrecce:
        tesoro = -tesoro
    frecceTot = dati[132] + frecceOttenute
    if frecceTot > maxFrecce:
        frecceTot = maxFrecce
    return frecceTot, tesoro


def ottieniOggetto(dati, numOggetto, qta):
    if dati[numOggetto] <= -1:
        dati[numOggetto] += 1
        dati[numOggetto] += qta
    elif dati[numOggetto] < 99:
        dati[numOggetto] += qta
    else:
        numOggetto = -numOggetto
    if dati[numOggetto] > 99:
        dati[numOggetto] = 99
    return dati, numOggetto


def ottieniCellaDiMemoria(dati):
    numCella = -1
    i = 101
    while i <= 110:
        if dati[i] == -1:
            numCella = i
            break
        i += 1
    if numCella != -1:
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
