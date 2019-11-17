# -*- coding: utf-8 -*-

import os
import random
from GlobalVarG2 import *


def messaggio(msg, colore, x, y, gr):
    gr = gr - 10
    gr = gpx * gr // 60
    y = y - (gpy // 8)
    carattere = "Gentium Book Basic"
    font = pygame.font.SysFont(carattere, gr)
    testo = font.render(msg, True, colore)
    schermo.blit(testo, (x, y))


def getStatistiche(dati, difesa = 0):
    """pvtot = 100 + (dati[4] * 5)
    att = 10 + (dati[4] * 2) + (dati[6] * 10)
    dif = 10 + (dati[4] * 2) + (dati[8] * 10) + 5 + (dati[7] * 5)"""
    esptot = pow(dati[4], 2) + (dati[4] * 10)
    pvtot = 50
    attVicino = 14 + ((dati[6] * dati[6]) * 10)
    attLontano = 12 + ((dati[128] * dati[128]) * 5)
    # velFrecce indica le caselle al turno fatte dalle frecce lanciate
    velFrecce = 4 + (dati[128] * dati[128])
    dif = 7 + ((dati[8] * dati[8]) * 10) + 5 + ((dati[7] * dati[7]) * 5)
    par = 3 + ((dati[7] * dati[7]) * 3)
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
                attVicino += (i * 2)
                attLontano += i
                break
            i += 3

    if dati[4] >= 3:
        i = 3
        while i <= 100:
            if dati[4] <= i + 2:
                dif += (i * 2)
                break
            i += 3

    entot = 240 + (dati[9] * dati[9] * 60)
    difro = 20 + (dati[9] * dati[9] * 30)

    return esptot, pvtot, entot, attVicino, attLontano, velFrecce, dif, difro, par


def guardaVideo(path, audio=0):
    schermo.fill(grigioscu)
    pygame.display.update()
    listaImg = []
    # load all the images
    for i in os.listdir(path):
        img = pygame.image.load(path + '/' + i).convert()
        img = pygame.transform.scale(img, (gsx, gsy))
        listaImg.append(img)
    if audio != 0:
        canaleSoundCanzone.play(audio)
    # play video
    i = 0
    while i < len(listaImg) + 10:
        if i >= 10:
            schermo.blit(listaImg[i - 10], (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    canaleSoundPuntatore.play(selezione)
                    if audio != 0:
                        canaleSoundCanzone.stop()
                    return True
        pygame.event.pump()
        clockVideo.tick(fpsVideo)
        i += 1
    if audio != 0:
        canaleSoundCanzone.stop()
    return False


def salvataggio(n, dati, porteini, portefin, cofaniini, cofanifin, porte, cofanetti):
    scrivi = open("Salvataggi/Salvataggio%i.txt" % n, "w")
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


def muri_porte(x, y, nx, ny, stanza, carim, mostro, robo, porte, cofanetti):
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

    # movimento personaggio
    x = x + nx
    y = y + ny

    return x, y, stanza, carim, cambiosta


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
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, gpx, 0, stanza, False, True, False, porte, cofanetti)
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
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, 0, gpy, stanza, False, True, False, porte, cofanetti)
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
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, -gpx, 0, stanza, False, True, False, porte, cofanetti)
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
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, 0, gpy, stanza, False, True, False, porte, cofanetti)
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
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, -gpx, 0, stanza, False, True, False, porte, cofanetti)
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
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, 0, -gpy, stanza, False, True, False, porte, cofanetti)
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
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, gpx, 0, stanza, False, True, False, porte, cofanetti)
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
            nmurx, nmury, stanza, carim, cambiosta = muri_porte(murx, mury, 0, -gpy, stanza, False, True, False, porte, cofanetti)
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


def aperturacofanetto(stanza, cx, cy, dati):
    tesoro = -1
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
        if cx == gpx * 5 and cy == gpy * 10:
            tesoro = 11
        if cx == gpx * 10 and cy == gpy * 9:
            tesoro = 81

    # assegna oggetto ottenuto
    if tesoro != -1:
        if dati[tesoro] <= -1 and (tesoro >= 31 and tesoro <= 40):
            dati[tesoro] = dati[tesoro] + 2
        else:
            if tesoro >= 101 and tesoro <= 120:
                dati[tesoro] = dati[tesoro] + 1
                dati[tesoro + 10] = dati[tesoro + 10] + 1
            else:
                dati[tesoro] = dati[tesoro] + 1
    return dati, tesoro


def scopriCaselleViste(x, y, rx, ry, numstanza, porte, cofanetti, caseviste):
    # contiene x e y delle caselle già esplorate
    caselleEsplorate = [x, y]

    # imposto tutte le caselle come non viste in caseviste
    i = 0
    while i < len(caseviste):
        caseviste[i + 2] = False
        i = i + 3

    # caselle viste da rallo
    j = 0
    while j < len(caselleEsplorate):
        nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -gpy, numstanza, False, True, False, porte, cofanetti)
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
        nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, gpy, numstanza, False, True, False, porte, cofanetti)
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
        nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], -gpx, 0, numstanza, False, True, False, porte, cofanetti)
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
        nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], gpx, 0, numstanza, False, True, False, porte, cofanetti)
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
        if caseviste[i + 2] and caseviste[i] == rx and caseviste[i + 1] == ry:
            incasevista = True
            break
        i = i + 3
    if not incasevista:
        caselleEsplorate = [rx, ry]
        j = 0
        while j < len(caselleEsplorate):
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -gpy, numstanza, False, True, False, porte, cofanetti)
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
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, gpy, numstanza, False, True, False, porte, cofanetti)
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
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], -gpx, 0, numstanza, False, True, False, porte, cofanetti)
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
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], gpx, 0, numstanza, False, True, False, porte, cofanetti)
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

    return caseviste


def pathFinding(xPartenza, yPartenza, xArrivo, yArrivo, numstanza, porte, cofanetti, vetnemici):
    # caselleEsplorate contiene x, y e valore delle caselle già esplorate (il valore serve per trovare il percorso più breve)
    valoreCasella = 0
    caselleEsplorate = [xPartenza, yPartenza, valoreCasella]

    impossibileRaggiungere = False
    if xPartenza == xArrivo and yPartenza == yArrivo:
        percorsoTrovato = "arrivato"
    else:
        # caselle viste da Colco
        arrivato = False
        j = 0
        while j < len(caselleEsplorate):
            valoreCasella += 1
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -gpy, numstanza, False, True, False, porte, cofanetti)
            k = 0
            while k < len(vetnemici):
                if nx == vetnemici[k] and ny == vetnemici[k + 1]:
                    nx = caselleEsplorate[j]
                    ny = caselleEsplorate[j + 1]
                k += 2
            if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                giaVisitata = False
                k = 0
                while k < len(caselleEsplorate):
                    if caselleEsplorate[k] == nx and caselleEsplorate[k + 1] == ny:
                        giaVisitata = True
                        break
                    k += 3
                if not giaVisitata:
                    caselleEsplorate.append(nx)
                    caselleEsplorate.append(ny)
                    caselleEsplorate.append(valoreCasella)
            if nx == xArrivo and ny == yArrivo:
                arrivato = True
                break
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, gpy, numstanza, False, True, False, porte, cofanetti)
            k = 0
            while k < len(vetnemici):
                if nx == vetnemici[k] and ny == vetnemici[k + 1]:
                    nx = caselleEsplorate[j]
                    ny = caselleEsplorate[j + 1]
                k += 2
            if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                giaVisitata = False
                k = 0
                while k < len(caselleEsplorate):
                    if caselleEsplorate[k] == nx and caselleEsplorate[k + 1] == ny:
                        giaVisitata = True
                        break
                    k += 3
                if not giaVisitata:
                    caselleEsplorate.append(nx)
                    caselleEsplorate.append(ny)
                    caselleEsplorate.append(valoreCasella)
            if nx == xArrivo and ny == yArrivo:
                arrivato = True
                break
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], -gpx, 0, numstanza, False, True, False, porte, cofanetti)
            k = 0
            while k < len(vetnemici):
                if nx == vetnemici[k] and ny == vetnemici[k + 1]:
                    nx = caselleEsplorate[j]
                    ny = caselleEsplorate[j + 1]
                k += 2
            if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                giaVisitata = False
                k = 0
                while k < len(caselleEsplorate):
                    if caselleEsplorate[k] == nx and caselleEsplorate[k + 1] == ny:
                        giaVisitata = True
                        break
                    k += 3
                if not giaVisitata:
                    caselleEsplorate.append(nx)
                    caselleEsplorate.append(ny)
                    caselleEsplorate.append(valoreCasella)
            if nx == xArrivo and ny == yArrivo:
                arrivato = True
                break
            nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], gpx, 0, numstanza, False, True, False, porte, cofanetti)
            k = 0
            while k < len(vetnemici):
                if nx == vetnemici[k] and ny == vetnemici[k + 1]:
                    nx = caselleEsplorate[j]
                    ny = caselleEsplorate[j + 1]
                k += 2
            if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                giaVisitata = False
                k = 0
                while k < len(caselleEsplorate):
                    if caselleEsplorate[k] == nx and caselleEsplorate[k + 1] == ny:
                        giaVisitata = True
                        break
                    k += 3
                if not giaVisitata:
                    caselleEsplorate.append(nx)
                    caselleEsplorate.append(ny)
                    caselleEsplorate.append(valoreCasella)
            if nx == xArrivo and ny == yArrivo:
                arrivato = True
                break
            j += 3

        if arrivato:
            # percorsoTrovato contiene x e y per ogni casella del percorso da restituire
            percorsoTrovato = []
            finito = False
            j = len(caselleEsplorate) - 3
            while not finito and not impossibileRaggiungere:
                valoreCasella1 = -1
                valoreCasella2 = -1
                valoreCasella3 = -1
                valoreCasella4 = -1
                xCasella1 = 0
                yCasella1 = 0
                xCasella2 = 0
                yCasella2 = 0
                xCasella3 = 0
                yCasella3 = 0
                xCasella4 = 0
                yCasella4 = 0
                nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, -gpy, numstanza, False, True, False, porte, cofanetti)
                k = 0
                while k < len(vetnemici):
                    if nx == vetnemici[k] and ny == vetnemici[k + 1]:
                        nx = caselleEsplorate[j]
                        ny = caselleEsplorate[j + 1]
                    k += 2
                if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                    i = 0
                    while i < len(caselleEsplorate):
                        if caselleEsplorate[i] == nx and caselleEsplorate[i + 1] == ny:
                            valoreCasella1 = caselleEsplorate[i + 2]
                            xCasella1 = nx
                            yCasella1 = ny
                            break
                        i += 3
                nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], 0, gpy, numstanza, False, True, False, porte, cofanetti)
                k = 0
                while k < len(vetnemici):
                    if nx == vetnemici[k] and ny == vetnemici[k + 1]:
                        nx = caselleEsplorate[j]
                        ny = caselleEsplorate[j + 1]
                    k += 2
                if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                    i = 0
                    while i < len(caselleEsplorate):
                        if caselleEsplorate[i] == nx and caselleEsplorate[i + 1] == ny:
                            valoreCasella2 = caselleEsplorate[i + 2]
                            xCasella2 = nx
                            yCasella2 = ny
                            break
                        i += 3
                nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], -gpx, 0, numstanza, False, True, False, porte, cofanetti)
                k = 0
                while k < len(vetnemici):
                    if nx == vetnemici[k] and ny == vetnemici[k + 1]:
                        nx = caselleEsplorate[j]
                        ny = caselleEsplorate[j + 1]
                    k += 2
                if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                    i = 0
                    while i < len(caselleEsplorate):
                        if caselleEsplorate[i] == nx and caselleEsplorate[i + 1] == ny:
                            valoreCasella3 = caselleEsplorate[i + 2]
                            xCasella3 = nx
                            yCasella3 = ny
                            break
                        i += 3
                nx, ny, stanza, carim, cambiosta = muri_porte(caselleEsplorate[j], caselleEsplorate[j + 1], gpx, 0, numstanza, False, True, False, porte, cofanetti)
                k = 0
                while k < len(vetnemici):
                    if nx == vetnemici[k] and ny == vetnemici[k + 1]:
                        nx = caselleEsplorate[j]
                        ny = caselleEsplorate[j + 1]
                    k += 2
                if caselleEsplorate[j] != nx or caselleEsplorate[j + 1] != ny:
                    i = 0
                    while i < len(caselleEsplorate):
                        if caselleEsplorate[i] == nx and caselleEsplorate[i + 1] == ny:
                            valoreCasella4 = caselleEsplorate[i + 2]
                            xCasella4 = nx
                            yCasella4 = ny
                            break
                        i += 3

                if valoreCasella1 == -1 and valoreCasella2 == -1 and valoreCasella3 == -1 and valoreCasella4 == -1:
                    impossibileRaggiungere = True
                else:
                    if valoreCasella1 != -1:
                        valorePiuBasso = valoreCasella1
                        xProssimaCasella = xCasella1
                        yProssimaCasella = yCasella1
                    elif valoreCasella2 != -1:
                        valorePiuBasso = valoreCasella2
                        xProssimaCasella = xCasella2
                        yProssimaCasella = yCasella2
                    elif valoreCasella3 != -1:
                        valorePiuBasso = valoreCasella3
                        xProssimaCasella = xCasella3
                        yProssimaCasella = yCasella3
                    elif valoreCasella4 != -1:
                        valorePiuBasso = valoreCasella4
                        xProssimaCasella = xCasella4
                        yProssimaCasella = yCasella4
                    if valoreCasella2 != -1 and valoreCasella2 < valorePiuBasso:
                        valorePiuBasso = valoreCasella2
                        xProssimaCasella = xCasella2
                        yProssimaCasella = yCasella2
                    elif valoreCasella2 == valorePiuBasso and random.randint(1, 2) == 1:
                        xProssimaCasella = xCasella2
                        yProssimaCasella = yCasella2
                    if valoreCasella3 != -1 and valoreCasella3 < valorePiuBasso:
                        valorePiuBasso = valoreCasella3
                        xProssimaCasella = xCasella3
                        yProssimaCasella = yCasella3
                    elif valoreCasella3 == valorePiuBasso and random.randint(1, 2) == 1:
                        xProssimaCasella = xCasella3
                        yProssimaCasella = yCasella3
                    if valoreCasella4 != -1 and valoreCasella4 < valorePiuBasso:
                        valorePiuBasso = valoreCasella4
                        xProssimaCasella = xCasella4
                        yProssimaCasella = yCasella4
                    elif valoreCasella4 == valorePiuBasso and random.randint(1, 2) == 1:
                        xProssimaCasella = xCasella4
                        yProssimaCasella = yCasella4
                    percorsoTrovato.append(xProssimaCasella)
                    percorsoTrovato.append(yProssimaCasella)
                i = 0
                while i < len(caselleEsplorate):
                    if caselleEsplorate[i] == xProssimaCasella and caselleEsplorate[i + 1] == yProssimaCasella:
                        j = i
                    i += 3
                if xProssimaCasella == xPartenza and yProssimaCasella == yPartenza:
                    finito = True
        else:
            impossibileRaggiungere = True

    if impossibileRaggiungere:
        return False
    else:
        return percorsoTrovato


def controllaMorteRallo(vitaRallo, inizio):
    if vitaRallo <= 0:
        schermo.fill(grigioscu)
        messaggio("Sei morto", grigiochi, gsx // 32 * 3, gsy // 18 * 13, 150)
        pygame.display.update()
        continua = False
        while not continua:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    canaleSoundPuntatore.play(selind)
                    continua = True
        inizio = True
    return inizio


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


"""# rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
pygame.draw.rect(schermo, blu, (nx, ny, gpx, gpy))
pygame.display.update()"""
