# -*- coding: utf-8 -*-

import random
from GenericFuncG2 import *


def scegli_sal(cosa, lunghezzadati):
    # posizione-dimensione puntatore
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx, gpy))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx, gpy))
    xp = gsx // 32 * 6
    yp = gsy // 18 * 10

    risposta = False
    conferma = False
    primaconf = False

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 5, gsy // 18 * 7, gsx // 32 * 22, gsy // 18 * 9.5))
        if cosa == 1:
            messaggio("Carica partita", grigiochi, gsx // 32 * 4, gsy // 18 * 4, 90)
        if cosa == 2:
            messaggio("Cancella salvataggio", grigiochi, gsx // 32 * 4, gsy // 18 * 4, 90)
        if cosa == 3:
            messaggio("Salva partita", grigiochi, gsx // 32 * 4, gsy // 18 * 4, 90)
        if conferma:
            if primaconf:
                vxp = xp
                vyp = yp
                xp = gsx // 32 * 22
                yp = gsy // 18 * 6
                primaconf = False
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 18, gsy // 18 * 3.5, gsx // 32 * 9, gsy // 18 * 5))
            messaggio("Confermi?", grigiochi, gsx // 32 * 20, gsy // 18 * 4.5, 70)
            messaggio("Si", grigiochi, gsx // 32 * 20.2, gsy // 18 * 6, 70)
            messaggio("No", grigiochi, gsx // 32 * 23.2, gsy // 18 * 6, 70)
            schermo.blit(puntatorevecchio, (vxp, vyp))
        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
        schermo.blit(s1, (gsx // 32 * 8, gsy // 18 * 8))
        schermo.blit(s2, (gsx // 32 * 15, gsy // 18 * 8))
        schermo.blit(s3, (gsx // 32 * 22, gsy // 18 * 8))

        # lettura salvataggi per riconoscerli
        contasalva = 1
        while contasalva <= 3:
            leggi = open("Salvataggi\Salvataggio%i.txt" % contasalva, "r")
            leggifile = leggi.read()
            dati = leggifile.split("_")
            dati.pop(len(dati) - 1)
            if len(dati) == 0:
                if contasalva == 1:
                    messaggio("Slot vuoto", grigiochi, gsx // 32 * 7.5, gsy // 18 * 11, 60)
                elif contasalva == 2:
                    messaggio("Slot vuoto", grigiochi, gsx // 32 * 14.5, gsy // 18 * 11, 60)
                elif contasalva == 3:
                    messaggio("Slot vuoto", grigiochi, gsx // 32 * 21.5, gsy // 18 * 11, 60)
            else:
                errore = False
                if len(dati) != lunghezzadati:
                    errore = True
                for i in range(0, len(dati)):
                    try:
                        dati[i] = int(dati[i])
                    except ValueError:
                        errore = True
                if contasalva == 1:
                    if not errore:
                        persalva = pygame.image.load('Immagini\Personaggi\Personaggio1.png')
                        persalva = pygame.transform.scale(persalva, (gpx * 3, gpy * 3))
                        spasalva = pygame.image.load('Immagini\Armi\Arma%is.png' % dati[6])
                        spasalva = pygame.transform.scale(spasalva, (gpx * 3, gpy * 3))
                        scusalva = pygame.image.load('Immagini\Scudi\Scudo%is.png' % dati[7])
                        scusalva = pygame.transform.scale(scusalva, (gpx * 3, gpy * 3))
                        armsalva = pygame.image.load('Immagini\Armature\Armatura%is.png' % dati[8])
                        armsalva = pygame.transform.scale(armsalva, (gpx * 3, gpy * 3))
                        messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 7.5, gsy // 18 * 11, 60)
                        schermo.blit(persalva, (gpx * 8, gpy * 12))
                        schermo.blit(armsalva, (gpx * 8, gpy * 12))
                        schermo.blit(scusalva, (gpx * 8, gpy * 12))
                        schermo.blit(spasalva, (gpx * 8, gpy * 12))
                    else:
                        messaggio("Dati corrotti", grigiochi, gsx // 32 * 7.5, gsy // 18 * 11, 60)
                elif contasalva == 2:
                    if not errore:
                        persalva = pygame.image.load('Immagini\Personaggi\Personaggio1.png')
                        persalva = pygame.transform.scale(persalva, (gpx * 3, gpy * 3))
                        spasalva = pygame.image.load('Immagini\Armi\Arma%is.png' % dati[6])
                        spasalva = pygame.transform.scale(spasalva, (gpx * 3, gpy * 3))
                        scusalva = pygame.image.load('Immagini\Scudi\Scudo%is.png' % dati[7])
                        scusalva = pygame.transform.scale(scusalva, (gpx * 3, gpy * 3))
                        armsalva = pygame.image.load('Immagini\Armature\Armatura%is.png' % dati[8])
                        armsalva = pygame.transform.scale(armsalva, (gpx * 3, gpy * 3))
                        messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 14.5, gsy // 18 * 11, 60)
                        schermo.blit(persalva, (gpx * 15, gpy * 12))
                        schermo.blit(armsalva, (gpx * 15, gpy * 12))
                        schermo.blit(scusalva, (gpx * 15, gpy * 12))
                        schermo.blit(spasalva, (gpx * 15, gpy * 12))
                    else:
                        messaggio("Dati corrotti", grigiochi, gsx // 32 * 14.5, gsy // 18 * 11, 60)
                elif contasalva == 3:
                    if not errore:
                        persalva = pygame.image.load('Immagini\Personaggi\Personaggio1.png')
                        persalva = pygame.transform.scale(persalva, (gpx * 3, gpy * 3))
                        spasalva = pygame.image.load('Immagini\Armi\Arma%is.png' % dati[6])
                        spasalva = pygame.transform.scale(spasalva, (gpx * 3, gpy * 3))
                        scusalva = pygame.image.load('Immagini\Scudi\Scudo%is.png' % dati[7])
                        scusalva = pygame.transform.scale(scusalva, (gpx * 3, gpy * 3))
                        armsalva = pygame.image.load('Immagini\Armature\Armatura%is.png' % dati[8])
                        armsalva = pygame.transform.scale(armsalva, (gpx * 3, gpy * 3))
                        messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 21.5, gsy // 18 * 11, 60)
                        schermo.blit(persalva, (gpx * 22, gpy * 12))
                        schermo.blit(armsalva, (gpx * 22, gpy * 12))
                        schermo.blit(scusalva, (gpx * 22, gpy * 12))
                        schermo.blit(spasalva, (gpx * 22, gpy * 12))
                    else:
                        messaggio("Dati corrotti", grigiochi, gsx // 32 * 21.5, gsy // 18 * 11, 60)
            contasalva = contasalva + 1
        leggi.close()

        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    if conferma:
                        selind.play()
                        xp = vxp
                        yp = vyp
                        conferma = False
                    else:
                        selind.play()
                        n = -1
                        return n
                if event.key == pygame.K_d:
                    if conferma:
                        if xp == gsx // 32 * 19:
                            spostapun.play()
                            xp = gsx // 32 * 22
                        elif xp == gsx // 32 * 22:
                            selimp.play()
                    else:
                        if xp == gsx // 32 * 6:
                            spostapun.play()
                            xp = gsx // 32 * 13
                        else:
                            if xp == gsx // 32 * 13:
                                spostapun.play()
                                xp = gsx // 32 * 20
                            else:
                                selimp.play()
                if event.key == pygame.K_a:
                    if conferma:
                        if xp == gsx // 32 * 22:
                            spostapun.play()
                            xp = gsx // 32 * 19
                        elif xp == gsx // 32 * 19:
                            selimp.play()
                    else:
                        if xp == gsx // 32 * 20:
                            spostapun.play()
                            xp = gsx // 32 * 13
                        else:
                            if xp == gsx // 32 * 13:
                                spostapun.play()
                                xp = gsx // 32 * 6
                            else:
                                selimp.play()
                if event.key == pygame.K_SPACE:
                    if conferma and xp == gsx // 32 * 19 and yp == gsy // 18 * 6:
                        selezione.play()
                        return n
                        risposta = True
                    if not conferma and yp == gsy // 18 * 10:
                        selezione.play()
                        if xp == gsx // 32 * 6:
                            conferma = True
                            primaconf = True
                            n = 1
                        if xp == gsx // 32 * 13:
                            conferma = True
                            primaconf = True
                            n = 2
                        if xp == gsx // 32 * 20:
                            conferma = True
                            primaconf = True
                            n = 3
                    if conferma and xp == gsx // 32 * 22 and yp == gsy // 18 * 6:
                        selind.play()
                        xp = vxp
                        yp = vyp
                        conferma = False

            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 5, gsy // 18 * 7, gsx // 32 * 22, gsy // 18 * 9.5))
            if cosa == 1:
                messaggio("Carica partita", grigiochi, gsx // 32 * 4, gsy // 18 * 4, 90)
            if cosa == 2:
                messaggio("Cancella salvataggio", grigiochi, gsx // 32 * 4, gsy // 18 * 4, 90)
            if cosa == 3:
                messaggio("Salva partita", grigiochi, gsx // 32 * 4, gsy // 18 * 4, 90)
            if conferma:
                if primaconf:
                    vxp = xp
                    vyp = yp
                    xp = gsx // 32 * 22
                    yp = gsy // 18 * 6
                    primaconf = False
                pygame.draw.rect(schermo, grigio, (gsx // 32 * 18, gsy // 18 * 3.5, gsx // 32 * 9, gsy // 18 * 5))
                messaggio("Confermi?", grigiochi, gsx // 32 * 20, gsy // 18 * 4.5, 70)
                messaggio("Si", grigiochi, gsx // 32 * 20.2, gsy // 18 * 6, 70)
                messaggio("No", grigiochi, gsx // 32 * 23.2, gsy // 18 * 6, 70)
                schermo.blit(puntatorevecchio, (vxp, vyp))
            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
            schermo.blit(s1, (gsx // 32 * 8, gsy // 18 * 8))
            schermo.blit(s2, (gsx // 32 * 15, gsy // 18 * 8))
            schermo.blit(s3, (gsx // 32 * 22, gsy // 18 * 8))

            # lettura salvataggi per riconoscerli
            contasalva = 1
            while contasalva <= 3:
                leggi = open("Salvataggi\Salvataggio%i.txt" % contasalva, "r")
                leggifile = leggi.read()
                dati = leggifile.split("_")
                dati.pop(len(dati) - 1)
                if len(dati) == 0:
                    if contasalva == 1:
                        messaggio("Slot vuoto", grigiochi, gsx // 32 * 7.5, gsy // 18 * 11, 60)
                    elif contasalva == 2:
                        messaggio("Slot vuoto", grigiochi, gsx // 32 * 14.5, gsy // 18 * 11, 60)
                    elif contasalva == 3:
                        messaggio("Slot vuoto", grigiochi, gsx // 32 * 21.5, gsy // 18 * 11, 60)
                else:
                    errore = False
                    if len(dati) != lunghezzadati:
                        errore = True
                    for i in range(0, len(dati)):
                        try:
                            dati[i] = int(dati[i])
                        except ValueError:
                            errore = True
                    if contasalva == 1:
                        if not errore:
                            persalva = pygame.image.load('Immagini\Personaggi\Personaggio1.png')
                            persalva = pygame.transform.scale(persalva, (gpx * 3, gpy * 3))
                            spasalva = pygame.image.load('Immagini\Armi\Arma%is.png' % dati[6])
                            spasalva = pygame.transform.scale(spasalva, (gpx * 3, gpy * 3))
                            scusalva = pygame.image.load('Immagini\Scudi\Scudo%is.png' % dati[7])
                            scusalva = pygame.transform.scale(scusalva, (gpx * 3, gpy * 3))
                            armsalva = pygame.image.load('Immagini\Armature\Armatura%is.png' % dati[8])
                            armsalva = pygame.transform.scale(armsalva, (gpx * 3, gpy * 3))
                            messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 7.5, gsy // 18 * 11, 60)
                            schermo.blit(persalva, (gpx * 8, gpy * 12))
                            schermo.blit(armsalva, (gpx * 8, gpy * 12))
                            schermo.blit(scusalva, (gpx * 8, gpy * 12))
                            schermo.blit(spasalva, (gpx * 8, gpy * 12))
                        else:
                            messaggio("Dati corrotti", grigiochi, gsx // 32 * 7.5, gsy // 18 * 11, 60)
                    elif contasalva == 2:
                        if not errore:
                            persalva = pygame.image.load('Immagini\Personaggi\Personaggio1.png')
                            persalva = pygame.transform.scale(persalva, (gpx * 3, gpy * 3))
                            spasalva = pygame.image.load('Immagini\Armi\Arma%is.png' % dati[6])
                            spasalva = pygame.transform.scale(spasalva, (gpx * 3, gpy * 3))
                            scusalva = pygame.image.load('Immagini\Scudi\Scudo%is.png' % dati[7])
                            scusalva = pygame.transform.scale(scusalva, (gpx * 3, gpy * 3))
                            armsalva = pygame.image.load('Immagini\Armature\Armatura%is.png' % dati[8])
                            armsalva = pygame.transform.scale(armsalva, (gpx * 3, gpy * 3))
                            messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 14.5, gsy // 18 * 11, 60)
                            schermo.blit(persalva, (gpx * 15, gpy * 12))
                            schermo.blit(armsalva, (gpx * 15, gpy * 12))
                            schermo.blit(scusalva, (gpx * 15, gpy * 12))
                            schermo.blit(spasalva, (gpx * 15, gpy * 12))
                        else:
                            messaggio("Dati corrotti", grigiochi, gsx // 32 * 14.5, gsy // 18 * 11, 60)
                    elif contasalva == 3:
                        if not errore:
                            persalva = pygame.image.load('Immagini\Personaggi\Personaggio1.png')
                            persalva = pygame.transform.scale(persalva, (gpx * 3, gpy * 3))
                            spasalva = pygame.image.load('Immagini\Armi\Arma%is.png' % dati[6])
                            spasalva = pygame.transform.scale(spasalva, (gpx * 3, gpy * 3))
                            scusalva = pygame.image.load('Immagini\Scudi\Scudo%is.png' % dati[7])
                            scusalva = pygame.transform.scale(scusalva, (gpx * 3, gpy * 3))
                            armsalva = pygame.image.load('Immagini\Armature\Armatura%is.png' % dati[8])
                            armsalva = pygame.transform.scale(armsalva, (gpx * 3, gpy * 3))
                            messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 21.5, gsy // 18 * 11, 60)
                            schermo.blit(persalva, (gpx * 22, gpy * 12))
                            schermo.blit(armsalva, (gpx * 22, gpy * 12))
                            schermo.blit(scusalva, (gpx * 22, gpy * 12))
                            schermo.blit(spasalva, (gpx * 22, gpy * 12))
                        else:
                            messaggio("Dati corrotti", grigiochi, gsx // 32 * 21.5, gsy // 18 * 11, 60)
                contasalva = contasalva + 1
            leggi.close()

            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()


def menu():
    # video
    fermavideo = guardaVideo('Video/videoinizio', c16)
    """clock = pygame.time.Clock()
    movie = pygame.movie.Movie(r'Video\videoinizio.mpg')
    movie_screen = pygame.Surface(schermo.get_size())
    movie.set_display(movie_screen, pygame.draw.rect(schermo, nero, (0, 0, gsx, gsy), 1))
    movie.play()
    while movie.get_busy() and not fermavideo:
        schermo.blit(movie_screen, (0, 0))
        pygame.display.update()
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                selezione.play()
                fermavideo = True"""

    c11.play(-1)
    # attesa dopo video
    if not fermavideo:
        schermo.fill(grigioscu)
        messaggio("Premi un tasto per continuare...", grigiochi, gsx // 32 * 4, gsy // 18 * 13, 100)
        pygame.display.update()
        finevideo = True
        while finevideo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    selezione.play()
                    finevideo = False

    puntatore = pygame.transform.scale(puntatoreorigi, (gpx, gpy))
    xp = gsx // 32 * 2
    yp = gsy // 18 * 3

    # numero per la posizione di robo all'avvio
    c = random.randint(1, 4)

    # primo frame
    if True:
        schermo.fill(grigioscu)
        persomenuinizio = pygame.transform.scale(persgraf, (gpx * 18, gpy * 18))
        if (c == 1):
            robomenuinizio = pygame.transform.scale(robogra, (gpx * 18, gpy * 18))
        if (c == 2):
            robomenuinizio = pygame.transform.scale(robograf, (gpx * 18, gpy * 18))
        if (c == 3):
            robomenuinizio = pygame.transform.scale(robograff, (gpx * 18, gpy * 18))
        if (c == 4):
            robomenuinizio = pygame.transform.scale(robografff, (gpx * 18, gpy * 18))
        schermo.blit(persomenuinizio, (gpx * 15, 0))
        schermo.blit(robomenuinizio, (gpx * 3, 0))
        messaggio("Nuova partita", grigiochi, gsx // 32 * 4, gsy // 18 * 3, 90)
        messaggio("Carica partita", grigiochi, gsx // 32 * 4, gsy // 18 * 5.5, 90)
        messaggio("Cancella salvataggio", grigiochi, gsx // 32 * 4, gsy // 18 * 8, 90)
        messaggio("Esci", grigiochi, gsx // 32 * 4, gsy // 18 * 13, 90)
        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while True:
        # posizione porte e cofanetti nel vettore dati
        porteini = 128
        portefin = 155
        cofaniini = portefin + 1
        cofanifin = 179
        lunghezzadati = cofanifin + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if yp != gsy // 18 * 13:
                        if yp == gsy // 18 * 3:
                            spostapun.play()
                            yp = gsy // 18 * 5.5
                        elif yp == gsy // 18 * 5.5:
                            spostapun.play()
                            yp = gsy // 18 * 8
                        elif yp == gsy // 18 * 8:
                            spostapun.play()
                            yp = gsy // 18 * 13
                    else:
                        selimp.play()
                if event.key == pygame.K_w:
                    if yp != gsy // 18 * 3:
                        if yp == gsy // 18 * 5.5:
                            spostapun.play()
                            yp = gsy // 18 * 3
                        elif yp == gsy // 18 * 8:
                            spostapun.play()
                            yp = gsy // 18 * 5.5
                        elif yp == gsy // 18 * 13:
                            spostapun.play()
                            yp = gsy // 18 * 8
                    else:
                        selimp.play()
                if event.key == pygame.K_SPACE:
                    selezione.play()

                    # nuova partita
                    if yp == gsy // 18 * 3:
                        x = gsx // 32 * 6
                        y = gsy // 18 * 2
                        # progresso - stanza - x - y - liv - pv - arma - scudo - armatura - armrob - energiarob - tecniche(20) - oggetti(10) - armi(30) - batterie(10) - condizioni(20) - gambit(20) -
                        # veleno - surriscalda - attp - difp - velp(x2) - efficienza - esperienza - porte(128-?) - cofanetti(?-?) // dimensione: 0-127 + porte e cofanetti
                        dati = [0, 1, x, y, 1, 105, 0, 0, 0, 0, 300,# <- statistiche
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,# <- tecniche
                                -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,# <- oggetti
                                2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,# <- armi
                                2, 0, 0, 0, 0, 0, 0, 0, 0, 0,# <- batterie
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,# <- condizioni
                                -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,# <- gambit
                                False, 0, 0, 0, 0, 0, 0,# <- altre statistiche
                                2, 3, 7, False, 2, 7, 12, False, 2, 12, 11, False, 2, 15, 9, False, 2, 15, 3, False, 2, 23, 5, False, 2, 23, 12, False,# <- porte
                                1, 3, 7, False, 1, 7, 12, False, 1, 12, 11, False, 2, 3, 5, False, 2, 5, 10, False, 2, 10, 9, False]# <- cofanetti
                        c11.stop()
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
                        return dati, porteini, portefin, cofaniini, cofanifin

                    # carica partita
                    if yp == gsy // 18 * 5.5:
                        n = scegli_sal(1, lunghezzadati)

                        # lettura salvataggio
                        if n != -1:
                            leggi = open("Salvataggi\Salvataggio%i.txt" % n, "r")
                            leggifile = leggi.read()
                            dati = leggifile.split("_")
                            dati.pop(len(dati) - 1)
                            if len(dati) == 0:
                                print "Slot vuoto"
                                indietro = False
                                schermo.fill(grigioscu)
                                robograsalva = pygame.transform.scale(robograff, (gpx * 18, gpy * 18))
                                schermo.blit(robograsalva, (gpx * 3, -gpy * 5))
                                messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
                                messaggio("Slot di salvataggio vuoto...", grigiochi, gsx // 32 * 4, gsy // 18 * 13, 100)
                                pygame.display.update()
                                while not indietro:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            quit()
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_q:
                                                selind.play()
                                                indietro = True
                            else:
                                errore = False
                                if len(dati) == lunghezzadati:
                                    for i in range(0, len(dati)):
                                        try:
                                            dati[i] = int(dati[i])
                                        except ValueError:
                                            errore = True
                                    if not errore:
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

                                        print "Salvataggio: " + str(n)
                                        leggi.close()
                                        c11.stop()
                                        return dati, porteini, portefin, cofaniini, cofanifin
                                if len(dati) != lunghezzadati or errore:
                                    print "Dati corrotti: " + str(len(dati))
                                    indietro = False
                                    schermo.fill(grigioscu)
                                    schermo.blit(robograsalva, (gpx * 15, -gpy * 3))
                                    messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
                                    messaggio("I dati sono corrotti...", grigiochi, gsx // 32 * 4, gsy // 18 * 13, 100)
                                    pygame.display.update()
                                    while not indietro:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                quit()
                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_q:
                                                    selind.play()
                                                    indietro = True
                            leggi.close()

                    # cancella partita
                    if yp == gsy // 18 * 8:
                        n = scegli_sal(2, lunghezzadati)
                        if n != -1:
                            leggi = open("Salvataggi\Salvataggio%i.txt" % n, "w")
                            leggi.close()

                    # esci dal gioco
                    if yp == gsy // 18 * 13:
                        pygame.quit()
                        quit()

            schermo.fill(grigioscu)
            persomenuinizio = pygame.transform.scale(persgraf, (gpx * 18, gpy * 18))
            if (c == 1):
                robomenuinizio = pygame.transform.scale(robogra, (gpx * 18, gpy * 18))
            if (c == 2):
                robomenuinizio = pygame.transform.scale(robograf, (gpx * 18, gpy * 18))
            if (c == 3):
                robomenuinizio = pygame.transform.scale(robograff, (gpx * 18, gpy * 18))
            if (c == 4):
                robomenuinizio = pygame.transform.scale(robografff, (gpx * 18, gpy * 18))
            schermo.blit(persomenuinizio, (gpx * 15, 0))
            schermo.blit(robomenuinizio, (gpx * 3, 0))
            messaggio("Nuova partita", grigiochi, gsx // 32 * 4, gsy // 18 * 3, 90)
            messaggio("Carica partita", grigiochi, gsx // 32 * 4, gsy // 18 * 5.5, 90)
            messaggio("Cancella salvataggio", grigiochi, gsx // 32 * 4, gsy // 18 * 8, 90)
            messaggio("Esci", grigiochi, gsx // 32 * 4, gsy // 18 * 13, 90)
            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()


def equip(dati):
    perssta = pygame.transform.scale(perso, (gpx * 8, gpy * 8))
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 12 * 5, gpy // 12 * 5))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 12 * 5, gpy // 12 * 5))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 6
    carim = True
    risposta = False

    esptot, pvtot, entot, att, dif, difro, par = getStatistiche(dati)

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 21, gsy // 18 * 12))
        # linea(dove,colore,inizio,fine,spessore)
        '''pygame.draw.line(schermo, grigioscu, (gsx // 32 * 8, (gsy // 18 * 4) + (gpy // 2)), (gsx // 32 * 8, (gsy // 18 * 15) + (gpy // 2)), 10)
        pygame.draw.line(schermo, grigioscu, (gsx // 32 * 15, (gsy // 18 * 4) + (gpy // 2)), (gsx // 32 * 15, (gsy // 18 * 15) + (gpy // 2)), 10)'''

        if carim:
            armas = pygame.image.load("Immagini\Armi\Arma%is.png" % dati[6])
            arma = pygame.transform.scale(armas, (gpx * 8, gpy * 8))
            scudos = pygame.image.load("Immagini\Scudi\Scudo%is.png" % dati[7])
            scudo = pygame.transform.scale(scudos, (gpx * 8, gpy * 8))
            armaturas = pygame.image.load("Immagini\Armature\Armatura%is.png" % dati[8])
            armatura = pygame.transform.scale(armaturas, (gpx * 8, gpy * 8))
            carim = False
        messaggio("Equipaggiamento", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
        messaggio("Armi", grigiochi, gsx // 32 * 2.5, gsy // 18 * 4.5, 60)
        if dati[41] > 0:
            messaggio("Niente", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
        if dati[42] > 0:
            messaggio("Spada di legno", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
        if dati[43] > 0:
            messaggio("Spada di ferro", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
        if dati[44] > 0:
            messaggio("Spadone d'acciaio", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
        if dati[45] > 0:
            messaggio("Spada del toro", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
        if dati[46] > 0:
            messaggio("Spada di diamante", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
        if dati[47] > 0:
            messaggio("Excalibur", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
        if dati[48] > 0:
            messaggio("Lykother", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
        if dati[49] > 0:
            messaggio("Sinego", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
        if dati[50] > 0:
            messaggio("Mendaxritas", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
        messaggio("Armature", grigiochi, gsx // 32 * 9.5, gsy // 18 * 4.5, 60)
        if dati[51] > 0:
            messaggio("Niente", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
        if dati[52] > 0:
            messaggio("Armatura di pelle", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
        if dati[53] > 0:
            messaggio("Armatura di ferro", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
        if dati[54] > 0:
            messaggio("Armatura d'acciaio", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
        if dati[55] > 0:
            messaggio("Armatura del toro", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
        if dati[56] > 0:
            messaggio("Armatura di diamante", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
        if dati[57] > 0:
            messaggio("Armatura leggendaria", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
        if dati[58] > 0:
            messaggio("Lykodes", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
        if dati[59] > 0:
            messaggio("Armatura antica", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
        if dati[60] > 0:
            messaggio("Loriquam", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
        messaggio("Scudi", grigiochi, gsx // 32 * 16.5, gsy // 18 * 4.5, 60)
        if dati[61] > 0:
            messaggio("Niente", grigiochi, gsx // 32 * 16, gsy // 18 * 6, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 6, 40)
        if dati[62] > 0:
            messaggio("Scudo di pelle", grigiochi, gsx // 32 * 16, gsy // 18 * 7, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 7, 40)
        if dati[63] > 0:
            messaggio("Scudo di ferro", grigiochi, gsx // 32 * 16, gsy // 18 * 8, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 8, 40)
        if dati[64] > 0:
            messaggio("Scudo d'acciaio", grigiochi, gsx // 32 * 16, gsy // 18 * 9, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 9, 40)
        if dati[65] > 0:
            messaggio("Scudo del toro", grigiochi, gsx // 32 * 16, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 10, 40)
        if dati[66] > 0:
            messaggio("Scudo di diamante", grigiochi, gsx // 32 * 16, gsy // 18 * 11, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 11, 40)
        if dati[67] > 0:
            messaggio("Scudo leggendario", grigiochi, gsx // 32 * 16, gsy // 18 * 12, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 12, 40)
        if dati[68] > 0:
            messaggio("Lykethmos", grigiochi, gsx // 32 * 16, gsy // 18 * 13, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 13, 40)
        if dati[69] > 0:
            messaggio("Scudo antico", grigiochi, gsx // 32 * 16, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 14, 40)
        if dati[70] > 0:
            messaggio("Clipequam", grigiochi, gsx // 32 * 16, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 15, 40)
        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
        schermo.blit(perssta, (gsx // 32 * 23, gsy // 18 * 4))
        schermo.blit(armatura, (gsx // 32 * 23, gsy // 18 * 4))
        schermo.blit(arma, (gsx // 32 * 23, gsy // 18 * 4))
        schermo.blit(scudo, (gsx // 32 * 23, gsy // 18 * 4))
        messaggio("Attacco: %i" % att, grigiochi, gsx // 32 * 23, gsy // 18 * 13, 45)
        messaggio("Difesa: %i" % dif, grigiochi, gsx // 32 * 23, gsy // 18 * 14, 45)
        messaggio(u"Probabilità parata: %i" % par + "%", grigiochi, gsx // 32 * 23, gsy // 18 * 15, 45)
        # confronto statistiche
        # armi
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
            if dati[41] != 0:
                diff = 0 - (dati[6] * 10)
                if dati[6] > 0:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                else:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
            if dati[42] != 0:
                diff = 10 - (dati[6] * 10)
                if dati[6] > 1:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 1:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 1:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
            if dati[43] != 0:
                diff = 20 - (dati[6] * 10)
                if dati[6] > 2:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 2:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 2:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
            if dati[44] != 0:
                diff = 30 - (dati[6] * 10)
                if dati[6] > 3:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 3:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 3:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
            if dati[45] != 0:
                diff = 40 - (dati[6] * 10)
                if dati[6] > 4:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 4:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 4:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
            if dati[46] != 0:
                diff = 50 - (dati[6] * 10)
                if dati[6] > 5:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 5:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 5:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
            if dati[47] != 0:
                diff = 60 - (dati[6] * 10)
                if dati[6] > 6:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 6:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 6:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
            if dati[48] != 0:
                diff = 70 - (dati[6] * 10)
                if dati[6] > 7:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 7:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 7:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
            if dati[49] != 0:
                diff = 80 - (dati[6] * 10)
                if dati[6] > 8:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 8:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 8:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
            if dati[50] != 0:
                diff = 90 - (dati[6] * 10)
                if dati[6] > 9:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 9:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 9:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        # armature
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 6:
            if dati[51] != 0:
                diff = 0 - (dati[8] * 10)
                if dati[8] > 0:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                else:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 7:
            if dati[52] != 0:
                diff = 10 - (dati[8] * 10)
                if dati[8] > 1:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 1:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 1:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 8:
            if dati[53] != 0:
                diff = 20 - (dati[8] * 10)
                if dati[8] > 2:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 2:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 2:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 9:
            if dati[54] != 0:
                diff = 30 - (dati[8] * 10)
                if dati[8] > 3:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 3:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 3:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 10:
            if dati[55] != 0:
                diff = 40 - (dati[8] * 10)
                if dati[8] > 4:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 4:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 4:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 11:
            if dati[56] != 0:
                diff = 50 - (dati[8] * 10)
                if dati[8] > 5:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 5:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 5:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 12:
            if dati[57] != 0:
                diff = 60 - (dati[8] * 10)
                if dati[8] > 6:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 6:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 6:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 13:
            if dati[58] != 0:
                diff = 70 - (dati[8] * 10)
                if dati[8] > 7:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 7:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 7:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 14:
            if dati[59] != 0:
                diff = 80 - (dati[8] * 10)
                if dati[8] > 8:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 8:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 8:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 15:
            if dati[60] != 0:
                diff = 90 - (dati[8] * 10)
                if dati[8] > 9:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 9:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 9:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        # scudi
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 6:
            if dati[61] != 0:
                diff = 0 - (dati[7] * 5)
                if dati[7] > 0:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                else:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 0 - (dati[7] * 3)
                if dati[7] > 0:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                else:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 7:
            if dati[62] != 0:
                diff = 5 - (dati[7] * 5)
                if dati[7] > 1:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 1:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 1:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 3 - (dati[7] * 3)
                if dati[7] > 1:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 1:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 1:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 8:
            if dati[63] != 0:
                diff = 10 - (dati[7] * 5)
                if dati[7] > 2:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 2:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 2:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 6 - (dati[7] * 3)
                if dati[7] > 2:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 2:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 2:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 9:
            if dati[64] != 0:
                diff = 15 - (dati[7] * 5)
                if dati[7] > 3:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 3:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 3:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 9 - (dati[7] * 3)
                if dati[7] > 3:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 3:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 3:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 10:
            if dati[65] != 0:
                diff = 20 - (dati[7] * 5)
                if dati[7] > 4:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 4:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 4:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 12 - (dati[7] * 3)
                if dati[7] > 4:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 4:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 4:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 11:
            if dati[66] != 0:
                diff = 25 - (dati[7] * 5)
                if dati[7] > 5:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 5:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 5:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 15 - (dati[7] * 3)
                if dati[7] > 5:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 5:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 5:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 12:
            if dati[67] != 0:
                diff = 30 - (dati[7] * 5)
                if dati[7] > 6:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 6:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 6:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 18 - (dati[7] * 3)
                if dati[7] > 6:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 6:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 6:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 13:
            if dati[68] != 0:
                diff = 35 - (dati[7] * 5)
                if dati[7] > 7:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 7:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 7:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 21 - (dati[7] * 3)
                if dati[7] > 7:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 7:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 7:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 14:
            if dati[69] != 0:
                diff = 40 - (dati[7] * 5)
                if dati[7] > 8:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 8:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 8:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 24 - (dati[7] * 3)
                if dati[7] > 8:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 8:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 8:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 15:
            if dati[70] != 0:
                diff = 45 - (dati[7] * 5)
                if dati[7] > 9:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 9:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 9:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 27 - (dati[7] * 3)
                if dati[7] > 9:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 9:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 9:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)

        # puntatore vecchio
        if dati[6] == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 6))
        if dati[6] == 1:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 7))
        if dati[6] == 2:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 8))
        if dati[6] == 3:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 9))
        if dati[6] == 4:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 10))
        if dati[6] == 5:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 11))
        if dati[6] == 6:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 12))
        if dati[6] == 7:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 13))
        if dati[6] == 8:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 14))
        if dati[6] == 9:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 15))

        if dati[8] == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 6))
        if dati[8] == 1:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 7))
        if dati[8] == 2:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 8))
        if dati[8] == 3:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 9))
        if dati[8] == 4:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 10))
        if dati[8] == 5:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 11))
        if dati[8] == 6:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 12))
        if dati[8] == 7:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 13))
        if dati[8] == 8:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 14))
        if dati[8] == 9:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 15))

        if dati[7] == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 6))
        if dati[7] == 1:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 7))
        if dati[7] == 2:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 8))
        if dati[7] == 3:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 9))
        if dati[7] == 4:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 10))
        if dati[7] == 5:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 11))
        if dati[7] == 6:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 12))
        if dati[7] == 7:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 13))
        if dati[7] == 8:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 14))
        if dati[7] == 9:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 15))

        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    selind.play()
                    risposta = True
                if event.key == pygame.K_s:
                    if (yp != gsy // 18 * 15):
                        spostapun.play()
                        yp = yp + gsy // 18 * 1
                    elif yp == gsy // 18 * 15:
                        spostapun.play()
                        yp = gsy // 18 * 6
                if event.key == pygame.K_w:
                    if (yp != gsy // 18 * 6):
                        spostapun.play()
                        yp = yp - gsy // 18 * 1
                    elif yp == gsy // 18 * 6:
                        spostapun.play()
                        yp = gsy // 18 * 15
                if event.key == pygame.K_d:
                    if (xp != gsx // 32 * 15):
                        spostapun.play()
                        xp = xp + gsx // 32 * 7
                    elif xp == gsx // 32 * 15:
                        spostapun.play()
                        xp = gsx // 32 * 1
                if event.key == pygame.K_a:
                    if (xp != gsx // 32 * 1):
                        spostapun.play()
                        xp = xp - gsx // 32 * 7
                    elif xp == gsx // 32 * 1:
                        spostapun.play()
                        xp = gsx // 32 * 15
                if event.key == pygame.K_SPACE:
                    carim = True
                    # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                    # armi
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
                        if dati[41] != 0:
                            selezione.play()
                            dati[6] = 0
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
                        if dati[42] != 0:
                            selezione.play()
                            dati[6] = 1
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
                        if dati[43] != 0:
                            selezione.play()
                            dati[6] = 2
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
                        if dati[44] != 0:
                            selezione.play()
                            dati[6] = 3
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
                        if dati[45] != 0:
                            selezione.play()
                            dati[6] = 4
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
                        if dati[46] != 0:
                            selezione.play()
                            dati[6] = 5
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
                        if dati[47] != 0:
                            selezione.play()
                            dati[6] = 6
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
                        if dati[48] != 0:
                            selezione.play()
                            dati[6] = 7
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
                        if dati[49] != 0:
                            selezione.play()
                            dati[6] = 8
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
                        if dati[50] != 0:
                            selezione.play()
                            dati[6] = 9
                        else:
                            selimp.play()
                    # armature
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 6:
                        if dati[51] != 0:
                            selezione.play()
                            dati[8] = 0
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 7:
                        if dati[52] != 0:
                            selezione.play()
                            dati[8] = 1
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 8:
                        if dati[53] != 0:
                            selezione.play()
                            dati[8] = 2
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 9:
                        if dati[54] != 0:
                            selezione.play()
                            dati[8] = 3
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 10:
                        if dati[55] != 0:
                            selezione.play()
                            dati[8] = 4
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 11:
                        if dati[56] != 0:
                            selezione.play()
                            dati[8] = 5
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 12:
                        if dati[57] != 0:
                            selezione.play()
                            dati[8] = 6
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 13:
                        if dati[58] != 0:
                            selezione.play()
                            dati[8] = 7
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 14:
                        if dati[59] != 0:
                            selezione.play()
                            dati[8] = 8
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 15:
                        if dati[60] != 0:
                            selezione.play()
                            dati[8] = 9
                        else:
                            selimp.play()
                    # scudi
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 6:
                        if dati[61] != 0:
                            selezione.play()
                            dati[7] = 0
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 7:
                        if dati[62] != 0:
                            selezione.play()
                            dati[7] = 1
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 8:
                        if dati[63] != 0:
                            selezione.play()
                            dati[7] = 2
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 9:
                        if dati[64] != 0:
                            selezione.play()
                            dati[7] = 3
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 10:
                        if dati[65] != 0:
                            selezione.play()
                            dati[7] = 4
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 11:
                        if dati[66] != 0:
                            selezione.play()
                            dati[7] = 5
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 12:
                        if dati[67] != 0:
                            selezione.play()
                            dati[7] = 6
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 13:
                        if dati[68] != 0:
                            selezione.play()
                            dati[7] = 7
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 14:
                        if dati[69] != 0:
                            selezione.play()
                            dati[7] = 8
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 15:
                        if dati[70] != 0:
                            selezione.play()
                            dati[7] = 9
                        else:
                            selimp.play()

            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 21, gsy // 18 * 12))
            # linea(dove,colore,inizio,fine,spessore)
            '''pygame.draw.line(schermo, grigioscu, (gsx // 32 * 8, (gsy // 18 * 4) + (gpy // 2)), (gsx // 32 * 8, (gsy // 18 * 15) + (gpy // 2)), 10)
            pygame.draw.line(schermo, grigioscu, (gsx // 32 * 15, (gsy // 18 * 4) + (gpy // 2)), (gsx // 32 * 15, (gsy // 18 * 15) + (gpy // 2)), 10)'''

            if carim:
                armas = pygame.image.load("Immagini\Armi\Arma%is.png" % dati[6])
                arma = pygame.transform.scale(armas, (gpx * 8, gpy * 8))
                scudos = pygame.image.load("Immagini\Scudi\Scudo%is.png" % dati[7])
                scudo = pygame.transform.scale(scudos, (gpx * 8, gpy * 8))
                armaturas = pygame.image.load("Immagini\Armature\Armatura%is.png" % dati[8])
                armatura = pygame.transform.scale(armaturas, (gpx * 8, gpy * 8))
                carim = False
            messaggio("Equipaggiamento", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
            messaggio("Armi", grigiochi, gsx // 32 * 2.5, gsy // 18 * 4.5, 60)
            if dati[41] > 0:
                messaggio("Niente", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if dati[42] > 0:
                messaggio("Spada di legno", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if dati[43] > 0:
                messaggio("Spada di ferro", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if dati[44] > 0:
                messaggio("Spadone d'acciaio", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if dati[45] > 0:
                messaggio("Spada del toro", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if dati[46] > 0:
                messaggio("Spada di diamante", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if dati[47] > 0:
                messaggio("Excalibur", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if dati[48] > 0:
                messaggio("Lykother", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if dati[49] > 0:
                messaggio("Sinego", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if dati[50] > 0:
                messaggio("Mendaxritas", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            messaggio("Armature", grigiochi, gsx // 32 * 9.5, gsy // 18 * 4.5, 60)
            if dati[51] > 0:
                messaggio("Niente", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
            if dati[52] > 0:
                messaggio("Armatura di pelle", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
            if dati[53] > 0:
                messaggio("Armatura di ferro", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
            if dati[54] > 0:
                messaggio("Armatura d'acciaio", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
            if dati[55] > 0:
                messaggio("Armatura del toro", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
            if dati[56] > 0:
                messaggio("Armatura di diamante", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
            if dati[57] > 0:
                messaggio("Armatura leggendaria", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
            if dati[58] > 0:
                messaggio("Lykodes", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
            if dati[59] > 0:
                messaggio("Armatura antica", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
            if dati[60] > 0:
                messaggio("Loriquam", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
            messaggio("Scudi", grigiochi, gsx // 32 * 16.5, gsy // 18 * 4.5, 60)
            if dati[61] > 0:
                messaggio("Niente", grigiochi, gsx // 32 * 16, gsy // 18 * 6, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 6, 40)
            if dati[62] > 0:
                messaggio("Scudo di pelle", grigiochi, gsx // 32 * 16, gsy // 18 * 7, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 7, 40)
            if dati[63] > 0:
                messaggio("Scudo di ferro", grigiochi, gsx // 32 * 16, gsy // 18 * 8, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 8, 40)
            if dati[64] > 0:
                messaggio("Scudo d'acciaio", grigiochi, gsx // 32 * 16, gsy // 18 * 9, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 9, 40)
            if dati[65] > 0:
                messaggio("Scudo del toro", grigiochi, gsx // 32 * 16, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 10, 40)
            if dati[66] > 0:
                messaggio("Scudo di diamante", grigiochi, gsx // 32 * 16, gsy // 18 * 11, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 11, 40)
            if dati[67] > 0:
                messaggio("Scudo leggendario", grigiochi, gsx // 32 * 16, gsy // 18 * 12, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 12, 40)
            if dati[68] > 0:
                messaggio("Lykethmos", grigiochi, gsx // 32 * 16, gsy // 18 * 13, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 13, 40)
            if dati[69] > 0:
                messaggio("Scudo antico", grigiochi, gsx // 32 * 16, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 14, 40)
            if dati[70] > 0:
                messaggio("Clipequam", grigiochi, gsx // 32 * 16, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 15, 40)
            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)

            esptot, pvtot, entot, att, dif, difro, par = getStatistiche(dati)

            schermo.blit(perssta, (gsx // 32 * 23, gsy // 18 * 4))
            schermo.blit(armatura, (gsx // 32 * 23, gsy // 18 * 4))
            schermo.blit(arma, (gsx // 32 * 23, gsy // 18 * 4))
            schermo.blit(scudo, (gsx // 32 * 23, gsy // 18 * 4))
            messaggio("Attacco: %i" % att, grigiochi, gsx // 32 * 23, gsy // 18 * 13, 45)
            messaggio("Difesa: %i" % dif, grigiochi, gsx // 32 * 23, gsy // 18 * 14, 45)
            messaggio(u"Probabilità parata: %i" % par + "%", grigiochi, gsx // 32 * 23, gsy // 18 * 15, 45)
            # confronto statistiche
            # armi
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
                if dati[41] != 0:
                    diff = 0 - (dati[6] * 10)
                    if dati[6] > 0:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    else:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
                if dati[42] != 0:
                    diff = 10 - (dati[6] * 10)
                    if dati[6] > 1:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 1:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 1:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
                if dati[43] != 0:
                    diff = 20 - (dati[6] * 10)
                    if dati[6] > 2:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 2:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 2:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
                if dati[44] != 0:
                    diff = 30 - (dati[6] * 10)
                    if dati[6] > 3:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 3:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 3:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
                if dati[45] != 0:
                    diff = 40 - (dati[6] * 10)
                    if dati[6] > 4:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 4:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 4:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
                if dati[46] != 0:
                    diff = 50 - (dati[6] * 10)
                    if dati[6] > 5:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 5:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 5:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
                if dati[47] != 0:
                    diff = 60 - (dati[6] * 10)
                    if dati[6] > 6:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 6:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 6:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
                if dati[48] != 0:
                    diff = 70 - (dati[6] * 10)
                    if dati[6] > 7:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 7:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 7:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
                if dati[49] != 0:
                    diff = 80 - (dati[6] * 10)
                    if dati[6] > 8:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 8:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 8:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
                if dati[50] != 0:
                    diff = 90 - (dati[6] * 10)
                    if dati[6] > 9:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 9:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 9:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            # armature
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 6:
                if dati[51] != 0:
                    diff = 0 - (dati[8] * 10)
                    if dati[8] > 0:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    else:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 7:
                if dati[52] != 0:
                    diff = 10 - (dati[8] * 10)
                    if dati[8] > 1:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 1:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 1:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 8:
                if dati[53] != 0:
                    diff = 20 - (dati[8] * 10)
                    if dati[8] > 2:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 2:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 2:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 9:
                if dati[54] != 0:
                    diff = 30 - (dati[8] * 10)
                    if dati[8] > 3:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 3:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 3:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 10:
                if dati[55] != 0:
                    diff = 40 - (dati[8] * 10)
                    if dati[8] > 4:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 4:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 4:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 11:
                if dati[56] != 0:
                    diff = 50 - (dati[8] * 10)
                    if dati[8] > 5:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 5:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 5:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 12:
                if dati[57] != 0:
                    diff = 60 - (dati[8] * 10)
                    if dati[8] > 6:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 6:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 6:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 13:
                if dati[58] != 0:
                    diff = 70 - (dati[8] * 10)
                    if dati[8] > 7:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 7:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 7:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 14:
                if dati[59] != 0:
                    diff = 80 - (dati[8] * 10)
                    if dati[8] > 8:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 8:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 8:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 15:
                if dati[60] != 0:
                    diff = 90 - (dati[8] * 10)
                    if dati[8] > 9:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 9:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 9:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            # scudi
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 6:
                if dati[61] != 0:
                    diff = 0 - (dati[7] * 5)
                    if dati[7] > 0:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    else:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 0 - (dati[7] * 3)
                    if dati[7] > 0:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    else:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 7:
                if dati[62] != 0:
                    diff = 5 - (dati[7] * 5)
                    if dati[7] > 1:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 1:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 1:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 3 - (dati[7] * 3)
                    if dati[7] > 1:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 1:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 1:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 8:
                if dati[63] != 0:
                    diff = 10 - (dati[7] * 5)
                    if dati[7] > 2:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 2:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 2:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 6 - (dati[7] * 3)
                    if dati[7] > 2:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 2:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 2:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 9:
                if dati[64] != 0:
                    diff = 15 - (dati[7] * 5)
                    if dati[7] > 3:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 3:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 3:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 9 - (dati[7] * 3)
                    if dati[7] > 3:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 3:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 3:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 10:
                if dati[65] != 0:
                    diff = 20 - (dati[7] * 5)
                    if dati[7] > 4:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 4:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 4:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 12 - (dati[7] * 3)
                    if dati[7] > 4:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 4:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 4:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 11:
                if dati[66] != 0:
                    diff = 25 - (dati[7] * 5)
                    if dati[7] > 5:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 5:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 5:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 15 - (dati[7] * 3)
                    if dati[7] > 5:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 5:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 5:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 12:
                if dati[67] != 0:
                    diff = 30 - (dati[7] * 5)
                    if dati[7] > 6:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 6:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 6:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 18 - (dati[7] * 3)
                    if dati[7] > 6:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 6:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 6:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 13:
                if dati[68] != 0:
                    diff = 35 - (dati[7] * 5)
                    if dati[7] > 7:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 7:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 7:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 21 - (dati[7] * 3)
                    if dati[7] > 7:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 7:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 7:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 14:
                if dati[69] != 0:
                    diff = 40 - (dati[7] * 5)
                    if dati[7] > 8:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 8:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 8:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 24 - (dati[7] * 3)
                    if dati[7] > 8:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 8:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 8:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 15:
                if dati[70] != 0:
                    diff = 45 - (dati[7] * 5)
                    if dati[7] > 9:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 9:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 9:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 27 - (dati[7] * 3)
                    if dati[7] > 9:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 9:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 9:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)

            # puntatore vecchio
            if dati[6] == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 6))
            if dati[6] == 1:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 7))
            if dati[6] == 2:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 8))
            if dati[6] == 3:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 9))
            if dati[6] == 4:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 10))
            if dati[6] == 5:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 11))
            if dati[6] == 6:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 12))
            if dati[6] == 7:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 13))
            if dati[6] == 8:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 14))
            if dati[6] == 9:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 15))

            if dati[8] == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 6))
            if dati[8] == 1:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 7))
            if dati[8] == 2:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 8))
            if dati[8] == 3:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 9))
            if dati[8] == 4:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 10))
            if dati[8] == 5:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 11))
            if dati[8] == 6:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 12))
            if dati[8] == 7:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 13))
            if dati[8] == 8:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 14))
            if dati[8] == 9:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 15))

            if dati[7] == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 6))
            if dati[7] == 1:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 7))
            if dati[7] == 2:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 8))
            if dati[7] == 3:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 9))
            if dati[7] == 4:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 10))
            if dati[7] == 5:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 11))
            if dati[7] == 6:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 12))
            if dati[7] == 7:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 13))
            if dati[7] == 8:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 14))
            if dati[7] == 9:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 15))

            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()
    return dati


def sceglicondiz(dati, condizione):
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 12 * 5, gpy // 12 * 5))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 12 * 5, gpy // 12 * 5))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 4.5
    risposta = False

    # carico le scenette
    scecond = [0]
    i = 1
    while i <= 20:
        condizioneimm = pygame.image.load("Immagini\GrafCondizioni\Condizione%i.png" % i)
        scecond.append(pygame.transform.scale(condizioneimm, (gpx * 12, gpy * 9)))
        i = i + 1

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 5, gsx // 32 * 15, gsy // 18 * 11))
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 5, gsy // 18 * 2))

        messaggio("Scegli condizione", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
        messaggio("Cancella", grigiochi, gsx // 32 * 2, gsy // 18 * 4.5, 45)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 4.5:
            messaggio("Cancella:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
            messaggio("cancella il settaggio di Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        if dati[81] > 0:
            messaggio("Rallo con pv < 80%", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
                schermo.blit(scecond[1], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Rallo con pv < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su di te quando hai pv < 80%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
        if dati[82] > 0:
            messaggio("Rallo con pv < 50%", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
                schermo.blit(scecond[2], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Rallo con pv < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su di te quando hai pv < 50%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
        if dati[83] > 0:
            messaggio("Rallo con pv < 30%", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
                schermo.blit(scecond[3], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Rallo con pv < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su di te quando hai pv < 30%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
        if dati[84] > 0:
            messaggio("Rallo con veleno", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
                schermo.blit(scecond[4], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Rallo con veleno:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su di te quando hai veleno", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
        if dati[85] > 0:
            messaggio("Colco surriscaldato", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
                schermo.blit(scecond[5], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Colco surriscaldato:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su Colco quando ha surriscaldamento", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
        if dati[86] > 0:
            messaggio("Colco con pe < 80%", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
                schermo.blit(scecond[6], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Colco con pe < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su Colco quando ha pe < 80%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
        if dati[87] > 0:
            messaggio("Colco con pe < 50%", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
                schermo.blit(scecond[7], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Colco con pe < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su Colco quando ha pe < 50%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
        if dati[88] > 0:
            messaggio("Colco con pe < 30%", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
                schermo.blit(scecond[8], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Colco con pe < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su Colco quando ha pe < 30%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
        if dati[89] > 0:
            messaggio("Sempre a Rallo", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
                schermo.blit(scecond[9], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Sempre a Rallo:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su di te in continuazione (se l'azione", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("comporta uno status alterativo, viene eseguita solo", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
                messaggio(u"quando lo status non è attivo)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
        if dati[90] > 0:
            messaggio("Sempre a Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
                schermo.blit(scecond[10], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Sempre a Colco:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su Colco in continuazione (se l'azione", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("comporta uno status alterativo, viene eseguita solo", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
                messaggio(u"quando lo status non è attivo)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
        if dati[91] > 0:
            messaggio("Nemico a caso", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 6:
                schermo.blit(scecond[11], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Nemico a caso:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su un nemico a caso", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
        if dati[92] > 0:
            messaggio("Nemico vicino", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 7:
                schermo.blit(scecond[12], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Nemico vicino:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio(u"esegue l'azione sul nemico più vicino a Colco nel", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("raggio di 2 caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
        if dati[93] > 0:
            messaggio("Nemico lontano", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 8:
                schermo.blit(scecond[13], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Nemico lontano:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione sul nemico lontano (distante di 3 o", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio(u"più caselle) più vicino a Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
        if dati[94] > 0:
            messaggio("Nemico con pv < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 9:
                schermo.blit(scecond[14], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Nemico con pv < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione sul nemico con pv < 80% (in caso di", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio(u"molteplici bersagli, esegue l'azione su quello più", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
                messaggio("vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
        if dati[95] > 0:
            messaggio("Nemico con pv < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 10:
                schermo.blit(scecond[15], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Nemico con pv < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione sul nemico con pv < 50% (in caso di", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio(u"molteplici bersagli, esegue l'azione su quello più", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
                messaggio("vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
        if dati[96] > 0:
            messaggio("Nemico con pv < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 11:
                schermo.blit(scecond[16], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Nemico con pv < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione sul nemico con pv < 30% (in caso di", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio(u"molteplici bersagli, esegue l'azione su quello più", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
                messaggio("vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
        if dati[97] > 0:
            messaggio("Nemico con meno pv", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 12:
                schermo.blit(scecond[17], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Nemico con meno pv:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione sul nemico con meno pv (in caso di", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio(u"molteplici bersagli, esegue l'azione su quello più", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
                messaggio("vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
        if dati[98] > 0:
            messaggio("Numero di nemici > 1", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 13:
                schermo.blit(scecond[18], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Numero di nemici > 1:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio(u"esegue l'azione quando nei paraggi ci sono più di 1", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("nemico (in caso di tecnica a bersaglio singolo, questa", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
                messaggio(u"viene eseguita sul nemico più vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16,
                          40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
        if dati[99] > 0:
            messaggio("Numero di nemici > 4", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 14:
                schermo.blit(scecond[19], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Numero di nemici > 4:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio(u"esegue l'azione quando nei paraggi ci sono più di 4", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("nemici (in caso di tecnica a bersaglio singolo, questa", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
                messaggio(u"viene eseguita sul nemico più vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16,
                          40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
        if dati[100] > 0:
            messaggio("Numero di nemici > 7", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 15:
                schermo.blit(scecond[20], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Numero di nemici > 7:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio(u"esegue l'azione quando nei paraggi ci sono più di 7", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("nemici (in caso di tecnica a bersaglio singolo, questa", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
                messaggio(u"viene eseguita sul nemico più vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16,
                          40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)

        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)

        # puntatore vecchio
        i = 1
        k = 6
        while i <= 10:
            if condizione == i:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * k))
            i = i + 1
            k = k + 1
        i = 11
        k = 6
        while i <= 20:
            if condizione == i:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * k))
            i = i + 1
            k = k + 1
        if condizione == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 4.5))

        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    selind.play()
                    risposta = True

                if event.key == pygame.K_s:
                    if yp == gsy // 18 * 4.5:
                        spostapun.play()
                        yp = yp + gsy // 18 * 1.5
                    else:
                        if yp != gsy // 18 * 15:
                            spostapun.play()
                            yp = yp + gsy // 18 * 1
                        elif yp == gsy // 18 * 15:
                            if xp == gsx // 32 * 1:
                                spostapun.play()
                                yp = gsy // 18 * 4.5
                            else:
                                spostapun.play()
                                yp = gsy // 18 * 6
                if event.key == pygame.K_w:
                    if yp == gsy // 18 * 6:
                        if xp == gsx // 32 * 1:
                            spostapun.play()
                            yp = yp - gsy // 18 * 1.5
                        else:
                            spostapun.play()
                            yp = gsy // 18 * 15
                    else:
                        if yp != gsy // 18 * 4.5:
                            spostapun.play()
                            yp = yp - gsy // 18 * 1
                        elif yp == gsy // 18 * 4.5:
                            spostapun.play()
                            yp = gsy // 18 * 15
                if event.key == pygame.K_d:
                    if yp != gsy // 18 * 4.5:
                        if xp != gsx // 32 * 8:
                            spostapun.play()
                            xp = xp + gsx // 32 * 7
                        elif xp == gsx // 32 * 8:
                            spostapun.play()
                            xp = gsx // 32 * 1
                    else:
                        selimp.play()
                if event.key == pygame.K_a:
                    if yp != gsy // 18 * 4.5:
                        if xp != gsx // 32 * 1:
                            spostapun.play()
                            xp = xp - gsx // 32 * 7
                        elif xp == gsx // 32 * 1:
                            spostapun.play()
                            xp = gsx // 32 * 8
                    else:
                        selimp.play()

                if event.key == pygame.K_SPACE:

                    # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)-condizioni(20)-gambit(20) // dimensione: 0-120
                    i = 81
                    c = 1
                    k = 6
                    while i <= 90:
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * k:
                            if dati[i] != 0:
                                selezione.play()
                                return c
                            else:
                                selimp.play()
                        i = i + 1
                        c = c + 1
                        k = k + 1
                    i = 91
                    c = 11
                    k = 6
                    while i <= 100:
                        if xp == gsx // 32 * 8 and yp == gsy // 18 * k:
                            if dati[i] != 0:
                                selezione.play()
                                return c
                            else:
                                selimp.play()
                        i = i + 1
                        c = c + 1
                        k = k + 1
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 4.5:
                        selezione.play()
                        return 0

            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 5, gsx // 32 * 15, gsy // 18 * 11))
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 5, gsy // 18 * 2))

            messaggio("Scegli condizione", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
            messaggio("Cancella", grigiochi, gsx // 32 * 2, gsy // 18 * 4.5, 45)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 4.5:
                messaggio("Cancella:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("cancella il settaggio di Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            if dati[81] > 0:
                messaggio("Rallo con pv < 80%", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
                    schermo.blit(scecond[1], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Rallo con pv < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su di te quando hai pv < 80%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if dati[82] > 0:
                messaggio("Rallo con pv < 50%", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
                    schermo.blit(scecond[2], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Rallo con pv < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su di te quando hai pv < 50%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if dati[83] > 0:
                messaggio("Rallo con pv < 30%", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
                    schermo.blit(scecond[3], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Rallo con pv < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su di te quando hai pv < 30%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if dati[84] > 0:
                messaggio("Rallo con veleno", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
                    schermo.blit(scecond[4], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Rallo con veleno:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su di te quando hai veleno", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if dati[85] > 0:
                messaggio("Colco surriscaldato", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
                    schermo.blit(scecond[5], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Colco surriscaldato:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su Colco quando ha surriscaldamento", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if dati[86] > 0:
                messaggio("Colco con pe < 80%", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
                    schermo.blit(scecond[6], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Colco con pe < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su Colco quando ha pe < 80%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if dati[87] > 0:
                messaggio("Colco con pe < 50%", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
                    schermo.blit(scecond[7], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Colco con pe < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su Colco quando ha pe < 50%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if dati[88] > 0:
                messaggio("Colco con pe < 30%", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
                    schermo.blit(scecond[8], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Colco con pe < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su Colco quando ha pe < 30%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if dati[89] > 0:
                messaggio("Sempre a Rallo", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
                    schermo.blit(scecond[9], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Sempre a Rallo:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su di te in continuazione (se l'azione", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("comporta uno status alterativo, viene eseguita solo", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
                    messaggio(u"quando lo status non è attivo)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if dati[90] > 0:
                messaggio("Sempre a Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
                    schermo.blit(scecond[10], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Sempre a Colco:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su Colco in continuazione (se l'azione", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("comporta uno status alterativo, viene eseguita solo", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
                    messaggio(u"quando lo status non è attivo)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            if dati[91] > 0:
                messaggio("Nemico a caso", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 6:
                    schermo.blit(scecond[11], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Nemico a caso:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su un nemico a caso", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
            if dati[92] > 0:
                messaggio("Nemico vicino", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 7:
                    schermo.blit(scecond[12], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Nemico vicino:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio(u"esegue l'azione sul nemico più vicino a Colco nel", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("raggio di 2 caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
            if dati[93] > 0:
                messaggio("Nemico lontano", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 8:
                    schermo.blit(scecond[13], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Nemico lontano:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione sul nemico lontano (distante di 3 o", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio(u"più caselle) più vicino a Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
            if dati[94] > 0:
                messaggio("Nemico con pv < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 9:
                    schermo.blit(scecond[14], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Nemico con pv < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione sul nemico con pv < 80% (in caso di", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio(u"molteplici bersagli, esegue l'azione su quello più", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
                    messaggio("vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
            if dati[95] > 0:
                messaggio("Nemico con pv < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 10:
                    schermo.blit(scecond[15], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Nemico con pv < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione sul nemico con pv < 50% (in caso di", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio(u"molteplici bersagli, esegue l'azione su quello più", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
                    messaggio("vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
            if dati[96] > 0:
                messaggio("Nemico con pv < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 11:
                    schermo.blit(scecond[16], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Nemico con pv < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione sul nemico con pv < 30% (in caso di", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio(u"molteplici bersagli, esegue l'azione su quello più", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
                    messaggio("vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
            if dati[97] > 0:
                messaggio("Nemico con meno pv", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 12:
                    schermo.blit(scecond[17], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Nemico con meno pv:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione sul nemico con meno pv (in caso di", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio(u"molteplici bersagli, esegue l'azione su quello più", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
                    messaggio("vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
            if dati[98] > 0:
                messaggio("Numero di nemici > 1", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 13:
                    schermo.blit(scecond[18], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Numero di nemici > 1:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio(u"esegue l'azione quando nei paraggi ci sono più di 1", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("nemico (in caso di tecnica a bersaglio singolo, questa", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
                    messaggio(u"viene eseguita sul nemico più vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
            if dati[99] > 0:
                messaggio("Numero di nemici > 4", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 14:
                    schermo.blit(scecond[19], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Numero di nemici > 4:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio(u"esegue l'azione quando nei paraggi ci sono più di 4", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("nemici (in caso di tecnica a bersaglio singolo, questa", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
                    messaggio(u"viene eseguita sul nemico più vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
            if dati[100] > 0:
                messaggio("Numero di nemici > 7", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 15:
                    schermo.blit(scecond[20], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Numero di nemici > 7:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio(u"esegue l'azione quando nei paraggi ci sono più di 7", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("nemici (in caso di tecnica a bersaglio singolo, questa", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
                    messaggio(u"viene eseguita sul nemico più vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)

            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)

            # puntatore vecchio
            i = 1
            k = 6
            while i <= 10:
                if condizione == i:
                    schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * k))
                i = i + 1
                k = k + 1
            i = 11
            k = 6
            while i <= 20:
                if condizione == i:
                    schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * k))
                i = i + 1
                k = k + 1
            if condizione == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 4.5))

            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()
    return condizione


def sceglitecn(dati, tecnica):
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 12 * 5, gpy // 12 * 5))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 12 * 5, gpy // 12 * 5))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 4.5
    usa = 0
    risposta = False

    # carico le scenette
    scetecn = [0]
    i = 1
    while i <= 20:
        tecnicaimm = pygame.image.load("Immagini\GrafTecniche\Tecnica%i.png" % i)
        scetecn.append(pygame.transform.scale(tecnicaimm, (gpx * 12, gpy * 9)))
        i = i + 1

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,(posizionex,posizioney,larghezza,altezza,spessore))
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 5, gsx // 32 * 15, gsy // 18 * 11))
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 5, gsy // 18 * 2))

        messaggio("Scegli tecnica", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
        messaggio("Cancella", grigiochi, gsx // 32 * 2, gsy // 18 * 4.5, 45)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 4.5:
            messaggio("Cancella:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
            messaggio("cancella il settaggio di Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        if dati[11] > 0:
            messaggio("Scossa", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 6 or usa == 9:
                schermo.blit(scetecn[1], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Scossa:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 5", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
        if dati[12] > 0:
            messaggio("Cura", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 7) or usa == 1:
                schermo.blit(scetecn[2], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Cura:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("recupera un po' dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
        if dati[13] > 0:
            messaggio("Antidoto", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 8) or usa == 2:
                schermo.blit(scetecn[3], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Antidoto:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("cura avvelenamento", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
        if dati[14] > 0:
            messaggio("Freccia elettrica", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 9 or usa == 10:
                schermo.blit(scetecn[4], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Freccia elettrica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 5", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
        if dati[15] > 0:
            messaggio("Tempesta elettrica", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 10 or usa == 11:
                schermo.blit(scetecn[5], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Tempesta elettrica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge danni a tutti i nemici entro il raggio di 4", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
        if dati[16] > 0:
            messaggio("Raffreddamento", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 11 or usa == 12:
                schermo.blit(scetecn[6], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Raffreddamento:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("annulla il surriscaldamento ma richiede due turni", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
        if dati[17] > 0:
            messaggio("Auto-ricarica", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 12) or usa == 3:
                schermo.blit(scetecn[7], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Auto-ricarica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 1", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("ricarica un po' Colco ma richiede due turni e provoca", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("surriscaldamento", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
        if dati[18] > 0:
            messaggio("Cura +", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 13) or usa == 4:
                schermo.blit(scetecn[8], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Cura +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("recupera molti dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
        if dati[19] > 0:
            messaggio("Scossa +", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 14 or usa == 13:
                schermo.blit(scetecn[9], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Scossa +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge molti danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
        if dati[20] > 0:
            messaggio("Freccia elettrica +", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 15 or usa == 14:
                schermo.blit(scetecn[10], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Freccia elettrica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge molti danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
        if dati[21] > 0:
            messaggio("Velocizza", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 6 or usa == 15:
                schermo.blit(scetecn[11], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Velocizza:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 15", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("permette a Colco, se non surriscaldato, di eseguire due", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("azioni al turno. Dopo 15 turni provoca surriscaldamento", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
        if dati[22] > 0:
            messaggio("Carica attacco", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
            if (xp == gsx // 32 * 8 and yp == gsy // 18 * 7) or usa == 7:
                schermo.blit(scetecn[12], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Carica attacco:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("incrementa il tuo attacco per 10 turni", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
        if dati[23] > 0:
            messaggio("Carica difesa", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
            if (xp == gsx // 32 * 8 and yp == gsy // 18 * 8) or usa == 8:
                schermo.blit(scetecn[13], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Carica difesa:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("incrementa la tua difesa per 10 turni", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
        if dati[24] > 0:
            messaggio("Efficienza", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 9 or usa == 16:
                schermo.blit(scetecn[14], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Efficienza:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio(u"tutte le tecniche costano la metà dei pe per 15 turni", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("(si annulla con surriscaldamento)", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
        if dati[25] > 0:
            messaggio("Tempesta elettrica +", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 10 or usa == 17:
                schermo.blit(scetecn[15], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Tempesta elettrica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge molti danni a tutti i nemici entro il raggio", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("di 5 caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
        if dati[26] > 0:
            messaggio("Cura ++", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
            if (xp == gsx // 32 * 8 and yp == gsy // 18 * 11) or usa == 5:
                schermo.blit(scetecn[16], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Cura ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("recupera un enorme parte dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
        if dati[27] > 0:
            messaggio("Auto-ricarica +", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
            if (xp == gsx // 32 * 8 and yp == gsy // 18 * 12) or usa == 6:
                schermo.blit(scetecn[17], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Auto-ricarica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 1", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("ricarica di molto Colco ma richiede due turni e", grigiochi, gsx // 32 * 18, gsy // 18 * 14,
                          40)
                messaggio("provoca surriscaldamento", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
        if dati[28] > 0:
            messaggio("Scossa ++", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 13 or usa == 18:
                schermo.blit(scetecn[18], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Scossa ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge enormi danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
        if dati[29] > 0:
            messaggio("Freccia Elettrica ++", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 14 or usa == 19:
                schermo.blit(scetecn[19], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Freccia Elettrica ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge enormi danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
        if dati[30] > 0:
            messaggio("Tempesta elettrica ++", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 15 or usa == 20:
                schermo.blit(scetecn[20], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Tempesta elettrica ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge enormi danni a tutti i nemici entro il raggio", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("di 6 caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)

        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)

        # puntatore vecchio
        i = 1
        k = 6
        while i <= 10:
            if tecnica == i:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * k))
            i = i + 1
            k = k + 1
        i = 11
        k = 6
        while i <= 20:
            if tecnica == i:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * k))
            i = i + 1
            k = k + 1
        if tecnica == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 4.5))

        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    selind.play()
                    risposta = True

                if event.key == pygame.K_s:
                    if yp == gsy // 18 * 4.5:
                        spostapun.play()
                        yp = yp + gsy // 18 * 1.5
                    else:
                        if yp != gsy // 18 * 15:
                            spostapun.play()
                            yp = yp + gsy // 18 * 1
                        elif yp == gsy // 18 * 15:
                            if xp == gsx // 32 * 1:
                                spostapun.play()
                                yp = gsy // 18 * 4.5
                            else:
                                spostapun.play()
                                yp = gsy // 18 * 6
                if event.key == pygame.K_w:
                    if yp == gsy // 18 * 6:
                        if xp == gsx // 32 * 1:
                            spostapun.play()
                            yp = yp - gsy // 18 * 1.5
                        else:
                            spostapun.play()
                            yp = gsy // 18 * 15
                    else:
                        if yp != gsy // 18 * 4.5:
                            spostapun.play()
                            yp = yp - gsy // 18 * 1
                        elif yp == gsy // 18 * 4.5:
                            spostapun.play()
                            yp = gsy // 18 * 15
                if event.key == pygame.K_d:
                    if yp != gsy // 18 * 4.5:
                        if xp != gsx // 32 * 8:
                            spostapun.play()
                            xp = xp + gsx // 32 * 7
                        elif xp == gsx // 32 * 8:
                            spostapun.play()
                            xp = gsx // 32 * 1
                    else:
                        selimp.play()
                if event.key == pygame.K_a:
                    if yp != gsy // 18 * 4.5:
                        if xp != gsx // 32 * 1:
                            spostapun.play()
                            xp = xp - gsx // 32 * 7
                        elif xp == gsx // 32 * 1:
                            spostapun.play()
                            xp = gsx // 32 * 8
                    else:
                        selimp.play()

                if event.key == pygame.K_SPACE:

                    i = 11
                    c = 1
                    k = 6
                    while i <= 20:
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * k:
                            if dati[i] != 0:
                                selezione.play()
                                tecnica = c
                                risposta = True
                                break
                            else:
                                selimp.play()
                        i = i + 1
                        c = c + 1
                        k = k + 1
                    i = 21
                    c = 11
                    k = 6
                    while i <= 30:
                        if xp == gsx // 32 * 8 and yp == gsy // 18 * k:
                            if dati[i] != 0:
                                selezione.play()
                                tecnica = c
                                risposta = True
                                break
                            else:
                                selimp.play()
                        i = i + 1
                        c = c + 1
                        k = k + 1
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 4.5:
                        selezione.play()
                        risposta = True
                        tecnica = 0

            schermo.fill(grigioscu)
            # rettangolo(dove,colore,(posizionex,posizioney,larghezza,altezza,spessore))
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 5, gsx // 32 * 15, gsy // 18 * 11))
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 5, gsy // 18 * 2))

            messaggio("Scegli tecnica", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
            messaggio("Cancella", grigiochi, gsx // 32 * 2, gsy // 18 * 4.5, 45)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 4.5:
                messaggio("Cancella:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("cancella il settaggio di Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            if dati[11] > 0:
                messaggio("Scossa", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 6 or usa == 9:
                    schermo.blit(scetecn[1], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Scossa:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 5", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if dati[12] > 0:
                messaggio("Cura", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 7) or usa == 1:
                    schermo.blit(scetecn[2], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Cura:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("recupera un po' dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if dati[13] > 0:
                messaggio("Antidoto", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 8) or usa == 2:
                    schermo.blit(scetecn[3], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Antidoto:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("cura avvelenamento", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if dati[14] > 0:
                messaggio("Freccia elettrica", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 9 or usa == 10:
                    schermo.blit(scetecn[4], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Freccia elettrica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 5", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if dati[15] > 0:
                messaggio("Tempesta elettrica", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 10 or usa == 11:
                    schermo.blit(scetecn[5], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Tempesta elettrica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge danni a tutti i nemici entro il raggio di 4", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if dati[16] > 0:
                messaggio("Raffreddamento", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 11 or usa == 12:
                    schermo.blit(scetecn[6], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Raffreddamento:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("annulla il surriscaldamento ma richiede due turni", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if dati[17] > 0:
                messaggio("Auto-ricarica", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 12) or usa == 3:
                    schermo.blit(scetecn[7], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Auto-ricarica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 1", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("ricarica un po' Colco ma richiede due turni e provoca", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("surriscaldamento", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if dati[18] > 0:
                messaggio("Cura +", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 13) or usa == 4:
                    schermo.blit(scetecn[8], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Cura +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("recupera molti dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if dati[19] > 0:
                messaggio("Scossa +", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 14 or usa == 13:
                    schermo.blit(scetecn[9], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Scossa +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge molti danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if dati[20] > 0:
                messaggio("Freccia elettrica +", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 15 or usa == 14:
                    schermo.blit(scetecn[10], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Freccia elettrica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge molti danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            if dati[21] > 0:
                messaggio("Velocizza", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 6 or usa == 15:
                    schermo.blit(scetecn[11], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Velocizza:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 15", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("permette a Colco, se non surriscaldato, di eseguire due", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("azioni al turno. Dopo 15 turni provoca surriscaldamento", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
            if dati[22] > 0:
                messaggio("Carica attacco", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
                if (xp == gsx // 32 * 8 and yp == gsy // 18 * 7) or usa == 7:
                    schermo.blit(scetecn[12], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Carica attacco:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("incrementa il tuo attacco per 10 turni", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
            if dati[23] > 0:
                messaggio("Carica difesa", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
                if (xp == gsx // 32 * 8 and yp == gsy // 18 * 8) or usa == 8:
                    schermo.blit(scetecn[13], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Carica difesa:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("incrementa la tua difesa per 10 turni", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
            if dati[24] > 0:
                messaggio("Efficienza", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 9 or usa == 16:
                    schermo.blit(scetecn[14], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Efficienza:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio(u"tutte le tecniche costano la metà dei pe per 15 turni", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("(si annulla con surriscaldamento)", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
            if dati[25] > 0:
                messaggio("Tempesta elettrica +", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 10 or usa == 17:
                    schermo.blit(scetecn[15], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Tempesta elettrica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge molti danni a tutti i nemici entro il raggio", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("di 5 caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
            if dati[26] > 0:
                messaggio("Cura ++", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
                if (xp == gsx // 32 * 8 and yp == gsy // 18 * 11) or usa == 5:
                    schermo.blit(scetecn[16], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Cura ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("recupera un enorme parte dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
            if dati[27] > 0:
                messaggio("Auto-ricarica +", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
                if (xp == gsx // 32 * 8 and yp == gsy // 18 * 12) or usa == 6:
                    schermo.blit(scetecn[17], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Auto-ricarica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 1", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("ricarica di molto Colco ma richiede due turni e", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("provoca surriscaldamento", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
            if dati[28] > 0:
                messaggio("Scossa ++", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 13 or usa == 18:
                    schermo.blit(scetecn[18], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Scossa ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge enormi danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
            if dati[29] > 0:
                messaggio("Freccia Elettrica ++", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 14 or usa == 19:
                    schermo.blit(scetecn[19], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Freccia Elettrica ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge enormi danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
            if dati[30] > 0:
                messaggio("Tempesta elettrica ++", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 15 or usa == 20:
                    schermo.blit(scetecn[20], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Tempesta elettrica ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge enormi danni a tutti i nemici entro il raggio", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("di 6 caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)

            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)

            # puntatore vecchio
            i = 1
            k = 6
            while i <= 10:
                if tecnica == i:
                    schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * k))
                i = i + 1
                k = k + 1
            i = 11
            k = 6
            while i <= 20:
                if tecnica == i:
                    schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * k))
                i = i + 1
                k = k + 1
            if tecnica == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 4.5))

            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()
    return tecnica


def equiprobo(dati):
    robosta = pygame.transform.scale(roboo, (gpx * 8, gpy * 8))
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 12 * 5, gpy // 12 * 5))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 12 * 5, gpy // 12 * 5))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 6
    carim = True
    risposta = False

    esptot, pvtot, entot, att, dif, difro, par = getStatistiche(dati)

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione,larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 6, gsy // 18 * 12))
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 8, gsy // 18 * 4, gsx // 32 * 15, gsy // 18 * 12))

        if carim:
            armrobs = pygame.image.load("Immagini\Armrobs\Armrob%is.png" % dati[9])
            armrob = pygame.transform.scale(armrobs, (gpx * 8, gpy * 8))
            carim = False
        messaggio("Setta Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)

        # equip batteria
        messaggio("Batterie", grigiochi, gsx // 32 * 2, gsy // 18 * 4.5, 60)
        if dati[71] > 0:
            messaggio("Niente", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
        if dati[72] > 0:
            messaggio("Batteria scarica", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
        if dati[73] > 0:
            messaggio("Batteria piccola", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
        if dati[74] > 0:
            messaggio("Batteria media", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
        if dati[75] > 0:
            messaggio("Batteria grande", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
        if dati[76] > 0:
            messaggio("Batteria discreta", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
        if dati[77] > 0:
            messaggio("Batteria affidabile", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
        if dati[78] > 0:
            messaggio("Batteria extra", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
        if dati[79] > 0:
            messaggio("Batteria efficiente", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
        if dati[80] > 0:
            messaggio("Batteria illimitata", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)

        # programmazione Colco
        messaggio("Condizione...", grigiochi, gsx // 32 * 9, gsy // 18 * 4.5, 60)
        c = 6
        for i in range(101, 111):
            if dati[i] == -1:
                messaggio("---", grigioscu, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 0:
                messaggio("---", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 1:
                messaggio("Rallo con pv < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 2:
                messaggio("Rallo con pv < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 3:
                messaggio("Rallo con pv < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 4:
                messaggio("Rallo con veleno", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 5:
                messaggio("Colco surriscaldato", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 6:
                messaggio("Colco con pe < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 7:
                messaggio("Colco con pe < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 8:
                messaggio("Colco con pe < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 9:
                messaggio("Sempre a Rallo", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 10:
                messaggio("Sempre a Colco", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 11:
                messaggio("Nemico a caso", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 12:
                messaggio("Nemico vicino", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 13:
                messaggio("Nemico lontano", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 14:
                messaggio("Nemico con pv < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 15:
                messaggio("Nemico con pv < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 16:
                messaggio("Nemico con pv < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 17:
                messaggio("Nemico con meno pv", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 18:
                messaggio("Numero di nemici > 1", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 19:
                messaggio("Numero di nemici > 4", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 20:
                messaggio("Numero di nemici > 7", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            c = c + 1
        messaggio("...Tecnica", grigiochi, gsx // 32 * 16, gsy // 18 * 4.5, 60)
        c = 6
        for i in range(111, 121):
            if dati[i] == -1:
                messaggio("---", grigioscu, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 0:
                messaggio("---", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 1:
                messaggio("Scossa", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 2:
                messaggio("Cura", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 3:
                messaggio("Antidoto", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 4:
                messaggio("Freccia elettrica", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 5:
                messaggio("Tempesta elettrica", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 6:
                messaggio("Raffreddamento", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 7:
                messaggio("Auto-ricarica", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 8:
                messaggio("Cura +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 9:
                messaggio("Scossa +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 10:
                messaggio("Freccia elettrica +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 11:
                messaggio("Velocizza", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 12:
                messaggio("Carica attacco", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 13:
                messaggio("Carica difesa", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 14:
                messaggio("Efficienza", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 15:
                messaggio("Tempesta elettrica +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 16:
                messaggio("Cura ++", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 17:
                messaggio("Auto-ricarica +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 18:
                messaggio("Scossa ++", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 19:
                messaggio("Freccia Elettrica ++", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 20:
                messaggio("Tempesta elettrica ++", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            c = c + 1

        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
        schermo.blit(robosta, (gsx // 32 * 23.5, gsy // 18 * 3.5))
        schermo.blit(armrob, (gsx // 32 * 23.5, gsy // 18 * 3.5))
        messaggio("Pe totali: %i" % entot, grigiochi, gsx // 32 * 24, gsy // 18 * 13, 45)
        messaggio("Difesa: %i" % difro, grigiochi, gsx // 32 * 24, gsy // 18 * 14, 45)

        # mostrare differenze statistiche delle batterie
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
            if dati[71] != 0:
                diff = 0 - (dati[9] * 100)
                if dati[9] > 0:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                else:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 0 - (dati[9] * 10)
                if dati[9] > 0:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                else:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
            if dati[72] != 0:
                diff = 100 - (dati[9] * 100)
                if dati[9] > 1:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 1:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 1:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 10 - (dati[9] * 10)
                if dati[9] > 1:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 1:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 1:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
            if dati[73] != 0:
                diff = 200 - (dati[9] * 100)
                if dati[9] > 2:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 2:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 2:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 20 - (dati[9] * 10)
                if dati[9] > 2:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 2:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 2:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
            if dati[74] != 0:
                diff = 300 - (dati[9] * 100)
                if dati[9] > 3:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 3:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 3:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 30 - (dati[9] * 10)
                if dati[9] > 3:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 3:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 3:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
            if dati[75] != 0:
                diff = 400 - (dati[9] * 100)
                if dati[9] > 4:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 4:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 4:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 40 - (dati[9] * 10)
                if dati[9] > 4:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 4:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 4:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
            if dati[76] != 0:
                diff = 500 - (dati[9] * 100)
                if dati[9] > 5:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 5:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 5:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 50 - (dati[9] * 10)
                if dati[9] > 5:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 5:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 5:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
            if dati[77] != 0:
                diff = 600 - (dati[9] * 100)
                if dati[9] > 6:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 6:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 6:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 60 - (dati[9] * 10)
                if dati[9] > 6:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 6:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 6:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
            if dati[78] != 0:
                diff = 700 - (dati[9] * 100)
                if dati[9] > 7:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 7:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 7:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 70 - (dati[9] * 10)
                if dati[9] > 7:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 7:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 7:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
            if dati[79] != 0:
                diff = 800 - (dati[9] * 100)
                if dati[9] > 8:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 8:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 8:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 80 - (dati[9] * 10)
                if dati[9] > 8:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 8:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 8:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
            if dati[80] != 0:
                diff = 900 - (dati[9] * 100)
                if dati[9] > 9:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 9:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 9:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 90 - (dati[9] * 10)
                if dati[9] > 9:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 9:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 9:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)

        # puntatore vecchio
        if dati[9] == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 6))
        if dati[9] == 1:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 7))
        if dati[9] == 2:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 8))
        if dati[9] == 3:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 9))
        if dati[9] == 4:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 10))
        if dati[9] == 5:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 11))
        if dati[9] == 6:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 12))
        if dati[9] == 7:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 13))
        if dati[9] == 8:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 14))
        if dati[9] == 9:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 15))

        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    selind.play()
                    risposta = True
                if event.key == pygame.K_s:
                    if (yp != gsy // 18 * 15):
                        spostapun.play()
                        yp = yp + gsy // 18 * 1
                    elif yp == gsy // 18 * 15:
                        spostapun.play()
                        yp = gsy // 18 * 6
                if event.key == pygame.K_w:
                    if (yp != gsy // 18 * 6):
                        spostapun.play()
                        yp = yp - gsy // 18 * 1
                    elif yp == gsy // 18 * 6:
                        spostapun.play()
                        yp = gsy // 18 * 15
                if event.key == pygame.K_d:
                    if (xp != gsx // 32 * 15):
                        spostapun.play()
                        xp = xp + gsx // 32 * 7
                    elif xp == gsx // 32 * 15:
                        spostapun.play()
                        xp = gsx // 32 * 1
                if event.key == pygame.K_a:
                    if (xp != gsx // 32 * 1):
                        spostapun.play()
                        xp = xp - gsx // 32 * 7
                    elif xp == gsx // 32 * 1:
                        spostapun.play()
                        xp = gsx // 32 * 15
                if event.key == pygame.K_SPACE:
                    carim = True
                    # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                    # armrob
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
                        if dati[71] != 0:
                            selezione.play()
                            dati[9] = 0
                            if dati[10] > 300 + (dati[9] * 100):
                                dati[10] = 300 + (dati[9] * 100)
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
                        if dati[72] != 0:
                            selezione.play()
                            dati[9] = 1
                            if dati[10] > 300 + (dati[9] * 100):
                                dati[10] = 300 + (dati[9] * 100)
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
                        if dati[73] != 0:
                            selezione.play()
                            dati[9] = 2
                            if dati[10] > 300 + (dati[9] * 100):
                                dati[10] = 300 + (dati[9] * 100)
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
                        if dati[74] != 0:
                            selezione.play()
                            dati[9] = 3
                            if dati[10] > 300 + (dati[9] * 100):
                                dati[10] = 300 + (dati[9] * 100)
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
                        if dati[75] != 0:
                            selezione.play()
                            dati[9] = 4
                            if dati[10] > 300 + (dati[9] * 100):
                                dati[10] = 300 + (dati[9] * 100)
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
                        if dati[76] != 0:
                            selezione.play()
                            dati[9] = 5
                            if dati[10] > 300 + (dati[9] * 100):
                                dati[10] = 300 + (dati[9] * 100)
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
                        if dati[77] != 0:
                            selezione.play()
                            dati[9] = 6
                            if dati[10] > 300 + (dati[9] * 100):
                                dati[10] = 300 + (dati[9] * 100)
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
                        if dati[78] != 0:
                            selezione.play()
                            dati[9] = 7
                            if dati[10] > 300 + (dati[9] * 100):
                                dati[10] = 300 + (dati[9] * 100)
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
                        if dati[79] != 0:
                            selezione.play()
                            dati[9] = 8
                            if dati[10] > 300 + (dati[9] * 100):
                                dati[10] = 300 + (dati[9] * 100)
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
                        if dati[80] != 0:
                            selezione.play()
                            dati[9] = 9
                            if dati[10] > 300 + (dati[9] * 100):
                                dati[10] = 300 + (dati[9] * 100)
                        else:
                            selimp.play()

                    # condizioni
                    i = 101
                    c = 6
                    while i <= 110:
                        if xp == gsx // 32 * 8 and yp == gsy // 18 * c:
                            if dati[i] != -1:
                                selezione.play()
                                dati[i] = sceglicondiz(dati, dati[i])
                            else:
                                selimp.play()
                        i = i + 1
                        c = c + 1

                    # tecniche
                    i = 111
                    c = 6
                    while i <= 120:
                        if xp == gsx // 32 * 15 and yp == gsy // 18 * c:
                            if dati[i] != -1:
                                selezione.play()
                                dati[i] = sceglitecn(dati, dati[i])
                            else:
                                selimp.play()
                        i = i + 1
                        c = c + 1

            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione,larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 6, gsy // 18 * 12))
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 8, gsy // 18 * 4, gsx // 32 * 15, gsy // 18 * 12))

            if carim:
                armrobs = pygame.image.load("Immagini\Armrobs\Armrob%is.png" % dati[9])
                armrob = pygame.transform.scale(armrobs, (gpx * 8, gpy * 8))
                carim = False
            messaggio("Setta Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)

            # equip batteria
            messaggio("Batterie", grigiochi, gsx // 32 * 2, gsy // 18 * 4.5, 60)
            if dati[71] > 0:
                messaggio("Niente", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if dati[72] > 0:
                messaggio("Batteria scarica", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if dati[73] > 0:
                messaggio("Batteria piccola", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if dati[74] > 0:
                messaggio("Batteria media", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if dati[75] > 0:
                messaggio("Batteria grande", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if dati[76] > 0:
                messaggio("Batteria discreta", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if dati[77] > 0:
                messaggio("Batteria affidabile", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if dati[78] > 0:
                messaggio("Batteria extra", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if dati[79] > 0:
                messaggio("Batteria efficiente", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if dati[80] > 0:
                messaggio("Batteria illimitata", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)

            # programmazione Colco
            messaggio("Condizione...", grigiochi, gsx // 32 * 9, gsy // 18 * 4.5, 60)
            c = 6
            for i in range(101, 111):
                if dati[i] == -1:
                    messaggio("---", grigioscu, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 0:
                    messaggio("---", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 1:
                    messaggio("Rallo con pv < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 2:
                    messaggio("Rallo con pv < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 3:
                    messaggio("Rallo con pv < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 4:
                    messaggio("Rallo con veleno", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 5:
                    messaggio("Colco surriscaldato", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 6:
                    messaggio("Colco con pe < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 7:
                    messaggio("Colco con pe < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 8:
                    messaggio("Colco con pe < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 9:
                    messaggio("Sempre a Rallo", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 10:
                    messaggio("Sempre a Colco", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 11:
                    messaggio("Nemico a caso", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 12:
                    messaggio("Nemico vicino", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 13:
                    messaggio("Nemico lontano", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 14:
                    messaggio("Nemico con pv < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 15:
                    messaggio("Nemico con pv < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 16:
                    messaggio("Nemico con pv < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 17:
                    messaggio("Nemico con meno pv", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 18:
                    messaggio("Numero di nemici > 1", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 19:
                    messaggio("Numero di nemici > 4", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 20:
                    messaggio("Numero di nemici > 7", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                c = c + 1
            messaggio("...Tecnica", grigiochi, gsx // 32 * 16, gsy // 18 * 4.5, 60)
            c = 6
            for i in range(111, 121):
                if dati[i] == -1:
                    messaggio("---", grigioscu, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 0:
                    messaggio("---", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 1:
                    messaggio("Scossa", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 2:
                    messaggio("Cura", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 3:
                    messaggio("Antidoto", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 4:
                    messaggio("Freccia elettrica", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 5:
                    messaggio("Tempesta elettrica", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 6:
                    messaggio("Raffreddamento", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 7:
                    messaggio("Auto-ricarica", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 8:
                    messaggio("Cura +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 9:
                    messaggio("Scossa +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 10:
                    messaggio("Freccia elettrica +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 11:
                    messaggio("Velocizza", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 12:
                    messaggio("Carica attacco", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 13:
                    messaggio("Carica difesa", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 14:
                    messaggio("Efficienza", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 15:
                    messaggio("Tempesta elettrica +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 16:
                    messaggio("Cura ++", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 17:
                    messaggio("Auto-ricarica +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 18:
                    messaggio("Scossa ++", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 19:
                    messaggio("Freccia Elettrica ++", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 20:
                    messaggio("Tempesta elettrica ++", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                c = c + 1

            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)

            esptot, pvtot, entot, att, dif, difro, par = getStatistiche(dati)

            schermo.blit(robosta, (gsx // 32 * 23.5, gsy // 18 * 3.5))
            schermo.blit(armrob, (gsx // 32 * 23.5, gsy // 18 * 3.5))
            messaggio("Pe totali: %i" % entot, grigiochi, gsx // 32 * 24, gsy // 18 * 13, 45)
            messaggio("Difesa: %i" % difro, grigiochi, gsx // 32 * 24, gsy // 18 * 14, 45)

            # mostrare differenze statistiche delle batterie
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
                if dati[71] != 0:
                    diff = 0 - (dati[9] * 100)
                    if dati[9] > 0:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    else:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 0 - (dati[9] * 10)
                    if dati[9] > 0:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    else:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
                if dati[72] != 0:
                    diff = 100 - (dati[9] * 100)
                    if dati[9] > 1:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 1:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 1:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 10 - (dati[9] * 10)
                    if dati[9] > 1:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 1:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 1:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
                if dati[73] != 0:
                    diff = 200 - (dati[9] * 100)
                    if dati[9] > 2:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 2:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 2:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 20 - (dati[9] * 10)
                    if dati[9] > 2:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 2:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 2:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
                if dati[74] != 0:
                    diff = 300 - (dati[9] * 100)
                    if dati[9] > 3:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 3:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 3:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 30 - (dati[9] * 10)
                    if dati[9] > 3:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 3:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 3:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
                if dati[75] != 0:
                    diff = 400 - (dati[9] * 100)
                    if dati[9] > 4:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 4:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 4:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 40 - (dati[9] * 10)
                    if dati[9] > 4:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 4:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 4:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
                if dati[76] != 0:
                    diff = 500 - (dati[9] * 100)
                    if dati[9] > 5:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 5:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 5:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 50 - (dati[9] * 10)
                    if dati[9] > 5:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 5:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 5:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
                if dati[77] != 0:
                    diff = 600 - (dati[9] * 100)
                    if dati[9] > 6:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 6:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 6:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 60 - (dati[9] * 10)
                    if dati[9] > 6:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 6:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 6:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
                if dati[78] != 0:
                    diff = 700 - (dati[9] * 100)
                    if dati[9] > 7:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 7:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 7:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 70 - (dati[9] * 10)
                    if dati[9] > 7:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 7:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 7:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
                if dati[79] != 0:
                    diff = 800 - (dati[9] * 100)
                    if dati[9] > 8:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 8:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 8:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 80 - (dati[9] * 10)
                    if dati[9] > 8:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 8:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 8:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
                if dati[80] != 0:
                    diff = 900 - (dati[9] * 100)
                    if dati[9] > 9:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 9:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 9:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 90 - (dati[9] * 10)
                    if dati[9] > 9:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 9:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 9:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)

            # puntatore vecchio
            if dati[9] == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 6))
            if dati[9] == 1:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 7))
            if dati[9] == 2:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 8))
            if dati[9] == 3:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 9))
            if dati[9] == 4:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 10))
            if dati[9] == 5:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 11))
            if dati[9] == 6:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 12))
            if dati[9] == 7:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 13))
            if dati[9] == 8:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 14))
            if dati[9] == 9:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 15))

            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()
    return dati


def oggetti(dati):
    oggetton = 1
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 12 * 5, gpy // 12 * 5))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 12 * 5, gpy // 12 * 5))
    sfondostastart = pygame.transform.scale(sfondostax3, (gpx * 4, gpy))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 6
    carim = True
    usauno = False
    usa = 0
    risposta = False
    attacco = 0

    esptot, pvtot, entot, att, dif, difro, par = getStatistiche(dati)

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 5, gsx // 32 * 9, gsy // 18 * 11))

        if carim:
            if dati[oggetton + 30] >= 0:
                oggetto = pygame.image.load("Immagini\Oggetti\Oggetto%i.png" % oggetton)
                oggetto = pygame.transform.scale(oggetto, (gpx * 10, gpy * 10))
            else:
                oggetto = pygame.image.load("Immagini\Oggetti\Sconosciuto.png")
                oggetto = pygame.transform.scale(oggetto, (gpx * 10, gpy * 10))
            carim = False

        # pozione, carica batt, bomba, antidoto, bomba veleno, esca, super poz, carica migliorato, bomba pot, bomba atomica
        messaggio("Oggetti", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
        if dati[31] >= 0:
            messaggio("Pozione x %i" % dati[31], grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 6) or usa == 1:
                messaggio("Pozione: recupera 100 pv", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
        if dati[32] >= 0:
            messaggio("Caricabatterie x %i" % dati[32], grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 7) or usa == 2:
                messaggio("Caricabatterie: recupera 250 pe di Colco", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
        if dati[33] >= 0:
            messaggio("Bomba x %i" % dati[33], grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 8) or usa == 3:
                messaggio("Bomba: infligge un po' di danni ai nemici su", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
                messaggio(u"cui è lanciata", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
        if dati[34] >= 0:
            messaggio("Medicina x %i" % dati[34], grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 9) or usa == 4:
                messaggio("Medicina: cura avvelenamento", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
        if dati[35] >= 0:
            messaggio("Bomba velenosa x %i" % dati[35], grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 10) or usa == 5:
                messaggio("Bomba velenosa: infligge avvelenamento a", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
                messaggio("un nemico", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
        if dati[36] >= 0:
            messaggio("Esca x %i" % dati[36], grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 11) or usa == 6:
                messaggio(u"Esca: distrae i nemici finché non viene distrutta.", grigiochi, gsx // 32 * 20,
                          gsy // 18 * 14, 40)
                messaggio(u"È possibile riprenderla passandoci sopra.", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
        if dati[37] >= 0:
            messaggio("Super pozione x %i" % dati[37], grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 12) or usa == 7:
                messaggio("Super pozione: recupera 300 pv", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
        if dati[38] >= 0:
            messaggio("Caricabatterie migliorato x %i" % dati[38], grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 13) or usa == 8:
                messaggio("Caricabatterie migliorato: recupera 600 pe", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
                messaggio("di Colco", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
        if dati[39] >= 0:
            messaggio("Bomba appiccicosa x %i" % dati[39], grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 14) or usa == 9:
                messaggio(u"Bomba appiccicosa: dimezza la velocità di", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
                messaggio("un nemico", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
        if dati[40] >= 0:
            messaggio("Bomba potenziata x %i" % dati[40], grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 15) or usa == 10:
                messaggio("Bomba potenziata: infligge molti danni ai", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
                messaggio(u"nemici su cui è lanciata in un vasto raggio", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)

        # vita-status personaggio
        if dati[5] < 0:
            dati[5] = 0
        messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), grigiochi, gsx // 32 * 14, gsy // 18 * 3.5, 50)
        messaggio("Status alterativi: ", grigiochi, gsx // 32 * 14, gsy // 18 * 4.5, 50)
        persmen = pygame.transform.scale(persgra, (gpx * 3, gpy * 3))
        schermo.blit(persmen, ((gsx // 32 * 10) + (gpx // 2), gsy // 18 * 3.5))
        schermo.blit(sfondostastart, (gsx // 32 * 14, (gsy // 18 * 5.5) + (gpy // 8)))
        if dati[121]:
            avvelenato = pygame.transform.scale(avvelenatoo, (gpx, gpy))
            schermo.blit(avvelenato, (gsx // 32 * 14, gsy // 18 * 5.5))
        if dati[123] > 0:
            attaccopiu = pygame.transform.scale(attaccopiuo, (gpx, gpy))
            schermo.blit(attaccopiu, ((gsx // 32 * 14) + (2 * gpx // 4 * 3), gsy // 18 * 5.5))
        if dati[124] > 0:
            difesapiu = pygame.transform.scale(difesapiuo, (gpx, gpy))
            schermo.blit(difesapiu, ((gsx // 32 * 14) + (4 * gpx // 4 * 3), gsy // 18 * 5.5))
        # vita-status robo
        if dati[10] < 0:
            dati[10] = 0
        messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), grigiochi, gsx // 32 * 14, gsy // 18 * 8.5, 50)
        messaggio("Status alterativi: ", grigiochi, gsx // 32 * 14, gsy // 18 * 9.5, 50)
        robomen = pygame.transform.scale(robograf, (gpx * 3, gpy * 3))
        schermo.blit(robomen, ((gsx // 32 * 10) + (gpx // 2), gsy // 18 * 7.5))
        schermo.blit(sfondostastart, (gsx // 32 * 14, (gsy // 18 * 10.5) + (gpy // 8)))
        if dati[122] > 0:
            surriscaldato = pygame.transform.scale(surriscaldatoo, (gpx, gpy))
            schermo.blit(surriscaldato, (gsx // 32 * 14, gsy // 18 * 10.5))
        if dati[125] > 0:
            velocitapiu = pygame.transform.scale(velocitapiuo, (gpx, gpy))
            schermo.blit(velocitapiu, ((gsx // 32 * 14) + (2 * gpx // 4 * 3), gsy // 18 * 10.5))
        if dati[126] > 0:
            efficienzapiu = pygame.transform.scale(efficienzapiuo, (gpx, gpy))
            schermo.blit(efficienzapiu, ((gsx // 32 * 14) + (4 * gpx // 4 * 3), gsy // 18 * 10.5))

        if attacco != 0:
            risposta = True

        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
        schermo.blit(oggetto, (gsx // 32 * 20, gsy // 18 * 3))
        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    if usa != 0:
                        selind.play()
                        xp = gsx // 32 * 1
                        if usa == 1:
                            yp = gsy // 18 * 6
                        if usa == 2:
                            yp = gsy // 18 * 7
                        if usa == 3:
                            yp = gsy // 18 * 8
                        if usa == 4:
                            yp = gsy // 18 * 9
                        if usa == 5:
                            yp = gsy // 18 * 10
                        if usa == 6:
                            yp = gsy // 18 * 11
                        if usa == 7:
                            yp = gsy // 18 * 12
                        if usa == 8:
                            yp = gsy // 18 * 13
                        if usa == 9:
                            yp = gsy // 18 * 14
                        if usa == 10:
                            yp = gsy // 18 * 15
                        usa = 0
                    else:
                        selind.play()
                        risposta = True
                if event.key == pygame.K_s and xp != gsx // 32 * 10 and xp != gsx // 32 * 13:
                        if xp != gsx // 32 * 12 and xp != gsx // 32 * 15:
                            carim = True
                            if yp != gsy // 18 * 15:
                                spostapun.play()
                                oggetton = oggetton + 1
                                yp = yp + gsy // 18 * 1
                            elif yp == gsy // 18 * 15:
                                spostapun.play()
                                yp = gsy // 18 * 6
                                oggetton = 1
                if event.key == pygame.K_w and xp != gsx // 32 * 10 and xp != gsx // 32 * 13:
                        carim = True
                        if xp != gsx // 32 * 13:
                            if (yp != gsy // 18 * 6):
                                spostapun.play()
                                oggetton = oggetton - 1
                                yp = yp - gsy // 18 * 1
                            elif yp == gsy // 18 * 6:
                                spostapun.play()
                                yp = gsy // 18 * 15
                                oggetton = 10
                if event.key == pygame.K_a:
                    if xp == gsx // 32 * 13:
                        spostapun.play()
                        xp = xp - gsx // 32 * 3
                    elif xp == gsx // 32 * 10:
                        selimp.play()
                if event.key == pygame.K_d:
                    if xp == gsx // 32 * 10:
                        spostapun.play()
                        xp = xp + gsx // 32 * 3
                    elif xp == gsx // 32 * 13:
                        selimp.play()
                if event.key == pygame.K_SPACE:
                    carim = True
                    usadue = True

                    # usa?
                    if xp == gsx // 32 * 10 and yp == gsy // 18 * 14.5:
                        selezione.play()
                        xp = gsx // 32 * 1
                        # pozione
                        if usa == 1:
                            dati[5] = dati[5] + 100
                            if dati[5] > pvtot:
                                dati[5] = pvtot
                            dati[31] = dati[31] - 1
                            yp = gsy // 18 * 6
                        # carica batt
                        if usa == 2:
                            dati[10] = dati[10] + 250
                            if dati[10] > entot:
                                dati[10] = entot
                            dati[32] = dati[32] - 1
                            yp = gsy // 18 * 7
                        # bomba
                        if usa == 3:
                            attacco = 2
                            yp = gsy // 18 * 8
                        # antidoto
                        if usa == 4:
                            dati[121] = 0
                            dati[34] = dati[34] - 1
                            yp = gsy // 18 * 9
                        # bomba veleno
                        if usa == 5:
                            attacco = 3
                            yp = gsy // 18 * 10
                        # esca
                        if usa == 6:
                            attacco = 4
                            yp = gsy // 18 * 11
                        # super pozione
                        if usa == 7:
                            dati[5] = dati[5] + 300
                            if dati[5] > pvtot:
                                dati[5] = pvtot
                            dati[37] = dati[37] - 1
                            yp = gsy // 18 * 12
                        # carica migliorato
                        if usa == 8:
                            dati[10] = dati[10] + 600
                            if dati[10] > entot:
                                dati[10] = entot
                            dati[38] = dati[38] - 1
                            yp = gsy // 18 * 13
                        # bomba appiccicosa
                        if usa == 9:
                            attacco = 5
                            yp = gsy // 18 * 14
                        # bomba potenziata
                        if usa == 10:
                            attacco = 6
                            yp = gsy // 18 * 15
                        usa = 0
                        usadue = False
                    elif xp == gsx // 32 * 13 and yp == gsy // 18 * 14.5:
                        selind.play()
                        xp = gsx // 32 * 1
                        if usa == 1:
                            yp = gsy // 18 * 6
                        if usa == 2:
                            yp = gsy // 18 * 7
                        if usa == 3:
                            yp = gsy // 18 * 8
                        if usa == 4:
                            yp = gsy // 18 * 9
                        if usa == 5:
                            yp = gsy // 18 * 10
                        if usa == 6:
                            yp = gsy // 18 * 11
                        if usa == 7:
                            yp = gsy // 18 * 12
                        if usa == 8:
                            yp = gsy // 18 * 13
                        if usa == 9:
                            yp = gsy // 18 * 14
                        if usa == 10:
                            yp = gsy // 18 * 15
                        usa = 0
                        usadue = False

                    # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                    if usadue:
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
                            if dati[31] > 0:
                                selezione.play()
                                usa = 1
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
                            if dati[32] > 0:
                                selezione.play()
                                usa = 2
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
                            if dati[33] > 0:
                                selezione.play()
                                usa = 3
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
                            if dati[34] > 0:
                                selezione.play()
                                usa = 4
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
                            if dati[35] > 0:
                                selezione.play()
                                usa = 5
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
                            if dati[36] > 0:
                                selezione.play()
                                usa = 6
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
                            if dati[37] > 0:
                                selezione.play()
                                usa = 7
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
                            if dati[38] > 0:
                                selezione.play()
                                usa = 8
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
                            if dati[39] > 0:
                                selezione.play()
                                usa = 9
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
                            if dati[40] > 0:
                                selezione.play()
                                usa = 10
                                usauno = True
                            else:
                                selimp.play()

            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 5, gsx // 32 * 9, gsy // 18 * 11))

            if carim:
                if dati[oggetton + 30] >= 0:
                    oggetto = pygame.image.load("Immagini\Oggetti\Oggetto%i.png" % oggetton)
                    oggetto = pygame.transform.scale(oggetto, (gpx * 10, gpy * 10))
                else:
                    oggetto = pygame.image.load("Immagini\Oggetti\Sconosciuto.png")
                    oggetto = pygame.transform.scale(oggetto, (gpx * 10, gpy * 10))
                carim = False

            # pozione, carica batt, bomba, antidoto, bomba veleno, esca, super poz, carica migliorato, bomba pot, bomba atomica
            messaggio("Oggetti", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
            if dati[31] >= 0:
                messaggio("Pozione x %i" % dati[31], grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 6) or usa == 1:
                    messaggio("Pozione: recupera 100 pv", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if dati[32] >= 0:
                messaggio("Caricabatterie x %i" % dati[32], grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 7) or usa == 2:
                    messaggio("Caricabatterie: recupera 250 pe di Colco", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if dati[33] >= 0:
                messaggio("Bomba x %i" % dati[33], grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 8) or usa == 3:
                    messaggio("Bomba: infligge un po' di danni ai nemici su", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
                    messaggio(u"cui è lanciata", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if dati[34] >= 0:
                messaggio("Medicina x %i" % dati[34], grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 9) or usa == 4:
                    messaggio("Medicina: cura avvelenamento", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if dati[35] >= 0:
                messaggio("Bomba velenosa x %i" % dati[35], grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 10) or usa == 5:
                    messaggio("Bomba velenosa: infligge avvelenamento a", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
                    messaggio("un nemico", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if dati[36] >= 0:
                messaggio("Esca x %i" % dati[36], grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 11) or usa == 6:
                    messaggio(u"Esca: distrae i nemici finché non viene distrutta.", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
                    messaggio(u"È possibile riprenderla passandoci sopra.", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if dati[37] >= 0:
                messaggio("Super pozione x %i" % dati[37], grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 12) or usa == 7:
                    messaggio("Super pozione: recupera 300 pv", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if dati[38] >= 0:
                messaggio("Caricabatterie migliorato x %i" % dati[38], grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 13) or usa == 8:
                    messaggio("Caricabatterie migliorato: recupera 600 pe", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
                    messaggio("di Colco", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if dati[39] >= 0:
                messaggio("Bomba appiccicosa x %i" % dati[39], grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 14) or usa == 9:
                    messaggio(u"Bomba appiccicosa: dimezza la velocità di", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
                    messaggio("un nemico", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if dati[40] >= 0:
                messaggio("Bomba potenziata x %i" % dati[40], grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 15) or usa == 10:
                    messaggio("Bomba potenziata: infligge molti danni ai", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
                    messaggio(u"nemici su cui è lanciata in un vasto raggio", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)

            # menu conferma
            if usa != 0:
                pygame.draw.rect(schermo, grigio, (gsx // 32 * 10, gsy // 18 * 12, gsx // 32 * 6.5, gsy // 18 * 4))
                puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 3 * 2, gpy // 3 * 2))
                # posizionare il cursore su menu usa
                if usauno:
                    xpv = xp
                    ypv = yp
                    xp = gsx // 32 * 13
                    yp = gsy // 18 * 14.5
                    usauno = False
                schermo.blit(puntatorevecchio, (xpv, ypv))
                messaggio("Usare?", grigiochi, gsx // 32 * 11, gsy // 18 * 12.5, 100)
                messaggio("Si", grigiochi, gsx // 32 * 11, gsy // 18 * 14.5, 60)
                messaggio("No", grigiochi, gsx // 32 * 14, gsy // 18 * 14.5, 60)
            else:
                puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 12 * 5, gpy // 12 * 5))

            # vita-status personaggio
            if dati[5] < 0:
                dati[5] = 0
            messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), grigiochi, gsx // 32 * 14, gsy // 18 * 3.5, 50)
            messaggio("Status alterativi: ", grigiochi, gsx // 32 * 14, gsy // 18 * 4.5, 50)
            persmen = pygame.transform.scale(persgra, (gpx * 3, gpy * 3))
            schermo.blit(persmen, ((gsx // 32 * 10) + (gpx // 2), gsy // 18 * 3.5))
            schermo.blit(sfondostastart, (gsx // 32 * 14, (gsy // 18 * 5.5) + (gpy // 8)))
            if dati[121]:
                avvelenato = pygame.transform.scale(avvelenatoo, (gpx, gpy))
                schermo.blit(avvelenato, (gsx // 32 * 14, gsy // 18 * 5.5))
            if dati[123] > 0:
                attaccopiu = pygame.transform.scale(attaccopiuo, (gpx, gpy))
                schermo.blit(attaccopiu, ((gsx // 32 * 14) + (2 * gpx // 4 * 3), gsy // 18 * 5.5))
            if dati[124] > 0:
                difesapiu = pygame.transform.scale(difesapiuo, (gpx, gpy))
                schermo.blit(difesapiu, ((gsx // 32 * 14) + (4 * gpx // 4 * 3), gsy // 18 * 5.5))
            # vita-status robo
            if dati[10] < 0:
                dati[10] = 0
            messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), grigiochi, gsx // 32 * 14, gsy // 18 * 8.5, 50)
            messaggio("Status alterativi: ", grigiochi, gsx // 32 * 14, gsy // 18 * 9.5, 50)
            robomen = pygame.transform.scale(robograf, (gpx * 3, gpy * 3))
            schermo.blit(robomen, ((gsx // 32 * 10) + (gpx // 2), gsy // 18 * 7.5))
            schermo.blit(sfondostastart, (gsx // 32 * 14, (gsy // 18 * 10.5) + (gpy // 8)))
            if dati[122] > 0:
                surriscaldato = pygame.transform.scale(surriscaldatoo, (gpx, gpy))
                schermo.blit(surriscaldato, (gsx // 32 * 14, gsy // 18 * 10.5))
            if dati[125] > 0:
                velocitapiu = pygame.transform.scale(velocitapiuo, (gpx, gpy))
                schermo.blit(velocitapiu, ((gsx // 32 * 14) + (2 * gpx // 4 * 3), gsy // 18 * 10.5))
            if dati[126] > 0:
                efficienzapiu = pygame.transform.scale(efficienzapiuo, (gpx, gpy))
                schermo.blit(efficienzapiu, ((gsx // 32 * 14) + (4 * gpx // 4 * 3), gsy // 18 * 10.5))

            if attacco != 0:
                risposta = True

            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
            schermo.blit(oggetto, (gsx // 32 * 20, gsy // 18 * 3))
            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()
    return dati, attacco


def chiediconferma(conferma):
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx * 2, gpy * 2))
    xp = gsx // 32 * 18
    yp = gsy // 18 * 10
    schermo.fill(grigioscu)
    if conferma == 1:
        messaggio(u"Tornare al menù principale?", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 120)
    elif conferma == 2:
        messaggio("Tornare a Windows?", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 120)
    messaggio("Si", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 120)
    messaggio("No", grigiochi, gsx // 32 * 21, gsy // 18 * 10, 120)
    messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
    schermo.blit(puntatore, (xp, yp))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    selind.play()
                    return False, False
                if event.key == pygame.K_a:
                    if xp == gsx // 32 * 18:
                        spostapun.play()
                        xp = gsx // 32 * 6
                    elif xp == gsx // 32 * 6:
                        selimp.play()
                if event.key == pygame.K_d:
                    if xp == gsx // 32 * 6:
                        spostapun.play()
                        xp = gsx // 32 * 18
                    elif xp == gsx // 32 * 18:
                        selimp.play()
                if event.key == pygame.K_SPACE:
                    if xp == gsx // 32 * 6:
                        selezione.play()
                        if conferma == 1:
                            return True, True
                        elif conferma == 2:
                            pygame.quit()
                            quit()
                    elif xp == gsx // 32 * 18:
                        selind.play()
                        return False, False
            schermo.fill(grigioscu)
            if conferma == 1:
                messaggio(u"Tornare al menù principale?", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 120)
            elif conferma == 2:
                messaggio("Tornare a Windows?", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 120)
            messaggio("Si", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 120)
            messaggio("No", grigiochi, gsx // 32 * 21, gsy // 18 * 10, 120)
            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()


def start(dati, nmost, porteini, portefin, cofaniini, cofanifin, porte, cofanetti, apriocchio):
    c16.play(-1)

    sfondostastart = pygame.transform.scale(sfondostax3, (gpx * 4, gpy))
    perssta = pygame.transform.scale(persgra, (gpx * 10, gpy * 10))
    robosta = pygame.transform.scale(robograf, (gpx * 10, gpy * 10))
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 2, gpy // 2))
    avvelenatosta = pygame.transform.scale(avvelenatoo, (gpx, gpy))
    surriscaldatosta = pygame.transform.scale(surriscaldatoo, (gpx, gpy))
    attaccopiusta = pygame.transform.scale(attaccopiuo, (gpx, gpy))
    difesapiusta = pygame.transform.scale(difesapiuo, (gpx, gpy))
    velocitapiusta = pygame.transform.scale(velocitapiuo, (gpx, gpy))
    efficienzapiusta = pygame.transform.scale(efficienzapiuo, (gpx, gpy))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 5
    carim = True
    risposta = False
    attacco = 0
    conferma = 0

    esptot, pvtot, entot, att, dif, difro, par = getStatistiche(dati)

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 10, gsy // 18 * 12.5))
        messaggio(u"Menù start", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 150)
        messaggio("Oggetti", grigiochi, gsx // 32 * 2, gsy // 18 * 5, 50)
        """if not apriocchio:
            messaggio("Tecniche", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 50)
        else:
            messaggio("Tecniche", grigioscu, gsx // 32 * 2, gsy // 18 * 6, 50)"""
        messaggio("Equipaggiamento", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 50)
        messaggio("Setta Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 50)
        messaggio("Mappa", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 50)
        messaggio("Diario", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 50)
        if nmost == -1:
            messaggio("Salva", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 50)
        else:
            messaggio("Salva", grigioscu, gsx // 32 * 2, gsy // 18 * 13, 50)
        messaggio(u"Torna al menù principale", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 50)
        messaggio("Torna a Windows", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 50)
        messaggio(u"Esc / Q: Esci dal menù", grigiochi, gsx // 32 * 23, gsy // 18 * 1, 50)
        if carim:
            if dati[10] <= 0:
                robosta = robograff
                robosta = pygame.transform.scale(robosta, (gpx * 10, gpy * 10))
            else:
                robosta = robograf
                robosta = pygame.transform.scale(robosta, (gpx * 10, gpy * 10))
            carim = False
        # vita-status personaggio
        if dati[5] < 0:
            dati[5] = 0
        messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), grigiochi, gsx // 32 * 14, gsy // 18 * 13, 50)
        messaggio("Lv:  " + str(dati[4]), grigiochi, gsx // 32 * 14, gsy // 18 * 14, 50)
        if dati[4] < 100:
            messaggio("Esp:  " + str(dati[127]) + " / " + str(esptot), grigiochi, (gsx // 32 * 16) + (gpx // 2),
                      gsy // 18 * 14, 50)
        else:
            messaggio("Esp:  -- / --", grigiochi, (gsx // 32 * 16) + (gpx // 2), gsy // 18 * 14, 50)
        messaggio("Status alterativi: ", grigiochi, gsx // 32 * 14, gsy // 18 * 15, 50)
        schermo.blit(sfondostastart, (gsx // 32 * 14, (gsy // 18 * 16) + (gpy // 8)))
        if dati[121]:
            schermo.blit(avvelenatosta, (gsx // 32 * 14, gsy // 18 * 16))
        if dati[123] > 0:
            schermo.blit(attaccopiusta, ((gsx // 32 * 14) + (2 * gpx // 4 * 3), gsy // 18 * 16))
        if dati[124] > 0:
            schermo.blit(difesapiusta, ((gsx // 32 * 14) + (4 * gpx // 4 * 3), gsy // 18 * 16))
        # vita-status robo
        if dati[10] < 0:
            dati[10] = 0
        messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), grigiochi, gsx // 32 * 23, gsy // 18 * 13, 50)
        messaggio("Status alterativi: ", grigiochi, gsx // 32 * 23, gsy // 18 * 14, 50)
        schermo.blit(sfondostastart, (gsx // 32 * 23, (gsy // 18 * 15) + (gpy // 8)))
        if dati[122] > 0:
            schermo.blit(surriscaldatosta, (gsx // 32 * 23, gsy // 18 * 15))
        if dati[125] > 0:
            schermo.blit(velocitapiusta, ((gsx // 32 * 23) + (2 * gpx // 4 * 3), gsy // 18 * 15))
        if dati[126] > 0:
            schermo.blit(efficienzapiusta, ((gsx // 32 * 23) + (4 * gpx // 4 * 3), gsy // 18 * 15))
        schermo.blit(perssta, (gsx // 32 * 12, gsy // 18 * 2))
        schermo.blit(robosta, (gsx // 32 * 21, gsy // 18 * 2))
        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    selind.play()
                    inizio = False
                    risposta = True
                if event.key == pygame.K_s:
                    if (yp != gsy // 18 * 9) and (yp != gsy // 18 * 15):
                        spostapun.play()
                        yp = yp + gsy // 18 * 1
                    else:
                        if yp == gsy // 18 * 9:
                            spostapun.play()
                            yp = yp + gsy // 18 * 4
                        else:
                            if yp == gsy // 18 * 15:
                                spostapun.play()
                                yp = gsy // 18 * 5
                if event.key == pygame.K_w:
                    if (yp != gsy // 18 * 13) and (yp != gsy // 18 * 5):
                        spostapun.play()
                        yp = yp - gsy // 18 * 1
                    else:
                        if yp == gsy // 18 * 13:
                            spostapun.play()
                            yp = yp - gsy // 18 * 4
                        else:
                            if yp == gsy // 18 * 5:
                                spostapun.play()
                                yp = gsy // 18 * 15
                if event.key == pygame.K_SPACE:
                    if yp == gsy // 18 * 13 and nmost > -1:
                        selimp.play()
                    else:
                        selezione.play()
                    inizio = False
                    # oggetti
                    if yp == gsy // 18 * 5:
                        dati, attacco = oggetti(dati)
                        carim = True
                    # tecniche
                    """if yp == gsy // 18 * 6:
                        #if not apriocchio:
                        dati, attacco = tecniche(dati)
                        carim = True"""
                    # equip pers
                    if yp == gsy // 18 * 6:
                        dati = equip(dati)
                        carim = True
                    # equip robot
                    if yp == gsy // 18 * 7:
                        dati = equiprobo(dati)
                        carim = True
                    # mappa
                    if yp == gsy // 18 * 8:
                        print ("mappa")
                    # diario
                    if yp == gsy // 18 * 9:
                        print ("diario")
                    # salva
                    if yp == gsy // 18 * 13:
                        #if nmost == -1:
                        n = scegli_sal(3, len(dati))
                        if n != -1:
                            salvataggio(n, dati, porteini, portefin, cofaniini, cofanifin, porte, cofanetti)
                    # menu
                    if yp == gsy // 18 * 14:
                        conferma = 1
                    # chiudi
                    if yp == gsy // 18 * 15:
                        conferma = 2

            # chiedere conferma per uscire
            if conferma != 0:
                inizio, risposta = chiediconferma(conferma)
                conferma = 0

            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 10, gsy // 18 * 12.5))
            messaggio(u"Menù start", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 150)
            messaggio("Oggetti", grigiochi, gsx // 32 * 2, gsy // 18 * 5, 50)
            """if not apriocchio:
                messaggio("Tecniche", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 50)
            else:
                messaggio("Tecniche", grigioscu, gsx // 32 * 2, gsy // 18 * 6, 50)"""
            messaggio("Equipaggiamento", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 50)
            messaggio("Setta Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 50)
            messaggio("Mappa", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 50)
            messaggio("Diario", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 50)
            if nmost == -1:
                messaggio("Salva", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 50)
            else:
                messaggio("Salva", grigioscu, gsx // 32 * 2, gsy // 18 * 13, 50)
            messaggio(u"Torna al menù principale", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 50)
            messaggio("Torna a Windows", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 50)
            messaggio(u"Esc / Q: Esci dal menù", grigiochi, gsx // 32 * 23, gsy // 18 * 1, 50)
            if carim:
                if dati[10] <= 0:
                    robosta = robograff
                    robosta = pygame.transform.scale(robosta, (gpx * 10, gpy * 10))
                else:
                    robosta = robograf
                    robosta = pygame.transform.scale(robosta, (gpx * 10, gpy * 10))
                carim = False

            # vita-status personaggio
            if dati[5] < 0:
                dati[5] = 0
            messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), grigiochi, gsx // 32 * 14, gsy // 18 * 13, 50)
            messaggio("Lv:  " + str(dati[4]), grigiochi, gsx // 32 * 14, gsy // 18 * 14, 50)
            if dati[4] < 100:
                messaggio("Esp:  " + str(dati[127]) + " / " + str(esptot), grigiochi, (gsx // 32 * 16) + (gpx // 2), gsy // 18 * 14, 50)
            else:
                messaggio("Esp:  -- / --", grigiochi, (gsx // 32 * 16) + (gpx // 2), gsy // 18 * 14, 50)
            messaggio("Status alterativi: ", grigiochi, gsx // 32 * 14, gsy // 18 * 15, 50)
            schermo.blit(sfondostastart, (gsx // 32 * 14, (gsy // 18 * 16) + (gpy // 8)))
            if dati[121]:
                schermo.blit(avvelenatosta, (gsx // 32 * 14, gsy // 18 * 16))
            if dati[123] > 0:
                schermo.blit(attaccopiusta, ((gsx // 32 * 14) + (2 * gpx // 4 * 3), gsy // 18 * 16))
            if dati[124] > 0:
                schermo.blit(difesapiusta, ((gsx // 32 * 14) + (4 * gpx // 4 * 3), gsy // 18 * 16))
            # vita-status robo
            if dati[10] < 0:
                dati[10] = 0
            messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), grigiochi, gsx // 32 * 23, gsy // 18 * 13, 50)
            messaggio("Status alterativi: ", grigiochi, gsx // 32 * 23, gsy // 18 * 14, 50)
            schermo.blit(sfondostastart, (gsx // 32 * 23, (gsy // 18 * 15) + (gpy // 8)))
            if dati[122] > 0:
                schermo.blit(surriscaldatosta, (gsx // 32 * 23, gsy // 18 * 15))
            if dati[125] > 0:
                schermo.blit(velocitapiusta, ((gsx // 32 * 23) + (2 * gpx // 4 * 3), gsy // 18 * 15))
            if dati[126] > 0:
                schermo.blit(efficienzapiusta, ((gsx // 32 * 23) + (4 * gpx // 4 * 3), gsy // 18 * 15))

            if attacco != 0:
                risposta = True

            schermo.blit(perssta, (gsx // 32 * 12, gsy // 18 * 2))
            schermo.blit(robosta, (gsx // 32 * 21, gsy // 18 * 2))
            schermo.blit(puntatore, (xp, yp))
            if not risposta:
                pygame.display.update()
            else:
                schermo.fill(grigioscu)
    c16.stop()
    return dati, inizio, attacco


def startBattaglia(dati):
    xp = gpx * 1
    yp = gpy * 5

    esptot, pvtot, entot, att, dif, difro, par = getStatistiche(dati)

    attacco = 0
    disegnoOggetto = 0
    risposta = False

    difensivi = True
    offensivi = False
    sposta = False

    oggetton = 1
    vettoreOggettiGraf = []
    vettoreOggettiIco = []
    nomiOggettiIco = ["Pozione", "Caricabatterie", "Bomba", "Medicina", "BombaVeleno", "Esca", "Superpozione", "CaricabatterieMigliorato", "BombaAppiccicosa", "BombaPotenziata"]
    while oggetton <= 10:
        if dati[oggetton + 30] >= 0:
            oggetto = pygame.image.load("Immagini\Oggetti\Oggetto%i.png" % oggetton)
            vettoreOggettiGraf.append(pygame.transform.scale(oggetto, (gpx * 4, gpy * 4)))
            oggetto = pygame.image.load("Immagini\Oggetti\%s.png" % nomiOggettiIco[oggetton - 1])
            vettoreOggettiIco.append(pygame.transform.scale(oggetto, (gpx, gpy)))
        else:
            oggetto = pygame.image.load("Immagini\Oggetti\Sconosciuto.png")
            vettoreOggettiGraf.append(pygame.transform.scale(oggetto, (gpx * 4, gpy * 4)))
            oggetto = pygame.image.load("Immagini\Oggetti\SconosciutoIco.png")
            vettoreOggettiIco.append(pygame.transform.scale(oggetto, (gpx, gpy)))
        oggetton += 1

    # primo frame
    if True:
        pygame.display.update()

    while not risposta:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    selind.play()
                    risposta = True
                if event.key == pygame.K_a:
                    if xp != gpx * 1:
                        spostapun.play()
                        xp = xp - gpx
                    else:
                        spostapun.play()
                        xp = gpx * 5
                if event.key == pygame.K_d:
                    if xp != gpx * 5:
                        spostapun.play()
                        xp = xp + gpx
                    else:
                        spostapun.play()
                        xp = gpx * 1
                if event.key == pygame.K_w:
                    if offensivi:
                        spostapun.play()
                        yp = gpy * 5
                        offensivi = False
                        difensivi = True
                    else:
                        selimp.play()
                if event.key == pygame.K_s:
                    if difensivi:
                        spostapun.play()
                        yp = (gpy * 5) + (gpy // 2)
                        difensivi = False
                        offensivi = True
                    else:
                        selimp.play()
                if event.key == pygame.K_SPACE:
                    # pozione
                    if difensivi and xp == gpx * 1 and dati[31] > 0:
                        dati[5] = dati[5] + 100
                        if dati[5] > pvtot:
                            dati[5] = pvtot
                        dati[31] = dati[31] - 1
                        sposta = True
                        risposta = True
                    # carica batt
                    if difensivi and xp == gpx * 2 and dati[32] > 0:
                        dati[10] = dati[10] + 250
                        if dati[10] > entot:
                            dati[10] = entot
                        dati[32] = dati[32] - 1
                        sposta = True
                        risposta = True
                    # bomba
                    if offensivi and xp == gpx * 1 and dati[33] > 0:
                        attacco = 2
                        risposta = True
                    # antidoto
                    if difensivi and xp == gpx * 3 and dati[34] > 0:
                        dati[121] = 0
                        dati[34] = dati[34] - 1
                        sposta = True
                        risposta = True
                    # bomba veleno
                    if offensivi and xp == gpx * 2 and dati[35] > 0:
                        attacco = 3
                        risposta = True
                    # esca
                    if offensivi and xp == gpx * 3 and dati[36] > 0:
                        attacco = 4
                        risposta = True
                    # super pozione
                    if difensivi and xp == gpx * 4 and dati[37] > 0:
                        dati[5] = dati[5] + 300
                        if dati[5] > pvtot:
                            dati[5] = pvtot
                        dati[37] = dati[37] - 1
                        sposta = True
                        risposta = True
                    # carica migliorato
                    if difensivi and xp == gpx * 5 and dati[38] > 0:
                        dati[10] = dati[10] + 600
                        if dati[10] > entot:
                            dati[10] = entot
                        dati[38] = dati[38] - 1
                        sposta = True
                        risposta = True
                    # bomba appiccicosa
                    if offensivi and xp == gpx * 4 and dati[39] > 0:
                        attacco = 5
                        risposta = True
                    # bomba potenziata
                    if offensivi and xp == gpx * 5 and dati[40] > 0:
                        attacco = 6
                        risposta = True

                    if risposta:
                        selezione.play()
                    else:
                        selimp.play()

            schermo.blit(sfondoStartBattaglia, (0, 0))
            if difensivi:
                if xp == gpx * 1:
                    disegnoOggetto = 0
                if xp == gpx * 2:
                    disegnoOggetto = 1
                if xp == gpx * 3:
                    disegnoOggetto = 3
                if xp == gpx * 4:
                    disegnoOggetto = 6
                if xp == gpx * 5:
                    disegnoOggetto = 7
            elif offensivi:
                if xp == gpx * 1:
                    disegnoOggetto = 2
                if xp == gpx * 2:
                    disegnoOggetto = 4
                if xp == gpx * 3:
                    disegnoOggetto = 5
                if xp == gpx * 4:
                    disegnoOggetto = 8
                if xp == gpx * 5:
                    disegnoOggetto = 9
            schermo.blit(vettoreOggettiGraf[disegnoOggetto], (gpx // 2, gpy * 1))
            if dati[disegnoOggetto + 31] <= 0:
                schermo.blit(puntatOut, (xp, yp))
                qta = 0
            else:
                schermo.blit(puntatIn, (xp, yp))
                qta = dati[disegnoOggetto + 31]
            messaggio("x%i" % qta, grigiochi, (gpx * 4) + (gpx // 2), gpy * 3, 80)
            disegnati = 0
            i = 0
            while i < 10:
                if difensivi and (i == 0 or i == 1 or i == 3 or i == 6 or i == 7):
                    schermo.blit(vettoreOggettiIco[i], (gpx * (disegnati + 1), gpy * 5))
                    disegnati += 1
                if offensivi and (i == 2 or i == 4 or i == 5 or i == 8 or i == 9):
                    schermo.blit(vettoreOggettiIco[i], (gpx * (disegnati + 1), (gpy * 5) + (gpy // 2)))
                    disegnati += 1
                i += 1
            if difensivi:
                messaggio("Oggetti curativi", grigiochi, gpx * 1, gpy // 2, 40)
                schermo.blit(scorriGiu, (gpx * 3, gpy * 6))
            if offensivi:
                messaggio("Oggetti offensivi", grigiochi, gpx * 1, gpy // 2, 40)
                schermo.blit(scorriSu, (gpx * 3, (gpy * 5) - (gpy // 2)))

            if not risposta:
                pygame.display.update()

    return dati, attacco, sposta
