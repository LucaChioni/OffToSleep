# -*- coding: utf-8 -*-

from CaricaSalvaPartita import *


def scegli_sal(possibileSalvare, lunghezzadati, porteini, portefin, cofaniini, cofanifin, porteAttuali, cofanettiAttuali, vitaescaAttuali, vettoreDenaroAttuali, datiAttuali, listaNemiciTotaliAttuali, stanzeGiaVisitateAttuali, listaPersonaggiTotaliAttuali, oggettiRimastiASamAttuali):
    puntatore = GlobalVar.puntatore
    puntatorevecchio = GlobalVar.puntatorevecchio
    xp = GlobalVar.gsx // 32 * 6.5
    yp = GlobalVar.gsy // 18 * 9.5
    vxp = xp
    vyp = yp
    if possibileSalvare:
        cosa = 3
    else:
        cosa = 1

    tastop = 0
    tastotempfps = 5

    aggiornaInterfacciaPerMouse = False
    risposta = False
    conferma = False
    primaconf = False
    salMarcato = 1
    voceMarcata = 2
    primoFrame = True
    aggiornaSchermo = False
    n = -1
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    # carico solo all'inizio i salvataggi
    contasalva = 1
    vetDatiSalvataggi = []
    while contasalva <= 3:
        dati, errore = caricaPartita(contasalva, lunghezzadati, porteini, portefin, cofaniini, cofanifin, False)
        vetTempDati = []
        vetTempDati.append(dati)
        vetTempDati.append(errore)
        vetDatiSalvataggi.append(vetTempDati)
        contasalva += 1

    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0 and tastop != 0:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        salMarcatoVecchio = salMarcato
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        suTornaIndietro = False
        suCambiaOperazione = False
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVar.mouseVisibile:
            aggiornaInterfacciaPerMouse = True
            pygame.mouse.set_visible(True)
            GlobalVar.mouseVisibile = True
        if GlobalVar.mouseVisibile:
            if not conferma:
                if GlobalVar.gsx // 32 * 21.8 <= xMouse <= GlobalVar.gsx and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    suTornaIndietro = True
                elif GlobalVar.gsx // 32 * 11.5 <= xMouse <= GlobalVar.gsx // 32 * 21.8 and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    suCambiaOperazione = True
                elif GlobalVar.gsy // 18 * 7 <= yMouse <= GlobalVar.gsy // 18 * 16.5:
                    if GlobalVar.gsx // 32 * 5 <= xMouse <= GlobalVar.gsx // 32 * 12.3:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        salMarcato = 1
                        xp = GlobalVar.gsx // 32 * 6.5
                        yp = GlobalVar.gsy // 18 * 9.5
                    elif GlobalVar.gsx // 32 * 12.3 <= xMouse <= GlobalVar.gsx // 32 * 19.7:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        salMarcato = 2
                        xp = GlobalVar.gsx // 32 * 13.5
                        yp = GlobalVar.gsy // 18 * 9.5
                    elif GlobalVar.gsx // 32 * 19.7 <= xMouse <= GlobalVar.gsx // 32 * 27:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        salMarcato = 3
                        xp = GlobalVar.gsx // 32 * 20.5
                        yp = GlobalVar.gsy // 18 * 9.5
                    else:
                        if not GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(True)
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            else:
                if GlobalVar.gsx // 32 * 21.8 <= xMouse <= GlobalVar.gsx and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    suTornaIndietro = True
                elif GlobalVar.gsx // 32 * 11.5 <= xMouse <= GlobalVar.gsx // 32 * 21.8 and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    suCambiaOperazione = True
                elif GlobalVar.gsy // 18 * 5.2 <= yMouse <= GlobalVar.gsy // 18 * 7:
                    if GlobalVar.gsx // 32 * 18 <= xMouse <= GlobalVar.gsx // 32 * 22.5:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalVar.gsx // 32 * 19.5
                        yp = GlobalVar.gsy // 18 * 5.7
                    elif GlobalVar.gsx // 32 * 22.5 <= xMouse <= GlobalVar.gsx // 32 * 27:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalVar.gsx // 32 * 22.5
                        yp = GlobalVar.gsy // 18 * 5.7
                    else:
                        if not GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(True)
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            if (voceMarcataVecchia != voceMarcata or salMarcatoVecchio != salMarcato) and not primoFrame:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)

        if not conferma:
            vxp = xp
            vyp = yp

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            tastotempfps = 5
            sinistroMouseVecchio = sinistroMouse
            centraleMouseVecchio = centraleMouse
            destroMouseVecchio = destroMouse
            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
            rotellaConCentralePremuto = False
            if centraleMouseVecchio and centraleMouse:
                rotellaConCentralePremuto = True
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
                GlobalVar.quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato and voceMarcataVecchia == voceMarcata and salMarcatoVecchio == salMarcato:
                if GlobalVar.mouseVisibile:
                    aggiornaInterfacciaPerMouse = True
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                tastop = event.key
                if event.key == pygame.K_q and not tastoTrovato:
                    tastoTrovato = True
                    if conferma:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                        xp = vxp
                        yp = vyp
                        conferma = False
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                        n = -1
                        return n, cosa
                if event.key == pygame.K_d and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse and not rotellaConCentralePremuto:
                tastop = "destroMouse"
                tastoTrovato = True
                if conferma:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    xp = vxp
                    yp = vyp
                    conferma = False
                else:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    n = -1
                    return n, cosa
            if (event.type == pygame.KEYDOWN and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT)) or (GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and centraleMouse and not rotellaConCentralePremuto):
                tastop = "centraleMouse"
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                tastoTrovato = True
                xp = vxp
                yp = vyp
                conferma = False
                if possibileSalvare:
                    if cosa == 1:
                        cosa = 2
                    elif cosa == 2:
                        cosa = 3
                    elif cosa == 3:
                        cosa = 1
                else:
                    if cosa == 1:
                        cosa = 2
                    elif cosa == 2:
                        cosa = 1
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and not GlobalVar.mouseBloccato):
                tastop = "spazioOsinistroMouse"
                tastoTrovato = True
                if event.type == pygame.MOUSEBUTTONDOWN and suTornaIndietro:
                    if conferma:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                        xp = vxp
                        yp = vyp
                        conferma = False
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                        n = -1
                        return n, cosa
                elif event.type == pygame.MOUSEBUTTONDOWN and suCambiaOperazione:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                    xp = vxp
                    yp = vyp
                    conferma = False
                    if possibileSalvare:
                        if cosa == 1:
                            cosa = 2
                        elif cosa == 2:
                            cosa = 3
                        elif cosa == 3:
                            cosa = 1
                    else:
                        if cosa == 1:
                            cosa = 2
                        elif cosa == 2:
                            cosa = 1
                else:
                    if conferma:
                        if voceMarcata == 1:
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                            if cosa == 1:
                                dati, listaNemiciTotali, datiEsche, datiMonete, stanzeGiaVisitate, listaPersonaggiTotali, oggettiRimastiASam = caricaPartita(n, lunghezzadati, porteini, portefin, cofaniini, cofanifin)
                                if dati:
                                    return n, cosa
                                else:
                                    conferma = False
                                    xp = vxp
                                    yp = vyp
                                primoFrame = True
                            elif cosa == 3:
                                salvataggio(n, datiAttuali, porteini, portefin, cofaniini, cofanifin, porteAttuali, cofanettiAttuali, listaNemiciTotaliAttuali, vitaescaAttuali, vettoreDenaroAttuali, stanzeGiaVisitateAttuali, listaPersonaggiTotaliAttuali, oggettiRimastiASamAttuali)
                                # ricarico i salvataggi
                                contasalva = 1
                                vetDatiSalvataggi = []
                                while contasalva <= 3:
                                    dati, errore = caricaPartita(contasalva, lunghezzadati, porteini, portefin, cofaniini, cofanifin, False)
                                    vetTempDati = []
                                    vetTempDati.append(dati)
                                    vetTempDati.append(errore)
                                    vetDatiSalvataggi.append(vetTempDati)
                                    contasalva += 1
                                xp = vxp
                                yp = vyp
                                conferma = False
                                primoFrame = True
                            elif cosa == 2:
                                leggi = GlobalVar.loadFile("Salvataggi/Salvataggio%i.txt" % n, "w")
                                leggi.close()
                                # ricarico i salvataggi
                                contasalva = 1
                                vetDatiSalvataggi = []
                                while contasalva <= 3:
                                    dati, errore = caricaPartita(contasalva, lunghezzadati, porteini, portefin, cofaniini, cofanifin, False)
                                    vetTempDati = []
                                    vetTempDati.append(dati)
                                    vetTempDati.append(errore)
                                    vetDatiSalvataggi.append(vetTempDati)
                                    contasalva += 1
                                xp = vxp
                                yp = vyp
                                conferma = False
                                primoFrame = True
                        if voceMarcata == 2:
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                            xp = vxp
                            yp = vyp
                            conferma = False
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                        conferma = True
                        primaconf = True
                        n = salMarcato
            elif GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and GlobalVar.mouseBloccato:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
            if (sinistroMouse or centraleMouse or destroMouse) and not rotellaConCentralePremuto and not GlobalVar.mouseVisibile:
                aggiornaInterfacciaPerMouse = True
                pygame.mouse.set_visible(True)
                GlobalVar.mouseVisibile = True

            if tastop != 0:
                aggiornaSchermo = True

            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0
            if event.type == pygame.MOUSEBUTTONUP:
                tastop = 0

        if aggiornaSchermo or primoMovimento or tastop == pygame.K_q or tastop == "spazioOsinistroMouse" or tastop == "centraleMouse" or tastop == "destroMouse" or tastop == pygame.K_LSHIFT or tastop == pygame.K_RSHIFT or ((tastop == pygame.K_a or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or salMarcatoVecchio != salMarcato or aggiornaInterfacciaPerMouse:
            aggiornaSchermo = False
            aggiornaInterfacciaPerMouse = False
            if not primoMovimento and (tastop == pygame.K_a or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_a:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if conferma:
                    if voceMarcata == 2:
                        voceMarcata -= 1
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        xp = GlobalVar.gsx // 32 * 19.5
                else:
                    if salMarcato == 3:
                        salMarcato -= 1
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        xp = GlobalVar.gsx // 32 * 13.5
                    elif salMarcato == 2:
                        salMarcato -= 1
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        xp = GlobalVar.gsx // 32 * 6.5
                    elif salMarcato == 1:
                        salMarcato += 2
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        xp = GlobalVar.gsx // 32 * 20.5
            if tastop == pygame.K_d:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if conferma:
                    if voceMarcata == 1:
                        voceMarcata += 1
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        xp = GlobalVar.gsx // 32 * 22.5
                else:
                    if salMarcato == 1:
                        salMarcato += 1
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        xp = GlobalVar.gsx // 32 * 13.5
                    elif salMarcato == 2:
                        salMarcato += 1
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        xp = GlobalVar.gsx // 32 * 20.5
                    elif salMarcato == 3:
                        salMarcato -= 2
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        xp = GlobalVar.gsx // 32 * 6.5

            if primoFrame or tastop == "centraleMouse" or tastop == pygame.K_LSHIFT or tastop == pygame.K_RSHIFT or (tastop == "spazioOsinistroMouse" and suCambiaOperazione):
                GlobalVar.schermo.fill(GlobalVar.grigioscu)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                if cosa == 2:
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.rossoScuro, (GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 7, GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 9.5))
                elif cosa == 1:
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.bluScuro, (GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 7, GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 9.5))
                else:
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.verdeScuro, (GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 7, GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 9.5))
                GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoSinistra, (GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 7))
                GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoDestra, (GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 7))
                GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoBassoDestra, (GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 15.5))
                GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoBassoSinistra, (GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 15.5))
                GlobalVar.schermo.blit(GlobalVar.s1, (GlobalVar.gsx // 32 * 7.6, GlobalVar.gsy // 18 * 8))
                GlobalVar.schermo.blit(GlobalVar.s2, (GlobalVar.gsx // 32 * 14.6, GlobalVar.gsy // 18 * 8))
                GlobalVar.schermo.blit(GlobalVar.s3, (GlobalVar.gsx // 32 * 21.6, GlobalVar.gsy // 18 * 8))
                if cosa == 1:
                    messaggio("Carica partita", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 5.5, GlobalVar.gsy // 18 * 4.3, 100)
                if cosa == 2:
                    messaggio("Cancella partita", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 5.5, GlobalVar.gsy // 18 * 4.3, 100)
                if cosa == 3:
                    messaggio("Salva partita", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 5.5, GlobalVar.gsy // 18 * 4.3, 100)

                contasalva = 1
                while contasalva <= len(vetDatiSalvataggi):
                    vetTemp = vetDatiSalvataggi[contasalva - 1]
                    dati = vetTemp[0]
                    errore = vetTemp[1]
                    if errore == 1:
                        if contasalva == 1:
                            messaggio("Slot vuoto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 7.25, GlobalVar.gsy // 18 * 11, 60)
                        elif contasalva == 2:
                            messaggio("Slot vuoto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 14.25, GlobalVar.gsy // 18 * 11, 60)
                        elif contasalva == 3:
                            messaggio("Slot vuoto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 21.25, GlobalVar.gsy // 18 * 11, 60)
                    else:
                        if contasalva == 1:
                            if not errore:
                                if GlobalVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= dati[0] < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                                    perso = GlobalVar.loadImage('Immagini/Personaggi/FratelloMaggiore/Personaggio1.png', True)
                                else:
                                    perso = GlobalVar.loadImage('Immagini/Personaggi/Sara/Personaggio1.png', True)
                                persalva = pygame.transform.smoothscale(perso, (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                persSalvaBraccia = pygame.transform.smoothscale(GlobalVar.persob, (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                spasalva = pygame.transform.smoothscale(GlobalVar.vetImgSpadePixellate[dati[6]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                arcsalva = pygame.transform.smoothscale(GlobalVar.vetImgArchiPixellate[dati[128]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                armsalva = pygame.transform.smoothscale(GlobalVar.vetImgArmaturePixellate[dati[8]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                scusalva = pygame.transform.smoothscale(GlobalVar.vetImgScudiPixellate[dati[7]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                guasalva = pygame.transform.smoothscale(GlobalVar.vetImgGuantiPixellate[dati[129]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                colsalva = pygame.transform.smoothscale(GlobalVar.vetImgCollanePixellate[dati[130]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                messaggio("Livello: " + str(dati[4]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 7.1, GlobalVar.gsy // 18 * 11, 60)
                                GlobalVar.schermo.blit(arcsalva, (GlobalVar.gpx * 7.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(persalva, (GlobalVar.gpx * 7.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(persSalvaBraccia, (GlobalVar.gpx * 7.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(armsalva, (GlobalVar.gpx * 7.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(colsalva, (GlobalVar.gpx * 7.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(spasalva, (GlobalVar.gpx * 7.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(guasalva, (GlobalVar.gpx * 7.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(scusalva, (GlobalVar.gpx * 7.6, GlobalVar.gpy * 12))
                            else:
                                messaggio("Slot corrotto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 6.8, GlobalVar.gsy // 18 * 11, 60)
                        elif contasalva == 2:
                            if not errore:
                                if GlobalVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= dati[0] < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                                    perso = GlobalVar.loadImage('Immagini/Personaggi/FratelloMaggiore/Personaggio1.png', True)
                                else:
                                    perso = GlobalVar.loadImage('Immagini/Personaggi/Sara/Personaggio1.png', True)
                                persalva = pygame.transform.smoothscale(perso, (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                persSalvaBraccia = pygame.transform.smoothscale(GlobalVar.persob, (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                spasalva = pygame.transform.smoothscale(GlobalVar.vetImgSpadePixellate[dati[6]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                arcsalva = pygame.transform.smoothscale(GlobalVar.vetImgArchiPixellate[dati[128]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                armsalva = pygame.transform.smoothscale(GlobalVar.vetImgArmaturePixellate[dati[8]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                scusalva = pygame.transform.smoothscale(GlobalVar.vetImgScudiPixellate[dati[7]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                guasalva = pygame.transform.smoothscale(GlobalVar.vetImgGuantiPixellate[dati[129]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                colsalva = pygame.transform.smoothscale(GlobalVar.vetImgCollanePixellate[dati[130]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                messaggio("Livello: " + str(dati[4]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 14.1, GlobalVar.gsy // 18 * 11, 60)
                                GlobalVar.schermo.blit(arcsalva, (GlobalVar.gpx * 14.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(persalva, (GlobalVar.gpx * 14.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(persSalvaBraccia, (GlobalVar.gpx * 14.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(armsalva, (GlobalVar.gpx * 14.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(colsalva, (GlobalVar.gpx * 14.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(spasalva, (GlobalVar.gpx * 14.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(guasalva, (GlobalVar.gpx * 14.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(scusalva, (GlobalVar.gpx * 14.6, GlobalVar.gpy * 12))
                            else:
                                messaggio("Slot corrotto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 13.8, GlobalVar.gsy // 18 * 11, 60)
                        elif contasalva == 3:
                            if not errore:
                                if GlobalVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= dati[0] < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                                    perso = GlobalVar.loadImage('Immagini/Personaggi/FratelloMaggiore/Personaggio1.png', True)
                                else:
                                    perso = GlobalVar.loadImage('Immagini/Personaggi/Sara/Personaggio1.png', True)
                                persalva = pygame.transform.smoothscale(perso, (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                persSalvaBraccia = pygame.transform.smoothscale(GlobalVar.persob, (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                spasalva = pygame.transform.smoothscale(GlobalVar.vetImgSpadePixellate[dati[6]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                arcsalva = pygame.transform.smoothscale(GlobalVar.vetImgArchiPixellate[dati[128]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                armsalva = pygame.transform.smoothscale(GlobalVar.vetImgArmaturePixellate[dati[8]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                scusalva = pygame.transform.smoothscale(GlobalVar.vetImgScudiPixellate[dati[7]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                guasalva = pygame.transform.smoothscale(GlobalVar.vetImgGuantiPixellate[dati[129]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                colsalva = pygame.transform.smoothscale(GlobalVar.vetImgCollanePixellate[dati[130]], (GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                                messaggio("Livello: " + str(dati[4]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 21.1, GlobalVar.gsy // 18 * 11, 60)
                                GlobalVar.schermo.blit(arcsalva, (GlobalVar.gpx * 21.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(persalva, (GlobalVar.gpx * 21.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(persSalvaBraccia, (GlobalVar.gpx * 21.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(armsalva, (GlobalVar.gpx * 21.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(colsalva, (GlobalVar.gpx * 21.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(spasalva, (GlobalVar.gpx * 21.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(guasalva, (GlobalVar.gpx * 21.6, GlobalVar.gpy * 12))
                                GlobalVar.schermo.blit(scusalva, (GlobalVar.gpx * 21.6, GlobalVar.gpy * 12))
                            else:
                                messaggio("Slot corrotto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20.8, GlobalVar.gsy // 18 * 11, 60)
                    contasalva += 1
            else:
                pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 10, 0, GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 2.5))
                pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 3.5, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 3.5))
                pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 18, (GlobalVar.gsy // 18 * 7) - 1), (GlobalVar.gsx // 32 * 27, (GlobalVar.gsy // 18 * 7) - 1), 1)
                if cosa == 2:
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.rossoScuro, (GlobalVar.gsx // 32 * 6.5, GlobalVar.gsy // 18 * 9.5, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 0.5))
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.rossoScuro, (GlobalVar.gsx // 32 * 13.5, GlobalVar.gsy // 18 * 9.5, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 0.5))
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.rossoScuro, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 9.5, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 0.5))
                elif cosa == 1:
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.bluScuro, (GlobalVar.gsx // 32 * 6.5, GlobalVar.gsy // 18 * 9.5, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 0.5))
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.bluScuro, (GlobalVar.gsx // 32 * 13.5, GlobalVar.gsy // 18 * 9.5, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 0.5))
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.bluScuro, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 9.5, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 0.5))
                else:
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.verdeScuro, (GlobalVar.gsx // 32 * 6.5, GlobalVar.gsy // 18 * 9.5, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 0.5))
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.verdeScuro, (GlobalVar.gsx // 32 * 13.5, GlobalVar.gsy // 18 * 9.5, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 0.5))
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.verdeScuro, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 9.5, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 0.5))

            if conferma:
                if primaconf:
                    vxp = xp
                    vyp = yp
                    xp = GlobalVar.gsx // 32 * 22.5
                    yp = GlobalVar.gsy // 18 * 5.7
                    voceMarcata = 2
                    primaconf = False
                if cosa == 2:
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.rossoScuroPiuScuro, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 3.5, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 3.5))
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.rossoScuroPiuScuro, (GlobalVar.gsx // 32 * 18, (GlobalVar.gsy // 18 * 7) - 1), (GlobalVar.gsx // 32 * 27, (GlobalVar.gsy // 18 * 7) - 1), 1)
                elif cosa == 1:
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.bluScuroPiuScuro, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 3.5, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 3.5))
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.bluScuroPiuScuro, (GlobalVar.gsx // 32 * 18, (GlobalVar.gsy // 18 * 7) - 1), (GlobalVar.gsx // 32 * 27, (GlobalVar.gsy // 18 * 7) - 1), 1)
                else:
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.verdeScuroPiuScuro, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 3.5, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 3.5))
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.verdeScuroPiuScuro, (GlobalVar.gsx // 32 * 18, (GlobalVar.gsy // 18 * 7) - 1), (GlobalVar.gsx // 32 * 27, (GlobalVar.gsy // 18 * 7) - 1), 1)
                GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoSinistra, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 3.5))
                GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoDestra, (GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 3.5))
                messaggio("Confermi?", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20.4, GlobalVar.gsy // 18 * 4.2, 70)
                messaggio("Si", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20.4, GlobalVar.gsy // 18 * 5.5, 70)
                messaggio("No", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23.4, GlobalVar.gsy // 18 * 5.5, 70)
                GlobalVar.schermo.blit(puntatorevecchio, (vxp, vyp))

            if cosa == 1:
                if GlobalVar.mouseVisibile:
                    messaggio("Tasto centrale: cancella partita", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 1, 50)
                else:
                    messaggio("SHIFT: cancella partita", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 1, 50)
            if cosa == 2:
                if possibileSalvare:
                    if GlobalVar.mouseVisibile:
                        messaggio("Tasto centrale: salva partita", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 1, 50)
                    else:
                        messaggio("SHIFT: salva partita", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 1, 50)
                else:
                    if GlobalVar.mouseVisibile:
                        messaggio("Tasto centrale: carica partita", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 1, 50)
                    else:
                        messaggio("SHIFT: carica partita", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 1, 50)
            if cosa == 3:
                if GlobalVar.mouseVisibile:
                    messaggio("Tasto centrale: carica partita", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 1, 50)
                else:
                    messaggio("SHIFT: carica partita", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 1, 50)
            if GlobalVar.mouseVisibile:
                messaggio("Tasto destro: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 1, 50)
            else:
                messaggio("Q: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 1, 50)

            primoFrame = False
            GlobalVar.schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        GlobalVar.clockMenu.tick(GlobalVar.fpsMenu)


def chiediconferma(conferma):
    puntatore = GlobalVar.puntatore
    xp = GlobalVar.gsx // 32 * 17.5
    yp = GlobalVar.gsy // 18 * 10.3
    schermo_temp = GlobalVar.schermo.copy()
    background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalVar.gsx, GlobalVar.gsy))
    dark = pygame.Surface((GlobalVar.gsx, GlobalVar.gsy), flags=pygame.SRCALPHA)
    dark.fill((0, 0, 0, 210))
    background.blit(dark, (0, 0))
    GlobalVar.schermo.blit(background, (0, 0))

    schermo_temp = GlobalVar.schermo.copy()
    backgroundUpdate1 = schermo_temp.subsurface(pygame.Rect(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 9, GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 3))
    backgroundUpdate2 = schermo_temp.subsurface(pygame.Rect(GlobalVar.gsx // 32 * 21, 0, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 2.5))

    tastop = 0
    tastotempfps = 5

    aggiornaInterfacciaPerMouse = False
    voceMarcata = 2
    primoFrame = True
    aggiornaSchermo = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    while True:
        # rallenta per i 30 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0 and tastop != 0:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        suTornaIndietro = False
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVar.mouseVisibile:
            aggiornaInterfacciaPerMouse = True
            pygame.mouse.set_visible(True)
            GlobalVar.mouseVisibile = True
        if GlobalVar.mouseVisibile:
            if GlobalVar.gsx // 32 * 21.5 <= xMouse <= GlobalVar.gsx and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalVar.gsy // 18 * 9 <= yMouse <= GlobalVar.gsy // 18 * 12:
                if GlobalVar.gsx // 32 * 9.5 <= xMouse <= GlobalVar.gsx // 32 * 16:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalVar.gsx // 32 * 9.5
                    yp = GlobalVar.gsy // 18 * 10.3
                elif GlobalVar.gsx // 32 * 16 <= xMouse <= GlobalVar.gsx // 32 * 22.5:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalVar.gsx // 32 * 17.5
                    yp = GlobalVar.gsy // 18 * 10.3
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            else:
                if not GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            tastotempfps = 5
            sinistroMouseVecchio = sinistroMouse
            centraleMouseVecchio = centraleMouse
            destroMouseVecchio = destroMouse
            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
            rotellaConCentralePremuto = False
            if centraleMouseVecchio and centraleMouse:
                rotellaConCentralePremuto = True
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
                GlobalVar.quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato and voceMarcataVecchia == voceMarcata:
                if GlobalVar.mouseVisibile:
                    aggiornaInterfacciaPerMouse = True
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                tastop = event.key
                if event.key == pygame.K_q and not tastoTrovato:
                    tastoTrovato = True
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    return False, False
                if event.key == pygame.K_a and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse and not rotellaConCentralePremuto:
                tastoTrovato = True
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                return False, False
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and not GlobalVar.mouseBloccato):
                tastop = "spazioOsinistroMouse"
                tastoTrovato = True
                if event.type == pygame.MOUSEBUTTONDOWN and suTornaIndietro:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    return False, False
                else:
                    if voceMarcata == 1:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                        if conferma == 1:
                            return True, True
                        elif conferma == 2:
                            pygame.quit()
                            GlobalVar.quit()
                        elif conferma == 3:
                            return False, True
                    elif voceMarcata == 2:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                        return False, False
            elif GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and GlobalVar.mouseBloccato:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
            if (sinistroMouse or centraleMouse or destroMouse) and not rotellaConCentralePremuto and not GlobalVar.mouseVisibile:
                aggiornaInterfacciaPerMouse = True
                pygame.mouse.set_visible(True)
                GlobalVar.mouseVisibile = True

            if tastop != 0:
                aggiornaSchermo = True

            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0
            if event.type == pygame.MOUSEBUTTONUP:
                tastop = 0

        if aggiornaSchermo or primoMovimento or tastop == "spazioOsinistroMouse" or ((tastop == pygame.K_a or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerMouse:
            aggiornaSchermo = False
            aggiornaInterfacciaPerMouse = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_a:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if voceMarcata == 2:
                    voceMarcata -= 1
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    xp = GlobalVar.gsx // 32 * 9.5
            if tastop == pygame.K_d:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if voceMarcata == 1:
                    voceMarcata += 1
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    xp = GlobalVar.gsx // 32 * 17.5
            if primoFrame:
                GlobalVar.schermo.blit(background, (0, 0))
                if conferma == 1:
                    messaggio(u"Tornare al menu principale?", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 5.8, GlobalVar.gsy // 18 * 6.5, 120)
                elif conferma == 2:
                    messaggio("Uscire dal gioco?", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9.9, GlobalVar.gsy // 18 * 6.5, 120)
                elif conferma == 3:
                    messaggio("Iniziare una nuova partita?", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 6.2, GlobalVar.gsy // 18 * 6.5, 120)
            else:
                GlobalVar.schermo.blit(backgroundUpdate1, (GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 9))
                GlobalVar.schermo.blit(backgroundUpdate2, (GlobalVar.gsx // 32 * 21, 0))
            messaggio("Si", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 9.5, 120)
            messaggio("No", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 9.5, 120)
            if GlobalVar.mouseVisibile:
                messaggio("Tasto destro: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 1, 50)
            else:
                messaggio("Q: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 1, 50)
            primoFrame = False
            GlobalVar.schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        GlobalVar.clockMenu.tick(GlobalVar.fpsMenu)


def menuImpostazioni(settaRisoluzione, dimezzaVolumeCanzone):
    puntatore = GlobalVar.puntatore
    xp = GlobalVar.gsx // 32 * 1
    yp = GlobalVar.gsy // 18 * 5.2
    risposta = False
    voceMarcata = 1
    primoFrame = True
    aggiornaSchermo = False
    aggiornaInterfacciaPerMouse = False
    sinistroMousePremuto = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    linguaTemp = GlobalVar.linguaImpostata
    volumeEffettiTemp = GlobalVar.volumeEffetti * 10
    volumeCanzoniTemp = GlobalVar.volumeCanzoni * 10
    gsxTemp = GlobalVar.gsx
    gsyTemp = GlobalVar.gsy
    schermoInteroTemp = GlobalVar.schermoIntero

    tastop = 0
    tastotempfps = 5

    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0 and tastop != 0:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        cursoreSuFrecciaSinistra = False
        cursoreSuFrecciaDestra = False
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        suTornaIndietro = False
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVar.mouseVisibile:
            aggiornaInterfacciaPerMouse = True
            pygame.mouse.set_visible(True)
            GlobalVar.mouseVisibile = True
        if GlobalVar.mouseVisibile:
            if GlobalVar.gsx // 32 * 21.5 <= xMouse <= GlobalVar.gsx and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalVar.gsx // 32 * 8 <= xMouse <= GlobalVar.gsx // 32 * 16 and GlobalVar.gsy // 18 * 13.5 <= yMouse <= GlobalVar.gsy // 18 * 16:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                voceMarcata = 6
                xp = GlobalVar.gsx // 32 * 9
                yp = GlobalVar.gsy // 18 * 14.7
            elif GlobalVar.gsx // 32 * 16 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 14 <= yMouse <= GlobalVar.gsy // 18 * 17:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                voceMarcata = 7
                xp = GlobalVar.gsx // 32 * 17
                yp = GlobalVar.gsy // 18 * 14.7
            elif GlobalVar.gsx // 32 * 15.2 <= xMouse <= GlobalVar.gsx // 32 * 15.7 and GlobalVar.gsy // 18 * 5 <= yMouse <= GlobalVar.gsy // 18 * 6:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalVar.gsx // 32 * 19.2 <= xMouse <= GlobalVar.gsx // 32 * 19.7 and GlobalVar.gsy // 18 * 5 <= yMouse <= GlobalVar.gsy // 18 * 6:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalVar.gsx // 32 * 15.2 <= xMouse <= GlobalVar.gsx // 32 * 15.7 and GlobalVar.gsy // 18 * 6.7 <= yMouse <= GlobalVar.gsy // 18 * 7.7:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalVar.gsx // 32 * 17.1 <= xMouse <= GlobalVar.gsx // 32 * 17.6 and GlobalVar.gsy // 18 * 6.7 <= yMouse <= GlobalVar.gsy // 18 * 7.7:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalVar.gsx // 32 * 15.2 <= xMouse <= GlobalVar.gsx // 32 * 15.7 and GlobalVar.gsy // 18 * 8.4 <= yMouse <= GlobalVar.gsy // 18 * 9.4:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalVar.gsx // 32 * 17.1 <= xMouse <= GlobalVar.gsx // 32 * 17.6 and GlobalVar.gsy // 18 * 8.4 <= yMouse <= GlobalVar.gsy // 18 * 9.4:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalVar.gsx // 32 * 15.2 <= xMouse <= GlobalVar.gsx // 32 * 15.7 and GlobalVar.gsy // 18 * 10.1 <= yMouse <= GlobalVar.gsy // 18 * 11.1:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalVar.gsx // 32 * 20.5 <= xMouse <= GlobalVar.gsx // 32 * 21 and GlobalVar.gsy // 18 * 10.1 <= yMouse <= GlobalVar.gsy // 18 * 11.1:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalVar.gsx // 32 * 15.2 <= xMouse <= GlobalVar.gsx // 32 * 15.7 and GlobalVar.gsy // 18 * 11.7 <= yMouse <= GlobalVar.gsy // 18 * 12.7:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalVar.gsx // 32 * 17.2 <= xMouse <= GlobalVar.gsx // 32 * 17.7 and GlobalVar.gsy // 18 * 11.7 <= yMouse <= GlobalVar.gsy // 18 * 12.7:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            else:
                if not GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(True)
            if GlobalVar.gsx // 32 * 1 <= xMouse <= GlobalVar.gsx // 32 * 31:
                if GlobalVar.gsy // 18 * 4.7 <= yMouse <= GlobalVar.gsy // 18 * 6.3:
                    voceMarcata = 1
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 5.2
                elif GlobalVar.gsy // 18 * 6.3 <= yMouse <= GlobalVar.gsy // 18 * 8:
                    voceMarcata = 2
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 6.9
                elif GlobalVar.gsy // 18 * 8 <= yMouse <= GlobalVar.gsy // 18 * 9.7:
                    voceMarcata = 3
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 8.6
                elif GlobalVar.gsy // 18 * 9.7 <= yMouse <= GlobalVar.gsy // 18 * 11.4:
                    voceMarcata = 4
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 10.3
                elif GlobalVar.gsy // 18 * 11.4 <= yMouse <= GlobalVar.gsy // 18 * 13.1:
                    voceMarcata = 5
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 12
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)

        buttonUp = False
        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            tastotempfps = 5
            sinistroMouseVecchio = sinistroMouse
            centraleMouseVecchio = centraleMouse
            destroMouseVecchio = destroMouse
            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
            rotellaConCentralePremuto = False
            if centraleMouseVecchio and centraleMouse:
                rotellaConCentralePremuto = True
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
                GlobalVar.quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato and voceMarcataVecchia == voceMarcata:
                if GlobalVar.mouseVisibile:
                    aggiornaInterfacciaPerMouse = True
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if event.key == pygame.K_q and not tastoTrovato:
                    tastoTrovato = True
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
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

            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse and not rotellaConCentralePremuto:
                tastoTrovato = True
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                risposta = True
            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and not GlobalVar.mouseBloccato and (cursoreSuFrecciaSinistra or cursoreSuFrecciaDestra):
                tastop = "spazioOsinistroMouse"
                primoMovimento = True
                tastoTrovato = True
                sinistroMousePremuto = True
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and not GlobalVar.mouseBloccato and not (cursoreSuFrecciaSinistra or cursoreSuFrecciaDestra)):
                tastop = "spazioOsinistroMouse"
                primoMovimento = True
                tastoTrovato = True
                if event.type == pygame.MOUSEBUTTONDOWN and suTornaIndietro:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    risposta = True
                else:
                    # quando clicchi spazio puoi modificare l'opzone selezionata
                    if voceMarcata == 6:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                        GlobalVar.linguaImpostata = linguaTemp
                        GlobalVar.volumeEffetti = volumeEffettiTemp / 10 * 1.0
                        GlobalVar.volumeCanzoni = volumeCanzoniTemp / 10 * 1.0
                        GlobalVar.initVolumeSounds()
                        if dimezzaVolumeCanzone:
                            GlobalVar.canaleSoundCanzone.set_volume(GlobalVar.volumeCanzoni / 2)
                            GlobalVar.canaleSoundSottofondoAmbientale.set_volume(GlobalVar.volumeEffetti / 2)
                        if GlobalVar.gsx != gsxTemp or GlobalVar.gsy != gsyTemp or GlobalVar.schermoIntero != schermoInteroTemp:
                            GlobalVar.schermoIntero = schermoInteroTemp
                            GlobalVar.gsx = gsxTemp
                            GlobalVar.gsy = gsyTemp
                            GlobalVar.gpx = GlobalVar.gsx // 32
                            GlobalVar.gpy = GlobalVar.gsy // 18
                            if GlobalVar.schermoIntero:
                                opzioni_schermo = pygame.FULLSCREEN | pygame.HWSURFACE
                                GlobalVar.schermo = pygame.display.set_mode((GlobalVar.gsx, GlobalVar.gsy), opzioni_schermo)
                            else:
                                GlobalVar.schermo = pygame.display.set_mode((GlobalVar.gsx, GlobalVar.gsy))
                            GlobalVar.loadImgs()
                        # salvo in un file la configurazione (ordine => lingua, volEffetti, volCanzoni, schermoIntero, gsx, gsy)
                        scrivi = GlobalVar.loadFile("Impostazioni/Impostazioni.txt", "w")
                        if GlobalVar.linguaImpostata == "italiano":
                            scrivi.write("0_")
                        elif GlobalVar.linguaImpostata == "inglese":
                            scrivi.write("1_")
                        scrivi.write(str(int(GlobalVar.volumeEffetti * 10)) + "_")
                        scrivi.write(str(int(GlobalVar.volumeCanzoni * 10)) + "_")
                        if GlobalVar.schermoIntero:
                            scrivi.write("1_")
                        else:
                            scrivi.write("0_")
                        scrivi.write(str(GlobalVar.gsx) + "_")
                        scrivi.write(str(GlobalVar.gsy) + "_")
                        scrivi.close()
                        puntatore = GlobalVar.puntatore
                        yp = GlobalVar.gsy // 18 * 14.7
                        xp = GlobalVar.gsx // 32 * 9
                        primoFrame = True
                    elif voceMarcata == 7:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                        risposta = True
            elif GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and GlobalVar.mouseBloccato:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
            if (sinistroMouse or centraleMouse or destroMouse) and not rotellaConCentralePremuto and not GlobalVar.mouseVisibile:
                aggiornaInterfacciaPerMouse = True
                pygame.mouse.set_visible(True)
                GlobalVar.mouseVisibile = True

            if tastop != 0:
                aggiornaSchermo = True

            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0
                buttonUp = True
            if event.type == pygame.MOUSEBUTTONUP:
                tastop = 0
                sinistroMousePremuto = False
                buttonUp = True

        if aggiornaSchermo or primoMovimento or buttonUp or ((tastop == "spazioOsinistroMouse" or tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerMouse:
            aggiornaSchermo = False
            aggiornaInterfacciaPerMouse = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                if voceMarcata == 2 or voceMarcata == 3 or voceMarcata == 4 or voceMarcata == 5:
                    voceMarcata -= 1
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = yp - GlobalVar.gsy // 18 * 1.7
                    xp = GlobalVar.gsx // 32 * 1
                elif voceMarcata == 6:
                    voceMarcata -= 1
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = GlobalVar.gsy // 18 * 12
                    xp = GlobalVar.gsx // 32 * 1
                elif voceMarcata == 7:
                    voceMarcata -= 2
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = GlobalVar.gsy // 18 * 12
                    xp = GlobalVar.gsx // 32 * 1
                elif voceMarcata == 1:
                    voceMarcata += 5
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = GlobalVar.gsy // 18 * 14.7
                    xp = GlobalVar.gsx // 32 * 9
            if tastop == pygame.K_a:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if voceMarcata == 1:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    if linguaTemp == "italiano":
                        linguaTemp = "inglese"
                    elif linguaTemp == "inglese":
                        linguaTemp = "italiano"
                elif voceMarcata == 2:
                    if volumeEffettiTemp != 0:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        volumeEffettiTemp -= 1
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                elif voceMarcata == 3:
                    if volumeCanzoniTemp != 0:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        volumeCanzoniTemp -= 1
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                elif voceMarcata == 4:
                    if settaRisoluzione:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        if gsxTemp == 800 and gsyTemp == 450:
                            gsxTemp = GlobalVar.maxGsx
                            gsyTemp = GlobalVar.maxGsy
                        elif gsxTemp == 1024 and gsyTemp == 576:
                            gsxTemp = 800
                            gsyTemp = 450
                        elif gsxTemp == 1280 and gsyTemp == 720:
                            gsxTemp = 1024
                            gsyTemp = 576
                        elif gsxTemp == 1920 and gsyTemp == 1080:
                            gsxTemp = 1280
                            gsyTemp = 720
                        elif gsxTemp == GlobalVar.maxGsx and gsyTemp == GlobalVar.maxGsy:
                            if GlobalVar.maxGsx > 1920 and GlobalVar.maxGsy > 1080:
                                gsxTemp = 1920
                                gsyTemp = 1080
                            elif GlobalVar.maxGsx > 1280 and GlobalVar.maxGsy > 720:
                                gsxTemp = 1280
                                gsyTemp = 720
                            elif GlobalVar.maxGsx > 1024 and GlobalVar.maxGsy > 576:
                                gsxTemp = 1024
                                gsyTemp = 576
                            elif GlobalVar.maxGsx > 800 and GlobalVar.maxGsy > 450:
                                gsxTemp = 800
                                gsyTemp = 450
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                elif voceMarcata == 5:
                    if settaRisoluzione:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        if schermoInteroTemp:
                            schermoInteroTemp = False
                        else:
                            schermoInteroTemp = True
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                elif voceMarcata == 6:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    voceMarcata += 1
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    xp = GlobalVar.gsx // 32 * 17
                elif voceMarcata == 7:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    voceMarcata -= 1
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    xp = GlobalVar.gsx // 32 * 9
            if tastop == pygame.K_s:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                if voceMarcata == 1 or voceMarcata == 2 or voceMarcata == 3 or voceMarcata == 4:
                    voceMarcata += 1
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = yp + GlobalVar.gsy // 18 * 1.7
                elif voceMarcata == 5:
                    voceMarcata += 1
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = GlobalVar.gsy // 18 * 14.7
                    xp = GlobalVar.gsx // 32 * 9
                elif voceMarcata == 6:
                    voceMarcata -= 5
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = GlobalVar.gsy // 18 * 5.2
                    xp = GlobalVar.gsx // 32 * 1
                elif voceMarcata == 7:
                    voceMarcata -= 6
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = GlobalVar.gsy // 18 * 5.2
                    xp = GlobalVar.gsx // 32 * 1
            if tastop == pygame.K_d:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if voceMarcata == 1:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    if linguaTemp == "italiano":
                        linguaTemp = "inglese"
                    elif linguaTemp == "inglese":
                        linguaTemp = "italiano"
                elif voceMarcata == 2:
                    if volumeEffettiTemp != 10:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        volumeEffettiTemp += 1
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                elif voceMarcata == 3:
                    if volumeCanzoniTemp != 10:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        volumeCanzoniTemp += 1
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                elif voceMarcata == 4:
                    if settaRisoluzione:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        if gsxTemp == 800 and gsyTemp == 450:
                            if GlobalVar.maxGsx > 1024 and GlobalVar.maxGsy > 576:
                                gsxTemp = 1024
                                gsyTemp = 576
                            else:
                                gsxTemp = GlobalVar.maxGsx
                                gsyTemp = GlobalVar.maxGsy
                        elif gsxTemp == 1024 and gsyTemp == 576:
                            if GlobalVar.maxGsx > 1280 and GlobalVar.maxGsy > 720:
                                gsxTemp = 1280
                                gsyTemp = 720
                            elif GlobalVar.maxGsx == 1024 and GlobalVar.maxGsy == 576:
                                gsxTemp = 800
                                gsyTemp = 450
                            else:
                                gsxTemp = GlobalVar.maxGsx
                                gsyTemp = GlobalVar.maxGsy
                        elif gsxTemp == 1280 and gsyTemp == 720:
                            if GlobalVar.maxGsx > 1920 and GlobalVar.maxGsy > 1080:
                                gsxTemp = 1920
                                gsyTemp = 1080
                            elif GlobalVar.maxGsx == 1280 and GlobalVar.maxGsy == 720:
                                gsxTemp = 800
                                gsyTemp = 450
                            else:
                                gsxTemp = GlobalVar.maxGsx
                                gsyTemp = GlobalVar.maxGsy
                        elif gsxTemp == 1920 and gsyTemp == 1080:
                            if GlobalVar.maxGsx > 1920 and GlobalVar.maxGsy > 1080:
                                gsxTemp = GlobalVar.maxGsx
                                gsyTemp = GlobalVar.maxGsy
                            else:
                                gsxTemp = 800
                                gsyTemp = 450
                        elif gsxTemp == GlobalVar.maxGsx and gsyTemp == GlobalVar.maxGsy:
                            if GlobalVar.maxGsx > 800 and GlobalVar.maxGsy > 450:
                                gsxTemp = 800
                                gsyTemp = 450
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                elif voceMarcata == 5:
                    if settaRisoluzione:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        if schermoInteroTemp:
                            schermoInteroTemp = False
                        else:
                            schermoInteroTemp = True
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                elif voceMarcata == 6:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    voceMarcata += 1
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    xp = GlobalVar.gsx // 32 * 17
                elif voceMarcata == 7:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    voceMarcata -= 1
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    xp = GlobalVar.gsx // 32 * 9
            if sinistroMousePremuto and cursoreSuFrecciaSinistra:
                if voceMarcata == 1:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    if linguaTemp == "italiano":
                        linguaTemp = "inglese"
                    elif linguaTemp == "inglese":
                        linguaTemp = "italiano"
                elif voceMarcata == 2:
                    if volumeEffettiTemp != 0:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        volumeEffettiTemp -= 1
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                elif voceMarcata == 3:
                    if volumeCanzoniTemp != 0:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        volumeCanzoniTemp -= 1
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                elif voceMarcata == 4:
                    if settaRisoluzione:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        if gsxTemp == 800 and gsyTemp == 450:
                            gsxTemp = GlobalVar.maxGsx
                            gsyTemp = GlobalVar.maxGsy
                        elif gsxTemp == 1024 and gsyTemp == 576:
                            gsxTemp = 800
                            gsyTemp = 450
                        elif gsxTemp == 1280 and gsyTemp == 720:
                            gsxTemp = 1024
                            gsyTemp = 576
                        elif gsxTemp == 1920 and gsyTemp == 1080:
                            gsxTemp = 1280
                            gsyTemp = 720
                        elif gsxTemp == GlobalVar.maxGsx and gsyTemp == GlobalVar.maxGsy:
                            if GlobalVar.maxGsx > 1920 and GlobalVar.maxGsy > 1080:
                                gsxTemp = 1920
                                gsyTemp = 1080
                            elif GlobalVar.maxGsx > 1280 and GlobalVar.maxGsy > 720:
                                gsxTemp = 1280
                                gsyTemp = 720
                            elif GlobalVar.maxGsx > 1024 and GlobalVar.maxGsy > 576:
                                gsxTemp = 1024
                                gsyTemp = 576
                            elif GlobalVar.maxGsx > 800 and GlobalVar.maxGsy > 450:
                                gsxTemp = 800
                                gsyTemp = 450
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                elif voceMarcata == 5:
                    if settaRisoluzione:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        if schermoInteroTemp:
                            schermoInteroTemp = False
                        else:
                            schermoInteroTemp = True
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
            if sinistroMousePremuto and cursoreSuFrecciaDestra:
                if voceMarcata == 1:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    if linguaTemp == "italiano":
                        linguaTemp = "inglese"
                    elif linguaTemp == "inglese":
                        linguaTemp = "italiano"
                elif voceMarcata == 2:
                    if volumeEffettiTemp != 10:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        volumeEffettiTemp += 1
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                elif voceMarcata == 3:
                    if volumeCanzoniTemp != 10:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        volumeCanzoniTemp += 1
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                elif voceMarcata == 4:
                    if settaRisoluzione:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        if gsxTemp == 800 and gsyTemp == 450:
                            if GlobalVar.maxGsx > 1024 and GlobalVar.maxGsy > 576:
                                gsxTemp = 1024
                                gsyTemp = 576
                            else:
                                gsxTemp = GlobalVar.maxGsx
                                gsyTemp = GlobalVar.maxGsy
                        elif gsxTemp == 1024 and gsyTemp == 576:
                            if GlobalVar.maxGsx > 1280 and GlobalVar.maxGsy > 720:
                                gsxTemp = 1280
                                gsyTemp = 720
                            elif GlobalVar.maxGsx == 1024 and GlobalVar.maxGsy == 576:
                                gsxTemp = 800
                                gsyTemp = 450
                            else:
                                gsxTemp = GlobalVar.maxGsx
                                gsyTemp = GlobalVar.maxGsy
                        elif gsxTemp == 1280 and gsyTemp == 720:
                            if GlobalVar.maxGsx > 1920 and GlobalVar.maxGsy > 1080:
                                gsxTemp = 1920
                                gsyTemp = 1080
                            elif GlobalVar.maxGsx == 1280 and GlobalVar.maxGsy == 720:
                                gsxTemp = 800
                                gsyTemp = 450
                            else:
                                gsxTemp = GlobalVar.maxGsx
                                gsyTemp = GlobalVar.maxGsy
                        elif gsxTemp == 1920 and gsyTemp == 1080:
                            if GlobalVar.maxGsx > 1920 and GlobalVar.maxGsy > 1080:
                                gsxTemp = GlobalVar.maxGsx
                                gsyTemp = GlobalVar.maxGsy
                            else:
                                gsxTemp = 800
                                gsyTemp = 450
                        elif gsxTemp == GlobalVar.maxGsx and gsyTemp == GlobalVar.maxGsy:
                            if GlobalVar.maxGsx > 800 and GlobalVar.maxGsy > 450:
                                gsxTemp = 800
                                gsyTemp = 450
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                elif voceMarcata == 5:
                    if settaRisoluzione:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        if schermoInteroTemp:
                            schermoInteroTemp = False
                        else:
                            schermoInteroTemp = True
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)

            if primoFrame:
                GlobalVar.schermo.fill(GlobalVar.grigioscu)
                messaggio("Impostazioni", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 1, 150)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 12.5))
                GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4))
                GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoDestra, (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 4))
                GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoBassoDestra, (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 15.5))
                GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoBassoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 15.5))
            else:
                pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 21, 0, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 2.5))
                pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4.5, GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 11.5))

            messaggio("Lingua", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 5, 70)
            messaggio("Volume effetti", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 6.7, 70)
            messaggio("Volume canzoni", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 8.4, 70)
            messaggio("Conferma", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 14.5, 70)
            messaggio("Indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 70)

            if linguaTemp == "italiano":
                messaggio("Italiano", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 5.1, 60)
            if linguaTemp == "inglese":
                messaggio("English", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 5.1, 60)
            if voceMarcata == 1:
                if tastop == pygame.K_a or (sinistroMousePremuto and cursoreSuFrecciaSinistra):
                    GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniSinistraBloccato, (GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 5))
                else:
                    GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniSinistra, (GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 5))
                if tastop == pygame.K_d or (sinistroMousePremuto and cursoreSuFrecciaDestra):
                    GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniDestraBloccato, (GlobalVar.gsx // 32 * 19.2, GlobalVar.gsy // 18 * 5))
                else:
                    GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniDestra, (GlobalVar.gsx // 32 * 19.2, GlobalVar.gsy // 18 * 5))
            messaggio(str(int(volumeEffettiTemp)), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 6.8, 60)
            if voceMarcata == 2:
                if volumeEffettiTemp != 0:
                    if tastop == pygame.K_a or (sinistroMousePremuto and cursoreSuFrecciaSinistra):
                        GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniSinistraBloccato, (GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 6.7))
                    else:
                        GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniSinistra, (GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 6.7))
                else:
                    GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniSinistraBloccato, (GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 6.7))
                if volumeEffettiTemp != 10:
                    if tastop == pygame.K_d or (sinistroMousePremuto and cursoreSuFrecciaDestra):
                        GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniDestraBloccato, (GlobalVar.gsx // 32 * 17.1, GlobalVar.gsy // 18 * 6.7))
                    else:
                        GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniDestra, (GlobalVar.gsx // 32 * 17.1, GlobalVar.gsy // 18 * 6.7))
                else:
                    GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniDestraBloccato, (GlobalVar.gsx // 32 * 17.1, GlobalVar.gsy // 18 * 6.7))
            messaggio(str(int(volumeCanzoniTemp)), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 8.5, 60)
            if voceMarcata == 3:
                if volumeCanzoniTemp != 0:
                    if tastop == pygame.K_a or (sinistroMousePremuto and cursoreSuFrecciaSinistra):
                        GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniSinistraBloccato, (GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 8.4))
                    else:
                        GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniSinistra, (GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 8.4))
                else:
                    GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniSinistraBloccato, (GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 8.4))
                if volumeCanzoniTemp != 10:
                    if tastop == pygame.K_d or (sinistroMousePremuto and cursoreSuFrecciaDestra):
                        GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniDestraBloccato, (GlobalVar.gsx // 32 * 17.1, GlobalVar.gsy // 18 * 8.4))
                    else:
                        GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniDestra, (GlobalVar.gsx // 32 * 17.1, GlobalVar.gsy // 18 * 8.4))
                else:
                    GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniDestraBloccato, (GlobalVar.gsx // 32 * 17.1, GlobalVar.gsy // 18 * 8.4))
            if settaRisoluzione:
                messaggio("Risoluzione", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 10.1, 70)
                messaggio("Schermo intero", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 11.7, 70)
                messaggio(str(gsxTemp) + "x" + str(gsyTemp), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 10.2, 60)
                if voceMarcata == 4:
                    if tastop == pygame.K_a or (sinistroMousePremuto and cursoreSuFrecciaSinistra):
                        GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniSinistraBloccato, (GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 10.1))
                    else:
                        GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniSinistra, (GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 10.1))
                    if tastop == pygame.K_d or (sinistroMousePremuto and cursoreSuFrecciaDestra):
                        GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniDestraBloccato, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 10.1))
                    else:
                        GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniDestra, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 10.1))
                if schermoInteroTemp:
                    messaggio("Si", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 11.8, 60)
                else:
                    messaggio("No", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 11.8, 60)
                if voceMarcata == 5:
                    if tastop == pygame.K_a or (sinistroMousePremuto and cursoreSuFrecciaSinistra):
                        GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniSinistraBloccato, (GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 11.7))
                    else:
                        GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniSinistra, (GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 11.7))
                    if tastop == pygame.K_d or (sinistroMousePremuto and cursoreSuFrecciaDestra):
                        GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniDestraBloccato, (GlobalVar.gsx // 32 * 17.2, GlobalVar.gsy // 18 * 11.7))
                    else:
                        GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniDestra, (GlobalVar.gsx // 32 * 17.2, GlobalVar.gsy // 18 * 11.7))
            else:
                messaggio("Risoluzione", GlobalVar.grigioscu, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 10.1, 70)
                messaggio(str(gsxTemp) + "x" + str(gsyTemp), GlobalVar.grigioscu, GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 10.2, 60)
                if voceMarcata == 4:
                    GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniSinistraBloccato, (GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 10.1))
                    GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniDestraBloccato, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 10.1))
                messaggio("Schermo intero", GlobalVar.grigioscu, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 11.7, 70)
                if schermoInteroTemp:
                    messaggio("Si", GlobalVar.grigioscu, GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 11.8, 60)
                else:
                    messaggio("No", GlobalVar.grigioscu, GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 11.8, 60)
                if voceMarcata == 5:
                    GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniSinistraBloccato, (GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 11.7))
                    GlobalVar.schermo.blit(GlobalVar.puntatoreImpostazioniDestraBloccato, (GlobalVar.gsx // 32 * 17.2, GlobalVar.gsy // 18 * 11.7))

            if GlobalVar.mouseVisibile:
                messaggio("Tasto destro: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 1, 50)
            else:
                messaggio("Q: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 1, 50)
            GlobalVar.schermo.blit(puntatore, (xp, yp))
            if voceMarcata != 6 and voceMarcata != 7:
                pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscu, ((xp + (int(GlobalVar.gpx // 1.5))), yp + (int(GlobalVar.gpy * 1))), (xp + (int(GlobalVar.gpx * 29)), yp + (int(GlobalVar.gpy * 1))), 2)
            primoFrame = False

            pygame.display.update()

        GlobalVar.clockMenu.tick(GlobalVar.fpsMenu)


def menuMappa(avanzamentoStoria):
    puntatore = GlobalVar.puntatore
    puntatorevecchio = GlobalVar.puntatorevecchio
    imgOmbreggiaturaContorniMappaMenu = GlobalVar.imgOmbreggiaturaContorniMappaMenu
    xp = GlobalVar.gsx // 32 * 1
    yp = GlobalVar.gsy // 18 * 4.5
    risposta = False
    voceMarcata = 1
    voceMarcataSottoMenu = False
    primoFrame = True
    aggiornaSchermo = False

    aggiornaInterfacciaPerMouse = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    tastop = 0
    tastotempfps = 5

    # carico la mappa a seconda dell'avanzamento
    imgMappaOrig = GlobalVar.imgMappa1
    postiSbloccati = {"Casa": False, "Città": False, "Avamposto di Rod": False, "Castello": False, "Palazzo di Rod": False, "Vulcano": False, "Laboratorio": False, "Foresta cadetta": False, "Selva arida": False, "Labirinto": False, "Passo montano": False, "Caverna": False, "Tunnel di Rod": False, "Tunnel subacqueo": False}
    if avanzamentoStoria >= 0:
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["mappaCasa"]:
            postiSbloccati["Casa"] = True
            imgMappaOrig = GlobalVar.imgMappa1
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["mappaForestaCadetta"]:
            postiSbloccati["Foresta cadetta"] = True
            imgMappaOrig = GlobalVar.imgMappa2
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["mappaCittà"]:
            postiSbloccati["Città"] = True
            imgMappaOrig = GlobalVar.imgMappa3
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["mappaSelvaArida"]:
            postiSbloccati["Selva arida"] = True
            imgMappaOrig = GlobalVar.imgMappa4
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["mappaAvampostoDiRod"]:
            postiSbloccati["Avamposto di Rod"] = True
            imgMappaOrig = GlobalVar.imgMappa5
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["mappaLabirinto"]:
            postiSbloccati["Labirinto"] = True
            imgMappaOrig = GlobalVar.imgMappa6
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["mappaCastello"]:
            postiSbloccati["Castello"] = True
            imgMappaOrig = GlobalVar.imgMappa7
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["mappaPassoMontano"]:
            postiSbloccati["Passo montano"] = True
            imgMappaOrig = GlobalVar.imgMappa8
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["mappaPalazzoDiRod"]:
            postiSbloccati["Palazzo di Rod"] = True
            imgMappaOrig = GlobalVar.imgMappa9
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["mappaCaverna"]:
            postiSbloccati["Caverna"] = True
            imgMappaOrig = GlobalVar.imgMappa10
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["mappaVulcano"]:
            postiSbloccati["Vulcano"] = True
            imgMappaOrig = GlobalVar.imgMappa10
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["mappaTunnelDiRod1"]:
            postiSbloccati["Tunnel di Rod"] = True# <- il tunnel di Rod è diviso in due parti
            imgMappaOrig = GlobalVar.imgMappa11
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["mappaTunnelDiRod2"]:
            postiSbloccati["Tunnel di Rod"] = True
            imgMappaOrig = GlobalVar.imgMappa12
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["mappaTunnelSubacqueo"]:
            postiSbloccati["Tunnel subacqueo"] = True
            imgMappaOrig = GlobalVar.imgMappa13
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["mappaLaboratorio"]:
            postiSbloccati["Laboratorio"] = True
            imgMappaOrig = GlobalVar.imgMappa14
    imgMappaA = pygame.transform.smoothscale(imgMappaOrig, (GlobalVar.gpx * 22, GlobalVar.gpy * 15))
    imgMappaB = pygame.transform.smoothscale(imgMappaOrig, (GlobalVar.gpx * 50, GlobalVar.gpy * 35))

    GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoAperturaMappa)
    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0 and tastop != 0:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        suTornaIndietro = False
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVar.mouseVisibile:
            aggiornaInterfacciaPerMouse = True
            pygame.mouse.set_visible(True)
            GlobalVar.mouseVisibile = True
        if GlobalVar.mouseVisibile:
            if GlobalVar.gsx // 32 * 21.5 <= xMouse <= GlobalVar.gsx and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                suTornaIndietro = True
            elif not voceMarcataSottoMenu and GlobalVar.gsx // 32 * 1 <= xMouse <= GlobalVar.gsx // 32 * 10:
                if GlobalVar.gsy // 18 * 4.3 <= yMouse <= GlobalVar.gsy // 18 * 5.1:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 4.5
                elif GlobalVar.gsy // 18 * 5.1 <= yMouse <= GlobalVar.gsy // 18 * 5.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 5.3
                elif GlobalVar.gsy // 18 * 5.9 <= yMouse <= GlobalVar.gsy // 18 * 6.7:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 6.1
                elif GlobalVar.gsy // 18 * 6.7 <= yMouse <= GlobalVar.gsy // 18 * 7.5:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 6.9
                elif GlobalVar.gsy // 18 * 7.5 <= yMouse <= GlobalVar.gsy // 18 * 8.3:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 7.7
                elif GlobalVar.gsy // 18 * 8.3 <= yMouse <= GlobalVar.gsy // 18 * 9.1:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 8.5
                elif GlobalVar.gsy // 18 * 9.1 <= yMouse <= GlobalVar.gsy // 18 * 9.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 9.3
                elif GlobalVar.gsy // 18 * 10.5 <= yMouse <= GlobalVar.gsy // 18 * 11.3:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 10.7
                elif GlobalVar.gsy // 18 * 11.3 <= yMouse <= GlobalVar.gsy // 18 * 12.1:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 11.5
                elif GlobalVar.gsy // 18 * 12.1 <= yMouse <= GlobalVar.gsy // 18 * 12.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 12.3
                elif GlobalVar.gsy // 18 * 12.9 <= yMouse <= GlobalVar.gsy // 18 * 13.7:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 13.1
                elif GlobalVar.gsy // 18 * 13.7 <= yMouse <= GlobalVar.gsy // 18 * 14.5:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 13.9
                elif GlobalVar.gsy // 18 * 14.5 <= yMouse <= GlobalVar.gsy // 18 * 15.3:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 14.7
                elif GlobalVar.gsy // 18 * 15.3 <= yMouse <= GlobalVar.gsy // 18 * 16.1:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 15.5
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            else:
                if not GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            tastotempfps = 5
            sinistroMouseVecchio = sinistroMouse
            centraleMouseVecchio = centraleMouse
            destroMouseVecchio = destroMouse
            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
            rotellaConCentralePremuto = False
            if centraleMouseVecchio and centraleMouse:
                rotellaConCentralePremuto = True
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
                GlobalVar.quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato and voceMarcataVecchia == voceMarcata:
                tastop = event.key
                if (event.key == pygame.K_q or event.key == pygame.K_a) and not tastoTrovato:
                    tastoTrovato = True
                    if voceMarcataSottoMenu:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                        voceMarcataSottoMenu = False
                        primoFrame = True
                    elif event.key == pygame.K_q:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                        risposta = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True

            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse and not rotellaConCentralePremuto and not tastoTrovato:
                tastop = "destroMouse"
                if voceMarcataSottoMenu:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    voceMarcataSottoMenu = False
                    primoFrame = True
                else:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    risposta = True
            if (event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_d)) or (GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and not GlobalVar.mouseBloccato) and not tastoTrovato:
                tastop = "spazioOsinistroMouse"
                primoFrame = True
                tastoTrovato = True
                if event.type == pygame.MOUSEBUTTONDOWN and suTornaIndietro:
                    if voceMarcataSottoMenu:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                        voceMarcataSottoMenu = False
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                        risposta = True
                elif not voceMarcataSottoMenu or (GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and not GlobalVar.mouseBloccato):
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
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                        tastoTrovato = True
                        voceMarcataSottoMenu = True
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
            elif GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and GlobalVar.mouseBloccato:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
            if (sinistroMouse or centraleMouse or destroMouse) and not rotellaConCentralePremuto and not GlobalVar.mouseVisibile:
                aggiornaInterfacciaPerMouse = True
                pygame.mouse.set_visible(True)
                GlobalVar.mouseVisibile = True

            if tastop != 0:
                aggiornaSchermo = True

            if event.type == pygame.KEYUP and (tastop == event.key or tastop == "spazioOsinistroMouse" or tastop == "destroMouse"):
                tastop = 0
            if event.type == pygame.MOUSEBUTTONUP:
                tastop = 0

        if aggiornaSchermo or primoMovimento or tastop == "spazioOsinistroMouse" or tastop == "destroMouse" or tastop == pygame.K_q or tastop == pygame.K_SPACE or tastop == pygame.K_a or tastop == pygame.K_d or ((tastop == pygame.K_w or tastop == pygame.K_s) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerMouse:
            aggiornaSchermo = False
            aggiornaInterfacciaPerMouse = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_s):
                tastotempfps = 2
            if tastop == pygame.K_w:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if not voceMarcataSottoMenu:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    if voceMarcata == 1:
                        voceMarcata = 14
                        yp = GlobalVar.gsy // 18 * 15.5
                    elif voceMarcata == 8:
                        voceMarcata -= 1
                        yp = yp - GlobalVar.gpy * 1.4
                    else:
                        voceMarcata -= 1
                        yp = yp - GlobalVar.gpy * 0.8
            if tastop == pygame.K_s:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if not voceMarcataSottoMenu:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    if voceMarcata == 14:
                        voceMarcata = 1
                        yp = GlobalVar.gsy // 18 * 4.5
                    elif voceMarcata == 7:
                        voceMarcata += 1
                        yp = yp + GlobalVar.gpy * 1.4
                    else:
                        voceMarcata += 1
                        yp = yp + GlobalVar.gpy * 0.8

            if not voceMarcataSottoMenu:
                if primoFrame:
                    GlobalVar.schermo.fill(GlobalVar.grigioscu)
                    imgMappa = imgMappaA
                    GlobalVar.schermo.blit(imgMappa, (GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 2.5))
                    # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 12.5))
                    GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4))
                    GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoDestra, (GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 4))
                    GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoBassoDestra, (GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 15.5))
                    GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoBassoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 15.5))
                else:
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 21, 0, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 2))
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4.5, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 11.6))
            else:
                if primoFrame:
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigioscuPiuScu, (GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 2, GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 16))
                    imgMappa = imgMappaB
                    if voceMarcata == 1:
                        GlobalVar.schermo.blit(imgMappa, (GlobalVar.gsx // 32 * (-16), GlobalVar.gsy // 18 * 1))
                    if voceMarcata == 2:
                        GlobalVar.schermo.blit(imgMappa, (GlobalVar.gsx // 32 * (-4.5), GlobalVar.gsy // 18 * (-1.5)))
                    if voceMarcata == 3:
                        GlobalVar.schermo.blit(imgMappa, (GlobalVar.gsx // 32 * (3), GlobalVar.gsy // 18 * (-9.5)))
                    if voceMarcata == 4:
                        GlobalVar.schermo.blit(imgMappa, (GlobalVar.gsx // 32 * (8.5), GlobalVar.gsy // 18 * (-17)))
                    if voceMarcata == 5:
                        GlobalVar.schermo.blit(imgMappa, (GlobalVar.gsx // 32 * (7.5), GlobalVar.gsy // 18 * (-0.5)))
                    if voceMarcata == 6:
                        GlobalVar.schermo.blit(imgMappa, (GlobalVar.gsx // 32 * (16), GlobalVar.gsy // 18 * (0)))
                    if voceMarcata == 7:
                        GlobalVar.schermo.blit(imgMappa, (GlobalVar.gsx // 32 * (-8), GlobalVar.gsy // 18 * (-17)))
                    if voceMarcata == 8:
                        GlobalVar.schermo.blit(imgMappa, (GlobalVar.gsx // 32 * (-13.5), GlobalVar.gsy // 18 * (-5)))
                    if voceMarcata == 9:
                        GlobalVar.schermo.blit(imgMappa, (GlobalVar.gsx // 32 * (0.5), GlobalVar.gsy // 18 * (-8)))
                    if voceMarcata == 10:
                        GlobalVar.schermo.blit(imgMappa, (GlobalVar.gsx // 32 * (4), GlobalVar.gsy // 18 * (-13)))
                    if voceMarcata == 11:
                        GlobalVar.schermo.blit(imgMappa, (GlobalVar.gsx // 32 * (3.5), GlobalVar.gsy // 18 * (-1.5)))
                    if voceMarcata == 12:
                        GlobalVar.schermo.blit(imgMappa, (GlobalVar.gsx // 32 * (11.5), GlobalVar.gsy // 18 * (0)))
                    if voceMarcata == 13:
                        GlobalVar.schermo.blit(imgMappa, (GlobalVar.gsx // 32 * (7), GlobalVar.gsy // 18 * (-6)))
                    if voceMarcata == 14:
                        GlobalVar.schermo.blit(imgMappa, (GlobalVar.gsx // 32 * (-1.5), GlobalVar.gsy // 18 * (-18.5)))
                    GlobalVar.schermo.blit(imgOmbreggiaturaContorniMappaMenu, (0, 0))
                    # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 12.5))
                    GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4))
                    GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoDestra, (GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 4))
                    GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoBassoDestra, (GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 15.5))
                    GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoBassoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 15.5))
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 12.5))
                    GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoDestra, (GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 4))
                    GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoBassoDestra, (GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 15.5))
                    GlobalVar.schermo.blit(puntatorevecchio, (xp, yp))
                    larghezzaTestoDescrizioni = GlobalVar.gpx * 9
                    spazioTraLeRigheTestoDescrizione = GlobalVar.gpy * 7 // 10
                    grandezzaScritteDescrizioni = 40
                    if voceMarcata == 1:
                        messaggio("Casa", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 5, 70)
                        messaggio(u"È l'abitazione in cui ho vissuto con la mia famiglia fin'ora. È stata costruita da un mio vecchio antenato e, da allora, è sempre stata abitata dalle varie generazioni della mia famiglia. Secondo il babbo Sam sarà il prossimo proprietario e l'idea non lo entusiasma affatto: durande diverse discussioni gli ha detto di non voler fare questo lavoro per tutta la vita come lui. Dice che è monotono, faticoso e anche instabile a causa delle enormi imposte dello stato e della spietata concorrenza.", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 2:
                        messaggio(u"Città", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 5, 70)
                        messaggio(u"Da quando ne ho sentito parlare per la prima volta, ho sempre avuto il desiderio di viverci. Da quello che so, lì a tutti è concesso scegliere quale mansione svolgere nella vita. Questo è diventato possibile grazie ai nuovi strumenti di produzione che hanno reso possibile un sistema in cui poche persone riescono a produrre abbastanza anche per tutte le altre. La parte di popolazione \"impoduttiva\" può quindi dedicarsi ad altre attività come musica, teatro, studio, sport e chissà cos'altro.", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 3:
                        messaggio("Avamposto di Rod", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 5, 70)
                        messaggio(u"Una piccola baracca che Rod esalta in maniera esagerata definendola \"avamposto\". Quella non è la sua abitazione ma, a suo dire, un luogo strategicamente fondamentale per la sopravvivenza dell'intero ecosistema cittadino. Rod non ispira molta fiducia ma tutti i suoi pensieri e ragionamenti mi sono sempre sembranti almeno sensati e coerenti... mi domando cosa nasconda quella baracca...", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 4:
                        messaggio("Castello", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 5, 70)
                        messaggio(u"La più grande struttura che abbia mai visto fino ad ora. È un castello composto da un centinaio di stanze abitato dall'amico del bibliotecario e dai suoi numerosi servitori. Il vasto terreno su cui è stato costruito comprende anche l'intero labirinto che è stato appositamente elaborato per tenere lontani i visitatori indesiderati. Il silenzio e il comportamento dei servi creano un'atmosfera molto cupa...", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 5:
                        messaggio("Palazzo di Rod", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 5, 70)
                        messaggio(u"La villa in cui dimora Rod. Risulta essere quasi sempre vuota e silenziosa dato che lui è costantemente fuori per lavoro o ricerche (mi domando ancora che cosa stia ricercando...). Il posto ricorda vagamente il castello di Norm ma in miniatura e con un passaggio montano al posto del labirinto per scoraggiare l'avvicinamento di viaggiatori sconosciuti.", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 6:
                        messaggio("Vulcano", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 5, 70)
                        messaggio(u"Un vulcano sommerso nelle montagne a ovest della città. È simile ad una montagna ma più grande e con un cratere sulla cima dal quale, a detta di Rod, fuoriesce del vapore incandescente. Chissà cosa c'è lì dentro...", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 7:
                        messaggio("Laboratorio", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 5, 70)
                        messaggio(u"Il laboratorio in cui Norm svolge le sue ricerche. È molto piccolo ma al suo interno è presente tutto ciò che serve, ossia un calcolatore di eventi, che si estende anche sotto il terreno, e diversi altri calcolatori che credo servano per gestire i sistemi di alimentazione e raffreddamento.", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 8:
                        messaggio("Foresta cadetta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 5, 70)
                        messaggio(u"La foresta che mi ha sempre separata dalla città... non mi è mai stato concesso attraversarla perchè entrambi i miei genitori la ritenevano troppo pericolosa per me. Il nome deriva dal fatto che viene utilizzata come terreno di prova per selezionare, tra i giovani appartenenti alla nobiltà, i futuri ufficiali dell'esercito.", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 9:
                        messaggio("Selva arida", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 5, 70)
                        messaggio(u"Denominata in questo modo perchè un tempo fitta e intricata ed ora composta soltanto da secchi abusti e funghi. Le ragioni di questo suo decadimento non sono note agli abitanti locali ma, diversi libri della biblioteca in città, sostenevano che ciò fosse dovuto ad un cambiamento climatico avvenuto circa 50 anni fa... strano... <br> Rod è solito attraversarla per tornare al suo avamposto.", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 10:
                        messaggio("Labirinto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 5, 70)
                        messaggio(u"Un enorme terreno estremamente complicato da superare a causa delle innumerevoli strade percorribili al suo interno prive di punti di riferimento. Rod mi ha fornito una mappa che mostra nel dettaglio la sua struttura sconsigliandomi di procedere: è molto probabile non riuscire ad uscirne se non si ha un buon senso dell'orientamento.", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 11:
                        messaggio("Passo montano", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 5, 70)
                        messaggio(u"Un passaggio tra le alture a ovest della città. In città nessuno sembrava sapere di questo varco apparte Rod che lo utilizza per raggiungere il proprio palazzo da più di vent'anni.", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 12:
                        messaggio("Caverna", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 5, 70)
                        messaggio(u"Una caverna in mezzo alle montagne che conduce ad un vulcano. All'interno vivono degli animali simili a Colco ma aggressivi. Rod è solito avventurarsi in quel posto per recuperare alimentazioni. Non mi spiego perché abbia deciso di viverci così vicino... forse ne è geloso e ne vuole controllare gli accessi?", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 13:
                        messaggio("Tunnel di Rod", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 5, 70)
                        messaggio(u"È un passaggio sicuro e veloce tra il palazzo di Rod e il suo avamposto. Rod lo utilizzava per trasportare direttamente le alimentazioni dalla caverna al castello di Norm. Adesso capisco l'importanza \"strategica\" di questi luoghi.", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 14:
                        messaggio("Tunnel subacqueo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 5, 70)
                        messaggio(u"Un passaggio segreto nei sotterranei del castello di Norm che porta al suo laboratorio principale sul fondo del lago. Nonostante le pareti del tunnel siano fatte di un materiale trasparente simile al vetro, non si riesce ad osservare chiaramente il fondale del bacino a causa delle sostanze con cui questo è stato contaminato circa 50 anni fa.", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 21, 0, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 2))


            if primoFrame:
                messaggio("Mappa", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 1, 150)
                grandezzaScritteNormali = 45
                if postiSbloccati["Casa"]:
                    messaggio("Casa", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 4.5, grandezzaScritteNormali)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 4.5, grandezzaScritteNormali)
                if postiSbloccati["Città"]:
                    messaggio(u"Città", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 5.3, grandezzaScritteNormali)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 5.3, grandezzaScritteNormali)
                if postiSbloccati["Avamposto di Rod"]:
                    messaggio("Avamposto di Rod", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 6.1, grandezzaScritteNormali)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 6.1, grandezzaScritteNormali)
                if postiSbloccati["Castello"]:
                    messaggio("Castello", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 6.9, grandezzaScritteNormali)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 6.9, grandezzaScritteNormali)
                if postiSbloccati["Palazzo di Rod"]:
                    messaggio("Palazzo di Rod", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7.7, grandezzaScritteNormali)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7.7, grandezzaScritteNormali)
                if postiSbloccati["Vulcano"]:
                    messaggio("Vulcano", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 8.5, grandezzaScritteNormali)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 8.5, grandezzaScritteNormali)
                if postiSbloccati["Laboratorio"]:
                    messaggio("Laboratorio", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 9.3, grandezzaScritteNormali)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 9.3, grandezzaScritteNormali)
                if postiSbloccati["Foresta cadetta"]:
                    messaggio("Foresta cadetta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 10.7, grandezzaScritteNormali)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 10.7, grandezzaScritteNormali)
                if postiSbloccati["Selva arida"]:
                    messaggio("Selva arida", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 11.5, grandezzaScritteNormali)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 11.5, grandezzaScritteNormali)
                if postiSbloccati["Labirinto"]:
                    messaggio("Labirinto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 12.3, grandezzaScritteNormali)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 12.3, grandezzaScritteNormali)
                if postiSbloccati["Passo montano"]:
                    messaggio("Passo montano", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13.1, grandezzaScritteNormali)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13.1, grandezzaScritteNormali)
                if postiSbloccati["Caverna"]:
                    messaggio("Caverna", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13.9, grandezzaScritteNormali)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13.9, grandezzaScritteNormali)
                if postiSbloccati["Tunnel di Rod"]:
                    messaggio("Tunnel di Rod", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 14.7, grandezzaScritteNormali)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 14.7, grandezzaScritteNormali)
                if postiSbloccati["Tunnel subacqueo"]:
                    messaggio("Tunnel subacqueo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 15.5, grandezzaScritteNormali)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 15.5, grandezzaScritteNormali)

            if GlobalVar.mouseVisibile:
                messaggio("Tasto destro: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 1, 50)
            else:
                messaggio("Q: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 1, 50)
            if not voceMarcataSottoMenu:
                GlobalVar.schermo.blit(puntatore, (xp, yp))
            primoFrame = False

            pygame.display.update()

        GlobalVar.clockMenu.tick(GlobalVar.fpsMenu)


def menuDiario(dati):
    puntatore = GlobalVar.puntatore
    puntatorevecchio = GlobalVar.puntatorevecchio
    xp = GlobalVar.gsx // 32 * 1
    yp = GlobalVar.gsy // 18 * 5.6
    xpv = xp
    ypv = yp
    risposta = False
    voceMarcata = 1
    voceMarcataSottoMenu = 0
    primoFrame = True
    aggiornaSchermo = False

    tastop = 0
    tastotempfps = 5

    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        elif tastotempfps == 0 and tastop != 0:
            tastotempfps = 2

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
            tastotempfps = 5
            if event.type == pygame.QUIT:
                tastoTrovato = True
                pygame.quit()
                GlobalVar.quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato:
                tastop = event.key
                if (event.key == pygame.K_q or event.key == pygame.K_a) and not tastoTrovato:
                    tastoTrovato = True
                    if voceMarcataSottoMenu != 0:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                        voceMarcataSottoMenu = 0
                        xp = xpv
                        yp = ypv
                    elif event.key == pygame.K_q:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                        risposta = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if (event.key == pygame.K_SPACE or event.key == pygame.K_d) and not tastoTrovato:
                    if voceMarcataSottoMenu == 0:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                        tastoTrovato = True
                        voceMarcataSottoMenu = 1
                        xpv = xp
                        ypv = yp
                        if voceMarcata == 4 or voceMarcata == 5:
                            xp = GlobalVar.gsx // 32 * 10
                            yp = GlobalVar.gsy // 18 * 8

            if tastop != 0:
                aggiornaSchermo = True

            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0

        if aggiornaSchermo or primoMovimento or tastop == pygame.K_q or tastop == pygame.K_SPACE or tastop == pygame.K_a or tastop == pygame.K_d or ((tastop == pygame.K_w or tastop == pygame.K_s) and tastotempfps == 0) or primoFrame:
            aggiornaSchermo = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_s):
                tastotempfps = 2
            if tastop == pygame.K_w:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                if voceMarcataSottoMenu == 0:
                    if voceMarcata == 1:
                        voceMarcata += 4
                        yp = GlobalVar.gsy // 18 * 14.6
                    elif voceMarcata == 4:
                        voceMarcata -= 1
                        yp = GlobalVar.gsy // 18 * 8.6
                    else:
                        voceMarcata -= 1
                        yp = yp - GlobalVar.gpy * 1.5
                else:
                    if voceMarcata == 4 or voceMarcata == 5:
                        if voceMarcataSottoMenu == 1:
                            voceMarcataSottoMenu += 2
                            yp = GlobalVar.gsy // 18 * 12
                        else:
                            voceMarcataSottoMenu -= 1
                            yp = yp - GlobalVar.gpy * 2
            if tastop == pygame.K_s:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                if voceMarcataSottoMenu == 0:
                    if voceMarcata == 5:
                        voceMarcata -= 4
                        yp = GlobalVar.gsy // 18 * 5.6
                    elif voceMarcata == 3:
                        voceMarcata += 1
                        yp = GlobalVar.gsy // 18 * 13.1
                    else:
                        voceMarcata += 1
                        yp = yp + GlobalVar.gpy * 1.5
                else:
                    if voceMarcata == 4 or voceMarcata == 5:
                        if voceMarcataSottoMenu == 3:
                            voceMarcataSottoMenu -= 2
                            yp = GlobalVar.gsy // 18 * 8
                        else:
                            voceMarcataSottoMenu += 1
                            yp = yp + GlobalVar.gpy * 2

            if primoFrame:
                GlobalVar.schermo.fill(GlobalVar.grigioscu)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 12.5))
                GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4))
                GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoDestra, (GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 4))
                GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoBassoDestra, (GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 15.5))
                GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoBassoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 15.5))

                messaggio("Diario", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 1, 150)
                messaggio("Oggetti speciali", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 5.5, 55)
                messaggio("Persone incontrate", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7, 55)
                messaggio("Nemici incontrati", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 8.5, 55)
                messaggio("Guida mouse", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13, 55)
                messaggio("Guida tatiera", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 14.5, 55)
            else:
                pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 21, 0, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 2.5))
                pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 5.6, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 10))
                pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 12.5))
                pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 3, GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 15))

            if voceMarcataSottoMenu != 0:
                pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 12.5))
                GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoDestra, (GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 4))
                GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoBassoDestra, (GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 15.5))
                GlobalVar.schermo.blit(puntatorevecchio, (xpv, ypv))
                if voceMarcata == 4 or voceMarcata == 5:
                    messaggio("Mod. movimento", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 7.9, 55)
                    messaggio("Mod. interazione", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 9.9, 55)
                    messaggio("Menu", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 11.9, 55)
                    if voceMarcata == 4:
                        if voceMarcataSottoMenu == 1:
                            GlobalVar.schermo.blit(GlobalVar.tutorialMouse, (GlobalVar.gsx // 32 * 20.2, GlobalVar.gsy // 18 * 4.8))
                            messaggio("Movimento (su casella libera) /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 5.6, 35)
                            messaggio("Interagisci (su casella interagibile) /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 6.1, 35)
                            messaggio("Attiva o disattiva Colco (su telecolco) /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 6.6, 35)
                            messaggio("Menu (su stato personaggio) /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 7.1, 35)
                            messaggio(u"Modalità interazione (su stato nemico)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 7.6, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 8.6), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 8.6), 2)
                            messaggio(u"Modalità interazione /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 9.9, 35)
                            messaggio("Rimuovi selezione (su stato nemico)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 10.4, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 12), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 12), 2)
                            messaggio("Menu", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 13.5, 35)
                        if voceMarcataSottoMenu == 2:
                            GlobalVar.schermo.blit(GlobalVar.tutorialMouse, (GlobalVar.gsx // 32 * 20.2, GlobalVar.gsy // 18 * 4.8))
                            messaggio("Inquadra o attacca (su casella nemica) /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 5.6, 35)
                            messaggio("Interagisci (su casella interagibile) /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 6.1, 35)
                            messaggio("Attiva o disattiva Colco (su telecolco) /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 6.6, 35)
                            messaggio("Menu (su stato personaggio) /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 7.1, 35)
                            messaggio(u"Modalità movimento (su stato nemico)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 7.6, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 8.6), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 8.6), 2)
                            messaggio(u"Modalità movimento", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 10.1, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 12), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 12), 2)
                            messaggio("Menu", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 13.5, 35)
                        if voceMarcataSottoMenu == 3:
                            GlobalVar.schermo.blit(GlobalVar.tutorialMouse, (GlobalVar.gsx // 32 * 20.2, GlobalVar.gsy // 18 * 4.8))
                            messaggio("Seleziona", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 6.6, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 8.6), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 8.6), 2)
                            messaggio("Indietro / Esci", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 10.1, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 12), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 12), 2)
                            messaggio("Cambia operazione (se consentito)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 13.5, 35)
                    if voceMarcata == 5:
                        if voceMarcataSottoMenu == 1:
                            GlobalVar.schermo.blit(GlobalVar.tutorialTastieraInGioco, (GlobalVar.gsx // 32 * 20.2, GlobalVar.gsy // 18 * 4.8))
                            messaggio("Menu", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 5.5, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 6.1), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 6.1), 2)
                            messaggio("Cambia bersaglio inquadrato", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 6.7, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 7.5), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 7.5), 2)
                            messaggio("Deseleziona bersaglio", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 8.1, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 8.9), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 8.9), 2)
                            messaggio(u"Modalità interazione", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 9.5, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 10.3), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 10.3), 2)
                            messaggio("Movimento", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 11.5, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 12.8), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 12.8), 2)
                            messaggio("Attiva o disattiva Colco", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 13.4, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 14.2), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 14.2), 2)
                            messaggio("Interagisci", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 14.8, 35)
                        if voceMarcataSottoMenu == 2:
                            GlobalVar.schermo.blit(GlobalVar.tutorialTastieraInGioco, (GlobalVar.gsx // 32 * 20.2, GlobalVar.gsy // 18 * 4.8))
                            messaggio("Menu", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 5.5, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 6.1), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 6.1), 2)
                            messaggio("Punta sul prossimo bersaglio", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 6.7, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 7.5), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 7.5), 2)
                            messaggio(u"Modalità movimento", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 8.1, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 8.9), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 8.9), 2)
                            messaggio("Inquadra bersaglio puntato", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 9.5, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 10.3), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 10.3), 2)
                            messaggio("Sposta puntatore", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 11.5, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 12.8), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 12.8), 2)
                            messaggio("Attiva o disattiva Colco", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 13.4, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 14.2), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 14.2), 2)
                            messaggio("Attacca / Interagisci", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 14.8, 35)
                        if voceMarcataSottoMenu == 3:
                            GlobalVar.schermo.blit(GlobalVar.tutorialTastieraInMenu, (GlobalVar.gsx // 32 * 20.2, GlobalVar.gsy // 18 * 4.8))
                            messaggio("Esci (dove specificato)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 6.9, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 7.5), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 7.5), 2)
                            messaggio("Indietro / Esci", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 8.1, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 8.9), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 8.9), 2)
                            messaggio("Sposta puntatore", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 10.1, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 11.4), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 11.4), 2)
                            messaggio("Cambia operazione (se consentito)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 12, 35)
                            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 12.8), (GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 12.8), 2)
                            messaggio("Seleziona", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24.2, GlobalVar.gsy // 18 * 13.4, 35)

            messaggio("Q: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 1, 50)
            GlobalVar.schermo.blit(puntatore, (xp, yp))
            primoFrame = False

            pygame.display.update()

        GlobalVar.clockMenu.tick(GlobalVar.fpsMenu)
