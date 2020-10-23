# -*- coding: utf-8 -*-

from UtilityOstacoliContenutoCofanetti import *


def muri_porte(x, y, nx, ny, stanza, carim, mostro, robo, porte, cofanetti, listaPersonaggi):
    cambiosta = False

    if x < 0 or y < 0 or x >= GlobalVar.gsx or y >= GlobalVar.gsy:
        return x, y, stanza, carim, cambiosta

    if (stanza == GlobalVar.dictStanze["sognoSara1"]) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if ny == +GlobalVar.gpy and x == GlobalVar.gsx // 32 * 15 and y == GlobalVar.gsy // 18 * 15 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["sognoSara2"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 15 and y == GlobalVar.gsy // 18 * 16 and not mostro and not robo:
            nx = 0
            ny = 0
        # bordi stanza
        elif nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
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
    if (stanza == GlobalVar.dictStanze["sognoSara2"]) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if ny == -GlobalVar.gpy and x == GlobalVar.gsx // 32 * 7 and y == GlobalVar.gsy // 18 * 2 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["sognoSara1"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 7 and y == GlobalVar.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
            ny = 0
        elif nx == GlobalVar.gpx and x == GlobalVar.gsx // 32 * 29 and y == GlobalVar.gsy // 18 * 3 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["sognoSara3"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 30 and y == GlobalVar.gsy // 18 * 3 and not mostro and not robo:
            nx = 0
            ny = 0
        # bordi stanza
        elif nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
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
    if (stanza == GlobalVar.dictStanze["sognoSara3"]) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if nx == -GlobalVar.gpx and x == GlobalVar.gsx // 32 * 2 and y == GlobalVar.gsy // 18 * 11 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["sognoSara2"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 1 and y == GlobalVar.gsy // 18 * 11 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == -GlobalVar.gpy and x == GlobalVar.gsx // 32 * 14 and y == GlobalVar.gsy // 18 * 2 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["sognoSara4"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 14 and y == GlobalVar.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
            ny = 0
        # bordi stanza
        elif nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
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
    if (stanza == GlobalVar.dictStanze["sognoSara4"]) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if ny == GlobalVar.gpy and x == GlobalVar.gsx // 32 * 15 and y == GlobalVar.gsy // 18 * 15 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["sognoSara3"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 15 and y == GlobalVar.gsy // 18 * 16 and not mostro and not robo:
            nx = 0
            ny = 0
        # bordi stanza
        elif nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
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
    if (stanza == GlobalVar.dictStanze["casaSamSara1"]) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if ny == GlobalVar.gpy and x == GlobalVar.gsx // 32 * 16 and y == GlobalVar.gsy // 18 * 15 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara2"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 16 and y == GlobalVar.gsy // 18 * 16 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == GlobalVar.gpy and x == GlobalVar.gsx // 32 * 17 and y == GlobalVar.gsy // 18 * 15 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara2"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 17 and y == GlobalVar.gsy // 18 * 16 and not mostro and not robo:
            nx = 0
            ny = 0
        # bordi stanza
        elif nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
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
        elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 1, GlobalVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 6, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 5, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 5, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 4, GlobalVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 2, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 3, GlobalVar.gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 7, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 4, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 5, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 3, GlobalVar.gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
    if (stanza == GlobalVar.dictStanze["casaSamSara2"]) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if ny == -GlobalVar.gpy and x == GlobalVar.gsx // 32 * 16 and y == GlobalVar.gsy // 18 * 2 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara1"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 16 and y == GlobalVar.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == -GlobalVar.gpy and x == GlobalVar.gsx // 32 * 17 and y == GlobalVar.gsy // 18 * 2 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara1"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 17 and y == GlobalVar.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == -GlobalVar.gpy and x == GlobalVar.gsx // 32 * 3 and y == GlobalVar.gsy // 18 * 2 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara3"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 3 and y == GlobalVar.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == -GlobalVar.gpy and x == GlobalVar.gsx // 32 * 4 and y == GlobalVar.gsy // 18 * 2 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara3"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 4 and y == GlobalVar.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == -GlobalVar.gpy and x == GlobalVar.gsx // 32 * 27 and y == GlobalVar.gsy // 18 * 2 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara3"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 27 and y == GlobalVar.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == -GlobalVar.gpy and x == GlobalVar.gsx // 32 * 28 and y == GlobalVar.gsy // 18 * 2 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara3"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 28 and y == GlobalVar.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == GlobalVar.gpy and x == GlobalVar.gsx // 32 * 13 and y == GlobalVar.gsy // 18 * 15 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara4"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 13 and y == GlobalVar.gsy // 18 * 16 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == GlobalVar.gpy and x == GlobalVar.gsx // 32 * 14 and y == GlobalVar.gsy // 18 * 15 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara4"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 14 and y == GlobalVar.gsy // 18 * 16 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == GlobalVar.gpy and x == GlobalVar.gsx // 32 * 15 and y == GlobalVar.gsy // 18 * 15 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara4"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 15 and y == GlobalVar.gsy // 18 * 16 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == GlobalVar.gpy and x == GlobalVar.gsx // 32 * 16 and y == GlobalVar.gsy // 18 * 15 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara4"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 16 and y == GlobalVar.gsy // 18 * 16 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == GlobalVar.gpy and x == GlobalVar.gsx // 32 * 17 and y == GlobalVar.gsy // 18 * 15 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara4"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 17 and y == GlobalVar.gsy // 18 * 16 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == GlobalVar.gpy and x == GlobalVar.gsx // 32 * 18 and y == GlobalVar.gsy // 18 * 15 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara4"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 18 and y == GlobalVar.gsy // 18 * 16 and not mostro and not robo:
            nx = 0
            ny = 0
        # bordi stanza
        elif nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
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
        elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 3, GlobalVar.gpy * 3, x, y, nx, ny):
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
        elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 11, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 11, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
    if (stanza == GlobalVar.dictStanze["casaSamSara3"]) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if ny == GlobalVar.gpy and x == GlobalVar.gsx // 32 * 3 and y == GlobalVar.gsy // 18 * 15 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara2"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 3 and y == GlobalVar.gsy // 18 * 16 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == GlobalVar.gpy and x == GlobalVar.gsx // 32 * 4 and y == GlobalVar.gsy // 18 * 15 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara2"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 4 and y == GlobalVar.gsy // 18 * 16 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == GlobalVar.gpy and x == GlobalVar.gsx // 32 * 27 and y == GlobalVar.gsy // 18 * 15 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara2"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 27 and y == GlobalVar.gsy // 18 * 16 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == GlobalVar.gpy and x == GlobalVar.gsx // 32 * 28 and y == GlobalVar.gsy // 18 * 15 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara2"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 28 and y == GlobalVar.gsy // 18 * 16 and not mostro and not robo:
            nx = 0
            ny = 0
        # bordi stanza
        elif nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
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
        elif oggetto(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 28, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 10, GlobalVar.gpx * 2, GlobalVar.gpy * 6, x, y, nx, ny):
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
    if (stanza == GlobalVar.dictStanze["casaSamSara4"]) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if ny == -GlobalVar.gpy and x == GlobalVar.gsx // 32 * 14 and y == GlobalVar.gsy // 18 * 2 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara2"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 14 and y == GlobalVar.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == -GlobalVar.gpy and x == GlobalVar.gsx // 32 * 15 and y == GlobalVar.gsy // 18 * 2 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara2"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 15 and y == GlobalVar.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == -GlobalVar.gpy and x == GlobalVar.gsx // 32 * 16 and y == GlobalVar.gsy // 18 * 2 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara2"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 16 and y == GlobalVar.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == -GlobalVar.gpy and x == GlobalVar.gsx // 32 * 17 and y == GlobalVar.gsy // 18 * 2 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara2"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 17 and y == GlobalVar.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == GlobalVar.gpy and x == GlobalVar.gsx // 32 * 15 and y == GlobalVar.gsy // 18 * 15 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["forestaCadetta1"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 15 and y == GlobalVar.gsy // 18 * 16 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == GlobalVar.gpy and x == GlobalVar.gsx // 32 * 16 and y == GlobalVar.gsy // 18 * 15 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["forestaCadetta1"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 16 and y == GlobalVar.gsy // 18 * 16 and not mostro and not robo:
            nx = 0
            ny = 0
        # bordi stanza
        elif nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
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
        elif oggetto(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 10, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 5, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 3, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 13, GlobalVar.gpx * 1, GlobalVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 12, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 5, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 2, GlobalVar.gpx * 1, GlobalVar.gpy * 10, x, y, nx, ny):
            nx = 0
            ny = 0
    if (stanza == GlobalVar.dictStanze["forestaCadetta1"]) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if ny == -GlobalVar.gpy and x == GlobalVar.gsx // 32 * 15 and y == GlobalVar.gsy // 18 * 2 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara4"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 15 and y == GlobalVar.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == -GlobalVar.gpy and x == GlobalVar.gsx // 32 * 16 and y == GlobalVar.gsy // 18 * 2 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["casaSamSara4"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 16 and y == GlobalVar.gsy // 18 * 1 and not mostro and not robo:
            nx = 0
            ny = 0
        elif nx == -GlobalVar.gpx and x == GlobalVar.gsx // 32 * 2 and y == GlobalVar.gsy // 18 * 4 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["forestaCadetta2"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 1 and y == GlobalVar.gsy // 18 * 4 and not mostro and not robo:
            nx = 0
            ny = 0
        # bordi stanza
        elif nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
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
        elif oggetto(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 8, GlobalVar.gpx * 4, GlobalVar.gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 14, GlobalVar.gpx * 3, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 9, GlobalVar.gpx * 9, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 3, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 6, GlobalVar.gpx * 2, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
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
    if (stanza == GlobalVar.dictStanze["forestaCadetta2"]) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if nx == GlobalVar.gpx and x == GlobalVar.gsx // 32 * 29 and y == GlobalVar.gsy // 18 * 14 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["forestaCadetta1"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 30 and y == GlobalVar.gsy // 18 * 14 and not mostro and not robo:
            nx = 0
            ny = 0
        elif ny == GlobalVar.gpy and x == GlobalVar.gsx // 32 * 12 and y == GlobalVar.gsy // 18 * 15 and not mostro and not robo:
            stanza = GlobalVar.dictStanze["forestaCadetta3"]
            cambiosta = True
            carim = True
        elif x == GlobalVar.gsx // 32 * 12 and y == GlobalVar.gsy // 18 * 16 and not mostro and not robo:
            nx = 0
            ny = 0
        # bordi stanza
        elif nx == -GlobalVar.gpx and x <= GlobalVar.gpx * 2:
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
        elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 11, GlobalVar.gpx * 1, GlobalVar.gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        elif oggetto(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 15, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
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

    # controllo se le porte sono chiuse o aperte
    if nx != 0 or ny != 0:
        i = 0
        while i < len(porte):
            if not porte[i + 3]:
                if oggetto(porte[i + 1], porte[i + 2], GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                    break
            i = i + 4
    # controllo cofanetti
    if nx != 0 or ny != 0:
        i = 0
        while i < len(cofanetti):
            if oggetto(cofanetti[i + 1], cofanetti[i + 2], GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
                break
            i = i + 4
    # controllo gli oggetti nella lista delle persone
    if nx != 0 or ny != 0:
        for persona in listaPersonaggi:
            if persona.mantieniSempreASchermo and oggetto(persona.x, persona.y, GlobalVar.gpx * 1, GlobalVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
                break

    # movimento personaggio
    x = x + nx
    y = y + ny

    return x, y, stanza, carim, cambiosta


def aperturacofanetto(stanza, cx, cy, dati):
    avanzamentoStoria = dati[0]

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

    if stanza == GlobalVar.dictStanze["sognoSara1"]:
        # ottieni pozione
        if cx == GlobalVar.gpx * 13 and cy == GlobalVar.gpy * 10:
            tesoro = 31
            avanzamentoStoria += 1
    if stanza == GlobalVar.dictStanze["sognoSara2"]:
        # ottieni pozione
        if cx == GlobalVar.gpx * 13 and cy == GlobalVar.gpy * 5:
            tesoro = 31
        # ottieni medicina
        if cx == GlobalVar.gpx * 28 and cy == GlobalVar.gpy * 7:
            tesoro = 33
    if stanza == GlobalVar.dictStanze["sognoSara3"]:
        # ottieni bomba
        if cx == GlobalVar.gpx * 3 and cy == GlobalVar.gpy * 13:
            tesoro = 36
    if stanza == GlobalVar.dictStanze["casaSamSara1"]:
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
            dati[tesoro] = ottieniMonete(dati, 50)
        elif tesoro == 132:
            dati[tesoro] = ottieniFrecce(dati, 5)
        else:
            tesoro = -2
    return dati, tesoro, avanzamentoStoria
