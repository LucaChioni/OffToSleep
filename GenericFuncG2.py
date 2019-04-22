# -*- coding: utf-8 -*-

import os
import random
from GlobalVarG2 import *


def messaggio(msg, colore, x, y, gr):
    gr = gr - 10
    y = y - (gpy // 8)
    carattere = "Gentium Book Basic"
    if gsx >= 3840 and gsy >= 2160:
        font = pygame.font.SysFont(carattere, gr * 2)
    if (gsx < 3840 and gsx > 1920) and (gsy < 2160 and gsy > 1080):
        font = pygame.font.SysFont(carattere, gr * 4 // 3)
    if gsx == 1920 and gsy == 1080:
        font = pygame.font.SysFont(carattere, gr)
    if (gsx < 1920 and gsx > 1600) and (gsy < 1080 and gsy > 900):
        font = pygame.font.SysFont(carattere, gr * 7 // 8)
    if gsx == 1600 and gsy == 900:
        font = pygame.font.SysFont(carattere, gr * 5 // 6)
    if (gsx < 1600 and gsx > 1280) and (gsy < 900 and gsy > 720):
        font = pygame.font.SysFont(carattere, gr * 3 // 4)
    if gsx == 1280 and gsy == 720:
        font = pygame.font.SysFont(carattere, gr * 2 // 3)
    if (gsx < 1280 and gsx >= 1024) and (gsy < 720 and gsy >= 576):
        font = pygame.font.SysFont(carattere, gr // 2)
    if gsx < 1024 and gsy < 576:
        font = pygame.font.SysFont(carattere, gr // 5 * 2)
    testo = font.render(msg, True, colore)
    schermo.blit(testo, (x, y))


def getStatistiche(dati):
    """pvtot = 100 + (dati[4] * 5)
    att = 10 + (dati[4] * 2) + (dati[6] * 10)
    dif = 10 + (dati[4] * 2) + (dati[8] * 10) + 5 + (dati[7] * 5)"""
    esptot = pow(dati[4], 2) + (dati[4] * 10)
    pvtot = 100
    att = 14 + (dati[6] * 10)
    dif = 12 + (dati[8] * 10) + 5 + (dati[7] * 5)
    par = 3 + (dati[7] * 3)

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
                att += (i * 2)
                break
            i += 3

    if dati[4] >= 3:
        i = 3
        while i <= 100:
            if dati[4] <= i + 2:
                dif += (i * 2)
                break
            i += 3

    entot = 300 + (dati[9] * 100)
    difro = 10 + (dati[9] * 10)

    return esptot, pvtot, entot, att, dif, difro, par


def guardaVideo(path, audio=0):
    listaImg = []
    # load all the images
    for i in os.listdir(path):
        img = pygame.image.load(path + '/' + i).convert()
        img = pygame.transform.scale(img, (gsx, gsy))
        listaImg.append(img)
    if audio != 0:
        audio.play(-1)
    # play video
    for i in listaImg:
        schermo.blit(i, (0, 0))
        pygame.display.update()
        clock.tick(fpsvideo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                selezione.play()
                if audio != 0:
                    audio.stop()
                return True
    if audio != 0:
        audio.stop()
    return False


def salvataggio(n, dati, porteini, portefin, cofaniini, cofanifin, porte, cofanetti):
    scrivi = open("Salvataggi\Salvataggio%i.txt" % n, "w")
    # conversione della posizione in caselle
    dati[2] = dati[2] // gpx
    dati[3] = dati[3] // gpy
    i = porteini
    while i <= portefin:
        j = 0
        while j < len(porte):
            if dati[i] == porte[j] and dati[i + 1] == porte[j + 1] and dati[i + 2] == porte[j + 2]:
                dati[i + 3] = porte[j + 3]
            j = j + 4
        dati[i + 1] = dati[i + 1] // gpx
        dati[i + 2] = dati[i + 2] // gpy
        i = i + 4
    i = cofaniini
    while i <= cofanifin:
        j = 0
        while j < len(cofanetti):
            if dati[i] == cofanetti[j] and dati[i + 1] == cofanetti[j + 1] and dati[i + 2] == cofanetti[j + 2]:
                dati[i + 3] = cofanetti[j + 3]
            j = j + 4
        dati[i + 1] = dati[i + 1] // gpx
        dati[i + 2] = dati[i + 2] // gpy
        i = i + 4

    for i in range(0, len(dati)):
        scrivi.write("%i_" % dati[i])
    scrivi.close()

    # conversione della posizione in pixel
    dati[2] = dati[2] * gpx
    dati[3] = dati[3] * gpy
    i = porteini
    while i <= portefin:
        dati[i + 1] = dati[i + 1] * gpx
        dati[i + 2] = dati[i + 2] * gpy
        i = i + 4
    i = cofaniini
    while i <= cofanifin:
        dati[i + 1] = dati[i + 1] * gpx
        dati[i + 2] = dati[i + 2] * gpy
        i = i + 4


def oggetto(x, y, dimx, dimy, px, py, nx, ny):
    a = x
    b = y
    dimx = dimx + x
    dimy = dimy + y
    while x < dimx:
        if (ny == -gpy and py == dimy and px == x) or (ny == gpy and py == y - gpy and px == x):
            return True
        x = x + gpx
    x = a
    y = b
    while y < dimy:
        if (nx == -gpx and px == dimx and py == y) or (nx == gpx and px == x - gpx and py == y):
            return True
        y = y + gpy


def muri_porte(x, y, nx, ny, stanza, carim, muovi, mostro, robo, porte, cofanetti):
    cambiosta = False
    # prima stanza
    if (stanza == 1) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if ny == -gpy and x == gsx // 32 * 6 and y == gsy // 18 * 2 and not mostro and not robo:
            stanza = 2
            cambiosta = True
            carim = True
        else:
            # bordi stanza
            if nx == -gpx and x <= gpx * 2:
                nx = 0
            if nx == gpx and x >= gsx - (gpx * 3):
                nx = 0
            if ny == -gpy and y <= gpy * 2:
                ny = 0
            if ny == gpy and y >= gsy - (gpy * 3):
                ny = 0
        # controllo muri-oggetti
        #          posizione x    posizione y     dim x    dim y   px py  nx  ny
        if oggetto(gsx // 32 * 7, gsy // 18 * 11, gpx * 1, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 18, gsy // 18 * 7, gpx * 2, gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 21, gsy // 18 * 11, gpx * 4, gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        # controllo se le porte sono chiuse o aperte
        i = 0
        while i < len(porte):
            if not porte[i + 3]:
                if oggetto(porte[i + 1], porte[i + 2], gpx * 1, gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
            i = i + 4
        # controllo cofanetti
        i = 0
        while i < len(cofanetti):
            if oggetto(cofanetti[i + 1], cofanetti[i + 2], gpx * 1, gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            i = i + 4
    # seconda stanza
    if (stanza == 2) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if ny == -gpy and x == gsx // 32 * 6 and y == gsy // 18 * 2 and not mostro and not robo:
            stanza = 1
            cambiosta = True
            carim = True
        else:
            # bordi stanza
            if nx == -gpx and x <= gpx * 2:
                nx = 0
            if nx == gpx and x >= gsx - (gpx * 3):
                nx = 0
            if ny == -gpy and y <= gpy * 2:
                ny = 0
            if ny == gpy and y >= gsy - (gpy * 3):
                ny = 0
        # controllo muri-oggetti
        #          posizione x    posizione y    dim x    dim y    px py nx  ny
        if oggetto(gsx // 32 * 9, gsy // 18 * 2, gpx * 1, gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 2, gsy // 18 * 7, gpx * 1, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 4, gsy // 18 * 7, gpx * 12, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 2, gsy // 18 * 11, gpx * 6, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 7, gsy // 18 * 13, gpx * 5, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 9, gsy // 18 * 13, gpx * 1, gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 11, gsy // 18 * 11, gpx * 1, gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 13, gsy // 18 * 11, gpx * 3, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 15, gsy // 18 * 10, gpx * 1, gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 15, gsy // 18 * 4, gpx * 1, gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 15, gsy // 18 * 2, gpx * 1, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 15, gsy // 18 * 6, gpx * 9, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 23, gsy // 18 * 4, gpx * 4, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 23, gsy // 18 * 6, gpx * 1, gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 23, gsy // 18 * 13, gpx * 1, gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 26, gsy // 18 * 4, gpx * 1, gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 26, gsy // 18 * 6, gpx * 4, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        # controllo se le porte sono chiuse o aperte
        i = 0
        while i < len(porte):
            if not porte[i + 3]:
                if oggetto(porte[i + 1], porte[i + 2], gpx * 1, gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
            i = i + 4
        # controllo cofanetti
        i = 0
        while i < len(cofanetti):
            if oggetto(cofanetti[i + 1], cofanetti[i + 2], gpx * 1, gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            i = i + 4

    # movimento mostri veloci
    if (mostro or robo) and muovi > 0:
        muovi = muovi - 1
    # movimento mostri lenti
    if (mostro or robo) and muovi < 0:
        muovi = muovi + 1

    # movimento personaggio
    x = x + nx
    y = y + ny

    return x, y, stanza, carim, muovi, cambiosta


def trovacasattaccabili(x, y, stanza, porte, cofanetti):
    range = 6
    # caseattac[x, y, flag, ... ] -> per trovare gli ostacoli in basso a destra
    caseattac = []
    n = -1
    while n < range:
        m = 0
        while m <= range:
            murx = x + (gpx * n)
            mury = y + (gpy * m)
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, gpx, 0, stanza, False, 0, True, False, porte, cofanetti)
            if murx != nmurx:
                caseattac.append(nmurx)
                caseattac.append(nmury)
                caseattac.append(True)
            else:
                caseattac.append(nmurx + gpx)
                caseattac.append(nmury)
                caseattac.append(False)
            m = m + 1
        n = n + 1
    n = -1
    while n < range:
        m = 0
        while m <= range:
            murx = x + (gpx * m)
            mury = y + (gpy * n)
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, gpy, stanza, False, 0, True, False, porte, cofanetti)
            if mury == nmury:
                i = 0
                while i < len(caseattac):
                    if caseattac[i] == nmurx and caseattac[i + 1] == nmury + gpy:
                        caseattac[i + 2] = False
                        break
                    i = i + 3
            m = m + 1
        n = n + 1
    #  caseattacbassodestra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli in basso a destra
    caseattacbassodestra = []
    # riempio caseattacbassodestra come se tutto il campo in basso a destra fosse libero
    n = 0
    while n <= range:
        m = 0
        while m <= range:
            caseattacbassodestra.append(x + (gpx * n))
            caseattacbassodestra.append(y + (gpy * m))
            caseattacbassodestra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacbassodestra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # situazione: 1a basso-destra
            if caseattac[i] == x and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione <= 6:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 9 and posizione <= 13:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 17 and posizione <= 20:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 41:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 2a basso-destra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 2 and posizione <= 6:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 10 and posizione <= 13:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 19 and posizione <= 20:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 3a basso-destra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 3 and posizione <= 6:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 12 and posizione <= 13:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 4a basso-destra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 4 and posizione <= 6:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 13:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5a basso-destra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 5 and posizione <= 6:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5.5a basso-destra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 6:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 6ab basso-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 8 and posizione <= 9:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 15 and posizione <= 19:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 23 and posizione <= 27:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 30 and posizione <= 34:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 37 and posizione <= 41:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 45 and posizione <= 48:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 7a basso-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 9 and posizione <= 11:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 17 and posizione <= 20:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 41:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 8a basso-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 10 and posizione <= 13:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 18 and posizione <= 20:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 27:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 9a basso-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 11 and posizione <= 13:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 19 and posizione <= 20:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10a basso-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 12 and posizione <= 13:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 20:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10.5a basso-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 13:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 11ab basso-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 16 and posizione <= 17:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 23 and posizione <= 25:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 31 and posizione <= 34:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 46 and posizione <= 48:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 12a basso-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 17 and posizione <= 18:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 41:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 13a basso-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 18 and posizione <= 20:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 26 and posizione <= 27:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 34:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14a basso-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 19 and posizione <= 20:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 27:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14.5a basso-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 20:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 15ab basso-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 24 and posizione <= 25:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 31 and posizione <= 33:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 16a basso-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 25 and posizione <= 26:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 41:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17a basso-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 26 and posizione <= 27:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 34:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17.5a basso-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 27:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 18ab basso-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 32 and posizione <= 33:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19a basso-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 41:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19a basso-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 41:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19.5a basso-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 34:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20ab basso-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 40 and posizione <= 41:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.5a basso-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 41:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.75ab basso-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 48:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 1b basso-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 7:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 14 and posizione <= 15:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 21 and posizione <= 23:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 28 and posizione <= 31:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 35 and posizione <= 39:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 42 and posizione <= 47:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 2b basso-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 14:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 21 and posizione <= 22:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 28 and posizione <= 29:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 35 and posizione <= 37:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 42 and posizione <= 44:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 3b basso-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 21:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 28:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 35 and posizione <= 36:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 42 and posizione <= 43:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 4b basso-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 28:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 35:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 42 and posizione <= 43:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5b basso-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 35:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 42:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5.5b basso-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 42:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 7b basso-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 15:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 22 and posizione <= 23:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 29 and posizione <= 31:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 37 and posizione <= 39:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 44 and posizione <= 47:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 8b basso-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 22:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 29 and posizione <= 30:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 36 and posizione <= 37:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 43 and posizione <= 45:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 9b basso-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 29:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 36 and posizione <= 37:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 43 and posizione <= 44:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10b basso-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 36:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 43 and posizione <= 44:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10.5b basso-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 43:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 12b basso-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 23:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 30 and posizione <= 31:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 38 and posizione <= 39:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 45 and posizione <= 47:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 13b basso-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 30:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 37 and posizione <= 38:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 44 and posizione <= 46:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14b basso-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 37:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 44 and posizione <= 45:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14.5b basso-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 44:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 16b basso-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 31:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 38 and posizione <= 39:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 46 and posizione <= 47:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17b basso-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 38:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 45 and posizione <= 46:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17.5b basso-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 45:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19b basso-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 39:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 46 and posizione <= 47:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19.5b basso-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 46:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.5b basso-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 47:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
        i = i + 3

    # caseattac[x, y, flag, ... ] -> per trovare gli ostacoli in basso a sinistra
    caseattac = []
    n = -1
    while n < range:
        m = 0
        while m <= range:
            murx = x - (gpx * n)
            mury = y + (gpy * m)
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, -gpx, 0, stanza, False, 0, True, False, porte, cofanetti)
            if murx != nmurx:
                caseattac.append(nmurx)
                caseattac.append(nmury)
                caseattac.append(True)
            else:
                caseattac.append(nmurx - gpx)
                caseattac.append(nmury)
                caseattac.append(False)
            m = m + 1
        n = n + 1
    n = -1
    while n < range:
        m = 0
        while m <= range:
            murx = x - (gpx * m)
            mury = y + (gpy * n)
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, gpy, stanza, False, 0, True, False, porte, cofanetti)
            if mury == nmury:
                i = 0
                while i < len(caseattac):
                    if caseattac[i] == nmurx and caseattac[i + 1] == nmury + gpy:
                        caseattac[i + 2] = False
                        break
                    i = i + 3
            m = m + 1
        n = n + 1
    #  caseattacbassosinistra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli in basso a sinistra
    caseattacbassosinistra = []
    # riempio caseattacbassosinistra come se tutto il campo in basso a sinistra fosse libero
    n = 0
    while n <= range:
        m = 0
        while m <= range:
            caseattacbassosinistra.append(x - (gpx * n))
            caseattacbassosinistra.append(y + (gpy * m))
            caseattacbassosinistra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacbassosinistra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # situazione: 1a basso-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione <= 6:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 9 and posizione <= 13:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 17 and posizione <= 20:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 2a basso-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 2 and posizione <= 6:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 10 and posizione <= 13:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 19 and posizione <= 20:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 3a basso-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 3 and posizione <= 6:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 12 and posizione <= 13:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 4a basso-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 4 and posizione <= 6:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 13:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5a basso-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 5 and posizione <= 6:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5.5a basso-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 6:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 6ab basso-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 8 and posizione <= 9:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 15 and posizione <= 19:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 23 and posizione <= 27:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 30 and posizione <= 34:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 37 and posizione <= 41:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 45 and posizione <= 48:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 7a basso-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 9 and posizione <= 11:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 17 and posizione <= 20:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 8a basso-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 10 and posizione <= 13:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 18 and posizione <= 20:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 27:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 9a basso-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 11 and posizione <= 13:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 19 and posizione <= 20:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10a basso-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 12 and posizione <= 13:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 20:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10.5a basso-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 13:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 11ab basso-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 16 and posizione <= 17:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 23 and posizione <= 25:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 31 and posizione <= 34:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 46 and posizione <= 48:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 12a basso-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 17 and posizione <= 18:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 13a basso-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 18 and posizione <= 20:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 26 and posizione <= 27:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 34:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14a basso-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 19 and posizione <= 20:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 27:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14.5a basso-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 20:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 15ab basso-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 24 and posizione <= 25:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 31 and posizione <= 33:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 16a basso-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 25 and posizione <= 26:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17a basso-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 26 and posizione <= 27:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 34:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17.5a basso-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 27:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 18ab basso-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 32 and posizione <= 33:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19a basso-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19a basso-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19.5a basso-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 34:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20ab basso-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 40 and posizione <= 41:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.5a basso-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 41:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.75ab basso-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 48:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 1b basso-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 7:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 14 and posizione <= 15:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 21 and posizione <= 23:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 28 and posizione <= 31:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 35 and posizione <= 39:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 42 and posizione <= 47:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 2b basso-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 14:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 21 and posizione <= 22:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 28 and posizione <= 29:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 35 and posizione <= 37:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 42 and posizione <= 44:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 3b basso-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 21:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 28:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 35 and posizione <= 36:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 42 and posizione <= 43:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 4b basso-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 28:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 35:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 42 and posizione <= 43:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5b basso-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 35:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 42:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5.5b basso-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 42:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 7b basso-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 15:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 22 and posizione <= 23:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 29 and posizione <= 31:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 37 and posizione <= 39:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 44 and posizione <= 47:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 8b basso-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 22:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 29 and posizione <= 30:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 36 and posizione <= 37:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 43 and posizione <= 45:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 9b basso-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 29:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 36 and posizione <= 37:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 43 and posizione <= 44:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10b basso-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 36:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 43 and posizione <= 44:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10.5b basso-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 43:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 12b basso-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 23:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 30 and posizione <= 31:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 38 and posizione <= 39:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 45 and posizione <= 47:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 13b basso-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 30:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 37 and posizione <= 38:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 44 and posizione <= 46:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14b basso-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 37:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 44 and posizione <= 45:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14.5b basso-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 44:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 16b basso-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 31:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 38 and posizione <= 39:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 46 and posizione <= 47:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17b basso-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 38:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 45 and posizione <= 46:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17.5b basso-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 45:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19b basso-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 39:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 46 and posizione <= 47:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19.5b basso-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 46:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.5b basso-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 47:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
        i = i + 3

    # caseattac[x, y, flag, ... ] -> per trovare gli ostacoli in alto a sinistra
    caseattac = []
    n = -1
    while n < range:
        m = 0
        while m <= range:
            murx = x - (gpx * n)
            mury = y - (gpy * m)
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, -gpx, 0, stanza, False, 0, True, False, porte, cofanetti)
            if murx != nmurx:
                caseattac.append(nmurx)
                caseattac.append(nmury)
                caseattac.append(True)
            else:
                caseattac.append(nmurx - gpx)
                caseattac.append(nmury)
                caseattac.append(False)
            m = m + 1
        n = n + 1
    n = -1
    while n < range:
        m = 0
        while m <= range:
            murx = x - (gpx * m)
            mury = y - (gpy * n)
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, -gpy, stanza, False, 0, True, False, porte, cofanetti)
            if mury == nmury:
                i = 0
                while i < len(caseattac):
                    if caseattac[i] == nmurx and caseattac[i + 1] == nmury - gpy:
                        caseattac[i + 2] = False
                        break
                    i = i + 3
            m = m + 1
        n = n + 1
    # caseattacaltosinistra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli in alto a sinistra
    caseattacaltosinistra = []
    # riempio caseattacaltosinistra come se tutto il campo in alto a sinistra fosse libero
    n = 0
    while n <= range:
        m = 0
        while m <= range:
            caseattacaltosinistra.append(x - (gpx * n))
            caseattacaltosinistra.append(y - (gpy * m))
            caseattacaltosinistra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacaltosinistra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # situazione: 1a alto-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione <= 6:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 9 and posizione <= 13:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 17 and posizione <= 20:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 2a alto-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 2 and posizione <= 6:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 10 and posizione <= 13:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 19 and posizione <= 20:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 3a alto-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 3 and posizione <= 6:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 12 and posizione <= 13:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 4a alto-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 4 and posizione <= 6:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 13:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5a alto-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 5 and posizione <= 6:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5.5a alto-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 6:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 6ab alto-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 8 and posizione <= 9:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 15 and posizione <= 19:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 23 and posizione <= 27:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 30 and posizione <= 34:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 37 and posizione <= 41:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 45 and posizione <= 48:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 7a alto-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 9 and posizione <= 11:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 17 and posizione <= 20:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 8a alto-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 10 and posizione <= 13:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 18 and posizione <= 20:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 27:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 9a alto-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 11 and posizione <= 13:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 19 and posizione <= 20:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10a alto-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 12 and posizione <= 13:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 20:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10.5a alto-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 13:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 11ab alto-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 16 and posizione <= 17:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 23 and posizione <= 25:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 31 and posizione <= 34:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 46 and posizione <= 48:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 12a alto-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 17 and posizione <= 18:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 13a alto-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 18 and posizione <= 20:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 26 and posizione <= 27:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 34:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14a alto-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 19 and posizione <= 20:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 27:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14.5a alto-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 20:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 15ab alto-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 24 and posizione <= 25:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 31 and posizione <= 33:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 16a alto-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 25 and posizione <= 26:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17a alto-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 26 and posizione <= 27:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 34:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17.5a alto-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 27:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 18ab alto-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 32 and posizione <= 33:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19a alto-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19a alto-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19.5a alto-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 34:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20ab alto-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 40 and posizione <= 41:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.5a alto-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 41:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.75ab alto-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 48:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 1b alto-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 7:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 14 and posizione <= 15:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 21 and posizione <= 23:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 28 and posizione <= 31:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 35 and posizione <= 39:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 42 and posizione <= 47:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 2b alto-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 14:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 21 and posizione <= 22:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 28 and posizione <= 29:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 35 and posizione <= 37:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 42 and posizione <= 44:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 3b alto-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 21:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 28:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 35 and posizione <= 36:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 42 and posizione <= 43:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 4b alto-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 28:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 35:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 42 and posizione <= 43:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5b alto-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 35:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 42:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5.5b alto-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 42:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 7b alto-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 15:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 22 and posizione <= 23:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 29 and posizione <= 31:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 37 and posizione <= 39:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 44 and posizione <= 47:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 8b alto-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 22:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 29 and posizione <= 30:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 36 and posizione <= 37:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 43 and posizione <= 45:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 9b alto-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 29:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 36 and posizione <= 37:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 43 and posizione <= 44:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10b alto-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 36:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 43 and posizione <= 44:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10.5b alto-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 43:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 12b alto-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 23:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 30 and posizione <= 31:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 38 and posizione <= 39:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 45 and posizione <= 47:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 13b alto-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 30:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 37 and posizione <= 38:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 44 and posizione <= 46:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14b alto-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 37:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 44 and posizione <= 45:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14.5b alto-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 44:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 16b alto-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 31:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 38 and posizione <= 39:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 46 and posizione <= 47:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17b alto-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 38:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 45 and posizione <= 46:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17.5b alto-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 45:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19b alto-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 39:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 46 and posizione <= 47:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19.5b alto-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 46:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.5b alto-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 47:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
        i = i + 3

    # caseattac[x, y, flag, ... ] -> per trovare gli ostacoli in alto a destra
    caseattac = []
    n = -1
    while n < range:
        m = 0
        while m <= range:
            murx = x + (gpx * n)
            mury = y - (gpy * m)
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, gpx, 0, stanza, False, 0, True, False, porte, cofanetti)
            if murx != nmurx:
                caseattac.append(nmurx)
                caseattac.append(nmury)
                caseattac.append(True)
            else:
                caseattac.append(nmurx + gpx)
                caseattac.append(nmury)
                caseattac.append(False)
            m = m + 1
        n = n + 1
    n = -1
    while n < range:
        m = 0
        while m <= range:
            murx = x + (gpx * m)
            mury = y - (gpy * n)
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, -gpy, stanza, False, 0, True, False, porte, cofanetti)
            if mury == nmury:
                i = 0
                while i < len(caseattac):
                    if caseattac[i] == nmurx and caseattac[i + 1] == nmury - gpy:
                        caseattac[i + 2] = False
                        break
                    i = i + 3
            m = m + 1
        n = n + 1
    # caseattacaltodestra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli in alto a destra
    caseattacaltodestra = []
    # riempio caseattacaltosinistra come se tutto il campo in alto a destra fosse libero
    n = 0
    while n <= range:
        m = 0
        while m <= range:
            caseattacaltodestra.append(x + (gpx * n))
            caseattacaltodestra.append(y - (gpy * m))
            caseattacaltodestra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacaltodestra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # situazione: 1a alto-destra
            if caseattac[i] == x and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione <= 6:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 9 and posizione <= 13:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 17 and posizione <= 20:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 41:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 2a alto-destra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 2 and posizione <= 6:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 10 and posizione <= 13:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 19 and posizione <= 20:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 3a alto-destra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 3 and posizione <= 6:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 12 and posizione <= 13:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 4a alto-destra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 4 and posizione <= 6:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 13:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5a alto-destra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 5 and posizione <= 6:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5.5a alto-destra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 6:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 6ab alto-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 8 and posizione <= 9:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 15 and posizione <= 19:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 23 and posizione <= 27:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 30 and posizione <= 34:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 37 and posizione <= 41:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 45 and posizione <= 48:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 7a alto-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 9 and posizione <= 11:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 17 and posizione <= 20:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 41:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 8a alto-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 10 and posizione <= 13:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 18 and posizione <= 20:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 27:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 9a alto-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 11 and posizione <= 13:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 19 and posizione <= 20:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10a alto-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 12 and posizione <= 13:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 20:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10.5a alto-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 13:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 11ab alto-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 16 and posizione <= 17:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 23 and posizione <= 25:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 31 and posizione <= 34:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 46 and posizione <= 48:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 12a alto-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 17 and posizione <= 18:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 41:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 13a alto-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 18 and posizione <= 20:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 26 and posizione <= 27:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 34:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14a alto-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 19 and posizione <= 20:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 27:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14.5a alto-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 20:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 15ab alto-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 24 and posizione <= 25:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 31 and posizione <= 33:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 16a alto-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 25 and posizione <= 26:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 41:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17a alto-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 26 and posizione <= 27:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 34:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17.5a alto-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 27:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 18ab alto-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 32 and posizione <= 33:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19a alto-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 41:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19a alto-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 41:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19.5a alto-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 34:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20ab alto-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 40 and posizione <= 41:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.5a alto-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 41:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.75ab alto-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 48:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 1b alto-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 7:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 14 and posizione <= 15:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 21 and posizione <= 23:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 28 and posizione <= 31:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 35 and posizione <= 39:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 42 and posizione <= 47:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 2b alto-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 14:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 21 and posizione <= 22:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 28 and posizione <= 29:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 35 and posizione <= 37:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 42 and posizione <= 44:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 3b alto-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 21:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 28:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 35 and posizione <= 36:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 42 and posizione <= 43:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 4b alto-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 28:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 35:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 42 and posizione <= 43:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5b alto-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 35:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 42:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5.5b alto-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 42:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 7b alto-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 15:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 22 and posizione <= 23:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 29 and posizione <= 31:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 37 and posizione <= 39:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 44 and posizione <= 47:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 8b alto-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 22:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 29 and posizione <= 30:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 36 and posizione <= 37:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 43 and posizione <= 45:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 9b alto-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 29:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 36 and posizione <= 37:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 43 and posizione <= 44:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10b alto-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 36:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 43 and posizione <= 44:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10.5b alto-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 43:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 12b alto-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 23:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 30 and posizione <= 31:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 38 and posizione <= 39:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 45 and posizione <= 47:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 13b alto-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 30:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 37 and posizione <= 38:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 44 and posizione <= 46:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14b alto-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 37:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 44 and posizione <= 45:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14.5b alto-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 44:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 16b alto-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 31:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 38 and posizione <= 39:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 46 and posizione <= 47:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17b alto-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 38:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 45 and posizione <= 46:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17.5b alto-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 45:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19b alto-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 39:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 46 and posizione <= 47:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19.5b alto-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 46:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.5b alto-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 47:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
        i = i + 3

    # caseattactot[x, y, flag, ... ] -> per definire la visibilita' ridotta da tutti gli ostacoli
    caseattactot = caseattacaltodestra + caseattacaltosinistra + caseattacbassodestra + caseattacbassosinistra

    return caseattactot


def movmostro(x, y, rx, ry, mx, my, stanza, tipo, muovimost, visto, dif, difro, par, dati, statom, vitaesca, porte, cofanetti):
    sposta = False
    mostro = True
    attrobo = False
    nmos = 0
    nmx = 0
    nmy = 0
    vistoesca = False
    escabersaglio = 0

    # burocrazia
    carim = False

    if visto:
        visto = False

    # caratteristiche nemici
    if tipo == "mostro":
        attlontano = True
        vistam = gpx * 5
        att = 10
        if muovimost == 0:
            if statom == 2 or statom == 3:
                muovimost = -2
            else:
                muovimost = 0
    if tipo == "pipistrello":
        attlontano = False
        vistam = gpx * 6
        att = 5
        if muovimost == 0:
            if statom == 2 or statom == 3:
                muovimost = 0
            else:
                muovimost = 2
    if tipo == "orco":
        attlontano = False
        vistam = gpx * 5
        att = 15
        if muovimost == 0:
            if statom == 2 or statom == 3:
                muovimost = -3
            else:
                muovimost = -2
    if tipo == 0:
        attlontano = False
        vistam = 0
        att = 0

    # movimenti verso esche o casuali
    primaesca = True
    i = 0
    while i < len(vitaesca):
        if abs(vitaesca[i + 2] - mx) <= vistam and abs(vitaesca[i + 3] - my) <= vistam:
            if primaesca:
                distminx = vitaesca[i + 2]
                distminy = vitaesca[i + 3]
                escabersaglio = i
                vistoesca = True
                primaesca = False
            if not primaesca and (abs(vitaesca[i + 2] - mx) + abs(vitaesca[i + 3] - my) < abs(distminx - mx) + abs(distminy - my)):
                distminx = vitaesca[i + 2]
                distminy = vitaesca[i + 3]
                escabersaglio = i
            # controllo caselle che si vedono
            caseattactot = trovacasattaccabili(mx, my, stanza, porte, cofanetti)
            j = 0
            while j < len(caseattactot):
                if caseattactot[j] == distminx and caseattactot[j + 1] == distminy and not caseattactot[j + 2]:
                    distminx = 0
                    distminy = 0
                    escabersaglio = 0
                    vistoesca = False
                    primaesca = True
                j = j + 3
        i = i + 4
    vistoprov1 = False
    vistoprov2 = False
    if not visto and not vistoesca:
        # controllo caselle che si vedono per pers e robo
        caseattactot = trovacasattaccabili(mx, my, stanza, porte, cofanetti)
        if abs(x - mx) <= vistam and abs(y - my) <= vistam and dati[5] > 0:
            j = 0
            while j < len(caseattactot):
                if caseattactot[j] == x and caseattactot[j + 1] == y:
                    if not caseattactot[j + 2]:
                        vistoprov1 = False
                    else:
                        vistoprov1 = True
                    break
                j = j + 3
        if abs(rx - mx) <= vistam and abs(ry - my) <= vistam and dati[10] > 0:
            j = 0
            while j < len(caseattactot):
                if caseattactot[j] == rx and caseattactot[j + 1] == ry:
                    if not caseattactot[j + 2]:
                        vistoprov2 = False
                    else:
                        vistoprov2 = True
                    break
                j = j + 3
            if dati[10] <= 0:
                vistoprov2 = False
        if vistoprov1 or vistoprov2:
            visto = True
        if not visto:
            nmos = random.randint(1, 4)
            sposta = True

    if (visto or vistoesca) and muovimost >= -1:
        if ((abs(rx - mx) + abs(ry - my)) < (abs(x - mx) + abs(y - my)) or not vistoprov1) and vistoprov2 and dati[10] > 0 and not vistoesca:
            x = rx
            y = ry
            attrobo = True
        if vistoesca:
            x = vitaesca[escabersaglio + 2]
            y = vitaesca[escabersaglio + 3]

        # nemici che attaccano da vicino
        if not attlontano:
            if abs(x - mx) > abs(y - my):
                if mx < x:
                    nmos = 1
                if mx > x:
                    nmos = 2
                sposta = True
            if abs(y - my) > abs(x - mx):
                if my < y:
                    nmos = 3
                if my > y:
                    nmos = 4
                sposta = True
            if (abs(x - mx) == abs(y - my)) and (x != mx) and (y != my):
                c = random.randint(1, 2)
                if mx < x and c == 1:
                    nmos = 1
                if mx > x and c == 1:
                    nmos = 2
                if my < y and c == 2:
                    nmos = 3
                if my > y and c == 2:
                    nmos = 4
                sposta = True
            if (x == mx + gpx and y == my) or (x == mx - gpx and y == my) or (x == mx and y == my + gpy) or (x == mx and y == my - gpy) or ((x == mx) and (y == my)):
                if vistoesca:
                    danno = att
                    if danno < 0:
                        danno = 0
                    print ("attacco vicino", tipo, "a esca", danno)
                    vitaesca[escabersaglio + 1] = vitaesca[escabersaglio + 1] - danno
                else:
                    if attrobo:
                        danno = att - difro
                        if danno < 0:
                            danno = 0
                        print ("attacco vicino", tipo, "a robo", danno)
                        dati[10] = dati[10] - danno
                    else:
                        danno = att - dif
                        if danno < 0:
                            danno = 0
                        if random.randint(1, 100) <= par and dati[7] > 0:
                            danno = 0
                            print ("parato:", par)
                        print ("attacco vicino", tipo, "a rallo", danno)
                        dati[5] = dati[5] - danno
                nmos = 0
                if x == mx + gpx and y == my:
                    nmos = 1
                if x == mx - gpx and y == my:
                    nmos = 2
                if x == mx and y == my + gpy:
                    nmos = 3
                if x == mx and y == my - gpy:
                    nmos = 4
                sposta = False

        # nemici che attaccano da lontano
        if attlontano:
            if vistoesca:
                danno = att
                if danno < 0:
                    danno = 0
                print ("attacco lontano", tipo, "a esca", danno)
                vitaesca[escabersaglio + 1] = vitaesca[escabersaglio + 1] - danno
            else:
                if attrobo:
                    danno = att - difro
                    if danno < 0:
                        danno = 0
                    print ("attacco lontano", tipo, "a robo", danno)
                    dati[10] = dati[10] - danno
                else:
                    danno = att - dif
                    if danno < 0:
                        danno = 0
                    if random.randint(1, 100) <= par and dati[7] > 0:
                        danno = 0
                        print ("parato:", par)
                    print ("attacco lontano", tipo, "a rallo", danno)
                    dati[5] = dati[5] - danno
            nmos = 0
            if abs(x - mx) > abs(y - my):
                if mx < x:
                    nmos = 1
                if mx > x:
                    nmos = 2
            if abs(y - my) > abs(x - mx):
                if my < y:
                    nmos = 3
                if my > y:
                    nmos = 4
            sposta = False

    # spostamento
    if sposta:
        if nmos == 1:
            if mx + gpx == x and my == y:
                nmx = 0
                nmy = 0
            else:
                nmx = gpx
                nmy = 0
            i = 2
            while i <= len(vitaesca):
                if mx + gpx == vitaesca[i] and my == vitaesca[i + 1]:
                    nmx = 0
                    nmy = 0
                i = i + 4
        if nmos == 2:
            if mx - gpx == x and my == y:
                nmx = 0
                nmy = 0
            else:
                nmx = -gpx
                nmy = 0
            i = 2
            while i <= len(vitaesca):
                if mx - gpx == vitaesca[i] and my == vitaesca[i + 1]:
                    nmx = 0
                    nmy = 0
                i = i + 4
        if nmos == 3:
            if mx == x and my + gpy == y:
                nmx = 0
                nmy = 0
            else:
                nmx = 0
                nmy = gpy
            i = 2
            while i <= len(vitaesca):
                if mx == vitaesca[i] and my + gpy == vitaesca[i + 1]:
                    nmx = 0
                    nmy = 0
                i = i + 4
        if nmos == 4:
            if mx == x and my - gpy == y:
                nmx = 0
                nmy = 0
            else:
                nmx = 0
                nmy = -gpy
            i = 2
            while i <= len(vitaesca):
                if mx == vitaesca[i] and my - gpy == vitaesca[i + 1]:
                    nmx = 0
                    nmy = 0
                i = i + 4

    if muovimost < -1:
        nmos = 0

    # alcuni sono inutili!!!
    mx, my, stanza, carim, muovimost, cambiosta = muri_porte(mx, my, nmx, nmy, stanza, carim, muovimost, mostro, False, porte, cofanetti)
    return mx, my, muovimost, nmos, visto, dati, vitaesca, vistam


def movrobo(x, y, vx, vy, rx, ry, stanza, muovirob, chiamarob, dati, porte, cofanetti):
    robo = True
    nrx = 0
    nry = 0

    # burocrazia
    carim = False

    nrob = 0
    sposta = False
    # movimento robot
    # no mostri
    if chiamarob:
        if abs(x - rx) > abs(y - ry):
            if rx < x:
                nrob = 1
            if rx > x:
                nrob = 2
            sposta = True
        if abs(y - ry) > abs(x - rx):
            if ry < y:
                nrob = 3
            if ry > y:
                nrob = 4
            sposta = True
        if (abs(x - rx) == abs(y - ry)) and (x != rx) and (y != ry):
            if abs(x - rx) == gpx:
                if vx == rx + gpx:
                    nrob = 1
                if vx == rx - gpx:
                    nrob = 2
                if vy == ry + gpy:
                    nrob = 3
                if vy == ry - gpy:
                    nrob = 4
            else:
                c = random.randint(1, 2)
                if rx < x and c == 1:
                    nrob = 1
                if rx > x and c == 1:
                    nrob = 2
                if ry < y and c == 2:
                    nrob = 3
                if ry > y and c == 2:
                    nrob = 4
            sposta = True
    # mostri si (gambit)
    elif muovirob >= -1:
        # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)-condizioni(20)-gambit(20) // dimensione: 0-120
        esecuzione = False
        condizione = False
        azione = False
        print ("gambit")

    # spostamento
    if sposta:
        if nrob == 1:
            if rx + gpx == x and ry == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = gpx
                nry = 0
        if nrob == 2:
            if rx - gpx == x and ry == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = -gpx
                nry = 0
        if nrob == 3:
            if rx == x and ry + gpy == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = 0
                nry = gpy
        if nrob == 4:
            if rx == x and ry - gpy == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = 0
                nry = -gpy

    # alcuni sono inutili!!!
    rx, ry, stanza, carim, muovirob, cambiosta = muri_porte(rx, ry, nrx, nry, stanza, carim, muovirob, False, robo, porte, cofanetti)
    return rx, ry, muovirob, nrob, dati


def aperturacofanetto(stanza, cx, cy, dati):
    # 11-30 -> tecniche(20) / 31-40 -> oggetti(10) / 41-70 -> armi(30) / 71-80 -> batterie(10) / 81-100 -> condizioni(20) / 101-120 -> gambit (=celle di memoria)(20)
    if stanza == 1:
        if cx == gpx * 3 and cy == gpy * 7:
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
    if stanza == 1:
        if cx == gpx * 7 and cy == gpy * 12:
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
    if stanza == 1:
        if cx == gpx * 12 and cy == gpy * 11:
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
    if stanza == 2:
        if cx == gpx * 3 and cy == gpy * 5:
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
    if stanza == 2:
        if cx == gpx * 5 and cy == gpy * 10:
            tesoro = 11
    if stanza == 2:
        if cx == gpx * 10 and cy == gpy * 9:
            tesoro = 81
    if dati[tesoro] <= -1 and (tesoro >= 31 and tesoro <= 40):
        dati[tesoro] = dati[tesoro] + 2
    else:
        dati[tesoro] = dati[tesoro] + 1
    return dati, tesoro


def scopriCaselleViste(x, y, numstanza, porte, cofanetti, caseviste):
    # contiene x e y delle caselle già esplorate
    caselleEsplorate = [x, y]

    # imposto tutte le caselle come non viste in caseviste
    i = 0
    while i < len(caseviste):
        caseviste[i + 2] = False
        i = i + 3

    j = 0
    while j < len(caselleEsplorate):
        nx, ny, stanza, carim, muovi, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -gpy, numstanza, False, 0, True, False, porte, cofanetti)
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
                i += 3
        nx, ny, stanza, carim, muovi, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, gpy, numstanza, False, 0, True, False, porte, cofanetti)
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
                i += 3
        nx, ny, stanza, carim, muovi, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], -gpx, 0, numstanza, False, 0, True, False, porte, cofanetti)
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
                i += 3
        nx, ny, stanza, carim, muovi, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], gpx, 0, numstanza, False, 0, True, False, porte, cofanetti)
        if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
            giaVisitata = False
            k = 0
            print caselleEsplorate
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
                i += 3
        j += 2

    return caseviste
