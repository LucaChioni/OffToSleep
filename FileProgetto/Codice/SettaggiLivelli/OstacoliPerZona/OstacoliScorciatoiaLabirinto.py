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
    if stanza == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["scorciatoiaLabirinto2"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 8, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0

    return stanza, x, y, nx, ny, escludiOggettiBassi
