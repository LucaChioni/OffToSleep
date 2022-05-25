# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.UtilityOstacoliContenutoCofanetti as UtilityOstacoliContenutoCofanetti


def setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria):
    if stanza == GlobalGameVar.dictStanze["tunnelSubacqueo1"]:
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
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
        if not (nx == 0 and ny == 0):
            if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 27, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 27, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
    elif stanza == GlobalGameVar.dictStanze["tunnelSubacqueo2"]:
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
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
        if not (nx == 0 and ny == 0):
            if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 28, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 28, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0

    return stanza, x, y, nx, ny, escludiOggettiBassi
