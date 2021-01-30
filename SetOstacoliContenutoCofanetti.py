# -*- coding: utf-8 -*-

from UtilityOstacoliContenutoCofanetti import *


def getEntrateStanze(stanza):
    entrateStanza = []

    if stanza == GlobalVar.dictStanze["sognoLucy1"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["sognoLucy2"]])
    elif stanza == GlobalVar.dictStanze["sognoLucy2"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["sognoLucy1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 3, +GlobalVar.gpx, 0, GlobalVar.dictStanze["sognoLucy3"]])
    elif stanza == GlobalVar.dictStanze["sognoLucy3"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 11, -GlobalVar.gpx, 0, GlobalVar.dictStanze["sognoLucy2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["sognoLucy4"]])
    elif stanza == GlobalVar.dictStanze["sognoLucy4"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["sognoLucy3"]])
    elif stanza == GlobalVar.dictStanze["casaHansLucy1"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy2"]])
    elif stanza == GlobalVar.dictStanze["casaHansLucy2"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy3"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy3"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy3"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy3"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy4"]])
    elif stanza == GlobalVar.dictStanze["casaHansLucy3"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy2"]])
    elif stanza == GlobalVar.dictStanze["casaHansLucy4"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta1"]])
    elif stanza == GlobalVar.dictStanze["forestaCadetta1"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 4, -GlobalVar.gpx, 0, GlobalVar.dictStanze["forestaCadetta2"]])
    elif stanza == GlobalVar.dictStanze["forestaCadetta2"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 14, +GlobalVar.gpx, 0, GlobalVar.dictStanze["forestaCadetta1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta3"]])
    elif stanza == GlobalVar.dictStanze["forestaCadetta3"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta4"]])
    elif stanza == GlobalVar.dictStanze["forestaCadetta4"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta3"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta5"]])
    elif stanza == GlobalVar.dictStanze["forestaCadetta5"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta4"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 8, +GlobalVar.gpx, 0, GlobalVar.dictStanze["forestaCadetta6"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta7"]])
    elif stanza == GlobalVar.dictStanze["forestaCadetta6"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 14, -GlobalVar.gpx, 0, GlobalVar.dictStanze["forestaCadetta5"]])
    elif stanza == GlobalVar.dictStanze["forestaCadetta7"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta5"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta8"]])
    elif stanza == GlobalVar.dictStanze["forestaCadetta8"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta7"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta9"]])
    elif stanza == GlobalVar.dictStanze["forestaCadetta9"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta8"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta8"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 15, 0, +GlobalVar.gpy, GlobalVar.dictStanze["stradaPerCittà1"]])
    elif stanza == GlobalVar.dictStanze["stradaPerCittà1"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta9"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta9"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta9"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta9"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta9"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta9"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta9"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta9"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta9"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta9"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta9"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta9"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta9"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 2, 0, -GlobalVar.gpy, GlobalVar.dictStanze["forestaCadetta9"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 6, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 8, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 9, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 10, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 11, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 12, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 14, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà2"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 15, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà2"]])
    elif stanza == GlobalVar.dictStanze["stradaPerCittà2"]:
        entrateStanza.extend([GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 4, +GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 5, +GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 6, +GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 7, +GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 8, +GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 9, +GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 10, +GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 11, +GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 12, +GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 13, +GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà1"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 4, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà3"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 5, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà3"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 6, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà3"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà3"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 8, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà3"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 9, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà3"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 10, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà3"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 11, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà3"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 12, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà3"]])
        entrateStanza.extend([GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13, -GlobalVar.gpx, 0, GlobalVar.dictStanze["stradaPerCittà3"]])

    return entrateStanza


def controlloOstacoli(x, y, nx, ny, stanza, carim, porte, cofanetti, escludiPorte=False, escludiOggettiBassi=False):
    cambiosta = False

    if x < 0 or y < 0 or x >= GlobalVar.gsx or y >= GlobalVar.gsy:
        return x, y, stanza, carim, cambiosta

    entrateStanza = getEntrateStanze(stanza)
    andandoVersoUscitaStanza = False
    i = 0
    while i < len(entrateStanza):
        if x == entrateStanza[i] and y == entrateStanza[i + 1] and nx == entrateStanza[i + 2] and ny == entrateStanza[i + 3] and not escludiPorte:
            stanza = entrateStanza[i + 4]
            cambiosta = True
            carim = True
            andandoVersoUscitaStanza = True
        elif x == entrateStanza[i] + entrateStanza[i + 2] and y == entrateStanza[i + 1] + entrateStanza[i + 3] and not escludiPorte:
            nx = 0
            ny = 0
            andandoVersoUscitaStanza = True
        i += 5

    if not andandoVersoUscitaStanza and not (nx == 0 and ny == 0) and not cambiosta:
        if stanza == GlobalVar.dictStanze["sognoLucy1"]:
            # bordi stanza
            if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 9, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 7, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 2, GlobalVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 7, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 2, GlobalVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalVar.dictStanze["sognoLucy2"]:
            # bordi stanza
            if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 9, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 6, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 4, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 5, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 7, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 11, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 4, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 7, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 4, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 5, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalVar.dictStanze["sognoLucy3"]:
            # bordi stanza
            if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 8, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 4, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 4, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalVar.dictStanze["sognoLucy4"]:
            # bordi stanza
            if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 1, GlobalVar.gpy * 7, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 5, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 5, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 1, GlobalVar.gpy * 7, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalVar.dictStanze["casaHansLucy1"]:
            # bordi stanza
            if not escludiOggettiBassi:
                if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                    nx = 0
                    ny = 0
                elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                    nx = 0
                    ny = 0
                elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                    nx = 0
                    ny = 0
                elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                    nx = 0
                    ny = 0
            else:
                if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 1:
                    nx = 0
                    ny = 0
                elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 2):
                    nx = 0
                    ny = 0
                elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 1:
                    nx = 0
                    ny = 0
                elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 2):
                    nx = 0
                    ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            if not (nx == 0 and ny == 0):
                if oggetto(GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 6, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 5, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 4, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 3, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 1, GlobalVar.gpx * 2, GlobalVar.gpy * 4, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 2, GlobalVar.gpy * 5, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 2, GlobalVar.gpy * 13, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 5, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 4, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 1, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 4, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 10, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 16, GlobalVar.gpx * 10, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 3, GlobalVar.gpy * 5, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 1, GlobalVar.gpy * 5, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
        if stanza == GlobalVar.dictStanze["casaHansLucy2"]:
            # bordi stanza
            if not escludiOggettiBassi:
                if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                    nx = 0
                    ny = 0
                elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                    nx = 0
                    ny = 0
                elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                    nx = 0
                    ny = 0
                elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                    nx = 0
                    ny = 0
            else:
                if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 1:
                    nx = 0
                    ny = 0
                elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 2):
                    nx = 0
                    ny = 0
                elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 1:
                    nx = 0
                    ny = 0
                elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 2):
                    nx = 0
                    ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            if not (nx == 0 and ny == 0):
                if oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 11, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 11, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 4, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 4, x, y, nx, ny):
                    nx = 0
                    ny = 0
        if stanza == GlobalVar.dictStanze["casaHansLucy3"]:
            # bordi stanza
            if not escludiOggettiBassi:
                if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                    nx = 0
                    ny = 0
                elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                    nx = 0
                    ny = 0
                elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                    nx = 0
                    ny = 0
                elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                    nx = 0
                    ny = 0
            else:
                if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 1:
                    nx = 0
                    ny = 0
                elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 2):
                    nx = 0
                    ny = 0
                elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 1:
                    nx = 0
                    ny = 0
                elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 2):
                    nx = 0
                    ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            if not (nx == 0 and ny == 0):
                if not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 28, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 1, GlobalVar.gpx * 2, GlobalVar.gpy * 16, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
        if stanza == GlobalVar.dictStanze["casaHansLucy4"]:
            # bordi stanza
            if not escludiOggettiBassi:
                if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                    nx = 0
                    ny = 0
                elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                    nx = 0
                    ny = 0
                elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                    nx = 0
                    ny = 0
                elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                    nx = 0
                    ny = 0
            else:
                if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 1:
                    nx = 0
                    ny = 0
                elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 2):
                    nx = 0
                    ny = 0
                elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 1:
                    nx = 0
                    ny = 0
                elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                    nx = 0
                    ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            if not (nx == 0 and ny == 0):
                if not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 10, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 5, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 3, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 5, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 10, x, y, nx, ny):
                    nx = 0
                    ny = 0
        if stanza == GlobalVar.dictStanze["forestaCadetta1"]:
            # bordi stanza
            if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 2, GlobalVar.gpy * 9, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 1, GlobalVar.gpy * 7, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 6, GlobalVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 4, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 5, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 3, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 8, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 4, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 5, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 3, GlobalVar.gpy * 9, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalVar.dictStanze["forestaCadetta2"]:
            # bordi stanza
            if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 3, GlobalVar.gpy * 14, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 6, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 2, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 1, GlobalVar.gpy * 5, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 3, GlobalVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 2, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 3, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalVar.dictStanze["forestaCadetta3"]:
            # bordi stanza
            if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 3, GlobalVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 2, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 9, GlobalVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 6, GlobalVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 5, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalVar.dictStanze["forestaCadetta4"]:
            # bordi stanza
            if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 6, GlobalVar.gpy * 14, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 2, GlobalVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 6, GlobalVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 4, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 2, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 2, GlobalVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 3, GlobalVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalVar.dictStanze["forestaCadetta5"]:
            # bordi stanza
            if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 13, GlobalVar.gpy * 14, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 8, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 13, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 12, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 10, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 9, GlobalVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 4, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalVar.dictStanze["forestaCadetta6"]:
            # bordi stanza
            if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 3, GlobalVar.gpy * 5, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 1, GlobalVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 4, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 7, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 4, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 2, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 4, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 2, GlobalVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 3, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 2, GlobalVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalVar.dictStanze["forestaCadetta7"]:
            # bordi stanza
            if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 2, GlobalVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 4, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 10, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 2, GlobalVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 4, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 4, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalVar.dictStanze["forestaCadetta8"]:
            # bordi stanza
            if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 3, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 5, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 4, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 2, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalVar.dictStanze["forestaCadetta9"]:
            # bordi stanza
            if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 3, GlobalVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 3, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 6, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 2, GlobalVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif oggetto(GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalVar.dictStanze["stradaPerCittà1"]:
            # bordi stanza
            if not escludiOggettiBassi:
                if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                    nx = 0
                    ny = 0
                elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                    nx = 0
                    ny = 0
                elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                    nx = 0
                    ny = 0
                elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                    nx = 0
                    ny = 0
            else:
                if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 1:
                    nx = 0
                    ny = 0
                elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 2):
                    nx = 0
                    ny = 0
                elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 1:
                    nx = 0
                    ny = 0
                elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 2):
                    nx = 0
                    ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            if not (nx == 0 and ny == 0):
                if oggetto(GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 1, GlobalVar.gpx * 11, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif oggetto(GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 6, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 16, GlobalVar.gpx * 30, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 13, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 5, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 4, x, y, nx, ny):
                    nx = 0
                    ny = 0
        if stanza == GlobalVar.dictStanze["stradaPerCittà2"]:
            # bordi stanza
            if not escludiOggettiBassi:
                if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
                    nx = 0
                    ny = 0
                elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 3):
                    nx = 0
                    ny = 0
                elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 2:
                    nx = 0
                    ny = 0
                elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 3):
                    nx = 0
                    ny = 0
            else:
                if nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 1:
                    nx = 0
                    ny = 0
                elif nx == GlobalVar.gpx and x >= GlobalVar.gsx - (GlobalVar.gpx * 2):
                    nx = 0
                    ny = 0
                elif ny == -GlobalVar.gpy and y <= GlobalVar.gpy * 1:
                    nx = 0
                    ny = 0
                elif ny == GlobalVar.gpy and y >= GlobalVar.gsy - (GlobalVar.gpy * 2):
                    nx = 0
                    ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            if not (nx == 0 and ny == 0):
                if oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 1, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 16, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 30, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 30, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and oggetto(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0

        # controllo se le porte sono chiuse o aperte
        if not (nx == 0 and ny == 0):
            i = 0
            while i < len(porte):
                if not porte[i + 3]:
                    if oggetto(porte[i + 1], porte[i + 2], GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                        nx = 0
                        ny = 0
                        break
                i = i + 4
        # controllo cofanetti
        if not (nx == 0 and ny == 0):
            i = 0
            while i < len(cofanetti):
                if oggetto(cofanetti[i + 1], cofanetti[i + 2], GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                    break
                i = i + 4

    # movimento personaggio
    x = x + nx
    y = y + ny

    return x, y, stanza, carim, cambiosta


def aperturacofanetto(stanza, cx, cy, dati):
    avanzamentoStoria = dati[0]
    numFrecceOttenute = 1
    numMoneteOttenute = 50

    tesoro = -1
    # 11-30 -> tecniche(20) / 31-40 -> oggetti(10) / 41-70 -> armi(30) / 71-75 -> batterie(10) / 81-100 -> condizioni(20) / 101-120 -> gambit (=celle di memoria)(20) / 131 -> monete / 132 frecce
    if stanza == -1:
        # ottieni pozione
        if cx == GlobalVar.gpx * 3 and cy == GlobalVar.gpy * 7:
            tesoro = 31
        # ottieni cella di memoria
        if cx == GlobalVar.gpx * 7 and cy == GlobalVar.gpy * 12:
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

    if stanza == GlobalVar.dictStanze["sognoLucy1"]:
        # ottieni pozione
        if cx == GlobalVar.gpx * 13 and cy == GlobalVar.gpy * 10:
            tesoro = 31
            avanzamentoStoria += 1
    if stanza == GlobalVar.dictStanze["sognoLucy2"]:
        # ottieni pozione
        if cx == GlobalVar.gpx * 13 and cy == GlobalVar.gpy * 5:
            tesoro = 31
        # ottieni medicina
        if cx == GlobalVar.gpx * 28 and cy == GlobalVar.gpy * 7:
            tesoro = 33
    if stanza == GlobalVar.dictStanze["sognoLucy3"]:
        # ottieni bomba
        if cx == GlobalVar.gpx * 3 and cy == GlobalVar.gpy * 13:
            tesoro = 36
    if stanza == GlobalVar.dictStanze["casaHansLucy1"]:
        # ottieni armatura
        if cx == GlobalVar.gpx * 23 and cy == GlobalVar.gpy * 13:
            tesoro = 52
            avanzamentoStoria += 1
        # ottieni spada
        if cx == GlobalVar.gpx * 24 and cy == GlobalVar.gpy * 15:
            tesoro = 42
            avanzamentoStoria += 1
        # ottieni scudo
        if cx == GlobalVar.gpx * 27 and cy == GlobalVar.gpy * 15:
            tesoro = 57
            avanzamentoStoria += 1
        # ottieni arco
        if cx == GlobalVar.gpx * 29 and cy == GlobalVar.gpy * 14:
            tesoro = 47
            avanzamentoStoria += 1
    if stanza == GlobalVar.dictStanze["casaHansLucy3"]:
        # ottieni pozione
        if cx == GlobalVar.gpx * 21 and cy == GlobalVar.gpy * 10:
            tesoro = 31
    if stanza == GlobalVar.dictStanze["forestaCadetta1"]:
        # ottieni pozione
        if cx == GlobalVar.gpx * 27 and cy == GlobalVar.gpy * 2:
            tesoro = 31
        # ottieni pozione
        if cx == GlobalVar.gpx * 4 and cy == GlobalVar.gpy * 15:
            tesoro = 31
        # ottieni freccia
        if cx == GlobalVar.gpx * 8 and cy == GlobalVar.gpy * 2:
            tesoro = 132
    if stanza == GlobalVar.dictStanze["forestaCadetta2"]:
        # ottieni bomba
        if cx == GlobalVar.gpx * 18 and cy == GlobalVar.gpy * 14:
            tesoro = 36
        # ottieni pozione
        if cx == GlobalVar.gpx * 11 and cy == GlobalVar.gpy * 2:
            tesoro = 31
        # ottieni esca
        if cx == GlobalVar.gpx * 5 and cy == GlobalVar.gpy * 9:
            tesoro = 38
    if stanza == GlobalVar.dictStanze["forestaCadetta3"]:
        # ottieni pozione
        if cx == GlobalVar.gpx * 20 and cy == GlobalVar.gpy * 2:
            tesoro = 31
        # ottieni freccia
        if cx == GlobalVar.gpx * 5 and cy == GlobalVar.gpy * 13:
            tesoro = 132
        # ottieni guanti vitali
        if cx == GlobalVar.gpx * 21 and cy == GlobalVar.gpy * 9:
            tesoro = 62
    if stanza == GlobalVar.dictStanze["forestaCadetta4"]:
        # ottieni pozione
        if cx == GlobalVar.gpx * 29 and cy == GlobalVar.gpy * 9:
            tesoro = 31
        # ottieni bomba
        if cx == GlobalVar.gpx * 10 and cy == GlobalVar.gpy * 2:
            tesoro = 36
    if stanza == GlobalVar.dictStanze["forestaCadetta6"]:
        # ottieni freccia
        if cx == GlobalVar.gpx * 12 and cy == GlobalVar.gpy * 2:
            tesoro = 132
        # ottieni esca
        if cx == GlobalVar.gpx * 21 and cy == GlobalVar.gpy * 2:
            tesoro = 38
    if stanza == GlobalVar.dictStanze["forestaCadetta7"]:
        # ottieni pozione
        if cx == GlobalVar.gpx * 26 and cy == GlobalVar.gpy * 15:
            tesoro = 31
        # ottieni collana rigenerante
        if cx == GlobalVar.gpx * 2 and cy == GlobalVar.gpy * 4:
            tesoro = 48
    if stanza == GlobalVar.dictStanze["forestaCadetta8"]:
        # ottieni arco di ferro
        if cx == GlobalVar.gpx * 2 and cy == GlobalVar.gpy * 6:
            tesoro = 67
    if stanza == GlobalVar.dictStanze["forestaCadetta9"]:
        # ottieni bomba veleno
        if cx == GlobalVar.gpx * 5 and cy == GlobalVar.gpy * 11:
            tesoro = 37

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
            dati[tesoro] = ottieniMonete(dati, numMoneteOttenute)
        elif tesoro == 132:
            dati[tesoro], tesoro = ottieniFrecce(dati, numFrecceOttenute, tesoro)
        else:
            tesoro = -2
    return dati, tesoro, avanzamentoStoria
