# -*- coding: utf-8 -*-

from CaricaSalvaPartitaG2 import *


def scegli_sal(possibileSalvare, lunghezzadati, porteini, portefin, cofaniini, cofanifin, canzone=False, background=False):
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatorevecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    xp = GlobalVarG2.gsx // 32 * 6.5
    yp = GlobalVarG2.gsy // 18 * 9.5
    vxp = xp
    vyp = yp
    if possibileSalvare:
        cosa = 3
    else:
        cosa = 1

    if background:
        schermo_temp = GlobalVarG2.schermo.copy()
        background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalVarG2.gsx, GlobalVarG2.gsy))
        dark = pygame.Surface((GlobalVarG2.gsx, GlobalVarG2.gsy), flags=pygame.SRCALPHA)
        dark.fill((0, 0, 0, 210))
        background.blit(dark, (0, 0))

    tastop = 0
    tastotempfps = 5

    aggiornaInterfacciaPerMouse = False
    risposta = False
    conferma = False
    primaconf = False
    salMarcato = 1
    voceMarcata = 2
    primoFrame = True
    n = -1
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    while not risposta:
        if canzone and not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

        # rallenta per i 30 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        else:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        salMarcatoVecchio = salMarcato
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        suTornaIndietro = False
        suCambiaOperazione = False
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVarG2.mouseVisibile:
            aggiornaInterfacciaPerMouse = True
            pygame.mouse.set_visible(True)
            GlobalVarG2.mouseVisibile = True
        if GlobalVarG2.mouseVisibile:
            if not conferma:
                if GlobalVarG2.gsx // 32 * 21.8 <= xMouse <= GlobalVarG2.gsx and 0 <= yMouse <= GlobalVarG2.gsy // 18 * 2:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    suTornaIndietro = True
                elif GlobalVarG2.gsx // 32 * 11.5 <= xMouse <= GlobalVarG2.gsx // 32 * 21.8 and 0 <= yMouse <= GlobalVarG2.gsy // 18 * 2:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    suCambiaOperazione = True
                elif GlobalVarG2.gsy // 18 * 7 <= yMouse <= GlobalVarG2.gsy // 18 * 16.5:
                    if GlobalVarG2.gsx // 32 * 5 <= xMouse <= GlobalVarG2.gsx // 32 * 12.3:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        salMarcato = 1
                        xp = GlobalVarG2.gsx // 32 * 6.5
                        yp = GlobalVarG2.gsy // 18 * 9.5
                    elif GlobalVarG2.gsx // 32 * 12.3 <= xMouse <= GlobalVarG2.gsx // 32 * 19.7:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        salMarcato = 2
                        xp = GlobalVarG2.gsx // 32 * 13.5
                        yp = GlobalVarG2.gsy // 18 * 9.5
                    elif GlobalVarG2.gsx // 32 * 19.7 <= xMouse <= GlobalVarG2.gsx // 32 * 27:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        salMarcato = 3
                        xp = GlobalVarG2.gsx // 32 * 20.5
                        yp = GlobalVarG2.gsy // 18 * 9.5
                    else:
                        if not GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(True)
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            else:
                if GlobalVarG2.gsx // 32 * 21.8 <= xMouse <= GlobalVarG2.gsx and 0 <= yMouse <= GlobalVarG2.gsy // 18 * 2:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    suTornaIndietro = True
                elif GlobalVarG2.gsx // 32 * 11.5 <= xMouse <= GlobalVarG2.gsx // 32 * 21.8 and 0 <= yMouse <= GlobalVarG2.gsy // 18 * 2:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    suCambiaOperazione = True
                elif GlobalVarG2.gsy // 18 * 5.2 <= yMouse <= GlobalVarG2.gsy // 18 * 7:
                    if GlobalVarG2.gsx // 32 * 18 <= xMouse <= GlobalVarG2.gsx // 32 * 22.5:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalVarG2.gsx // 32 * 19.5
                        yp = GlobalVarG2.gsy // 18 * 5.7
                    elif GlobalVarG2.gsx // 32 * 22.5 <= xMouse <= GlobalVarG2.gsx // 32 * 27:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalVarG2.gsx // 32 * 22.5
                        yp = GlobalVarG2.gsy // 18 * 5.7
                    else:
                        if not GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(True)
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            if (voceMarcataVecchia != voceMarcata or salMarcatoVecchio != salMarcato) and not primoFrame:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)

        if not conferma:
            vxp = xp
            vyp = yp

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            sinistroMouseVecchio = sinistroMouse
            centraleMouseVecchio = centraleMouse
            destroMouseVecchio = destroMouse
            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
            if not sinistroMouseVecchio and sinistroMouse:
                centraleMouse = False
                destroMouse = False
            elif not centraleMouseVecchio and centraleMouse:
                sinistroMouse = False
                destroMouse = False
            elif not destroMouseVecchio and destroMouse:
                sinistroMouse = False
                centraleMouse = False

            if event.type == pygame.QUIT:
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato and voceMarcataVecchia == voceMarcata and salMarcatoVecchio == salMarcato:
                if GlobalVarG2.mouseVisibile:
                    aggiornaInterfacciaPerMouse = True
                    pygame.mouse.set_visible(False)
                    GlobalVarG2.mouseVisibile = False
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
                        return n, cosa
                if event.key == pygame.K_d and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse:
                tastop = "destroMouse"
                tastoTrovato = True
                if conferma:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    xp = vxp
                    yp = vyp
                    conferma = False
                else:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    n = -1
                    return n, cosa
            if (event.type == pygame.KEYDOWN and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT)) or (GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and centraleMouse):
                tastop = "centraleMouse"
                tastoTrovato = True
                xp = vxp
                yp = vyp
                conferma = False
                if possibileSalvare:
                    if cosa == 1:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selsta)
                        cosa = 2
                    elif cosa == 2:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selsta)
                        cosa = 3
                    elif cosa == 3:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selsta)
                        cosa = 1
                else:
                    if cosa == 1:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selsta)
                        cosa = 2
                    elif cosa == 2:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selsta)
                        cosa = 1
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato):
                tastop = "spazioOsinistroMouse"
                tastoTrovato = True
                if event.type == pygame.MOUSEBUTTONDOWN and suTornaIndietro:
                    if conferma:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        xp = vxp
                        yp = vyp
                        conferma = False
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        n = -1
                        return n, cosa
                elif event.type == pygame.MOUSEBUTTONDOWN and suCambiaOperazione:
                    xp = vxp
                    yp = vyp
                    conferma = False
                    if possibileSalvare:
                        if cosa == 1:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selsta)
                            cosa = 2
                        elif cosa == 2:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selsta)
                            cosa = 3
                        elif cosa == 3:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selsta)
                            cosa = 1
                    else:
                        if cosa == 1:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selsta)
                            cosa = 2
                        elif cosa == 2:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selsta)
                            cosa = 1
                else:
                    if conferma:
                        if voceMarcata == 1:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            if cosa == 1:
                                dati, datiNemici, datiEsche, datiMonete, stanzeGiaVisitate, ultimoObbiettivoColco, obbiettivoCasualeColco = caricaPartita(n, lunghezzadati, porteini, portefin, cofaniini, cofanifin, background)
                                if dati:
                                    return n, cosa
                                else:
                                    conferma = False
                                    xp = vxp
                                    yp = vyp
                            elif cosa == 3:
                                return n, cosa
                            elif cosa == 2:
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
            elif GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and GlobalVarG2.mouseBloccato:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if (sinistroMouse or centraleMouse or destroMouse) and not GlobalVarG2.mouseVisibile:
                aggiornaInterfacciaPerMouse = True
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0
            if event.type == pygame.MOUSEBUTTONUP:
                tastop = 0

        if primoMovimento or tastop == pygame.K_q or tastop == "spazioOsinistroMouse" or tastop == "centraleMouse" or tastop == "destroMouse" or tastop == pygame.K_LSHIFT or tastop == pygame.K_RSHIFT or ((tastop == pygame.K_a or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or salMarcatoVecchio != salMarcato or aggiornaInterfacciaPerMouse:
            aggiornaInterfacciaPerMouse = False
            primoFrame = False
            if not primoMovimento and (tastop == pygame.K_a or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_a:
                if GlobalVarG2.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVarG2.mouseVisibile = False
                if conferma:
                    if voceMarcata == 2:
                        voceMarcata -= 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 19.5
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
                if GlobalVarG2.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVarG2.mouseVisibile = False
                if conferma:
                    if voceMarcata == 1:
                        voceMarcata += 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 22.5
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

            if background:
                GlobalVarG2.schermo.blit(background, (0, 0))
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 4.7, GlobalVarG2.gsy // 18 * 3.2, GlobalVarG2.gsx // 32 * 22.6, GlobalVarG2.gsy // 18 * 13.6))
            else:
                GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            if cosa == 2:
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.rossoScuro, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 7, GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 9.5))
            elif cosa == 1:
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.bluScuro, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 7, GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 9.5))
            else:
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 7, GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 9.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 7))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 26, GlobalVarG2.gsy // 18 * 7))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 26, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 15.5))
            if cosa == 1:
                messaggio("Recupera momento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5.2, GlobalVarG2.gsy // 18 * 4.3, 100)
                if GlobalVarG2.mouseVisibile:
                    messaggio("Tasto centrale: cancella momento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 12, GlobalVarG2.gsy // 18 * 1, 50)
                else:
                    messaggio("SHIFT: cancella momento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17, GlobalVarG2.gsy // 18 * 1, 50)
            if cosa == 2:
                messaggio("Cancella momento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5.2, GlobalVarG2.gsy // 18 * 4.3, 100)
                if possibileSalvare:
                    if GlobalVarG2.mouseVisibile:
                        messaggio("Tasto centrale: fissa momento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 12, GlobalVarG2.gsy // 18 * 1, 50)
                    else:
                        messaggio("SHIFT: fissa momento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17, GlobalVarG2.gsy // 18 * 1, 50)
                else:
                    if GlobalVarG2.mouseVisibile:
                        messaggio("Tasto centrale: recupera momento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 12, GlobalVarG2.gsy // 18 * 1, 50)
                    else:
                        messaggio("SHIFT: recupera momento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17, GlobalVarG2.gsy // 18 * 1, 50)
            if cosa == 3:
                messaggio("Fissa momento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5.2, GlobalVarG2.gsy // 18 * 4.3, 100)
                if GlobalVarG2.mouseVisibile:
                    messaggio("Tasto centrale: recupera momento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 12, GlobalVarG2.gsy // 18 * 1, 50)
                else:
                    messaggio("SHIFT: recupera momento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17, GlobalVarG2.gsy // 18 * 1, 50)
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
                elif cosa == 1:
                    pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.bluScuroPiuScuro, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 3.5, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 3.5))
                else:
                    pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 3.5, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 3.5))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 3.5))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 26, GlobalVarG2.gsy // 18 * 3.5))
                messaggio("Confermi?", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20.3, GlobalVarG2.gsy // 18 * 4.2, 70)
                messaggio("Si", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20.4, GlobalVarG2.gsy // 18 * 5.5, 70)
                messaggio("No", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23.4, GlobalVarG2.gsy // 18 * 5.5, 70)
                GlobalVarG2.schermo.blit(puntatorevecchio, (vxp, vyp))
            if GlobalVarG2.mouseVisibile:
                messaggio("Tasto destro: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 1, 50)
            else:
                messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
            GlobalVarG2.schermo.blit(GlobalVarG2.s1, (GlobalVarG2.gsx // 32 * 7.6, GlobalVarG2.gsy // 18 * 8))
            GlobalVarG2.schermo.blit(GlobalVarG2.s2, (GlobalVarG2.gsx // 32 * 14.6, GlobalVarG2.gsy // 18 * 8))
            GlobalVarG2.schermo.blit(GlobalVarG2.s3, (GlobalVarG2.gsx // 32 * 21.6, GlobalVarG2.gsy // 18 * 8))

            # lettura salvataggi per riconoscerli
            contasalva = 1
            while contasalva <= 3:
                dati, errore = caricaPartita(contasalva, lunghezzadati, porteini, portefin, cofaniini, cofanifin, False, False)
                if errore == 1:
                    if contasalva == 1:
                        messaggio("Slot vuoto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 7.25, GlobalVarG2.gsy // 18 * 11, 60)
                    elif contasalva == 2:
                        messaggio("Slot vuoto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14.25, GlobalVarG2.gsy // 18 * 11, 60)
                    elif contasalva == 3:
                        messaggio("Slot vuoto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 21.25, GlobalVarG2.gsy // 18 * 11, 60)
                else:
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
                            messaggio("Livello: " + str(dati[4]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 7.1, GlobalVarG2.gsy // 18 * 11, 60)
                            GlobalVarG2.schermo.blit(arcsalva, (GlobalVarG2.gpx * 7.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(persalva, (GlobalVarG2.gpx * 7.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(persSalvaBraccia, (GlobalVarG2.gpx * 7.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(armsalva, (GlobalVarG2.gpx * 7.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(colsalva, (GlobalVarG2.gpx * 7.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(spasalva, (GlobalVarG2.gpx * 7.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(guasalva, (GlobalVarG2.gpx * 7.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(scusalva, (GlobalVarG2.gpx * 7.6, GlobalVarG2.gpy * 12))
                        else:
                            messaggio("Slot corrotto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 6.8, GlobalVarG2.gsy // 18 * 11, 60)
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
                            messaggio("Livello: " + str(dati[4]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14.1, GlobalVarG2.gsy // 18 * 11, 60)
                            GlobalVarG2.schermo.blit(arcsalva, (GlobalVarG2.gpx * 14.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(persalva, (GlobalVarG2.gpx * 14.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(persSalvaBraccia, (GlobalVarG2.gpx * 14.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(armsalva, (GlobalVarG2.gpx * 14.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(colsalva, (GlobalVarG2.gpx * 14.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(spasalva, (GlobalVarG2.gpx * 14.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(guasalva, (GlobalVarG2.gpx * 14.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(scusalva, (GlobalVarG2.gpx * 14.6, GlobalVarG2.gpy * 12))
                        else:
                            messaggio("Slot corrotto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 13.8, GlobalVarG2.gsy // 18 * 11, 60)
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
                            messaggio("Livello: " + str(dati[4]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 21.1, GlobalVarG2.gsy // 18 * 11, 60)
                            GlobalVarG2.schermo.blit(arcsalva, (GlobalVarG2.gpx * 21.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(persalva, (GlobalVarG2.gpx * 21.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(persSalvaBraccia, (GlobalVarG2.gpx * 21.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(armsalva, (GlobalVarG2.gpx * 21.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(colsalva, (GlobalVarG2.gpx * 21.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(spasalva, (GlobalVarG2.gpx * 21.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(guasalva, (GlobalVarG2.gpx * 21.6, GlobalVarG2.gpy * 12))
                            GlobalVarG2.schermo.blit(scusalva, (GlobalVarG2.gpx * 21.6, GlobalVarG2.gpy * 12))
                        else:
                            messaggio("Slot corrotto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20.8, GlobalVarG2.gsy // 18 * 11, 60)
                contasalva = contasalva + 1

            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)


def chiediconferma(conferma, canzone=False):
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

    aggiornaInterfacciaPerMouse = False
    voceMarcata = 2
    primoFrame = True
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    while True:
        if canzone and not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

        # rallenta per i 30 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        else:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        suTornaIndietro = False
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVarG2.mouseVisibile:
            aggiornaInterfacciaPerMouse = True
            pygame.mouse.set_visible(True)
            GlobalVarG2.mouseVisibile = True
        if GlobalVarG2.mouseVisibile:
            if GlobalVarG2.gsx // 32 * 21.5 <= xMouse <= GlobalVarG2.gsx and 0 <= yMouse <= GlobalVarG2.gsy // 18 * 2:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalVarG2.gsy // 18 * 9 <= yMouse <= GlobalVarG2.gsy // 18 * 12:
                if GlobalVarG2.gsx // 32 * 9.5 <= xMouse <= GlobalVarG2.gsx // 32 * 16:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalVarG2.gsx // 32 * 9.5
                    yp = GlobalVarG2.gsy // 18 * 10.3
                elif GlobalVarG2.gsx // 32 * 16 <= xMouse <= GlobalVarG2.gsx // 32 * 22.5:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalVarG2.gsx // 32 * 17.5
                    yp = GlobalVarG2.gsy // 18 * 10.3
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            else:
                if not GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            sinistroMouseVecchio = sinistroMouse
            centraleMouseVecchio = centraleMouse
            destroMouseVecchio = destroMouse
            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
            if not sinistroMouseVecchio and sinistroMouse:
                centraleMouse = False
                destroMouse = False
            elif not centraleMouseVecchio and centraleMouse:
                sinistroMouse = False
                destroMouse = False
            elif not destroMouseVecchio and destroMouse:
                sinistroMouse = False
                centraleMouse = False

            if event.type == pygame.QUIT:
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato and voceMarcataVecchia == voceMarcata:
                if GlobalVarG2.mouseVisibile:
                    aggiornaInterfacciaPerMouse = True
                    pygame.mouse.set_visible(False)
                    GlobalVarG2.mouseVisibile = False
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
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse:
                tastoTrovato = True
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                return False, False
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato):
                tastop = "spazioOsinistroMouse"
                tastoTrovato = True
                if event.type == pygame.MOUSEBUTTONDOWN and suTornaIndietro:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    return False, False
                else:
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
            elif GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and GlobalVarG2.mouseBloccato:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if (sinistroMouse or centraleMouse or destroMouse) and not GlobalVarG2.mouseVisibile:
                aggiornaInterfacciaPerMouse = True
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0
            if event.type == pygame.MOUSEBUTTONUP:
                tastop = 0

        if primoMovimento or tastop == "spazioOsinistroMouse" or ((tastop == pygame.K_a or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerMouse:
            aggiornaInterfacciaPerMouse = False
            primoFrame = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_a:
                if GlobalVarG2.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVarG2.mouseVisibile = False
                if voceMarcata == 2:
                    voceMarcata -= 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 9.5
            if tastop == pygame.K_d:
                if GlobalVarG2.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVarG2.mouseVisibile = False
                if voceMarcata == 1:
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 17.5
            GlobalVarG2.schermo.blit(background, (0, 0))
            if conferma == 1:
                messaggio(u"Tornare al menu principale?", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 6.5, 120)
            elif conferma == 2:
                messaggio("Uscire dal gioco?", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.6, GlobalVarG2.gsy // 18 * 6.5, 120)
            messaggio("Si", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 9.5, 120)
            messaggio("No", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 9.5, 120)
            if GlobalVarG2.mouseVisibile:
                messaggio("Tasto destro: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 1, 50)
            else:
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
    aggiornaInterfacciaPerMouse = False
    sinistroMousePremuto = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

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
        else:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        cursoreSuFrecciaSinistra = False
        cursoreSuFrecciaDestra = False
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        suTornaIndietro = False
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVarG2.mouseVisibile:
            aggiornaInterfacciaPerMouse = True
            pygame.mouse.set_visible(True)
            GlobalVarG2.mouseVisibile = True
        if GlobalVarG2.mouseVisibile:
            if GlobalVarG2.gsx // 32 * 21.5 <= xMouse <= GlobalVarG2.gsx and 0 <= yMouse <= GlobalVarG2.gsy // 18 * 2:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalVarG2.gsx // 32 * 8 <= xMouse <= GlobalVarG2.gsx // 32 * 16 and GlobalVarG2.gsy // 18 * 13.5 <= yMouse <= GlobalVarG2.gsy // 18 * 16:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                voceMarcata = 6
                xp = GlobalVarG2.gsx // 32 * 9
                yp = GlobalVarG2.gsy // 18 * 14.7
            elif GlobalVarG2.gsx // 32 * 16 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 14 <= yMouse <= GlobalVarG2.gsy // 18 * 17:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                voceMarcata = 7
                xp = GlobalVarG2.gsx // 32 * 17
                yp = GlobalVarG2.gsy // 18 * 14.7
            elif GlobalVarG2.gsx // 32 * 15.2 <= xMouse <= GlobalVarG2.gsx // 32 * 15.7 and GlobalVarG2.gsy // 18 * 5 <= yMouse <= GlobalVarG2.gsy // 18 * 6:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalVarG2.gsx // 32 * 19.2 <= xMouse <= GlobalVarG2.gsx // 32 * 19.7 and GlobalVarG2.gsy // 18 * 5 <= yMouse <= GlobalVarG2.gsy // 18 * 6:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalVarG2.gsx // 32 * 15.2 <= xMouse <= GlobalVarG2.gsx // 32 * 15.7 and GlobalVarG2.gsy // 18 * 6.7 <= yMouse <= GlobalVarG2.gsy // 18 * 7.7:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalVarG2.gsx // 32 * 17.1 <= xMouse <= GlobalVarG2.gsx // 32 * 17.6 and GlobalVarG2.gsy // 18 * 6.7 <= yMouse <= GlobalVarG2.gsy // 18 * 7.7:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalVarG2.gsx // 32 * 15.2 <= xMouse <= GlobalVarG2.gsx // 32 * 15.7 and GlobalVarG2.gsy // 18 * 8.4 <= yMouse <= GlobalVarG2.gsy // 18 * 9.4:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalVarG2.gsx // 32 * 17.1 <= xMouse <= GlobalVarG2.gsx // 32 * 17.6 and GlobalVarG2.gsy // 18 * 8.4 <= yMouse <= GlobalVarG2.gsy // 18 * 9.4:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalVarG2.gsx // 32 * 15.2 <= xMouse <= GlobalVarG2.gsx // 32 * 15.7 and GlobalVarG2.gsy // 18 * 10.1 <= yMouse <= GlobalVarG2.gsy // 18 * 11.1:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalVarG2.gsx // 32 * 19.9 <= xMouse <= GlobalVarG2.gsx // 32 * 20.4 and GlobalVarG2.gsy // 18 * 10.1 <= yMouse <= GlobalVarG2.gsy // 18 * 11.1:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalVarG2.gsx // 32 * 15.2 <= xMouse <= GlobalVarG2.gsx // 32 * 15.7 and GlobalVarG2.gsy // 18 * 11.7 <= yMouse <= GlobalVarG2.gsy // 18 * 12.7:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalVarG2.gsx // 32 * 17.2 <= xMouse <= GlobalVarG2.gsx // 32 * 17.7 and GlobalVarG2.gsy // 18 * 11.7 <= yMouse <= GlobalVarG2.gsy // 18 * 12.7:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            else:
                if not GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(True)
            if GlobalVarG2.gsx // 32 * 1 <= xMouse <= GlobalVarG2.gsx // 32 * 31:
                if GlobalVarG2.gsy // 18 * 4.7 <= yMouse <= GlobalVarG2.gsy // 18 * 6.3:
                    voceMarcata = 1
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 5.2
                elif GlobalVarG2.gsy // 18 * 6.3 <= yMouse <= GlobalVarG2.gsy // 18 * 8:
                    voceMarcata = 2
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 6.9
                elif GlobalVarG2.gsy // 18 * 8 <= yMouse <= GlobalVarG2.gsy // 18 * 9.7:
                    voceMarcata = 3
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 8.6
                elif GlobalVarG2.gsy // 18 * 9.7 <= yMouse <= GlobalVarG2.gsy // 18 * 11.4:
                    voceMarcata = 4
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 10.3
                elif GlobalVarG2.gsy // 18 * 11.4 <= yMouse <= GlobalVarG2.gsy // 18 * 13.1:
                    voceMarcata = 5
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 12
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            sinistroMouseVecchio = sinistroMouse
            centraleMouseVecchio = centraleMouse
            destroMouseVecchio = destroMouse
            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
            if not sinistroMouseVecchio and sinistroMouse:
                centraleMouse = False
                destroMouse = False
            elif not centraleMouseVecchio and centraleMouse:
                sinistroMouse = False
                destroMouse = False
            elif not destroMouseVecchio and destroMouse:
                sinistroMouse = False
                centraleMouse = False

            if event.type == pygame.QUIT:
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato and voceMarcataVecchia == voceMarcata:
                if GlobalVarG2.mouseVisibile:
                    aggiornaInterfacciaPerMouse = True
                    pygame.mouse.set_visible(False)
                    GlobalVarG2.mouseVisibile = False
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

            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse:
                tastoTrovato = True
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                risposta = True
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato and (cursoreSuFrecciaSinistra or cursoreSuFrecciaDestra):
                tastop = "spazioOsinistroMouse"
                tastotempfps = 5
                primoMovimento = True
                tastoTrovato = True
                sinistroMousePremuto = True
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato and not (cursoreSuFrecciaSinistra or cursoreSuFrecciaDestra)):
                tastop = "spazioOsinistroMouse"
                tastotempfps = 5
                primoMovimento = True
                tastoTrovato = True
                if event.type == pygame.MOUSEBUTTONDOWN and suTornaIndietro:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    risposta = True
                else:
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
                        puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
                        yp = GlobalVarG2.gsy // 18 * 14.7
                        xp = GlobalVarG2.gsx // 32 * 9
                        primoFrame = True
                    elif voceMarcata == 7:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        risposta = True
            elif GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and GlobalVarG2.mouseBloccato:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if (sinistroMouse or centraleMouse or destroMouse) and not GlobalVarG2.mouseVisibile:
                aggiornaInterfacciaPerMouse = True
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0
            if event.type == pygame.MOUSEBUTTONUP:
                tastop = 0
                sinistroMousePremuto = False

        if primoMovimento or ((tastop == "spazioOsinistroMouse" or tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerMouse:
            aggiornaInterfacciaPerMouse = False
            primoFrame = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w:
                if GlobalVarG2.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVarG2.mouseVisibile = False
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
                if GlobalVarG2.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVarG2.mouseVisibile = False
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
                if GlobalVarG2.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVarG2.mouseVisibile = False
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
                if GlobalVarG2.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVarG2.mouseVisibile = False
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
            if sinistroMousePremuto and cursoreSuFrecciaSinistra:
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
            if sinistroMousePremuto and cursoreSuFrecciaDestra:
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

            if GlobalVarG2.mouseVisibile:
                messaggio("Tasto destro: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5,
                          GlobalVarG2.gsy // 18 * 1, 50)
            else:
                messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25,
                          GlobalVarG2.gsy // 18 * 1, 50)
            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            if voceMarcata != 6 and voceMarcata != 7:
                pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, ((xp + (int(GlobalVarG2.gpx // 1.5))), yp + (int(GlobalVarG2.gpy * 1))), (xp + (int(GlobalVarG2.gpx * 29)), yp + (int(GlobalVarG2.gpy * 1))), 2)

            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)


def menuMappa(progresso, canzone):
    print "menu mappa"


def menuDiario(dati, canzone):
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatorevecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    xp = GlobalVarG2.gsx // 32 * 1
    yp = GlobalVarG2.gsy // 18 * 5.6
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
        else:
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
                    if voceMarcataSottoMenu == 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        tastoTrovato = True
                        voceMarcataSottoMenu = 1
                        xpv = xp
                        ypv = yp
                        if voceMarcata == 4 or voceMarcata == 5:
                            xp = GlobalVarG2.gsx // 32 * 10
                            yp = GlobalVarG2.gsy // 18 * 8
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
                        voceMarcata += 4
                        yp = GlobalVarG2.gsy // 18 * 14.6
                    elif voceMarcata == 4:
                        voceMarcata -= 1
                        yp = GlobalVarG2.gsy // 18 * 8.6
                    else:
                        voceMarcata -= 1
                        yp = yp - GlobalVarG2.gpy * 1.5
                else:
                    if voceMarcata == 4 or voceMarcata == 5:
                        if voceMarcataSottoMenu == 1:
                            voceMarcataSottoMenu += 2
                            yp = GlobalVarG2.gsy // 18 * 12
                        else:
                            voceMarcataSottoMenu -= 1
                            yp = yp - GlobalVarG2.gpy * 2
            if tastop == pygame.K_s:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                if voceMarcataSottoMenu == 0:
                    if voceMarcata == 5:
                        voceMarcata -= 4
                        yp = GlobalVarG2.gsy // 18 * 5.6
                    elif voceMarcata == 3:
                        voceMarcata += 1
                        yp = GlobalVarG2.gsy // 18 * 13.1
                    else:
                        voceMarcata += 1
                        yp = yp + GlobalVarG2.gpy * 1.5
                else:
                    if voceMarcata == 4 or voceMarcata == 5:
                        if voceMarcataSottoMenu == 3:
                            voceMarcataSottoMenu -= 2
                            yp = GlobalVarG2.gsy // 18 * 8
                        else:
                            voceMarcataSottoMenu += 1
                            yp = yp + GlobalVarG2.gpy * 2

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
                if voceMarcata == 4 or voceMarcata == 5:
                    messaggio("Mod. movimento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 7.9, 55)
                    messaggio("Mod. attacco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 9.9, 55)
                    messaggio("Menu", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 11.9, 55)
                    if voceMarcata == 4:
                        if voceMarcataSottoMenu == 1:
                            GlobalVarG2.schermo.blit(GlobalVarG2.tutorialMouse, (GlobalVarG2.gsx // 32 * 20.2, GlobalVarG2.gsy // 18 * 4.8))
                            messaggio("Movimento (su casella libera) /", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.6, 35)
                            messaggio("Interagisci (su casella interagibile) /", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 6.1, 35)
                            messaggio("Attiva o disattiva Colco (su telecolco) /", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 6.6, 35)
                            messaggio("Menu start (su stato personaggio) /", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 7.1, 35)
                            messaggio(u"Modalità attacco (su stato nemico)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 7.6, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 8.6), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 8.6), 2)
                            messaggio(u"Modalità attacco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 10.1, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 12), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 12), 2)
                            messaggio("Menu start", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 13.5, 35)
                        if voceMarcataSottoMenu == 2:
                            GlobalVarG2.schermo.blit(GlobalVarG2.tutorialMouse, (GlobalVarG2.gsx // 32 * 20.2, GlobalVarG2.gsy // 18 * 4.8))
                            messaggio("Inquadra o attacca (su casella nemica) /", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.6, 35)
                            messaggio("Interagisci (su casella interagibile) /", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 6.1, 35)
                            messaggio("Attiva o disattiva Colco (su telecolco) /", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 6.6, 35)
                            messaggio("Menu start (su stato personaggio) /", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 7.1, 35)
                            messaggio(u"Modalità movimento (su stato nemico)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 7.6, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 8.6), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 8.6), 2)
                            messaggio(u"Modalità movimento /", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 9.9, 35)
                            messaggio("Rimuovi selezione (su nemico inquadrato)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 10.4, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 12), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 12), 2)
                            messaggio("Menu start", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 13.5, 35)
                        if voceMarcataSottoMenu == 3:
                            GlobalVarG2.schermo.blit(GlobalVarG2.tutorialMouse, (GlobalVarG2.gsx // 32 * 20.2, GlobalVarG2.gsy // 18 * 4.8))
                            messaggio("Seleziona", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 6.6, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 8.6), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 8.6), 2)
                            messaggio("Indietro / Esci", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 10.1, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 12), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 12), 2)
                            messaggio("Cambia operazione (se consentito)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 13.5, 35)
                    if voceMarcata == 5:
                        if voceMarcataSottoMenu == 1:
                            GlobalVarG2.schermo.blit(GlobalVarG2.tutorialTastieraInGioco, (GlobalVarG2.gsx // 32 * 20.2, GlobalVarG2.gsy // 18 * 4.8))
                            messaggio("Menu start", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 5.5, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 6.1), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 6.1), 2)
                            messaggio("Cambia bersaglio inquadrato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 6.7, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 7.5), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 7.5), 2)
                            messaggio("Deseleziona bersaglio", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 8.1, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 8.9), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 8.9), 2)
                            messaggio(u"Modalità attacco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 9.5, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 10.3), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 10.3), 2)
                            messaggio("Movimento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 11.5, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 12.8), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 12.8), 2)
                            messaggio("Attiva o disattiva Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 13.4, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 14.2), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 14.2), 2)
                            messaggio("Interagisci", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 14.8, 35)
                        if voceMarcataSottoMenu == 2:
                            GlobalVarG2.schermo.blit(GlobalVarG2.tutorialTastieraInGioco, (GlobalVarG2.gsx // 32 * 20.2, GlobalVarG2.gsy // 18 * 4.8))
                            messaggio("Menu start", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 5.5, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 6.1), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 6.1), 2)
                            messaggio("Punta sul prossimo bersaglio", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 6.7, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 7.5), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 7.5), 2)
                            messaggio(u"Modalità movimento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 8.1, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 8.9), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 8.9), 2)
                            messaggio("Inquadra bersaglio puntato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 9.5, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 10.3), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 10.3), 2)
                            messaggio("Sposta puntatore", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 11.5, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 12.8), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 12.8), 2)
                            messaggio("Attiva o disattiva Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 13.4, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 14.2), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 14.2), 2)
                            messaggio("Attacca / Interagisci", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 14.8, 35)
                        if voceMarcataSottoMenu == 3:
                            GlobalVarG2.schermo.blit(GlobalVarG2.tutorialTastieraInMenu, (GlobalVarG2.gsx // 32 * 20.2, GlobalVarG2.gsy // 18 * 4.8))
                            messaggio("Esci (dove specificato)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 6.9, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 7.5), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 7.5), 2)
                            messaggio("Indietro / Esci", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 8.1, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 8.9), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 8.9), 2)
                            messaggio("Sposta puntatore", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 10.1, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 11.4), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 11.4), 2)
                            messaggio("Cambia operazione (se consentito)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 12, 35)
                            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 12.8), (GlobalVarG2.gsx // 32 * 30, GlobalVarG2.gsy // 18 * 12.8), 2)
                            messaggio("Seleziona", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24.2, GlobalVarG2.gsy // 18 * 13.4, 35)

            messaggio("Diario", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
            messaggio("Oggetti speciali", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 5.5, 55)
            messaggio("Personaggi incontrati", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7, 55)
            messaggio("Nemici incontrati", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8.5, 55)
            messaggio("Guida mouse", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13, 55)
            messaggio("Guida tatiera", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14.5, 55)

            messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
            GlobalVarG2.schermo.blit(puntatore, (xp, yp))

            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)
