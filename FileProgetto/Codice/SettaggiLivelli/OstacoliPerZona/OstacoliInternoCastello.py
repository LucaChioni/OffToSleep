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
    if stanza == GlobalGameVar.dictStanze["internoCastello1"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello2"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny) and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello3"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 10, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 7, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 8, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 7, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello4"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 7, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 23, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 7, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 9, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 8, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 8, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 9, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello5"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 8, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 7, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 19, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 11, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello6"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 27, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 25, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 8, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 8, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 10, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 12, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello7"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 17, GlobalHWVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 7, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 7, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello8"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 8, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 8, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello9"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 17, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 9, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 8, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello10"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 11, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 17, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 17, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello11"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 8, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 7, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello12"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 8, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello13"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 7, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 8, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 14, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 25, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 17, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 8, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello14"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 10, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 7, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 10, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 9, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 7, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello15"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 9, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello16"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 7, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello17"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 9, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 8, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello18"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 17, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 11, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 9, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello19"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 11, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny) and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
    elif stanza == GlobalGameVar.dictStanze["internoCastello20"] and not (nx == 0 and ny == 0):
        # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx, ny)
        if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 19, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 25, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 9, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 8, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 7, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0

    return stanza, x, y, nx, ny, escludiOggettiBassi
