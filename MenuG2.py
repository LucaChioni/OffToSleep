# -*- coding: utf-8 -*-

from GenericFuncG2 import *


def scegli_sal(cosa, lunghezzadati, canzone):
    # posizione-dimensione puntatore
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatorevecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    xp = GlobalVarG2.gsx // 32 * 6.5
    yp = GlobalVarG2.gsy // 18 * 9.5
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
        GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        if cosa == 2:
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.rossoScuro, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 7, GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 9.5))
        else:
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 7, GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 9.5))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 7))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 26, GlobalVarG2.gsy // 18 * 7))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 26, GlobalVarG2.gsy // 18 * 15.5))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 15.5))
        if cosa == 1:
            messaggio("Carica partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 4.5, 120)
            messaggio("SHIFT: cancella partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 1, 50)
        if cosa == 2:
            messaggio("Cancella partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 4.5, 120)
            messaggio("SHIFT: carica partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 1, 50)
        if cosa == 3:
            messaggio("Salva partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 4.5, 120)
        if conferma:
            if primaconf:
                vxp = xp
                vyp = yp
                xp = GlobalVarG2.gsx // 32 * 22.3
                yp = GlobalVarG2.gsy // 18 * 6.3
                voceMarcata = 2
                primaconf = False
            if cosa == 2:
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.rossoScuro, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 3.5, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 5))
            else:
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 3.5, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 3.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 26, GlobalVarG2.gsy // 18 * 3.5))
            messaggio("Confermi?", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 4.5, 70)
            messaggio("Si", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20.2, GlobalVarG2.gsy // 18 * 6, 70)
            messaggio("No", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23.2, GlobalVarG2.gsy // 18 * 6, 70)
            GlobalVarG2.schermo.blit(puntatorevecchio, (vxp, vyp))
        messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
        GlobalVarG2.schermo.blit(GlobalVarG2.s1, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 8))
        GlobalVarG2.schermo.blit(GlobalVarG2.s2, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 8))
        GlobalVarG2.schermo.blit(GlobalVarG2.s3, (GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 8))

        # lettura salvataggi per riconoscerli
        contasalva = 1
        while contasalva <= 3:
            leggi = open("Salvataggi/Salvataggio%i.txt" % contasalva, "r")
            leggifile = leggi.read()
            dati = leggifile.split("_")
            dati.pop(len(dati) - 1)
            if len(dati) == 0:
                if contasalva == 1:
                    messaggio("Slot vuoto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 7.5, GlobalVarG2.gsy // 18 * 11, 60)
                elif contasalva == 2:
                    messaggio("Slot vuoto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14.5, GlobalVarG2.gsy // 18 * 11, 60)
                elif contasalva == 3:
                    messaggio("Slot vuoto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 21.5, GlobalVarG2.gsy // 18 * 11, 60)
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
                        persalva = pygame.transform.scale(GlobalVarG2.perso, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        persSalvaBraccia = pygame.transform.scale(GlobalVarG2.persob, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        spasalva = pygame.transform.scale(GlobalVarG2.vetImgSpadePixellate[dati[6]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        arcsalva = pygame.transform.scale(GlobalVarG2.vetImgArchiPixellate[dati[128]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        armsalva = pygame.transform.scale(GlobalVarG2.vetImgArmaturePixellate[dati[8]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        scusalva = pygame.transform.scale(GlobalVarG2.vetImgScudiPixellate[dati[7]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        guasalva = pygame.transform.scale(GlobalVarG2.vetImgGuantiPixellate[dati[129]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        colsalva = pygame.transform.scale(GlobalVarG2.vetImgCollanePixellate[dati[130]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        messaggio("Livello: " + str(dati[4]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 7.5, GlobalVarG2.gsy // 18 * 11, 60)
                        GlobalVarG2.schermo.blit(arcsalva, (GlobalVarG2.gpx * 8, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(persalva, (GlobalVarG2.gpx * 8, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(persSalvaBraccia, (GlobalVarG2.gpx * 8, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(armsalva, (GlobalVarG2.gpx * 8, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(colsalva, (GlobalVarG2.gpx * 8, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(spasalva, (GlobalVarG2.gpx * 8, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(guasalva, (GlobalVarG2.gpx * 8, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(scusalva, (GlobalVarG2.gpx * 8, GlobalVarG2.gpy * 12))
                    else:
                        messaggio("Dati corrotti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 7.5, GlobalVarG2.gsy // 18 * 11, 60)
                elif contasalva == 2:
                    if not errore:
                        persalva = pygame.transform.scale(GlobalVarG2.perso, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        persSalvaBraccia = pygame.transform.scale(GlobalVarG2.persob, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        spasalva = pygame.transform.scale(GlobalVarG2.vetImgSpadePixellate[dati[6]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        arcsalva = pygame.transform.scale(GlobalVarG2.vetImgArchiPixellate[dati[128]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        armsalva = pygame.transform.scale(GlobalVarG2.vetImgArmaturePixellate[dati[8]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        scusalva = pygame.transform.scale(GlobalVarG2.vetImgScudiPixellate[dati[7]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        guasalva = pygame.transform.scale(GlobalVarG2.vetImgGuantiPixellate[dati[129]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        colsalva = pygame.transform.scale(GlobalVarG2.vetImgCollanePixellate[dati[130]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        messaggio("Livello: " + str(dati[4]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14.5, GlobalVarG2.gsy // 18 * 11, 60)
                        GlobalVarG2.schermo.blit(arcsalva, (GlobalVarG2.gpx * 15, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(persalva, (GlobalVarG2.gpx * 15, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(persSalvaBraccia, (GlobalVarG2.gpx * 15, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(armsalva, (GlobalVarG2.gpx * 15, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(colsalva, (GlobalVarG2.gpx * 15, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(spasalva, (GlobalVarG2.gpx * 15, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(guasalva, (GlobalVarG2.gpx * 15, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(scusalva, (GlobalVarG2.gpx * 15, GlobalVarG2.gpy * 12))
                    else:
                        messaggio("Dati corrotti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14.5, GlobalVarG2.gsy // 18 * 11, 60)
                elif contasalva == 3:
                    if not errore:
                        persalva = pygame.transform.scale(GlobalVarG2.perso, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        persSalvaBraccia = pygame.transform.scale(GlobalVarG2.persob, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        spasalva = pygame.transform.scale(GlobalVarG2.vetImgSpadePixellate[dati[6]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        arcsalva = pygame.transform.scale(GlobalVarG2.vetImgArchiPixellate[dati[128]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        armsalva = pygame.transform.scale(GlobalVarG2.vetImgArmaturePixellate[dati[8]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        scusalva = pygame.transform.scale(GlobalVarG2.vetImgScudiPixellate[dati[7]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        guasalva = pygame.transform.scale(GlobalVarG2.vetImgGuantiPixellate[dati[129]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        colsalva = pygame.transform.scale(GlobalVarG2.vetImgCollanePixellate[dati[130]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                        messaggio("Livello: " + str(dati[4]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 21.5, GlobalVarG2.gsy // 18 * 11, 60)
                        GlobalVarG2.schermo.blit(arcsalva, (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(persalva, (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(persSalvaBraccia, (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(armsalva, (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(colsalva, (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(spasalva, (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(guasalva, (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 12))
                        GlobalVarG2.schermo.blit(scusalva, (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 12))
                    else:
                        messaggio("Dati corrotti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 21.5, GlobalVarG2.gsy // 18 * 11, 60)
            contasalva = contasalva + 1
            leggi.close()

        GlobalVarG2.schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 2

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
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        xp = vxp
                        yp = vyp
                        conferma = False
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        n = -1
                        return n
                if event.key == pygame.K_d and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_LSHIFT and not tastoTrovato:
                    tastoTrovato = True
                    if conferma and (cosa == 1 or cosa == 2):
                        xp = vxp
                        yp = vyp
                        conferma = False
                    if cosa == 1:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selsta)
                        cosa = 2
                    elif cosa == 2:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selsta)
                        cosa = 1
                if event.key == pygame.K_SPACE and not tastoTrovato:
                    tastoTrovato = True
                    if conferma:
                        if voceMarcata == 1:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            if cosa == 1 or cosa == 3:
                                risposta = True
                                return n
                            else:
                                leggi = open("Salvataggi/Salvataggio%i.txt" % n, "w")
                                leggi.close()
                                xp = vxp
                                yp = vyp
                                conferma = False
                        if voceMarcata == 2:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                            xp = vxp
                            yp = vyp
                            conferma = False
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        conferma = True
                        primaconf = True
                        n = salMarcato
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_q or tastop == pygame.K_SPACE or tastop == pygame.K_LSHIFT or ((tastop == pygame.K_a or tastop == pygame.K_d) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_a or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_a:
                if conferma:
                    if voceMarcata == 2:
                        voceMarcata -= 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 19.3
                else:
                    if salMarcato == 3:
                        salMarcato -= 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 13.5
                    elif salMarcato == 2:
                        salMarcato -= 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 6.5
                    elif salMarcato == 1:
                        salMarcato += 2
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 20.5
            if tastop == pygame.K_d:
                if conferma:
                    if voceMarcata == 1:
                        voceMarcata += 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 22.3
                else:
                    if salMarcato == 1:
                        salMarcato += 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 13.5
                    elif salMarcato == 2:
                        salMarcato += 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 20.5
                    elif salMarcato == 3:
                        salMarcato -= 2
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 6.5

            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            if cosa == 2:
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.rossoScuro, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 7, GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 9.5))
            else:
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 7, GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 9.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 7))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 26, GlobalVarG2.gsy // 18 * 7))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 26, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 15.5))
            if cosa == 1:
                messaggio("Carica partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 4.5, 120)
                messaggio("SHIFT: cancella partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 1, 50)
            if cosa == 2:
                messaggio("Cancella partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 4.5, 120)
                messaggio("SHIFT: carica partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 1, 50)
            if cosa == 3:
                messaggio("Salva partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 4.5, 120)
            if conferma:
                if primaconf:
                    vxp = xp
                    vyp = yp
                    xp = GlobalVarG2.gsx // 32 * 22.3
                    yp = GlobalVarG2.gsy // 18 * 6.3
                    voceMarcata = 2
                    primaconf = False
                if cosa == 2:
                    pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.rossoScuro, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 3.5, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 5))
                else:
                    pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 3.5, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 5))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 3.5))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 26, GlobalVarG2.gsy // 18 * 3.5))
                messaggio("Confermi?", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 4.5, 70)
                messaggio("Si", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20.2, GlobalVarG2.gsy // 18 * 6, 70)
                messaggio("No", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23.2, GlobalVarG2.gsy // 18 * 6, 70)
                GlobalVarG2.schermo.blit(puntatorevecchio, (vxp, vyp))
            messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
            GlobalVarG2.schermo.blit(GlobalVarG2.s1, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 8))
            GlobalVarG2.schermo.blit(GlobalVarG2.s2, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 8))
            GlobalVarG2.schermo.blit(GlobalVarG2.s3, (GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 8))

            # lettura salvataggi per riconoscerli
            contasalva = 1
            while contasalva <= 3:
                leggi = open("Salvataggi/Salvataggio%i.txt" % contasalva, "r")
                leggifile = leggi.read()
                dati = leggifile.split("_")
                dati.pop(len(dati) - 1)
                if len(dati) == 0:
                    if contasalva == 1:
                        messaggio("Slot vuoto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 7.5, GlobalVarG2.gsy // 18 * 11, 60)
                    elif contasalva == 2:
                        messaggio("Slot vuoto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14.5, GlobalVarG2.gsy // 18 * 11, 60)
                    elif contasalva == 3:
                        messaggio("Slot vuoto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 21.5, GlobalVarG2.gsy // 18 * 11, 60)
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
                            persalva = pygame.transform.scale(GlobalVarG2.perso, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            persSalvaBraccia = pygame.transform.scale(GlobalVarG2.persob, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            spasalva = pygame.transform.scale(GlobalVarG2.vetImgSpadePixellate[dati[6]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            arcsalva = pygame.transform.scale(GlobalVarG2.vetImgArchiPixellate[dati[128]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            armsalva = pygame.transform.scale(GlobalVarG2.vetImgArmaturePixellate[dati[8]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            scusalva = pygame.transform.scale(GlobalVarG2.vetImgScudiPixellate[dati[7]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            guasalva = pygame.transform.scale(GlobalVarG2.vetImgGuantiPixellate[dati[129]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            colsalva = pygame.transform.scale(GlobalVarG2.vetImgCollanePixellate[dati[130]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            messaggio("Livello: " + str(dati[4]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 7.5, GlobalVarG2.gsy // 18 * 11, 60)
                            GlobalVarG2.schermo.blit(arcsalva, (GlobalVarG2.gpx * 8, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(persalva, (GlobalVarG2.gpx * 8, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(persSalvaBraccia, (GlobalVarG2.gpx * 8, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(armsalva, (GlobalVarG2.gpx * 8, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(colsalva, (GlobalVarG2.gpx * 8, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(spasalva, (GlobalVarG2.gpx * 8, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(guasalva, (GlobalVarG2.gpx * 8, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(scusalva, (GlobalVarG2.gpx * 8, GlobalVarG2.gpy * 12))
                        else:
                            messaggio("Dati corrotti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 7.5, GlobalVarG2.gsy // 18 * 11, 60)
                    elif contasalva == 2:
                        if not errore:
                            persalva = pygame.transform.scale(GlobalVarG2.perso, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            persSalvaBraccia = pygame.transform.scale(GlobalVarG2.persob, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            spasalva = pygame.transform.scale(GlobalVarG2.vetImgSpadePixellate[dati[6]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            arcsalva = pygame.transform.scale(GlobalVarG2.vetImgArchiPixellate[dati[128]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            armsalva = pygame.transform.scale(GlobalVarG2.vetImgArmaturePixellate[dati[8]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            scusalva = pygame.transform.scale(GlobalVarG2.vetImgScudiPixellate[dati[7]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            guasalva = pygame.transform.scale(GlobalVarG2.vetImgGuantiPixellate[dati[129]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            colsalva = pygame.transform.scale(GlobalVarG2.vetImgCollanePixellate[dati[130]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            messaggio("Livello: " + str(dati[4]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14.5, GlobalVarG2.gsy // 18 * 11, 60)
                            GlobalVarG2.schermo.blit(arcsalva, (GlobalVarG2.gpx * 15, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(persalva, (GlobalVarG2.gpx * 15, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(persSalvaBraccia, (GlobalVarG2.gpx * 15, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(armsalva, (GlobalVarG2.gpx * 15, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(colsalva, (GlobalVarG2.gpx * 15, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(spasalva, (GlobalVarG2.gpx * 15, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(guasalva, (GlobalVarG2.gpx * 15, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(scusalva, (GlobalVarG2.gpx * 15, GlobalVarG2.gpy * 12))
                        else:
                            messaggio("Dati corrotti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14.5, GlobalVarG2.gsy // 18 * 11, 60)
                    elif contasalva == 3:
                        if not errore:
                            persalva = pygame.transform.scale(GlobalVarG2.perso, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            persSalvaBraccia = pygame.transform.scale(GlobalVarG2.persob, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            spasalva = pygame.transform.scale(GlobalVarG2.vetImgSpadePixellate[dati[6]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            arcsalva = pygame.transform.scale(GlobalVarG2.vetImgArchiPixellate[dati[128]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            armsalva = pygame.transform.scale(GlobalVarG2.vetImgArmaturePixellate[dati[8]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            scusalva = pygame.transform.scale(GlobalVarG2.vetImgScudiPixellate[dati[7]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            guasalva = pygame.transform.scale(GlobalVarG2.vetImgGuantiPixellate[dati[129]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            colsalva = pygame.transform.scale(GlobalVarG2.vetImgCollanePixellate[dati[130]], (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                            messaggio("Livello: " + str(dati[4]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 21.5, GlobalVarG2.gsy // 18 * 11, 60)
                            GlobalVarG2.schermo.blit(arcsalva, (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(persalva, (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(persSalvaBraccia, (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(armsalva, (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(colsalva, (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(spasalva, (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(guasalva, (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(scusalva, (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 12))
                        else:
                            messaggio("Dati corrotti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 21.5, GlobalVarG2.gsy // 18 * 11, 60)
                contasalva = contasalva + 1
                leggi.close()

            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)


def menu():
    # video
    fermavideo = guardaVideo('Video/videoinizio')
    # attesa dopo video
    if not fermavideo:
        GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
        messaggio("Premi un tasto per continuare...", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 13, 100)
        pygame.display.update()
        finevideo = True
        while finevideo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                    finevideo = False

    xp = GlobalVarG2.gsx // 32 * 3
    yp = GlobalVarG2.gsy // 18 * 3.5
    voceMarcata = 1
    primoFrame = True
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    robomenuinizio = pygame.transform.scale(GlobalVarG2.robogra, (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))

    tastop = 0
    tastotempfps = 5

    # numero per la posizione di robo all'avvio
    c = random.randint(1, 4)

    while True:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(GlobalVarG2.c11)

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
            tastotempfps = 2

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
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)

                    # nuova partita
                    if voceMarcata == 1:
                        x = GlobalVarG2.gsx // 32 * 6
                        y = GlobalVarG2.gsy // 18 * 2
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
                        GlobalVarG2.canaleSoundCanzone.stop()
                        i = porteini
                        while i <= portefin:
                            dati[i + 1] = dati[i + 1] * GlobalVarG2.gpx
                            dati[i + 2] = dati[i + 2] * GlobalVarG2.gpy
                            i = i + 4
                        i = cofaniini
                        while i <= cofanifin:
                            dati[i + 1] = dati[i + 1] * GlobalVarG2.gpx
                            dati[i + 2] = dati[i + 2] * GlobalVarG2.gpy
                            i = i + 4
                        return dati, porteini, portefin, cofaniini, cofanifin

                    # carica partita
                    if voceMarcata == 2:
                        n = scegli_sal(1, lunghezzadati, GlobalVarG2.c11)

                        # lettura salvataggio
                        if n != -1:
                            leggi = open("Salvataggi/Salvataggio%i.txt" % n, "r")
                            leggifile = leggi.read()
                            dati = leggifile.split("_")
                            dati.pop(len(dati) - 1)
                            if len(dati) == 0:
                                print "Slot vuoto"
                                indietro = False
                                GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
                                robograsalva = pygame.transform.scale(GlobalVarG2.robograff, (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))
                                GlobalVarG2.schermo.blit(robograsalva, (GlobalVarG2.gpx * 3, -GlobalVarG2.gpy * 5))
                                messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
                                messaggio("Slot di salvataggio vuoto...", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 13, 100)
                                pygame.display.update()
                                while not indietro:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            quit()
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_q:
                                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
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
                                        dati[2] = dati[2] * GlobalVarG2.gpx
                                        dati[3] = dati[3] * GlobalVarG2.gpy
                                        i = porteini
                                        while i <= portefin:
                                            dati[i + 1] = dati[i + 1] * GlobalVarG2.gpx
                                            dati[i + 2] = dati[i + 2] * GlobalVarG2.gpy
                                            i = i + 4
                                        i = cofaniini
                                        while i <= cofanifin:
                                            dati[i + 1] = dati[i + 1] * GlobalVarG2.gpx
                                            dati[i + 2] = dati[i + 2] * GlobalVarG2.gpy
                                            i = i + 4

                                        print "Salvataggio: " + str(n)
                                        leggi.close()
                                        GlobalVarG2.canaleSoundCanzone.stop()
                                        return dati, porteini, portefin, cofaniini, cofanifin
                                if len(dati) != lunghezzadati or errore:
                                    print "Dati corrotti: " + str(len(dati))
                                    indietro = False
                                    GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
                                    robograsalva = pygame.transform.scale(GlobalVarG2.robograffff, (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))
                                    GlobalVarG2.schermo.blit(robograsalva, (GlobalVarG2.gpx * 15, -GlobalVarG2.gpy * 3))
                                    messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
                                    messaggio("I dati sono corrotti...", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 13, 100)
                                    pygame.display.update()
                                    while not indietro:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                quit()
                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_q:
                                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                                                    indietro = True
                            leggi.close()

                    # Impostazioni
                    if voceMarcata == 3:
                        menuImpostazioni(GlobalVarG2.c11, True)
                        primoFrame = True

                    # esci dal gioco
                    if voceMarcata == 4:
                        pygame.quit()
                        quit()
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_SPACE or ((tastop == pygame.K_s or tastop == pygame.K_w) and tastotempfps == 0) or primoFrame:
            if primoFrame:
                puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
                xp = GlobalVarG2.gsx // 32 * 3
                yp = GlobalVarG2.gsy // 18 * 3.5
                if voceMarcata == 3:
                    yp = GlobalVarG2.gsy // 18 * 8.5
                primoFrame = False
            if not primoMovimento and (tastop == pygame.K_s or tastop == pygame.K_w):
                tastotempfps = 2
            if tastop == pygame.K_s:
                if voceMarcata != 4:
                    if voceMarcata == 1:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 6
                    elif voceMarcata == 2:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 8.5
                    elif voceMarcata == 3:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 13.5
                    voceMarcata += 1
                else:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 3.5
                    voceMarcata -= 3
            if tastop == pygame.K_w:
                if voceMarcata != 1:
                    if voceMarcata == 2:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 3.5
                    elif voceMarcata == 3:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 6
                    elif voceMarcata == 4:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 8.5
                    voceMarcata -= 1
                else:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 13.5
                    voceMarcata += 3
            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            persomenuinizio = pygame.transform.scale(GlobalVarG2.persGrafInizio, (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))
            if (c == 1):
                robomenuinizio = pygame.transform.scale(GlobalVarG2.robogra, (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))
            if (c == 2):
                robomenuinizio = pygame.transform.scale(GlobalVarG2.robograf, (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))
            if (c == 3):
                robomenuinizio = pygame.transform.scale(GlobalVarG2.robograff, (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))
            if (c == 4):
                robomenuinizio = pygame.transform.scale(GlobalVarG2.robografff, (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))
            GlobalVarG2.schermo.blit(persomenuinizio, (GlobalVarG2.gpx * 15, 0))
            GlobalVarG2.schermo.blit(robomenuinizio, (GlobalVarG2.gpx * 3, 0))
            messaggio("Nuova partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 3, 90)
            messaggio("Carica partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 5.5, 90)
            messaggio("Impostazioni", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 8, 90)
            messaggio("Esci", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 13, 90)
            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)


def equip(dati, canzone):
    perssta = pygame.transform.scale(GlobalVarG2.perso, (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
    persstab = pygame.transform.scale(GlobalVarG2.persob, (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatorevecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    sfondoOggetto = pygame.transform.scale(GlobalVarG2.sfondoOggettoMenu, (int(GlobalVarG2.gpx * 2), int(GlobalVarG2.gpy * 2)))
    sconosciutoEquip = pygame.transform.scale(GlobalVarG2.sconosciutoEquipMenu, (int(GlobalVarG2.gpx * 2), int(GlobalVarG2.gpy * 2)))
    xp = GlobalVarG2.gsx // 32 * 1
    yp = GlobalVarG2.gsy // 18 * 6.8
    risposta = False
    voceMarcata = 1

    tastop = 0
    tastotempfps = 5

    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
    spada = pygame.transform.scale(GlobalVarG2.vetImgSpadePixellate[dati[6]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
    arco = pygame.transform.scale(GlobalVarG2.vetImgArchiPixellate[dati[128]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
    scudo = pygame.transform.scale(GlobalVarG2.vetImgScudiPixellate[dati[7]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
    armatura = pygame.transform.scale(GlobalVarG2.vetImgArmaturePixellate[dati[8]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
    guanti = pygame.transform.scale(GlobalVarG2.vetImgGuantiPixellate[dati[129]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
    collana = pygame.transform.scale(GlobalVarG2.vetImgCollanePixellate[dati[130]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
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
            vetImgSpade.append(GlobalVarG2.vetImgSpadeMenu[i])
        else:
            vetImgSpade.append(sconosciutoEquip)
        if dati[46 + i] > 0:
            vetImgArchi.append(GlobalVarG2.vetImgArchiMenu[i])
        else:
            vetImgArchi.append(sconosciutoEquip)
        if dati[51 + i] > 0:
            vetImgArmature.append(GlobalVarG2.vetImgArmatureMenu[i])
        else:
            vetImgArmature.append(sconosciutoEquip)
        if dati[56 + i] > 0:
            vetImgScudi.append(GlobalVarG2.vetImgScudiMenu[i])
        else:
            vetImgScudi.append(sconosciutoEquip)
        if dati[61 + i] > 0:
            vetImgGuanti.append(GlobalVarG2.vetImgGuantiMenu[i])
        else:
            vetImgGuanti.append(sconosciutoEquip)
        if dati[66 + i] > 0:
            vetImgCollane.append(GlobalVarG2.vetImgCollaneMenu[i])
        else:
            vetImgCollane.append(sconosciutoEquip)
        i += 1

    # primo frame
    if True:
        GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 21, GlobalVarG2.gsy // 18 * 12.5))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 21, GlobalVarG2.gsy // 18 * 4))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 21, GlobalVarG2.gsy // 18 * 15.5))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))
        # linea(dove,colore,inizio,fine,spessore)
        pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 4.5, (GlobalVarG2.gsy // 18 * 5.5) + (GlobalVarG2.gpy // 2)),
                         (GlobalVarG2.gsx // 32 * 4.5, (GlobalVarG2.gsy // 18 * 15) + (GlobalVarG2.gpy // 2)), GlobalVarG2.gpx // 30)
        pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 8, (GlobalVarG2.gsy // 18 * 4) + (GlobalVarG2.gpy // 2)),
                         (GlobalVarG2.gsx // 32 * 8, (GlobalVarG2.gsy // 18 * 15.5) + (GlobalVarG2.gpy // 2)), GlobalVarG2.gpx // 20)
        pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 11.5, (GlobalVarG2.gsy // 18 * 5.5) + (GlobalVarG2.gpy // 2)),
                         (GlobalVarG2.gsx // 32 * 11.5, (GlobalVarG2.gsy // 18 * 15) + (GlobalVarG2.gpy // 2)), GlobalVarG2.gpx // 30)
        pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 15, (GlobalVarG2.gsy // 18 * 4) + (GlobalVarG2.gpy // 2)),
                         (GlobalVarG2.gsx // 32 * 15, (GlobalVarG2.gsy // 18 * 15.5) + (GlobalVarG2.gpy // 2)), GlobalVarG2.gpx // 20)
        pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 18.5, (GlobalVarG2.gsy // 18 * 5.5) + (GlobalVarG2.gpy // 2)),
                         (GlobalVarG2.gsx // 32 * 18.5, (GlobalVarG2.gsy // 18 * 15) + (GlobalVarG2.gpy // 2)), GlobalVarG2.gpx // 30)

        if carim:
            spada = pygame.transform.scale(GlobalVarG2.vetImgSpadePixellate[dati[6]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
            arco = pygame.transform.scale(GlobalVarG2.vetImgArchiPixellate[dati[128]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
            scudo = pygame.transform.scale(GlobalVarG2.vetImgScudiPixellate[dati[7]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
            armatura = pygame.transform.scale(GlobalVarG2.vetImgArmaturePixellate[dati[8]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
            guanti = pygame.transform.scale(GlobalVarG2.vetImgGuantiPixellate[dati[129]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
            collana = pygame.transform.scale(GlobalVarG2.vetImgCollanePixellate[dati[130]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
            carim = False
        messaggio("Equipaggiamento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
        messaggio("Armi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 3.6, GlobalVarG2.gsy // 18 * 4.3, 60)
        messaggio("Spade", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 5.3, 50)
        i = 0
        while i < 5:
            GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 1.7, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
            GlobalVarG2.schermo.blit(vetImgSpade[i], (GlobalVarG2.gsx // 32 * 1.7, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
            i += 1
        messaggio("Archi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5.5, GlobalVarG2.gsy // 18 * 5.3, 50)
        i = 0
        while i < 5:
            GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 5.2, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
            GlobalVarG2.schermo.blit(vetImgArchi[i], (GlobalVarG2.gsx // 32 * 5.2, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
            i += 1
        messaggio("Protezioni", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.6, GlobalVarG2.gsy // 18 * 4.3, 60)
        messaggio("Armature", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 8.4, GlobalVarG2.gsy // 18 * 5.3, 50)
        i = 0
        while i < 5:
            GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 8.7, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
            GlobalVarG2.schermo.blit(vetImgArmature[i], (GlobalVarG2.gsx // 32 * 8.7, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
            i += 1
        messaggio("Scudi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 12.5, GlobalVarG2.gsy // 18 * 5.3, 50)
        i = 0
        while i < 5:
            GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 12.2, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
            GlobalVarG2.schermo.blit(vetImgScudi[i], (GlobalVarG2.gsx // 32 * 12.2, int((GlobalVarG2.gsy // 18 * 6) + (GlobalVarG2.gpy * 2 * i))))
            i += 1
        messaggio("Accessori", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.7, GlobalVarG2.gsy // 18 * 4.3, 60)
        messaggio("Guanti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 15.8, GlobalVarG2.gsy // 18 * 5.3, 50)
        i = 0
        while i < 5:
            GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 15.7, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
            GlobalVarG2.schermo.blit(vetImgGuanti[i], (GlobalVarG2.gsx // 32 * 15.7, int((GlobalVarG2.gsy // 18 * 6) + (GlobalVarG2.gpy * 2 * i))))
            i += 1
        messaggio("Collane", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19.2, GlobalVarG2.gsy // 18 * 5.3, 50)
        i = 0
        while i < 5:
            GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 19.2, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
            GlobalVarG2.schermo.blit(vetImgCollane[i], (GlobalVarG2.gsx // 32 * 19.2, ((GlobalVarG2.gsy // 18 * 6) + (GlobalVarG2.gpy * 2 * i))))
            i += 1

        esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
        if dati[5] > pvtot:
            dati[5] = pvtot

        GlobalVarG2.schermo.blit(arco, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
        GlobalVarG2.schermo.blit(perssta, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
        GlobalVarG2.schermo.blit(persstab, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
        GlobalVarG2.schermo.blit(armatura, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
        GlobalVarG2.schermo.blit(collana, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
        GlobalVarG2.schermo.blit(spada, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
        GlobalVarG2.schermo.blit(guanti, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
        GlobalVarG2.schermo.blit(scudo, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
        messaggio("Statistiche:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 6.7, 50)
        messaggio("Punti vita: %i" % pvtot, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 7.5, 35)
        messaggio("Attacco ravvicinato: %i" % attVicino, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 8, 35)
        messaggio("Attacco a distanza: %i" % attLontano, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 8.5, 35)
        messaggio("Difesa: %i" % dif, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 9, 35)
        messaggio(u"Probabilità parata: %i" % par + "%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 9.5, 35)
        # confronto statistiche
        # spade
        if voceMarcata == 1:
            if dati[41] != 0:
                messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Rimuovi spada", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diff = 0 - ((dati[6] * dati[6]) * 10)
                if dati[6] > 0:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
        if voceMarcata == 2:
            if dati[42] != 0:
                messaggio("Spada di ferro:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Semplice spada di ferro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diff = 10 - ((dati[6] * dati[6]) * 10)
                if dati[6] > 1:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                elif dati[6] < 1:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
        if voceMarcata == 3:
            if dati[43] != 0:
                messaggio("Spadone d'acciaio:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Grande spadone in acciaio con ornamenti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("in oro. Rappresenta il modello di spada", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("migliore mai prodotto dall'uomo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diff = 40 - ((dati[6] * dati[6]) * 10)
                if dati[6] > 2:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                elif dati[6] < 2:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
        if voceMarcata == 4:
            if dati[44] != 0:
                messaggio("Lykother:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Spada molto leggera e affilata. Si dice che in", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8,
                          35)
                messaggio("origine fosse un dente di un lupo enorme", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diff = 90 - ((dati[6] * dati[6]) * 10)
                if dati[6] > 3:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                elif dati[6] < 3:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
        if voceMarcata == 5:
            if dati[45] != 0:
                messaggio("Mendaxritas:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Potentissima spada composta da materiali", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("ignoti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diff = 160 - ((dati[6] * dati[6]) * 10)
                if dati[6] > 4:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                elif dati[6] < 4:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
        # archi
        if voceMarcata == 6:
            if dati[46] != 0:
                messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Rimuovi arco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diffAtt = 0 - ((dati[128] * dati[128]) * 10)
                if dati[128] > 0:
                    messaggio(str(diffAtt), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
        if voceMarcata == 7:
            if dati[47] != 0:
                messaggio("Arco di legno:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Semplice arco in legno usato dalla maggior", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("parte dei forestieri", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diffAtt = 5 - ((dati[128] * dati[128]) * 10)
                if dati[128] > 1:
                    messaggio(str(diffAtt), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                elif dati[128] < 1:
                    messaggio("+" + str(diffAtt), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
        if voceMarcata == 8:
            if dati[48] != 0:
                messaggio("Arco di ferro:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio(u"Elaborato arco in ferro usato solo dai più", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("esperti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diffAtt = 20 - ((dati[128] * dati[128]) * 10)
                if dati[128] > 2:
                    messaggio(str(diffAtt), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                elif dati[128] < 2:
                    messaggio("+" + str(diffAtt), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
        if voceMarcata == 9:
            if dati[49] != 0:
                messaggio("Arco di precisione:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Sofisticato arco in legno e acciaio. Molto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("leggero e potente. Massima espressione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("dell'ingegno umano", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diffAtt = 45 - ((dati[128] * dati[128]) * 10)
                if dati[128] > 3:
                    messaggio(str(diffAtt), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                elif dati[128] < 3:
                    messaggio("+" + str(diffAtt), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
        if voceMarcata == 10:
            if dati[50] != 0:
                messaggio("Accipiter:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Potentissimo arco di origine sconosciuta", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diffAtt = 80 - ((dati[128] * dati[128]) * 10)
                if dati[128] > 4:
                    messaggio(str(diffAtt), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                elif dati[128] < 4:
                    messaggio("+" + str(diffAtt), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
        # armature
        if voceMarcata == 11:
            if dati[51] != 0:
                messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Rimuovi armatura", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diff = 0 - ((dati[8] * dati[8]) * 10)
                if dati[8] > 0:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
        if voceMarcata == 12:
            if dati[52] != 0:
                messaggio("Armatura di pelle:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Semplice armatura in pelle", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diff = 10 - ((dati[8] * dati[8]) * 10)
                if dati[8] > 1:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                elif dati[8] < 1:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
        if voceMarcata == 13:
            if dati[53] != 0:
                messaggio("Armatura d'acciaio:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Grande armatura d'acciaio con ornamenti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("in oro. Usata solo dagli ufficiali", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("dell'esercito", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diff = 40 - ((dati[8] * dati[8]) * 10)
                if dati[8] > 2:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                elif dati[8] < 2:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
        if voceMarcata == 14:
            if dati[54] != 0:
                messaggio("Lykodes:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Armatura formata da materiali leggieri e", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("resistenti. Si dice essere composta da ossa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("di un enorme lupo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diff = 90 - ((dati[8] * dati[8]) * 10)
                if dati[8] > 3:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                elif dati[8] < 3:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
        if voceMarcata == 15:
            if dati[55] != 0:
                messaggio("Loriquam:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Armatura incredibilmente resistente.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio(u"La sua origine è ignota", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diff = 160 - ((dati[8] * dati[8]) * 10)
                if dati[8] > 4:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                elif dati[8] < 4:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
        # scudi
        if voceMarcata == 16:
            if dati[56] != 0:
                messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Rimuovi scudo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diff = 0 - ((dati[7] * dati[7]) * 5)
                if dati[7] > 0:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                diff = 0 - ((dati[7] * dati[7]) * 3)
                if dati[7] > 0:
                    messaggio(str(diff) + "%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
        if voceMarcata == 17:
            if dati[57] != 0:
                messaggio("Scudo di pelle:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Semplice scudo in pelle", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diff = 5 - ((dati[7] * dati[7]) * 5)
                if dati[7] > 1:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                elif dati[7] < 1:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                diff = 3 - ((dati[7] * dati[7]) * 3)
                if dati[7] > 1:
                    messaggio(str(diff) + "%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
                elif dati[7] < 1:
                    messaggio("+" + str(diff) + "%", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
        if voceMarcata == 18:
            if dati[58] != 0:
                messaggio("Scudo d'acciaio:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Sofisticato scudo in acciaio e oro. Studiato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8,
                          35)
                messaggio(u"per respingere gli attacchi più pesanti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diff = 20 - ((dati[7] * dati[7]) * 5)
                if dati[7] > 2:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                elif dati[7] < 2:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                diff = 12 - ((dati[7] * dati[7]) * 3)
                if dati[7] > 2:
                    messaggio(str(diff) + "%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
                elif dati[7] < 2:
                    messaggio("+" + str(diff) + "%", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
        if voceMarcata == 19:
            if dati[59] != 0:
                messaggio("Lykethmos:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Scudo molto leggere e resistente. Si dice", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio(u"essere composto dalle ossa più resistenti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("di un enorme lupo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diff = 45 - ((dati[7] * dati[7]) * 5)
                if dati[7] > 3:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                elif dati[7] < 3:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                diff = 27 - ((dati[7] * dati[7]) * 3)
                if dati[7] > 3:
                    messaggio(str(diff) + "%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
                elif dati[7] < 3:
                    messaggio("+" + str(diff) + "%", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
        if voceMarcata == 20:
            if dati[60] != 0:
                messaggio("Clipequam:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio(u"Scudo incredibilmente resistente. Non è ", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("nota l'origine", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                diff = 80 - ((dati[7] * dati[7]) * 5)
                if dati[7] > 4:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                elif dati[7] < 4:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                diff = 48 - ((dati[7] * dati[7]) * 3)
                if dati[7] > 4:
                    messaggio(str(diff) + "%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
                elif dati[7] < 4:
                    messaggio("+" + str(diff) + "%", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
        # guanti
        if voceMarcata == 21:
            if dati[61] != 0:
                messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Rimuovi guanti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                if dati[129] == 1:
                    messaggio("-50", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 7.5, 35)
                elif dati[129] == 2:
                    messaggio("-30", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                elif dati[129] == 3:
                    messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                    messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                elif dati[129] == 4:
                    messaggio("-10%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
        if voceMarcata == 22:
            if dati[62] != 0:
                messaggio("Guanti vitali:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Guanti che aumentano i punti vita massimi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("del portatore", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                if dati[129] != 1:
                    messaggio("+50", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 7.5, 35)
                if dati[129] == 2:
                    messaggio("-30", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                elif dati[129] == 3:
                    messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                    messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                elif dati[129] == 4:
                    messaggio("-10%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
        if voceMarcata == 23:
            if dati[63] != 0:
                messaggio("Guanti difensivi:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Guanti che consentono di subire meno danno", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("grazie ad una presa salda dello scudo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                if dati[129] != 2:
                    messaggio("+30", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                if dati[129] == 1:
                    messaggio("-50", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 7.5, 35)
                elif dati[129] == 3:
                    messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                    messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                elif dati[129] == 4:
                    messaggio("-10%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
        if voceMarcata == 24:
            if dati[64] != 0:
                messaggio("Guanti offensivi:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Guanti che consentono una presa salda", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("dell'arma. Aumentano l'attacco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                if dati[129] != 3:
                    messaggio("+20", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                    messaggio("+20", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                if dati[129] == 1:
                    messaggio("-50", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 7.5, 35)
                elif dati[129] == 2:
                    messaggio("-30", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                elif dati[129] == 4:
                    messaggio("-10%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
        if voceMarcata == 25:
            if dati[65] != 0:
                messaggio("Guanti confortevoli:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio(u"Guanti che aumentano la probabilità di", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("parare gli attacchi grazie ad una presa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("agevole dello scudo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                if dati[129] != 4:
                    messaggio("+10%", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
                if dati[129] == 1:
                    messaggio("-50", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 7.5, 35)
                elif dati[129] == 2:
                    messaggio("-30", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                elif dati[129] == 3:
                    messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                    messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
        # collane
        if voceMarcata == 26:
            if dati[66] != 0:
                messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Rimuovi collana", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
        if voceMarcata == 27:
            if dati[67] != 0:
                messaggio("Collana medicinale:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Collana composta da erbe il cui odore", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio(u"neutralizza la tissicità del veleno", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio(u"(non ha effetto se si è già avvelenati)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
        if voceMarcata == 28:
            if dati[68] != 0:
                messaggio("Collana rigenerante:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio("Collana composta da erbe il cui odore", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("ripristina punti vita ogni turno", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
        if voceMarcata == 29:
            if dati[69] != 0:
                messaggio("Apprendimaschera:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio(u"Collana che consente di ricevere più punti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                messaggio("esperienza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
        if voceMarcata == 30:
            if dati[70] != 0:
                messaggio("Portafortuna:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                messaggio(u"Collana che permette di ottenere più monete", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8,
                          35)
                messaggio("dai nemici", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)

        # puntatore vecchio
        if dati[6] == 0:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 6.8))
        if dati[6] == 1:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 8.8))
        if dati[6] == 2:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 10.8))
        if dati[6] == 3:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 12.8))
        if dati[6] == 4:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 14.8))
        if dati[128] == 0:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 4.5, GlobalVarG2.gsy // 18 * 6.8))
        if dati[128] == 1:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 4.5, GlobalVarG2.gsy // 18 * 8.8))
        if dati[128] == 2:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 4.5, GlobalVarG2.gsy // 18 * 10.8))
        if dati[128] == 3:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 4.5, GlobalVarG2.gsy // 18 * 12.8))
        if dati[128] == 4:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 4.5, GlobalVarG2.gsy // 18 * 14.8))
        if dati[8] == 0:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 6.8))
        if dati[8] == 1:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 8.8))
        if dati[8] == 2:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 10.8))
        if dati[8] == 3:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 12.8))
        if dati[8] == 4:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 14.8))
        if dati[7] == 0:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 6.8))
        if dati[7] == 1:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 8.8))
        if dati[7] == 2:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 10.8))
        if dati[7] == 3:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 12.8))
        if dati[7] == 4:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 14.8))
        if dati[129] == 0:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 6.8))
        if dati[129] == 1:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 8.8))
        if dati[129] == 2:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 10.8))
        if dati[129] == 3:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 12.8))
        if dati[129] == 4:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 14.8))
        if dati[130] == 0:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 18.5, GlobalVarG2.gsy // 18 * 6.8))
        if dati[130] == 1:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 18.5, GlobalVarG2.gsy // 18 * 8.8))
        if dati[130] == 2:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 18.5, GlobalVarG2.gsy // 18 * 10.8))
        if dati[130] == 3:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 18.5, GlobalVarG2.gsy // 18 * 12.8))
        if dati[130] == 4:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 18.5, GlobalVarG2.gsy // 18 * 14.8))

        messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
        GlobalVarG2.schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 2

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
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
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
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[6] = 0
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 2:
                        if dati[42] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[6] = 1
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 3:
                        if dati[43] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[6] = 2
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 4:
                        if dati[44] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[6] = 3
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 5:
                        if dati[45] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[6] = 4
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    # spade
                    if voceMarcata == 6:
                        if dati[46] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[128] = 0
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 7:
                        if dati[47] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[128] = 1
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 8:
                        if dati[48] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[128] = 2
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 9:
                        if dati[49] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[128] = 3
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 10:
                        if dati[50] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[128] = 4
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    # armature
                    if voceMarcata == 11:
                        if dati[51] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[8] = 0
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 12:
                        if dati[52] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[8] = 1
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 13:
                        if dati[53] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[8] = 2
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 14:
                        if dati[54] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[8] = 3
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 15:
                        if dati[55] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[8] = 4
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    # scudi
                    if voceMarcata == 16:
                        if dati[56] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[7] = 0
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 17:
                        if dati[57] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[7] = 1
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 18:
                        if dati[58] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[7] = 2
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 19:
                        if dati[59] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[7] = 3
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 20:
                        if dati[60] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[7] = 4
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    # guanti
                    if voceMarcata == 21:
                        if dati[61] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[129] = 0
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 22:
                        if dati[62] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[129] = 1
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 23:
                        if dati[63] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[129] = 2
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 24:
                        if dati[64] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[129] = 3
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 25:
                        if dati[65] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[129] = 4
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    # collane
                    if voceMarcata == 26:
                        if dati[66] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[130] = 0
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 27:
                        if dati[67] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[130] = 1
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 28:
                        if dati[68] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[130] = 2
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 29:
                        if dati[69] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[130] = 3
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 30:
                        if dati[70] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[130] = 4
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_q or tastop == pygame.K_SPACE or ((tastop == pygame.K_d or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_w) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_d or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_w):
                tastotempfps = 2
            if tastop == pygame.K_s:
                if voceMarcata == 5 or voceMarcata == 10 or voceMarcata == 15 or voceMarcata == 20 or voceMarcata == 25 or voceMarcata == 30:
                    voceMarcata -= 4
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 6.8
                else:
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp += GlobalVarG2.gsy // 18 * 2
            if tastop == pygame.K_w:
                if voceMarcata == 1 or voceMarcata == 6 or voceMarcata == 11 or voceMarcata == 16 or voceMarcata == 21 or voceMarcata == 26:
                    voceMarcata += 4
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 14.8
                else:
                    voceMarcata -= 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = yp - GlobalVarG2.gsy // 18 * 2
            if tastop == pygame.K_d:
                if voceMarcata == 26 or voceMarcata == 27 or voceMarcata == 28 or voceMarcata == 29 or voceMarcata == 30:
                    voceMarcata -= 25
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 1
                else:
                    voceMarcata += 5
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = xp + GlobalVarG2.gsx // 32 * 3.5
            if tastop == pygame.K_a:
                if voceMarcata == 1 or voceMarcata == 2 or voceMarcata == 3 or voceMarcata == 4 or voceMarcata == 5:
                    voceMarcata += 25
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 18.5
                else:
                    voceMarcata -= 5
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = xp - GlobalVarG2.gsx // 32 * 3.5
            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 21, GlobalVarG2.gsy // 18 * 12.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 21, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 21, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))
            # linea(dove,colore,inizio,fine,spessore)
            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 4.5, (GlobalVarG2.gsy // 18 * 5.5) + (GlobalVarG2.gpy // 2)), (GlobalVarG2.gsx // 32 * 4.5, (GlobalVarG2.gsy // 18 * 15) + (GlobalVarG2.gpy // 2)), GlobalVarG2.gpx // 30)
            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 8, (GlobalVarG2.gsy // 18 * 4) + (GlobalVarG2.gpy // 2)), (GlobalVarG2.gsx // 32 * 8, (GlobalVarG2.gsy // 18 * 15.5) + (GlobalVarG2.gpy // 2)), GlobalVarG2.gpx // 20)
            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 11.5, (GlobalVarG2.gsy // 18 * 5.5) + (GlobalVarG2.gpy // 2)), (GlobalVarG2.gsx // 32 * 11.5, (GlobalVarG2.gsy // 18 * 15) + (GlobalVarG2.gpy // 2)), GlobalVarG2.gpx // 30)
            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 15, (GlobalVarG2.gsy // 18 * 4) + (GlobalVarG2.gpy // 2)), (GlobalVarG2.gsx // 32 * 15, (GlobalVarG2.gsy // 18 * 15.5) + (GlobalVarG2.gpy // 2)), GlobalVarG2.gpx // 20)
            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 18.5, (GlobalVarG2.gsy // 18 * 5.5) + (GlobalVarG2.gpy // 2)), (GlobalVarG2.gsx // 32 * 18.5, (GlobalVarG2.gsy // 18 * 15) + (GlobalVarG2.gpy // 2)), GlobalVarG2.gpx // 30)

            if carim:
                spada = pygame.transform.scale(GlobalVarG2.vetImgSpadePixellate[dati[6]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
                arco = pygame.transform.scale(GlobalVarG2.vetImgArchiPixellate[dati[128]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
                scudo = pygame.transform.scale(GlobalVarG2.vetImgScudiPixellate[dati[7]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
                armatura = pygame.transform.scale(GlobalVarG2.vetImgArmaturePixellate[dati[8]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
                guanti = pygame.transform.scale(GlobalVarG2.vetImgGuantiPixellate[dati[129]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
                collana = pygame.transform.scale(GlobalVarG2.vetImgCollanePixellate[dati[130]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
                carim = False
            messaggio("Equipaggiamento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
            messaggio("Armi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 3.6, GlobalVarG2.gsy // 18 * 4.3, 60)
            messaggio("Spade", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 1.7, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                GlobalVarG2.schermo.blit(vetImgSpade[i], (GlobalVarG2.gsx // 32 * 1.7, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                i += 1
            messaggio("Archi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5.5, GlobalVarG2.gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 5.2, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                GlobalVarG2.schermo.blit(vetImgArchi[i], (GlobalVarG2.gsx // 32 * 5.2, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                i += 1
            messaggio("Protezioni", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.6, GlobalVarG2.gsy // 18 * 4.3, 60)
            messaggio("Armature", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 8.4, GlobalVarG2.gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 8.7, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                GlobalVarG2.schermo.blit(vetImgArmature[i], (GlobalVarG2.gsx // 32 * 8.7, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                i += 1
            messaggio("Scudi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 12.5, GlobalVarG2.gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 12.2, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                GlobalVarG2.schermo.blit(vetImgScudi[i], (GlobalVarG2.gsx // 32 * 12.2, int((GlobalVarG2.gsy // 18 * 6) + (GlobalVarG2.gpy * 2 * i))))
                i += 1
            messaggio("Accessori", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.7, GlobalVarG2.gsy // 18 * 4.3, 60)
            messaggio("Guanti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 15.8, GlobalVarG2.gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 15.7, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                GlobalVarG2.schermo.blit(vetImgGuanti[i], (GlobalVarG2.gsx // 32 * 15.7, int((GlobalVarG2.gsy // 18 * 6) + (GlobalVarG2.gpy * 2 * i))))
                i += 1
            messaggio("Collane", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19.2, GlobalVarG2.gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 19.2, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                GlobalVarG2.schermo.blit(vetImgCollane[i], (GlobalVarG2.gsx // 32 * 19.2, ((GlobalVarG2.gsy // 18 * 6) + (GlobalVarG2.gpy * 2 * i))))
                i += 1

            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
            if dati[5] > pvtot:
                dati[5] = pvtot

            GlobalVarG2.schermo.blit(arco, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
            GlobalVarG2.schermo.blit(perssta, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
            GlobalVarG2.schermo.blit(persstab, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
            GlobalVarG2.schermo.blit(armatura, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
            GlobalVarG2.schermo.blit(collana, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
            GlobalVarG2.schermo.blit(spada, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
            GlobalVarG2.schermo.blit(guanti, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
            GlobalVarG2.schermo.blit(scudo, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
            messaggio("Statistiche:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 6.7, 50)
            messaggio("Punti vita: %i" % pvtot, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 7.5, 35)
            messaggio("Attacco ravvicinato: %i" % attVicino, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 8, 35)
            messaggio("Attacco a distanza: %i" % attLontano, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 8.5, 35)
            messaggio("Difesa: %i" % dif, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 9, 35)
            messaggio(u"Probabilità parata: %i" % par + "%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 9.5, 35)
            # confronto statistiche
            # spade
            if voceMarcata == 1:
                if dati[41] != 0:
                    messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi spada", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 0 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 0:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
            if voceMarcata == 2:
                if dati[42] != 0:
                    messaggio("Spada di ferro:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Semplice spada di ferro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 10 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 1:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                    elif dati[6] < 1:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
            if voceMarcata == 3:
                if dati[43] != 0:
                    messaggio("Spadone d'acciaio:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Grande spadone in acciaio con ornamenti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("in oro. Rappresenta il modello di spada", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("migliore mai prodotto dall'uomo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 40 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 2:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                    elif dati[6] < 2:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
            if voceMarcata == 4:
                if dati[44] != 0:
                    messaggio("Lykother:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Spada molto leggera e affilata. Si dice che in", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("origine fosse un dente di un lupo enorme", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 90 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 3:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                    elif dati[6] < 3:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
            if voceMarcata == 5:
                if dati[45] != 0:
                    messaggio("Mendaxritas:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Potentissima spada composta da materiali", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("ignoti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 160 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 4:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                    elif dati[6] < 4:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
            # archi
            if voceMarcata == 6:
                if dati[46] != 0:
                    messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi arco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diffAtt = 0 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 0:
                        messaggio(str(diffAtt), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
            if voceMarcata == 7:
                if dati[47] != 0:
                    messaggio("Arco di legno:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Semplice arco in legno usato dalla maggior", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("parte dei forestieri", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diffAtt = 5 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 1:
                        messaggio(str(diffAtt), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[128] < 1:
                        messaggio("+" + str(diffAtt), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
            if voceMarcata == 8:
                if dati[48] != 0:
                    messaggio("Arco di ferro:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio(u"Elaborato arco in ferro usato solo dai più", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("esperti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diffAtt = 20 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 2:
                        messaggio(str(diffAtt), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[128] < 2:
                        messaggio("+" + str(diffAtt), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
            if voceMarcata == 9:
                if dati[49] != 0:
                    messaggio("Arco di precisione:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Sofisticato arco in legno e acciaio. Molto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("leggero e potente. Massima espressione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("dell'ingegno umano", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diffAtt = 45 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 3:
                        messaggio(str(diffAtt), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[128] < 3:
                        messaggio("+" + str(diffAtt), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
            if voceMarcata == 10:
                if dati[50] != 0:
                    messaggio("Accipiter:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Potentissimo arco di origine sconosciuta", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diffAtt = 80 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 4:
                        messaggio(str(diffAtt), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[128] < 4:
                        messaggio("+" + str(diffAtt), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
            # armature
            if voceMarcata == 11:
                if dati[51] != 0:
                    messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi armatura", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 0 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 0:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            if voceMarcata == 12:
                if dati[52] != 0:
                    messaggio("Armatura di pelle:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Semplice armatura in pelle", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 10 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 1:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[8] < 1:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            if voceMarcata == 13:
                if dati[53] != 0:
                    messaggio("Armatura d'acciaio:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Grande armatura d'acciaio con ornamenti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("in oro. Usata solo dagli ufficiali", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("dell'esercito", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 40 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 2:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[8] < 2:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            if voceMarcata == 14:
                if dati[54] != 0:
                    messaggio("Lykodes:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Armatura formata da materiali leggieri e", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("resistenti. Si dice essere composta da ossa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("di un enorme lupo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 90 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 3:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[8] < 3:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            if voceMarcata == 15:
                if dati[55] != 0:
                    messaggio("Loriquam:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Armatura incredibilmente resistente.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio(u"La sua origine è ignota", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 160 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 4:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[8] < 4:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            # scudi
            if voceMarcata == 16:
                if dati[56] != 0:
                    messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi scudo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 0 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 0:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    diff = 0 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 0:
                        messaggio(str(diff) + "%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            if voceMarcata == 17:
                if dati[57] != 0:
                    messaggio("Scudo di pelle:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Semplice scudo in pelle", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 5 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 1:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[7] < 1:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    diff = 3 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 1:
                        messaggio(str(diff) + "%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
                    elif dati[7] < 1:
                        messaggio("+" + str(diff) + "%", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            if voceMarcata == 18:
                if dati[58] != 0:
                    messaggio("Scudo d'acciaio:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Sofisticato scudo in acciaio e oro. Studiato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio(u"per respingere gli attacchi più pesanti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 20 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 2:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[7] < 2:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    diff = 12 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 2:
                        messaggio(str(diff) + "%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
                    elif dati[7] < 2:
                        messaggio("+" + str(diff) + "%", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            if voceMarcata == 19:
                if dati[59] != 0:
                    messaggio("Lykethmos:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Scudo molto leggere e resistente. Si dice", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio(u"essere composto dalle ossa più resistenti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("di un enorme lupo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 45 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 3:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[7] < 3:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    diff = 27 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 3:
                        messaggio(str(diff) + "%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
                    elif dati[7] < 3:
                        messaggio("+" + str(diff) + "%", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            if voceMarcata == 20:
                if dati[60] != 0:
                    messaggio("Clipequam:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio(u"Scudo incredibilmente resistente. Non è ", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("nota l'origine", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 80 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 4:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[7] < 4:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    diff = 48 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 4:
                        messaggio(str(diff) + "%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
                    elif dati[7] < 4:
                        messaggio("+" + str(diff) + "%", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            # guanti
            if voceMarcata == 21:
                if dati[61] != 0:
                    messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi guanti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    if dati[129] == 1:
                        messaggio("-50", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 7.5, 35)
                    elif dati[129] == 2:
                        messaggio("-30", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[129] == 3:
                        messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                        messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[129] == 4:
                        messaggio("-10%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            if voceMarcata == 22:
                if dati[62] != 0:
                    messaggio("Guanti vitali:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Guanti che aumentano i punti vita massimi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("del portatore", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    if dati[129] != 1:
                        messaggio("+50", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 7.5, 35)
                    if dati[129] == 2:
                        messaggio("-30", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[129] == 3:
                        messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                        messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[129] == 4:
                        messaggio("-10%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            if voceMarcata == 23:
                if dati[63] != 0:
                    messaggio("Guanti difensivi:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Guanti che consentono di subire meno danno", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("grazie ad una presa salda dello scudo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    if dati[129] != 2:
                        messaggio("+30", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    if dati[129] == 1:
                        messaggio("-50", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 7.5, 35)
                    elif dati[129] == 3:
                        messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                        messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[129] == 4:
                        messaggio("-10%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            if voceMarcata == 24:
                if dati[64] != 0:
                    messaggio("Guanti offensivi:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Guanti che consentono una presa salda", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("dell'arma. Aumentano l'attacco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    if dati[129] != 3:
                        messaggio("+20", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                        messaggio("+20", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    if dati[129] == 1:
                        messaggio("-50", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 7.5, 35)
                    elif dati[129] == 2:
                        messaggio("-30", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[129] == 4:
                        messaggio("-10%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            if voceMarcata == 25:
                if dati[65] != 0:
                    messaggio("Guanti confortevoli:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio(u"Guanti che aumentano la probabilità di", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("parare gli attacchi grazie ad una presa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("agevole dello scudo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    if dati[129] != 4:
                        messaggio("+10%", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
                    if dati[129] == 1:
                        messaggio("-50", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 7.5, 35)
                    elif dati[129] == 2:
                        messaggio("-30", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[129] == 3:
                        messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                        messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
            # collane
            if voceMarcata == 26:
                if dati[66] != 0:
                    messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi collana", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
            if voceMarcata == 27:
                if dati[67] != 0:
                    messaggio("Collana medicinale:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Collana composta da erbe il cui odore", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio(u"neutralizza la tissicità del veleno", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio(u"(non ha effetto se si è già avvelenati)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
            if voceMarcata == 28:
                if dati[68] != 0:
                    messaggio("Collana rigenerante:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Collana composta da erbe il cui odore", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("ripristina punti vita ogni turno", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
            if voceMarcata == 29:
                if dati[69] != 0:
                    messaggio("Apprendimaschera:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio(u"Collana che consente di ricevere più punti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("esperienza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
            if voceMarcata == 30:
                if dati[70] != 0:
                    messaggio("Portafortuna:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio(u"Collana che permette di ottenere più monete", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("dai nemici", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)

            # puntatore vecchio
            if dati[6] == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 6.8))
            if dati[6] == 1:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 8.8))
            if dati[6] == 2:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 10.8))
            if dati[6] == 3:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 12.8))
            if dati[6] == 4:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 14.8))
            if dati[128] == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 4.5, GlobalVarG2.gsy // 18 * 6.8))
            if dati[128] == 1:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 4.5, GlobalVarG2.gsy // 18 * 8.8))
            if dati[128] == 2:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 4.5, GlobalVarG2.gsy // 18 * 10.8))
            if dati[128] == 3:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 4.5, GlobalVarG2.gsy // 18 * 12.8))
            if dati[128] == 4:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 4.5, GlobalVarG2.gsy // 18 * 14.8))
            if dati[8] == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 6.8))
            if dati[8] == 1:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 8.8))
            if dati[8] == 2:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 10.8))
            if dati[8] == 3:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 12.8))
            if dati[8] == 4:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 14.8))
            if dati[7] == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 6.8))
            if dati[7] == 1:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 8.8))
            if dati[7] == 2:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 10.8))
            if dati[7] == 3:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 12.8))
            if dati[7] == 4:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 14.8))
            if dati[129] == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 6.8))
            if dati[129] == 1:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 8.8))
            if dati[129] == 2:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 10.8))
            if dati[129] == 3:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 12.8))
            if dati[129] == 4:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 14.8))
            if dati[130] == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 18.5, GlobalVarG2.gsy // 18 * 6.8))
            if dati[130] == 1:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 18.5, GlobalVarG2.gsy // 18 * 8.8))
            if dati[130] == 2:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 18.5, GlobalVarG2.gsy // 18 * 10.8))
            if dati[130] == 3:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 18.5, GlobalVarG2.gsy // 18 * 12.8))
            if dati[130] == 4:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 18.5, GlobalVarG2.gsy // 18 * 14.8))

            messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)
    return dati


def sceglicondiz(dati, condizione, canzone):
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatorevecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    xp = GlobalVarG2.gsx // 32 * 1
    yp = GlobalVarG2.gsy // 18 * 4.6
    risposta = False
    voceMarcata = 0

    tastop = 0
    tastotempfps = 5

    # carico le scenette
    scecond = GlobalVarG2.vetImgCondizioniMenu

    # primo frame
    if True:
        GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 12.5))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 4))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 15.5))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))

        messaggio("Scegli condizione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
        messaggio("Cancella", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 4.7, 45)
        if voceMarcata == 0:
            messaggio("Cancella:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
            messaggio("Cancella il settaggio di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
            messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
            messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        if dati[81] > 0:
            messaggio("Rallo con pv < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.2, 40)
            if voceMarcata == 1:
                GlobalVarG2.schermo.blit(scecond[1], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Rallo con pv < 80%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su Rallo quando ha pv < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5,
                          35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.2, 40)
        if dati[82] > 0:
            messaggio("Rallo con pv < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7.2, 40)
            if voceMarcata == 2:
                GlobalVarG2.schermo.blit(scecond[2], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Rallo con pv < 50%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su Rallo quando ha pv < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5,
                          35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7.2, 40)
        if dati[83] > 0:
            messaggio("Rallo con pv < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8.2, 40)
            if voceMarcata == 3:
                GlobalVarG2.schermo.blit(scecond[3], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Rallo con pv < 30%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su Rallo quando ha pv < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5,
                          35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8.2, 40)
        if dati[84] > 0:
            messaggio("Rallo con veleno", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9.2, 40)
            if voceMarcata == 4:
                GlobalVarG2.schermo.blit(scecond[4], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Rallo con veleno:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio(u"Esegue l'azione su Rallo quando è avvelenato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5,
                          35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9.2, 40)
        if dati[85] > 0:
            messaggio("Colco surriscaldato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10.2, 40)
            if voceMarcata == 5:
                GlobalVarG2.schermo.blit(scecond[5], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Colco surriscaldato:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio(u"Esegue l'azione su Colco quando è surriscaldato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18,
                          GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10.2, 40)
        if dati[86] > 0:
            messaggio("Colco con pe < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11.2, 40)
            if voceMarcata == 6:
                GlobalVarG2.schermo.blit(scecond[6], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Colco con pe < 80%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su Colco quando ha pe < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5,
                          35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11.2, 40)
        if dati[87] > 0:
            messaggio("Colco con pe < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12.2, 40)
            if voceMarcata == 7:
                GlobalVarG2.schermo.blit(scecond[7], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Colco con pe < 50%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su Colco quando ha pe < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5,
                          35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12.2, 40)
        if dati[88] > 0:
            messaggio("Colco con pe < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13.2, 40)
            if voceMarcata == 8:
                GlobalVarG2.schermo.blit(scecond[8], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Colco con pe < 30%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su Colco quando ha pe < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5,
                          35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13.2, 40)
        if dati[89] > 0:
            messaggio("Sempre a Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14.2, 40)
            if voceMarcata == 9:
                GlobalVarG2.schermo.blit(scecond[9], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Sempre a Rallo:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su Rallo in continuazione (se la tecnica associata", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("comporta uno status alterativo, viene eseguita solo se lo status non", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio(u"è attivo)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14.2, 40)
        if dati[90] > 0:
            messaggio("Sempre a Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15.2, 40)
            if voceMarcata == 10:
                GlobalVarG2.schermo.blit(scecond[10], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Sempre a Colco:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su Colco in continuazione (se la tecnica associata", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("comporta uno status alterativo, viene eseguita solo se lo status non", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio(u"è attivo)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15.2, 40)
        if dati[91] > 0:
            messaggio("Nemico a caso", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 6.2, 40)
            if voceMarcata == 11:
                GlobalVarG2.schermo.blit(scecond[11], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Nemico a caso:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su un nemico a caso", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 6.2, 40)
        if dati[92] > 0:
            messaggio("Nemico vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 7.2, 40)
            if voceMarcata == 12:
                GlobalVarG2.schermo.blit(scecond[12], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Nemico vicino:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio(u"Esegue l'azione sul nemico più vicino a Colco nel raggio di 2 caselle", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 7.2, 40)
        if dati[93] > 0:
            messaggio("Nemico lontano", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 8.2, 40)
            if voceMarcata == 13:
                GlobalVarG2.schermo.blit(scecond[13], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Nemico lontano:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio(u"Esegue l'azione sul nemico lontano (distante di 3 o più caselle) più", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("vicino a Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 8.2, 40)
        if dati[94] > 0:
            messaggio("Nemico con pv < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 9.2, 40)
            if voceMarcata == 14:
                GlobalVarG2.schermo.blit(scecond[14], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Nemico con pv < 80%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su un nemico con pv < 80% (in caso di molteplici bersagli,", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio(u"esegue l'azione su quello più vicino a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15,
                          35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 9.2, 40)
        if dati[95] > 0:
            messaggio("Nemico con pv < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 10.2, 40)
            if voceMarcata == 15:
                GlobalVarG2.schermo.blit(scecond[15], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Nemico con pv < 50%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su un nemico con pv < 50% (in caso di molteplici bersagli,", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio(u"esegue l'azione su quello più vicino a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15,
                          35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 10.2, 40)
        if dati[96] > 0:
            messaggio("Nemico con pv < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 11.2, 40)
            if voceMarcata == 16:
                GlobalVarG2.schermo.blit(scecond[16], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Nemico con pv < 30%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione su un nemico con pv < 30% (in caso di molteplici bersagli,", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio(u"esegue l'azione su quello più vicino a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15,
                          35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 11.2, 40)
        if dati[97] > 0:
            messaggio("Nemico con meno pv", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 12.2, 40)
            if voceMarcata == 17:
                GlobalVarG2.schermo.blit(scecond[17], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Nemico con meno pv:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Esegue l'azione sul nemico con meno pv (in caso di molteplici bersagli,", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio(u"esegue l'azione su quello più vicino a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15,
                          35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 12.2, 40)
        if dati[98] > 0:
            messaggio("Numero di nemici > 1", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 13.2, 40)
            if voceMarcata == 18:
                GlobalVarG2.schermo.blit(scecond[18], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Numero di nemici > 1:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio(u"Esegue l'azione quando nei paraggi c'è più di 1 nemico (in caso di", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio(u"tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 13.2, 40)
        if dati[99] > 0:
            messaggio("Numero di nemici > 4", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 14.2, 40)
            if voceMarcata == 19:
                GlobalVarG2.schermo.blit(scecond[19], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Numero di nemici > 4:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio(u"Esegue l'azione quando nei paraggi ci sono più di 4 nemici (in caso di", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio(u"tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 14.2, 40)
        if dati[100] > 0:
            messaggio("Numero di nemici > 7", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 15.2, 40)
            if voceMarcata == 20:
                GlobalVarG2.schermo.blit(scecond[20], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Numero di nemici > 7:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio(u"Esegue l'azione quando nei paraggi ci sono più di 7 nemici (in caso di", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio(u"tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 15.2, 40)

        messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)

        # puntatore vecchio
        i = 1
        k = 6.1
        while i <= 10:
            if condizione == i:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * k))
            i = i + 1
            k = k + 1
        i = 11
        k = 6.1
        while i <= 20:
            if condizione == i:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * k))
            i = i + 1
            k = k + 1
        if condizione == 0:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4.6))

        GlobalVarG2.schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 2

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
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
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
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                return c
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        i += 1
                        c += 1
                    if voceMarcata == 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        return 0
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_SPACE or ((tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w:
                if voceMarcata == 1 or voceMarcata == 11:
                    if voceMarcata == 1:
                        voceMarcata -= 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = yp - GlobalVarG2.gsy // 18 * 1.5
                        xp = GlobalVarG2.gsx // 32 * 1
                    else:
                        voceMarcata += 9
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 15.1
                else:
                    if voceMarcata != 0:
                        voceMarcata -= 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = yp - GlobalVarG2.gsy // 18 * 1
                    else:
                        voceMarcata += 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 15.1
            if tastop == pygame.K_a:
                if voceMarcata != 0:
                    if 11 <= voceMarcata <= 20:
                        voceMarcata -= 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = xp - GlobalVarG2.gsx // 32 * 7
                    else:
                        voceMarcata += 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 8
            if tastop == pygame.K_s:
                if voceMarcata == 0:
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = yp + GlobalVarG2.gsy // 18 * 1.5
                else:
                    if voceMarcata == 10 or voceMarcata == 20:
                        if voceMarcata == 10:
                            voceMarcata -= 10
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = GlobalVarG2.gsy // 18 * 4.6
                            xp = GlobalVarG2.gsx // 32 * 1
                        else:
                            voceMarcata -= 9
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = GlobalVarG2.gsy // 18 * 6.1
                    else:
                        voceMarcata += 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = yp + GlobalVarG2.gsy // 18 * 1
            if tastop == pygame.K_d:
                if voceMarcata != 0:
                    if 1 <= voceMarcata <= 10:
                        voceMarcata += 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = xp + GlobalVarG2.gsx // 32 * 7
                    else:
                        voceMarcata -= 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 1
            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 12.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))

            messaggio("Scegli condizione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
            messaggio("Cancella", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 4.7, 45)
            if voceMarcata == 0:
                messaggio("Cancella:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Cancella il settaggio di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            if dati[81] > 0:
                messaggio("Rallo con pv < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.2, 40)
                if voceMarcata == 1:
                    GlobalVarG2.schermo.blit(scecond[1], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Rallo con pv < 80%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Rallo quando ha pv < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.2, 40)
            if dati[82] > 0:
                messaggio("Rallo con pv < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7.2, 40)
                if voceMarcata == 2:
                    GlobalVarG2.schermo.blit(scecond[2], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Rallo con pv < 50%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Rallo quando ha pv < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7.2, 40)
            if dati[83] > 0:
                messaggio("Rallo con pv < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8.2, 40)
                if voceMarcata == 3:
                    GlobalVarG2.schermo.blit(scecond[3], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Rallo con pv < 30%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Rallo quando ha pv < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8.2, 40)
            if dati[84] > 0:
                messaggio("Rallo con veleno", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9.2, 40)
                if voceMarcata == 4:
                    GlobalVarG2.schermo.blit(scecond[4], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Rallo con veleno:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione su Rallo quando è avvelenato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9.2, 40)
            if dati[85] > 0:
                messaggio("Colco surriscaldato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10.2, 40)
                if voceMarcata == 5:
                    GlobalVarG2.schermo.blit(scecond[5], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Colco surriscaldato:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione su Colco quando è surriscaldato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10.2, 40)
            if dati[86] > 0:
                messaggio("Colco con pe < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11.2, 40)
                if voceMarcata == 6:
                    GlobalVarG2.schermo.blit(scecond[6], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Colco con pe < 80%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Colco quando ha pe < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11.2, 40)
            if dati[87] > 0:
                messaggio("Colco con pe < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12.2, 40)
                if voceMarcata == 7:
                    GlobalVarG2.schermo.blit(scecond[7], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Colco con pe < 50%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Colco quando ha pe < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12.2, 40)
            if dati[88] > 0:
                messaggio("Colco con pe < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13.2, 40)
                if voceMarcata == 8:
                    GlobalVarG2.schermo.blit(scecond[8], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Colco con pe < 30%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Colco quando ha pe < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13.2, 40)
            if dati[89] > 0:
                messaggio("Sempre a Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14.2, 40)
                if voceMarcata == 9:
                    GlobalVarG2.schermo.blit(scecond[9], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Sempre a Rallo:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Rallo in continuazione (se la tecnica associata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("comporta uno status alterativo, viene eseguita solo se lo status non", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio(u"è attivo)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14.2, 40)
            if dati[90] > 0:
                messaggio("Sempre a Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15.2, 40)
                if voceMarcata == 10:
                    GlobalVarG2.schermo.blit(scecond[10], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Sempre a Colco:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Colco in continuazione (se la tecnica associata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("comporta uno status alterativo, viene eseguita solo se lo status non", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio(u"è attivo)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15.2, 40)
            if dati[91] > 0:
                messaggio("Nemico a caso", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 6.2, 40)
                if voceMarcata == 11:
                    GlobalVarG2.schermo.blit(scecond[11], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Nemico a caso:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su un nemico a caso", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 6.2, 40)
            if dati[92] > 0:
                messaggio("Nemico vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 7.2, 40)
                if voceMarcata == 12:
                    GlobalVarG2.schermo.blit(scecond[12], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Nemico vicino:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione sul nemico più vicino a Colco nel raggio di 2 caselle", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 7.2, 40)
            if dati[93] > 0:
                messaggio("Nemico lontano", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 8.2, 40)
                if voceMarcata == 13:
                    GlobalVarG2.schermo.blit(scecond[13], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Nemico lontano:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione sul nemico lontano (distante di 3 o più caselle) più", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("vicino a Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 8.2, 40)
            if dati[94] > 0:
                messaggio("Nemico con pv < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 9.2, 40)
                if voceMarcata == 14:
                    GlobalVarG2.schermo.blit(scecond[14], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Nemico con pv < 80%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su un nemico con pv < 80% (in caso di molteplici bersagli,", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio(u"esegue l'azione su quello più vicino a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 9.2, 40)
            if dati[95] > 0:
                messaggio("Nemico con pv < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 10.2, 40)
                if voceMarcata == 15:
                    GlobalVarG2.schermo.blit(scecond[15], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Nemico con pv < 50%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su un nemico con pv < 50% (in caso di molteplici bersagli,", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio(u"esegue l'azione su quello più vicino a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 10.2, 40)
            if dati[96] > 0:
                messaggio("Nemico con pv < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 11.2, 40)
                if voceMarcata == 16:
                    GlobalVarG2.schermo.blit(scecond[16], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Nemico con pv < 30%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su un nemico con pv < 30% (in caso di molteplici bersagli,", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio(u"esegue l'azione su quello più vicino a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 11.2, 40)
            if dati[97] > 0:
                messaggio("Nemico con meno pv", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 12.2, 40)
                if voceMarcata == 17:
                    GlobalVarG2.schermo.blit(scecond[17], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Nemico con meno pv:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione sul nemico con meno pv (in caso di molteplici bersagli,", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio(u"esegue l'azione su quello più vicino a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 12.2, 40)
            if dati[98] > 0:
                messaggio("Numero di nemici > 1", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 13.2, 40)
                if voceMarcata == 18:
                    GlobalVarG2.schermo.blit(scecond[18], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Numero di nemici > 1:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione quando nei paraggi c'è più di 1 nemico (in caso di", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio(u"tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 13.2, 40)
            if dati[99] > 0:
                messaggio("Numero di nemici > 4", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 14.2, 40)
                if voceMarcata == 19:
                    GlobalVarG2.schermo.blit(scecond[19], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Numero di nemici > 4:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione quando nei paraggi ci sono più di 4 nemici (in caso di", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio(u"tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 14.2, 40)
            if dati[100] > 0:
                messaggio("Numero di nemici > 7", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 15.2, 40)
                if voceMarcata == 20:
                    GlobalVarG2.schermo.blit(scecond[20], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Numero di nemici > 7:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione quando nei paraggi ci sono più di 7 nemici (in caso di", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio(u"tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 15.2, 40)

            messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)

            # puntatore vecchio
            i = 1
            k = 6.1
            while i <= 10:
                if condizione == i:
                    GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * k))
                i = i + 1
                k = k + 1
            i = 11
            k = 6.1
            while i <= 20:
                if condizione == i:
                    GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * k))
                i = i + 1
                k = k + 1
            if condizione == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4.6))

            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)
    return condizione


def sceglitecn(dati, tecnica, canzone):
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatorevecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    xp = GlobalVarG2.gsx // 32 * 1
    yp = GlobalVarG2.gsy // 18 * 4.6
    risposta = False
    voceMarcata = 0

    tastop = 0
    tastotempfps = 5

    # carico le scenette
    scetecn = GlobalVarG2.vetImgTecnicheMenu

    # primo frame
    if True:
        GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
        # rettangolo(dove,colore,(posizionex,posizioney,larghezza,altezza,spessore))
        pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 12.5))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 4))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 15.5))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))

        messaggio("Scegli tecnica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
        messaggio("Cancella", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 4.7, 45)
        if voceMarcata == 0:
            messaggio("Cancella:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
            messaggio("Cancella il settaggio di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
            messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
            messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        if dati[11] > 0:
            messaggio("Scossa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.2, 40)
            if voceMarcata == 1:
                GlobalVarG2.schermo.blit(scetecn[1], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Scossa:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[0]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("Infligge danni a un nemico vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.2, 40)
        if dati[12] > 0:
            messaggio("Cura", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7.2, 40)
            if voceMarcata == 2:
                GlobalVarG2.schermo.blit(scetecn[2], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Cura:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[1]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("Recupera un po' di pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7.2, 40)
        if dati[13] > 0:
            messaggio("Antidoto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8.2, 40)
            if voceMarcata == 3:
                GlobalVarG2.schermo.blit(scetecn[3], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Antidoto:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[2]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("Cura avvelenamento a Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8.2, 40)
        if dati[14] > 0:
            messaggio("Freccia elettrica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9.2, 40)
            if voceMarcata == 4:
                GlobalVarG2.schermo.blit(scetecn[4], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Freccia elettrica:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[3]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("Infligge danni a distanza a un nemico", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9.2, 40)
        if dati[15] > 0:
            messaggio("Tempesta elettrica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10.2, 40)
            if voceMarcata == 5:
                GlobalVarG2.schermo.blit(scetecn[5], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Tempesta elettrica:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[4]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("Infligge danni a tutti i nemici o alleati nel raggio visivo di Colco", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10.2, 40)
        if dati[16] > 0:
            messaggio("Raffreddamento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11.2, 40)
            if voceMarcata == 6:
                GlobalVarG2.schermo.blit(scetecn[6], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Raffreddamento:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[5]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("Annulla il surriscaldamento ma richiede due turni (applicata sempre", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("su Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11.2, 40)
        if dati[17] > 0:
            messaggio("Auto-ricarica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12.2, 40)
            if voceMarcata == 7:
                GlobalVarG2.schermo.blit(scetecn[7], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Auto-ricarica:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[6]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("Ricarica un po' Colco ma richiede due turni e provoca", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18,
                          GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("surriscaldamento (applicata sempre su Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12.2, 40)
        if dati[18] > 0:
            messaggio("Cura +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13.2, 40)
            if voceMarcata == 8:
                GlobalVarG2.schermo.blit(scetecn[8], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Cura +:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[7]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("recupera molti pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13.2, 40)
        if dati[19] > 0:
            messaggio("Scossa +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14.2, 40)
            if voceMarcata == 9:
                GlobalVarG2.schermo.blit(scetecn[9], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Scossa +:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[8]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("Infligge molti danni a un nemico vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14.2, 40)
        if dati[20] > 0:
            messaggio("Freccia elettrica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15.2, 40)
            if voceMarcata == 10:
                GlobalVarG2.schermo.blit(scetecn[10], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Freccia elettrica +:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[9]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("Infligge molti danni a distanza a un nemico", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5,
                          35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15.2, 40)
        if dati[21] > 0:
            messaggio("Velocizza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 6.2, 40)
            if voceMarcata == 11:
                GlobalVarG2.schermo.blit(scetecn[11], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Velocizza:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[10]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("Permette a Colco, se non surriscaldato, di eseguire due azioni al turno.", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("Dopo 15 turni provoca surriscaldamento (applicata sempre su Colco)", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 6.2, 40)
        if dati[22] > 0:
            messaggio("Carica attacco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 7.2, 40)
            if voceMarcata == 12:
                GlobalVarG2.schermo.blit(scetecn[12], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Carica attacco:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[11]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("Incrementa l'attacco di Rallo per 10 turni (non ha effetto sui nemici)", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 7.2, 40)
        if dati[23] > 0:
            messaggio("Carica difesa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 8.2, 40)
            if voceMarcata == 13:
                GlobalVarG2.schermo.blit(scetecn[13], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Carica difesa:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[12]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("Incrementa la difesa di Rallo per 10 turni (non ha effetto sui nemici)", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 8.2, 40)
        if dati[24] > 0:
            messaggio("Efficienza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 9.2, 40)
            if voceMarcata == 14:
                GlobalVarG2.schermo.blit(scetecn[14], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Efficienza:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[13]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio(u"Tutte le tecniche costano la metà dei pe per 15 turni. Si annulla con", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("surriscaldamento (applicata sempre su Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 9.2, 40)
        if dati[25] > 0:
            messaggio("Tempesta elettrica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 10.2, 40)
            if voceMarcata == 15:
                GlobalVarG2.schermo.blit(scetecn[15], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Tempesta elettrica +:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[14]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("Infligge molti danni a tutti i nemici o alleati nel raggio visivo di Colco", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 10.2, 40)
        if dati[26] > 0:
            messaggio("Cura ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 11.2, 40)
            if voceMarcata == 16:
                GlobalVarG2.schermo.blit(scetecn[16], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Cura ++:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[15]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio(u"Recupera un enorme quantità dei pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5,
                          35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 11.2, 40)
        if dati[27] > 0:
            messaggio("Auto-ricarica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 12.2, 40)
            if voceMarcata == 17:
                GlobalVarG2.schermo.blit(scetecn[17], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Auto-ricarica +:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[16]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("Ricarica di molto Colco ma richiede due turni e provoca", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18,
                          GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("surriscaldamento (applicata sempre su Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 12.2, 40)
        if dati[28] > 0:
            messaggio("Scossa ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 13.2, 40)
            if voceMarcata == 18:
                GlobalVarG2.schermo.blit(scetecn[18], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Scossa ++:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[17]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("Infligge enormi danni a un nemico vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 13.2, 40)
        if dati[29] > 0:
            messaggio("Freccia Elettrica ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 14.2, 40)
            if voceMarcata == 19:
                GlobalVarG2.schermo.blit(scetecn[19], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Freccia Elettrica ++:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[18]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("Infligge enormi danni a distanza a un nemico", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5,
                          35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 14.2, 40)
        if dati[30] > 0:
            messaggio("Tempesta elettrica ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 15.2, 40)
            if voceMarcata == 20:
                GlobalVarG2.schermo.blit(scetecn[20], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                messaggio("Tempesta elettrica ++:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[19]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                messaggio("Infligge enormi danni a tutti i nemici o alleati nel raggio visivo di", GlobalVarG2.grigiochi,
                          GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 15, 40)

        messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)

        # puntatore vecchio
        i = 1
        k = 6.1
        while i <= 10:
            if tecnica == i:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * k))
            i = i + 1
            k = k + 1
        i = 11
        k = 6.1
        while i <= 20:
            if tecnica == i:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * k))
            i = i + 1
            k = k + 1
        if tecnica == 0:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4.6))

        GlobalVarG2.schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 2

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
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
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
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                tecnica = c
                                risposta = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                            break
                        i += 1
                        c += 1
                    if voceMarcata == 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        tecnica = 0
                        risposta = True
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_SPACE or ((tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w:
                if voceMarcata == 1 or voceMarcata == 11:
                    if voceMarcata == 1:
                        voceMarcata -= 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = yp - GlobalVarG2.gsy // 18 * 1.5
                        xp = GlobalVarG2.gsx // 32 * 1
                    else:
                        voceMarcata += 9
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 15.1
                else:
                    if voceMarcata == 0:
                        voceMarcata += 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 15.1
                    else:
                        voceMarcata -= 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = yp - GlobalVarG2.gsy // 18 * 1
            if tastop == pygame.K_a:
                if voceMarcata != 0:
                    if 11 <= voceMarcata <= 20:
                        voceMarcata -= 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = xp - GlobalVarG2.gsx // 32 * 7
                    else:
                        voceMarcata += 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 8
            if tastop == pygame.K_s:
                if voceMarcata == 0:
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = yp + GlobalVarG2.gsy // 18 * 1.5
                else:
                    if voceMarcata == 10 or voceMarcata == 20:
                        if voceMarcata == 10:
                            voceMarcata -= 10
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = GlobalVarG2.gsy // 18 * 4.6
                            xp = GlobalVarG2.gsx // 32 * 1
                        else:
                            voceMarcata -= 9
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = GlobalVarG2.gsy // 18 * 6.1
                    else:
                        voceMarcata += 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = yp + GlobalVarG2.gsy // 18 * 1
            if tastop == pygame.K_d:
                if voceMarcata != 0:
                    if 1 <= voceMarcata <= 10:
                        voceMarcata += 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = xp + GlobalVarG2.gsx // 32 * 7
                    else:
                        voceMarcata -= 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 1
            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,(posizionex,posizioney,larghezza,altezza,spessore))
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 12.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))

            messaggio("Scegli tecnica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
            messaggio("Cancella", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 4.7, 45)
            if voceMarcata == 0:
                messaggio("Cancella:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Cancella il settaggio di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            if dati[11] > 0:
                messaggio("Scossa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.2, 40)
                if voceMarcata == 1:
                    GlobalVarG2.schermo.blit(scetecn[1], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Scossa:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[0]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge danni a un nemico vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.2, 40)
            if dati[12] > 0:
                messaggio("Cura", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7.2, 40)
                if voceMarcata == 2:
                    GlobalVarG2.schermo.blit(scetecn[2], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Cura:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[1]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Recupera un po' di pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7.2, 40)
            if dati[13] > 0:
                messaggio("Antidoto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8.2, 40)
                if voceMarcata == 3:
                    GlobalVarG2.schermo.blit(scetecn[3], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Antidoto:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[2]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Cura avvelenamento a Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8.2, 40)
            if dati[14] > 0:
                messaggio("Freccia elettrica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9.2, 40)
                if voceMarcata == 4:
                    GlobalVarG2.schermo.blit(scetecn[4], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Freccia elettrica:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[3]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge danni a distanza a un nemico", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9.2, 40)
            if dati[15] > 0:
                messaggio("Tempesta elettrica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10.2, 40)
                if voceMarcata == 5:
                    GlobalVarG2.schermo.blit(scetecn[5], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Tempesta elettrica:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[4]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge danni a tutti i nemici o alleati nel raggio visivo di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10.2, 40)
            if dati[16] > 0:
                messaggio("Raffreddamento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11.2, 40)
                if voceMarcata == 6:
                    GlobalVarG2.schermo.blit(scetecn[6], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Raffreddamento:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[5]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Annulla il surriscaldamento ma richiede due turni (applicata sempre", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("su Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11.2, 40)
            if dati[17] > 0:
                messaggio("Auto-ricarica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12.2, 40)
                if voceMarcata == 7:
                    GlobalVarG2.schermo.blit(scetecn[7], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Auto-ricarica:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[6]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Ricarica un po' Colco ma richiede due turni e provoca", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("surriscaldamento (applicata sempre su Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12.2, 40)
            if dati[18] > 0:
                messaggio("Cura +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13.2, 40)
                if voceMarcata == 8:
                    GlobalVarG2.schermo.blit(scetecn[8], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Cura +:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[7]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("recupera molti pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13.2, 40)
            if dati[19] > 0:
                messaggio("Scossa +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14.2, 40)
                if voceMarcata == 9:
                    GlobalVarG2.schermo.blit(scetecn[9], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Scossa +:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[8]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge molti danni a un nemico vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14.2, 40)
            if dati[20] > 0:
                messaggio("Freccia elettrica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15.2, 40)
                if voceMarcata == 10:
                    GlobalVarG2.schermo.blit(scetecn[10], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Freccia elettrica +:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[9]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge molti danni a distanza a un nemico", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15.2, 40)
            if dati[21] > 0:
                messaggio("Velocizza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 6.2, 40)
                if voceMarcata == 11:
                    GlobalVarG2.schermo.blit(scetecn[11], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Velocizza:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[10]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Permette a Colco, se non surriscaldato, di eseguire due azioni al turno.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("Dopo 15 turni provoca surriscaldamento (applicata sempre su Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 6.2, 40)
            if dati[22] > 0:
                messaggio("Carica attacco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 7.2, 40)
                if voceMarcata == 12:
                    GlobalVarG2.schermo.blit(scetecn[12], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Carica attacco:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[11]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Incrementa l'attacco di Rallo per 10 turni (non ha effetto sui nemici)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 7.2, 40)
            if dati[23] > 0:
                messaggio("Carica difesa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 8.2, 40)
                if voceMarcata == 13:
                    GlobalVarG2.schermo.blit(scetecn[13], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Carica difesa:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[12]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Incrementa la difesa di Rallo per 10 turni (non ha effetto sui nemici)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 8.2, 40)
            if dati[24] > 0:
                messaggio("Efficienza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 9.2, 40)
                if voceMarcata == 14:
                    GlobalVarG2.schermo.blit(scetecn[14], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Efficienza:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[13]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio(u"Tutte le tecniche costano la metà dei pe per 15 turni. Si annulla con", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("surriscaldamento (applicata sempre su Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 9.2, 40)
            if dati[25] > 0:
                messaggio("Tempesta elettrica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 10.2, 40)
                if voceMarcata == 15:
                    GlobalVarG2.schermo.blit(scetecn[15], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Tempesta elettrica +:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[14]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge molti danni a tutti i nemici o alleati nel raggio visivo di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 10.2, 40)
            if dati[26] > 0:
                messaggio("Cura ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 11.2, 40)
                if voceMarcata == 16:
                    GlobalVarG2.schermo.blit(scetecn[16], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Cura ++:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[15]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio(u"Recupera un enorme quantità dei pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 11.2, 40)
            if dati[27] > 0:
                messaggio("Auto-ricarica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 12.2, 40)
                if voceMarcata == 17:
                    GlobalVarG2.schermo.blit(scetecn[17], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Auto-ricarica +:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[16]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Ricarica di molto Colco ma richiede due turni e provoca", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("surriscaldamento (applicata sempre su Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 12.2, 40)
            if dati[28] > 0:
                messaggio("Scossa ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 13.2, 40)
                if voceMarcata == 18:
                    GlobalVarG2.schermo.blit(scetecn[18], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Scossa ++:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[17]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge enormi danni a un nemico vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 13.2, 40)
            if dati[29] > 0:
                messaggio("Freccia Elettrica ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 14.2, 40)
                if voceMarcata == 19:
                    GlobalVarG2.schermo.blit(scetecn[19], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Freccia Elettrica ++:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[18]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge enormi danni a distanza a un nemico", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 14.2, 40)
            if dati[30] > 0:
                messaggio("Tempesta elettrica ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 15.2, 40)
                if voceMarcata == 20:
                    GlobalVarG2.schermo.blit(scetecn[20], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Tempesta elettrica ++:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[19]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge enormi danni a tutti i nemici o alleati nel raggio visivo di", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 15, 40)

            messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)

            # puntatore vecchio
            i = 1
            k = 6.1
            while i <= 10:
                if tecnica == i:
                    GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * k))
                i = i + 1
                k = k + 1
            i = 11
            k = 6.1
            while i <= 20:
                if tecnica == i:
                    GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * k))
                i = i + 1
                k = k + 1
            if tecnica == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4.6))

            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)
    return tecnica


def equiprobo(dati, canzone):
    robosta = pygame.transform.scale(GlobalVarG2.roboo, (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatorevecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    sfondoOggetto = pygame.transform.scale(GlobalVarG2.sfondoOggettoMenu, (int(GlobalVarG2.gpx * 2), int(GlobalVarG2.gpy * 2)))
    sconosciutoEquip = pygame.transform.scale(GlobalVarG2.sconosciutoEquipMenu, (int(GlobalVarG2.gpx * 2), int(GlobalVarG2.gpy * 2)))
    xp = GlobalVarG2.gsx // 32 * 1
    yp = GlobalVarG2.gsy // 18 * 6.8
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

    vetImgBatterie = GlobalVarG2.vetImgBatterieMenu

    vetIcoBatterie = []
    i = 0
    while i < 5:
        if dati[41 + i] > 0:
            vetIcoBatterie.append(GlobalVarG2.vetIcoBatterieMenu[i])
        else:
            vetIcoBatterie.append(sconosciutoEquip)
        i += 1

    # primo frame
    if True:
        GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
        # rettangolo(dove,colore,posizione,larghezza/altezza,spessore)
        pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 12.5))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 4))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 15.5))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))
        pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 7, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 12.5))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 7, GlobalVarG2.gsy // 18 * 4))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 4))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 15.5))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 7, GlobalVarG2.gsy // 18 * 15.5))

        if annullaRiordinamento:
            dati = list(datiPrimaDiRiordinamento)
            annullaRiordinamento = False
            xp = vxpGambit
            yp = vypGambit
            voceMarcata = voceGambitMarcata

        if riordinamento:
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigiochi, (xp, yp - (GlobalVarG2.gpy // 4), GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 1))

        messaggio("Setta Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)

        # equip batteria
        messaggio("Batterie", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 4.5, 60)
        i = 0
        while i < 5:
            GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 2.5, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
            GlobalVarG2.schermo.blit(vetIcoBatterie[i], (GlobalVarG2.gsx // 32 * 2.5, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
            i += 1

        # programmazione Colco
        messaggio("Ordine", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 7.5, GlobalVarG2.gsy // 18 * 4.5, 60)
        i = 1
        while i <= 10:
            if i == 10:
                if riordinamento and voceMarcata == i + 5:
                    messaggio(str(i), GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 8.3, GlobalVarG2.gsy // 18 * (i + 5), 50)
                else:
                    messaggio(str(i), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 8.3, GlobalVarG2.gsy // 18 * (i + 5), 50)
            else:
                if riordinamento and voceMarcata == i + 5:
                    messaggio(str(i), GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 8.5, GlobalVarG2.gsy // 18 * (i + 5), 50)
                else:
                    messaggio(str(i), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 8.5, GlobalVarG2.gsy // 18 * (i + 5), 50)
            i += 1
        messaggio("Condizione...", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 4.5, 60)
        c = 6.1
        for i in range(101, 111):
            if dati[i] == -1:
                messaggio("---", GlobalVarG2.grigioscu, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 0:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("---", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 1:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Rallo con pv < 80%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Rallo con pv < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 2:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Rallo con pv < 50%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Rallo con pv < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 3:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Rallo con pv < 30%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Rallo con pv < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 4:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Rallo con veleno", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Rallo con veleno", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 5:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Colco surriscaldato", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Colco surriscaldato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 6:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Colco con pe < 80%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Colco con pe < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 7:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Colco con pe < 50%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Colco con pe < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 8:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Colco con pe < 30%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Colco con pe < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 9:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Sempre a Rallo", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Sempre a Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 10:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Sempre a Colco", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Sempre a Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 11:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Nemico a caso", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Nemico a caso", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 12:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Nemico vicino", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Nemico vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 13:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Nemico lontano", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Nemico lontano", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 14:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Nemico con pv < 80%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Nemico con pv < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 15:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Nemico con pv < 50%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Nemico con pv < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 16:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Nemico con pv < 30%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Nemico con pv < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 17:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Nemico con meno pv", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Nemico con meno pv", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 18:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Numero di nemici > 1", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Numero di nemici > 1", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 19:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Numero di nemici > 4", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Numero di nemici > 4", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 20:
                if riordinamento and voceMarcata == i - 95:
                    messaggio("Numero di nemici > 7", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Numero di nemici > 7", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
            c += 1
        messaggio("...Tecnica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * 4.5, 60)
        c = 6.1
        for i in range(111, 121):
            if dati[i] == -1:
                messaggio("---", GlobalVarG2.grigioscu, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 0:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("---", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 1:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Scossa", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Scossa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 2:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Cura", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Cura", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 3:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Antidoto", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Antidoto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 4:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Freccia elettrica", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Freccia elettrica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 5:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Tempesta elettrica", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Tempesta elettrica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 6:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Raffreddamento", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Raffreddamento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 7:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Auto-ricarica", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Auto-ricarica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 8:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Cura +", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Cura +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 9:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Scossa +", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Scossa +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 10:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Freccia elettrica +", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Freccia elettrica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 11:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Velocizza", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Velocizza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 12:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Carica attacco", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Carica attacco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 13:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Carica difesa", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Carica difesa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 14:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Efficienza", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Efficienza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 15:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Tempesta elettrica +", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Tempesta elettrica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 16:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Cura ++", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Cura ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 17:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Auto-ricarica +", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Auto-ricarica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 18:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Scossa ++", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Scossa ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 19:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Freccia Elettrica ++", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Freccia Elettrica ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            if dati[i] == 20:
                if riordinamento and voceMarcata == i - 105:
                    messaggio("Tempesta elettrica ++", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                else:
                    messaggio("Tempesta elettrica ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
            c = c + 1

        messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)

        esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

        GlobalVarG2.schermo.blit(robosta, (GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 10))
        GlobalVarG2.schermo.blit(vetImgBatterie[dati[9]], (GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 10))
        messaggio("Statistiche:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 7.7, 50)
        messaggio("Pe totali: %i" % entot, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 8.5, 35)
        messaggio("Difesa: %i" % difro, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 9, 35)

        # mostrare descrizione batterie / priorità / condizioni / azioni
        if voceMarcata == 1:
            if dati[71] != 0:
                messaggio("Batteria piccola:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                messaggio("Batteria che contiene poca alimentazione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)
                diff = (0 * 0 * 80) - (dati[9] * dati[9] * 80)
                if dati[9] > 0:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                diff = 0 - (dati[9] * dati[9] * 30)
                if dati[9] > 0:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
        if voceMarcata == 2:
            if dati[72] != 0:
                messaggio("Batteria discreta:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                messaggio("Batteria con una buona capienza e", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                messaggio("ottimizzazione del sistema difensivo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)
                diff = (1 * 1 * 80) - (dati[9] * dati[9] * 80)
                if dati[9] > 1:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                elif dati[9] < 1:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                diff = 30 - (dati[9] * dati[9] * 30)
                if dati[9] > 1:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                elif dati[9] < 1:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
        if voceMarcata == 3:
            if dati[73] != 0:
                messaggio("Batteria capiente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                messaggio(u"Batteria con una grande capacità e un", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                messaggio("ottimo sistema difensivo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)
                diff = (2 * 2 * 80) - (dati[9] * dati[9] * 80)
                if dati[9] > 2:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                elif dati[9] < 2:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                diff = 120 - (dati[9] * dati[9] * 30)
                if dati[9] > 2:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                elif dati[9] < 2:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
        if voceMarcata == 4:
            if dati[74] != 0:
                messaggio("Batteria enorme:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                messaggio("Grande batteria che permette a Colco di", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                messaggio(u"utilizzare le tecniche più dispendiose", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)
                diff = (3 * 3 * 80) - (dati[9] * dati[9] * 80)
                if dati[9] > 3:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                elif dati[9] < 3:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                diff = 270 - (dati[9] * dati[9] * 30)
                if dati[9] > 3:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                elif dati[9] < 3:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
        if voceMarcata == 5:
            if dati[75] != 0:
                messaggio("Batteria illimitata:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                messaggio("Batteria incredibilmente capiente.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                messaggio("Permette un eccellente ottimizzazione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                messaggio("del sistema difensivo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)
                diff = (4 * 4 * 80) - (dati[9] * dati[9] * 80)
                if dati[9] > 4:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                elif dati[9] < 4:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                diff = 480 - (dati[9] * dati[9] * 30)
                if dati[9] > 4:
                    messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                elif dati[9] < 4:
                    messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)

        if 6 <= voceMarcata <= 15:
            messaggio(u"Ordine:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
            messaggio(u"Determina il livello di priorità dell'evento.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
            messaggio(u"Colco eseguirà la prima tecnica della lista", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
            messaggio(u"la cui condizione si è verificata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)

        if 16 <= voceMarcata <= 25:
            messaggio("Condizione:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
            messaggio("Indica la situazione che si deve verificare", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
            messaggio(u"affinchè Colco esegua la tecnica associata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
            messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)

        if 26 <= voceMarcata <= 35:
            messaggio("Tecnica:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
            messaggio(u"La tecnica che Colco eseguirà quando si", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
            messaggio("verifica la condizione associata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
            messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)

        # puntatore vecchio batterie/riordinamento gambit
        if dati[9] == 0:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 6.8))
        if dati[9] == 1:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 8.8))
        if dati[9] == 2:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 10.8))
        if dati[9] == 3:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 12.8))
        if dati[9] == 4:
            GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 14.8))
        if riordinamento:
            GlobalVarG2.schermo.blit(puntatorevecchio, (vxpGambit, vypGambit))

        GlobalVarG2.schermo.blit(puntatore, (xp, yp))
        if voceMarcata >= 6 and not riordinamento:
            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 7.5, yp + (int(GlobalVarG2.gpy * 0.7))), (GlobalVarG2.gsx // 32 * 22.5, yp + (int(GlobalVarG2.gpy * 0.7))), 2)

        pygame.display.update()

    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 2

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
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
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
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        riordinamento = False
                    else:
                        # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                        # armrob
                        if voceMarcata == 1:
                            if dati[71] != 0:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                dati[9] = 0
                                esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                                if dati[10] > entot:
                                    dati[10] = entot
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if voceMarcata == 2:
                            if dati[72] != 0:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                dati[9] = 1
                                esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                                if dati[10] > entot:
                                    dati[10] = entot
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if voceMarcata == 3:
                            if dati[73] != 0:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                dati[9] = 2
                                esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                                if dati[10] > entot:
                                    dati[10] = entot
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if voceMarcata == 4:
                            if dati[74] != 0:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                dati[9] = 3
                                esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                                if dati[10] > entot:
                                    dati[10] = entot
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if voceMarcata == 5:
                            if dati[75] != 0:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                dati[9] = 4
                                esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                                if dati[10] > entot:
                                    dati[10] = entot
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)

                        # riordina
                        if 6 <= voceMarcata <= 15:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
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
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                    dati[i] = sceglicondiz(dati, dati[i], canzone)
                                else:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                            i += 1
                            c += 1

                        # tecniche
                        i = 111
                        c = 26
                        while i <= 120:
                            if voceMarcata == c:
                                if dati[i] != -1:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                    dati[i] = sceglitecn(dati, dati[i], canzone)
                                else:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                            i += 1
                            c += 1
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_q or tastop == pygame.K_SPACE or ((tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w:
                if riordinamento:
                    if voceMarcata != 6:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
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
                        yp = yp - GlobalVarG2.gsy // 18 * 1
                else:
                    if 1 <= voceMarcata <= 5:
                        if voceMarcata == 1:
                            voceMarcata += 4
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = GlobalVarG2.gsy // 18 * 14.8
                        else:
                            voceMarcata -= 1
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = yp - GlobalVarG2.gsy // 18 * 2
                    else:
                        if voceMarcata == 6 or voceMarcata == 16 or voceMarcata == 26:
                            voceMarcata += 9
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = GlobalVarG2.gsy // 18 * 15
                        else:
                            voceMarcata -= 1
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = yp - GlobalVarG2.gsy // 18 * 1
            if tastop == pygame.K_a and not riordinamento:
                if 1 <= voceMarcata <= 5:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    if voceMarcata == 1:
                        voceMarcata += 26
                        yp = GlobalVarG2.gsy // 18 * 7
                    elif voceMarcata == 2:
                        voceMarcata += 27
                        yp = GlobalVarG2.gsy // 18 * 9
                    elif voceMarcata == 3:
                        voceMarcata += 28
                        yp = GlobalVarG2.gsy // 18 * 11
                    elif voceMarcata == 4:
                        voceMarcata += 29
                        yp = GlobalVarG2.gsy // 18 * 13
                    elif voceMarcata == 5:
                        voceMarcata += 30
                        yp = GlobalVarG2.gsy // 18 * 15
                    xp = GlobalVarG2.gsx // 32 * 16.5
                elif 6 <= voceMarcata <= 15:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    if 6 <= voceMarcata <= 7:
                        if voceMarcata == 6:
                            voceMarcata -= 5
                        elif voceMarcata == 7:
                            voceMarcata -= 6
                        yp = GlobalVarG2.gsy // 18 * 6.8
                    elif 8 <= voceMarcata <= 9:
                        if voceMarcata == 8:
                            voceMarcata -= 6
                        elif voceMarcata == 9:
                            voceMarcata -= 7
                        yp = GlobalVarG2.gsy // 18 * 8.8
                    elif 10 <= voceMarcata <= 11:
                        if voceMarcata == 10:
                            voceMarcata -= 7
                        elif voceMarcata == 11:
                            voceMarcata -= 8
                        yp = GlobalVarG2.gsy // 18 * 10.8
                    elif 12 <= voceMarcata <= 13:
                        if voceMarcata == 12:
                            voceMarcata -= 8
                        elif voceMarcata == 13:
                            voceMarcata -= 9
                        yp = GlobalVarG2.gsy // 18 * 12.8
                    elif 14 <= voceMarcata <= 15:
                        if voceMarcata == 14:
                            voceMarcata -= 9
                        elif voceMarcata == 15:
                            voceMarcata -= 10
                        yp = GlobalVarG2.gsy // 18 * 14.8
                    xp = GlobalVarG2.gsx // 32 * 1
                elif 16 <= voceMarcata <= 25:
                    voceMarcata -= 10
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 7
                elif 26 <= voceMarcata <= 35:
                    voceMarcata -= 10
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 10
            if tastop == pygame.K_s:
                if riordinamento:
                    if voceMarcata != 15:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
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
                        yp = yp + GlobalVarG2.gsy // 18 * 1
                else:
                    if 1 <= voceMarcata <= 5:
                        if voceMarcata == 5:
                            voceMarcata -= 4
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = GlobalVarG2.gsy // 18 * 6.8
                        else:
                            voceMarcata += 1
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = yp + GlobalVarG2.gsy // 18 * 2
                    else:
                        if voceMarcata == 15 or voceMarcata == 25 or voceMarcata == 35:
                            voceMarcata -= 9
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = GlobalVarG2.gsy // 18 * 6
                        else:
                            voceMarcata += 1
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = yp + GlobalVarG2.gsy // 18 * 1
            if tastop == pygame.K_d and not riordinamento:
                if 1 <= voceMarcata <= 5:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    if voceMarcata == 1:
                        voceMarcata += 6
                        yp = GlobalVarG2.gsy // 18 * 7
                    elif voceMarcata == 2:
                        voceMarcata += 7
                        yp = GlobalVarG2.gsy // 18 * 9
                    elif voceMarcata == 3:
                        voceMarcata += 8
                        yp = GlobalVarG2.gsy // 18 * 11
                    elif voceMarcata == 4:
                        voceMarcata += 9
                        yp = GlobalVarG2.gsy // 18 * 13
                    elif voceMarcata == 5:
                        voceMarcata += 10
                        yp = GlobalVarG2.gsy // 18 * 15
                    xp = GlobalVarG2.gsx // 32 * 7
                elif 6 <= voceMarcata <= 15:
                    voceMarcata += 10
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 10
                elif 16 <= voceMarcata <= 25:
                    voceMarcata += 10
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 16.5
                elif 26 <= voceMarcata <= 35:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    if 26 <= voceMarcata <= 27:
                        if voceMarcata == 26:
                            voceMarcata -= 25
                        elif voceMarcata == 27:
                            voceMarcata -= 26
                        yp = GlobalVarG2.gsy // 18 * 6.8
                    elif 28 <= voceMarcata <= 29:
                        if voceMarcata == 28:
                            voceMarcata -= 26
                        elif voceMarcata == 29:
                            voceMarcata -= 27
                        yp = GlobalVarG2.gsy // 18 * 8.8
                    elif 30 <= voceMarcata <= 31:
                        if voceMarcata == 30:
                            voceMarcata -= 27
                        elif voceMarcata == 31:
                            voceMarcata -= 28
                        yp = GlobalVarG2.gsy // 18 * 10.8
                    elif 32 <= voceMarcata <= 33:
                        if voceMarcata == 32:
                            voceMarcata -= 28
                        elif voceMarcata == 33:
                            voceMarcata -= 29
                        yp = GlobalVarG2.gsy // 18 * 12.8
                    elif 34 <= voceMarcata <= 35:
                        if voceMarcata == 34:
                            voceMarcata -= 29
                        elif voceMarcata == 35:
                            voceMarcata -= 30
                        yp = GlobalVarG2.gsy // 18 * 14.8
                    xp = GlobalVarG2.gsx // 32 * 1
            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,posizione,larghezza/altezza,spessore)
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 12.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 7, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 12.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 7, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 7, GlobalVarG2.gsy // 18 * 15.5))

            if annullaRiordinamento:
                dati = list(datiPrimaDiRiordinamento)
                annullaRiordinamento = False
                xp = vxpGambit
                yp = vypGambit
                voceMarcata = voceGambitMarcata

            if riordinamento:
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigiochi, (xp, yp - (GlobalVarG2.gpy // 4), GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 1))

            messaggio("Setta Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)

            # equip batteria
            messaggio("Batterie", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 4.5, 60)
            i = 0
            while i < 5:
                GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 2.5, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                GlobalVarG2.schermo.blit(vetIcoBatterie[i], (GlobalVarG2.gsx // 32 * 2.5, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                i += 1

            # programmazione Colco
            messaggio("Ordine", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 7.5, GlobalVarG2.gsy // 18 * 4.5, 60)
            i = 1
            while i <= 10:
                if i == 10:
                    if riordinamento and voceMarcata == i + 5:
                        messaggio(str(i), GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 8.3, GlobalVarG2.gsy // 18 * (i + 5), 50)
                    else:
                        messaggio(str(i), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 8.3, GlobalVarG2.gsy // 18 * (i + 5), 50)
                else:
                    if riordinamento and voceMarcata == i + 5:
                        messaggio(str(i), GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 8.5, GlobalVarG2.gsy // 18 * (i + 5), 50)
                    else:
                        messaggio(str(i), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 8.5, GlobalVarG2.gsy // 18 * (i + 5), 50)
                i += 1
            messaggio("Condizione...", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 4.5, 60)
            c = 6.1
            for i in range(101, 111):
                if dati[i] == -1:
                    messaggio("---", GlobalVarG2.grigioscu, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 0:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("---", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 1:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Rallo con pv < 80%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Rallo con pv < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 2:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Rallo con pv < 50%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Rallo con pv < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 3:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Rallo con pv < 30%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Rallo con pv < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 4:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Rallo con veleno", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Rallo con veleno", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 5:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Colco surriscaldato", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Colco surriscaldato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 6:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Colco con pe < 80%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Colco con pe < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 7:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Colco con pe < 50%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Colco con pe < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 8:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Colco con pe < 30%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Colco con pe < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 9:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Sempre a Rallo", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Sempre a Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 10:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Sempre a Colco", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Sempre a Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 11:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Nemico a caso", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Nemico a caso", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 12:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Nemico vicino", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Nemico vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 13:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Nemico lontano", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Nemico lontano", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 14:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Nemico con pv < 80%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Nemico con pv < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 15:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Nemico con pv < 50%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Nemico con pv < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 16:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Nemico con pv < 30%", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Nemico con pv < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 17:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Nemico con meno pv", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Nemico con meno pv", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 18:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Numero di nemici > 1", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Numero di nemici > 1", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 19:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Numero di nemici > 4", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Numero di nemici > 4", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 20:
                    if riordinamento and voceMarcata == i - 95:
                        messaggio("Numero di nemici > 7", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Numero di nemici > 7", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                c += 1
            messaggio("...Tecnica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * 4.5, 60)
            c = 6.1
            for i in range(111, 121):
                if dati[i] == -1:
                    messaggio("---", GlobalVarG2.grigioscu, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 0:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("---", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 1:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Scossa", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Scossa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 2:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Cura", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Cura", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 3:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Antidoto", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Antidoto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 4:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Freccia elettrica", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Freccia elettrica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 5:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Tempesta elettrica", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Tempesta elettrica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 6:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Raffreddamento", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Raffreddamento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 7:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Auto-ricarica", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Auto-ricarica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 8:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Cura +", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Cura +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 9:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Scossa +", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Scossa +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 10:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Freccia elettrica +", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Freccia elettrica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 11:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Velocizza", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Velocizza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 12:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Carica attacco", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Carica attacco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 13:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Carica difesa", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Carica difesa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 14:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Efficienza", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Efficienza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 15:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Tempesta elettrica +", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Tempesta elettrica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 16:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Cura ++", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Cura ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 17:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Auto-ricarica +", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Auto-ricarica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 18:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Scossa ++", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Scossa ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 19:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Freccia Elettrica ++", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Freccia Elettrica ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 20:
                    if riordinamento and voceMarcata == i - 105:
                        messaggio("Tempesta elettrica ++", GlobalVarG2.grigio, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                    else:
                        messaggio("Tempesta elettrica ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                c = c + 1

            messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)

            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

            GlobalVarG2.schermo.blit(robosta, (GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 10))
            GlobalVarG2.schermo.blit(vetImgBatterie[dati[9]], (GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 10))
            messaggio("Statistiche:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 7.7, 50)
            messaggio("Pe totali: %i" % entot, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 8.5, 35)
            messaggio("Difesa: %i" % difro, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 9, 35)

            # mostrare descrizione batterie / priorità / condizioni / azioni
            if voceMarcata == 1:
                if dati[71] != 0:
                    messaggio("Batteria piccola:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                    messaggio("Batteria che contiene poca alimentazione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)
                    diff = (0 * 0 * 80) - (dati[9] * dati[9] * 80)
                    if dati[9] > 0:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    diff = 0 - (dati[9] * dati[9] * 30)
                    if dati[9] > 0:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            if voceMarcata == 2:
                if dati[72] != 0:
                    messaggio("Batteria discreta:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                    messaggio("Batteria con una buona capienza e", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                    messaggio("ottimizzazione del sistema difensivo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)
                    diff = (1 * 1 * 80) - (dati[9] * dati[9] * 80)
                    if dati[9] > 1:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[9] < 1:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    diff = 30 - (dati[9] * dati[9] * 30)
                    if dati[9] > 1:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[9] < 1:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            if voceMarcata == 3:
                if dati[73] != 0:
                    messaggio("Batteria capiente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                    messaggio(u"Batteria con una grande capacità e un", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                    messaggio("ottimo sistema difensivo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)
                    diff = (2 * 2 * 80) - (dati[9] * dati[9] * 80)
                    if dati[9] > 2:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[9] < 2:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    diff = 120 - (dati[9] * dati[9] * 30)
                    if dati[9] > 2:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[9] < 2:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            if voceMarcata == 4:
                if dati[74] != 0:
                    messaggio("Batteria enorme:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                    messaggio("Grande batteria che permette a Colco di", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                    messaggio(u"utilizzare le tecniche più dispendiose", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)
                    diff = (3 * 3 * 80) - (dati[9] * dati[9] * 80)
                    if dati[9] > 3:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[9] < 3:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    diff = 270 - (dati[9] * dati[9] * 30)
                    if dati[9] > 3:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[9] < 3:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            if voceMarcata == 5:
                if dati[75] != 0:
                    messaggio("Batteria illimitata:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                    messaggio("Batteria incredibilmente capiente.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                    messaggio("Permette un eccellente ottimizzazione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                    messaggio("del sistema difensivo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)
                    diff = (4 * 4 * 80) - (dati[9] * dati[9] * 80)
                    if dati[9] > 4:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[9] < 4:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    diff = 480 - (dati[9] * dati[9] * 30)
                    if dati[9] > 4:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[9] < 4:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)

            if 6 <= voceMarcata <= 15:
                messaggio(u"Ordine:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                messaggio(u"Determina il livello di priorità dell'evento.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                messaggio(u"Colco eseguirà la prima tecnica della lista", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                messaggio(u"la cui condizione si è verificata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)

            if 16 <= voceMarcata <= 25:
                messaggio("Condizione:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                messaggio("Indica la situazione che si deve verificare", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                messaggio(u"affinchè Colco esegua la tecnica associata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)

            if 26 <= voceMarcata <= 35:
                messaggio("Tecnica:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                messaggio(u"La tecnica che Colco eseguirà quando si", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                messaggio("verifica la condizione associata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)

            # puntatore vecchio batterie/riordinamento gambit
            if dati[9] == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 6.8))
            if dati[9] == 1:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 8.8))
            if dati[9] == 2:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 10.8))
            if dati[9] == 3:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 12.8))
            if dati[9] == 4:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 14.8))
            if riordinamento:
                GlobalVarG2.schermo.blit(puntatorevecchio, (vxpGambit, vypGambit))

            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            if voceMarcata >= 6 and not riordinamento:
                pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 7.5, yp + (int(GlobalVarG2.gpy * 0.7))), (GlobalVarG2.gsx // 32 * 22.5, yp + (int(GlobalVarG2.gpy * 0.7))), 2)

            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)
    return dati


def oggetti(dati, canzone):
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatorevecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    sfondostastart = pygame.transform.scale(GlobalVarG2.sfondostax3, (GlobalVarG2.gpx * 4, GlobalVarG2.gpy))
    sconosciutoOggetto = pygame.transform.scale(GlobalVarG2.sconosciutoOggettoMenu, (GlobalVarG2.gpx * 10, GlobalVarG2.gpy * 10))
    xp = GlobalVarG2.gsx // 32 * 1
    yp = GlobalVarG2.gsy // 18 * 5
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
            imgOggetti.append(GlobalVarG2.vetImgOggettiMenu[i - 1])
        else:
            imgOggetti.append(sconosciutoOggetto)
        i += 1

    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

    # primo frame
    if True:
        GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 12.5))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 4))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 15.5))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))

        # menu conferma
        if usa != 0:
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 12.5, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 12.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5))
            # posizionare il cursore su menu usa
            if usauno:
                xpv = xp
                ypv = yp
                xp = GlobalVarG2.gsx // 32 * 15
                yp = GlobalVarG2.gsy // 18 * 15.1
                voceMarcata = 2
                usauno = False
            GlobalVarG2.schermo.blit(puntatorevecchio, (xpv, ypv))
            messaggio("Usare?", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 13.3, GlobalVarG2.gsy // 18 * 13.2, 80)
            messaggio("Si", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 13, GlobalVarG2.gsy // 18 * 15, 60)
            messaggio("No", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 15, 60)

        # pozione, carica batt, bomba, antidoto, bomba veleno, esca, super poz, carica migliorato, bomba pot, bomba atomica
        messaggio("Oggetti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
        if dati[31] >= 0:
            messaggio("Pozione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 5, 45)
            messaggio("x %i" % dati[31], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 5, 45)
            if oggetton == 1:
                messaggio("Pozione:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Recupera 100 pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 5, 45)
        if dati[32] >= 0:
            messaggio("Caricabatterie", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6, 45)
            messaggio("x %i" % dati[32], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 6, 45)
            if oggetton == 2:
                messaggio("Caricabatterie:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Recupera 250 pe di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6, 45)
        if dati[33] >= 0:
            messaggio("Medicina", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7, 45)
            messaggio("x %i" % dati[33], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 7, 45)
            if oggetton == 3:
                messaggio("Medicina:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Cura avvelenamento a Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7, 45)
        if dati[34] >= 0:
            messaggio("Super pozione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8, 45)
            messaggio("x %i" % dati[34], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 8, 45)
            if oggetton == 4:
                messaggio("Super pozione:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Recupera 300 pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8, 45)
        if dati[35] >= 0:
            messaggio("Carica plus", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9, 45)
            messaggio("x %i" % dati[35], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 9, 45)
            if oggetton == 5:
                messaggio("Carica plus:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Recupera 600 pe di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9, 45)
        if dati[36] >= 0:
            messaggio("Bomba", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11, 45)
            messaggio("x %i" % dati[36], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 11, 45)
            if oggetton == 6:
                messaggio("Bomba:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Infligge un po' di danni ai nemici su cui viene lanciata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20,
                          GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11, 45)
        if dati[37] >= 0:
            messaggio("Bomba velenosa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12, 45)
            messaggio("x %i" % dati[37], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 12, 45)
            if oggetton == 7:
                messaggio("Bomba velenosa:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Infligge avvelenamento al nemico su cui viene lanciata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20,
                          GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12, 45)
        if dati[38] >= 0:
            messaggio("Esca", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13, 45)
            messaggio("x %i" % dati[38], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 13, 45)
            if oggetton == 8:
                messaggio("Esca:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio(u"Distrae i nemici finché non viene distrutta. È possibile", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20,
                          GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("riprenderla passandoci sopra", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13, 45)
        if dati[39] >= 0:
            messaggio("Bomba appiccicosa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14, 45)
            messaggio("x %i" % dati[39], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 14, 45)
            if oggetton == 9:
                messaggio("Bomba appiccicosa:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio(u"Dimezza la velocità del nemico su cui viene lanciata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20,
                          GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14, 45)
        if dati[40] >= 0:
            messaggio("Bomba potenziata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15, 45)
            messaggio("x %i" % dati[40], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 15, 45)
            if oggetton == 10:
                messaggio("Bomba potenziata:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Infligge molti danni ai nemici su cui viene lanciata in un", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20,
                          GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("vasto raggio", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
        else:
            messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15, 45)

        # vita-status personaggio
        if dati[5] < 0:
            dati[5] = 0
        messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 4, 50)
        messaggio("Status alterativi: ", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 5, 50)
        persmen = pygame.transform.scale(GlobalVarG2.persGrafMenu, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
        GlobalVarG2.schermo.blit(persmen, (GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 4))
        GlobalVarG2.schermo.blit(sfondostastart, (GlobalVarG2.gsx // 32 * 14, (GlobalVarG2.gsy // 18 * 6) + (GlobalVarG2.gpy // 8)))
        if dati[121]:
            avvelenato = pygame.transform.scale(GlobalVarG2.avvelenatoo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
            GlobalVarG2.schermo.blit(avvelenato, (GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 6))
        if dati[123] > 0:
            attaccopiu = pygame.transform.scale(GlobalVarG2.attaccopiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
            GlobalVarG2.schermo.blit(attaccopiu, ((GlobalVarG2.gsx // 32 * 14) + (2 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 6))
        if dati[124] > 0:
            difesapiu = pygame.transform.scale(GlobalVarG2.difesapiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
            GlobalVarG2.schermo.blit(difesapiu, ((GlobalVarG2.gsx // 32 * 14) + (4 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 6))
        # vita-status robo
        if dati[10] < 0:
            dati[10] = 0
        messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 9, 50)
        messaggio("Status alterativi: ", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 10, 50)
        robomen = pygame.transform.scale(GlobalVarG2.robograf, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
        GlobalVarG2.schermo.blit(robomen, (GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 8))
        GlobalVarG2.schermo.blit(sfondostastart, (GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 11))
        if dati[122] > 0:
            surriscaldato = pygame.transform.scale(GlobalVarG2.surriscaldatoo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
            GlobalVarG2.schermo.blit(surriscaldato, (GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 11))
        if dati[125] > 0:
            velocitapiu = pygame.transform.scale(GlobalVarG2.velocitapiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
            GlobalVarG2.schermo.blit(velocitapiu, ((GlobalVarG2.gsx // 32 * 14) + (2 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 11))
        if dati[126] > 0:
            efficienzapiu = pygame.transform.scale(GlobalVarG2.efficienzapiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
            GlobalVarG2.schermo.blit(efficienzapiu, ((GlobalVarG2.gsx // 32 * 14) + (4 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 11))

        if attacco != 0:
            risposta = True

        messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
        GlobalVarG2.schermo.blit(imgOggetti[oggetton - 1], (GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 3))
        GlobalVarG2.schermo.blit(puntatore, (xp, yp))
        if usa == 0:
            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, ((xp + (int(GlobalVarG2.gpx // 1.5))), yp + (int(GlobalVarG2.gpy * 0.7))), (xp + (int(GlobalVarG2.gpx * 9.5)), yp + (int(GlobalVarG2.gpy * 0.7))), 2)
        else:
            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, ((xpv + (int(GlobalVarG2.gpx // 1.5))), ypv + (int(GlobalVarG2.gpy * 0.7))), (xpv + (int(GlobalVarG2.gpx * 9.5)), ypv + (int(GlobalVarG2.gpy * 0.7))), 2)

        pygame.display.update()

    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 2

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
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        xp = GlobalVarG2.gsx // 32 * 1
                        if usa == 1:
                            yp = GlobalVarG2.gsy // 18 * 5
                        if usa == 2:
                            yp = GlobalVarG2.gsy // 18 * 6
                        if usa == 3:
                            yp = GlobalVarG2.gsy // 18 * 7
                        if usa == 4:
                            yp = GlobalVarG2.gsy // 18 * 8
                        if usa == 5:
                            yp = GlobalVarG2.gsy // 18 * 9
                        if usa == 6:
                            yp = GlobalVarG2.gsy // 18 * 11
                        if usa == 7:
                            yp = GlobalVarG2.gsy // 18 * 12
                        if usa == 8:
                            yp = GlobalVarG2.gsy // 18 * 13
                        if usa == 9:
                            yp = GlobalVarG2.gsy // 18 * 14
                        if usa == 10:
                            yp = GlobalVarG2.gsy // 18 * 15
                        usa = 0
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
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
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        xp = GlobalVarG2.gsx // 32 * 1
                        # pozione
                        if usa == 1:
                            dati[5] = dati[5] + 100
                            if dati[5] > pvtot:
                                dati[5] = pvtot
                            dati[31] = dati[31] - 1
                            yp = GlobalVarG2.gsy // 18 * 5
                        # carica batt
                        if usa == 2:
                            dati[10] = dati[10] + 250
                            if dati[10] > entot:
                                dati[10] = entot
                            dati[32] = dati[32] - 1
                            yp = GlobalVarG2.gsy // 18 * 6
                        # antidoto
                        if usa == 3:
                            dati[121] = 0
                            dati[33] = dati[33] - 1
                            yp = GlobalVarG2.gsy // 18 * 7
                        # super pozione
                        if usa == 4:
                            dati[5] = dati[5] + 300
                            if dati[5] > pvtot:
                                dati[5] = pvtot
                            dati[34] = dati[34] - 1
                            yp = GlobalVarG2.gsy // 18 * 8
                        # carica migliorato
                        if usa == 5:
                            dati[10] = dati[10] + 600
                            if dati[10] > entot:
                                dati[10] = entot
                            dati[35] = dati[35] - 1
                            yp = GlobalVarG2.gsy // 18 * 9
                        # bomba
                        if usa == 6:
                            attacco = 2
                            yp = GlobalVarG2.gsy // 18 * 11
                        # bomba veleno
                        if usa == 7:
                            attacco = 3
                            yp = GlobalVarG2.gsy // 18 * 12
                        # esca
                        if usa == 8:
                            attacco = 4
                            yp = GlobalVarG2.gsy // 18 * 13
                        # bomba appiccicosa
                        if usa == 9:
                            attacco = 5
                            yp = GlobalVarG2.gsy // 18 * 14
                        # bomba potenziata
                        if usa == 10:
                            attacco = 6
                            yp = GlobalVarG2.gsy // 18 * 15
                        usa = 0
                        usadue = False
                    elif voceMarcata == 2:
                        voceMarcata = 0
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        xp = GlobalVarG2.gsx // 32 * 1
                        if usa == 1:
                            yp = GlobalVarG2.gsy // 18 * 5
                        if usa == 2:
                            yp = GlobalVarG2.gsy // 18 * 6
                        if usa == 3:
                            yp = GlobalVarG2.gsy // 18 * 7
                        if usa == 4:
                            yp = GlobalVarG2.gsy // 18 * 8
                        if usa == 5:
                            yp = GlobalVarG2.gsy // 18 * 9
                        if usa == 6:
                            yp = GlobalVarG2.gsy // 18 * 11
                        if usa == 7:
                            yp = GlobalVarG2.gsy // 18 * 12
                        if usa == 8:
                            yp = GlobalVarG2.gsy // 18 * 13
                        if usa == 9:
                            yp = GlobalVarG2.gsy // 18 * 14
                        if usa == 10:
                            yp = GlobalVarG2.gsy // 18 * 15
                        usa = 0
                        usadue = False

                    # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                    if usadue:
                        if oggetton == 1:
                            if dati[31] > 0:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                usa = 1
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 2:
                            if dati[32] > 0:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                usa = 2
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 3:
                            if dati[33] > 0:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                usa = 3
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 4:
                            if dati[34] > 0:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                usa = 4
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 5:
                            if dati[35] > 0:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                usa = 5
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 6:
                            if dati[36] > 0:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                usa = 6
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 7:
                            if dati[37] > 0:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                usa = 7
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 8:
                            if dati[38] > 0:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                usa = 8
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 9:
                            if dati[39] > 0:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                usa = 9
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 10:
                            if dati[40] > 0:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                usa = 10
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_q or tastop == pygame.K_SPACE or ((tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w and voceMarcata == 0:
                if oggetton != 1 and oggetton != 6:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    oggetton = oggetton - 1
                    yp = yp - GlobalVarG2.gsy // 18 * 1
                elif oggetton == 6:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    oggetton = oggetton - 1
                    yp = yp - GlobalVarG2.gsy // 18 * 2
                elif oggetton == 1:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 15
                    oggetton = 10
            if tastop == pygame.K_a and voceMarcata != 0:
                if voceMarcata == 2:
                    voceMarcata -= 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = xp - GlobalVarG2.gsx // 32 * 3
            if tastop == pygame.K_s and voceMarcata == 0:
                if oggetton != 10 and oggetton != 5:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    oggetton = oggetton + 1
                    yp = yp + GlobalVarG2.gsy // 18 * 1
                elif oggetton == 5:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    oggetton = oggetton + 1
                    yp = yp + GlobalVarG2.gsy // 18 * 2
                elif oggetton == 10:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 5
                    oggetton = 1
            if tastop == pygame.K_d and voceMarcata != 0:
                if voceMarcata == 1:
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = xp + GlobalVarG2.gsx // 32 * 3
            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 12.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))

            # menu conferma
            if usa != 0:
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 12.5, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 4))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 12.5))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5))
                # posizionare il cursore su menu usa
                if usauno:
                    xpv = xp
                    ypv = yp
                    xp = GlobalVarG2.gsx // 32 * 15
                    yp = GlobalVarG2.gsy // 18 * 15.1
                    voceMarcata = 2
                    usauno = False
                GlobalVarG2.schermo.blit(puntatorevecchio, (xpv, ypv))
                messaggio("Usare?", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 13.3, GlobalVarG2.gsy // 18 * 13.2, 80)
                messaggio("Si", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 13, GlobalVarG2.gsy // 18 * 15, 60)
                messaggio("No", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 15, 60)

            # pozione, carica batt, bomba, antidoto, bomba veleno, esca, super poz, carica migliorato, bomba pot, bomba atomica
            messaggio("Oggetti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
            if dati[31] >= 0:
                messaggio("Pozione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 5, 45)
                messaggio("x %i" % dati[31], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 5, 45)
                if oggetton == 1:
                    messaggio("Pozione:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Recupera 100 pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 5, 45)
            if dati[32] >= 0:
                messaggio("Caricabatterie", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6, 45)
                messaggio("x %i" % dati[32], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 6, 45)
                if oggetton == 2:
                    messaggio("Caricabatterie:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Recupera 250 pe di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6, 45)
            if dati[33] >= 0:
                messaggio("Medicina", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7, 45)
                messaggio("x %i" % dati[33], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 7, 45)
                if oggetton == 3:
                    messaggio("Medicina:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Cura avvelenamento a Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7, 45)
            if dati[34] >= 0:
                messaggio("Super pozione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8, 45)
                messaggio("x %i" % dati[34], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 8, 45)
                if oggetton == 4:
                    messaggio("Super pozione:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Recupera 300 pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8, 45)
            if dati[35] >= 0:
                messaggio("Carica plus", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9, 45)
                messaggio("x %i" % dati[35], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 9, 45)
                if oggetton == 5:
                    messaggio("Carica plus:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Recupera 600 pe di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9, 45)
            if dati[36] >= 0:
                messaggio("Bomba", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11, 45)
                messaggio("x %i" % dati[36], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 11, 45)
                if oggetton == 6:
                    messaggio("Bomba:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Infligge un po' di danni ai nemici su cui viene lanciata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20,
                              GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11, 45)
            if dati[37] >= 0:
                messaggio("Bomba velenosa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12, 45)
                messaggio("x %i" % dati[37], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 12, 45)
                if oggetton == 7:
                    messaggio("Bomba velenosa:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Infligge avvelenamento al nemico su cui viene lanciata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20,
                              GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12, 45)
            if dati[38] >= 0:
                messaggio("Esca", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13, 45)
                messaggio("x %i" % dati[38], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 13, 45)
                if oggetton == 8:
                    messaggio("Esca:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Distrae i nemici finché non viene distrutta. È possibile", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20,
                              GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("riprenderla passandoci sopra", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13, 45)
            if dati[39] >= 0:
                messaggio("Bomba appiccicosa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14, 45)
                messaggio("x %i" % dati[39], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 14, 45)
                if oggetton == 9:
                    messaggio("Bomba appiccicosa:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Dimezza la velocità del nemico su cui viene lanciata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20,
                              GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14, 45)
            if dati[40] >= 0:
                messaggio("Bomba potenziata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15, 45)
                messaggio("x %i" % dati[40], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 15, 45)
                if oggetton == 10:
                    messaggio("Bomba potenziata:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Infligge molti danni ai nemici su cui viene lanciata in un", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20,
                              GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("vasto raggio", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15, 45)

            # vita-status personaggio
            if dati[5] < 0:
                dati[5] = 0
            messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 4, 50)
            messaggio("Status alterativi: ", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 5, 50)
            persmen = pygame.transform.scale(GlobalVarG2.persGrafMenu, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
            GlobalVarG2.schermo.blit(persmen, (GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(sfondostastart, (GlobalVarG2.gsx // 32 * 14, (GlobalVarG2.gsy // 18 * 6) + (GlobalVarG2.gpy // 8)))
            if dati[121]:
                avvelenato = pygame.transform.scale(GlobalVarG2.avvelenatoo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                GlobalVarG2.schermo.blit(avvelenato, (GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 6))
            if dati[123] > 0:
                attaccopiu = pygame.transform.scale(GlobalVarG2.attaccopiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                GlobalVarG2.schermo.blit(attaccopiu, ((GlobalVarG2.gsx // 32 * 14) + (2 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 6))
            if dati[124] > 0:
                difesapiu = pygame.transform.scale(GlobalVarG2.difesapiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                GlobalVarG2.schermo.blit(difesapiu, ((GlobalVarG2.gsx // 32 * 14) + (4 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 6))
            # vita-status robo
            if dati[10] < 0:
                dati[10] = 0
            messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 9, 50)
            messaggio("Status alterativi: ", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 10, 50)
            robomen = pygame.transform.scale(GlobalVarG2.robograf, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
            GlobalVarG2.schermo.blit(robomen, (GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 8))
            GlobalVarG2.schermo.blit(sfondostastart, (GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 11))
            if dati[122] > 0:
                surriscaldato = pygame.transform.scale(GlobalVarG2.surriscaldatoo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                GlobalVarG2.schermo.blit(surriscaldato, (GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 11))
            if dati[125] > 0:
                velocitapiu = pygame.transform.scale(GlobalVarG2.velocitapiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                GlobalVarG2.schermo.blit(velocitapiu, ((GlobalVarG2.gsx // 32 * 14) + (2 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 11))
            if dati[126] > 0:
                efficienzapiu = pygame.transform.scale(GlobalVarG2.efficienzapiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                GlobalVarG2.schermo.blit(efficienzapiu, ((GlobalVarG2.gsx // 32 * 14) + (4 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 11))

            if attacco != 0:
                risposta = True

            messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
            GlobalVarG2.schermo.blit(imgOggetti[oggetton - 1], (GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 3))
            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            if usa == 0:
                pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, ((xp + (int(GlobalVarG2.gpx // 1.5))), yp + (int(GlobalVarG2.gpy * 0.7))), (xp + (int(GlobalVarG2.gpx * 9.5)), yp + (int(GlobalVarG2.gpy * 0.7))), 2)
            else:
                pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, ((xpv + (int(GlobalVarG2.gpx // 1.5))), ypv + (int(GlobalVarG2.gpy * 0.7))), (xpv + (int(GlobalVarG2.gpx * 9.5)), ypv + (int(GlobalVarG2.gpy * 0.7))), 2)

            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)
    return dati, attacco


def chiediconferma(conferma, canzone):
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    xp = GlobalVarG2.gsx // 32 * 17.5
    yp = GlobalVarG2.gsy // 18 * 10.3

    tastop = 0
    tastotempfps = 5

    GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
    if conferma == 1:
        messaggio(u"Tornare al menu principale?", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 6.5, 120)
    elif conferma == 2:
        messaggio("Tornare a Windows?", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 6.5, 120)
    messaggio("Si", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 9.5, 120)
    messaggio("No", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 9.5, 120)
    messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
    GlobalVarG2.schermo.blit(puntatore, (xp, yp))
    pygame.display.update()
    voceMarcata = 2
    while True:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 2

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
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
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
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        if conferma == 1:
                            return True, True
                        elif conferma == 2:
                            pygame.quit()
                            quit()
                    elif voceMarcata == 2:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        return False, False
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_SPACE or ((tastop == pygame.K_a or tastop == pygame.K_d) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_a:
                if voceMarcata == 2:
                    voceMarcata -= 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 9.5
            if tastop == pygame.K_d:
                if voceMarcata == 1:
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 17.5
            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            if conferma == 1:
                messaggio(u"Tornare al menu principale?", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 6.5, 120)
            elif conferma == 2:
                messaggio("Tornare a Windows?", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 6.5, 120)
            messaggio("Si", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 9.5, 120)
            messaggio("No", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 9.5, 120)
            messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)


def start(dati, nmost, porteini, portefin, cofaniini, cofanifin, porte, cofanetti, apriocchio):
    sfondostastart = pygame.transform.scale(GlobalVarG2.sfondostax3, (GlobalVarG2.gpx * 4, GlobalVarG2.gpy))
    perssta = pygame.transform.scale(GlobalVarG2.persGrafMenu, (GlobalVarG2.gpx * 10, GlobalVarG2.gpy * 10))
    robosta = pygame.transform.scale(GlobalVarG2.robograf, (GlobalVarG2.gpx * 10, GlobalVarG2.gpy * 10))
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    avvelenatosta = pygame.transform.scale(GlobalVarG2.avvelenatoo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    surriscaldatosta = pygame.transform.scale(GlobalVarG2.surriscaldatoo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    attaccopiusta = pygame.transform.scale(GlobalVarG2.attaccopiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    difesapiusta = pygame.transform.scale(GlobalVarG2.difesapiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    velocitapiusta = pygame.transform.scale(GlobalVarG2.velocitapiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    efficienzapiusta = pygame.transform.scale(GlobalVarG2.efficienzapiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    if dati[133] == 0:
        faretraFrecceStart = GlobalVarG2.faretraFrecceStart0
        maxFrecce = 1
    elif dati[133] == 1:
        faretraFrecceStart = GlobalVarG2.faretraFrecceStart1
        maxFrecce = 5
    elif dati[133] == 2:
        faretraFrecceStart = GlobalVarG2.faretraFrecceStart2
        maxFrecce = 20
    elif dati[133] == 3:
        faretraFrecceStart = GlobalVarG2.faretraFrecceStart3
        maxFrecce = 60
    else:
        faretraFrecceStart = 0
        maxFrecce = 0
    xp = GlobalVarG2.gsx // 32 * 1
    yp = GlobalVarG2.gsy // 18 * 5
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

        GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 12.5))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 4))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 15.5))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))
        messaggio("Menu start", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
        messaggio("Oggetti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 5, 50)
        messaggio("Equipaggiamento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6, 50)
        messaggio("Setta Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7, 50)
        messaggio("Mappa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8, 50)
        messaggio("Diario", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9, 50)
        messaggio("Impostazioni", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12, 50)
        if nmost == -1:
            messaggio("Salva", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13, 50)
        else:
            messaggio("Salva", GlobalVarG2.grigioscu, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13, 50)
        messaggio(u"Torna al menu principale", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14, 50)
        messaggio("Torna a Windows", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15, 50)
        messaggio(u"Esc / Q: Esci dal menu", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 1, 50)
        if carim:
            if dati[10] <= 0:
                robosta = GlobalVarG2.robograff
                robosta = pygame.transform.scale(robosta, (GlobalVarG2.gpx * 10, GlobalVarG2.gpy * 10))
            else:
                robosta = GlobalVarG2.robograf
                robosta = pygame.transform.scale(robosta, (GlobalVarG2.gpx * 10, GlobalVarG2.gpy * 10))
            carim = False

        # vita-status personaggio
        if dati[5] < 0:
            dati[5] = 0
        messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 13.5, GlobalVarG2.gsy // 18 * 13, 50)
        messaggio("Lv:  " + str(dati[4]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 13.5, GlobalVarG2.gsy // 18 * 14, 50)
        if dati[4] < 100:
            messaggio("Esp:  " + str(dati[127]) + " / " + str(esptot), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 14,
                      50)
        else:
            messaggio("Esp:  -- / --", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 14, 50)
        messaggio("Status alterativi: ", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 13.5, GlobalVarG2.gsy // 18 * 15, 50)
        GlobalVarG2.schermo.blit(sfondostastart, (GlobalVarG2.gsx // 32 * 13.5, (GlobalVarG2.gsy // 18 * 16) + (GlobalVarG2.gpy // 8)))
        if dati[121]:
            GlobalVarG2.schermo.blit(avvelenatosta, (GlobalVarG2.gsx // 32 * 13.5, GlobalVarG2.gsy // 18 * 16))
        if dati[123] > 0:
            GlobalVarG2.schermo.blit(attaccopiusta, ((GlobalVarG2.gsx // 32 * 13.5) + (2 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 16))
        if dati[124] > 0:
            GlobalVarG2.schermo.blit(difesapiusta, ((GlobalVarG2.gsx // 32 * 13.5) + (4 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 16))
        # vita-status robo
        if dati[10] < 0:
            dati[10] = 0
        messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23.5, GlobalVarG2.gsy // 18 * 13, 50)
        messaggio("Status alterativi: ", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23.5, GlobalVarG2.gsy // 18 * 14, 50)
        GlobalVarG2.schermo.blit(sfondostastart, (GlobalVarG2.gsx // 32 * 23.5, (GlobalVarG2.gsy // 18 * 15) + (GlobalVarG2.gpy // 8)))
        if dati[122] > 0:
            GlobalVarG2.schermo.blit(surriscaldatosta, (GlobalVarG2.gsx // 32 * 23.5, GlobalVarG2.gsy // 18 * 15))
        if dati[125] > 0:
            GlobalVarG2.schermo.blit(velocitapiusta, ((GlobalVarG2.gsx // 32 * 23.5) + (2 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 15))
        if dati[126] > 0:
            GlobalVarG2.schermo.blit(efficienzapiusta, ((GlobalVarG2.gsx // 32 * 23.5) + (4 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 15))

        if attacco != 0:
            risposta = True

        if faretraFrecceStart != 0:
            GlobalVarG2.schermo.blit(faretraFrecceStart, (GlobalVarG2.gsx // 32 * 21.5, GlobalVarG2.gsy // 18 * 2.5))
            messaggio("Frecce: " + str(dati[132]) + " / " + str(maxFrecce), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 21.5, GlobalVarG2.gsy // 18 * 6, 50)
        GlobalVarG2.schermo.blit(GlobalVarG2.sacchettoDenaroStart, (GlobalVarG2.gsx // 32 * 26.5, GlobalVarG2.gsy // 18 * 2.5))
        messaggio("Monete: " + str(dati[131]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 26.5, GlobalVarG2.gsy // 18 * 6, 50)

        GlobalVarG2.schermo.blit(perssta, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 2))
        GlobalVarG2.schermo.blit(robosta, (GlobalVarG2.gsx // 32 * 21, GlobalVarG2.gsy // 18 * 2))
        GlobalVarG2.schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(GlobalVarG2.c27)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 2

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
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
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
                    if voceMarcata != 7 or (voceMarcata == 7 and nmost == -1):
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    inizio = False
                    # oggetti
                    if voceMarcata == 1:
                        dati, attacco = oggetti(dati, GlobalVarG2.c27)
                        carim = True
                    # equip pers
                    if voceMarcata == 2:
                        dati = equip(dati, GlobalVarG2.c27)
                        carim = True
                    # equip robot
                    if voceMarcata == 3:
                        dati = equiprobo(dati, GlobalVarG2.c27)
                        carim = True
                    # mappa
                    if voceMarcata == 4:
                        print ("mappa")
                    # diario
                    if voceMarcata == 5:
                        print ("diario")
                    # impostazioni
                    if voceMarcata == 6:
                        menuImpostazioni(GlobalVarG2.c27, False)
                    # salva
                    if voceMarcata == 7:
                        #if nmost == -1:
                        n = scegli_sal(3, len(dati), GlobalVarG2.c27)
                        if n != -1:
                            salvataggio(n, dati, porteini, portefin, cofaniini, cofanifin, porte, cofanetti)
                    # menu
                    if voceMarcata == 8:
                        conferma = 1
                    # chiudi
                    if voceMarcata == 9:
                        conferma = 2
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_SPACE or ((tastop == pygame.K_s or tastop == pygame.K_w) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_s:
                if voceMarcata != 5 and voceMarcata != 9:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = yp + GlobalVarG2.gsy // 18 * 1
                    voceMarcata += 1
                else:
                    if voceMarcata == 5:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = yp + GlobalVarG2.gsy // 18 * 3
                        voceMarcata += 1
                    elif voceMarcata == 9:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 5
                        voceMarcata = 1
            if tastop == pygame.K_w:
                if voceMarcata != 6 and voceMarcata != 1:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = yp - GlobalVarG2.gsy // 18 * 1
                    voceMarcata -= 1
                else:
                    if voceMarcata == 6:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = yp - GlobalVarG2.gsy // 18 * 3
                        voceMarcata -= 1
                    elif voceMarcata == 1:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 15
                        voceMarcata = 9
            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

            # chiedere conferma per uscire
            if conferma != 0:
                inizio, risposta = chiediconferma(conferma, GlobalVarG2.c27)
                conferma = 0

            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 12.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))
            messaggio("Menu start", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
            messaggio("Oggetti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 5, 50)
            messaggio("Equipaggiamento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6, 50)
            messaggio("Setta Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7, 50)
            messaggio("Mappa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8, 50)
            messaggio("Diario", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9, 50)
            messaggio("Impostazioni", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12, 50)
            if nmost == -1:
                messaggio("Salva", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13, 50)
            else:
                messaggio("Salva", GlobalVarG2.grigioscu, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13, 50)
            messaggio(u"Torna al menu principale", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14, 50)
            messaggio("Torna a Windows", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15, 50)
            messaggio(u"Esc / Q: Esci dal menu", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 1, 50)
            if carim:
                if dati[10] <= 0:
                    robosta = GlobalVarG2.robograff
                    robosta = pygame.transform.scale(robosta, (GlobalVarG2.gpx * 10, GlobalVarG2.gpy * 10))
                else:
                    robosta = GlobalVarG2.robograf
                    robosta = pygame.transform.scale(robosta, (GlobalVarG2.gpx * 10, GlobalVarG2.gpy * 10))
                carim = False

            # vita-status personaggio
            if dati[5] < 0:
                dati[5] = 0
            messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 13.5, GlobalVarG2.gsy // 18 * 13, 50)
            messaggio("Lv:  " + str(dati[4]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 13.5, GlobalVarG2.gsy // 18 * 14, 50)
            if dati[4] < 100:
                messaggio("Esp:  " + str(dati[127]) + " / " + str(esptot), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 14, 50)
            else:
                messaggio("Esp:  -- / --", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 14, 50)
            messaggio("Status alterativi: ", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 13.5, GlobalVarG2.gsy // 18 * 15, 50)
            GlobalVarG2.schermo.blit(sfondostastart, (GlobalVarG2.gsx // 32 * 13.5, (GlobalVarG2.gsy // 18 * 16) + (GlobalVarG2.gpy // 8)))
            if dati[121]:
                GlobalVarG2.schermo.blit(avvelenatosta, (GlobalVarG2.gsx // 32 * 13.5, GlobalVarG2.gsy // 18 * 16))
            if dati[123] > 0:
                GlobalVarG2.schermo.blit(attaccopiusta, ((GlobalVarG2.gsx // 32 * 13.5) + (2 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 16))
            if dati[124] > 0:
                GlobalVarG2.schermo.blit(difesapiusta, ((GlobalVarG2.gsx // 32 * 13.5) + (4 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 16))
            # vita-status robo
            if dati[10] < 0:
                dati[10] = 0
            messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23.5, GlobalVarG2.gsy // 18 * 13, 50)
            messaggio("Status alterativi: ", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23.5, GlobalVarG2.gsy // 18 * 14, 50)
            GlobalVarG2.schermo.blit(sfondostastart, (GlobalVarG2.gsx // 32 * 23.5, (GlobalVarG2.gsy // 18 * 15) + (GlobalVarG2.gpy // 8)))
            if dati[122] > 0:
                GlobalVarG2.schermo.blit(surriscaldatosta, (GlobalVarG2.gsx // 32 * 23.5, GlobalVarG2.gsy // 18 * 15))
            if dati[125] > 0:
                GlobalVarG2.schermo.blit(velocitapiusta, ((GlobalVarG2.gsx // 32 * 23.5) + (2 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 15))
            if dati[126] > 0:
                GlobalVarG2.schermo.blit(efficienzapiusta, ((GlobalVarG2.gsx // 32 * 23.5) + (4 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 15))

            if attacco != 0:
                risposta = True

            if faretraFrecceStart != 0:
                GlobalVarG2.schermo.blit(faretraFrecceStart, (GlobalVarG2.gsx // 32 * 21.5, GlobalVarG2.gsy // 18 * 2.5))
                messaggio("Frecce: " + str(dati[132]) + " / " + str(maxFrecce), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 21.5, GlobalVarG2.gsy // 18 * 6, 50)
            GlobalVarG2.schermo.blit(GlobalVarG2.sacchettoDenaroStart, (GlobalVarG2.gsx // 32 * 26.5, GlobalVarG2.gsy // 18 * 2.5))
            messaggio("Monete: " + str(dati[131]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 26.5, GlobalVarG2.gsy // 18 * 6, 50)

            GlobalVarG2.schermo.blit(perssta, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 2))
            GlobalVarG2.schermo.blit(robosta, (GlobalVarG2.gsx // 32 * 21, GlobalVarG2.gsy // 18 * 2))
            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            if not risposta:
                pygame.display.update()
            else:
                GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)
    GlobalVarG2.canaleSoundCanzone.stop()
    return dati, inizio, attacco


def startBattaglia(dati, animaOggetto, x, y, npers, rx, ry):
    xp = GlobalVarG2.gpx * 1
    yp = GlobalVarG2.gpy * 5
    sconosciutoOggetto = pygame.transform.scale(GlobalVarG2.sconosciutoOggettoMenu, (GlobalVarG2.gpx * 4, GlobalVarG2.gpy * 4))
    sconosciutoOggettoIco = pygame.transform.scale(GlobalVarG2.sconosciutoOggettoIcoMenu, (GlobalVarG2.gpx, GlobalVarG2.gpy))

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
            vettoreOggettiGraf.append(GlobalVarG2.vetImgOggettiStart[oggetton - 1])
            vettoreOggettiIco.append(GlobalVarG2.vetIcoOggettiMenu[oggetton - 1])
        else:
            vettoreOggettiGraf.append(sconosciutoOggetto)
            vettoreOggettiIco.append(sconosciutoOggettoIco)
        oggetton += 1

    # primo frame
    if True:
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoStartBattaglia, (0, 0))
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
        GlobalVarG2.schermo.blit(vettoreOggettiGraf[disegnoOggetto], (GlobalVarG2.gpx // 2, GlobalVarG2.gpy * 1))
        if dati[disegnoOggetto + 31] <= 0:
            GlobalVarG2.schermo.blit(GlobalVarG2.puntatOut, (xp, yp))
            qta = 0
        else:
            GlobalVarG2.schermo.blit(GlobalVarG2.puntatIn, (xp, yp))
            qta = dati[disegnoOggetto + 31]
        messaggio("x%i" % qta, GlobalVarG2.grigiochi, (GlobalVarG2.gpx * 4) + (GlobalVarG2.gpx // 2), GlobalVarG2.gpy * 3, 80)
        disegnati = 0
        i = 0
        while i < 10:
            if difensivi and (i == 0 or i == 1 or i == 2 or i == 3 or i == 4):
                GlobalVarG2.schermo.blit(vettoreOggettiIco[i], (GlobalVarG2.gpx * (disegnati + 1), GlobalVarG2.gpy * 5))
                disegnati += 1
            if offensivi and (i == 5 or i == 6 or i == 7 or i == 8 or i == 9):
                GlobalVarG2.schermo.blit(vettoreOggettiIco[i], (GlobalVarG2.gpx * (disegnati + 1), (GlobalVarG2.gpy * 5) + (GlobalVarG2.gpy // 2)))
                disegnati += 1
            i += 1
        if difensivi:
            if voceMarcata == 1:
                messaggio("Pozione", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
            if voceMarcata == 2:
                messaggio("Caricabatterie", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
            if voceMarcata == 3:
                messaggio("Medicina", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
            if voceMarcata == 4:
                messaggio("Super pozione", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
            if voceMarcata == 5:
                messaggio("Carica plus", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
            GlobalVarG2.schermo.blit(GlobalVarG2.scorriGiu, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 6))
        if offensivi:
            if voceMarcata == 1:
                messaggio("Bomba", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
            if voceMarcata == 2:
                messaggio("Bomba velenosa", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
            if voceMarcata == 3:
                messaggio("Esca", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
            if voceMarcata == 4:
                messaggio("Bomba appiccicosa", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
            if voceMarcata == 5:
                messaggio("Bomba potenziata", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
            GlobalVarG2.schermo.blit(GlobalVarG2.scorriSu, (GlobalVarG2.gpx * 3, (GlobalVarG2.gpy * 5) - (GlobalVarG2.gpy // 2)))

        if not risposta:
            pygame.display.update()

    while not risposta:
        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 2

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
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
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
                        if voceMarcata == 2 and dati[32] > 0 and (abs(x - rx) + abs(y - ry)) <= GlobalVarG2.gpx:
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
                        if voceMarcata == 5 and dati[35] > 0 and (abs(x - rx) + abs(y - ry)) <= GlobalVarG2.gpx:
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
                        if offensivi:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_SPACE or ((tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d or tastop == pygame.K_w) and tastotempfps == 0):
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w:
                if offensivi:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gpy * 5
                    offensivi = False
                    difensivi = True
            if tastop == pygame.K_a:
                if voceMarcata != 1:
                    voceMarcata -= 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = xp - GlobalVarG2.gpx
                else:
                    voceMarcata += 4
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gpx * 5
            if tastop == pygame.K_s:
                if difensivi:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = (GlobalVarG2.gpy * 5) + (GlobalVarG2.gpy // 2)
                    difensivi = False
                    offensivi = True
            if tastop == pygame.K_d:
                if voceMarcata != 5:
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = xp + GlobalVarG2.gpx
                else:
                    voceMarcata -= 4
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gpx * 1
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoStartBattaglia, (0, 0))
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
            GlobalVarG2.schermo.blit(vettoreOggettiGraf[disegnoOggetto], (GlobalVarG2.gpx // 2, GlobalVarG2.gpy * 1))
            if dati[disegnoOggetto + 31] <= 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.puntatOut, (xp, yp))
                qta = 0
            elif (disegnoOggetto == 1 or disegnoOggetto == 4) and abs(x - rx) + abs(y - ry) > GlobalVarG2.gpx:
                GlobalVarG2.schermo.blit(GlobalVarG2.puntatOut, (xp, yp))
                qta = dati[disegnoOggetto + 31]
            else:
                GlobalVarG2.schermo.blit(GlobalVarG2.puntatIn, (xp, yp))
                qta = dati[disegnoOggetto + 31]
            messaggio("x%i" % qta, GlobalVarG2.grigiochi, (GlobalVarG2.gpx * 4) + (GlobalVarG2.gpx // 2), GlobalVarG2.gpy * 3, 80)
            disegnati = 0
            i = 0
            while i < 10:
                if difensivi and (i == 0 or i == 1 or i == 2 or i == 3 or i == 4):
                    GlobalVarG2.schermo.blit(vettoreOggettiIco[i], (GlobalVarG2.gpx * (disegnati + 1), GlobalVarG2.gpy * 5))
                    disegnati += 1
                if offensivi and (i == 5 or i == 6 or i == 7 or i == 8 or i == 9):
                    GlobalVarG2.schermo.blit(vettoreOggettiIco[i], (GlobalVarG2.gpx * (disegnati + 1), (GlobalVarG2.gpy * 5) + (GlobalVarG2.gpy // 2)))
                    disegnati += 1
                i += 1
            if difensivi:
                if voceMarcata == 1:
                    messaggio("Pozione", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                if voceMarcata == 2:
                    messaggio("Caricabatterie", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                if voceMarcata == 3:
                    messaggio("Medicina", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                if voceMarcata == 4:
                    messaggio("Super pozione", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                if voceMarcata == 5:
                    messaggio("Carica plus", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                GlobalVarG2.schermo.blit(GlobalVarG2.scorriGiu, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 6))
            if offensivi:
                if voceMarcata == 1:
                    messaggio("Bomba", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                if voceMarcata == 2:
                    messaggio("Bomba velenosa", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                if voceMarcata == 3:
                    messaggio("Esca", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                if voceMarcata == 4:
                    messaggio("Bomba appiccicosa", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                if voceMarcata == 5:
                    messaggio("Bomba potenziata", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                GlobalVarG2.schermo.blit(GlobalVarG2.scorriSu, (GlobalVarG2.gpx * 3, (GlobalVarG2.gpy * 5) - (GlobalVarG2.gpy // 2)))

            if not risposta:
                pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)
    return dati, attacco, sposta, animaOggetto, npers


def menuMercante(dati):
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatorevecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    sconosciutoOggetto = pygame.transform.scale(GlobalVarG2.sconosciutoOggettoMenu, (GlobalVarG2.gpx * 10, GlobalVarG2.gpy * 10))
    xp = GlobalVarG2.gsx // 32 * 10.5
    yp = GlobalVarG2.gsy // 18 * 6.1
    xpv = xp
    ypv = yp
    usauno = False
    usa = 0
    risposta = False
    oggetton = 0
    voceMarcata = 0
    numeroOggettiAcquistati = 1
    moneteInsufficienti = False
    inventarioPieno = False
    primoFrame = True

    maxFrecce = 1
    if dati[133] == 1:
        maxFrecce = 5
    elif dati[133] == 2:
        maxFrecce = 20
    elif dati[133] == 3:
        maxFrecce = 60

    tastop = 0
    tastotempfps = 5

    imgOggetti = []
    i = 1
    while i <= 10:
        if (i == 1 and dati[0] > -1) or (i == 2 and dati[0] > -1) or (i == 3 and dati[0] > -1) or (i == 4 and dati[0] > -1) or (i == 5 and dati[0] > -1) or (i == 6 and dati[0] > -1) or (i == 7 and dati[0] > -1) or (i == 8 and dati[0] > -1) or (i == 9 and dati[0] > -1) or (i == 10 and dati[0] > -1):
            imgOggetti.append(GlobalVarG2.vetImgOggettiMercante[i - 1])
        else:
            imgOggetti.append(sconosciutoOggetto)
        i += 1

    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(GlobalVarG2.c27)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 2

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
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    numeroOggettiAcquistati = 1
                    moneteInsufficienti = False
                    inventarioPieno = False
                    tastoTrovato = True
                    voceMarcata = 0
                    if usa != 0:
                        xp = GlobalVarG2.gsx // 32 * 10.5
                        if usa == -1:
                            yp = GlobalVarG2.gsy // 18 * 6.1
                        if usa == 1:
                            yp = GlobalVarG2.gsy // 18 * 7
                        if usa == 2:
                            yp = GlobalVarG2.gsy // 18 * 7.9
                        if usa == 3:
                            yp = GlobalVarG2.gsy // 18 * 8.8
                        if usa == 4:
                            yp = GlobalVarG2.gsy // 18 * 9.7
                        if usa == 5:
                            yp = GlobalVarG2.gsy // 18 * 10.6
                        if usa == 6:
                            yp = GlobalVarG2.gsy // 18 * 11.5
                        if usa == 7:
                            yp = GlobalVarG2.gsy // 18 * 12.4
                        if usa == 8:
                            yp = GlobalVarG2.gsy // 18 * 13.3
                        if usa == 9:
                            yp = GlobalVarG2.gsy // 18 * 14.2
                        if usa == 10:
                            yp = GlobalVarG2.gsy // 18 * 15.1
                        if usa == 11:
                            yp = GlobalVarG2.gsy // 18 * 16
                        usa = 0
                    else:
                        risposta = True
                if event.key == pygame.K_s and not tastoTrovato:
                    moneteInsufficienti = False
                    inventarioPieno = False
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    moneteInsufficienti = False
                    inventarioPieno = False
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and voceMarcata != 0 and not tastoTrovato:
                    moneteInsufficienti = False
                    inventarioPieno = False
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and voceMarcata != 0 and not tastoTrovato:
                    moneteInsufficienti = False
                    inventarioPieno = False
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_SPACE and not tastoTrovato:
                    moneteInsufficienti = False
                    inventarioPieno = False
                    tastoTrovato = True
                    usadue = True

                    # usa?
                    if voceMarcata == 1:
                        if 0 <= oggetton <= 10 and GlobalVarG2.costoOggetti[oggetton] * numeroOggettiAcquistati <= dati[131]:
                            GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.rumoreAcquisto)
                            dati[131] -= GlobalVarG2.costoOggetti[oggetton] * numeroOggettiAcquistati
                            voceMarcata = 0
                            xp = GlobalVarG2.gsx // 32 * 10.5
                            # freccia
                            if usa == -1:
                                dati[132] += numeroOggettiAcquistati
                                yp = GlobalVarG2.gsy // 18 * 6.1
                            # pozione
                            if usa == 1:
                                dati[31] += numeroOggettiAcquistati
                                yp = GlobalVarG2.gsy // 18 * 7
                            # carica batt
                            if usa == 2:
                                dati[32] += numeroOggettiAcquistati
                                yp = GlobalVarG2.gsy // 18 * 7.9
                            # antidoto
                            if usa == 3:
                                dati[33] += numeroOggettiAcquistati
                                yp = GlobalVarG2.gsy // 18 * 8.8
                            # super pozione
                            if usa == 4:
                                dati[34] += numeroOggettiAcquistati
                                yp = GlobalVarG2.gsy // 18 * 9.7
                            # carica migliorato
                            if usa == 5:
                                dati[35] += numeroOggettiAcquistati
                                yp = GlobalVarG2.gsy // 18 * 10.6
                            # bomba
                            if usa == 6:
                                dati[36] += numeroOggettiAcquistati
                                yp = GlobalVarG2.gsy // 18 * 11.5
                            # bomba veleno
                            if usa == 7:
                                dati[37] += numeroOggettiAcquistati
                                yp = GlobalVarG2.gsy // 18 * 12.4
                            # esca
                            if usa == 8:
                                dati[38] += numeroOggettiAcquistati
                                yp = GlobalVarG2.gsy // 18 * 13.3
                            # bomba appiccicosa
                            if usa == 9:
                                dati[39] += numeroOggettiAcquistati
                                yp = GlobalVarG2.gsy // 18 * 14.2
                            # bomba potenziata
                            if usa == 10:
                                dati[40] += numeroOggettiAcquistati
                                yp = GlobalVarG2.gsy // 18 * 15.1
                            usa = 0
                            usadue = False
                        elif oggetton == 11:
                            if dati[133] == 0 and GlobalVarG2.costoOggetti[oggetton] * numeroOggettiAcquistati <= dati[131]:
                                GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.rumoreAcquisto)
                                dati[131] -= GlobalVarG2.costoOggetti[oggetton] * numeroOggettiAcquistati
                                voceMarcata = 0
                                xp = GlobalVarG2.gsx // 32 * 10.5
                                # faretra
                                if usa == 10:
                                    dati[40] += numeroOggettiAcquistati
                                    yp = GlobalVarG2.gsy // 18 * 15.1
                                usa = 0
                                usadue = False
                            elif dati[133] == 1 and GlobalVarG2.costoOggetti[oggetton + 1] * numeroOggettiAcquistati <= dati[131]:
                                GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.rumoreAcquisto)
                                dati[131] -= GlobalVarG2.costoOggetti[oggetton + 1] * numeroOggettiAcquistati
                                voceMarcata = 0
                                xp = GlobalVarG2.gsx // 32 * 10.5
                                # faretra
                                if usa == 10:
                                    dati[40] += numeroOggettiAcquistati
                                    yp = GlobalVarG2.gsy // 18 * 15.1
                                usa = 0
                                usadue = False
                            elif dati[133] == 2 and GlobalVarG2.costoOggetti[oggetton + 2] * numeroOggettiAcquistati <= dati[131]:
                                GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.rumoreAcquisto)
                                dati[131] -= GlobalVarG2.costoOggetti[oggetton + 2] * numeroOggettiAcquistati
                                voceMarcata = 0
                                xp = GlobalVarG2.gsx // 32 * 10.5
                                # faretra
                                if usa == 10:
                                    dati[40] += numeroOggettiAcquistati
                                    yp = GlobalVarG2.gsy // 18 * 15.1
                                usa = 0
                                usadue = False
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                                moneteInsufficienti = True
                                usadue = False
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                            moneteInsufficienti = True
                            usadue = False
                    elif voceMarcata == 2:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        voceMarcata = 0
                        numeroOggettiAcquistati = 1
                        moneteInsufficienti = False
                        inventarioPieno = False
                        xp = GlobalVarG2.gsx // 32 * 10.5
                        if usa == -1:
                            yp = GlobalVarG2.gsy // 18 * 6.1
                        if usa == 1:
                            yp = GlobalVarG2.gsy // 18 * 7
                        if usa == 2:
                            yp = GlobalVarG2.gsy // 18 * 7.9
                        if usa == 3:
                            yp = GlobalVarG2.gsy // 18 * 8.8
                        if usa == 4:
                            yp = GlobalVarG2.gsy // 18 * 9.7
                        if usa == 5:
                            yp = GlobalVarG2.gsy // 18 * 10.6
                        if usa == 6:
                            yp = GlobalVarG2.gsy // 18 * 11.5
                        if usa == 7:
                            yp = GlobalVarG2.gsy // 18 * 12.4
                        if usa == 8:
                            yp = GlobalVarG2.gsy // 18 * 13.3
                        if usa == 9:
                            yp = GlobalVarG2.gsy // 18 * 14.2
                        if usa == 10:
                            yp = GlobalVarG2.gsy // 18 * 15.1
                        if usa == 11:
                            yp = GlobalVarG2.gsy // 18 * 16
                        usa = 0
                        usadue = False

                    # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                    if usadue:
                        if 1 <= oggetton <= 10 and dati[30 + oggetton] < 99:
                            numeroOggettiAcquistati = 1
                            if oggetton == 1:
                                if imgOggetti[0] != sconosciutoOggetto:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                    usa = 1
                                    usauno = True
                                else:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                            if oggetton == 2:
                                if imgOggetti[1] != sconosciutoOggetto:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                    usa = 2
                                    usauno = True
                                else:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                            if oggetton == 3:
                                if imgOggetti[2] != sconosciutoOggetto:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                    usa = 3
                                    usauno = True
                                else:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                            if oggetton == 4:
                                if imgOggetti[3] != sconosciutoOggetto:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                    usa = 4
                                    usauno = True
                                else:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                            if oggetton == 5:
                                if imgOggetti[4] != sconosciutoOggetto:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                    usa = 5
                                    usauno = True
                                else:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                            if oggetton == 6:
                                if imgOggetti[5] != sconosciutoOggetto:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                    usa = 6
                                    usauno = True
                                else:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                            if oggetton == 7:
                                if imgOggetti[6] != sconosciutoOggetto:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                    usa = 7
                                    usauno = True
                                else:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                            if oggetton == 8:
                                if imgOggetti[7] != sconosciutoOggetto:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                    usa = 8
                                    usauno = True
                                else:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                            if oggetton == 9:
                                if imgOggetti[8] != sconosciutoOggetto:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                    usa = 9
                                    usauno = True
                                else:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                            if oggetton == 10:
                                if imgOggetti[9] != sconosciutoOggetto:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                    usa = 10
                                    usauno = True
                                else:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        elif oggetton == 0 and dati[132] < maxFrecce:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            usa = -1
                            usauno = True
                        elif oggetton == 11 and dati[133] != 3:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            usa = 11
                            usauno = True
                        else:
                            inventarioPieno = True
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_q or tastop == pygame.K_SPACE or ((tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame:
            primoFrame = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w:
                if voceMarcata == 0:
                    if oggetton != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        oggetton = oggetton - 1
                        yp = yp - GlobalVarG2.gsy // 18 * 0.9
                    elif oggetton == 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 16
                        oggetton = 11
                elif voceMarcata != 0:
                    if oggetton != 11:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        if 1 <= oggetton <= 10 and numeroOggettiAcquistati + dati[30 + oggetton] >= 99:
                            numeroOggettiAcquistati = 1
                        elif oggetton == 0 and numeroOggettiAcquistati + dati[132] < maxFrecce:
                            numeroOggettiAcquistati += 1
                        else:
                            numeroOggettiAcquistati = 1
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        numeroOggettiAcquistati = 1
            if tastop == pygame.K_a and voceMarcata != 0:
                if voceMarcata == 2:
                    voceMarcata -= 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = xp - GlobalVarG2.gsx // 32 * 4
            if tastop == pygame.K_s:
                if voceMarcata == 0:
                    if oggetton != 11:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        oggetton = oggetton + 1
                        yp = yp + GlobalVarG2.gsy // 18 * 0.9
                    elif oggetton == 11:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 6.1
                        oggetton = 0
                elif voceMarcata != 0:
                    if oggetton != 11:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        if 1 <= oggetton <= 10 and numeroOggettiAcquistati == 1:
                            numeroOggettiAcquistati = 99 - dati[30 + oggetton]
                        elif oggetton == 0 and numeroOggettiAcquistati == 1:
                            numeroOggettiAcquistati = maxFrecce - dati[132]
                        else:
                            numeroOggettiAcquistati -= 1
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        numeroOggettiAcquistati = 1
            if tastop == pygame.K_d and voceMarcata != 0:
                if voceMarcata == 1:
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = xp + GlobalVarG2.gsx // 32 * 4

            maxFrecce = 1
            if dati[133] == 1:
                maxFrecce = 5
            elif dati[133] == 2:
                maxFrecce = 20
            elif dati[133] == 3:
                maxFrecce = 60

            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 13.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 16.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 16.5))

            GlobalVarG2.schermo.blit(GlobalVarG2.sacchettoDenaroMercante, (GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 14))
            messaggio("Monete: " + str(dati[131]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 26, GlobalVarG2.gsy // 18 * 15.8, 50)

            GlobalVarG2.schermo.blit(GlobalVarG2.mercanteGraf, (GlobalVarG2.gsx // 32 * 0, GlobalVarG2.gsy // 18 * 8.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoDialogoMercante, (GlobalVarG2.gsx // 32 * 0.5, GlobalVarG2.gsy // 18 * 4))
            if moneteInsufficienti:
                messaggio("Non hai abbastanza monete!", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 2.1, GlobalVarG2.gsy // 18 * 6.1, 40)
            if inventarioPieno:
                messaggio("Non puoi prenderne altri...", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 2.4, GlobalVarG2.gsy // 18 * 5.3, 40)
            if usa == 0:
                messaggio("Prendi quello che ti serve", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4.5, 50)
            else:
                messaggio("Quanti te ne servono?", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4.5, 50)

            messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
            if 1 <= oggetton <= 10:
                GlobalVarG2.schermo.blit(imgOggetti[oggetton - 1], (GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3))
            elif oggetton == 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.frecciaMenu, (GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3))
            elif oggetton == 11:
                if dati[133] == 0:
                    GlobalVarG2.schermo.blit(GlobalVarG2.faretra1Menu, (GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3))
                elif dati[133] == 1:
                    GlobalVarG2.schermo.blit(GlobalVarG2.faretra2Menu, (GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3))
                else:
                    GlobalVarG2.schermo.blit(GlobalVarG2.faretra3Menu, (GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3))

            # menu conferma
            if usa != 0:
                # posizionare il cursore sul menu compra
                if usauno:
                    xpv = xp
                    ypv = yp
                    xp = GlobalVarG2.gsx // 32 * 5.3
                    yp = GlobalVarG2.gsy // 18 * 6.9
                    voceMarcata = 2
                    usauno = False
                GlobalVarG2.schermo.blit(puntatorevecchio, (xpv, ypv))
                messaggio("x" + str(numeroOggettiAcquistati), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 7.5, GlobalVarG2.gsy // 18 * 4.5, 50)
                if oggetton == 11:
                    GlobalVarG2.schermo.blit(GlobalVarG2.scorriSuGiuBloccato, (GlobalVarG2.gsx // 32 * 8.5, GlobalVarG2.gsy // 18 * 4.3))
                    if dati[133] == 1:
                        messaggio("(Monete necessarie: %i)" % (GlobalVarG2.costoOggetti[oggetton + 1] * numeroOggettiAcquistati), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 5.3, 50)
                    elif dati[133] >= 2:
                        messaggio("(Monete necessarie: %i)" % (GlobalVarG2.costoOggetti[oggetton + 2] * numeroOggettiAcquistati), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 5.3, 50)
                    else:
                        messaggio("(Monete necessarie: %i)" % (GlobalVarG2.costoOggetti[oggetton] * numeroOggettiAcquistati), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 5.3, 50)
                else:
                    GlobalVarG2.schermo.blit(GlobalVarG2.scorriSuGiu, (GlobalVarG2.gsx // 32 * 8.5, GlobalVarG2.gsy // 18 * 4.3))
                    messaggio("(Monete necessarie: %i)" % (GlobalVarG2.costoOggetti[oggetton] * numeroOggettiAcquistati), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 5.3, 50)
                messaggio("Conferma", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.9, 50)
                messaggio("Annulla", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 6, GlobalVarG2.gsy // 18 * 6.9, 50)

            messaggio("Acquista oggetti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
            messaggio("Oggetti acquistabili", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 4.8, 40)
            messaggio("Costo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.5, GlobalVarG2.gsy // 18 * 4.8, 40)
            messaggio("Posseduti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18.5, GlobalVarG2.gsy // 18 * 4.8, 40)
            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigiochi, (int(GlobalVarG2.gpx * 11), int(GlobalVarG2.gpy * 5.5)), (int(GlobalVarG2.gpx * 21), int(GlobalVarG2.gpy * 5.5)), 1)

            messaggio("Freccia", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 6.2, 40)
            messaggio(str(GlobalVarG2.costoOggetti[0]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 6.2, 40)
            messaggio("x%i" % dati[132], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 6.2, 40)
            if oggetton == 0:
                messaggio("Freccia:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                messaggio("Usate per attaccare i nemici a distanza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            if imgOggetti[0] != sconosciutoOggetto:
                messaggio("Pozione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 7.1, 40)
                messaggio(str(GlobalVarG2.costoOggetti[1]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 7.1, 40)
                if dati[31] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 7.1, 40)
                else:
                    messaggio("x%i" % dati[31], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 7.1, 40)
                if oggetton == 1:
                    messaggio("Pozione:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio("Recupera 100 pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 7.1, 40)
            if imgOggetti[1] != sconosciutoOggetto:
                messaggio("Caricabatterie", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 8, 40)
                messaggio(str(GlobalVarG2.costoOggetti[2]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 8, 40)
                if dati[32] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 8, 40)
                else:
                    messaggio("x%i" % dati[32], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 8, 40)
                if oggetton == 2:
                    messaggio("Caricabatterie:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio("Recupera 250 pe di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 8, 40)
            if imgOggetti[2] != sconosciutoOggetto:
                messaggio("Medicina", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 8.9, 40)
                messaggio(str(GlobalVarG2.costoOggetti[3]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 8.9, 40)
                if dati[33] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 8.9, 40)
                else:
                    messaggio("x%i" % dati[33], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 8.9, 40)
                if oggetton == 3:
                    messaggio("Medicina:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio("Cura avvelenamento a Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 8.9, 40)
            if imgOggetti[3] != sconosciutoOggetto:
                messaggio("Super pozione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 9.8, 40)
                messaggio(str(GlobalVarG2.costoOggetti[4]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 9.8, 40)
                if dati[34] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 9.8, 40)
                else:
                    messaggio("x%i" % dati[34], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 9.8, 40)
                if oggetton == 4:
                    messaggio("Super pozione:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio("Recupera 300 pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 9.8, 40)
            if imgOggetti[4] != sconosciutoOggetto:
                messaggio("Carica plus", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 10.7, 40)
                messaggio(str(GlobalVarG2.costoOggetti[5]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 10.7, 40)
                if dati[35] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 10.7, 40)
                else:
                    messaggio("x%i" % dati[35], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 10.7, 40)
                if oggetton == 5:
                    messaggio("Carica plus:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio("Recupera 600 pe di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 10.7, 40)
            if imgOggetti[5] != sconosciutoOggetto:
                messaggio("Bomba", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 11.6, 40)
                messaggio(str(GlobalVarG2.costoOggetti[6]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 11.6, 40)
                if dati[36] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 11.6, 40)
                else:
                    messaggio("x%i" % dati[36], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 11.6, 40)
                if oggetton == 6:
                    messaggio("Bomba:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio("Infligge un po' di danni ai nemici su cui viene", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("lanciata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 11.6, 40)
            if imgOggetti[6] != sconosciutoOggetto:
                messaggio("Bomba velenosa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 12.5, 40)
                messaggio(str(GlobalVarG2.costoOggetti[7]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 12.5, 40)
                if dati[37] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 12.5, 40)
                else:
                    messaggio("x%i" % dati[37], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 12.5, 40)
                if oggetton == 7:
                    messaggio("Bomba velenosa:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio("Infligge avvelenamento al nemico su cui viene", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("lanciata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 12.5, 40)
            if imgOggetti[7] != sconosciutoOggetto:
                messaggio("Esca", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 13.4, 40)
                messaggio(str(GlobalVarG2.costoOggetti[8]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 13.4, 40)
                if dati[38] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 13.4, 40)
                else:
                    messaggio("x%i" % dati[38], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 13.4, 40)
                if oggetton == 8:
                    messaggio("Esca:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio(u"Distrae i nemici finché non viene distrutta. È", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("possibile riprenderla passandoci sopra", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 13.4, 40)
            if imgOggetti[8] != sconosciutoOggetto:
                messaggio("Bomba appiccicosa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 14.3, 40)
                messaggio(str(GlobalVarG2.costoOggetti[9]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 14.3, 40)
                if dati[39] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 14.3, 40)
                else:
                    messaggio("x%i" % dati[39], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 14.3, 40)
                if oggetton == 9:
                    messaggio("Bomba appiccicosa:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio(u"Dimezza la velocità del nemico su cui viene", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("lanciata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 14.3, 40)
            if imgOggetti[9] != sconosciutoOggetto:
                messaggio("Bomba potenziata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 15.2, 40)
                messaggio(str(GlobalVarG2.costoOggetti[10]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 15.2, 40)
                if dati[40] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 15.2, 40)
                else:
                    messaggio("x%i" % dati[40], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 15.2, 40)
                if oggetton == 10:
                    messaggio("Bomba potenziata:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio("Infligge molti danni ai nemici su cui viene", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("lanciata in un vasto raggio", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 15.2, 40)
            messaggio("Faretra", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 16.1, 40)
            if dati[133] == 0:
                messaggio(str(GlobalVarG2.costoOggetti[11]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 16.1, 40)
            if dati[133] == 1:
                messaggio(str(GlobalVarG2.costoOggetti[12]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 16.1, 40)
            if dati[133] >= 2:
                messaggio(str(GlobalVarG2.costoOggetti[13]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 16.1, 40)
            if dati[133] == 3:
                messaggio("x1", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 16.1, 40)
            else:
                messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 16.1, 40)
            if oggetton == 11:
                messaggio("Faretra:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                messaggio(u"Permette di trasportare più frecce", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)

            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            if usa == 0:
                pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, ((xp + (int(GlobalVarG2.gpx // 1.5))), yp + (int(GlobalVarG2.gpy * 0.7))), (xp + (int(GlobalVarG2.gpx * 9.5)), yp + (int(GlobalVarG2.gpy * 0.7))), 2)
            else:
                pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, ((xpv + (int(GlobalVarG2.gpx // 1.5))), ypv + (int(GlobalVarG2.gpy * 0.7))), (xpv + (int(GlobalVarG2.gpx * 9.5)), ypv + (int(GlobalVarG2.gpy * 0.7))), 2)
            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)

    GlobalVarG2.canaleSoundCanzone.stop()
    return dati


def menuImpostazioni(canzone, settaRisoluzione):
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    xp = GlobalVarG2.gsx // 32 * 1
    yp = GlobalVarG2.gsy // 18 * 5.2
    risposta = False
    voceMarcata = 1
    primoFrame = True

    linguaTemp = GlobalVarG2.linguaImpostata
    volumeEffettiTemp = GlobalVarG2.volumeEffetti * 10
    volumeCanzoniTemp = GlobalVarG2.volumeCanzoni * 10
    gsxTemp = GlobalVarG2.gsx
    gsyTemp = GlobalVarG2.gsy
    schermoInteroTemp = GlobalVarG2.schermoIntero

    tastop = 0
    tastotempfps = 5

    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0:
            tastotempfps = 2

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato:
                tastotempfps = 5
                if event.key == pygame.K_q and not tastoTrovato:
                    tastoTrovato = True
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    risposta = True

                if event.key == pygame.K_s and not tastoTrovato:
                    tastop = event.key
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    tastop = event.key
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and not tastoTrovato:
                    tastop = event.key
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and not tastoTrovato:
                    tastop = event.key
                    primoMovimento = True
                    tastoTrovato = True

                if event.key == pygame.K_SPACE and not tastoTrovato:
                    tastop = event.key
                    tastoTrovato = True
                    # quando clicchi spazio puoi modificare l'opzone selezionata
                    if voceMarcata == 6:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        GlobalVarG2.linguaImpostata = linguaTemp
                        GlobalVarG2.volumeEffetti = volumeEffettiTemp / 10 * 1.0
                        GlobalVarG2.volumeCanzoni = volumeCanzoniTemp / 10 * 1.0
                        GlobalVarG2.initVolumeSounds()
                        if GlobalVarG2.gsx != gsxTemp or GlobalVarG2.gsy != gsyTemp or GlobalVarG2.schermoIntero != schermoInteroTemp:
                            GlobalVarG2.schermoIntero = schermoInteroTemp
                            GlobalVarG2.gsx = gsxTemp
                            GlobalVarG2.gsy = gsyTemp
                            GlobalVarG2.gpx = GlobalVarG2.gsx // 32
                            GlobalVarG2.gpy = GlobalVarG2.gsy // 18
                            if GlobalVarG2.schermoIntero:
                                opzioni_schermo = pygame.FULLSCREEN | pygame.HWSURFACE
                                GlobalVarG2.schermo = pygame.display.set_mode((GlobalVarG2.gsx, GlobalVarG2.gsy), opzioni_schermo)
                            else:
                                GlobalVarG2.schermo = pygame.display.set_mode((GlobalVarG2.gsx, GlobalVarG2.gsy))
                            GlobalVarG2.loadImg()
                        # salvo in un file la configurazione (ordine => lingua, volEffetti, volCanzoni, schermoIntero, gsx, gsy)
                        scrivi = open("Impostazioni/Impostazioni.txt", "w")
                        if GlobalVarG2.linguaImpostata == "italiano":
                            scrivi.write("0_")
                        elif GlobalVarG2.linguaImpostata == "inglese":
                            scrivi.write("1_")
                        scrivi.write(str(int(GlobalVarG2.volumeEffetti * 10)) + "_")
                        scrivi.write(str(int(GlobalVarG2.volumeCanzoni * 10)) + "_")
                        if GlobalVarG2.schermoIntero:
                            scrivi.write("1_")
                        else:
                            scrivi.write("0_")
                        scrivi.write(str(GlobalVarG2.gsx) + "_")
                        scrivi.write(str(GlobalVarG2.gsy) + "_")
                        scrivi.close()
                        primoFrame = True
                    elif voceMarcata == 7:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        risposta = True
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_SPACE or ((tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame:
            if primoFrame:
                puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
                xp = GlobalVarG2.gsx // 32 * 1
                yp = GlobalVarG2.gsy // 18 * 5.2
                if voceMarcata == 6:
                    xp = GlobalVarG2.gsx // 32 * 9
                    yp = GlobalVarG2.gsy // 18 * 14.7
                primoFrame = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                if voceMarcata == 2 or voceMarcata == 3 or voceMarcata == 4 or voceMarcata == 5:
                    voceMarcata -= 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = yp - GlobalVarG2.gsy // 18 * 1.7
                    xp = GlobalVarG2.gsx // 32 * 1
                elif voceMarcata == 6:
                    voceMarcata -= 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 11.9
                    xp = GlobalVarG2.gsx // 32 * 1
                elif voceMarcata == 7:
                    voceMarcata -= 2
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 11.9
                    xp = GlobalVarG2.gsx // 32 * 1
                elif voceMarcata == 1:
                    voceMarcata += 5
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 14.7
                    xp = GlobalVarG2.gsx // 32 * 9
            if tastop == pygame.K_a:
                if voceMarcata == 1:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    if linguaTemp == "italiano":
                        linguaTemp = "inglese"
                    elif linguaTemp == "inglese":
                        linguaTemp = "italiano"
                elif voceMarcata == 2:
                    if volumeEffettiTemp != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        volumeEffettiTemp -= 1
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                elif voceMarcata == 3:
                    if volumeCanzoniTemp != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        volumeCanzoniTemp -= 1
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                elif voceMarcata == 4:
                    if settaRisoluzione:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        if gsxTemp == 800 and gsyTemp == 450:
                            gsxTemp = GlobalVarG2.maxGsx
                            gsyTemp = GlobalVarG2.maxGsy
                        elif gsxTemp == 1024 and gsyTemp == 576:
                            gsxTemp = 800
                            gsyTemp = 450
                        elif gsxTemp == 1280 and gsyTemp == 720:
                            gsxTemp = 1024
                            gsyTemp = 576
                        elif gsxTemp == 1920 and gsyTemp == 1080:
                            gsxTemp = 1280
                            gsyTemp = 720
                        elif gsxTemp == GlobalVarG2.maxGsx and gsyTemp == GlobalVarG2.maxGsy:
                            if GlobalVarG2.maxGsx > 1920 and GlobalVarG2.maxGsy > 1080:
                                gsxTemp = 1920
                                gsyTemp = 1080
                            elif GlobalVarG2.maxGsx > 1280 and GlobalVarG2.maxGsy > 720:
                                gsxTemp = 1280
                                gsyTemp = 720
                            elif GlobalVarG2.maxGsx > 1024 and GlobalVarG2.maxGsy > 576:
                                gsxTemp = 1024
                                gsyTemp = 576
                            elif GlobalVarG2.maxGsx > 800 and GlobalVarG2.maxGsy > 450:
                                gsxTemp = 800
                                gsyTemp = 450
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                elif voceMarcata == 5:
                    if settaRisoluzione:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        if schermoInteroTemp:
                            schermoInteroTemp = False
                        else:
                            schermoInteroTemp = True
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                elif voceMarcata == 6:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 17
                elif voceMarcata == 7:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    voceMarcata -= 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 9
            if tastop == pygame.K_s:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                if voceMarcata == 1 or voceMarcata == 2 or voceMarcata == 3 or voceMarcata == 4:
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = yp + GlobalVarG2.gsy // 18 * 1.7
                elif voceMarcata == 5:
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 14.7
                    xp = GlobalVarG2.gsx // 32 * 9
                elif voceMarcata == 6:
                    voceMarcata -= 5
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 5.2
                    xp = GlobalVarG2.gsx // 32 * 1
                elif voceMarcata == 7:
                    voceMarcata -= 6
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 5.2
                    xp = GlobalVarG2.gsx // 32 * 1
            if tastop == pygame.K_d:
                if voceMarcata == 1:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    if linguaTemp == "italiano":
                        linguaTemp = "inglese"
                    elif linguaTemp == "inglese":
                        linguaTemp = "italiano"
                elif voceMarcata == 2:
                    if volumeEffettiTemp != 10:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        volumeEffettiTemp += 1
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                elif voceMarcata == 3:
                    if volumeCanzoniTemp != 10:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        volumeCanzoniTemp += 1
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                elif voceMarcata == 4:
                    if settaRisoluzione:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        if gsxTemp == 800 and gsyTemp == 450:
                            if GlobalVarG2.maxGsx > 1024 and GlobalVarG2.maxGsy > 576:
                                gsxTemp = 1024
                                gsyTemp = 576
                            else:
                                gsxTemp = GlobalVarG2.maxGsx
                                gsyTemp = GlobalVarG2.maxGsy
                        elif gsxTemp == 1024 and gsyTemp == 576:
                            if GlobalVarG2.maxGsx > 1280 and GlobalVarG2.maxGsy > 720:
                                gsxTemp = 1280
                                gsyTemp = 720
                            elif GlobalVarG2.maxGsx == 1024 and GlobalVarG2.maxGsy == 576:
                                gsxTemp = 800
                                gsyTemp = 450
                            else:
                                gsxTemp = GlobalVarG2.maxGsx
                                gsyTemp = GlobalVarG2.maxGsy
                        elif gsxTemp == 1280 and gsyTemp == 720:
                            if GlobalVarG2.maxGsx > 1920 and GlobalVarG2.maxGsy > 1080:
                                gsxTemp = 1920
                                gsyTemp = 1080
                            elif GlobalVarG2.maxGsx == 1280 and GlobalVarG2.maxGsy == 720:
                                gsxTemp = 800
                                gsyTemp = 450
                            else:
                                gsxTemp = GlobalVarG2.maxGsx
                                gsyTemp = GlobalVarG2.maxGsy
                        elif gsxTemp == 1920 and gsyTemp == 1080:
                            if GlobalVarG2.maxGsx > 1920 and GlobalVarG2.maxGsy > 1080:
                                gsxTemp = GlobalVarG2.maxGsx
                                gsyTemp = GlobalVarG2.maxGsy
                            else:
                                gsxTemp = 800
                                gsyTemp = 450
                        elif gsxTemp == GlobalVarG2.maxGsx and gsyTemp == GlobalVarG2.maxGsy:
                            if GlobalVarG2.maxGsx > 800 and GlobalVarG2.maxGsy > 450:
                                gsxTemp = 800
                                gsyTemp = 450
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                elif voceMarcata == 5:
                    if settaRisoluzione:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        if schermoInteroTemp:
                            schermoInteroTemp = False
                        else:
                            schermoInteroTemp = True
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                elif voceMarcata == 6:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 17
                elif voceMarcata == 7:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    voceMarcata -= 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 9
            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 12.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))

            messaggio("Impostazioni", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
            messaggio("Lingua", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 5, 70)
            if linguaTemp == "italiano":
                messaggio("Italiano", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 5.1, 60)
            if linguaTemp == "inglese":
                messaggio("English", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 5.1, 60)
            if voceMarcata == 1:
                GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistra, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 5))
                GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestra, (GlobalVarG2.gsx // 32 * 19.2, GlobalVarG2.gsy // 18 * 5))
            messaggio("Volume effetti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.7, 70)
            messaggio(str(int(volumeEffettiTemp)), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 6.8, 60)
            if voceMarcata == 2:
                if volumeEffettiTemp != 0:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistra, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 6.7))
                else:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistraBloccato, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 6.7))
                if volumeEffettiTemp != 10:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestra, (GlobalVarG2.gsx // 32 * 17.1, GlobalVarG2.gsy // 18 * 6.7))
                else:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestraBloccato, (GlobalVarG2.gsx // 32 * 17.1, GlobalVarG2.gsy // 18 * 6.7))
            messaggio("Volume canzoni", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8.4, 70)
            messaggio(str(int(volumeCanzoniTemp)), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 8.5, 60)
            if voceMarcata == 3:
                if volumeCanzoniTemp != 0:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistra, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 8.4))
                else:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistraBloccato, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 8.4))
                if volumeCanzoniTemp != 10:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestra, (GlobalVarG2.gsx // 32 * 17.1, GlobalVarG2.gsy // 18 * 8.4))
                else:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestraBloccato, (GlobalVarG2.gsx // 32 * 17.1, GlobalVarG2.gsy // 18 * 8.4))
            if settaRisoluzione:
                messaggio("Risoluzione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10.1, 70)
                messaggio(str(gsxTemp) + "x" + str(gsyTemp), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 10.2, 60)
                if voceMarcata == 4:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistra, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 10.1))
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestra, (GlobalVarG2.gsx // 32 * 19.9, GlobalVarG2.gsy // 18 * 10.1))
                messaggio("Schermo intero", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11.7, 70)
                if schermoInteroTemp:
                    messaggio("Si", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 11.8, 60)
                else:
                    messaggio("No", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 11.8, 60)
                if voceMarcata == 5:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistra, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 11.7))
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestra, (GlobalVarG2.gsx // 32 * 17.2, GlobalVarG2.gsy // 18 * 11.7))
            else:
                messaggio("Risoluzione", GlobalVarG2.grigioscu, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10.1, 70)
                messaggio(str(gsxTemp) + "x" + str(gsyTemp), GlobalVarG2.grigioscu, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 10.2, 60)
                if voceMarcata == 4:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistraBloccato, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 10.1))
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestraBloccato, (GlobalVarG2.gsx // 32 * 19.9, GlobalVarG2.gsy // 18 * 10.1))
                messaggio("Schermo intero", GlobalVarG2.grigioscu, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11.7, 70)
                if schermoInteroTemp:
                    messaggio("Si", GlobalVarG2.grigioscu, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 11.8, 60)
                else:
                    messaggio("No", GlobalVarG2.grigioscu, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 11.8, 60)
                if voceMarcata == 5:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistraBloccato, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 11.7))
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestraBloccato, (GlobalVarG2.gsx // 32 * 17.2, GlobalVarG2.gsy // 18 * 11.7))

            messaggio("Conferma", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 14.5, 70)
            messaggio("Indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 70)

            messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            if voceMarcata != 6 and voceMarcata != 7:
                pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, ((xp + (int(GlobalVarG2.gpx // 1.5))), yp + (int(GlobalVarG2.gpy * 1))), (xp + (int(GlobalVarG2.gpx * 29)), yp + (int(GlobalVarG2.gpy * 1))), 2)

            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)
