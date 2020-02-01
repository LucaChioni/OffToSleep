# -*- coding: utf-8 -*-

from GenericFuncG2 import *


def scegli_sal(cosa, lunghezzadati, canzone):
    # posizione-dimensione puntatore
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 2, gpy // 2))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 2, gpy // 2))
    xp = gsx // 32 * 6.5
    yp = gsy // 18 * 9.5
    vxp = xp
    vyp = yp

    tastop = 0
    tastotempfps = 5

    risposta = False
    conferma = False
    primaconf = False
    salMarcato = 1
    voceMarcata = 2
    n = -1

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 5, gsy // 18 * 7, gsx // 32 * 22, gsy // 18 * 9.5))
        if cosa == 1:
            messaggio("Carica partita", grigiochi, gsx // 32 * 5, gsy // 18 * 4.5, 120)
        if cosa == 2:
            messaggio("Cancella salvataggio", grigiochi, gsx // 32 * 5, gsy // 18 * 5, 100)
        if cosa == 3:
            messaggio("Salva partita", grigiochi, gsx // 32 * 5, gsy // 18 * 4.5, 120)
        if conferma:
            if primaconf:
                vxp = xp
                vyp = yp
                xp = gsx // 32 * 22.3
                yp = gsy // 18 * 6.3
                voceMarcata = 2
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
        leggi = 0
        contasalva = 1
        while contasalva <= 3:
            leggi = open("Salvataggi/Salvataggio%i.txt" % contasalva, "r")
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
                else:
                    for i in range(0, len(dati)):
                        try:
                            dati[i] = int(dati[i])
                        except ValueError:
                            errore = True
                if contasalva == 1:
                    if not errore:
                        persalva = pygame.transform.scale(perso, (gpx * 3, gpy * 3))
                        persSalvaBraccia = pygame.transform.scale(persob, (gpx * 3, gpy * 3))
                        spasalva = pygame.transform.scale(vetImgSpadePixellate[dati[6]], (gpx * 3, gpy * 3))
                        arcsalva = pygame.transform.scale(vetImgArchiPixellate[dati[128]], (gpx * 3, gpy * 3))
                        armsalva = pygame.transform.scale(vetImgArmaturePixellate[dati[8]], (gpx * 3, gpy * 3))
                        scusalva = pygame.transform.scale(vetImgScudiPixellate[dati[7]], (gpx * 3, gpy * 3))
                        guasalva = pygame.transform.scale(vetImgGuantiPixellate[dati[129]], (gpx * 3, gpy * 3))
                        colsalva = pygame.transform.scale(vetImgCollanePixellate[dati[130]], (gpx * 3, gpy * 3))
                        messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 7.5, gsy // 18 * 11, 60)
                        schermo.blit(arcsalva, (gpx * 8, gpy * 12))
                        schermo.blit(persalva, (gpx * 8, gpy * 12))
                        schermo.blit(persSalvaBraccia, (gpx * 8, gpy * 12))
                        schermo.blit(armsalva, (gpx * 8, gpy * 12))
                        schermo.blit(colsalva, (gpx * 8, gpy * 12))
                        schermo.blit(spasalva, (gpx * 8, gpy * 12))
                        schermo.blit(guasalva, (gpx * 8, gpy * 12))
                        schermo.blit(scusalva, (gpx * 8, gpy * 12))
                    else:
                        messaggio("Dati corrotti", grigiochi, gsx // 32 * 7.5, gsy // 18 * 11, 60)
                elif contasalva == 2:
                    if not errore:
                        persalva = pygame.transform.scale(perso, (gpx * 3, gpy * 3))
                        persSalvaBraccia = pygame.transform.scale(persob, (gpx * 3, gpy * 3))
                        spasalva = pygame.transform.scale(vetImgSpadePixellate[dati[6]], (gpx * 3, gpy * 3))
                        arcsalva = pygame.transform.scale(vetImgArchiPixellate[dati[128]], (gpx * 3, gpy * 3))
                        armsalva = pygame.transform.scale(vetImgArmaturePixellate[dati[8]], (gpx * 3, gpy * 3))
                        scusalva = pygame.transform.scale(vetImgScudiPixellate[dati[7]], (gpx * 3, gpy * 3))
                        guasalva = pygame.transform.scale(vetImgGuantiPixellate[dati[129]], (gpx * 3, gpy * 3))
                        colsalva = pygame.transform.scale(vetImgCollanePixellate[dati[130]], (gpx * 3, gpy * 3))
                        messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 14.5, gsy // 18 * 11, 60)
                        schermo.blit(arcsalva, (gpx * 15, gpy * 12))
                        schermo.blit(persalva, (gpx * 15, gpy * 12))
                        schermo.blit(persSalvaBraccia, (gpx * 15, gpy * 12))
                        schermo.blit(armsalva, (gpx * 15, gpy * 12))
                        schermo.blit(colsalva, (gpx * 15, gpy * 12))
                        schermo.blit(spasalva, (gpx * 15, gpy * 12))
                        schermo.blit(guasalva, (gpx * 15, gpy * 12))
                        schermo.blit(scusalva, (gpx * 15, gpy * 12))
                    else:
                        messaggio("Dati corrotti", grigiochi, gsx // 32 * 14.5, gsy // 18 * 11, 60)
                elif contasalva == 3:
                    if not errore:
                        persalva = pygame.transform.scale(perso, (gpx * 3, gpy * 3))
                        persSalvaBraccia = pygame.transform.scale(persob, (gpx * 3, gpy * 3))
                        spasalva = pygame.transform.scale(vetImgSpadePixellate[dati[6]], (gpx * 3, gpy * 3))
                        arcsalva = pygame.transform.scale(vetImgArchiPixellate[dati[128]], (gpx * 3, gpy * 3))
                        armsalva = pygame.transform.scale(vetImgArmaturePixellate[dati[8]], (gpx * 3, gpy * 3))
                        scusalva = pygame.transform.scale(vetImgScudiPixellate[dati[7]], (gpx * 3, gpy * 3))
                        guasalva = pygame.transform.scale(vetImgGuantiPixellate[dati[129]], (gpx * 3, gpy * 3))
                        colsalva = pygame.transform.scale(vetImgCollanePixellate[dati[130]], (gpx * 3, gpy * 3))
                        messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 21.5, gsy // 18 * 11, 60)
                        schermo.blit(arcsalva, (gpx * 22, gpy * 12))
                        schermo.blit(persalva, (gpx * 22, gpy * 12))
                        schermo.blit(persSalvaBraccia, (gpx * 22, gpy * 12))
                        schermo.blit(armsalva, (gpx * 22, gpy * 12))
                        schermo.blit(colsalva, (gpx * 22, gpy * 12))
                        schermo.blit(spasalva, (gpx * 22, gpy * 12))
                        schermo.blit(guasalva, (gpx * 22, gpy * 12))
                        schermo.blit(scusalva, (gpx * 22, gpy * 12))
                    else:
                        messaggio("Dati corrotti", grigiochi, gsx // 32 * 21.5, gsy // 18 * 11, 60)
            contasalva = contasalva + 1
        leggi.close()

        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        if not canaleSoundCanzone.get_busy():
            canaleSoundCanzone.play(canzone)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 3

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato:
                tastop = event.key
                tastotempfps = 5
                if event.key == pygame.K_q and not tastoTrovato:
                    tastoTrovato = True
                    if conferma:
                        canaleSoundPuntatore.play(selind)
                        xp = vxp
                        yp = vyp
                        conferma = False
                    else:
                        canaleSoundPuntatore.play(selind)
                        n = -1
                        return n
                if event.key == pygame.K_d and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_SPACE and not tastoTrovato:
                    tastoTrovato = True
                    if conferma:
                        if voceMarcata == 1:
                            canaleSoundPuntatore.play(selezione)
                            risposta = True
                            return n
                        if voceMarcata == 2:
                            canaleSoundPuntatore.play(selind)
                            xp = vxp
                            yp = vyp
                            conferma = False
                    else:
                        canaleSoundPuntatore.play(selezione)
                        conferma = True
                        primaconf = True
                        n = salMarcato
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_q or tastop == pygame.K_SPACE or ((tastop == pygame.K_a or tastop == pygame.K_d) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_a or tastop == pygame.K_d):
                tastotempfps = 3
            if tastop == pygame.K_a:
                if conferma:
                    if voceMarcata == 2:
                        voceMarcata -= 1
                        canaleSoundPuntatore.play(spostapun)
                        xp = gsx // 32 * 19.3
                    else:
                        canaleSoundPuntatore.play(selimp)
                else:
                    if salMarcato == 3:
                        salMarcato -= 1
                        canaleSoundPuntatore.play(spostapun)
                        xp = gsx // 32 * 13.5
                    elif salMarcato == 2:
                        salMarcato -= 1
                        canaleSoundPuntatore.play(spostapun)
                        xp = gsx // 32 * 6.5
                    else:
                        canaleSoundPuntatore.play(selimp)
            if tastop == pygame.K_d:
                if conferma:
                    if voceMarcata == 1:
                        voceMarcata += 1
                        canaleSoundPuntatore.play(spostapun)
                        xp = gsx // 32 * 22.3
                    else:
                        canaleSoundPuntatore.play(selimp)
                else:
                    if salMarcato == 1:
                        salMarcato += 1
                        canaleSoundPuntatore.play(spostapun)
                        xp = gsx // 32 * 13.5
                    elif salMarcato == 2:
                        salMarcato += 1
                        canaleSoundPuntatore.play(spostapun)
                        xp = gsx // 32 * 20.5
                    else:
                        canaleSoundPuntatore.play(selimp)

            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 5, gsy // 18 * 7, gsx // 32 * 22, gsy // 18 * 9.5))
            if cosa == 1:
                messaggio("Carica partita", grigiochi, gsx // 32 * 5, gsy // 18 * 4.5, 120)
            if cosa == 2:
                messaggio("Cancella salvataggio", grigiochi, gsx // 32 * 5, gsy // 18 * 5, 100)
            if cosa == 3:
                messaggio("Salva partita", grigiochi, gsx // 32 * 5, gsy // 18 * 4.5, 120)
            if conferma:
                if primaconf:
                    vxp = xp
                    vyp = yp
                    xp = gsx // 32 * 22.3
                    yp = gsy // 18 * 6.3
                    voceMarcata = 2
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
                leggi = open("Salvataggi/Salvataggio%i.txt" % contasalva, "r")
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
                    else:
                        for i in range(0, len(dati)):
                            try:
                                dati[i] = int(dati[i])
                            except ValueError:
                                errore = True
                    if contasalva == 1:
                        if not errore:
                            persalva = pygame.transform.scale(perso, (gpx * 3, gpy * 3))
                            persSalvaBraccia = pygame.transform.scale(persob, (gpx * 3, gpy * 3))
                            spasalva = pygame.transform.scale(vetImgSpadePixellate[dati[6]], (gpx * 3, gpy * 3))
                            arcsalva = pygame.transform.scale(vetImgArchiPixellate[dati[128]], (gpx * 3, gpy * 3))
                            armsalva = pygame.transform.scale(vetImgArmaturePixellate[dati[8]], (gpx * 3, gpy * 3))
                            scusalva = pygame.transform.scale(vetImgScudiPixellate[dati[7]], (gpx * 3, gpy * 3))
                            guasalva = pygame.transform.scale(vetImgGuantiPixellate[dati[129]], (gpx * 3, gpy * 3))
                            colsalva = pygame.transform.scale(vetImgCollanePixellate[dati[130]], (gpx * 3, gpy * 3))
                            messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 7.5, gsy // 18 * 11, 60)
                            schermo.blit(arcsalva, (gpx * 8, gpy * 12))
                            schermo.blit(persalva, (gpx * 8, gpy * 12))
                            schermo.blit(persSalvaBraccia, (gpx * 8, gpy * 12))
                            schermo.blit(armsalva, (gpx * 8, gpy * 12))
                            schermo.blit(colsalva, (gpx * 8, gpy * 12))
                            schermo.blit(spasalva, (gpx * 8, gpy * 12))
                            schermo.blit(guasalva, (gpx * 8, gpy * 12))
                            schermo.blit(scusalva, (gpx * 8, gpy * 12))
                        else:
                            messaggio("Dati corrotti", grigiochi, gsx // 32 * 7.5, gsy // 18 * 11, 60)
                    elif contasalva == 2:
                        if not errore:
                            persalva = pygame.transform.scale(perso, (gpx * 3, gpy * 3))
                            persSalvaBraccia = pygame.transform.scale(persob, (gpx * 3, gpy * 3))
                            spasalva = pygame.transform.scale(vetImgSpadePixellate[dati[6]], (gpx * 3, gpy * 3))
                            arcsalva = pygame.transform.scale(vetImgArchiPixellate[dati[128]], (gpx * 3, gpy * 3))
                            armsalva = pygame.transform.scale(vetImgArmaturePixellate[dati[8]], (gpx * 3, gpy * 3))
                            scusalva = pygame.transform.scale(vetImgScudiPixellate[dati[7]], (gpx * 3, gpy * 3))
                            guasalva = pygame.transform.scale(vetImgGuantiPixellate[dati[129]], (gpx * 3, gpy * 3))
                            colsalva = pygame.transform.scale(vetImgCollanePixellate[dati[130]], (gpx * 3, gpy * 3))
                            messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 14.5, gsy // 18 * 11, 60)
                            schermo.blit(arcsalva, (gpx * 15, gpy * 12))
                            schermo.blit(persalva, (gpx * 15, gpy * 12))
                            schermo.blit(persSalvaBraccia, (gpx * 15, gpy * 12))
                            schermo.blit(armsalva, (gpx * 15, gpy * 12))
                            schermo.blit(colsalva, (gpx * 15, gpy * 12))
                            schermo.blit(spasalva, (gpx * 15, gpy * 12))
                            schermo.blit(guasalva, (gpx * 15, gpy * 12))
                            schermo.blit(scusalva, (gpx * 15, gpy * 12))
                        else:
                            messaggio("Dati corrotti", grigiochi, gsx // 32 * 14.5, gsy // 18 * 11, 60)
                    elif contasalva == 3:
                        if not errore:
                            persalva = pygame.transform.scale(perso, (gpx * 3, gpy * 3))
                            persSalvaBraccia = pygame.transform.scale(persob, (gpx * 3, gpy * 3))
                            spasalva = pygame.transform.scale(vetImgSpadePixellate[dati[6]], (gpx * 3, gpy * 3))
                            arcsalva = pygame.transform.scale(vetImgArchiPixellate[dati[128]], (gpx * 3, gpy * 3))
                            armsalva = pygame.transform.scale(vetImgArmaturePixellate[dati[8]], (gpx * 3, gpy * 3))
                            scusalva = pygame.transform.scale(vetImgScudiPixellate[dati[7]], (gpx * 3, gpy * 3))
                            guasalva = pygame.transform.scale(vetImgGuantiPixellate[dati[129]], (gpx * 3, gpy * 3))
                            colsalva = pygame.transform.scale(vetImgCollanePixellate[dati[130]], (gpx * 3, gpy * 3))
                            messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 21.5, gsy // 18 * 11, 60)
                            schermo.blit(arcsalva, (gpx * 22, gpy * 12))
                            schermo.blit(persalva, (gpx * 22, gpy * 12))
                            schermo.blit(persSalvaBraccia, (gpx * 22, gpy * 12))
                            schermo.blit(armsalva, (gpx * 22, gpy * 12))
                            schermo.blit(colsalva, (gpx * 22, gpy * 12))
                            schermo.blit(spasalva, (gpx * 22, gpy * 12))
                            schermo.blit(guasalva, (gpx * 22, gpy * 12))
                            schermo.blit(scusalva, (gpx * 22, gpy * 12))
                        else:
                            messaggio("Dati corrotti", grigiochi, gsx // 32 * 21.5, gsy // 18 * 11, 60)
                contasalva = contasalva + 1
            leggi.close()

            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        clockMenu.tick(fpsMenu)


def menu():
    # video
    fermavideo = guardaVideo('Video/videoinizio')
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
                    canaleSoundPuntatore.play(selezione)
                    finevideo = False

    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 2, gpy // 2))
    xp = gsx // 32 * 3
    yp = gsy // 18 * 3.5
    voceMarcata = 1

    tastop = 0
    tastotempfps = 5

    # numero per la posizione di robo all'avvio
    c = random.randint(1, 4)

    # primo frame
    if True:
        schermo.fill(grigioscu)
        persomenuinizio = pygame.transform.scale(persGrafInizio, (gpx * 18, gpy * 18))
        if c == 1:
            robomenuinizio = pygame.transform.scale(robogra, (gpx * 18, gpy * 18))
        elif c == 2:
            robomenuinizio = pygame.transform.scale(robograf, (gpx * 18, gpy * 18))
        elif c == 3:
            robomenuinizio = pygame.transform.scale(robograff, (gpx * 18, gpy * 18))
        else:
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
        if not canaleSoundCanzone.get_busy():
            canaleSoundCanzone.play(c11)

        # posizione porte e cofanetti nel vettore dati
        porteini = 134
        portefin = 161
        cofaniini = portefin + 1
        cofanifin = 185
        lunghezzadati = cofanifin + 1

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 3

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato:
                tastop = event.key
                tastotempfps = 5
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_SPACE and not tastoTrovato:
                    tastoTrovato = True
                    canaleSoundPuntatore.play(selezione)

                    # nuova partita
                    if voceMarcata == 1:
                        x = gsx // 32 * 6
                        y = gsy // 18 * 2
                        # progresso - stanza - x - y - liv - pv - spada - scudo - armatura - armrob - energiarob - tecniche(20) - oggetti(10) - equipaggiamento(30) - batterie(10) - condizioni(20) - gambit(20) -
                        # veleno - surriscalda - attp - difp - velp(x2) - efficienza - esperienza - arco - guanti - collana - monete - frecce - faretra - porte(134-?) - cofanetti(?-?) // dimensione: 0-133 + porte e cofanetti
                        dati = [0, 1, x, y, 1, 55, 0, 0, 0, 0, 220,# <- statistiche
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,# <- tecniche
                                -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,# <- oggetti
                                2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0,# <- equpaggiamento
                                2, 0, 0, 0, 0, -1, -1, -1, -1, -1,# <- batterie (sono utilizzati solo i primi 5)
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,# <- condizioni
                                -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,# <- gambit
                                False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,# <- altre statistiche
                                2, 3, 7, False, 2, 7, 12, False, 2, 12, 11, False, 2, 15, 9, False, 2, 15, 3, False, 2, 23, 5, False, 2, 23, 12, False,# <- porte
                                1, 3, 7, False, 1, 7, 12, False, 1, 12, 11, False, 2, 3, 5, False, 2, 5, 10, False, 2, 10, 9, False]# <- cofanetti
                        canaleSoundCanzone.stop()
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
                    if voceMarcata == 2:
                        n = scegli_sal(1, lunghezzadati, c11)

                        # lettura salvataggio
                        if n != -1:
                            leggi = open("Salvataggi/Salvataggio%i.txt" % n, "r")
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
                                                canaleSoundPuntatore.play(selind)
                                                indietro = True
                            else:
                                errore = False
                                if len(dati) != lunghezzadati:
                                    errore = True
                                else:
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
                                        canaleSoundCanzone.stop()
                                        return dati, porteini, portefin, cofaniini, cofanifin
                                if len(dati) != lunghezzadati or errore:
                                    print "Dati corrotti: " + str(len(dati))
                                    indietro = False
                                    schermo.fill(grigioscu)
                                    robograsalva = pygame.transform.scale(robograffff, (gpx * 18, gpy * 18))
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
                                                    canaleSoundPuntatore.play(selind)
                                                    indietro = True
                            leggi.close()

                    # cancella partita
                    if voceMarcata == 3:
                        n = scegli_sal(2, lunghezzadati, c11)
                        if n != -1:
                            leggi = open("Salvataggi/Salvataggio%i.txt" % n, "w")
                            leggi.close()

                    # esci dal gioco
                    if voceMarcata == 4:
                        pygame.quit()
                        quit()
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_SPACE or ((tastop == pygame.K_s or tastop == pygame.K_w) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_s or tastop == pygame.K_w):
                tastotempfps = 3
            if tastop == pygame.K_s:
                if voceMarcata != 4:
                    if voceMarcata == 1:
                        canaleSoundPuntatore.play(spostapun)
                        yp = gsy // 18 * 6
                    elif voceMarcata == 2:
                        canaleSoundPuntatore.play(spostapun)
                        yp = gsy // 18 * 8.5
                    elif voceMarcata == 3:
                        canaleSoundPuntatore.play(spostapun)
                        yp = gsy // 18 * 13.5
                    voceMarcata += 1
                else:
                    canaleSoundPuntatore.play(selimp)
            if tastop == pygame.K_w:
                if voceMarcata != 1:
                    if voceMarcata == 2:
                        canaleSoundPuntatore.play(spostapun)
                        yp = gsy // 18 * 3.5
                    elif voceMarcata == 3:
                        canaleSoundPuntatore.play(spostapun)
                        yp = gsy // 18 * 6
                    elif voceMarcata == 4:
                        canaleSoundPuntatore.play(spostapun)
                        yp = gsy // 18 * 8.5
                    voceMarcata -= 1
                else:
                    canaleSoundPuntatore.play(selimp)
            schermo.fill(grigioscu)
            persomenuinizio = pygame.transform.scale(persGrafInizio, (gpx * 18, gpy * 18))
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

        clockMenu.tick(fpsMenu)


def equip(dati, canzone):
    perssta = pygame.transform.scale(perso, (gpx * 5, gpy * 5))
    persstab = pygame.transform.scale(persob, (gpx * 5, gpy * 5))
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 2, gpy // 2))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 2, gpy // 2))
    sfondoOggetto = pygame.transform.scale(sfondoOggettoMenu, (int(gpx * 2), int(gpy * 2)))
    sconosciutoEquip = pygame.transform.scale(sconosciutoEquipMenu, (int(gpx * 2), int(gpy * 2)))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 6.8
    risposta = False
    voceMarcata = 1

    tastop = 0
    tastotempfps = 5

    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
    spada = pygame.transform.scale(vetImgSpadePixellate[dati[6]], (gpx * 5, gpy * 5))
    arco = pygame.transform.scale(vetImgArchiPixellate[dati[128]], (gpx * 5, gpy * 5))
    scudo = pygame.transform.scale(vetImgScudiPixellate[dati[7]], (gpx * 5, gpy * 5))
    armatura = pygame.transform.scale(vetImgArmaturePixellate[dati[8]], (gpx * 5, gpy * 5))
    guanti = pygame.transform.scale(vetImgGuantiPixellate[dati[129]], (gpx * 5, gpy * 5))
    collana = pygame.transform.scale(vetImgCollanePixellate[dati[130]], (gpx * 5, gpy * 5))
    carim = False

    vetImgSpade = []
    vetImgArchi = []
    vetImgArmature = []
    vetImgScudi = []
    vetImgGuanti = []
    vetImgCollane = []
    i = 0
    while i < 5:
        if dati[41 + i] > 0:
            vetImgSpade.append(vetImgSpadeMenu[i])
        else:
            vetImgSpade.append(sconosciutoEquip)
        if dati[46 + i] > 0:
            vetImgArchi.append(vetImgArchiMenu[i])
        else:
            vetImgArchi.append(sconosciutoEquip)
        if dati[51 + i] > 0:
            vetImgArmature.append(vetImgArmatureMenu[i])
        else:
            vetImgArmature.append(sconosciutoEquip)
        if dati[56 + i] > 0:
            vetImgScudi.append(vetImgScudiMenu[i])
        else:
            vetImgScudi.append(sconosciutoEquip)
        if dati[61 + i] > 0:
            vetImgGuanti.append(vetImgGuantiMenu[i])
        else:
            vetImgGuanti.append(sconosciutoEquip)
        if dati[66 + i] > 0:
            vetImgCollane.append(vetImgCollaneMenu[i])
        else:
            vetImgCollane.append(sconosciutoEquip)
        i += 1

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 21, gsy // 18 * 12.5))
        # linea(dove,colore,inizio,fine,spessore)
        pygame.draw.line(schermo, grigioscu, (gsx // 32 * 4.5, (gsy // 18 * 5.5) + (gpy // 2)), (gsx // 32 * 4.5, (gsy // 18 * 15) + (gpy // 2)), gpx // 30)
        pygame.draw.line(schermo, grigioscu, (gsx // 32 * 8, (gsy // 18 * 4) + (gpy // 2)), (gsx // 32 * 8, (gsy // 18 * 15.5) + (gpy // 2)), gpx // 20)
        pygame.draw.line(schermo, grigioscu, (gsx // 32 * 11.5, (gsy // 18 * 5.5) + (gpy // 2)), (gsx // 32 * 11.5, (gsy // 18 * 15) + (gpy // 2)), gpx // 30)
        pygame.draw.line(schermo, grigioscu, (gsx // 32 * 15, (gsy // 18 * 4) + (gpy // 2)), (gsx // 32 * 15, (gsy // 18 * 15.5) + (gpy // 2)), gpx // 20)
        pygame.draw.line(schermo, grigioscu, (gsx // 32 * 18.5, (gsy // 18 * 5.5) + (gpy // 2)), (gsx // 32 * 18.5, (gsy // 18 * 15) + (gpy // 2)), gpx // 30)

        if carim:
            spada = pygame.transform.scale(vetImgSpadePixellate[dati[6]], (gpx * 5, gpy * 5))
            arco = pygame.transform.scale(vetImgArchiPixellate[dati[128]], (gpx * 5, gpy * 5))
            scudo = pygame.transform.scale(vetImgScudiPixellate[dati[7]], (gpx * 5, gpy * 5))
            armatura = pygame.transform.scale(vetImgArmaturePixellate[dati[8]], (gpx * 5, gpy * 5))
            guanti = pygame.transform.scale(vetImgGuantiPixellate[dati[129]], (gpx * 5, gpy * 5))
            collana = pygame.transform.scale(vetImgCollanePixellate[dati[130]], (gpx * 5, gpy * 5))
            carim = False
        messaggio("Equipaggiamento", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
        messaggio("Armi", grigiochi, gsx // 32 * 3.3, gsy // 18 * 4.2, 70)
        messaggio("Spade", grigiochi, gsx // 32 * 2, gsy // 18 * 5.3, 50)
        i = 0
        while i < 5:
            schermo.blit(sfondoOggetto, (gsx // 32 * 1.7, (gsy // 18 * 6 + (gpy * 2 * i))))
            schermo.blit(vetImgSpade[i], (gsx // 32 * 1.7, (gsy // 18 * 6 + (gpy * 2 * i))))
            i += 1
        messaggio("Archi", grigiochi, gsx // 32 * 5.5, gsy // 18 * 5.3, 50)
        i = 0
        while i < 5:
            schermo.blit(sfondoOggetto, (gsx // 32 * 5.2, (gsy // 18 * 6 + (gpy * 2 * i))))
            schermo.blit(vetImgArchi[i], (gsx // 32 * 5.2, (gsy // 18 * 6 + (gpy * 2 * i))))
            i += 1
        messaggio("Protezioni", grigiochi, gsx // 32 * 9.3, gsy // 18 * 4.2, 70)
        messaggio("Armature", grigiochi, gsx // 32 * 8.4, gsy // 18 * 5.3, 50)
        i = 0
        while i < 5:
            schermo.blit(sfondoOggetto, (gsx // 32 * 8.7, (gsy // 18 * 6 + (gpy * 2 * i))))
            schermo.blit(vetImgArmature[i], (gsx // 32 * 8.7, (gsy // 18 * 6 + (gpy * 2 * i))))
            i += 1
        messaggio("Scudi", grigiochi, gsx // 32 * 12.5, gsy // 18 * 5.3, 50)
        i = 0
        while i < 5:
            schermo.blit(sfondoOggetto, (gsx // 32 * 12.2, (gsy // 18 * 6 + (gpy * 2 * i))))
            schermo.blit(vetImgScudi[i], (gsx // 32 * 12.2, int((gsy // 18 * 6) + (gpy * 2 * i))))
            i += 1
        messaggio("Accessori", grigiochi, gsx // 32 * 16.3, gsy // 18 * 4.2, 70)
        messaggio("Guanti", grigiochi, gsx // 32 * 15.8, gsy // 18 * 5.3, 50)
        i = 0
        while i < 5:
            schermo.blit(sfondoOggetto, (gsx // 32 * 15.7, (gsy // 18 * 6 + (gpy * 2 * i))))
            schermo.blit(vetImgGuanti[i], (gsx // 32 * 15.7, int((gsy // 18 * 6) + (gpy * 2 * i))))
            i += 1
        messaggio("Collane", grigiochi, gsx // 32 * 19.2, gsy // 18 * 5.3, 50)
        i = 0
        while i < 5:
            schermo.blit(sfondoOggetto, (gsx // 32 * 19.2, (gsy // 18 * 6 + (gpy * 2 * i))))
            schermo.blit(vetImgCollane[i], (gsx // 32 * 19.2, ((gsy // 18 * 6) + (gpy * 2 * i))))
            i += 1

        esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

        schermo.blit(arco, (gsx // 32 * 24.5, gsy // 18 * 11.3))
        schermo.blit(perssta, (gsx // 32 * 24.5, gsy // 18 * 11.3))
        schermo.blit(persstab, (gsx // 32 * 24.5, gsy // 18 * 11.3))
        schermo.blit(armatura, (gsx // 32 * 24.5, gsy // 18 * 11.3))
        schermo.blit(collana, (gsx // 32 * 24.5, gsy // 18 * 11.3))
        schermo.blit(spada, (gsx // 32 * 24.5, gsy // 18 * 11.3))
        schermo.blit(guanti, (gsx // 32 * 24.5, gsy // 18 * 11.3))
        schermo.blit(scudo, (gsx // 32 * 24.5, gsy // 18 * 11.3))
        messaggio("Statistiche:", grigiochi, gsx // 32 * 23, gsy // 18 * 6.7, 50)
        messaggio("Punti vita: %i" % pvtot, grigiochi, gsx // 32 * 23, gsy // 18 * 7.5, 35)
        messaggio("Attacco ravvicinato: %i" % attVicino, grigiochi, gsx // 32 * 23, gsy // 18 * 8, 35)
        messaggio("Attacco a distanza: %i" % attLontano, grigiochi, gsx // 32 * 23, gsy // 18 * 8.5, 35)
        messaggio("Difesa: %i" % dif, grigiochi, gsx // 32 * 23, gsy // 18 * 9, 35)
        messaggio(u"Probabilità parata: %i" % par + "%", grigiochi, gsx // 32 * 23, gsy // 18 * 9.5, 35)
        # confronto statistiche
        # spade
        if voceMarcata == 1:
            if dati[41] != 0:
                messaggio("Niente:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Rimuovi spada", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diff = 0 - ((dati[6] * dati[6]) * 10)
                if dati[6] > 0:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
        if voceMarcata == 2:
            if dati[42] != 0:
                messaggio("Spada di ferro:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Semplice spada di ferro", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diff = 10 - ((dati[6] * dati[6]) * 10)
                if dati[6] > 1:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
                elif dati[6] < 1:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 8, 35)
        if voceMarcata == 3:
            if dati[43] != 0:
                messaggio("Spadone d'acciaio:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Grande spadone in acciaio con ornamenti", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("in oro. Rappresenta il modello di spada", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("migliore mai prodotto dall'uomo", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diff = 40 - ((dati[6] * dati[6]) * 10)
                if dati[6] > 2:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
                elif dati[6] < 2:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 8, 35)
        if voceMarcata == 4:
            if dati[44] != 0:
                messaggio("Lykother:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Spada molto leggera e affilata. Si dice che in", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8,
                          35)
                messaggio("origine fosse un dente di un lupo enorme", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diff = 90 - ((dati[6] * dati[6]) * 10)
                if dati[6] > 3:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
                elif dati[6] < 3:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 8, 35)
        if voceMarcata == 5:
            if dati[45] != 0:
                messaggio("Mendaxritas:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Potentissima spada composta da materiali", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("ignoti", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diff = 160 - ((dati[6] * dati[6]) * 10)
                if dati[6] > 4:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
                elif dati[6] < 4:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 8, 35)
        # archi
        if voceMarcata == 6:
            if dati[46] != 0:
                messaggio("Niente:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Rimuovi arco", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diffAtt = 0 - ((dati[128] * dati[128]) * 5)
                if dati[128] > 0:
                    messaggio(str(diffAtt), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
        if voceMarcata == 7:
            if dati[47] != 0:
                messaggio("Arco di legno:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Semplice arco in legno usato dalla maggior", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("parte dei forestieri", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diffAtt = 5 - ((dati[128] * dati[128]) * 5)
                if dati[128] > 1:
                    messaggio(str(diffAtt), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                elif dati[128] < 1:
                    messaggio("+" + str(diffAtt), verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
        if voceMarcata == 8:
            if dati[48] != 0:
                messaggio("Arco di ferro:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio(u"Elaborato arco in ferro usato solo dai più", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("esperti", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diffAtt = 20 - ((dati[128] * dati[128]) * 5)
                if dati[128] > 2:
                    messaggio(str(diffAtt), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                elif dati[128] < 2:
                    messaggio("+" + str(diffAtt), verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
        if voceMarcata == 9:
            if dati[49] != 0:
                messaggio("Arco di precisione:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Sofisticato arco in legno e acciaio. Molto", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("leggero e potente. Massima espressione", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("dell'ingegno umano", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diffAtt = 45 - ((dati[128] * dati[128]) * 5)
                if dati[128] > 3:
                    messaggio(str(diffAtt), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                elif dati[128] < 3:
                    messaggio("+" + str(diffAtt), verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
        if voceMarcata == 10:
            if dati[50] != 0:
                messaggio("Accipiter:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Potentissimo arco di origine sconosciuta", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diffAtt = 80 - ((dati[128] * dati[128]) * 5)
                if dati[128] > 4:
                    messaggio(str(diffAtt), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                elif dati[128] < 4:
                    messaggio("+" + str(diffAtt), verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
        # armature
        if voceMarcata == 11:
            if dati[51] != 0:
                messaggio("Niente:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Rimuovi armatura", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diff = 0 - ((dati[8] * dati[8]) * 10)
                if dati[8] > 0:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
        if voceMarcata == 12:
            if dati[52] != 0:
                messaggio("Armatura di pelle:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Semplice armatura in pelle", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diff = 10 - ((dati[8] * dati[8]) * 10)
                if dati[8] > 1:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                elif dati[8] < 1:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
        if voceMarcata == 13:
            if dati[53] != 0:
                messaggio("Armatura d'acciaio:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Grande armatura d'acciaio con ornamenti", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("in oro. Usata solo dagli ufficiali", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("dell'esercito", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diff = 40 - ((dati[8] * dati[8]) * 10)
                if dati[8] > 2:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                elif dati[8] < 2:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
        if voceMarcata == 14:
            if dati[54] != 0:
                messaggio("Lykodes:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Armatura formata da materiali leggieri e", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("resistenti. Si dice essere composta da ossa", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("di un enorme lupo", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diff = 90 - ((dati[8] * dati[8]) * 10)
                if dati[8] > 3:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                elif dati[8] < 3:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
        if voceMarcata == 15:
            if dati[55] != 0:
                messaggio("Loriquam:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Armatura incredibilmente resistente.", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio(u"La sua origine è ignota", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diff = 160 - ((dati[8] * dati[8]) * 10)
                if dati[8] > 4:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                elif dati[8] < 4:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
        # scudi
        if voceMarcata == 16:
            if dati[56] != 0:
                messaggio("Niente:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Rimuovi scudo", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diff = 0 - ((dati[7] * dati[7]) * 5)
                if dati[7] > 0:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                diff = 0 - ((dati[7] * dati[7]) * 3)
                if dati[7] > 0:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
        if voceMarcata == 17:
            if dati[57] != 0:
                messaggio("Scudo di pelle:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Semplice scudo in pelle", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diff = 5 - ((dati[7] * dati[7]) * 5)
                if dati[7] > 1:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                elif dati[7] < 1:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
                diff = 3 - ((dati[7] * dati[7]) * 3)
                if dati[7] > 1:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
                elif dati[7] < 1:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 28, gsy // 18 * 9.5, 35)
        if voceMarcata == 18:
            if dati[58] != 0:
                messaggio("Scudo d'acciaio:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Sofisticato scudo in acciaio e oro. Studiato", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8,
                          35)
                messaggio(u"per respingere gli attacchi più pesanti", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diff = 20 - ((dati[7] * dati[7]) * 5)
                if dati[7] > 2:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                elif dati[7] < 2:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
                diff = 12 - ((dati[7] * dati[7]) * 3)
                if dati[7] > 2:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
                elif dati[7] < 2:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 28, gsy // 18 * 9.5, 35)
        if voceMarcata == 19:
            if dati[59] != 0:
                messaggio("Lykethmos:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Scudo molto leggere e resistente. Si dice", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio(u"essere composto dalle ossa più resistenti", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("di un enorme lupo", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diff = 45 - ((dati[7] * dati[7]) * 5)
                if dati[7] > 3:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                elif dati[7] < 3:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
                diff = 27 - ((dati[7] * dati[7]) * 3)
                if dati[7] > 3:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
                elif dati[7] < 3:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 28, gsy // 18 * 9.5, 35)
        if voceMarcata == 20:
            if dati[60] != 0:
                messaggio("Clipequam:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio(u"Scudo incredibilmente resistente. Non è ", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("nota l'origine", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                diff = 80 - ((dati[7] * dati[7]) * 5)
                if dati[7] > 4:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                elif dati[7] < 4:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
                diff = 48 - ((dati[7] * dati[7]) * 3)
                if dati[7] > 4:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
                elif dati[7] < 4:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 28, gsy // 18 * 9.5, 35)
        # guanti
        if voceMarcata == 21:
            if dati[61] != 0:
                messaggio("Niente:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Rimuovi guanti", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                if dati[129] == 1:
                    messaggio("-50", rosso, gsx // 32 * 28, gsy // 18 * 7.5, 35)
                elif dati[129] == 2:
                    messaggio("-30", rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                elif dati[129] == 3:
                    messaggio("-30", rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
                    messaggio("-20", rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                elif dati[129] == 4:
                    messaggio("-10%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
        if voceMarcata == 22:
            if dati[62] != 0:
                messaggio("Guanti vitali:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Guanti che aumentano i punti vita massimi", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("del portatore", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                if dati[129] != 1:
                    messaggio("+50", verde, gsx // 32 * 28, gsy // 18 * 7.5, 35)
                if dati[129] == 2:
                    messaggio("-30", rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                elif dati[129] == 3:
                    messaggio("-30", rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
                    messaggio("-20", rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                elif dati[129] == 4:
                    messaggio("-10%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
        if voceMarcata == 23:
            if dati[63] != 0:
                messaggio("Guanti difensivi:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Guanti che consentono di subire meno danno", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("grazie ad una presa salda dello scudo", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                if dati[129] != 2:
                    messaggio("+30", verde, gsx // 32 * 28, gsy // 18 * 9, 35)
                if dati[129] == 1:
                    messaggio("-50", rosso, gsx // 32 * 28, gsy // 18 * 7.5, 35)
                elif dati[129] == 3:
                    messaggio("-30", rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
                    messaggio("-20", rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                elif dati[129] == 4:
                    messaggio("-10%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
        if voceMarcata == 24:
            if dati[64] != 0:
                messaggio("Guanti offensivi:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Guanti che consentono una presa salda", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("dell'arma. Aumentano l'attacco", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                if dati[129] != 3:
                    messaggio("+30", verde, gsx // 32 * 28, gsy // 18 * 8, 35)
                    messaggio("+20", verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                if dati[129] == 1:
                    messaggio("-50", rosso, gsx // 32 * 28, gsy // 18 * 7.5, 35)
                elif dati[129] == 2:
                    messaggio("-30", rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                elif dati[129] == 4:
                    messaggio("-10%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
        if voceMarcata == 25:
            if dati[65] != 0:
                messaggio("Guanti confortevoli:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio(u"Guanti che aumentano la probabilità di", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("parare gli attacchi grazie ad una presa", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("agevole dello scudo", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                if dati[129] != 4:
                    messaggio("+10%", verde, gsx // 32 * 28, gsy // 18 * 9.5, 35)
                if dati[129] == 1:
                    messaggio("-50", rosso, gsx // 32 * 28, gsy // 18 * 7.5, 35)
                elif dati[129] == 2:
                    messaggio("-30", rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                elif dati[129] == 3:
                    messaggio("-30", rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
                    messaggio("-20", rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
        # collane
        if voceMarcata == 26:
            if dati[66] != 0:
                messaggio("Niente:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Rimuovi collana", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
        if voceMarcata == 27:
            if dati[67] != 0:
                messaggio("Collana medicinale:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Collana composta da erbe il cui odore", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio(u"neutralizza la tissicità del veleno", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio(u"(non ha effetto se si è già avvelenati)", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
        if voceMarcata == 28:
            if dati[68] != 0:
                messaggio("Collana rigenerante:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio("Collana composta da erbe il cui odore", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("ripristina punti vita ogni turno", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
        if voceMarcata == 29:
            if dati[69] != 0:
                messaggio("Apprendimaschera:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio(u"Collana che consente di ricevere più punti", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                messaggio("esperienza", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
        if voceMarcata == 30:
            if dati[70] != 0:
                messaggio("Portafortuna:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                messaggio(u"Collana che permette di ottenere più monete", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8,
                          35)
                messaggio("dai nemici", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)

        # puntatore vecchio
        if dati[6] == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 6.8))
        if dati[6] == 1:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 8.8))
        if dati[6] == 2:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 10.8))
        if dati[6] == 3:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 12.8))
        if dati[6] == 4:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 14.8))
        if dati[128] == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 4.5, gsy // 18 * 6.8))
        if dati[128] == 1:
            schermo.blit(puntatorevecchio, (gsx // 32 * 4.5, gsy // 18 * 8.8))
        if dati[128] == 2:
            schermo.blit(puntatorevecchio, (gsx // 32 * 4.5, gsy // 18 * 10.8))
        if dati[128] == 3:
            schermo.blit(puntatorevecchio, (gsx // 32 * 4.5, gsy // 18 * 12.8))
        if dati[128] == 4:
            schermo.blit(puntatorevecchio, (gsx // 32 * 4.5, gsy // 18 * 14.8))
        if dati[8] == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 6.8))
        if dati[8] == 1:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 8.8))
        if dati[8] == 2:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 10.8))
        if dati[8] == 3:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 12.8))
        if dati[8] == 4:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 14.8))
        if dati[7] == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 11.5, gsy // 18 * 6.8))
        if dati[7] == 1:
            schermo.blit(puntatorevecchio, (gsx // 32 * 11.5, gsy // 18 * 8.8))
        if dati[7] == 2:
            schermo.blit(puntatorevecchio, (gsx // 32 * 11.5, gsy // 18 * 10.8))
        if dati[7] == 3:
            schermo.blit(puntatorevecchio, (gsx // 32 * 11.5, gsy // 18 * 12.8))
        if dati[7] == 4:
            schermo.blit(puntatorevecchio, (gsx // 32 * 11.5, gsy // 18 * 14.8))
        if dati[129] == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 6.8))
        if dati[129] == 1:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 8.8))
        if dati[129] == 2:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 10.8))
        if dati[129] == 3:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 12.8))
        if dati[129] == 4:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 14.8))
        if dati[130] == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 18.5, gsy // 18 * 6.8))
        if dati[130] == 1:
            schermo.blit(puntatorevecchio, (gsx // 32 * 18.5, gsy // 18 * 8.8))
        if dati[130] == 2:
            schermo.blit(puntatorevecchio, (gsx // 32 * 18.5, gsy // 18 * 10.8))
        if dati[130] == 3:
            schermo.blit(puntatorevecchio, (gsx // 32 * 18.5, gsy // 18 * 12.8))
        if dati[130] == 4:
            schermo.blit(puntatorevecchio, (gsx // 32 * 18.5, gsy // 18 * 14.8))

        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        if not canaleSoundCanzone.get_busy():
            canaleSoundCanzone.play(canzone)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 3

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato:
                tastop = event.key
                tastotempfps = 5
                if event.key == pygame.K_q and not tastoTrovato:
                    tastoTrovato = True
                    canaleSoundPuntatore.play(selind)
                    risposta = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_SPACE and not tastoTrovato:
                    tastoTrovato = True
                    carim = True
                    # progresso-stanza-x-y-liv-pv-spada-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                    # spade
                    if voceMarcata == 1:
                        if dati[41] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[6] = 0
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 2:
                        if dati[42] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[6] = 1
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 3:
                        if dati[43] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[6] = 2
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 4:
                        if dati[44] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[6] = 3
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 5:
                        if dati[45] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[6] = 4
                        else:
                            canaleSoundPuntatore.play(selimp)
                    # spade
                    if voceMarcata == 6:
                        if dati[46] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[128] = 0
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 7:
                        if dati[47] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[128] = 1
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 8:
                        if dati[48] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[128] = 2
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 9:
                        if dati[49] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[128] = 3
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 10:
                        if dati[50] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[128] = 4
                        else:
                            canaleSoundPuntatore.play(selimp)
                    # armature
                    if voceMarcata == 11:
                        if dati[51] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[8] = 0
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 12:
                        if dati[52] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[8] = 1
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 13:
                        if dati[53] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[8] = 2
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 14:
                        if dati[54] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[8] = 3
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 15:
                        if dati[55] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[8] = 4
                        else:
                            canaleSoundPuntatore.play(selimp)
                    # scudi
                    if voceMarcata == 16:
                        if dati[56] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[7] = 0
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 17:
                        if dati[57] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[7] = 1
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 18:
                        if dati[58] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[7] = 2
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 19:
                        if dati[59] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[7] = 3
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 20:
                        if dati[60] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[7] = 4
                        else:
                            canaleSoundPuntatore.play(selimp)
                    # guanti
                    if voceMarcata == 21:
                        if dati[61] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[129] = 0
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 22:
                        if dati[62] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[129] = 1
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 23:
                        if dati[63] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[129] = 2
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 24:
                        if dati[64] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[129] = 3
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 25:
                        if dati[65] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[129] = 4
                        else:
                            canaleSoundPuntatore.play(selimp)
                    # collane
                    if voceMarcata == 26:
                        if dati[66] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[130] = 0
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 27:
                        if dati[67] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[130] = 1
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 28:
                        if dati[68] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[130] = 2
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 29:
                        if dati[69] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[130] = 3
                        else:
                            canaleSoundPuntatore.play(selimp)
                    if voceMarcata == 30:
                        if dati[70] != 0:
                            canaleSoundPuntatore.play(selezione)
                            dati[130] = 4
                        else:
                            canaleSoundPuntatore.play(selimp)
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_q or tastop == pygame.K_SPACE or ((tastop == pygame.K_d or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_w) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_d or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_w):
                tastotempfps = 3
            if tastop == pygame.K_s:
                if voceMarcata == 5 or voceMarcata == 10 or voceMarcata == 15 or voceMarcata == 20 or voceMarcata == 25 or voceMarcata == 30:
                    voceMarcata -= 4
                    canaleSoundPuntatore.play(spostapun)
                    yp = gsy // 18 * 6.8
                else:
                    voceMarcata += 1
                    canaleSoundPuntatore.play(spostapun)
                    yp += gsy // 18 * 2
            if tastop == pygame.K_w:
                if voceMarcata == 1 or voceMarcata == 6 or voceMarcata == 11 or voceMarcata == 16 or voceMarcata == 21 or voceMarcata == 26:
                    voceMarcata += 4
                    canaleSoundPuntatore.play(spostapun)
                    yp = gsy // 18 * 14.8
                else:
                    voceMarcata -= 1
                    canaleSoundPuntatore.play(spostapun)
                    yp = yp - gsy // 18 * 2
            if tastop == pygame.K_d:
                if voceMarcata == 26 or voceMarcata == 27 or voceMarcata == 28 or voceMarcata == 29 or voceMarcata == 30:
                    voceMarcata -= 25
                    canaleSoundPuntatore.play(spostapun)
                    xp = gsx // 32 * 1
                else:
                    voceMarcata += 5
                    canaleSoundPuntatore.play(spostapun)
                    xp = xp + gsx // 32 * 3.5
            if tastop == pygame.K_a:
                if voceMarcata == 1 or voceMarcata == 2 or voceMarcata == 3 or voceMarcata == 4 or voceMarcata == 5:
                    voceMarcata += 25
                    canaleSoundPuntatore.play(spostapun)
                    xp = gsx // 32 * 18.5
                else:
                    voceMarcata -= 5
                    canaleSoundPuntatore.play(spostapun)
                    xp = xp - gsx // 32 * 3.5
            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 21, gsy // 18 * 12.5))
            # linea(dove,colore,inizio,fine,spessore)
            pygame.draw.line(schermo, grigioscu, (gsx // 32 * 4.5, (gsy // 18 * 5.5) + (gpy // 2)), (gsx // 32 * 4.5, (gsy // 18 * 15) + (gpy // 2)), gpx // 30)
            pygame.draw.line(schermo, grigioscu, (gsx // 32 * 8, (gsy // 18 * 4) + (gpy // 2)), (gsx // 32 * 8, (gsy // 18 * 15.5) + (gpy // 2)), gpx // 20)
            pygame.draw.line(schermo, grigioscu, (gsx // 32 * 11.5, (gsy // 18 * 5.5) + (gpy // 2)), (gsx // 32 * 11.5, (gsy // 18 * 15) + (gpy // 2)), gpx // 30)
            pygame.draw.line(schermo, grigioscu, (gsx // 32 * 15, (gsy // 18 * 4) + (gpy // 2)), (gsx // 32 * 15, (gsy // 18 * 15.5) + (gpy // 2)), gpx // 20)
            pygame.draw.line(schermo, grigioscu, (gsx // 32 * 18.5, (gsy // 18 * 5.5) + (gpy // 2)), (gsx // 32 * 18.5, (gsy // 18 * 15) + (gpy // 2)), gpx // 30)

            if carim:
                spada = pygame.transform.scale(vetImgSpadePixellate[dati[6]], (gpx * 5, gpy * 5))
                arco = pygame.transform.scale(vetImgArchiPixellate[dati[128]], (gpx * 5, gpy * 5))
                scudo = pygame.transform.scale(vetImgScudiPixellate[dati[7]], (gpx * 5, gpy * 5))
                armatura = pygame.transform.scale(vetImgArmaturePixellate[dati[8]], (gpx * 5, gpy * 5))
                guanti = pygame.transform.scale(vetImgGuantiPixellate[dati[129]], (gpx * 5, gpy * 5))
                collana = pygame.transform.scale(vetImgCollanePixellate[dati[130]], (gpx * 5, gpy * 5))
                carim = False
            messaggio("Equipaggiamento", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
            messaggio("Armi", grigiochi, gsx // 32 * 3.3, gsy // 18 * 4.2, 70)
            messaggio("Spade", grigiochi, gsx // 32 * 2, gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                schermo.blit(sfondoOggetto, (gsx // 32 * 1.7, (gsy // 18 * 6 + (gpy * 2 * i))))
                schermo.blit(vetImgSpade[i], (gsx // 32 * 1.7, (gsy // 18 * 6 + (gpy * 2 * i))))
                i += 1
            messaggio("Archi", grigiochi, gsx // 32 * 5.5, gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                schermo.blit(sfondoOggetto, (gsx // 32 * 5.2, (gsy // 18 * 6 + (gpy * 2 * i))))
                schermo.blit(vetImgArchi[i], (gsx // 32 * 5.2, (gsy // 18 * 6 + (gpy * 2 * i))))
                i += 1
            messaggio("Protezioni", grigiochi, gsx // 32 * 9.3, gsy // 18 * 4.2, 70)
            messaggio("Armature", grigiochi, gsx // 32 * 8.4, gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                schermo.blit(sfondoOggetto, (gsx // 32 * 8.7, (gsy // 18 * 6 + (gpy * 2 * i))))
                schermo.blit(vetImgArmature[i], (gsx // 32 * 8.7, (gsy // 18 * 6 + (gpy * 2 * i))))
                i += 1
            messaggio("Scudi", grigiochi, gsx // 32 * 12.5, gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                schermo.blit(sfondoOggetto, (gsx // 32 * 12.2, (gsy // 18 * 6 + (gpy * 2 * i))))
                schermo.blit(vetImgScudi[i], (gsx // 32 * 12.2, int((gsy // 18 * 6) + (gpy * 2 * i))))
                i += 1
            messaggio("Accessori", grigiochi, gsx // 32 * 16.3, gsy // 18 * 4.2, 70)
            messaggio("Guanti", grigiochi, gsx // 32 * 15.8, gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                schermo.blit(sfondoOggetto, (gsx // 32 * 15.7, (gsy // 18 * 6 + (gpy * 2 * i))))
                schermo.blit(vetImgGuanti[i], (gsx // 32 * 15.7, int((gsy // 18 * 6) + (gpy * 2 * i))))
                i += 1
            messaggio("Collane", grigiochi, gsx // 32 * 19.2, gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                schermo.blit(sfondoOggetto, (gsx // 32 * 19.2, (gsy // 18 * 6 + (gpy * 2 * i))))
                schermo.blit(vetImgCollane[i], (gsx // 32 * 19.2, ((gsy // 18 * 6) + (gpy * 2 * i))))
                i += 1

            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
            if dati[5] > pvtot:
                dati[5] = pvtot

            schermo.blit(arco, (gsx // 32 * 24.5, gsy // 18 * 11.3))
            schermo.blit(perssta, (gsx // 32 * 24.5, gsy // 18 * 11.3))
            schermo.blit(persstab, (gsx // 32 * 24.5, gsy // 18 * 11.3))
            schermo.blit(armatura, (gsx // 32 * 24.5, gsy // 18 * 11.3))
            schermo.blit(collana, (gsx // 32 * 24.5, gsy // 18 * 11.3))
            schermo.blit(spada, (gsx // 32 * 24.5, gsy // 18 * 11.3))
            schermo.blit(guanti, (gsx // 32 * 24.5, gsy // 18 * 11.3))
            schermo.blit(scudo, (gsx // 32 * 24.5, gsy // 18 * 11.3))
            messaggio("Statistiche:", grigiochi, gsx // 32 * 23, gsy // 18 * 6.7, 50)
            messaggio("Punti vita: %i" % pvtot, grigiochi, gsx // 32 * 23, gsy // 18 * 7.5, 35)
            messaggio("Attacco ravvicinato: %i" % attVicino, grigiochi, gsx // 32 * 23, gsy // 18 * 8, 35)
            messaggio("Attacco a distanza: %i" % attLontano, grigiochi, gsx // 32 * 23, gsy // 18 * 8.5, 35)
            messaggio("Difesa: %i" % dif, grigiochi, gsx // 32 * 23, gsy // 18 * 9, 35)
            messaggio(u"Probabilità parata: %i" % par + "%", grigiochi, gsx // 32 * 23, gsy // 18 * 9.5, 35)
            # confronto statistiche
            # spade
            if voceMarcata == 1:
                if dati[41] != 0:
                    messaggio("Niente:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi spada", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diff = 0 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 0:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
            if voceMarcata == 2:
                if dati[42] != 0:
                    messaggio("Spada di ferro:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Semplice spada di ferro", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diff = 10 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 1:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
                    elif dati[6] < 1:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 8, 35)
            if voceMarcata == 3:
                if dati[43] != 0:
                    messaggio("Spadone d'acciaio:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Grande spadone in acciaio con ornamenti", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("in oro. Rappresenta il modello di spada", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("migliore mai prodotto dall'uomo", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diff = 40 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 2:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
                    elif dati[6] < 2:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 8, 35)
            if voceMarcata == 4:
                if dati[44] != 0:
                    messaggio("Lykother:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Spada molto leggera e affilata. Si dice che in", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("origine fosse un dente di un lupo enorme", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diff = 90 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 3:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
                    elif dati[6] < 3:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 8, 35)
            if voceMarcata == 5:
                if dati[45] != 0:
                    messaggio("Mendaxritas:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Potentissima spada composta da materiali", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("ignoti", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diff = 160 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 4:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
                    elif dati[6] < 4:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 8, 35)
            # archi
            if voceMarcata == 6:
                if dati[46] != 0:
                    messaggio("Niente:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi arco", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diffAtt = 0 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 0:
                        messaggio(str(diffAtt), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
            if voceMarcata == 7:
                if dati[47] != 0:
                    messaggio("Arco di legno:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Semplice arco in legno usato dalla maggior", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("parte dei forestieri", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diffAtt = 5 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 1:
                        messaggio(str(diffAtt), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                    elif dati[128] < 1:
                        messaggio("+" + str(diffAtt), verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
            if voceMarcata == 8:
                if dati[48] != 0:
                    messaggio("Arco di ferro:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio(u"Elaborato arco in ferro usato solo dai più", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("esperti", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diffAtt = 20 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 2:
                        messaggio(str(diffAtt), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                    elif dati[128] < 2:
                        messaggio("+" + str(diffAtt), verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
            if voceMarcata == 9:
                if dati[49] != 0:
                    messaggio("Arco di precisione:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Sofisticato arco in legno e acciaio. Molto", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("leggero e potente. Massima espressione", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("dell'ingegno umano", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diffAtt = 45 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 3:
                        messaggio(str(diffAtt), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                    elif dati[128] < 3:
                        messaggio("+" + str(diffAtt), verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
            if voceMarcata == 10:
                if dati[50] != 0:
                    messaggio("Accipiter:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Potentissimo arco di origine sconosciuta", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diffAtt = 80 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 4:
                        messaggio(str(diffAtt), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                    elif dati[128] < 4:
                        messaggio("+" + str(diffAtt), verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
            # armature
            if voceMarcata == 11:
                if dati[51] != 0:
                    messaggio("Niente:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi armatura", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diff = 0 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 0:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
            if voceMarcata == 12:
                if dati[52] != 0:
                    messaggio("Armatura di pelle:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Semplice armatura in pelle", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diff = 10 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 1:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                    elif dati[8] < 1:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
            if voceMarcata == 13:
                if dati[53] != 0:
                    messaggio("Armatura d'acciaio:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Grande armatura d'acciaio con ornamenti", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("in oro. Usata solo dagli ufficiali", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("dell'esercito", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diff = 40 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 2:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                    elif dati[8] < 2:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
            if voceMarcata == 14:
                if dati[54] != 0:
                    messaggio("Lykodes:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Armatura formata da materiali leggieri e", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("resistenti. Si dice essere composta da ossa", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("di un enorme lupo", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diff = 90 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 3:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                    elif dati[8] < 3:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
            if voceMarcata == 15:
                if dati[55] != 0:
                    messaggio("Loriquam:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Armatura incredibilmente resistente.", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio(u"La sua origine è ignota", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diff = 160 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 4:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                    elif dati[8] < 4:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
            # scudi
            if voceMarcata == 16:
                if dati[56] != 0:
                    messaggio("Niente:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi scudo", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diff = 0 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 0:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                    diff = 0 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 0:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
            if voceMarcata == 17:
                if dati[57] != 0:
                    messaggio("Scudo di pelle:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Semplice scudo in pelle", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diff = 5 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 1:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                    elif dati[7] < 1:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
                    diff = 3 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 1:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
                    elif dati[7] < 1:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 28, gsy // 18 * 9.5, 35)
            if voceMarcata == 18:
                if dati[58] != 0:
                    messaggio("Scudo d'acciaio:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Sofisticato scudo in acciaio e oro. Studiato", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio(u"per respingere gli attacchi più pesanti", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diff = 20 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 2:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                    elif dati[7] < 2:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
                    diff = 12 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 2:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
                    elif dati[7] < 2:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 28, gsy // 18 * 9.5, 35)
            if voceMarcata == 19:
                if dati[59] != 0:
                    messaggio("Lykethmos:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Scudo molto leggere e resistente. Si dice", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio(u"essere composto dalle ossa più resistenti", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("di un enorme lupo", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diff = 45 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 3:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                    elif dati[7] < 3:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
                    diff = 27 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 3:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
                    elif dati[7] < 3:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 28, gsy // 18 * 9.5, 35)
            if voceMarcata == 20:
                if dati[60] != 0:
                    messaggio("Clipequam:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio(u"Scudo incredibilmente resistente. Non è ", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("nota l'origine", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    diff = 80 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 4:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                    elif dati[7] < 4:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
                    diff = 48 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 4:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
                    elif dati[7] < 4:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 28, gsy // 18 * 9.5, 35)
            # guanti
            if voceMarcata == 21:
                if dati[61] != 0:
                    messaggio("Niente:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi guanti", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    if dati[129] == 1:
                        messaggio("-50", rosso, gsx // 32 * 28, gsy // 18 * 7.5, 35)
                    elif dati[129] == 2:
                        messaggio("-30", rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                    elif dati[129] == 3:
                        messaggio("-20", rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
                        messaggio("-20", rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                    elif dati[129] == 4:
                        messaggio("-10%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
            if voceMarcata == 22:
                if dati[62] != 0:
                    messaggio("Guanti vitali:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Guanti che aumentano i punti vita massimi", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("del portatore", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    if dati[129] != 1:
                        messaggio("+50", verde, gsx // 32 * 28, gsy // 18 * 7.5, 35)
                    if dati[129] == 2:
                        messaggio("-30", rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                    elif dati[129] == 3:
                        messaggio("-20", rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
                        messaggio("-20", rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                    elif dati[129] == 4:
                        messaggio("-10%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
            if voceMarcata == 23:
                if dati[63] != 0:
                    messaggio("Guanti difensivi:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Guanti che consentono di subire meno danno", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("grazie ad una presa salda dello scudo", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    if dati[129] != 2:
                        messaggio("+30", verde, gsx // 32 * 28, gsy // 18 * 9, 35)
                    if dati[129] == 1:
                        messaggio("-50", rosso, gsx // 32 * 28, gsy // 18 * 7.5, 35)
                    elif dati[129] == 3:
                        messaggio("-20", rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
                        messaggio("-20", rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                    elif dati[129] == 4:
                        messaggio("-10%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
            if voceMarcata == 24:
                if dati[64] != 0:
                    messaggio("Guanti offensivi:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Guanti che consentono una presa salda", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("dell'arma. Aumentano l'attacco", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    if dati[129] != 3:
                        messaggio("+20", verde, gsx // 32 * 28, gsy // 18 * 8, 35)
                        messaggio("+20", verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                    if dati[129] == 1:
                        messaggio("-50", rosso, gsx // 32 * 28, gsy // 18 * 7.5, 35)
                    elif dati[129] == 2:
                        messaggio("-30", rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                    elif dati[129] == 4:
                        messaggio("-10%", rosso, gsx // 32 * 28, gsy // 18 * 9.5, 35)
            if voceMarcata == 25:
                if dati[65] != 0:
                    messaggio("Guanti confortevoli:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio(u"Guanti che aumentano la probabilità di", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("parare gli attacchi grazie ad una presa", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("agevole dello scudo", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
                    if dati[129] != 4:
                        messaggio("+10%", verde, gsx // 32 * 28, gsy // 18 * 9.5, 35)
                    if dati[129] == 1:
                        messaggio("-50", rosso, gsx // 32 * 28, gsy // 18 * 7.5, 35)
                    elif dati[129] == 2:
                        messaggio("-30", rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                    elif dati[129] == 3:
                        messaggio("-20", rosso, gsx // 32 * 28, gsy // 18 * 8, 35)
                        messaggio("-20", rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
            # collane
            if voceMarcata == 26:
                if dati[66] != 0:
                    messaggio("Niente:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi collana", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
            if voceMarcata == 27:
                if dati[67] != 0:
                    messaggio("Collana medicinale:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Collana composta da erbe il cui odore", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio(u"neutralizza la tissicità del veleno", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio(u"(non ha effetto se si è già avvelenati)", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
            if voceMarcata == 28:
                if dati[68] != 0:
                    messaggio("Collana rigenerante:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio("Collana composta da erbe il cui odore", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("ripristina punti vita ogni turno", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
            if voceMarcata == 29:
                if dati[69] != 0:
                    messaggio("Apprendimaschera:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio(u"Collana che consente di ricevere più punti", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("esperienza", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)
            if voceMarcata == 30:
                if dati[70] != 0:
                    messaggio("Portafortuna:", grigiochi, gsx // 32 * 23, gsy // 18 * 3.8, 60)
                    messaggio(u"Collana che permette di ottenere più monete", grigiochi, gsx // 32 * 23, gsy // 18 * 4.8, 35)
                    messaggio("dai nemici", grigiochi, gsx // 32 * 23, gsy // 18 * 5.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 23, gsy // 18 * 5.8, 35)

            # puntatore vecchio
            if dati[6] == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 6.8))
            if dati[6] == 1:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 8.8))
            if dati[6] == 2:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 10.8))
            if dati[6] == 3:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 12.8))
            if dati[6] == 4:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 14.8))
            if dati[128] == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 4.5, gsy // 18 * 6.8))
            if dati[128] == 1:
                schermo.blit(puntatorevecchio, (gsx // 32 * 4.5, gsy // 18 * 8.8))
            if dati[128] == 2:
                schermo.blit(puntatorevecchio, (gsx // 32 * 4.5, gsy // 18 * 10.8))
            if dati[128] == 3:
                schermo.blit(puntatorevecchio, (gsx // 32 * 4.5, gsy // 18 * 12.8))
            if dati[128] == 4:
                schermo.blit(puntatorevecchio, (gsx // 32 * 4.5, gsy // 18 * 14.8))
            if dati[8] == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 6.8))
            if dati[8] == 1:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 8.8))
            if dati[8] == 2:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 10.8))
            if dati[8] == 3:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 12.8))
            if dati[8] == 4:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 14.8))
            if dati[7] == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 11.5, gsy // 18 * 6.8))
            if dati[7] == 1:
                schermo.blit(puntatorevecchio, (gsx // 32 * 11.5, gsy // 18 * 8.8))
            if dati[7] == 2:
                schermo.blit(puntatorevecchio, (gsx // 32 * 11.5, gsy // 18 * 10.8))
            if dati[7] == 3:
                schermo.blit(puntatorevecchio, (gsx // 32 * 11.5, gsy // 18 * 12.8))
            if dati[7] == 4:
                schermo.blit(puntatorevecchio, (gsx // 32 * 11.5, gsy // 18 * 14.8))
            if dati[129] == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 6.8))
            if dati[129] == 1:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 8.8))
            if dati[129] == 2:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 10.8))
            if dati[129] == 3:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 12.8))
            if dati[129] == 4:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 14.8))
            if dati[130] == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 18.5, gsy // 18 * 6.8))
            if dati[130] == 1:
                schermo.blit(puntatorevecchio, (gsx // 32 * 18.5, gsy // 18 * 8.8))
            if dati[130] == 2:
                schermo.blit(puntatorevecchio, (gsx // 32 * 18.5, gsy // 18 * 10.8))
            if dati[130] == 3:
                schermo.blit(puntatorevecchio, (gsx // 32 * 18.5, gsy // 18 * 12.8))
            if dati[130] == 4:
                schermo.blit(puntatorevecchio, (gsx // 32 * 18.5, gsy // 18 * 14.8))

            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        clockMenu.tick(fpsMenu)
    return dati


def sceglicondiz(dati, condizione, canzone):
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 2, gpy // 2))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 2, gpy // 2))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 4.6
    risposta = False
    voceMarcata = 0

    tastop = 0
    tastotempfps = 5

    # carico le scenette
    scecond = vetImgCondizioniMenu

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 15, gsy // 18 * 12.5))

        messaggio("Scegli condizione", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
        messaggio("Cancella", grigiochi, gsx // 32 * 2, gsy // 18 * 4.7, 45)
        if voceMarcata == 0:
            messaggio("Cancella:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
            messaggio("Cancella il settaggio di Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
            messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
            messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        if dati[81] > 0:
            messaggio("Rallo con pv < 80%", grigiochi, gsx // 32 * 2, gsy // 18 * 6.2, 40)
            if voceMarcata == 1:
                schermo.blit(scecond[1], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Rallo con pv < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su Rallo quando ha pv < 80%", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5,
                          35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6.2, 40)
        if dati[82] > 0:
            messaggio("Rallo con pv < 50%", grigiochi, gsx // 32 * 2, gsy // 18 * 7.2, 40)
            if voceMarcata == 2:
                schermo.blit(scecond[2], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Rallo con pv < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su Rallo quando ha pv < 50%", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5,
                          35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7.2, 40)
        if dati[83] > 0:
            messaggio("Rallo con pv < 30%", grigiochi, gsx // 32 * 2, gsy // 18 * 8.2, 40)
            if voceMarcata == 3:
                schermo.blit(scecond[3], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Rallo con pv < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su Rallo quando ha pv < 30%", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5,
                          35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8.2, 40)
        if dati[84] > 0:
            messaggio("Rallo con veleno", grigiochi, gsx // 32 * 2, gsy // 18 * 9.2, 40)
            if voceMarcata == 4:
                schermo.blit(scecond[4], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Rallo con veleno:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio(u"Esegue l'azione su Rallo quando è avvelenato", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5,
                          35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9.2, 40)
        if dati[85] > 0:
            messaggio("Colco surriscaldato", grigiochi, gsx // 32 * 2, gsy // 18 * 10.2, 40)
            if voceMarcata == 5:
                schermo.blit(scecond[5], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Colco surriscaldato:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio(u"Esegue l'azione su Colco quando è surriscaldato", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10.2, 40)
        if dati[86] > 0:
            messaggio("Colco con pe < 80%", grigiochi, gsx // 32 * 2, gsy // 18 * 11.2, 40)
            if voceMarcata == 6:
                schermo.blit(scecond[6], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Colco con pe < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su Colco quando ha pe < 80%", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5,
                          35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11.2, 40)
        if dati[87] > 0:
            messaggio("Colco con pe < 50%", grigiochi, gsx // 32 * 2, gsy // 18 * 12.2, 40)
            if voceMarcata == 7:
                schermo.blit(scecond[7], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Colco con pe < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su Colco quando ha pe < 50%", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5,
                          35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12.2, 40)
        if dati[88] > 0:
            messaggio("Colco con pe < 30%", grigiochi, gsx // 32 * 2, gsy // 18 * 13.2, 40)
            if voceMarcata == 8:
                schermo.blit(scecond[8], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Colco con pe < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su Colco quando ha pe < 30%", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5,
                          35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13.2, 40)
        if dati[89] > 0:
            messaggio("Sempre a Rallo", grigiochi, gsx // 32 * 2, gsy // 18 * 14.2, 40)
            if voceMarcata == 9:
                schermo.blit(scecond[9], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Sempre a Rallo:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su Rallo in continuazione (se la tecnica associata", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("comporta uno status alterativo, viene eseguita solo se lo status non", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio(u"è attivo)", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14.2, 40)
        if dati[90] > 0:
            messaggio("Sempre a Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 15.2, 40)
            if voceMarcata == 10:
                schermo.blit(scecond[10], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Sempre a Colco:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su Colco in continuazione (se la tecnica associata", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("comporta uno status alterativo, viene eseguita solo se lo status non", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio(u"è attivo)", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15.2, 40)
        if dati[91] > 0:
            messaggio("Nemico a caso", grigiochi, gsx // 32 * 9, gsy // 18 * 6.2, 40)
            if voceMarcata == 11:
                schermo.blit(scecond[11], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Nemico a caso:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su un nemico a caso", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6.2, 40)
        if dati[92] > 0:
            messaggio("Nemico vicino", grigiochi, gsx // 32 * 9, gsy // 18 * 7.2, 40)
            if voceMarcata == 12:
                schermo.blit(scecond[12], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Nemico vicino:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio(u"Esegue l'azione sul nemico più vicino a Colco nel raggio di 2 caselle", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7.2, 40)
        if dati[93] > 0:
            messaggio("Nemico lontano", grigiochi, gsx // 32 * 9, gsy // 18 * 8.2, 40)
            if voceMarcata == 13:
                schermo.blit(scecond[13], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Nemico lontano:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio(u"Esegue l'azione sul nemico lontano (distante di 3 o più caselle) più", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("vicino a Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8.2, 40)
        if dati[94] > 0:
            messaggio("Nemico con pv < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * 9.2, 40)
            if voceMarcata == 14:
                schermo.blit(scecond[14], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Nemico con pv < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su un nemico con pv < 80% (in caso di molteplici bersagli,", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio(u"esegue l'azione su quello più vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15,
                          35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9.2, 40)
        if dati[95] > 0:
            messaggio("Nemico con pv < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * 10.2, 40)
            if voceMarcata == 15:
                schermo.blit(scecond[15], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Nemico con pv < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su un nemico con pv < 50% (in caso di molteplici bersagli,", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio(u"esegue l'azione su quello più vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15,
                          35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10.2, 40)
        if dati[96] > 0:
            messaggio("Nemico con pv < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * 11.2, 40)
            if voceMarcata == 16:
                schermo.blit(scecond[16], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Nemico con pv < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su un nemico con pv < 30% (in caso di molteplici bersagli,", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio(u"esegue l'azione su quello più vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15,
                          35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11.2, 40)
        if dati[97] > 0:
            messaggio("Nemico con meno pv", grigiochi, gsx // 32 * 9, gsy // 18 * 12.2, 40)
            if voceMarcata == 17:
                schermo.blit(scecond[17], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Nemico con meno pv:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione sul nemico con meno pv (in caso di molteplici bersagli,", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio(u"esegue l'azione su quello più vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15,
                          35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12.2, 40)
        if dati[98] > 0:
            messaggio("Numero di nemici > 1", grigiochi, gsx // 32 * 9, gsy // 18 * 13.2, 40)
            if voceMarcata == 18:
                schermo.blit(scecond[18], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Numero di nemici > 1:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio(u"Esegue l'azione quando nei paraggi c'è più di 1 nemico (in caso di", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio(u"tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13.2, 40)
        if dati[99] > 0:
            messaggio("Numero di nemici > 4", grigiochi, gsx // 32 * 9, gsy // 18 * 14.2, 40)
            if voceMarcata == 19:
                schermo.blit(scecond[19], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Numero di nemici > 4:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio(u"Esegue l'azione quando nei paraggi ci sono più di 4 nemici (in caso di", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio(u"tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14.2, 40)
        if dati[100] > 0:
            messaggio("Numero di nemici > 7", grigiochi, gsx // 32 * 9, gsy // 18 * 15.2, 40)
            if voceMarcata == 20:
                schermo.blit(scecond[20], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Numero di nemici > 7:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio(u"Esegue l'azione quando nei paraggi ci sono più di 7 nemici (in caso di", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio(u"tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15.2, 40)

        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)

        # puntatore vecchio
        i = 1
        k = 6.1
        while i <= 10:
            if condizione == i:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * k))
            i = i + 1
            k = k + 1
        i = 11
        k = 6.1
        while i <= 20:
            if condizione == i:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * k))
            i = i + 1
            k = k + 1
        if condizione == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 4.6))

        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        if not canaleSoundCanzone.get_busy():
            canaleSoundCanzone.play(canzone)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 3

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato:
                tastop = event.key
                tastotempfps = 5
                if event.key == pygame.K_q and not tastoTrovato:
                    tastoTrovato = True
                    canaleSoundPuntatore.play(selind)
                    risposta = True

                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True

                if event.key == pygame.K_SPACE and not tastoTrovato:
                    tastoTrovato = True

                    # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)-condizioni(20)-gambit(20) // dimensione: 0-120
                    i = 81
                    c = 1
                    while i <= 100:
                        if voceMarcata == c:
                            if dati[i] != 0:
                                canaleSoundPuntatore.play(selezione)
                                return c
                            else:
                                canaleSoundPuntatore.play(selimp)
                        i += 1
                        c += 1
                    if voceMarcata == 0:
                        canaleSoundPuntatore.play(selezione)
                        return 0
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_SPACE or ((tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 3
            if tastop == pygame.K_w:
                if voceMarcata == 1 or voceMarcata == 11:
                    if voceMarcata == 1:
                        voceMarcata -= 1
                        canaleSoundPuntatore.play(spostapun)
                        yp = yp - gsy // 18 * 1.5
                    else:
                        voceMarcata -= 11
                        canaleSoundPuntatore.play(spostapun)
                        yp = gsy // 18 * 4.6
                    xp = gsx // 32 * 1
                else:
                    if voceMarcata != 0:
                        voceMarcata -= 1
                        canaleSoundPuntatore.play(spostapun)
                        yp = yp - gsy // 18 * 1
                    else:
                        voceMarcata += 10
                        canaleSoundPuntatore.play(spostapun)
                        yp = gsy // 18 * 15.1
            if tastop == pygame.K_a:
                if voceMarcata != 0:
                    if 11 <= voceMarcata <= 20:
                        voceMarcata -= 10
                        canaleSoundPuntatore.play(spostapun)
                        xp = xp - gsx // 32 * 7
                    else:
                        voceMarcata += 10
                        canaleSoundPuntatore.play(spostapun)
                        xp = gsx // 32 * 8
                else:
                    canaleSoundPuntatore.play(selimp)
            if tastop == pygame.K_s:
                if voceMarcata == 0:
                    voceMarcata += 1
                    canaleSoundPuntatore.play(spostapun)
                    yp = yp + gsy // 18 * 1.5
                else:
                    if voceMarcata == 10 or voceMarcata == 20:
                        if voceMarcata == 10:
                            voceMarcata -= 10
                            canaleSoundPuntatore.play(spostapun)
                            yp = gsy // 18 * 4.6
                        else:
                            voceMarcata -= 20
                            canaleSoundPuntatore.play(spostapun)
                            yp = gsy // 18 * 4.6
                        xp = gsx // 32 * 1
                    else:
                        voceMarcata += 1
                        canaleSoundPuntatore.play(spostapun)
                        yp = yp + gsy // 18 * 1
            if tastop == pygame.K_d:
                if voceMarcata != 0:
                    if 1 <= voceMarcata <= 10:
                        voceMarcata += 10
                        canaleSoundPuntatore.play(spostapun)
                        xp = xp + gsx // 32 * 7
                    else:
                        voceMarcata -= 10
                        canaleSoundPuntatore.play(spostapun)
                        xp = gsx // 32 * 1
                else:
                    canaleSoundPuntatore.play(selimp)
            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 15, gsy // 18 * 12.5))

            messaggio("Scegli condizione", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
            messaggio("Cancella", grigiochi, gsx // 32 * 2, gsy // 18 * 4.7, 45)
            if voceMarcata == 0:
                messaggio("Cancella:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Cancella il settaggio di Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            if dati[81] > 0:
                messaggio("Rallo con pv < 80%", grigiochi, gsx // 32 * 2, gsy // 18 * 6.2, 40)
                if voceMarcata == 1:
                    schermo.blit(scecond[1], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Rallo con pv < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Rallo quando ha pv < 80%", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6.2, 40)
            if dati[82] > 0:
                messaggio("Rallo con pv < 50%", grigiochi, gsx // 32 * 2, gsy // 18 * 7.2, 40)
                if voceMarcata == 2:
                    schermo.blit(scecond[2], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Rallo con pv < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Rallo quando ha pv < 50%", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7.2, 40)
            if dati[83] > 0:
                messaggio("Rallo con pv < 30%", grigiochi, gsx // 32 * 2, gsy // 18 * 8.2, 40)
                if voceMarcata == 3:
                    schermo.blit(scecond[3], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Rallo con pv < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Rallo quando ha pv < 30%", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8.2, 40)
            if dati[84] > 0:
                messaggio("Rallo con veleno", grigiochi, gsx // 32 * 2, gsy // 18 * 9.2, 40)
                if voceMarcata == 4:
                    schermo.blit(scecond[4], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Rallo con veleno:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione su Rallo quando è avvelenato", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9.2, 40)
            if dati[85] > 0:
                messaggio("Colco surriscaldato", grigiochi, gsx // 32 * 2, gsy // 18 * 10.2, 40)
                if voceMarcata == 5:
                    schermo.blit(scecond[5], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Colco surriscaldato:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione su Colco quando è surriscaldato", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10.2, 40)
            if dati[86] > 0:
                messaggio("Colco con pe < 80%", grigiochi, gsx // 32 * 2, gsy // 18 * 11.2, 40)
                if voceMarcata == 6:
                    schermo.blit(scecond[6], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Colco con pe < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Colco quando ha pe < 80%", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11.2, 40)
            if dati[87] > 0:
                messaggio("Colco con pe < 50%", grigiochi, gsx // 32 * 2, gsy // 18 * 12.2, 40)
                if voceMarcata == 7:
                    schermo.blit(scecond[7], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Colco con pe < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Colco quando ha pe < 50%", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12.2, 40)
            if dati[88] > 0:
                messaggio("Colco con pe < 30%", grigiochi, gsx // 32 * 2, gsy // 18 * 13.2, 40)
                if voceMarcata == 8:
                    schermo.blit(scecond[8], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Colco con pe < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Colco quando ha pe < 30%", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13.2, 40)
            if dati[89] > 0:
                messaggio("Sempre a Rallo", grigiochi, gsx // 32 * 2, gsy // 18 * 14.2, 40)
                if voceMarcata == 9:
                    schermo.blit(scecond[9], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Sempre a Rallo:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Rallo in continuazione (se la tecnica associata", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("comporta uno status alterativo, viene eseguita solo se lo status non", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio(u"è attivo)", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14.2, 40)
            if dati[90] > 0:
                messaggio("Sempre a Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 15.2, 40)
                if voceMarcata == 10:
                    schermo.blit(scecond[10], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Sempre a Colco:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Colco in continuazione (se la tecnica associata", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("comporta uno status alterativo, viene eseguita solo se lo status non", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio(u"è attivo)", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15.2, 40)
            if dati[91] > 0:
                messaggio("Nemico a caso", grigiochi, gsx // 32 * 9, gsy // 18 * 6.2, 40)
                if voceMarcata == 11:
                    schermo.blit(scecond[11], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Nemico a caso:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su un nemico a caso", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6.2, 40)
            if dati[92] > 0:
                messaggio("Nemico vicino", grigiochi, gsx // 32 * 9, gsy // 18 * 7.2, 40)
                if voceMarcata == 12:
                    schermo.blit(scecond[12], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Nemico vicino:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione sul nemico più vicino a Colco nel raggio di 2 caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7.2, 40)
            if dati[93] > 0:
                messaggio("Nemico lontano", grigiochi, gsx // 32 * 9, gsy // 18 * 8.2, 40)
                if voceMarcata == 13:
                    schermo.blit(scecond[13], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Nemico lontano:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione sul nemico lontano (distante di 3 o più caselle) più", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("vicino a Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8.2, 40)
            if dati[94] > 0:
                messaggio("Nemico con pv < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * 9.2, 40)
                if voceMarcata == 14:
                    schermo.blit(scecond[14], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Nemico con pv < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su un nemico con pv < 80% (in caso di molteplici bersagli,", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio(u"esegue l'azione su quello più vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9.2, 40)
            if dati[95] > 0:
                messaggio("Nemico con pv < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * 10.2, 40)
                if voceMarcata == 15:
                    schermo.blit(scecond[15], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Nemico con pv < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su un nemico con pv < 50% (in caso di molteplici bersagli,", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio(u"esegue l'azione su quello più vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10.2, 40)
            if dati[96] > 0:
                messaggio("Nemico con pv < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * 11.2, 40)
                if voceMarcata == 16:
                    schermo.blit(scecond[16], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Nemico con pv < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su un nemico con pv < 30% (in caso di molteplici bersagli,", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio(u"esegue l'azione su quello più vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11.2, 40)
            if dati[97] > 0:
                messaggio("Nemico con meno pv", grigiochi, gsx // 32 * 9, gsy // 18 * 12.2, 40)
                if voceMarcata == 17:
                    schermo.blit(scecond[17], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Nemico con meno pv:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione sul nemico con meno pv (in caso di molteplici bersagli,", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio(u"esegue l'azione su quello più vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12.2, 40)
            if dati[98] > 0:
                messaggio("Numero di nemici > 1", grigiochi, gsx // 32 * 9, gsy // 18 * 13.2, 40)
                if voceMarcata == 18:
                    schermo.blit(scecond[18], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Numero di nemici > 1:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione quando nei paraggi c'è più di 1 nemico (in caso di", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio(u"tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13.2, 40)
            if dati[99] > 0:
                messaggio("Numero di nemici > 4", grigiochi, gsx // 32 * 9, gsy // 18 * 14.2, 40)
                if voceMarcata == 19:
                    schermo.blit(scecond[19], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Numero di nemici > 4:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione quando nei paraggi ci sono più di 4 nemici (in caso di", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio(u"tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14.2, 40)
            if dati[100] > 0:
                messaggio("Numero di nemici > 7", grigiochi, gsx // 32 * 9, gsy // 18 * 15.2, 40)
                if voceMarcata == 20:
                    schermo.blit(scecond[20], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Numero di nemici > 7:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione quando nei paraggi ci sono più di 7 nemici (in caso di", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio(u"tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15.2, 40)

            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)

            # puntatore vecchio
            i = 1
            k = 6.1
            while i <= 10:
                if condizione == i:
                    schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * k))
                i = i + 1
                k = k + 1
            i = 11
            k = 6.1
            while i <= 20:
                if condizione == i:
                    schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * k))
                i = i + 1
                k = k + 1
            if condizione == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 4.6))

            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        clockMenu.tick(fpsMenu)
    return condizione


def sceglitecn(dati, tecnica, canzone):
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 2, gpy // 2))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 2, gpy // 2))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 4.6
    risposta = False
    voceMarcata = 0

    tastop = 0
    tastotempfps = 5

    # carico le scenette
    scetecn = vetImgTecnicheMenu

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,(posizionex,posizioney,larghezza,altezza,spessore))
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 15, gsy // 18 * 12.5))

        messaggio("Scegli tecnica", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
        messaggio("Cancella", grigiochi, gsx // 32 * 2, gsy // 18 * 4.7, 45)
        if voceMarcata == 0:
            messaggio("Cancella:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
            messaggio("Cancella il settaggio di Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
            messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
            messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        if dati[11] > 0:
            messaggio("Scossa", grigiochi, gsx // 32 * 2, gsy // 18 * 6.2, 40)
            if voceMarcata == 1:
                schermo.blit(scetecn[1], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Scossa:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[0]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("Infligge danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6.2, 40)
        if dati[12] > 0:
            messaggio("Cura", grigiochi, gsx // 32 * 2, gsy // 18 * 7.2, 40)
            if voceMarcata == 2:
                schermo.blit(scetecn[2], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Cura:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[1]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("Recupera un po' di pv di Rallo", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7.2, 40)
        if dati[13] > 0:
            messaggio("Antidoto", grigiochi, gsx // 32 * 2, gsy // 18 * 8.2, 40)
            if voceMarcata == 3:
                schermo.blit(scetecn[3], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Antidoto:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[2]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("Cura avvelenamento a Rallo", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8.2, 40)
        if dati[14] > 0:
            messaggio("Freccia elettrica", grigiochi, gsx // 32 * 2, gsy // 18 * 9.2, 40)
            if voceMarcata == 4:
                schermo.blit(scetecn[4], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Freccia elettrica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[3]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("Infligge danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9.2, 40)
        if dati[15] > 0:
            messaggio("Tempesta elettrica", grigiochi, gsx // 32 * 2, gsy // 18 * 10.2, 40)
            if voceMarcata == 5:
                schermo.blit(scetecn[5], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Tempesta elettrica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[4]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("Infligge danni a tutti i nemici o alleati nel raggio visivo di Colco", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10.2, 40)
        if dati[16] > 0:
            messaggio("Raffreddamento", grigiochi, gsx // 32 * 2, gsy // 18 * 11.2, 40)
            if voceMarcata == 6:
                schermo.blit(scetecn[6], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Raffreddamento:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[5]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("Annulla il surriscaldamento ma richiede due turni (applicata sempre", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("su Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11.2, 40)
        if dati[17] > 0:
            messaggio("Auto-ricarica", grigiochi, gsx // 32 * 2, gsy // 18 * 12.2, 40)
            if voceMarcata == 7:
                schermo.blit(scetecn[7], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Auto-ricarica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[6]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("Ricarica un po' Colco ma richiede due turni e provoca", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14.5, 35)
                messaggio("surriscaldamento (applicata sempre su Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12.2, 40)
        if dati[18] > 0:
            messaggio("Cura +", grigiochi, gsx // 32 * 2, gsy // 18 * 13.2, 40)
            if voceMarcata == 8:
                schermo.blit(scetecn[8], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Cura +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[7]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("recupera molti pv di Rallo", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13.2, 40)
        if dati[19] > 0:
            messaggio("Scossa +", grigiochi, gsx // 32 * 2, gsy // 18 * 14.2, 40)
            if voceMarcata == 9:
                schermo.blit(scetecn[9], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Scossa +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[8]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("Infligge molti danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14.2, 40)
        if dati[20] > 0:
            messaggio("Freccia elettrica +", grigiochi, gsx // 32 * 2, gsy // 18 * 15.2, 40)
            if voceMarcata == 10:
                schermo.blit(scetecn[10], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Freccia elettrica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[9]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("Infligge molti danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5,
                          35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15.2, 40)
        if dati[21] > 0:
            messaggio("Velocizza", grigiochi, gsx // 32 * 9, gsy // 18 * 6.2, 40)
            if voceMarcata == 11:
                schermo.blit(scetecn[11], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Velocizza:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[10]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("Permette a Colco, se non surriscaldato, di eseguire due azioni al turno.", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("Dopo 15 turni provoca surriscaldamento (applicata sempre su Colco)", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6.2, 40)
        if dati[22] > 0:
            messaggio("Carica attacco", grigiochi, gsx // 32 * 9, gsy // 18 * 7.2, 40)
            if voceMarcata == 12:
                schermo.blit(scetecn[12], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Carica attacco:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[11]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("Incrementa l'attacco di Rallo per 10 turni (non ha effetto sui nemici)", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7.2, 40)
        if dati[23] > 0:
            messaggio("Carica difesa", grigiochi, gsx // 32 * 9, gsy // 18 * 8.2, 40)
            if voceMarcata == 13:
                schermo.blit(scetecn[13], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Carica difesa:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[12]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("Incrementa la difesa di Rallo per 10 turni (non ha effetto sui nemici)", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8.2, 40)
        if dati[24] > 0:
            messaggio("Efficienza", grigiochi, gsx // 32 * 9, gsy // 18 * 9.2, 40)
            if voceMarcata == 14:
                schermo.blit(scetecn[14], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Efficienza:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[13]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio(u"Tutte le tecniche costano la metà dei pe per 15 turni. Si annulla con", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("surriscaldamento (applicata sempre su Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9.2, 40)
        if dati[25] > 0:
            messaggio("Tempesta elettrica +", grigiochi, gsx // 32 * 9, gsy // 18 * 10.2, 40)
            if voceMarcata == 15:
                schermo.blit(scetecn[15], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Tempesta elettrica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[14]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("Infligge molti danni a tutti i nemici o alleati nel raggio visivo di Colco", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10.2, 40)
        if dati[26] > 0:
            messaggio("Cura ++", grigiochi, gsx // 32 * 9, gsy // 18 * 11.2, 40)
            if voceMarcata == 16:
                schermo.blit(scetecn[16], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Cura ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[15]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio(u"Recupera un enorme quantità dei pv di Rallo", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5,
                          35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11.2, 40)
        if dati[27] > 0:
            messaggio("Auto-ricarica +", grigiochi, gsx // 32 * 9, gsy // 18 * 12.2, 40)
            if voceMarcata == 17:
                schermo.blit(scetecn[17], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Auto-ricarica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[16]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("Ricarica di molto Colco ma richiede due turni e provoca", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14.5, 35)
                messaggio("surriscaldamento (applicata sempre su Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12.2, 40)
        if dati[28] > 0:
            messaggio("Scossa ++", grigiochi, gsx // 32 * 9, gsy // 18 * 13.2, 40)
            if voceMarcata == 18:
                schermo.blit(scetecn[18], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Scossa ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[17]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("Infligge enormi danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13.2, 40)
        if dati[29] > 0:
            messaggio("Freccia Elettrica ++", grigiochi, gsx // 32 * 9, gsy // 18 * 14.2, 40)
            if voceMarcata == 19:
                schermo.blit(scetecn[19], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Freccia Elettrica ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[18]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("Infligge enormi danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5,
                          35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14.2, 40)
        if dati[30] > 0:
            messaggio("Tempesta elettrica ++", grigiochi, gsx // 32 * 9, gsy // 18 * 15.2, 40)
            if voceMarcata == 20:
                schermo.blit(scetecn[20], (gsx // 32 * 18, gsy // 18 * 4))
                messaggio("Tempesta elettrica ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(costoTecniche[19]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                messaggio("Infligge enormi danni a tutti i nemici o alleati nel raggio visivo di", grigiochi,
                          gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)

        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)

        # puntatore vecchio
        i = 1
        k = 6.1
        while i <= 10:
            if tecnica == i:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * k))
            i = i + 1
            k = k + 1
        i = 11
        k = 6.1
        while i <= 20:
            if tecnica == i:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * k))
            i = i + 1
            k = k + 1
        if tecnica == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 4.6))

        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        if not canaleSoundCanzone.get_busy():
            canaleSoundCanzone.play(canzone)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 3

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato:
                tastop = event.key
                tastotempfps = 5
                if event.key == pygame.K_q and not tastoTrovato:
                    tastoTrovato = True
                    canaleSoundPuntatore.play(selind)
                    risposta = True

                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True

                if event.key == pygame.K_SPACE and not tastoTrovato:
                    tastoTrovato = True

                    i = 11
                    c = 1
                    while i <= 30:
                        if voceMarcata == c:
                            if dati[i] != 0:
                                canaleSoundPuntatore.play(selezione)
                                tecnica = c
                                risposta = True
                            else:
                                canaleSoundPuntatore.play(selimp)
                            break
                        i += 1
                        c += 1
                    if voceMarcata == 0:
                        canaleSoundPuntatore.play(selezione)
                        tecnica = 0
                        risposta = True
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_SPACE or ((tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 3
            if tastop == pygame.K_w:
                if voceMarcata == 1 or voceMarcata == 11:
                    if voceMarcata == 1:
                        voceMarcata -= 1
                        canaleSoundPuntatore.play(spostapun)
                        yp = yp - gsy // 18 * 1.5
                    else:
                        voceMarcata -= 11
                        canaleSoundPuntatore.play(spostapun)
                        yp = yp - gsy // 18 * 1.5
                    xp = gsx // 32 * 1
                else:
                    if voceMarcata == 0:
                        voceMarcata += 10
                        canaleSoundPuntatore.play(spostapun)
                        yp = gsy // 18 * 15.1
                    else:
                        voceMarcata -= 1
                        canaleSoundPuntatore.play(spostapun)
                        yp = yp - gsy // 18 * 1
            if tastop == pygame.K_a:
                if voceMarcata != 0:
                    if 11 <= voceMarcata <= 20:
                        voceMarcata -= 10
                        canaleSoundPuntatore.play(spostapun)
                        xp = xp - gsx // 32 * 7
                    else:
                        voceMarcata += 10
                        canaleSoundPuntatore.play(spostapun)
                        xp = gsx // 32 * 8
                else:
                    canaleSoundPuntatore.play(selimp)
            if tastop == pygame.K_s:
                if voceMarcata == 0:
                    voceMarcata += 1
                    canaleSoundPuntatore.play(spostapun)
                    yp = yp + gsy // 18 * 1.5
                else:
                    if voceMarcata == 10 or voceMarcata == 20:
                        if voceMarcata == 10:
                            voceMarcata -= 10
                            canaleSoundPuntatore.play(spostapun)
                            yp = gsy // 18 * 4.6
                        else:
                            voceMarcata -= 20
                            canaleSoundPuntatore.play(spostapun)
                            yp = gsy // 18 * 4.6
                        xp = gsx // 32 * 1
                    else:
                        voceMarcata += 1
                        canaleSoundPuntatore.play(spostapun)
                        yp = yp + gsy // 18 * 1
            if tastop == pygame.K_d:
                if voceMarcata != 0:
                    if 1 <= voceMarcata <= 10:
                        voceMarcata += 10
                        canaleSoundPuntatore.play(spostapun)
                        xp = xp + gsx // 32 * 7
                    else:
                        voceMarcata -= 10
                        canaleSoundPuntatore.play(spostapun)
                        xp = gsx // 32 * 1
                else:
                    canaleSoundPuntatore.play(selimp)
            schermo.fill(grigioscu)
            # rettangolo(dove,colore,(posizionex,posizioney,larghezza,altezza,spessore))
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 15, gsy // 18 * 12.5))

            messaggio("Scegli tecnica", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
            messaggio("Cancella", grigiochi, gsx // 32 * 2, gsy // 18 * 4.7, 45)
            if voceMarcata == 0:
                messaggio("Cancella:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                messaggio("Cancella il settaggio di Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            if dati[11] > 0:
                messaggio("Scossa", grigiochi, gsx // 32 * 2, gsy // 18 * 6.2, 40)
                if voceMarcata == 1:
                    schermo.blit(scetecn[1], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Scossa:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[0]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("Infligge danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6.2, 40)
            if dati[12] > 0:
                messaggio("Cura", grigiochi, gsx // 32 * 2, gsy // 18 * 7.2, 40)
                if voceMarcata == 2:
                    schermo.blit(scetecn[2], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Cura:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[1]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("Recupera un po' di pv di Rallo", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7.2, 40)
            if dati[13] > 0:
                messaggio("Antidoto", grigiochi, gsx // 32 * 2, gsy // 18 * 8.2, 40)
                if voceMarcata == 3:
                    schermo.blit(scetecn[3], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Antidoto:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[2]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("Cura avvelenamento a Rallo", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8.2, 40)
            if dati[14] > 0:
                messaggio("Freccia elettrica", grigiochi, gsx // 32 * 2, gsy // 18 * 9.2, 40)
                if voceMarcata == 4:
                    schermo.blit(scetecn[4], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Freccia elettrica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[3]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("Infligge danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9.2, 40)
            if dati[15] > 0:
                messaggio("Tempesta elettrica", grigiochi, gsx // 32 * 2, gsy // 18 * 10.2, 40)
                if voceMarcata == 5:
                    schermo.blit(scetecn[5], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Tempesta elettrica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[4]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("Infligge danni a tutti i nemici o alleati nel raggio visivo di Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10.2, 40)
            if dati[16] > 0:
                messaggio("Raffreddamento", grigiochi, gsx // 32 * 2, gsy // 18 * 11.2, 40)
                if voceMarcata == 6:
                    schermo.blit(scetecn[6], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Raffreddamento:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[5]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("Annulla il surriscaldamento ma richiede due turni (applicata sempre", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("su Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11.2, 40)
            if dati[17] > 0:
                messaggio("Auto-ricarica", grigiochi, gsx // 32 * 2, gsy // 18 * 12.2, 40)
                if voceMarcata == 7:
                    schermo.blit(scetecn[7], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Auto-ricarica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[6]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("Ricarica un po' Colco ma richiede due turni e provoca", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("surriscaldamento (applicata sempre su Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12.2, 40)
            if dati[18] > 0:
                messaggio("Cura +", grigiochi, gsx // 32 * 2, gsy // 18 * 13.2, 40)
                if voceMarcata == 8:
                    schermo.blit(scetecn[8], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Cura +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[7]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("recupera molti pv di Rallo", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13.2, 40)
            if dati[19] > 0:
                messaggio("Scossa +", grigiochi, gsx // 32 * 2, gsy // 18 * 14.2, 40)
                if voceMarcata == 9:
                    schermo.blit(scetecn[9], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Scossa +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[8]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("Infligge molti danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14.2, 40)
            if dati[20] > 0:
                messaggio("Freccia elettrica +", grigiochi, gsx // 32 * 2, gsy // 18 * 15.2, 40)
                if voceMarcata == 10:
                    schermo.blit(scetecn[10], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Freccia elettrica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[9]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("Infligge molti danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15.2, 40)
            if dati[21] > 0:
                messaggio("Velocizza", grigiochi, gsx // 32 * 9, gsy // 18 * 6.2, 40)
                if voceMarcata == 11:
                    schermo.blit(scetecn[11], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Velocizza:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[10]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("Permette a Colco, se non surriscaldato, di eseguire due azioni al turno.", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("Dopo 15 turni provoca surriscaldamento (applicata sempre su Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6.2, 40)
            if dati[22] > 0:
                messaggio("Carica attacco", grigiochi, gsx // 32 * 9, gsy // 18 * 7.2, 40)
                if voceMarcata == 12:
                    schermo.blit(scetecn[12], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Carica attacco:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[11]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("Incrementa l'attacco di Rallo per 10 turni (non ha effetto sui nemici)", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7.2, 40)
            if dati[23] > 0:
                messaggio("Carica difesa", grigiochi, gsx // 32 * 9, gsy // 18 * 8.2, 40)
                if voceMarcata == 13:
                    schermo.blit(scetecn[13], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Carica difesa:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[12]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("Incrementa la difesa di Rallo per 10 turni (non ha effetto sui nemici)", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8.2, 40)
            if dati[24] > 0:
                messaggio("Efficienza", grigiochi, gsx // 32 * 9, gsy // 18 * 9.2, 40)
                if voceMarcata == 14:
                    schermo.blit(scetecn[14], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Efficienza:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[13]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio(u"Tutte le tecniche costano la metà dei pe per 15 turni. Si annulla con", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("surriscaldamento (applicata sempre su Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9.2, 40)
            if dati[25] > 0:
                messaggio("Tempesta elettrica +", grigiochi, gsx // 32 * 9, gsy // 18 * 10.2, 40)
                if voceMarcata == 15:
                    schermo.blit(scetecn[15], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Tempesta elettrica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[14]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("Infligge molti danni a tutti i nemici o alleati nel raggio visivo di Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10.2, 40)
            if dati[26] > 0:
                messaggio("Cura ++", grigiochi, gsx // 32 * 9, gsy // 18 * 11.2, 40)
                if voceMarcata == 16:
                    schermo.blit(scetecn[16], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Cura ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[15]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio(u"Recupera un enorme quantità dei pv di Rallo", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11.2, 40)
            if dati[27] > 0:
                messaggio("Auto-ricarica +", grigiochi, gsx // 32 * 9, gsy // 18 * 12.2, 40)
                if voceMarcata == 17:
                    schermo.blit(scetecn[17], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Auto-ricarica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[16]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("Ricarica di molto Colco ma richiede due turni e provoca", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("surriscaldamento (applicata sempre su Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12.2, 40)
            if dati[28] > 0:
                messaggio("Scossa ++", grigiochi, gsx // 32 * 9, gsy // 18 * 13.2, 40)
                if voceMarcata == 18:
                    schermo.blit(scetecn[18], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Scossa ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[17]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("Infligge enormi danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13.2, 40)
            if dati[29] > 0:
                messaggio("Freccia Elettrica ++", grigiochi, gsx // 32 * 9, gsy // 18 * 14.2, 40)
                if voceMarcata == 19:
                    schermo.blit(scetecn[19], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Freccia Elettrica ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[18]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("Infligge enormi danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14.2, 40)
            if dati[30] > 0:
                messaggio("Tempesta elettrica ++", grigiochi, gsx // 32 * 9, gsy // 18 * 15.2, 40)
                if voceMarcata == 20:
                    schermo.blit(scetecn[20], (gsx // 32 * 18, gsy // 18 * 4))
                    messaggio("Tempesta elettrica ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(costoTecniche[19]), grigiochi, gsx // 32 * 27.5, gsy // 18 * 13.8, 45)
                    messaggio("Infligge enormi danni a tutti i nemici o alleati nel raggio visivo di", grigiochi, gsx // 32 * 18, gsy // 18 * 14.5, 35)
                    messaggio("Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 18, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)

            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)

            # puntatore vecchio
            i = 1
            k = 6.1
            while i <= 10:
                if tecnica == i:
                    schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * k))
                i = i + 1
                k = k + 1
            i = 11
            k = 6.1
            while i <= 20:
                if tecnica == i:
                    schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * k))
                i = i + 1
                k = k + 1
            if tecnica == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 4.6))

            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        clockMenu.tick(fpsMenu)
    return tecnica


def equiprobo(dati, canzone):
    robosta = pygame.transform.scale(roboo, (gpx * 5, gpy * 5))
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 2, gpy // 2))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 2, gpy // 2))
    sfondoOggetto = pygame.transform.scale(sfondoOggettoMenu, (int(gpx * 2), int(gpy * 2)))
    sconosciutoEquip = pygame.transform.scale(sconosciutoEquipMenu, (int(gpx * 2), int(gpy * 2)))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 6.8
    risposta = False
    riordinamento = False
    annullaRiordinamento = False
    datiPrimaDiRiordinamento = list(dati)
    vxpGambit = xp
    vypGambit = yp
    voceMarcata = 1
    voceGambitMarcata = 11

    tastop = 0
    tastotempfps = 5

    vetImgBatterie = vetImgBatterieMenu

    vetIcoBatterie = []
    i = 0
    while i < 5:
        if dati[41 + i] > 0:
            vetIcoBatterie.append(vetIcoBatterieMenu[i])
        else:
            vetIcoBatterie.append(sconosciutoEquip)
        i += 1

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione,larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 5, gsy // 18 * 12.5))
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 7, gsy // 18 * 4, gsx // 32 * 16, gsy // 18 * 12.5))

        if annullaRiordinamento:
            dati = list(datiPrimaDiRiordinamento)
            annullaRiordinamento = False
            xp = vxpGambit
            yp = vypGambit
            voceMarcata = voceGambitMarcata

        if riordinamento:
            pygame.draw.rect(schermo, grigiochi, (xp, yp - (gpy // 4), gsx // 32 * 16, gsy // 18 * 1))

        messaggio("Setta Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)

        # equip batteria
        messaggio("Batterie", grigiochi, gsx // 32 * 2, gsy // 18 * 4.5, 60)
        i = 0
        while i < 5:
            schermo.blit(sfondoOggetto, (gsx // 32 * 2.5, (gsy // 18 * 6 + (gpy * 2 * i))))
            schermo.blit(vetIcoBatterie[i], (gsx // 32 * 2.5, (gsy // 18 * 6 + (gpy * 2 * i))))
            i += 1

        # programmazione Colco
        messaggio("Ordine", grigiochi, gsx // 32 * 7.5, gsy // 18 * 4.5, 60)
        i = 1
        while i <= 10:
            if i == 10:
                if riordinamento and voceMarcata == i + 5:
                    messaggio(str(i), grigio, gsx // 32 * 8.3, gsy // 18 * (i + 5), 50)
                else:
                    messaggio(str(i), grigiochi, gsx // 32 * 8.3, gsy // 18 * (i + 5), 50)
            else:
                if riordinamento and voceMarcata == i + 5:
                    messaggio(str(i), grigio, gsx // 32 * 8.5, gsy // 18 * (i + 5), 50)
                else:
                    messaggio(str(i), grigiochi, gsx // 32 * 8.5, gsy // 18 * (i + 5), 50)
            i += 1
        messaggio("Condizione...", grigiochi, gsx // 32 * 11, gsy // 18 * 4.5, 60)
        c = 6.1
        for i in range(101, 111):
            if dati[i] == -1:
                messaggio("---", grigioscu, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 0:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("---", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("---", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 1:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Rallo con pv < 80%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Rallo con pv < 80%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 2:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Rallo con pv < 50%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Rallo con pv < 50%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 3:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Rallo con pv < 30%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Rallo con pv < 30%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 4:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Rallo con veleno", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Rallo con veleno", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 5:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Colco surriscaldato", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Colco surriscaldato", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 6:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Colco con pe < 80%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Colco con pe < 80%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 7:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Colco con pe < 50%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Colco con pe < 50%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 8:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Colco con pe < 30%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Colco con pe < 30%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 9:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Sempre a Rallo", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Sempre a Rallo", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 10:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Sempre a Colco", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Sempre a Colco", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 11:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Nemico a caso", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Nemico a caso", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 12:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Nemico vicino", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Nemico vicino", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 13:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Nemico lontano", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Nemico lontano", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 14:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Nemico con pv < 80%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Nemico con pv < 80%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 15:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Nemico con pv < 50%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Nemico con pv < 50%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 16:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Nemico con pv < 30%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Nemico con pv < 30%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 17:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Nemico con meno pv", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Nemico con meno pv", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 18:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Numero di nemici > 1", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Numero di nemici > 1", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 19:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Numero di nemici > 4", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Numero di nemici > 4", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            if dati[i] == 20:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Numero di nemici > 7", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                else:
                    messaggio("Numero di nemici > 7", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
            c += 1
        messaggio("...Tecnica", grigiochi, gsx // 32 * 17.5, gsy // 18 * 4.5, 60)
        c = 6.1
        for i in range(111, 121):
            if dati[i] == -1:
                messaggio("---", grigioscu, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 0:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("---", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("---", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 1:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Scossa", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Scossa", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 2:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Cura", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Cura", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 3:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Antidoto", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Antidoto", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 4:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Freccia elettrica", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Freccia elettrica", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 5:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Tempesta elettrica", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Tempesta elettrica", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 6:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Raffreddamento", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Raffreddamento", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 7:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Auto-ricarica", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Auto-ricarica", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 8:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Cura +", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Cura +", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 9:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Scossa +", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Scossa +", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 10:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Freccia elettrica +", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Freccia elettrica +", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 11:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Velocizza", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Velocizza", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 12:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Carica attacco", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Carica attacco", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 13:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Carica difesa", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Carica difesa", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 14:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Efficienza", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Efficienza", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 15:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Tempesta elettrica +", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Tempesta elettrica +", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 16:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Cura ++", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Cura ++", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 17:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Auto-ricarica +", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Auto-ricarica +", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 18:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Scossa ++", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Scossa ++", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 19:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Freccia Elettrica ++", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Freccia Elettrica ++", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            if dati[i] == 20:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Tempesta elettrica ++", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                else:
                    messaggio("Tempesta elettrica ++", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
            c = c + 1

        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)

        esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

        schermo.blit(robosta, (gsx // 32 * 25, gsy // 18 * 10))
        schermo.blit(vetImgBatterie[dati[9]], (gsx // 32 * 25, gsy // 18 * 10))
        messaggio("Statistiche:", grigiochi, gsx // 32 * 24, gsy // 18 * 7.7, 50)
        messaggio("Pe totali: %i" % entot, grigiochi, gsx // 32 * 24, gsy // 18 * 8.5, 35)
        messaggio("Difesa: %i" % difro, grigiochi, gsx // 32 * 24, gsy // 18 * 9, 35)

        # mostrare descrizione batterie / priorità / condizioni / azioni
        if voceMarcata == 1:
            if dati[71] != 0:
                messaggio("Batteria piccola:", grigiochi, gsx // 32 * 24, gsy // 18 * 4.8, 60)
                messaggio("Batteria che contiene poca alimentazione", grigiochi, gsx // 32 * 24, gsy // 18 * 5.8, 35)
                messaggio("", grigiochi, gsx // 32 * 24, gsy // 18 * 6.3, 35)
                messaggio("", grigiochi, gsx // 32 * 24, gsy // 18 * 6.8, 35)
                diff = (0 * 0 * 80) - (dati[9] * dati[9] * 80)
                if dati[9] > 0:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                diff = 0 - (dati[9] * dati[9] * 30)
                if dati[9] > 0:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
        if voceMarcata == 2:
            if dati[72] != 0:
                messaggio("Batteria discreta:", grigiochi, gsx // 32 * 24, gsy // 18 * 4.8, 60)
                messaggio("Batteria con una buona capienza e", grigiochi, gsx // 32 * 24, gsy // 18 * 5.8, 35)
                messaggio("ottimizzazione del sistema difensivo", grigiochi, gsx // 32 * 24, gsy // 18 * 6.3, 35)
                messaggio("", grigiochi, gsx // 32 * 24, gsy // 18 * 6.8, 35)
                diff = (1 * 1 * 80) - (dati[9] * dati[9] * 80)
                if dati[9] > 1:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                elif dati[9] < 1:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                diff = 30 - (dati[9] * dati[9] * 30)
                if dati[9] > 1:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                elif dati[9] < 1:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
        if voceMarcata == 3:
            if dati[73] != 0:
                messaggio("Batteria capiente:", grigiochi, gsx // 32 * 24, gsy // 18 * 4.8, 60)
                messaggio(u"Batteria con una grande capacità e un", grigiochi, gsx // 32 * 24, gsy // 18 * 5.8, 35)
                messaggio("ottimo sistema difensivo", grigiochi, gsx // 32 * 24, gsy // 18 * 6.3, 35)
                messaggio("", grigiochi, gsx // 32 * 24, gsy // 18 * 6.8, 35)
                diff = (2 * 2 * 80) - (dati[9] * dati[9] * 80)
                if dati[9] > 2:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                elif dati[9] < 2:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                diff = 120 - (dati[9] * dati[9] * 30)
                if dati[9] > 2:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                elif dati[9] < 2:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
        if voceMarcata == 4:
            if dati[74] != 0:
                messaggio("Batteria enorme:", grigiochi, gsx // 32 * 24, gsy // 18 * 4.8, 60)
                messaggio("Grande batteria che permette a Colco di", grigiochi, gsx // 32 * 24, gsy // 18 * 5.8, 35)
                messaggio(u"utilizzare le tecniche più dispendiose", grigiochi, gsx // 32 * 24, gsy // 18 * 6.3, 35)
                messaggio("", grigiochi, gsx // 32 * 24, gsy // 18 * 6.8, 35)
                diff = (3 * 3 * 80) - (dati[9] * dati[9] * 80)
                if dati[9] > 3:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                elif dati[9] < 3:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                diff = 270 - (dati[9] * dati[9] * 30)
                if dati[9] > 3:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                elif dati[9] < 3:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
        if voceMarcata == 5:
            if dati[75] != 0:
                messaggio("Batteria illimitata:", grigiochi, gsx // 32 * 24, gsy // 18 * 4.8, 60)
                messaggio("Batteria incredibilmente capiente.", grigiochi, gsx // 32 * 24, gsy // 18 * 5.8, 35)
                messaggio("Permette un eccellente ottimizzazione", grigiochi, gsx // 32 * 24, gsy // 18 * 6.3, 35)
                messaggio("del sistema difensivo", grigiochi, gsx // 32 * 24, gsy // 18 * 6.8, 35)
                diff = (4 * 4 * 80) - (dati[9] * dati[9] * 80)
                if dati[9] > 4:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                elif dati[9] < 4:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                diff = 480 - (dati[9] * dati[9] * 30)
                if dati[9] > 4:
                    messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                elif dati[9] < 4:
                    messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)

        if 6 <= voceMarcata <= 15:
            messaggio(u"Ordine:", grigiochi, gsx // 32 * 24, gsy // 18 * 4.8, 60)
            messaggio(u"Determina il livello di priorità dell'evento.", grigiochi, gsx // 32 * 24, gsy // 18 * 5.8, 35)
            messaggio(u"Colco eseguirà la prima tecnica della lista", grigiochi, gsx // 32 * 24, gsy // 18 * 6.3, 35)
            messaggio(u"la cui condizione si è verificata", grigiochi, gsx // 32 * 24, gsy // 18 * 6.8, 35)

        if 16 <= voceMarcata <= 25:
            messaggio("Condizione:", grigiochi, gsx // 32 * 24, gsy // 18 * 4.8, 60)
            messaggio("Indica la situazione che si deve verificare", grigiochi, gsx // 32 * 24, gsy // 18 * 5.8, 35)
            messaggio(u"affinchè Colco esegua la tecnica associata", grigiochi, gsx // 32 * 24, gsy // 18 * 6.3, 35)
            messaggio("", grigiochi, gsx // 32 * 24, gsy // 18 * 6.8, 35)

        if 26 <= voceMarcata <= 35:
            messaggio("Tecnica:", grigiochi, gsx // 32 * 24, gsy // 18 * 4.8, 60)
            messaggio(u"La tecnica che Colco eseguirà quando si", grigiochi, gsx // 32 * 24, gsy // 18 * 5.8, 35)
            messaggio("verifica la condizione associata", grigiochi, gsx // 32 * 24, gsy // 18 * 6.3, 35)
            messaggio("", grigiochi, gsx // 32 * 24, gsy // 18 * 6.8, 35)

        # puntatore vecchio batterie/riordinamento gambit
        if dati[9] == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 6.8))
        if dati[9] == 1:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 8.8))
        if dati[9] == 2:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 10.8))
        if dati[9] == 3:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 12.8))
        if dati[9] == 4:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 14.8))
        if riordinamento:
            schermo.blit(puntatorevecchio, (vxpGambit, vypGambit))

        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        if not canaleSoundCanzone.get_busy():
            canaleSoundCanzone.play(canzone)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 3

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato:
                tastop = event.key
                tastotempfps = 5
                if event.key == pygame.K_q and not tastoTrovato:
                    tastoTrovato = True
                    canaleSoundPuntatore.play(selind)
                    if not riordinamento:
                        risposta = True
                    else:
                        riordinamento = False
                        annullaRiordinamento = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and not riordinamento and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and not riordinamento and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_SPACE:
                    tastoTrovato = True
                    # riordina
                    if riordinamento:
                        canaleSoundPuntatore.play(selezione)
                        riordinamento = False
                    else:
                        # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                        # armrob
                        if voceMarcata == 1:
                            if dati[71] != 0:
                                canaleSoundPuntatore.play(selezione)
                                dati[9] = 0
                                esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                                if dati[10] > entot:
                                    dati[10] = entot
                            else:
                                canaleSoundPuntatore.play(selimp)
                        if voceMarcata == 2:
                            if dati[72] != 0:
                                canaleSoundPuntatore.play(selezione)
                                dati[9] = 1
                                esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                                if dati[10] > entot:
                                    dati[10] = entot
                            else:
                                canaleSoundPuntatore.play(selimp)
                        if voceMarcata == 3:
                            if dati[73] != 0:
                                canaleSoundPuntatore.play(selezione)
                                dati[9] = 2
                                esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                                if dati[10] > entot:
                                    dati[10] = entot
                            else:
                                canaleSoundPuntatore.play(selimp)
                        if voceMarcata == 4:
                            if dati[74] != 0:
                                canaleSoundPuntatore.play(selezione)
                                dati[9] = 3
                                esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                                if dati[10] > entot:
                                    dati[10] = entot
                            else:
                                canaleSoundPuntatore.play(selimp)
                        if voceMarcata == 5:
                            if dati[75] != 0:
                                canaleSoundPuntatore.play(selezione)
                                dati[9] = 4
                                esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                                if dati[10] > entot:
                                    dati[10] = entot
                            else:
                                canaleSoundPuntatore.play(selimp)

                        # riordina
                        if 6 <= voceMarcata <= 15:
                            canaleSoundPuntatore.play(selezione)
                            riordinamento = True
                            datiPrimaDiRiordinamento = list(dati)
                            vxpGambit = xp
                            vypGambit = yp
                            voceGambitMarcata = voceMarcata

                        # condizioni
                        i = 101
                        c = 16
                        while i <= 110:
                            if voceMarcata == c:
                                if dati[i] != -1:
                                    canaleSoundPuntatore.play(selezione)
                                    dati[i] = sceglicondiz(dati, dati[i], canzone)
                                else:
                                    canaleSoundPuntatore.play(selimp)
                            i += 1
                            c += 1

                        # tecniche
                        i = 111
                        c = 26
                        while i <= 120:
                            if voceMarcata == c:
                                if dati[i] != -1:
                                    canaleSoundPuntatore.play(selezione)
                                    dati[i] = sceglitecn(dati, dati[i], canzone)
                                else:
                                    canaleSoundPuntatore.play(selimp)
                            i += 1
                            c += 1
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_q or tastop == pygame.K_SPACE or ((tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 3
            if tastop == pygame.K_w:
                if riordinamento:
                    if voceMarcata != 6:
                        canaleSoundPuntatore.play(spostapun)
                        i = 0
                        while i < 10:
                            if voceMarcata == i + 6:
                                condizioneSelezionata = dati[101 + i]
                                dati[101 + i] = dati[101 + i - 1]
                                dati[101 + i - 1] = condizioneSelezionata
                                azioneSelezionata = dati[111 + i]
                                dati[111 + i] = dati[111 + i - 1]
                                dati[111 + i - 1] = azioneSelezionata
                                break
                            i += 1
                        voceMarcata -= 1
                        yp = yp - gsy // 18 * 1
                    else:
                        canaleSoundPuntatore.play(selimp)
                else:
                    if 1 <= voceMarcata <= 5:
                        if voceMarcata == 1:
                            voceMarcata += 4
                            canaleSoundPuntatore.play(spostapun)
                            yp = gsy // 18 * 14.8
                        else:
                            voceMarcata -= 1
                            canaleSoundPuntatore.play(spostapun)
                            yp = yp - gsy // 18 * 2
                    else:
                        if voceMarcata == 6 or voceMarcata == 16 or voceMarcata == 26:
                            voceMarcata += 9
                            canaleSoundPuntatore.play(spostapun)
                            yp = gsy // 18 * 15
                        else:
                            voceMarcata -= 1
                            canaleSoundPuntatore.play(spostapun)
                            yp = yp - gsy // 18 * 1
            if tastop == pygame.K_a and not riordinamento:
                if 1 <= voceMarcata <= 5:
                    canaleSoundPuntatore.play(spostapun)
                    if voceMarcata == 1:
                        voceMarcata += 26
                        yp = gsy // 18 * 7
                    elif voceMarcata == 2:
                        voceMarcata += 27
                        yp = gsy // 18 * 9
                    elif voceMarcata == 3:
                        voceMarcata += 28
                        yp = gsy // 18 * 11
                    elif voceMarcata == 4:
                        voceMarcata += 29
                        yp = gsy // 18 * 13
                    elif voceMarcata == 5:
                        voceMarcata += 30
                        yp = gsy // 18 * 15
                    xp = gsx // 32 * 16.5
                elif 6 <= voceMarcata <= 15:
                    canaleSoundPuntatore.play(spostapun)
                    if 6 <= voceMarcata <= 7:
                        if voceMarcata == 6:
                            voceMarcata -= 5
                        elif voceMarcata == 7:
                            voceMarcata -= 6
                        yp = gsy // 18 * 6.8
                    elif 8 <= voceMarcata <= 9:
                        if voceMarcata == 8:
                            voceMarcata -= 6
                        elif voceMarcata == 9:
                            voceMarcata -= 7
                        yp = gsy // 18 * 8.8
                    elif 10 <= voceMarcata <= 11:
                        if voceMarcata == 10:
                            voceMarcata -= 7
                        elif voceMarcata == 11:
                            voceMarcata -= 8
                        yp = gsy // 18 * 10.8
                    elif 12 <= voceMarcata <= 13:
                        if voceMarcata == 12:
                            voceMarcata -= 8
                        elif voceMarcata == 13:
                            voceMarcata -= 9
                        yp = gsy // 18 * 12.8
                    elif 14 <= voceMarcata <= 15:
                        if voceMarcata == 14:
                            voceMarcata -= 9
                        elif voceMarcata == 15:
                            voceMarcata -= 10
                        yp = gsy // 18 * 14.8
                    xp = gsx // 32 * 1
                elif 16 <= voceMarcata <= 25:
                    voceMarcata -= 10
                    canaleSoundPuntatore.play(spostapun)
                    xp = gsx // 32 * 7
                elif 26 <= voceMarcata <= 35:
                    voceMarcata -= 10
                    canaleSoundPuntatore.play(spostapun)
                    xp = gsx // 32 * 10
            if tastop == pygame.K_s:
                if riordinamento:
                    if voceMarcata != 15:
                        canaleSoundPuntatore.play(spostapun)
                        i = 0
                        while i < 10:
                            if voceMarcata == i + 6:
                                condizioneSelezionata = dati[101 + i]
                                dati[101 + i] = dati[101 + i + 1]
                                dati[101 + i + 1] = condizioneSelezionata
                                azioneSelezionata = dati[111 + i]
                                dati[111 + i] = dati[111 + i + 1]
                                dati[111 + i + 1] = azioneSelezionata
                                break
                            i += 1
                        voceMarcata += 1
                        yp = yp + gsy // 18 * 1
                    else:
                        canaleSoundPuntatore.play(selimp)
                else:
                    if 1 <= voceMarcata <= 5:
                        if voceMarcata == 5:
                            voceMarcata -= 4
                            canaleSoundPuntatore.play(spostapun)
                            yp = gsy // 18 * 6.8
                        else:
                            voceMarcata += 1
                            canaleSoundPuntatore.play(spostapun)
                            yp = yp + gsy // 18 * 2
                    else:
                        if voceMarcata == 15 or voceMarcata == 25 or voceMarcata == 35:
                            voceMarcata -= 9
                            canaleSoundPuntatore.play(spostapun)
                            yp = gsy // 18 * 6
                        else:
                            voceMarcata += 1
                            canaleSoundPuntatore.play(spostapun)
                            yp = yp + gsy // 18 * 1
            if tastop == pygame.K_d and not riordinamento:
                if 1 <= voceMarcata <= 5:
                    canaleSoundPuntatore.play(spostapun)
                    if voceMarcata == 1:
                        voceMarcata += 6
                        yp = gsy // 18 * 7
                    elif voceMarcata == 2:
                        voceMarcata += 7
                        yp = gsy // 18 * 9
                    elif voceMarcata == 3:
                        voceMarcata += 8
                        yp = gsy // 18 * 11
                    elif voceMarcata == 4:
                        voceMarcata += 9
                        yp = gsy // 18 * 13
                    elif voceMarcata == 5:
                        voceMarcata += 10
                        yp = gsy // 18 * 15
                    xp = gsx // 32 * 7
                elif 6 <= voceMarcata <= 15:
                    voceMarcata += 10
                    canaleSoundPuntatore.play(spostapun)
                    xp = gsx // 32 * 10
                elif 16 <= voceMarcata <= 25:
                    voceMarcata += 10
                    canaleSoundPuntatore.play(spostapun)
                    xp = gsx // 32 * 16.5
                elif 26 <= voceMarcata <= 35:
                    canaleSoundPuntatore.play(spostapun)
                    if 26 <= voceMarcata <= 27:
                        if voceMarcata == 26:
                            voceMarcata -= 25
                        elif voceMarcata == 27:
                            voceMarcata -= 26
                        yp = gsy // 18 * 6.8
                    elif 28 <= voceMarcata <= 29:
                        if voceMarcata == 28:
                            voceMarcata -= 26
                        elif voceMarcata == 29:
                            voceMarcata -= 27
                        yp = gsy // 18 * 8.8
                    elif 30 <= voceMarcata <= 31:
                        if voceMarcata == 30:
                            voceMarcata -= 27
                        elif voceMarcata == 31:
                            voceMarcata -= 28
                        yp = gsy // 18 * 10.8
                    elif 32 <= voceMarcata <= 33:
                        if voceMarcata == 32:
                            voceMarcata -= 28
                        elif voceMarcata == 33:
                            voceMarcata -= 29
                        yp = gsy // 18 * 12.8
                    elif 34 <= voceMarcata <= 35:
                        if voceMarcata == 34:
                            voceMarcata -= 29
                        elif voceMarcata == 35:
                            voceMarcata -= 30
                        yp = gsy // 18 * 14.8
                    xp = gsx // 32 * 1
            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione,larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 5, gsy // 18 * 12.5))
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 7, gsy // 18 * 4, gsx // 32 * 16, gsy // 18 * 12.5))

            if annullaRiordinamento:
                dati = list(datiPrimaDiRiordinamento)
                annullaRiordinamento = False
                xp = vxpGambit
                yp = vypGambit
                voceMarcata = voceGambitMarcata

            if riordinamento:
                pygame.draw.rect(schermo, grigiochi, (xp, yp - (gpy // 4), gsx // 32 * 16, gsy // 18 * 1))

            messaggio("Setta Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)

            # equip batteria
            messaggio("Batterie", grigiochi, gsx // 32 * 2, gsy // 18 * 4.5, 60)
            i = 0
            while i < 5:
                schermo.blit(sfondoOggetto, (gsx // 32 * 2.5, (gsy // 18 * 6 + (gpy * 2 * i))))
                schermo.blit(vetIcoBatterie[i], (gsx // 32 * 2.5, (gsy // 18 * 6 + (gpy * 2 * i))))
                i += 1

            # programmazione Colco
            messaggio("Ordine", grigiochi, gsx // 32 * 7.5, gsy // 18 * 4.5, 60)
            i = 1
            while i <= 10:
                if i == 10:
                    if riordinamento and voceMarcata == i + 5:
                        messaggio(str(i), grigio, gsx // 32 * 8.3, gsy // 18 * (i + 5), 50)
                    else:
                        messaggio(str(i), grigiochi, gsx // 32 * 8.3, gsy // 18 * (i + 5), 50)
                else:
                    if riordinamento and voceMarcata == i + 5:
                        messaggio(str(i), grigio, gsx // 32 * 8.5, gsy // 18 * (i + 5), 50)
                    else:
                        messaggio(str(i), grigiochi, gsx // 32 * 8.5, gsy // 18 * (i + 5), 50)
                i += 1
            messaggio("Condizione...", grigiochi, gsx // 32 * 11, gsy // 18 * 4.5, 60)
            c = 6.1
            for i in range(101, 111):
                if dati[i] == -1:
                    messaggio("---", grigioscu, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 0:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("---", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("---", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 1:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Rallo con pv < 80%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Rallo con pv < 80%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 2:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Rallo con pv < 50%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Rallo con pv < 50%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 3:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Rallo con pv < 30%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Rallo con pv < 30%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 4:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Rallo con veleno", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Rallo con veleno", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 5:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Colco surriscaldato", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Colco surriscaldato", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 6:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Colco con pe < 80%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Colco con pe < 80%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 7:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Colco con pe < 50%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Colco con pe < 50%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 8:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Colco con pe < 30%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Colco con pe < 30%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 9:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Sempre a Rallo", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Sempre a Rallo", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 10:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Sempre a Colco", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Sempre a Colco", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 11:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Nemico a caso", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Nemico a caso", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 12:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Nemico vicino", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Nemico vicino", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 13:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Nemico lontano", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Nemico lontano", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 14:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Nemico con pv < 80%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Nemico con pv < 80%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 15:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Nemico con pv < 50%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Nemico con pv < 50%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 16:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Nemico con pv < 30%", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Nemico con pv < 30%", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 17:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Nemico con meno pv", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Nemico con meno pv", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 18:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Numero di nemici > 1", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Numero di nemici > 1", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 19:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Numero di nemici > 4", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Numero di nemici > 4", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                if dati[i] == 20:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Numero di nemici > 7", grigio, gsx // 32 * 11, gsy // 18 * c, 40)
                    else:
                        messaggio("Numero di nemici > 7", grigiochi, gsx // 32 * 11, gsy // 18 * c, 40)
                c += 1
            messaggio("...Tecnica", grigiochi, gsx // 32 * 17.5, gsy // 18 * 4.5, 60)
            c = 6.1
            for i in range(111, 121):
                if dati[i] == -1:
                    messaggio("---", grigioscu, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 0:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("---", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("---", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 1:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Scossa", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Scossa", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 2:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Cura", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Cura", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 3:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Antidoto", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Antidoto", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 4:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Freccia elettrica", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Freccia elettrica", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 5:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Tempesta elettrica", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Tempesta elettrica", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 6:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Raffreddamento", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Raffreddamento", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 7:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Auto-ricarica", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Auto-ricarica", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 8:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Cura +", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Cura +", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 9:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Scossa +", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Scossa +", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 10:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Freccia elettrica +", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Freccia elettrica +", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 11:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Velocizza", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Velocizza", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 12:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Carica attacco", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Carica attacco", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 13:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Carica difesa", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Carica difesa", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 14:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Efficienza", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Efficienza", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 15:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Tempesta elettrica +", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Tempesta elettrica +", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 16:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Cura ++", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Cura ++", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 17:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Auto-ricarica +", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Auto-ricarica +", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 18:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Scossa ++", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Scossa ++", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 19:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Freccia Elettrica ++", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Freccia Elettrica ++", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                if dati[i] == 20:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Tempesta elettrica ++", grigio, gsx // 32 * 17.5, gsy // 18 * c, 40)
                    else:
                        messaggio("Tempesta elettrica ++", grigiochi, gsx // 32 * 17.5, gsy // 18 * c, 40)
                c = c + 1

            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)

            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

            schermo.blit(robosta, (gsx // 32 * 25, gsy // 18 * 10))
            schermo.blit(vetImgBatterie[dati[9]], (gsx // 32 * 25, gsy // 18 * 10))
            messaggio("Statistiche:", grigiochi, gsx // 32 * 24, gsy // 18 * 7.7, 50)
            messaggio("Pe totali: %i" % entot, grigiochi, gsx // 32 * 24, gsy // 18 * 8.5, 35)
            messaggio("Difesa: %i" % difro, grigiochi, gsx // 32 * 24, gsy // 18 * 9, 35)

            # mostrare descrizione batterie / priorità / condizioni / azioni
            if voceMarcata == 1:
                if dati[71] != 0:
                    messaggio("Batteria piccola:", grigiochi, gsx // 32 * 24, gsy // 18 * 4.8, 60)
                    messaggio("Batteria che contiene poca alimentazione", grigiochi, gsx // 32 * 24, gsy // 18 * 5.8, 35)
                    messaggio("", grigiochi, gsx // 32 * 24, gsy // 18 * 6.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 24, gsy // 18 * 6.8, 35)
                    diff = (0 * 0 * 80) - (dati[9] * dati[9] * 80)
                    if dati[9] > 0:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                    diff = 0 - (dati[9] * dati[9] * 30)
                    if dati[9] > 0:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
            if voceMarcata == 2:
                if dati[72] != 0:
                    messaggio("Batteria discreta:", grigiochi, gsx // 32 * 24, gsy // 18 * 4.8, 60)
                    messaggio("Batteria con una buona capienza e", grigiochi, gsx // 32 * 24, gsy // 18 * 5.8, 35)
                    messaggio("ottimizzazione del sistema difensivo", grigiochi, gsx // 32 * 24, gsy // 18 * 6.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 24, gsy // 18 * 6.8, 35)
                    diff = (1 * 1 * 80) - (dati[9] * dati[9] * 80)
                    if dati[9] > 1:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                    elif dati[9] < 1:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                    diff = 30 - (dati[9] * dati[9] * 30)
                    if dati[9] > 1:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                    elif dati[9] < 1:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
            if voceMarcata == 3:
                if dati[73] != 0:
                    messaggio("Batteria capiente:", grigiochi, gsx // 32 * 24, gsy // 18 * 4.8, 60)
                    messaggio(u"Batteria con una grande capacità e un", grigiochi, gsx // 32 * 24, gsy // 18 * 5.8, 35)
                    messaggio("ottimo sistema difensivo", grigiochi, gsx // 32 * 24, gsy // 18 * 6.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 24, gsy // 18 * 6.8, 35)
                    diff = (2 * 2 * 80) - (dati[9] * dati[9] * 80)
                    if dati[9] > 2:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                    elif dati[9] < 2:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                    diff = 120 - (dati[9] * dati[9] * 30)
                    if dati[9] > 2:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                    elif dati[9] < 2:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
            if voceMarcata == 4:
                if dati[74] != 0:
                    messaggio("Batteria enorme:", grigiochi, gsx // 32 * 24, gsy // 18 * 4.8, 60)
                    messaggio("Grande batteria che permette a Colco di", grigiochi, gsx // 32 * 24, gsy // 18 * 5.8, 35)
                    messaggio(u"utilizzare le tecniche più dispendiose", grigiochi, gsx // 32 * 24, gsy // 18 * 6.3, 35)
                    messaggio("", grigiochi, gsx // 32 * 24, gsy // 18 * 6.8, 35)
                    diff = (3 * 3 * 80) - (dati[9] * dati[9] * 80)
                    if dati[9] > 3:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                    elif dati[9] < 3:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                    diff = 270 - (dati[9] * dati[9] * 30)
                    if dati[9] > 3:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                    elif dati[9] < 3:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)
            if voceMarcata == 5:
                if dati[75] != 0:
                    messaggio("Batteria illimitata:", grigiochi, gsx // 32 * 24, gsy // 18 * 4.8, 60)
                    messaggio("Batteria incredibilmente capiente.", grigiochi, gsx // 32 * 24, gsy // 18 * 5.8, 35)
                    messaggio("Permette un eccellente ottimizzazione", grigiochi, gsx // 32 * 24, gsy // 18 * 6.3, 35)
                    messaggio("del sistema difensivo", grigiochi, gsx // 32 * 24, gsy // 18 * 6.8, 35)
                    diff = (4 * 4 * 80) - (dati[9] * dati[9] * 80)
                    if dati[9] > 4:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                    elif dati[9] < 4:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 8.5, 35)
                    diff = 480 - (dati[9] * dati[9] * 30)
                    if dati[9] > 4:
                        messaggio(str(diff), rosso, gsx // 32 * 28, gsy // 18 * 9, 35)
                    elif dati[9] < 4:
                        messaggio("+" + str(diff), verde, gsx // 32 * 28, gsy // 18 * 9, 35)

            if 6 <= voceMarcata <= 15:
                messaggio(u"Ordine:", grigiochi, gsx // 32 * 24, gsy // 18 * 4.8, 60)
                messaggio(u"Determina il livello di priorità dell'evento.", grigiochi, gsx // 32 * 24, gsy // 18 * 5.8, 35)
                messaggio(u"Colco eseguirà la prima tecnica della lista", grigiochi, gsx // 32 * 24, gsy // 18 * 6.3, 35)
                messaggio(u"la cui condizione si è verificata", grigiochi, gsx // 32 * 24, gsy // 18 * 6.8, 35)

            if 16 <= voceMarcata <= 25:
                messaggio("Condizione:", grigiochi, gsx // 32 * 24, gsy // 18 * 4.8, 60)
                messaggio("Indica la situazione che si deve verificare", grigiochi, gsx // 32 * 24, gsy // 18 * 5.8, 35)
                messaggio(u"affinchè Colco esegua la tecnica associata", grigiochi, gsx // 32 * 24, gsy // 18 * 6.3, 35)
                messaggio("", grigiochi, gsx // 32 * 24, gsy // 18 * 6.8, 35)

            if 26 <= voceMarcata <= 35:
                messaggio("Tecnica:", grigiochi, gsx // 32 * 24, gsy // 18 * 4.8, 60)
                messaggio(u"La tecnica che Colco eseguirà quando si", grigiochi, gsx // 32 * 24, gsy // 18 * 5.8, 35)
                messaggio("verifica la condizione associata", grigiochi, gsx // 32 * 24, gsy // 18 * 6.3, 35)
                messaggio("", grigiochi, gsx // 32 * 24, gsy // 18 * 6.8, 35)

            # puntatore vecchio batterie/riordinamento gambit
            if dati[9] == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 6.8))
            if dati[9] == 1:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 8.8))
            if dati[9] == 2:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 10.8))
            if dati[9] == 3:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 12.8))
            if dati[9] == 4:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 14.8))
            if riordinamento:
                schermo.blit(puntatorevecchio, (vxpGambit, vypGambit))

            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        clockMenu.tick(fpsMenu)
    return dati


def oggetti(dati, canzone):
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 2, gpy // 2))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 2, gpy // 2))
    sfondostastart = pygame.transform.scale(sfondostax3, (gpx * 4, gpy))
    sconosciutoOggetto = pygame.transform.scale(sconosciutoOggettoMenu, (gpx * 10, gpy * 10))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 5
    xpv = xp
    ypv = yp
    usauno = False
    usa = 0
    risposta = False
    attacco = 0
    oggetton = 1
    voceMarcata = 0

    tastop = 0
    tastotempfps = 5

    imgOggetti = []
    i = 1
    while i <= 10:
        if dati[i + 30] >= 0:
            imgOggetti.append(vetImgOggettiMenu[i - 1])
        else:
            imgOggetti.append(sconosciutoOggetto)
        i += 1

    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 10, gsy // 18 * 12.5))

        # pozione, carica batt, bomba, antidoto, bomba veleno, esca, super poz, carica migliorato, bomba pot, bomba atomica
        messaggio("Oggetti", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
        if dati[31] >= 0:
            messaggio("Pozione", grigiochi, gsx // 32 * 2, gsy // 18 * 5, 45)
            messaggio("x %i" % dati[31], grigiochi, gsx // 32 * 9.3, gsy // 18 * 5, 45)
            if oggetton == 1:
                messaggio("Pozione:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                messaggio("Recupera 100 pv di Rallo", grigiochi, gsx // 32 * 20, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 5, 45)
        if dati[32] >= 0:
            messaggio("Caricabatterie", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 45)
            messaggio("x %i" % dati[32], grigiochi, gsx // 32 * 9.3, gsy // 18 * 6, 45)
            if oggetton == 2:
                messaggio("Caricabatterie:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                messaggio("Recupera 250 pe di Colco", grigiochi, gsx // 32 * 20, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 45)
        if dati[33] >= 0:
            messaggio("Medicina", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 45)
            messaggio("x %i" % dati[33], grigiochi, gsx // 32 * 9.3, gsy // 18 * 7, 45)
            if oggetton == 3:
                messaggio("Medicina:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                messaggio("Cura avvelenamento a Rallo", grigiochi, gsx // 32 * 20, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 45)
        if dati[34] >= 0:
            messaggio("Super pozione", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 45)
            messaggio("x %i" % dati[34], grigiochi, gsx // 32 * 9.3, gsy // 18 * 8, 45)
            if oggetton == 4:
                messaggio("Super pozione:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                messaggio("Recupera 300 pv di Rallo", grigiochi, gsx // 32 * 20, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 45)
        if dati[35] >= 0:
            messaggio("Caricabatterie migliorato", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 45)
            messaggio("x %i" % dati[35], grigiochi, gsx // 32 * 9.3, gsy // 18 * 9, 45)
            if oggetton == 5:
                messaggio("Caricabatterie migliorato:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                messaggio("Recupera 600 pe di Colco", grigiochi, gsx // 32 * 20, gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 45)
        if dati[36] >= 0:
            messaggio("Bomba", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 45)
            messaggio("x %i" % dati[36], grigiochi, gsx // 32 * 9.3, gsy // 18 * 11, 45)
            if oggetton == 6:
                messaggio("Bomba:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                messaggio("Infligge un po' di danni ai nemici su cui viene lanciata", grigiochi, gsx // 32 * 20,
                          gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 45)
        if dati[37] >= 0:
            messaggio("Bomba velenosa", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 45)
            messaggio("x %i" % dati[37], grigiochi, gsx // 32 * 9.3, gsy // 18 * 12, 45)
            if oggetton == 7:
                messaggio("Bomba velenosa:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                messaggio("Infligge avvelenamento al nemico su cui viene lanciata", grigiochi, gsx // 32 * 20,
                          gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 45)
        if dati[38] >= 0:
            messaggio("Esca", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 45)
            messaggio("x %i" % dati[38], grigiochi, gsx // 32 * 9.3, gsy // 18 * 13, 45)
            if oggetton == 8:
                messaggio("Esca:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                messaggio(u"Distrae i nemici finché non viene distrutta. È possibile", grigiochi, gsx // 32 * 20,
                          gsy // 18 * 14.5, 35)
                messaggio("riprenderla passandoci sopra", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 45)
        if dati[39] >= 0:
            messaggio("Bomba appiccicosa", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 45)
            messaggio("x %i" % dati[39], grigiochi, gsx // 32 * 9.3, gsy // 18 * 14, 45)
            if oggetton == 9:
                messaggio("Bomba appiccicosa:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                messaggio(u"Dimezza la velocità del nemico su cui viene lanciata", grigiochi, gsx // 32 * 20,
                          gsy // 18 * 14.5, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 45)
        if dati[40] >= 0:
            messaggio("Bomba potenziata", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 45)
            messaggio("x %i" % dati[40], grigiochi, gsx // 32 * 9.3, gsy // 18 * 15, 45)
            if oggetton == 10:
                messaggio("Bomba potenziata:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                messaggio("Infligge molti danni ai nemici su cui viene lanciata in un", grigiochi, gsx // 32 * 20,
                          gsy // 18 * 14.5, 35)
                messaggio("vasto raggio", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 45)

        # menu conferma
        if usa != 0:
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 11, gsy // 18 * 12.5, gsx // 32 * 8, gsy // 18 * 4))
            # posizionare il cursore su menu usa
            if usauno:
                xpv = xp
                ypv = yp
                xp = gsx // 32 * 15
                yp = gsy // 18 * 15.1
                voceMarcata = 2
                usauno = False
            schermo.blit(puntatorevecchio, (xpv, ypv))
            messaggio("Usare?", grigiochi, gsx // 32 * 13.3, gsy // 18 * 13.2, 80)
            messaggio("Si", grigiochi, gsx // 32 * 13, gsy // 18 * 15, 60)
            messaggio("No", grigiochi, gsx // 32 * 16, gsy // 18 * 15, 60)

        # vita-status personaggio
        if dati[5] < 0:
            dati[5] = 0
        messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), grigiochi, gsx // 32 * 14, gsy // 18 * 4, 50)
        messaggio("Status alterativi: ", grigiochi, gsx // 32 * 14, gsy // 18 * 5, 50)
        persmen = pygame.transform.scale(persGrafMenu, (gpx * 3, gpy * 3))
        schermo.blit(persmen, (gsx // 32 * 11, gsy // 18 * 4))
        schermo.blit(sfondostastart, (gsx // 32 * 14, (gsy // 18 * 6) + (gpy // 8)))
        if dati[121]:
            avvelenato = pygame.transform.scale(avvelenatoo, (gpx, gpy))
            schermo.blit(avvelenato, (gsx // 32 * 14, gsy // 18 * 6))
        if dati[123] > 0:
            attaccopiu = pygame.transform.scale(attaccopiuo, (gpx, gpy))
            schermo.blit(attaccopiu, ((gsx // 32 * 14) + (2 * gpx // 4 * 3), gsy // 18 * 6))
        if dati[124] > 0:
            difesapiu = pygame.transform.scale(difesapiuo, (gpx, gpy))
            schermo.blit(difesapiu, ((gsx // 32 * 14) + (4 * gpx // 4 * 3), gsy // 18 * 6))
        # vita-status robo
        if dati[10] < 0:
            dati[10] = 0
        messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), grigiochi, gsx // 32 * 14, gsy // 18 * 9, 50)
        messaggio("Status alterativi: ", grigiochi, gsx // 32 * 14, gsy // 18 * 10, 50)
        robomen = pygame.transform.scale(robograf, (gpx * 3, gpy * 3))
        schermo.blit(robomen, (gsx // 32 * 11, gsy // 18 * 8))
        schermo.blit(sfondostastart, (gsx // 32 * 14, gsy // 18 * 11))
        if dati[122] > 0:
            surriscaldato = pygame.transform.scale(surriscaldatoo, (gpx, gpy))
            schermo.blit(surriscaldato, (gsx // 32 * 14, gsy // 18 * 11))
        if dati[125] > 0:
            velocitapiu = pygame.transform.scale(velocitapiuo, (gpx, gpy))
            schermo.blit(velocitapiu, ((gsx // 32 * 14) + (2 * gpx // 4 * 3), gsy // 18 * 11))
        if dati[126] > 0:
            efficienzapiu = pygame.transform.scale(efficienzapiuo, (gpx, gpy))
            schermo.blit(efficienzapiu, ((gsx // 32 * 14) + (4 * gpx // 4 * 3), gsy // 18 * 11))

        if attacco != 0:
            risposta = True

        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
        schermo.blit(imgOggetti[oggetton - 1], (gsx // 32 * 20, gsy // 18 * 3))
        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        if not canaleSoundCanzone.get_busy():
            canaleSoundCanzone.play(canzone)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 3

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato:
                tastop = event.key
                tastotempfps = 5
                if event.key == pygame.K_q and not tastoTrovato:
                    tastoTrovato = True
                    voceMarcata = 0
                    if usa != 0:
                        canaleSoundPuntatore.play(selind)
                        xp = gsx // 32 * 1
                        if usa == 1:
                            yp = gsy // 18 * 5
                        if usa == 2:
                            yp = gsy // 18 * 6
                        if usa == 3:
                            yp = gsy // 18 * 7
                        if usa == 4:
                            yp = gsy // 18 * 8
                        if usa == 5:
                            yp = gsy // 18 * 9
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
                        canaleSoundPuntatore.play(selind)
                        risposta = True
                if event.key == pygame.K_s and voceMarcata == 0 and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and voceMarcata == 0 and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and voceMarcata != 0 and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and voceMarcata != 0 and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_SPACE and not tastoTrovato:
                    tastoTrovato = True
                    usadue = True

                    # usa?
                    if voceMarcata == 1:
                        voceMarcata = 0
                        canaleSoundPuntatore.play(selezione)
                        xp = gsx // 32 * 1
                        # pozione
                        if usa == 1:
                            dati[5] = dati[5] + 100
                            if dati[5] > pvtot:
                                dati[5] = pvtot
                            dati[31] = dati[31] - 1
                            yp = gsy // 18 * 5
                        # carica batt
                        if usa == 2:
                            dati[10] = dati[10] + 250
                            if dati[10] > entot:
                                dati[10] = entot
                            dati[32] = dati[32] - 1
                            yp = gsy // 18 * 6
                        # antidoto
                        if usa == 3:
                            dati[121] = 0
                            dati[33] = dati[33] - 1
                            yp = gsy // 18 * 7
                        # super pozione
                        if usa == 4:
                            dati[5] = dati[5] + 300
                            if dati[5] > pvtot:
                                dati[5] = pvtot
                            dati[34] = dati[34] - 1
                            yp = gsy // 18 * 8
                        # carica migliorato
                        if usa == 5:
                            dati[10] = dati[10] + 600
                            if dati[10] > entot:
                                dati[10] = entot
                            dati[35] = dati[35] - 1
                            yp = gsy // 18 * 9
                        # bomba
                        if usa == 6:
                            attacco = 2
                            yp = gsy // 18 * 11
                        # bomba veleno
                        if usa == 7:
                            attacco = 3
                            yp = gsy // 18 * 12
                        # esca
                        if usa == 8:
                            attacco = 4
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
                    elif voceMarcata == 2:
                        voceMarcata = 0
                        canaleSoundPuntatore.play(selind)
                        xp = gsx // 32 * 1
                        if usa == 1:
                            yp = gsy // 18 * 5
                        if usa == 2:
                            yp = gsy // 18 * 6
                        if usa == 3:
                            yp = gsy // 18 * 7
                        if usa == 4:
                            yp = gsy // 18 * 8
                        if usa == 5:
                            yp = gsy // 18 * 9
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
                        if oggetton == 1:
                            if dati[31] > 0:
                                canaleSoundPuntatore.play(selezione)
                                usa = 1
                                usauno = True
                            else:
                                canaleSoundPuntatore.play(selimp)
                        if oggetton == 2:
                            if dati[32] > 0:
                                canaleSoundPuntatore.play(selezione)
                                usa = 2
                                usauno = True
                            else:
                                canaleSoundPuntatore.play(selimp)
                        if oggetton == 3:
                            if dati[33] > 0:
                                canaleSoundPuntatore.play(selezione)
                                usa = 3
                                usauno = True
                            else:
                                canaleSoundPuntatore.play(selimp)
                        if oggetton == 4:
                            if dati[34] > 0:
                                canaleSoundPuntatore.play(selezione)
                                usa = 4
                                usauno = True
                            else:
                                canaleSoundPuntatore.play(selimp)
                        if oggetton == 5:
                            if dati[35] > 0:
                                canaleSoundPuntatore.play(selezione)
                                usa = 5
                                usauno = True
                            else:
                                canaleSoundPuntatore.play(selimp)
                        if oggetton == 6:
                            if dati[36] > 0:
                                canaleSoundPuntatore.play(selezione)
                                usa = 6
                                usauno = True
                            else:
                                canaleSoundPuntatore.play(selimp)
                        if oggetton == 7:
                            if dati[37] > 0:
                                canaleSoundPuntatore.play(selezione)
                                usa = 7
                                usauno = True
                            else:
                                canaleSoundPuntatore.play(selimp)
                        if oggetton == 8:
                            if dati[38] > 0:
                                canaleSoundPuntatore.play(selezione)
                                usa = 8
                                usauno = True
                            else:
                                canaleSoundPuntatore.play(selimp)
                        if oggetton == 9:
                            if dati[39] > 0:
                                canaleSoundPuntatore.play(selezione)
                                usa = 9
                                usauno = True
                            else:
                                canaleSoundPuntatore.play(selimp)
                        if oggetton == 10:
                            if dati[40] > 0:
                                canaleSoundPuntatore.play(selezione)
                                usa = 10
                                usauno = True
                            else:
                                canaleSoundPuntatore.play(selimp)
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_q or tastop == pygame.K_SPACE or ((tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 3
            if tastop == pygame.K_w and voceMarcata == 0:
                if oggetton != 1 and oggetton != 6:
                    canaleSoundPuntatore.play(spostapun)
                    oggetton = oggetton - 1
                    yp = yp - gsy // 18 * 1
                elif oggetton == 6:
                    canaleSoundPuntatore.play(spostapun)
                    oggetton = oggetton - 1
                    yp = yp - gsy // 18 * 2
                elif oggetton == 1:
                    canaleSoundPuntatore.play(spostapun)
                    yp = gsy // 18 * 15
                    oggetton = 10
            if tastop == pygame.K_a and voceMarcata != 0:
                if voceMarcata == 2:
                    voceMarcata -= 1
                    canaleSoundPuntatore.play(spostapun)
                    xp = xp - gsx // 32 * 3
                elif voceMarcata == 1:
                    canaleSoundPuntatore.play(selimp)
            if tastop == pygame.K_s and voceMarcata == 0:
                if oggetton != 10 and oggetton != 5:
                    canaleSoundPuntatore.play(spostapun)
                    oggetton = oggetton + 1
                    yp = yp + gsy // 18 * 1
                elif oggetton == 5:
                    canaleSoundPuntatore.play(spostapun)
                    oggetton = oggetton + 1
                    yp = yp + gsy // 18 * 2
                elif oggetton == 10:
                    canaleSoundPuntatore.play(spostapun)
                    yp = gsy // 18 * 5
                    oggetton = 1
            if tastop == pygame.K_d and voceMarcata != 0:
                if voceMarcata == 1:
                    voceMarcata += 1
                    canaleSoundPuntatore.play(spostapun)
                    xp = xp + gsx // 32 * 3
                elif voceMarcata == 2:
                    canaleSoundPuntatore.play(selimp)
            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 10, gsy // 18 * 12.5))

            # pozione, carica batt, bomba, antidoto, bomba veleno, esca, super poz, carica migliorato, bomba pot, bomba atomica
            messaggio("Oggetti", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
            if dati[31] >= 0:
                messaggio("Pozione", grigiochi, gsx // 32 * 2, gsy // 18 * 5, 45)
                messaggio("x %i" % dati[31], grigiochi, gsx // 32 * 9.3, gsy // 18 * 5, 45)
                if oggetton == 1:
                    messaggio("Pozione:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                    messaggio("Recupera 100 pv di Rallo", grigiochi, gsx // 32 * 20, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 5, 45)
            if dati[32] >= 0:
                messaggio("Caricabatterie", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 45)
                messaggio("x %i" % dati[32], grigiochi, gsx // 32 * 9.3, gsy // 18 * 6, 45)
                if oggetton == 2:
                    messaggio("Caricabatterie:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                    messaggio("Recupera 250 pe di Colco", grigiochi, gsx // 32 * 20, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 45)
            if dati[33] >= 0:
                messaggio("Medicina", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 45)
                messaggio("x %i" % dati[33], grigiochi, gsx // 32 * 9.3, gsy // 18 * 7, 45)
                if oggetton == 3:
                    messaggio("Medicina:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                    messaggio("Cura avvelenamento a Rallo", grigiochi, gsx // 32 * 20, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 45)
            if dati[34] >= 0:
                messaggio("Super pozione", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 45)
                messaggio("x %i" % dati[34], grigiochi, gsx // 32 * 9.3, gsy // 18 * 8, 45)
                if oggetton == 4:
                    messaggio("Super pozione:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                    messaggio("Recupera 300 pv di Rallo", grigiochi, gsx // 32 * 20, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 45)
            if dati[35] >= 0:
                messaggio("Caricabatterie migliorato", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 45)
                messaggio("x %i" % dati[35], grigiochi, gsx // 32 * 9.3, gsy // 18 * 9, 45)
                if oggetton == 5:
                    messaggio("Caricabatterie migliorato:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                    messaggio("Recupera 600 pe di Colco", grigiochi, gsx // 32 * 20, gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 45)
            if dati[36] >= 0:
                messaggio("Bomba", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 45)
                messaggio("x %i" % dati[36], grigiochi, gsx // 32 * 9.3, gsy // 18 * 11, 45)
                if oggetton == 6:
                    messaggio("Bomba:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                    messaggio("Infligge un po' di danni ai nemici su cui viene lanciata", grigiochi, gsx // 32 * 20,
                              gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 45)
            if dati[37] >= 0:
                messaggio("Bomba velenosa", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 45)
                messaggio("x %i" % dati[37], grigiochi, gsx // 32 * 9.3, gsy // 18 * 12, 45)
                if oggetton == 7:
                    messaggio("Bomba velenosa:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                    messaggio("Infligge avvelenamento al nemico su cui viene lanciata", grigiochi, gsx // 32 * 20,
                              gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 45)
            if dati[38] >= 0:
                messaggio("Esca", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 45)
                messaggio("x %i" % dati[38], grigiochi, gsx // 32 * 9.3, gsy // 18 * 13, 45)
                if oggetton == 8:
                    messaggio("Esca:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                    messaggio(u"Distrae i nemici finché non viene distrutta. È possibile", grigiochi, gsx // 32 * 20,
                              gsy // 18 * 14.5, 35)
                    messaggio("riprenderla passandoci sopra", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 45)
            if dati[39] >= 0:
                messaggio("Bomba appiccicosa", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 45)
                messaggio("x %i" % dati[39], grigiochi, gsx // 32 * 9.3, gsy // 18 * 14, 45)
                if oggetton == 9:
                    messaggio("Bomba appiccicosa:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                    messaggio(u"Dimezza la velocità del nemico su cui viene lanciata", grigiochi, gsx // 32 * 20,
                              gsy // 18 * 14.5, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 45)
            if dati[40] >= 0:
                messaggio("Bomba potenziata", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 45)
                messaggio("x %i" % dati[40], grigiochi, gsx // 32 * 9.3, gsy // 18 * 15, 45)
                if oggetton == 10:
                    messaggio("Bomba potenziata:", grigiochi, gsx // 32 * 20, gsy // 18 * 13.5, 60)
                    messaggio("Infligge molti danni ai nemici su cui viene lanciata in un", grigiochi, gsx // 32 * 20,
                              gsy // 18 * 14.5, 35)
                    messaggio("vasto raggio", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 35)
                    messaggio("", grigiochi, gsx // 32 * 20, gsy // 18 * 15.5, 35)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 45)

            # menu conferma
            if usa != 0:
                pygame.draw.rect(schermo, grigio, (gsx // 32 * 11, gsy // 18 * 12.5, gsx // 32 * 8, gsy // 18 * 4))
                # posizionare il cursore su menu usa
                if usauno:
                    xpv = xp
                    ypv = yp
                    xp = gsx // 32 * 15
                    yp = gsy // 18 * 15.1
                    voceMarcata = 2
                    usauno = False
                schermo.blit(puntatorevecchio, (xpv, ypv))
                messaggio("Usare?", grigiochi, gsx // 32 * 13.3, gsy // 18 * 13.2, 80)
                messaggio("Si", grigiochi, gsx // 32 * 13, gsy // 18 * 15, 60)
                messaggio("No", grigiochi, gsx // 32 * 16, gsy // 18 * 15, 60)

            # vita-status personaggio
            if dati[5] < 0:
                dati[5] = 0
            messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), grigiochi, gsx // 32 * 14, gsy // 18 * 4, 50)
            messaggio("Status alterativi: ", grigiochi, gsx // 32 * 14, gsy // 18 * 5, 50)
            persmen = pygame.transform.scale(persGrafMenu, (gpx * 3, gpy * 3))
            schermo.blit(persmen, (gsx // 32 * 11, gsy // 18 * 4))
            schermo.blit(sfondostastart, (gsx // 32 * 14, (gsy // 18 * 6) + (gpy // 8)))
            if dati[121]:
                avvelenato = pygame.transform.scale(avvelenatoo, (gpx, gpy))
                schermo.blit(avvelenato, (gsx // 32 * 14, gsy // 18 * 6))
            if dati[123] > 0:
                attaccopiu = pygame.transform.scale(attaccopiuo, (gpx, gpy))
                schermo.blit(attaccopiu, ((gsx // 32 * 14) + (2 * gpx // 4 * 3), gsy // 18 * 6))
            if dati[124] > 0:
                difesapiu = pygame.transform.scale(difesapiuo, (gpx, gpy))
                schermo.blit(difesapiu, ((gsx // 32 * 14) + (4 * gpx // 4 * 3), gsy // 18 * 6))
            # vita-status robo
            if dati[10] < 0:
                dati[10] = 0
            messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), grigiochi, gsx // 32 * 14, gsy // 18 * 9, 50)
            messaggio("Status alterativi: ", grigiochi, gsx // 32 * 14, gsy // 18 * 10, 50)
            robomen = pygame.transform.scale(robograf, (gpx * 3, gpy * 3))
            schermo.blit(robomen, (gsx // 32 * 11, gsy // 18 * 8))
            schermo.blit(sfondostastart, (gsx // 32 * 14, gsy // 18 * 11))
            if dati[122] > 0:
                surriscaldato = pygame.transform.scale(surriscaldatoo, (gpx, gpy))
                schermo.blit(surriscaldato, (gsx // 32 * 14, gsy // 18 * 11))
            if dati[125] > 0:
                velocitapiu = pygame.transform.scale(velocitapiuo, (gpx, gpy))
                schermo.blit(velocitapiu, ((gsx // 32 * 14) + (2 * gpx // 4 * 3), gsy // 18 * 11))
            if dati[126] > 0:
                efficienzapiu = pygame.transform.scale(efficienzapiuo, (gpx, gpy))
                schermo.blit(efficienzapiu, ((gsx // 32 * 14) + (4 * gpx // 4 * 3), gsy // 18 * 11))

            if attacco != 0:
                risposta = True

            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
            schermo.blit(imgOggetti[oggetton - 1], (gsx // 32 * 20, gsy // 18 * 3))
            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        clockMenu.tick(fpsMenu)
    return dati, attacco


def chiediconferma(conferma, canzone):
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 2, gpy // 2))
    xp = gsx // 32 * 17.5
    yp = gsy // 18 * 10.3

    tastop = 0
    tastotempfps = 5

    schermo.fill(grigioscu)
    if conferma == 1:
        messaggio(u"Tornare al menu principale?", grigiochi, gsx // 32 * 5, gsy // 18 * 6, 120)
    elif conferma == 2:
        messaggio("Tornare a Windows?", grigiochi, gsx // 32 * 8, gsy // 18 * 6.5, 120)
    messaggio("Si", grigiochi, gsx // 32 * 11, gsy // 18 * 9.5, 120)
    messaggio("No", grigiochi, gsx // 32 * 19, gsy // 18 * 9.5, 120)
    messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
    schermo.blit(puntatore, (xp, yp))
    pygame.display.update()
    voceMarcata = 2
    while True:
        if not canaleSoundCanzone.get_busy():
            canaleSoundCanzone.play(canzone)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 3

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato:
                tastop = event.key
                tastotempfps = 5
                if event.key == pygame.K_q and not tastoTrovato:
                    tastoTrovato = True
                    canaleSoundPuntatore.play(selind)
                    return False, False
                if event.key == pygame.K_a and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_SPACE and not tastoTrovato:
                    tastoTrovato = True
                    if voceMarcata == 1:
                        canaleSoundPuntatore.play(selezione)
                        if conferma == 1:
                            return True, True
                        elif conferma == 2:
                            pygame.quit()
                            quit()
                    elif voceMarcata == 2:
                        canaleSoundPuntatore.play(selind)
                        return False, False
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_SPACE or ((tastop == pygame.K_a or tastop == pygame.K_d) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 3
            if tastop == pygame.K_a:
                if voceMarcata == 2:
                    voceMarcata -= 1
                    canaleSoundPuntatore.play(spostapun)
                    xp = gsx // 32 * 9.5
                else:
                    canaleSoundPuntatore.play(selimp)
            if tastop == pygame.K_d:
                if voceMarcata == 1:
                    voceMarcata += 1
                    canaleSoundPuntatore.play(spostapun)
                    xp = gsx // 32 * 17.5
                else:
                    canaleSoundPuntatore.play(selimp)
            schermo.fill(grigioscu)
            if conferma == 1:
                messaggio(u"Tornare al menu principale?", grigiochi, gsx // 32 * 5, gsy // 18 * 6, 120)
            elif conferma == 2:
                messaggio("Tornare a Windows?", grigiochi, gsx // 32 * 8, gsy // 18 * 6.5, 120)
            messaggio("Si", grigiochi, gsx // 32 * 11, gsy // 18 * 9.5, 120)
            messaggio("No", grigiochi, gsx // 32 * 19, gsy // 18 * 9.5, 120)
            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        clockMenu.tick(fpsMenu)


def start(dati, nmost, porteini, portefin, cofaniini, cofanifin, porte, cofanetti, apriocchio):
    sfondostastart = pygame.transform.scale(sfondostax3, (gpx * 4, gpy))
    perssta = pygame.transform.scale(persGrafMenu, (gpx * 10, gpy * 10))
    robosta = pygame.transform.scale(robograf, (gpx * 10, gpy * 10))
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 2, gpy // 2))
    avvelenatosta = pygame.transform.scale(avvelenatoo, (gpx, gpy))
    surriscaldatosta = pygame.transform.scale(surriscaldatoo, (gpx, gpy))
    attaccopiusta = pygame.transform.scale(attaccopiuo, (gpx, gpy))
    difesapiusta = pygame.transform.scale(difesapiuo, (gpx, gpy))
    velocitapiusta = pygame.transform.scale(velocitapiuo, (gpx, gpy))
    efficienzapiusta = pygame.transform.scale(efficienzapiuo, (gpx, gpy))
    if dati[133] == 0:
        faretraFrecceStart = faretraFrecceStart0
        maxFrecce = 1
    elif dati[133] == 1:
        faretraFrecceStart = faretraFrecceStart1
        maxFrecce = 5
    elif dati[133] == 2:
        faretraFrecceStart = faretraFrecceStart2
        maxFrecce = 20
    elif dati[133] == 3:
        faretraFrecceStart = faretraFrecceStart3
        maxFrecce = 60
    else:
        faretraFrecceStart = 0
        maxFrecce = 0
    xp = gsx // 32 * 1
    yp = gsy // 18 * 5
    carim = True
    risposta = False
    attacco = 0
    conferma = 0
    inizio = False
    voceMarcata = 1

    tastop = 0
    tastotempfps = 5

    # primo frame
    if True:
        esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 10, gsy // 18 * 12.5))
        messaggio("Menu start", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
        messaggio("Oggetti", grigiochi, gsx // 32 * 2, gsy // 18 * 5, 50)
        messaggio("Equipaggiamento", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 50)
        messaggio("Setta Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 50)
        messaggio("Mappa", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 50)
        messaggio("Diario", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 50)
        if nmost == -1:
            messaggio("Salva", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 50)
        else:
            messaggio("Salva", grigioscu, gsx // 32 * 2, gsy // 18 * 13, 50)
        messaggio(u"Torna al menu principale", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 50)
        messaggio("Torna a Windows", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 50)
        messaggio(u"Esc / Q: Esci dal menu", grigiochi, gsx // 32 * 23, gsy // 18 * 1, 50)
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
        messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), grigiochi, gsx // 32 * 13.5, gsy // 18 * 13, 50)
        messaggio("Lv:  " + str(dati[4]), grigiochi, gsx // 32 * 13.5, gsy // 18 * 14, 50)
        if dati[4] < 100:
            messaggio("Esp:  " + str(dati[127]) + " / " + str(esptot), grigiochi, gsx // 32 * 16, gsy // 18 * 14,
                      50)
        else:
            messaggio("Esp:  -- / --", grigiochi, gsx // 32 * 16, gsy // 18 * 14, 50)
        messaggio("Status alterativi: ", grigiochi, gsx // 32 * 13.5, gsy // 18 * 15, 50)
        schermo.blit(sfondostastart, (gsx // 32 * 13.5, (gsy // 18 * 16) + (gpy // 8)))
        if dati[121]:
            schermo.blit(avvelenatosta, (gsx // 32 * 13.5, gsy // 18 * 16))
        if dati[123] > 0:
            schermo.blit(attaccopiusta, ((gsx // 32 * 13.5) + (2 * gpx // 4 * 3), gsy // 18 * 16))
        if dati[124] > 0:
            schermo.blit(difesapiusta, ((gsx // 32 * 13.5) + (4 * gpx // 4 * 3), gsy // 18 * 16))
        # vita-status robo
        if dati[10] < 0:
            dati[10] = 0
        messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), grigiochi, gsx // 32 * 23.5, gsy // 18 * 13, 50)
        messaggio("Status alterativi: ", grigiochi, gsx // 32 * 23.5, gsy // 18 * 14, 50)
        schermo.blit(sfondostastart, (gsx // 32 * 23.5, (gsy // 18 * 15) + (gpy // 8)))
        if dati[122] > 0:
            schermo.blit(surriscaldatosta, (gsx // 32 * 23.5, gsy // 18 * 15))
        if dati[125] > 0:
            schermo.blit(velocitapiusta, ((gsx // 32 * 23.5) + (2 * gpx // 4 * 3), gsy // 18 * 15))
        if dati[126] > 0:
            schermo.blit(efficienzapiusta, ((gsx // 32 * 23.5) + (4 * gpx // 4 * 3), gsy // 18 * 15))

        if attacco != 0:
            risposta = True

        if faretraFrecceStart != 0:
            schermo.blit(faretraFrecceStart, (gsx // 32 * 21.5, gsy // 18 * 2.5))
            messaggio("Frecce: " + str(dati[132]) + " / " + str(maxFrecce), grigiochi, gsx // 32 * 21.5, gsy // 18 * 6, 50)
        schermo.blit(sacchettoDenaroStart, (gsx // 32 * 26.5, gsy // 18 * 2.5))
        messaggio("Monete: " + str(dati[131]), grigiochi, gsx // 32 * 26.5, gsy // 18 * 6, 50)

        schermo.blit(perssta, (gsx // 32 * 11.5, gsy // 18 * 2))
        schermo.blit(robosta, (gsx // 32 * 21, gsy // 18 * 2))
        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        if not canaleSoundCanzone.get_busy():
            canaleSoundCanzone.play(c27)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 3

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato:
                tastop = event.key
                tastotempfps = 5
                if (event.key == pygame.K_q or event.key == pygame.K_ESCAPE) and not tastoTrovato:
                    tastoTrovato = True
                    canaleSoundPuntatore.play(selind)
                    inizio = False
                    risposta = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_SPACE and not tastoTrovato:
                    tastoTrovato = True
                    if voceMarcata == 6 and nmost > -1:
                        canaleSoundPuntatore.play(selimp)
                    else:
                        canaleSoundPuntatore.play(selezione)
                    inizio = False
                    # oggetti
                    if voceMarcata == 1:
                        dati, attacco = oggetti(dati, c27)
                        carim = True
                    # tecniche
                    """if yp == gsy // 18 * 6:
                        #if not apriocchio:
                        dati, attacco = tecniche(dati)
                        carim = True"""
                    # equip pers
                    if voceMarcata == 2:
                        dati = equip(dati, c27)
                        carim = True
                    # equip robot
                    if voceMarcata == 3:
                        dati = equiprobo(dati, c27)
                        carim = True
                    # mappa
                    if voceMarcata == 4:
                        print ("mappa")
                    # diario
                    if voceMarcata == 5:
                        print ("diario")
                    # salva
                    if voceMarcata == 6:
                        #if nmost == -1:
                        n = scegli_sal(3, len(dati), c27)
                        if n != -1:
                            salvataggio(n, dati, porteini, portefin, cofaniini, cofanifin, porte, cofanetti)
                    # menu
                    if voceMarcata == 7:
                        conferma = 1
                    # chiudi
                    if voceMarcata == 8:
                        conferma = 2
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_SPACE or ((tastop == pygame.K_s or tastop == pygame.K_w) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 3
            if tastop == pygame.K_s:
                if voceMarcata != 5 and voceMarcata != 8:
                    canaleSoundPuntatore.play(spostapun)
                    yp = yp + gsy // 18 * 1
                    voceMarcata += 1
                else:
                    if voceMarcata == 5:
                        canaleSoundPuntatore.play(spostapun)
                        yp = yp + gsy // 18 * 4
                        voceMarcata += 1
                    elif voceMarcata == 8:
                        canaleSoundPuntatore.play(spostapun)
                        yp = gsy // 18 * 5
                        voceMarcata = 1
            if tastop == pygame.K_w:
                if voceMarcata != 6 and voceMarcata != 1:
                    canaleSoundPuntatore.play(spostapun)
                    yp = yp - gsy // 18 * 1
                    voceMarcata -= 1
                else:
                    if voceMarcata == 6:
                        canaleSoundPuntatore.play(spostapun)
                        yp = yp - gsy // 18 * 4
                        voceMarcata -= 1
                    elif voceMarcata == 1:
                        canaleSoundPuntatore.play(spostapun)
                        yp = gsy // 18 * 15
                        voceMarcata = 8
            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

            # chiedere conferma per uscire
            if conferma != 0:
                inizio, risposta = chiediconferma(conferma, c27)
                conferma = 0

            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 10, gsy // 18 * 12.5))
            messaggio("Menu start", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
            messaggio("Oggetti", grigiochi, gsx // 32 * 2, gsy // 18 * 5, 50)
            messaggio("Equipaggiamento", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 50)
            messaggio("Setta Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 50)
            messaggio("Mappa", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 50)
            messaggio("Diario", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 50)
            if nmost == -1:
                messaggio("Salva", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 50)
            else:
                messaggio("Salva", grigioscu, gsx // 32 * 2, gsy // 18 * 13, 50)
            messaggio(u"Torna al menu principale", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 50)
            messaggio("Torna a Windows", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 50)
            messaggio(u"Esc / Q: Esci dal menu", grigiochi, gsx // 32 * 23, gsy // 18 * 1, 50)
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
            messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), grigiochi, gsx // 32 * 13.5, gsy // 18 * 13, 50)
            messaggio("Lv:  " + str(dati[4]), grigiochi, gsx // 32 * 13.5, gsy // 18 * 14, 50)
            if dati[4] < 100:
                messaggio("Esp:  " + str(dati[127]) + " / " + str(esptot), grigiochi, gsx // 32 * 16, gsy // 18 * 14, 50)
            else:
                messaggio("Esp:  -- / --", grigiochi, gsx // 32 * 16, gsy // 18 * 14, 50)
            messaggio("Status alterativi: ", grigiochi, gsx // 32 * 13.5, gsy // 18 * 15, 50)
            schermo.blit(sfondostastart, (gsx // 32 * 13.5, (gsy // 18 * 16) + (gpy // 8)))
            if dati[121]:
                schermo.blit(avvelenatosta, (gsx // 32 * 13.5, gsy // 18 * 16))
            if dati[123] > 0:
                schermo.blit(attaccopiusta, ((gsx // 32 * 13.5) + (2 * gpx // 4 * 3), gsy // 18 * 16))
            if dati[124] > 0:
                schermo.blit(difesapiusta, ((gsx // 32 * 13.5) + (4 * gpx // 4 * 3), gsy // 18 * 16))
            # vita-status robo
            if dati[10] < 0:
                dati[10] = 0
            messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), grigiochi, gsx // 32 * 23.5, gsy // 18 * 13, 50)
            messaggio("Status alterativi: ", grigiochi, gsx // 32 * 23.5, gsy // 18 * 14, 50)
            schermo.blit(sfondostastart, (gsx // 32 * 23.5, (gsy // 18 * 15) + (gpy // 8)))
            if dati[122] > 0:
                schermo.blit(surriscaldatosta, (gsx // 32 * 23.5, gsy // 18 * 15))
            if dati[125] > 0:
                schermo.blit(velocitapiusta, ((gsx // 32 * 23.5) + (2 * gpx // 4 * 3), gsy // 18 * 15))
            if dati[126] > 0:
                schermo.blit(efficienzapiusta, ((gsx // 32 * 23.5) + (4 * gpx // 4 * 3), gsy // 18 * 15))

            if attacco != 0:
                risposta = True

            if faretraFrecceStart != 0:
                schermo.blit(faretraFrecceStart, (gsx // 32 * 21.5, gsy // 18 * 2.5))
                messaggio("Frecce: " + str(dati[132]) + " / " + str(maxFrecce), grigiochi, gsx // 32 * 21.5, gsy // 18 * 6, 50)
            schermo.blit(sacchettoDenaroStart, (gsx // 32 * 26.5, gsy // 18 * 2.5))
            messaggio("Monete: " + str(dati[131]), grigiochi, gsx // 32 * 26.5, gsy // 18 * 6, 50)

            schermo.blit(perssta, (gsx // 32 * 11.5, gsy // 18 * 2))
            schermo.blit(robosta, (gsx // 32 * 21, gsy // 18 * 2))
            schermo.blit(puntatore, (xp, yp))
            if not risposta:
                pygame.display.update()
            else:
                schermo.fill(grigioscu)

        clockMenu.tick(fpsMenu)
    canaleSoundCanzone.stop()
    return dati, inizio, attacco


def startBattaglia(dati, animaOggetto, x, y, npers, rx, ry):
    xp = gpx * 1
    yp = gpy * 5
    sconosciutoOggetto = pygame.transform.scale(sconosciutoOggettoMenu, (gpx * 4, gpy * 4))
    sconosciutoOggettoIco = pygame.transform.scale(sconosciutoOggettoIcoMenu, (gpx, gpy))

    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

    attacco = 0
    disegnoOggetto = 0
    risposta = False
    voceMarcata = 1

    tastop = 0
    tastotempfps = 5

    difensivi = True
    offensivi = False
    sposta = False

    oggetton = 1
    vettoreOggettiGraf = []
    vettoreOggettiIco = []
    while oggetton <= 10:
        if dati[oggetton + 30] >= 0:
            vettoreOggettiGraf.append(vetImgOggettiStart[oggetton - 1])
            vettoreOggettiIco.append(vetIcoOggettiMenu[oggetton - 1])
        else:
            vettoreOggettiGraf.append(sconosciutoOggetto)
            vettoreOggettiIco.append(sconosciutoOggettoIco)
        oggetton += 1

    # primo frame
    if True:
        schermo.blit(sfondoStartBattaglia, (0, 0))
        if difensivi:
            if voceMarcata == 1:
                disegnoOggetto = 0
            if voceMarcata == 2:
                disegnoOggetto = 1
            if voceMarcata == 3:
                disegnoOggetto = 2
            if voceMarcata == 4:
                disegnoOggetto = 3
            if voceMarcata == 5:
                disegnoOggetto = 4
        elif offensivi:
            if voceMarcata == 1:
                disegnoOggetto = 5
            if voceMarcata == 2:
                disegnoOggetto = 6
            if voceMarcata == 3:
                disegnoOggetto = 7
            if voceMarcata == 4:
                disegnoOggetto = 8
            if voceMarcata == 5:
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
            if difensivi and (i == 0 or i == 1 or i == 2 or i == 3 or i == 4):
                schermo.blit(vettoreOggettiIco[i], (gpx * (disegnati + 1), gpy * 5))
                disegnati += 1
            if offensivi and (i == 5 or i == 6 or i == 7 or i == 8 or i == 9):
                schermo.blit(vettoreOggettiIco[i], (gpx * (disegnati + 1), (gpy * 5) + (gpy // 2)))
                disegnati += 1
            i += 1
        if difensivi:
            if voceMarcata == 1:
                messaggio("Pozione", grigiochi, gpx // 3, gpy // 3, 45)
            if voceMarcata == 2:
                messaggio("Caricabatterie", grigiochi, gpx // 3, gpy // 3, 45)
            if voceMarcata == 3:
                messaggio("Medicina", grigiochi, gpx // 3, gpy // 3, 45)
            if voceMarcata == 4:
                messaggio("Super pozione", grigiochi, gpx // 3, gpy // 3, 45)
            if voceMarcata == 5:
                messaggio("Caricabatterie migliorato", grigiochi, gpx // 3, gpy // 3, 45)
            schermo.blit(scorriGiu, (gpx * 3, gpy * 6))
        if offensivi:
            if voceMarcata == 1:
                messaggio("Bomba", grigiochi, gpx // 3, gpy // 3, 45)
            if voceMarcata == 2:
                messaggio("Bomba velenosa", grigiochi, gpx // 3, gpy // 3, 45)
            if voceMarcata == 3:
                messaggio("Esca", grigiochi, gpx // 3, gpy // 3, 45)
            if voceMarcata == 4:
                messaggio("Bomba appiccicosa", grigiochi, gpx // 3, gpy // 3, 45)
            if voceMarcata == 5:
                messaggio("Bomba potenziata", grigiochi, gpx // 3, gpy // 3, 45)
            schermo.blit(scorriSu, (gpx * 3, (gpy * 5) - (gpy // 2)))

        if not risposta:
            pygame.display.update()

    while not risposta:
        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 3

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato:
                tastop = event.key
                tastotempfps = 5
                if (event.key == pygame.K_q or event.key == pygame.K_ESCAPE) and not tastoTrovato:
                    tastoTrovato = True
                    canaleSoundPuntatore.play(selind)
                    risposta = True
                if event.key == pygame.K_a and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_SPACE and not tastoTrovato:
                    tastoTrovato = True
                    if difensivi:
                        # pozione
                        if voceMarcata == 1 and dati[31] > 0:
                            animaOggetto[0] = "pozione"
                            dati[5] = dati[5] + 100
                            if dati[5] > pvtot:
                                dati[5] = pvtot
                            dati[31] = dati[31] - 1
                            sposta = True
                            risposta = True
                        # carica batt
                        if voceMarcata == 2 and dati[32] > 0 and (abs(x - rx) + abs(y - ry)) <= gpx:
                            animaOggetto[0] = "caricaBatterie"
                            dati[10] = dati[10] + 250
                            if dati[10] > entot:
                                dati[10] = entot
                            dati[32] = dati[32] - 1
                            # npers: 1=d, 2=a, 3=w, 4=s
                            if x < rx:
                                npers = 1
                            elif x > rx:
                                npers = 2
                            elif y < ry:
                                npers = 4
                            elif y > ry:
                                npers = 3
                            sposta = True
                            risposta = True
                        # antidoto
                        if voceMarcata == 3 and dati[33] > 0:
                            animaOggetto[0] = "medicina"
                            dati[121] = 0
                            dati[33] = dati[33] - 1
                            sposta = True
                            risposta = True
                        # super pozione
                        if voceMarcata == 4 and dati[34] > 0:
                            animaOggetto[0] = "superPozione"
                            dati[5] = dati[5] + 300
                            if dati[5] > pvtot:
                                dati[5] = pvtot
                            dati[34] = dati[34] - 1
                            sposta = True
                            risposta = True
                        # carica migliorato
                        if voceMarcata == 5 and dati[35] > 0 and (abs(x - rx) + abs(y - ry)) <= gpx:
                            animaOggetto[0] = "caricaBatterieMigliorato"
                            dati[10] = dati[10] + 600
                            if dati[10] > entot:
                                dati[10] = entot
                            dati[35] = dati[35] - 1
                            # npers: 1=d, 2=a, 3=w, 4=s
                            if x < rx:
                                npers = 1
                            elif x > rx:
                                npers = 2
                            elif y < ry:
                                npers = 4
                            elif y > ry:
                                npers = 3
                            sposta = True
                            risposta = True
                    elif offensivi:
                        # bomba
                        if voceMarcata == 1 and dati[36] > 0:
                            attacco = 2
                            risposta = True
                        # bomba veleno
                        if voceMarcata == 2 and dati[37] > 0:
                            attacco = 3
                            risposta = True
                        # esca
                        if voceMarcata == 3 and dati[38] > 0:
                            attacco = 4
                            risposta = True
                        # bomba appiccicosa
                        if voceMarcata == 4 and dati[39] > 0:
                            attacco = 5
                            risposta = True
                        # bomba potenziata
                        if voceMarcata == 5 and dati[40] > 0:
                            attacco = 6
                            risposta = True

                    if risposta:
                        canaleSoundPuntatore.play(selezione)
                    else:
                        canaleSoundPuntatore.play(selimp)
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_SPACE or ((tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d or tastop == pygame.K_w) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 3
            if tastop == pygame.K_w:
                if offensivi:
                    canaleSoundPuntatore.play(spostapun)
                    yp = gpy * 5
                    offensivi = False
                    difensivi = True
                else:
                    canaleSoundPuntatore.play(selimp)
            if tastop == pygame.K_a:
                if voceMarcata != 1:
                    voceMarcata -= 1
                    canaleSoundPuntatore.play(spostapun)
                    xp = xp - gpx
                else:
                    voceMarcata += 4
                    canaleSoundPuntatore.play(spostapun)
                    xp = gpx * 5
            if tastop == pygame.K_s:
                if difensivi:
                    canaleSoundPuntatore.play(spostapun)
                    yp = (gpy * 5) + (gpy // 2)
                    difensivi = False
                    offensivi = True
                else:
                    canaleSoundPuntatore.play(selimp)
            if tastop == pygame.K_d:
                if voceMarcata != 5:
                    voceMarcata += 1
                    canaleSoundPuntatore.play(spostapun)
                    xp = xp + gpx
                else:
                    voceMarcata -= 4
                    canaleSoundPuntatore.play(spostapun)
                    xp = gpx * 1
            schermo.blit(sfondoStartBattaglia, (0, 0))
            if difensivi:
                if voceMarcata == 1:
                    disegnoOggetto = 0
                if voceMarcata == 2:
                    disegnoOggetto = 1
                if voceMarcata == 3:
                    disegnoOggetto = 2
                if voceMarcata == 4:
                    disegnoOggetto = 3
                if voceMarcata == 5:
                    disegnoOggetto = 4
            elif offensivi:
                if voceMarcata == 1:
                    disegnoOggetto = 5
                if voceMarcata == 2:
                    disegnoOggetto = 6
                if voceMarcata == 3:
                    disegnoOggetto = 7
                if voceMarcata == 4:
                    disegnoOggetto = 8
                if voceMarcata == 5:
                    disegnoOggetto = 9
            schermo.blit(vettoreOggettiGraf[disegnoOggetto], (gpx // 2, gpy * 1))
            if dati[disegnoOggetto + 31] <= 0:
                schermo.blit(puntatOut, (xp, yp))
                qta = 0
            elif (disegnoOggetto == 1 or disegnoOggetto == 4) and abs(x - rx) + abs(y - ry) > gpx:
                schermo.blit(puntatOut, (xp, yp))
                qta = dati[disegnoOggetto + 31]
            else:
                schermo.blit(puntatIn, (xp, yp))
                qta = dati[disegnoOggetto + 31]
            messaggio("x%i" % qta, grigiochi, (gpx * 4) + (gpx // 2), gpy * 3, 80)
            disegnati = 0
            i = 0
            while i < 10:
                if difensivi and (i == 0 or i == 1 or i == 2 or i == 3 or i == 4):
                    schermo.blit(vettoreOggettiIco[i], (gpx * (disegnati + 1), gpy * 5))
                    disegnati += 1
                if offensivi and (i == 5 or i == 6 or i == 7 or i == 8 or i == 9):
                    schermo.blit(vettoreOggettiIco[i], (gpx * (disegnati + 1), (gpy * 5) + (gpy // 2)))
                    disegnati += 1
                i += 1
            if difensivi:
                if voceMarcata == 1:
                    messaggio("Pozione", grigiochi, gpx // 3, gpy // 3, 45)
                if voceMarcata == 2:
                    messaggio("Caricabatterie", grigiochi, gpx // 3, gpy // 3, 45)
                if voceMarcata == 3:
                    messaggio("Medicina", grigiochi, gpx // 3, gpy // 3, 45)
                if voceMarcata == 4:
                    messaggio("Super pozione", grigiochi, gpx // 3, gpy // 3, 45)
                if voceMarcata == 5:
                    messaggio("Caricabatterie migliorato", grigiochi, gpx // 3, gpy // 3, 45)
                schermo.blit(scorriGiu, (gpx * 3, gpy * 6))
            if offensivi:
                if voceMarcata == 1:
                    messaggio("Bomba", grigiochi, gpx // 3, gpy // 3, 45)
                if voceMarcata == 2:
                    messaggio("Bomba velenosa", grigiochi, gpx // 3, gpy // 3, 45)
                if voceMarcata == 3:
                    messaggio("Esca", grigiochi, gpx // 3, gpy // 3, 45)
                if voceMarcata == 4:
                    messaggio("Bomba appiccicosa", grigiochi, gpx // 3, gpy // 3, 45)
                if voceMarcata == 5:
                    messaggio("Bomba potenziata", grigiochi, gpx // 3, gpy // 3, 45)
                schermo.blit(scorriSu, (gpx * 3, (gpy * 5) - (gpy // 2)))

            if not risposta:
                pygame.display.update()

        clockMenu.tick(fpsMenu)
    return dati, attacco, sposta, animaOggetto, npers
