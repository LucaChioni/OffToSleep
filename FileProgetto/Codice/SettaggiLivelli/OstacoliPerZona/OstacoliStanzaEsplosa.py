# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.UtilityOstacoliContenutoCofanetti as UtilityOstacoliContenutoCofanetti


def setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria):
    # bordi stanza
    if not escludiOggettiBassi:
        if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
            nx = 0
            ny = 0
        elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
            nx = 0
            ny = 0
        elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
            nx = 0
            ny = 0
        elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
            nx = 0
            ny = 0
    else:
        if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 1:
            nx = 0
            ny = 0
        elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 2):
            nx = 0
            ny = 0
        elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 1:
            nx = 0
            ny = 0
        elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 2):
            nx = 0
            ny = 0
    # controllo muri-oggetti
    if stanza == GlobalGameVar.dictStanze["stanzaEsplosa"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0

    return stanza, x, y, nx, ny, escludiOggettiBassi
