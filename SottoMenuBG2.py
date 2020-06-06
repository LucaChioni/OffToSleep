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
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.verdeScuro, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 7, GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 9.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 7))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 26, GlobalVarG2.gsy // 18 * 7))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 26, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 15.5))
            if cosa == 1:
                messaggio("Carica partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5.5, GlobalVarG2.gsy // 18 * 4.3, 100)
                if GlobalVarG2.mouseVisibile:
                    messaggio("Tasto centrale: cancella partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 12, GlobalVarG2.gsy // 18 * 1, 50)
                else:
                    messaggio("SHIFT: cancella partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17, GlobalVarG2.gsy // 18 * 1, 50)
            if cosa == 2:
                messaggio("Cancella partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5.5, GlobalVarG2.gsy // 18 * 4.3, 100)
                if possibileSalvare:
                    if GlobalVarG2.mouseVisibile:
                        messaggio("Tasto centrale: salva partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 12, GlobalVarG2.gsy // 18 * 1, 50)
                    else:
                        messaggio("SHIFT: salva partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17, GlobalVarG2.gsy // 18 * 1, 50)
                else:
                    if GlobalVarG2.mouseVisibile:
                        messaggio("Tasto centrale: carica partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 12, GlobalVarG2.gsy // 18 * 1, 50)
                    else:
                        messaggio("SHIFT: carica partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17, GlobalVarG2.gsy // 18 * 1, 50)
            if cosa == 3:
                messaggio("Salva partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5.5, GlobalVarG2.gsy // 18 * 4.3, 100)
                if GlobalVarG2.mouseVisibile:
                    messaggio("Tasto centrale: carica partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 12, GlobalVarG2.gsy // 18 * 1, 50)
                else:
                    messaggio("SHIFT: carica partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17, GlobalVarG2.gsy // 18 * 1, 50)
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
                    pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.verdeScuroPiuScuro, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 3.5, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 3.5))
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
        if canzone and not GlobalVarG2.canaleSoundCanzone.get_busy():
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

        buttonUp = False
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
                buttonUp = True
            if event.type == pygame.MOUSEBUTTONUP:
                tastop = 0
                sinistroMousePremuto = False
                buttonUp = True

        if primoMovimento or buttonUp or ((tastop == "spazioOsinistroMouse" or tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerMouse:
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
                if tastop == pygame.K_a or (sinistroMousePremuto and cursoreSuFrecciaSinistra):
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistraBloccato, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 5))
                else:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistra, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 5))
                if tastop == pygame.K_d or (sinistroMousePremuto and cursoreSuFrecciaDestra):
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestraBloccato, (GlobalVarG2.gsx // 32 * 19.2, GlobalVarG2.gsy // 18 * 5))
                else:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestra, (GlobalVarG2.gsx // 32 * 19.2, GlobalVarG2.gsy // 18 * 5))
            messaggio("Volume effetti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.7, 70)
            messaggio(str(int(volumeEffettiTemp)), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 6.8, 60)
            if voceMarcata == 2:
                if volumeEffettiTemp != 0:
                    if tastop == pygame.K_a or (sinistroMousePremuto and cursoreSuFrecciaSinistra):
                        GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistraBloccato, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 6.7))
                    else:
                        GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistra, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 6.7))
                else:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistraBloccato, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 6.7))
                if volumeEffettiTemp != 10:
                    if tastop == pygame.K_d or (sinistroMousePremuto and cursoreSuFrecciaDestra):
                        GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestraBloccato, (GlobalVarG2.gsx // 32 * 17.1, GlobalVarG2.gsy // 18 * 6.7))
                    else:
                        GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestra, (GlobalVarG2.gsx // 32 * 17.1, GlobalVarG2.gsy // 18 * 6.7))
                else:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestraBloccato, (GlobalVarG2.gsx // 32 * 17.1, GlobalVarG2.gsy // 18 * 6.7))
            messaggio("Volume canzoni", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8.4, 70)
            messaggio(str(int(volumeCanzoniTemp)), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 8.5, 60)
            if voceMarcata == 3:
                if volumeCanzoniTemp != 0:
                    if tastop == pygame.K_a or (sinistroMousePremuto and cursoreSuFrecciaSinistra):
                        GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistraBloccato, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 8.4))
                    else:
                        GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistra, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 8.4))
                else:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistraBloccato, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 8.4))
                if volumeCanzoniTemp != 10:
                    if tastop == pygame.K_d or (sinistroMousePremuto and cursoreSuFrecciaDestra):
                        GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestraBloccato, (GlobalVarG2.gsx // 32 * 17.1, GlobalVarG2.gsy // 18 * 8.4))
                    else:
                        GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestra, (GlobalVarG2.gsx // 32 * 17.1, GlobalVarG2.gsy // 18 * 8.4))
                else:
                    GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestraBloccato, (GlobalVarG2.gsx // 32 * 17.1, GlobalVarG2.gsy // 18 * 8.4))
            if settaRisoluzione:
                messaggio("Risoluzione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10.1, 70)
                messaggio(str(gsxTemp) + "x" + str(gsyTemp), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 10.2, 60)
                if voceMarcata == 4:
                    if tastop == pygame.K_a or (sinistroMousePremuto and cursoreSuFrecciaSinistra):
                        GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistraBloccato, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 10.1))
                    else:
                        GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistra, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 10.1))
                    if tastop == pygame.K_d or (sinistroMousePremuto and cursoreSuFrecciaDestra):
                        GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestraBloccato, (GlobalVarG2.gsx // 32 * 19.9, GlobalVarG2.gsy // 18 * 10.1))
                    else:
                        GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestra, (GlobalVarG2.gsx // 32 * 19.9, GlobalVarG2.gsy // 18 * 10.1))
                messaggio("Schermo intero", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11.7, 70)
                if schermoInteroTemp:
                    messaggio("Si", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 11.8, 60)
                else:
                    messaggio("No", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 11.8, 60)
                if voceMarcata == 5:
                    if tastop == pygame.K_a or (sinistroMousePremuto and cursoreSuFrecciaSinistra):
                        GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistraBloccato, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 11.7))
                    else:
                        GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniSinistra, (GlobalVarG2.gsx // 32 * 14.7, GlobalVarG2.gsy // 18 * 11.7))
                    if tastop == pygame.K_d or (sinistroMousePremuto and cursoreSuFrecciaDestra):
                        GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreImpostazioniDestraBloccato, (GlobalVarG2.gsx // 32 * 17.2, GlobalVarG2.gsy // 18 * 11.7))
                    else:
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
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatorevecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    imgOmbreggiatoraContorniMappaMenu = pygame.transform.scale(GlobalVarG2.imgOmbreggiatoraContorniMappaMenu, (GlobalVarG2.gsx, GlobalVarG2.gsy))
    xp = GlobalVarG2.gsx // 32 * 1
    yp = GlobalVarG2.gsy // 18 * 4.5
    risposta = False
    voceMarcata = 1
    voceMarcataSottoMenu = False
    primoFrame = True


    aggiornaInterfacciaPerMouse = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    tastop = 0
    tastotempfps = 5

    # carico la mappa a seconda dell'avanzamento
    imgMappaOrig = GlobalVarG2.imgMappa1
    postiSbloccati = {"Casa": False, "Città": False, "Avamposto di Rod": False, "Castello": False, "Palazzo di Rod": False, "Vulcano": False, "Laboratorio": False, "Foresta cadetta": False, "Selva arida": False, "Labirinto": False, "Passo montano": False, "Caverna": False, "Tunnel di Rod": False, "Tunnel subacqueo": False}
    if progresso >= 0:
        postiSbloccati["Casa"] = True
        imgMappaOrig = GlobalVarG2.imgMappa1
        if progresso >= 0:
            postiSbloccati["Foresta cadetta"] = True
            imgMappaOrig = GlobalVarG2.imgMappa2
        if progresso >= 0:
            postiSbloccati["Città"] = True
            imgMappaOrig = GlobalVarG2.imgMappa3
        if progresso >= 0:
            postiSbloccati["Selva arida"] = True
            imgMappaOrig = GlobalVarG2.imgMappa4
        if progresso >= 0:
            postiSbloccati["Avamposto di Rod"] = True
            imgMappaOrig = GlobalVarG2.imgMappa5
        if progresso >= 0:
            postiSbloccati["Labirinto"] = True
            imgMappaOrig = GlobalVarG2.imgMappa6
        if progresso >= 0:
            postiSbloccati["Castello"] = True
            imgMappaOrig = GlobalVarG2.imgMappa7
        if progresso >= 0:
            postiSbloccati["Passo montano"] = True
            imgMappaOrig = GlobalVarG2.imgMappa8
        if progresso >= 0:
            postiSbloccati["Palazzo di Rod"] = True
            imgMappaOrig = GlobalVarG2.imgMappa9
        if progresso >= 0:
            postiSbloccati["Caverna"] = True
            imgMappaOrig = GlobalVarG2.imgMappa10
        if progresso >= 0:
            postiSbloccati["Vulcano"] = True
            imgMappaOrig = GlobalVarG2.imgMappa10
        if progresso >= 0:
            postiSbloccati["Tunnel di Rod"] = True# <- il tunnel di Rod è diviso in due parti
            imgMappaOrig = GlobalVarG2.imgMappa11
        if progresso >= 0:
            postiSbloccati["Tunnel di Rod"] = True
            imgMappaOrig = GlobalVarG2.imgMappa12
        if progresso >= 0:
            postiSbloccati["Tunnel subacqueo"] = True
            imgMappaOrig = GlobalVarG2.imgMappa13
        if progresso >= 0:
            postiSbloccati["Laboratorio"] = True
            imgMappaOrig = GlobalVarG2.imgMappa14

    GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.suonoAperturaMappa)
    while not risposta:
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
            elif not voceMarcataSottoMenu and GlobalVarG2.gsx // 32 * 1 <= xMouse <= GlobalVarG2.gsx // 32 * 10:
                if GlobalVarG2.gsy // 18 * 4.3 <= yMouse <= GlobalVarG2.gsy // 18 * 5.1:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 4.5
                elif GlobalVarG2.gsy // 18 * 5.1 <= yMouse <= GlobalVarG2.gsy // 18 * 5.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 5.3
                elif GlobalVarG2.gsy // 18 * 5.9 <= yMouse <= GlobalVarG2.gsy // 18 * 6.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 6.1
                elif GlobalVarG2.gsy // 18 * 6.7 <= yMouse <= GlobalVarG2.gsy // 18 * 7.5:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 6.9
                elif GlobalVarG2.gsy // 18 * 7.5 <= yMouse <= GlobalVarG2.gsy // 18 * 8.3:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 7.7
                elif GlobalVarG2.gsy // 18 * 8.3 <= yMouse <= GlobalVarG2.gsy // 18 * 9.1:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 8.5
                elif GlobalVarG2.gsy // 18 * 9.1 <= yMouse <= GlobalVarG2.gsy // 18 * 9.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 9.3
                elif GlobalVarG2.gsy // 18 * 10.5 <= yMouse <= GlobalVarG2.gsy // 18 * 11.3:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 10.7
                elif GlobalVarG2.gsy // 18 * 11.3 <= yMouse <= GlobalVarG2.gsy // 18 * 12.1:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 11.5
                elif GlobalVarG2.gsy // 18 * 12.1 <= yMouse <= GlobalVarG2.gsy // 18 * 12.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 12.3
                elif GlobalVarG2.gsy // 18 * 12.9 <= yMouse <= GlobalVarG2.gsy // 18 * 13.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 13.1
                elif GlobalVarG2.gsy // 18 * 13.7 <= yMouse <= GlobalVarG2.gsy // 18 * 14.5:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 13.9
                elif GlobalVarG2.gsy // 18 * 14.5 <= yMouse <= GlobalVarG2.gsy // 18 * 15.3:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 14.7
                elif GlobalVarG2.gsy // 18 * 15.3 <= yMouse <= GlobalVarG2.gsy // 18 * 16.1:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 15.5
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
                tastop = event.key
                tastotempfps = 5
                if (event.key == pygame.K_q or event.key == pygame.K_a) and not tastoTrovato:
                    tastoTrovato = True
                    if voceMarcataSottoMenu:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        voceMarcataSottoMenu = False
                    elif event.key == pygame.K_q:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        risposta = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True

            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse:
                if voceMarcataSottoMenu:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    voceMarcataSottoMenu = False
                else:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    risposta = True
            if (event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_d)) or (GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato):
                tastop = "spazioOsinistroMouse"
                tastoTrovato = True
                if event.type == pygame.MOUSEBUTTONDOWN and suTornaIndietro:
                    if voceMarcataSottoMenu:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        voceMarcataSottoMenu = False
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        risposta = True
                elif not voceMarcataSottoMenu or (GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato):
                    luogoMarcato = ""
                    if voceMarcata == 1:
                        luogoMarcato = "Casa"
                    if voceMarcata == 2:
                        luogoMarcato = "Città"
                    if voceMarcata == 3:
                        luogoMarcato = "Avamposto di Rod"
                    if voceMarcata == 4:
                        luogoMarcato = "Castello"
                    if voceMarcata == 5:
                        luogoMarcato = "Palazzo di Rod"
                    if voceMarcata == 6:
                        luogoMarcato = "Vulcano"
                    if voceMarcata == 7:
                        luogoMarcato = "Laboratorio"
                    if voceMarcata == 8:
                        luogoMarcato = "Foresta cadetta"
                    if voceMarcata == 9:
                        luogoMarcato = "Selva arida"
                    if voceMarcata == 10:
                        luogoMarcato = "Labirinto"
                    if voceMarcata == 11:
                        luogoMarcato = "Passo montano"
                    if voceMarcata == 12:
                        luogoMarcato = "Caverna"
                    if voceMarcata == 13:
                        luogoMarcato = "Tunnel di Rod"
                    if voceMarcata == 14:
                        luogoMarcato = "Tunnel subacqueo"
                    if postiSbloccati[luogoMarcato]:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        tastoTrovato = True
                        voceMarcataSottoMenu = True
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            elif GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and GlobalVarG2.mouseBloccato:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if (sinistroMouse or centraleMouse or destroMouse) and not GlobalVarG2.mouseVisibile:
                aggiornaInterfacciaPerMouse = True
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True

            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if primoMovimento or tastop == "spazioOsinistroMouse" or tastop == pygame.K_q or tastop == pygame.K_SPACE or tastop == pygame.K_a or tastop == pygame.K_d or ((tastop == pygame.K_w or tastop == pygame.K_s) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerMouse:
            aggiornaInterfacciaPerMouse = False
            primoFrame = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_s):
                tastotempfps = 2
            if tastop == pygame.K_w:
                if GlobalVarG2.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVarG2.mouseVisibile = False
                if not voceMarcataSottoMenu:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    if voceMarcata == 1:
                        voceMarcata = 14
                        yp = GlobalVarG2.gsy // 18 * 15.5
                    elif voceMarcata == 8:
                        voceMarcata -= 1
                        yp = yp - GlobalVarG2.gpy * 1.4
                    else:
                        voceMarcata -= 1
                        yp = yp - GlobalVarG2.gpy * 0.8
            if tastop == pygame.K_s:
                if GlobalVarG2.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVarG2.mouseVisibile = False
                if not voceMarcataSottoMenu:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    if voceMarcata == 14:
                        voceMarcata = 1
                        yp = GlobalVarG2.gsy // 18 * 4.5
                    elif voceMarcata == 7:
                        voceMarcata += 1
                        yp = yp + GlobalVarG2.gpy * 1.4
                    else:
                        voceMarcata += 1
                        yp = yp + GlobalVarG2.gpy * 0.8

            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            if not voceMarcataSottoMenu:
                imgMappa = pygame.transform.scale(imgMappaOrig, (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 15))
                GlobalVarG2.schermo.blit(imgMappa, (GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 2.5))
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 12.5))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 4))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 15.5))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))
            else:
                imgMappa = pygame.transform.scale(imgMappaOrig, (GlobalVarG2.gpx * 50, GlobalVarG2.gpy * 35))
                if voceMarcata == 1:
                    GlobalVarG2.schermo.blit(imgMappa, (GlobalVarG2.gsx // 32 * (-16), GlobalVarG2.gsy // 18 * 1))
                if voceMarcata == 2:
                    GlobalVarG2.schermo.blit(imgMappa, (GlobalVarG2.gsx // 32 * (-4.5), GlobalVarG2.gsy // 18 * (-1.5)))
                if voceMarcata == 3:
                    GlobalVarG2.schermo.blit(imgMappa, (GlobalVarG2.gsx // 32 * (3), GlobalVarG2.gsy // 18 * (-9.5)))
                if voceMarcata == 4:
                    GlobalVarG2.schermo.blit(imgMappa, (GlobalVarG2.gsx // 32 * (8.5), GlobalVarG2.gsy // 18 * (-17)))
                if voceMarcata == 5:
                    GlobalVarG2.schermo.blit(imgMappa, (GlobalVarG2.gsx // 32 * (7.5), GlobalVarG2.gsy // 18 * (-0.5)))
                if voceMarcata == 6:
                    GlobalVarG2.schermo.blit(imgMappa, (GlobalVarG2.gsx // 32 * (16), GlobalVarG2.gsy // 18 * (0)))
                if voceMarcata == 7:
                    GlobalVarG2.schermo.blit(imgMappa, (GlobalVarG2.gsx // 32 * (-8), GlobalVarG2.gsy // 18 * (-17)))
                if voceMarcata == 8:
                    GlobalVarG2.schermo.blit(imgMappa, (GlobalVarG2.gsx // 32 * (-13.5), GlobalVarG2.gsy // 18 * (-5)))
                if voceMarcata == 9:
                    GlobalVarG2.schermo.blit(imgMappa, (GlobalVarG2.gsx // 32 * (0.5), GlobalVarG2.gsy // 18 * (-8)))
                if voceMarcata == 10:
                    GlobalVarG2.schermo.blit(imgMappa, (GlobalVarG2.gsx // 32 * (4), GlobalVarG2.gsy // 18 * (-13)))
                if voceMarcata == 11:
                    GlobalVarG2.schermo.blit(imgMappa, (GlobalVarG2.gsx // 32 * (3.5), GlobalVarG2.gsy // 18 * (-1.5)))
                if voceMarcata == 12:
                    GlobalVarG2.schermo.blit(imgMappa, (GlobalVarG2.gsx // 32 * (11.5), GlobalVarG2.gsy // 18 * (0)))
                if voceMarcata == 13:
                    GlobalVarG2.schermo.blit(imgMappa, (GlobalVarG2.gsx // 32 * (7), GlobalVarG2.gsy // 18 * (-6)))
                if voceMarcata == 14:
                    GlobalVarG2.schermo.blit(imgMappa, (GlobalVarG2.gsx // 32 * (-1.5), GlobalVarG2.gsy // 18 * (-18.5)))
                GlobalVarG2.schermo.blit(imgOmbreggiatoraContorniMappaMenu, (0, 0))
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 12.5))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 4))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 15.5))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 12.5))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 4))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 15.5))
                GlobalVarG2.schermo.blit(puntatorevecchio, (xp, yp))
                if voceMarcata == 1:
                    messaggio("Casa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 5, 70)
                    messaggio(u"È l'abitazione in cui ho vissuto con la", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 6.5, 45)
                    messaggio(u"mia famiglia fin'ora. È stata costruita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.2, 45)
                    messaggio("da un mio vecchio antenato e, da", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.9, 45)
                    messaggio(u"allora, è sempre stata abitata dalle", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 8.6, 45)
                    messaggio("varie generazioni della mia famiglia.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 9.3, 45)
                    messaggio(u"Secondo il babbo io sarò il prossimo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10, 45)
                    messaggio("proprietario e l'idea non mi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10.7, 45)
                    messaggio("entusiasma affatto: non voglio fare", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 11.4, 45)
                    messaggio("il contadino per tutta la vita come", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.1, 45)
                    messaggio(u"lui! È un lavoro monotono, faticoso e", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.8, 45)
                    messaggio("anche instabile a causa delle enormi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 13.5, 45)
                    messaggio("imposte dello stato e della spietata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.2, 45)
                    messaggio("concorrenza.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.9, 45)
                if voceMarcata == 2:
                    messaggio(u"Città", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 5, 70)
                    messaggio("Da quando ne ho sentito parlare per", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 6.5, 45)
                    messaggio("la prima volta, ho sempre avuto il", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.2, 45)
                    messaggio("desiderio di viverci. Da quello che ho", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.9, 45)
                    messaggio(u"sentito, lì a tutti è concesso di poter", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 8.6, 45)
                    messaggio(u"scegliere quale attività svolgere per", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 9.3, 45)
                    messaggio(u"sopravvivere: non necessariamente", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10, 45)
                    messaggio(u"tutti devono coltivare o cacciare dato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10.7, 45)
                    messaggio(u"che, con il sistema che è stato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 11.4, 45)
                    messaggio("organizzato, poche persone sono", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.1, 45)
                    messaggio("capaci di produrre per tutte le altre.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.8, 45)
                    messaggio("Quest'ultime possono quindi dedicarsi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 13.5, 45)
                    messaggio(u"ad altre attività come musica, teatro,", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.2, 45)
                    messaggio(u"studio, sport e chissà cos'altro.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.9, 45)
                if voceMarcata == 3:
                    messaggio("Avamposto di Rod", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 5, 70)
                    messaggio("Una piccola baracca che Rod esalta", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 6.5, 45)
                    messaggio("in maniera esagerata definendola", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.2, 45)
                    messaggio("\"avamposto\".", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.9, 45)
                    messaggio(u"Quella non è la sua abitazione ma,", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 8.6, 45)
                    messaggio("a suo dire, un luogo strategicamente", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 9.3, 45)
                    messaggio("fondamentale per la sopravvivenza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10, 45)
                    messaggio("dell'intero ecosistema cittadino.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10.7, 45)
                    messaggio(u"Rod mi è sempre sembrato un po'", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 11.4, 45)
                    messaggio("strano, ma, tutti i suoi pensieri e", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.1, 45)
                    messaggio("ragionamenti mi sembrano ponderati", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.8, 45)
                    messaggio("e coerenti... mi domando cosa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 13.5, 45)
                    messaggio("nasconda quella baracca...", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.2, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.9, 45)
                if voceMarcata == 4:
                    messaggio("Castello", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 5, 70)
                    messaggio(u"La più grande struttura che abbia", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 6.5, 45)
                    messaggio("mai visto fino ad ora.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.2, 45)
                    messaggio(u"È un castello composto da un", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.9, 45)
                    messaggio("centinaio di stanze abitato dal", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 8.6, 45)
                    messaggio("maestro del bibliotecario e dai", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 9.3, 45)
                    messaggio("suoi numerosi servitori.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10, 45)
                    messaggio(u"Il vasto terreno su cui è stato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10.7, 45)
                    messaggio("costruito, comprende anche l'intero", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 11.4, 45)
                    messaggio(u"labirinto che è stato appositamente", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.1, 45)
                    messaggio("elaborato per tenere lontani i", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.8, 45)
                    messaggio("visitatori indesiderati. Il silenzio", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 13.5, 45)
                    messaggio("e il comportamento dei servi creano", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.2, 45)
                    messaggio("un'atmosfera un po' malinconica...", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.9, 45)
                if voceMarcata == 5:
                    messaggio("Palazzo di Rod", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 5, 70)
                    messaggio("La villa in cui dimora Rod.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 6.5, 45)
                    messaggio("Risulta essere quasi sempre vuota e", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.2, 45)
                    messaggio(u"silenziosa dato che lui è sempre", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.9, 45)
                    messaggio("fuori per lavoro o ricerche (mi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 8.6, 45)
                    messaggio("domando ancora cosa stia", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 9.3, 45)
                    messaggio("ricercando...).", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10, 45)
                    messaggio("Il posto ricorda vagamente il", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10.7, 45)
                    messaggio("castello di Norm ma in miniatura", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 11.4, 45)
                    messaggio("e con un passaggio montano al", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.1, 45)
                    messaggio("posto del labirinto.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.8, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 13.5, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.2, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.9, 45)
                if voceMarcata == 6:
                    messaggio("Vulcano", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 5, 70)
                    messaggio("Un vulcano sommerso nelle ", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 6.5, 45)
                    messaggio(u"montagne a ovest della città.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.2, 45)
                    messaggio(u"È simile ad una montagna ma più", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.9, 45)
                    messaggio("grande e con un cratere sulla cima,", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 8.6, 45)
                    messaggio("dalla quale, a detta di Rod,", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 9.3, 45)
                    messaggio("fuoriesce del vapore incandescente.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10, 45)
                    messaggio(u"Chissà cosa c'è lì dentro...", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10.7, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 11.4, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.1, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.8, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 13.5, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.2, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.9, 45)
                if voceMarcata == 7:
                    messaggio("Laboratorio", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 5, 70)
                    messaggio("Il laboratorio in cui Norm svolge", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 6.5, 45)
                    messaggio("le sue ricerche.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.2, 45)
                    messaggio(u"È molto piccolo ma al suo interno", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.9, 45)
                    messaggio(u"è presente tutto ciò che serve,", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 8.6, 45)
                    messaggio("ossia un calcolatore di eventi,", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 9.3, 45)
                    messaggio("che si estende anche sotto il", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10, 45)
                    messaggio("terreno, e alcuni altri calcolatori", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10.7, 45)
                    messaggio("che credo servano per gestire", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 11.4, 45)
                    messaggio("i sistemi di alimentazione e", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.1, 45)
                    messaggio("raffreddamento.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.8, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 13.5, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.2, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.9, 45)
                if voceMarcata == 8:
                    messaggio("Foresta cadetta", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 5, 70)
                    messaggio("La foresta che mi ha sempre separato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 6.5, 45)
                    messaggio(u"dalla città... non mi è mai stato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.2, 45)
                    messaggio(u"concesso attraversarla perchè", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.9, 45)
                    messaggio("entrambi i miei genitori la ritenevano", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 8.6, 45)
                    messaggio("troppo pericolosa per me.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 9.3, 45)
                    messaggio("Il nome deriva dal fatto che viene", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10, 45)
                    messaggio("utilizzata come terreno di prova per", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10.7, 45)
                    messaggio("selezionare, tra i giovani ", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 11.4, 45)
                    messaggio(u"appartenenti alla nobiltà, i futuri", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.1, 45)
                    messaggio("ufficiali dell'esercito.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.8, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 13.5, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.2, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.9, 45)
                if voceMarcata == 9:
                    messaggio("Selva arida", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 5, 70)
                    messaggio(u"Denominata in questo modo perchè", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 6.5, 45)
                    messaggio("un tempo fitta e intricata ed ora", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.2, 45)
                    messaggio("composta soltanto da secchi abusti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.9, 45)
                    messaggio("e funghi.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 8.6, 45)
                    messaggio("Le ragioni di questo suo decadimento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 9.3, 45)
                    messaggio("non sono note agli abitanti locali", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10, 45)
                    messaggio("ma, diversi libri della biblioteca", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10.7, 45)
                    messaggio(u"in città, sostenevano che ciò fosse", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 11.4, 45)
                    messaggio("dovuto ad un cambiamento climatico", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.1, 45)
                    messaggio("avvenuto circa 50 anni fa... strano...", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.8, 45)
                    messaggio(u"Rod è solito attraversarla per", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 13.5, 45)
                    messaggio("tornare al suo avamposto.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.2, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.9, 45)
                if voceMarcata == 10:
                    messaggio("Labirinto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 5, 70)
                    messaggio("Un enorme terreno estremamente", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 6.5, 45)
                    messaggio("complicato da superare a causa delle", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.2, 45)
                    messaggio("innumerevoli strade percorribili al", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.9, 45)
                    messaggio("suo interno prive di punti di", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 8.6, 45)
                    messaggio("riferimento.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 9.3, 45)
                    messaggio("Rod mi ha fornito una mappa che", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10, 45)
                    messaggio("mostra nel dettaglio la sua", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10.7, 45)
                    messaggio("struttura sconsigliandomi di", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 11.4, 45)
                    messaggio(u"procedere: è molto probabile non", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.1, 45)
                    messaggio("riuscire ad uscirne se non si ha", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.8, 45)
                    messaggio("un buon senso dell'orientamento.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 13.5, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.2, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.9, 45)
                if voceMarcata == 11:
                    messaggio("Passo montano", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 5, 70)
                    messaggio("Un passaggio tra le alture a ovest", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 6.5, 45)
                    messaggio(u"della città.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.2, 45)
                    messaggio(u"In città nessuno sembrava sapere di", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.9, 45)
                    messaggio("questo varco apparte Rod che lo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 8.6, 45)
                    messaggio("utilizza per raggiungere il proprio", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 9.3, 45)
                    messaggio("palazzo in mezzo alle montagne da", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10, 45)
                    messaggio(u"più di vent'anni.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10.7, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 11.4, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.1, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.8, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 13.5, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.2, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.9, 45)
                if voceMarcata == 12:
                    messaggio("Caverna", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 5, 70)
                    messaggio("Una caverna in mezzo alle montagne", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 6.5, 45)
                    messaggio("che conduce ad un vulcano.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.2, 45)
                    messaggio("All'interno vivono degli animali", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.9, 45)
                    messaggio("simili a Colco ma aggressivi.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 8.6, 45)
                    messaggio(u"Rod è solito avventurarsi in quel", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 9.3, 45)
                    messaggio("posto per recuperare alimentazioni.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10, 45)
                    messaggio(u"Non mi spiego perché abbia deciso", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10.7, 45)
                    messaggio(u"di vivere così vicino a quel posto...", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 11.4, 45)
                    messaggio("forse per controllare gli accessi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.1, 45)
                    messaggio("alla caverna?", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.8, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 13.5, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.2, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.9, 45)
                if voceMarcata == 13:
                    messaggio("Tunnel di Rod", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 5, 70)
                    messaggio(u"È un passaggio sicuro e veloce tra", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 6.5, 45)
                    messaggio("il palazzo di Rod e il suo avamposto.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.2, 45)
                    messaggio("Rod lo utilizzava per trasportare", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.9, 45)
                    messaggio("direttamente le alimentazioni dalla", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 8.6, 45)
                    messaggio("caverna al castello di Norm.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 9.3, 45)
                    messaggio("Adesso capisco l'importanza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10, 45)
                    messaggio("\"strategica\" di questi luoghi.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10.7, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 11.4, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.1, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.8, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 13.5, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.2, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.9, 45)
                if voceMarcata == 14:
                    messaggio("Tunnel subacqueo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 5, 70)
                    messaggio("Un passaggio segreto nei sotterranei", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 6.5, 45)
                    messaggio("del castello di Norm che porta al", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.2, 45)
                    messaggio("suo laboratorio principale sul fondo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 7.9, 45)
                    messaggio("del lago.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 8.6, 45)
                    messaggio("Nonostante le pareti del tunnel siano", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 9.3, 45)
                    messaggio("fatte di un materiale trasparente", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10, 45)
                    messaggio("simile al vetro, non si riesce ad", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 10.7, 45)
                    messaggio("ammirare chiaramente il fondale del", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 11.4, 45)
                    messaggio("bacino a causa delle sostanze di cui", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.1, 45)
                    messaggio(u"questo è stato riempito.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 12.8, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 13.5, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.2, 45)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 14.9, 45)

            messaggio("Mappa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
            if postiSbloccati["Casa"]:
                messaggio("Casa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 4.5, 45)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 4.5, 45)
            if postiSbloccati["Città"]:
                messaggio(u"Città", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 5.3, 45)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 5.3, 45)
            if postiSbloccati["Avamposto di Rod"]:
                messaggio("Avamposto di Rod", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.1, 45)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.1, 45)
            if postiSbloccati["Castello"]:
                messaggio("Castello", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.9, 45)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.9, 45)
            if postiSbloccati["Palazzo di Rod"]:
                messaggio("Palazzo di Rod", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7.7, 45)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7.7, 45)
            if postiSbloccati["Vulcano"]:
                messaggio("Vulcano", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8.5, 45)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8.5, 45)
            if postiSbloccati["Laboratorio"]:
                messaggio("Laboratorio", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9.3, 45)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9.3, 45)
            if postiSbloccati["Foresta cadetta"]:
                messaggio("Foresta cadetta", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10.7, 45)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10.7, 45)
            if postiSbloccati["Selva arida"]:
                messaggio("Selva arida", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11.5, 45)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11.5, 45)
            if postiSbloccati["Labirinto"]:
                messaggio("Labirinto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12.3, 45)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12.3, 45)
            if postiSbloccati["Passo montano"]:
                messaggio("Passo montano", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13.1, 45)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13.1, 45)
            if postiSbloccati["Caverna"]:
                messaggio("Caverna", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13.9, 45)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13.9, 45)
            if postiSbloccati["Tunnel di Rod"]:
                messaggio("Tunnel di Rod", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14.7, 45)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14.7, 45)
            if postiSbloccati["Tunnel subacqueo"]:
                messaggio("Tunnel subacqueo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15.5, 45)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15.5, 45)

            messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
            if not voceMarcataSottoMenu:
                GlobalVarG2.schermo.blit(puntatore, (xp, yp))

            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)


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
                if (event.key == pygame.K_q or event.key == pygame.K_a) and not tastoTrovato:
                    tastoTrovato = True
                    if voceMarcataSottoMenu != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        voceMarcataSottoMenu = 0
                        xp = xpv
                        yp = ypv
                    elif event.key == pygame.K_q:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        risposta = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if (event.key == pygame.K_SPACE or event.key == pygame.K_d) and not tastoTrovato:
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

        if primoMovimento or tastop == pygame.K_q or tastop == pygame.K_SPACE or tastop == pygame.K_a or tastop == pygame.K_d or ((tastop == pygame.K_w or tastop == pygame.K_s) and tastotempfps == 0) or primoFrame:
            primoFrame = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_s):
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
