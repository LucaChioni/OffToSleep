# -*- coding: utf-8 -*-

from GenericFuncG2 import *


def scegli_sal(cosa, lunghezzadati, canzone):
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
    primoFrame = True
    n = -1
    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

        # rallenta per i 30 fps
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
                if (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT) and not tastoTrovato:
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

        if primoMovimento or tastop == pygame.K_q or tastop == pygame.K_SPACE or tastop == pygame.K_LSHIFT or tastop == pygame.K_RSHIFT or ((tastop == pygame.K_a or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame:
            primoFrame = False
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
                    xp = GlobalVarG2.gsx // 32 * 22.5
                    yp = GlobalVarG2.gsy // 18 * 5.7
                    voceMarcata = 2
                    primaconf = False
                if cosa == 2:
                    pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.rossoScuroPiuScuro, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 3.5, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 3.5))
                else:
                    pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 3.5, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 3.5))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 3.5))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 26, GlobalVarG2.gsy // 18 * 3.5))
                messaggio("Confermi?", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20.3, GlobalVarG2.gsy // 18 * 4.2, 70)
                messaggio("Si", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20.4, GlobalVarG2.gsy // 18 * 5.5, 70)
                messaggio("No", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23.4, GlobalVarG2.gsy // 18 * 5.5, 70)
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


def chiediconferma(conferma, canzone):
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    xp = GlobalVarG2.gsx // 32 * 17.5
    yp = GlobalVarG2.gsy // 18 * 10.3
    schermo_temp = GlobalVarG2.schermo.copy()
    background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalVarG2.gsx, GlobalVarG2.gsy))
    dark = pygame.Surface((GlobalVarG2.gsx, GlobalVarG2.gsy), flags=pygame.SRCALPHA)
    dark.fill((0, 0, 0, 210))
    background.blit(dark, (0, 0))

    tastop = 0
    tastotempfps = 5

    voceMarcata = 2
    primoFrame = True
    while True:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

        # rallenta per i 30 fps
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

        if primoMovimento or tastop == pygame.K_SPACE or ((tastop == pygame.K_a or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame:
            primoFrame = False
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
            GlobalVarG2.schermo.blit(background, (0, 0))
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

        # rallenta per i 30 fps
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


def menuMappa(progresso, canzone):
    print "menu mappa"


def menuDiario(progresso, canzone):
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatorevecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    xp = GlobalVarG2.gsx // 32 * 1
    yp = GlobalVarG2.gsy // 18 * 6.1
    xpv = xp
    ypv = yp
    risposta = False
    voceMarcata = 1
    voceMarcataSottoMenu = 0
    primoFrame = True

    tastop = 0
    tastotempfps = 5

    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

        # rallenta per i 30 fps
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
                    tastoTrovato = True
                    if voceMarcataSottoMenu != 0:
                        voceMarcataSottoMenu = 0
                        xp = xpv
                        yp = ypv
                    else:
                        risposta = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_SPACE and not tastoTrovato:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                    tastoTrovato = True
                    voceMarcataSottoMenu = 1
                    xpv = xp
                    ypv = yp
                    xp = GlobalVarG2.gsx // 32 * 10
                    yp = GlobalVarG2.gsy // 18 * 5
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == pygame.K_q or tastop == pygame.K_SPACE or ((tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame:
            primoFrame = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                if voceMarcataSottoMenu == 0:
                    if voceMarcata == 1:
                        voceMarcata += 3
                        yp = GlobalVarG2.gsy // 18 * 14.1
                    elif voceMarcata == 4:
                        voceMarcata -= 1
                        yp = yp - GlobalVarG2.gpy * 4
                    else:
                        voceMarcata -= 1
                        yp = yp - GlobalVarG2.gpy * 2
                elif voceMarcataSottoMenu == 4:
                    print "ciao"
            if tastop == pygame.K_s:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                if voceMarcataSottoMenu == 0:
                    if voceMarcata == 4:
                        voceMarcata -= 3
                        yp = GlobalVarG2.gsy // 18 * 6.1
                    elif voceMarcata == 3:
                        voceMarcata += 1
                        yp = yp + GlobalVarG2.gpy * 4
                    else:
                        voceMarcata += 1
                        yp = yp + GlobalVarG2.gpy * 2
                elif voceMarcataSottoMenu == 4:
                    print "ciao"

            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 12.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))

            if voceMarcataSottoMenu != 0:
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 12.5))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 17, GlobalVarG2.gsy // 18 * 4))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 17, GlobalVarG2.gsy // 18 * 15.5))
                GlobalVarG2.schermo.blit(puntatorevecchio, (xpv, ypv))

            messaggio("Diario", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
            messaggio("Persoaggi incontrati", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6, 55)
            messaggio("Nemici incontrati", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8, 55)
            messaggio("Oggetti speciali", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10, 55)
            messaggio("Guida", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14, 55)

            messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
            GlobalVarG2.schermo.blit(puntatore, (xp, yp))

            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)
