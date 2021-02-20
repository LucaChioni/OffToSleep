# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import GlobalImgVar
import GlobalSndVar
import GlobalGameVar
import GestioneInput
import GenericFunc
import CaricaSalvaPartita


def ricaricaSalvataggi(lunghezzadati, lunghezzadatiPorte, lunghezzadatiCofanetti, numSalvataggio=-1):
    if numSalvataggio == -1:
        contasalva = 1
        GlobalGameVar.vetDatiSalvataggi = []
        while contasalva <= 3:
            dati, datiGameover, errore = CaricaSalvaPartita.caricaPartita(contasalva, lunghezzadati, lunghezzadatiPorte, lunghezzadatiCofanetti, True)
            vetTempDati = []
            vetTempDati.append(dati[0])
            vetTempDati.append(datiGameover[0])
            vetTempDati.append(errore)
            GlobalGameVar.vetDatiSalvataggi.append(vetTempDati)
            contasalva += 1
    else:
        dati, datiGameover, errore = CaricaSalvaPartita.caricaPartita(numSalvataggio, lunghezzadati, lunghezzadatiPorte, lunghezzadatiCofanetti, True)
        vetTempDati = []
        vetTempDati.append(dati[0])
        vetTempDati.append(datiGameover[0])
        vetTempDati.append(errore)
        GlobalGameVar.vetDatiSalvataggi[numSalvataggio - 1] = vetTempDati


def mostraErroreCaricamentoSalvataggio(errore):
    if errore == 1:
        print ("Slot vuoto")
        aggiornaSchermata = True
        bottoneDown = False
        aggiornaInterfacciaPerCambioInput = True
        indietro = False
        while not indietro:
            xMouse, yMouse = pygame.mouse.get_pos()
            if GlobalHWVar.mouseVisibile:
                if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)

            # gestione degli input
            bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
            if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCerchio":
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                aggiornaSchermata = True
                indietro = True
                bottoneDown = False
            if bottoneDown:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                bottoneDown = False
            if aggiornaSchermata or aggiornaInterfacciaPerCambioInput:
                aggiornaSchermata = False
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robograf2, (GlobalHWVar.gpx * 7, int(-GlobalHWVar.gpy * 4.45)))
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.nero, (GlobalHWVar.gpx * 10, int(GlobalHWVar.gpy * 13.5)), (GlobalHWVar.gpx * 22, int(GlobalHWVar.gpy * 13.5)), 2)
                if GlobalHWVar.mouseVisibile:
                    GenericFunc.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    GenericFunc.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    GenericFunc.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)
                GenericFunc.messaggio("Slot di memoria vuoto...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 8.5, GlobalHWVar.gsy // 18 * 14, 100)
                GlobalHWVar.aggiornaSchermo()

            pygame.event.pump()
            GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    if errore == 2:
        print ("Dati corrotti")
        aggiornaSchermata = True
        bottoneDown = False
        aggiornaInterfacciaPerCambioInput = True
        indietro = False
        while not indietro:
            xMouse, yMouse = pygame.mouse.get_pos()
            if GlobalHWVar.mouseVisibile:
                if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)

            # gestione degli input
            bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
            if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCerchio":
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                aggiornaSchermata = True
                indietro = True
                bottoneDown = False
            if bottoneDown:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                bottoneDown = False
            if aggiornaSchermata or aggiornaInterfacciaPerCambioInput:
                aggiornaSchermata = False
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robograf4, (GlobalHWVar.gpx * 7, -GlobalHWVar.gpy * 4.45))
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.nero, (GlobalHWVar.gpx * 10, int(GlobalHWVar.gpy * 13.5)), (GlobalHWVar.gpx * 22, int(GlobalHWVar.gpy * 13.5)), 2)
                if GlobalHWVar.mouseVisibile:
                    GenericFunc.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    GenericFunc.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    GenericFunc.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)
                GenericFunc.messaggio("Slot di memoria danneggiato...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 6.5, GlobalHWVar.gsy // 18 * 14, 100)
                GlobalHWVar.aggiornaSchermo()

            pygame.event.pump()
            GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def scegli_sal(possibileSalvare, lunghezzadati, lunghezzadatiPorte, lunghezzadatiCofanetti, porteAttuali, cofanettiAttuali, vitaescaAttuali, vettoreDenaroAttuali, datiAttuali, listaNemiciTotaliAttuali, stanzeGiaVisitateAttuali, listaPersonaggiTotaliAttuali, listaAvanzamentoDialoghi, oggettiRimastiAHansAttuali, ultimoObbiettivoColco, obbiettivoCasualeColco):
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    xp = GlobalHWVar.gsx // 32 * 2
    yp = GlobalHWVar.gsy // 18 * 8.2
    vxp = xp
    vyp = yp
    if possibileSalvare:
        cosa = 3
    else:
        cosa = 1
    aggiornaTutto = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    risposta = False
    conferma = False
    primaconf = False
    salMarcato = 1
    voceMarcata = 2
    aggiornaSchermo = False
    n = -1

    persoLucy1 = GlobalImgVar.persoLucy1
    persoLucy2 = GlobalImgVar.persoLucy2
    persobLucy = GlobalImgVar.persobLucy
    persoFraMaggiore = GlobalImgVar.persoFraMaggiore
    persobFraMaggiore = GlobalImgVar.persobFraMaggiore

    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        salMarcatoVecchio = salMarcato
        xMouse, yMouse = pygame.mouse.get_pos()
        suTornaIndietro = False
        suCambiaOperazione = False
        if GlobalHWVar.mouseVisibile:
            if not conferma:
                if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    suTornaIndietro = True
                elif 0 <= xMouse <= GlobalHWVar.gsx // 32 * 10 and GlobalHWVar.gsy // 18 * 16.2 <= yMouse <= GlobalHWVar.gsy:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    suCambiaOperazione = True
                elif GlobalHWVar.gsy // 18 * 4.5 <= yMouse <= GlobalHWVar.gsy // 18 * 12.5:
                    if GlobalHWVar.gsx // 32 * 2 <= xMouse <= GlobalHWVar.gsx // 32 * 11.3:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        salMarcato = 1
                        xp = GlobalHWVar.gsx // 32 * 2
                        yp = GlobalHWVar.gsy // 18 * 8.2
                    elif GlobalHWVar.gsx // 32 * 11.3 <= xMouse <= GlobalHWVar.gsx // 32 * 20.6:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        salMarcato = 2
                        xp = GlobalHWVar.gsx // 32 * 11.3
                        yp = GlobalHWVar.gsy // 18 * 8.2
                    elif GlobalHWVar.gsx // 32 * 20.6 <= xMouse <= GlobalHWVar.gsx // 32 * 29.9:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        salMarcato = 3
                        xp = GlobalHWVar.gsx // 32 * 20.6
                        yp = GlobalHWVar.gsy // 18 * 8.2
                    else:
                        if not GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(True)
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            else:
                if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    suTornaIndietro = True
                elif 0 <= xMouse <= GlobalHWVar.gsx // 32 * 10 and GlobalHWVar.gsy // 18 * 16.2 <= yMouse <= GlobalHWVar.gsy:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    suCambiaOperazione = True
                elif GlobalHWVar.gsy // 18 * 14 <= yMouse <= GlobalHWVar.gsy // 18 * 16:
                    if (GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3) <= xMouse <= (GlobalHWVar.gsx // 32 * 6.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3):
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 1
                        xp = (GlobalHWVar.gsx // 32 * 3.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3)
                        yp = GlobalHWVar.gsy // 18 * 14.7
                    elif (GlobalHWVar.gsx // 32 * 6.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3) <= xMouse <= (GlobalHWVar.gsx // 32 * 11.3) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3):
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 2
                        xp = (GlobalHWVar.gsx // 32 * 6.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3)
                        yp = GlobalHWVar.gsy // 18 * 14.7
                    else:
                        if not GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(True)
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            if (voceMarcataVecchia != voceMarcata or salMarcatoVecchio != salMarcato) and not primoFrame:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)

        if not conferma:
            vxp = xp
            vyp = yp

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            if conferma:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                xp = vxp
                yp = vyp
                conferma = False
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                n = -1
                return n, cosa
            bottoneDown = False
        if bottoneDown == pygame.K_LSHIFT or bottoneDown == pygame.K_RSHIFT or bottoneDown == "mouseCentrale" or bottoneDown == "padTriangolo":
            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
            aggiornaTutto = True
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
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                if conferma:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    xp = vxp
                    yp = vyp
                    conferma = False
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    n = -1
                    return n, cosa
            elif bottoneDown == "mouseSinistro" and suCambiaOperazione:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                aggiornaTutto = True
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
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        if cosa == 1:
                            vetTemp = GlobalGameVar.vetDatiSalvataggi[n - 1]
                            erroreDatiVettore = vetTemp[2]
                            if erroreDatiVettore == 0:
                                return n, cosa
                            else:
                                mostraErroreCaricamentoSalvataggio(erroreDatiVettore)
                                conferma = False
                                xp = vxp
                                yp = vyp
                            primoFrame = True
                        elif cosa == 3:
                            GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.verdeScuroPiuScuro, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 12.5, GlobalHWVar.gsx // 32 * 9.3, GlobalHWVar.gsy // 18 * 3.5))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.verdeScuroPiuScuro, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 12.5) - 1), ((GlobalHWVar.gsx // 32 * 11.3) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 12.5) - 1), 2)
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 15))
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, ((GlobalHWVar.gsx // 32 * 10.3) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 15))
                            GenericFunc.messaggio("Salvando...", GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 6.7) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 13.7, 80, centrale=True)
                            GlobalHWVar.aggiornaSchermo()
                            datiAttualiTotali = [datiAttuali, porteAttuali, cofanettiAttuali, listaNemiciTotaliAttuali, vitaescaAttuali, vettoreDenaroAttuali, stanzeGiaVisitateAttuali, listaPersonaggiTotaliAttuali, listaAvanzamentoDialoghi, oggettiRimastiAHansAttuali, ultimoObbiettivoColco, obbiettivoCasualeColco]
                            datiGameoverTotali = [GlobalGameVar.vetDatiSalvataggioGameOver[0], GlobalGameVar.vetDatiSalvataggioGameOver[1], GlobalGameVar.vetDatiSalvataggioGameOver[2], GlobalGameVar.vetDatiSalvataggioGameOver[3], GlobalGameVar.vetDatiSalvataggioGameOver[4], GlobalGameVar.vetDatiSalvataggioGameOver[5], GlobalGameVar.vetDatiSalvataggioGameOver[6], GlobalGameVar.vetDatiSalvataggioGameOver[7], GlobalGameVar.vetDatiSalvataggioGameOver[8], GlobalGameVar.vetDatiSalvataggioGameOver[9], GlobalGameVar.vetDatiSalvataggioGameOver[10], GlobalGameVar.vetDatiSalvataggioGameOver[11]]
                            CaricaSalvaPartita.salvataggio(n, datiAttualiTotali, datiGameoverTotali)
                            # ricarico i salvataggi
                            ricaricaSalvataggi(lunghezzadati, lunghezzadatiPorte, lunghezzadatiCofanetti, numSalvataggio=n)
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            xp = vxp
                            yp = vyp
                            conferma = False
                            primoFrame = True
                        elif cosa == 2:
                            GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.rossoScuroPiuScuro, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 12.5, GlobalHWVar.gsx // 32 * 9.3, GlobalHWVar.gsy // 18 * 3.5))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.rossoScuroPiuScuro, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 12.5) - 1), ((GlobalHWVar.gsx // 32 * 11.3) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 12.5) - 1), 2)
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 15))
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, ((GlobalHWVar.gsx // 32 * 10.3) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 15))
                            GenericFunc.messaggio("Cancellando...", GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 6.7) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 13.7, 80, centrale=True)
                            GlobalHWVar.aggiornaSchermo()
                            leggi = GlobalHWVar.loadFile("Salvataggi/Salvataggio%i.txt" % n, "w")
                            leggi.close()
                            leggi = GlobalHWVar.loadFile("Salvataggi/Salvataggio%i-backup.txt" % n, "w")
                            leggi.close()
                            # ricarico i salvataggi
                            ricaricaSalvataggi(lunghezzadati, lunghezzadatiPorte, lunghezzadatiCofanetti, numSalvataggio=n)
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            xp = vxp
                            yp = vyp
                            conferma = False
                            primoFrame = True
                    if voceMarcata == 2:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                        xp = vxp
                        yp = vyp
                        conferma = False
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    conferma = True
                    primaconf = True
                    n = salMarcato
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == pygame.K_d or bottoneDown == pygame.K_a or bottoneDown == "padDestra" or bottoneDown == "padSinistra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or salMarcatoVecchio != salMarcato or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if conferma:
                    if voceMarcata == 2:
                        voceMarcata -= 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = (GlobalHWVar.gsx // 32 * 3.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3)
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        bottoneDown = False
                else:
                    if salMarcato == 3:
                        salMarcato -= 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 11.3
                    elif salMarcato == 2:
                        salMarcato -= 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 2
                    elif salMarcato == 1:
                        salMarcato += 2
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 20.6
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                if conferma:
                    if voceMarcata == 1:
                        voceMarcata += 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = (GlobalHWVar.gsx // 32 * 6.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3)
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        bottoneDown = False
                else:
                    if salMarcato == 1:
                        salMarcato += 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 11.3
                    elif salMarcato == 2:
                        salMarcato += 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 20.6
                    elif salMarcato == 3:
                        salMarcato -= 2
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 2
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame or aggiornaTutto:
                aggiornaInterfacciaPerCambioInput = True
                aggiornaTutto = False
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                if cosa == 2:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.rossoScuro, (GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 27.9, GlobalHWVar.gsy // 18 * 8))
                elif cosa == 1:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.bluScuro, (GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 27.9, GlobalHWVar.gsy // 18 * 8))
                else:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.verdeScuro, (GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 27.9, GlobalHWVar.gsy // 18 * 8))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 28.9, GlobalHWVar.gsy // 18 * 4.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 28.9, GlobalHWVar.gsy // 18 * 11.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.s1, (GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 7))
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gsx // 32 * 11.3) - 1, GlobalHWVar.gsy // 18 * 5), ((GlobalHWVar.gsx // 32 * 11.3) - 1, GlobalHWVar.gsy // 18 * 12), 2)
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.s2, (GlobalHWVar.gsx // 32 * 12.3, GlobalHWVar.gsy // 18 * 7))
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gsx // 32 * 20.6) - 1, GlobalHWVar.gsy // 18 * 5), ((GlobalHWVar.gsx // 32 * 20.6) - 1, GlobalHWVar.gsy // 18 * 12), 2)
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.s3, (GlobalHWVar.gsx // 32 * 21.6, GlobalHWVar.gsy // 18 * 7))
                if cosa == 1:
                    GenericFunc.messaggio("Carica partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                if cosa == 2:
                    GenericFunc.messaggio("Cancella partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                if cosa == 3:
                    GenericFunc.messaggio("Salva partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)

                contasalva = 1
                while contasalva <= len(GlobalGameVar.vetDatiSalvataggi):
                    vetTemp = GlobalGameVar.vetDatiSalvataggi[contasalva - 1]
                    dati = vetTemp[0]
                    errore = vetTemp[2]
                    if errore == 1:
                        GenericFunc.messaggio("Slot vuoto", GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 6.5) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 8.2, 60)
                    else:
                        if not errore:
                            if dati[0] < GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
                                persalva = persoLucy1
                                persSalvaBraccia = persobLucy
                            elif GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= dati[0] < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                                persalva = persoFraMaggiore
                                persSalvaBraccia = persobFraMaggiore
                            elif dati[0] < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
                                persalva = persoLucy1
                                persSalvaBraccia = persobLucy
                            else:
                                persalva = persoLucy2
                                persSalvaBraccia = persobLucy

                            spasalva = GlobalImgVar.vetImgSpadePixellate[dati[6]]
                            arcsalva = GlobalImgVar.vetImgArchiPixellate[dati[128]]
                            armsalva = GlobalImgVar.vetImgArmaturePixellate[dati[8]]
                            scusalva = GlobalImgVar.vetImgScudiPixellate[dati[7]]
                            guasalva = GlobalImgVar.vetImgGuantiPixellate[dati[129]]
                            colsalva = GlobalImgVar.vetImgCollanePixellate[dati[130]]
                            GenericFunc.messaggio("Livello: " + str(dati[4]), GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 8.3) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 11, 60, centrale=True)
                            GlobalHWVar.disegnaImmagineSuSchermo(arcsalva, ((GlobalHWVar.gpx * 5.8) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.5))
                            GlobalHWVar.disegnaImmagineSuSchermo(persalva, ((GlobalHWVar.gpx * 5.8) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.5))
                            GlobalHWVar.disegnaImmagineSuSchermo(persSalvaBraccia, ((GlobalHWVar.gpx * 5.8) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.5))
                            GlobalHWVar.disegnaImmagineSuSchermo(armsalva, ((GlobalHWVar.gpx * 5.8) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.5))
                            GlobalHWVar.disegnaImmagineSuSchermo(colsalva, ((GlobalHWVar.gpx * 5.8) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.5))
                            GlobalHWVar.disegnaImmagineSuSchermo(spasalva, ((GlobalHWVar.gpx * 5.8) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.5))
                            GlobalHWVar.disegnaImmagineSuSchermo(guasalva, ((GlobalHWVar.gpx * 5.8) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.5))
                            GlobalHWVar.disegnaImmagineSuSchermo(scusalva, ((GlobalHWVar.gpx * 5.8) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.5))
                        else:
                            GenericFunc.messaggio("Slot corrotto", GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 6.2) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 8.2, 60)
                    contasalva += 1
            else:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.5, GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 3.5))
                if cosa == 2:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.rossoScuro, (GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.2, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.rossoScuro, (GlobalHWVar.gsx // 32 * 11.3, GlobalHWVar.gsy // 18 * 8.2, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.rossoScuro, (GlobalHWVar.gsx // 32 * 20.6, GlobalHWVar.gsy // 18 * 8.2, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
                elif cosa == 1:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.bluScuro, (GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.2, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.bluScuro, (GlobalHWVar.gsx // 32 * 11.3, GlobalHWVar.gsy // 18 * 8.2, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.bluScuro, (GlobalHWVar.gsx // 32 * 20.6, GlobalHWVar.gsy // 18 * 8.2, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
                else:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.verdeScuro, (GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.2, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.verdeScuro, (GlobalHWVar.gsx // 32 * 11.3, GlobalHWVar.gsy // 18 * 8.2, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.verdeScuro, (GlobalHWVar.gsx // 32 * 20.6, GlobalHWVar.gsy // 18 * 8.2, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gsx // 32 * 11.3) - 1, GlobalHWVar.gsy // 18 * 5.5), ((GlobalHWVar.gsx // 32 * 11.3) - 1, GlobalHWVar.gsy // 18 * 11.5), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gsx // 32 * 20.6) - 1, GlobalHWVar.gsy // 18 * 5.5), ((GlobalHWVar.gsx // 32 * 20.6) - 1, GlobalHWVar.gsy // 18 * 11.5), 2)
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (0, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2))
                if cosa == 1:
                    if GlobalHWVar.mouseVisibile:
                        GenericFunc.messaggio("Tasto centrale: cancella partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 16.8, 50)
                    elif GlobalHWVar.usandoIlController:
                        GenericFunc.messaggio("Triangolo: cancella partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 16.8, 50)
                    else:
                        GenericFunc.messaggio("SHIFT: cancella partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 16.8, 50)
                if cosa == 2:
                    if possibileSalvare:
                        if GlobalHWVar.mouseVisibile:
                            GenericFunc.messaggio("Tasto centrale: salva partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 16.8, 50)
                        elif GlobalHWVar.usandoIlController:
                            GenericFunc.messaggio("Triangolo: salva partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 16.8, 50)
                        else:
                            GenericFunc.messaggio("SHIFT: salva partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 16.8, 50)
                    else:
                        if GlobalHWVar.mouseVisibile:
                            GenericFunc.messaggio("Tasto centrale: carica partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 16.8, 50)
                        elif GlobalHWVar.usandoIlController:
                            GenericFunc.messaggio("Triangolo: carica partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 16.8, 50)
                        else:
                            GenericFunc.messaggio("SHIFT: carica partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 16.8, 50)
                if cosa == 3:
                    if GlobalHWVar.mouseVisibile:
                        GenericFunc.messaggio("Tasto centrale: carica partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 16.8, 50)
                    elif GlobalHWVar.usandoIlController:
                        GenericFunc.messaggio("Triangolo: carica partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 16.8, 50)
                    else:
                        GenericFunc.messaggio("SHIFT: carica partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 16.8, 50)
                if GlobalHWVar.mouseVisibile:
                    GenericFunc.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    GenericFunc.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    GenericFunc.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            if conferma:
                if primaconf:
                    vxp = xp
                    vyp = yp
                    xp = (GlobalHWVar.gsx // 32 * 6.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3)
                    yp = GlobalHWVar.gsy // 18 * 14.7
                    voceMarcata = 2
                    primaconf = False
                if cosa == 2:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.rossoScuroPiuScuro, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 12.5, GlobalHWVar.gsx // 32 * 9.3, GlobalHWVar.gsy // 18 * 3.5))
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.rossoScuroPiuScuro, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 12.5) - 1), ((GlobalHWVar.gsx // 32 * 11.3) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 12.5) - 1), 2)
                elif cosa == 1:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.bluScuroPiuScuro, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 12.5, GlobalHWVar.gsx // 32 * 9.3, GlobalHWVar.gsy // 18 * 3.5))
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.bluScuroPiuScuro, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 12.5) - 1), ((GlobalHWVar.gsx // 32 * 11.3) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 12.5) - 1), 2)
                else:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.verdeScuroPiuScuro, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 12.5, GlobalHWVar.gsx // 32 * 9.3, GlobalHWVar.gsy // 18 * 3.5))
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.verdeScuroPiuScuro, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 12.5) - 1), ((GlobalHWVar.gsx // 32 * 11.3) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 12.5) - 1), 2)
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 15))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, ((GlobalHWVar.gsx // 32 * 10.3) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 15))
                GenericFunc.messaggio("Confermi?", GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 4.5) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 13, 70)
                GenericFunc.messaggio(u"Sì", GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 4.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 14.5, 70)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gsx // 32 * 6.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3) - 1, GlobalHWVar.gsy // 18 * 14.3), ((GlobalHWVar.gsx // 32 * 6.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3) - 1, GlobalHWVar.gsy // 18 * 15.7), 2)
                GenericFunc.messaggio("No", GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 7.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 14.5, 70)
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (vxp, vyp))

            primoFrame = False
            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            GlobalHWVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def chiediconferma(conferma):
    puntatore = GlobalImgVar.puntatore
    xp = GlobalHWVar.gsx // 32 * 17.5
    yp = GlobalHWVar.gsy // 18 * 10.3
    schermo_temp = GlobalHWVar.schermo.copy().convert()
    background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalHWVar.gsx, GlobalHWVar.gsy)).convert()
    dark = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
    dark.fill((0, 0, 0, 210))
    background.blit(dark, (0, 0))
    GlobalHWVar.disegnaImmagineSuSchermo(background, (0, 0))

    schermo_temp = GlobalHWVar.schermo.copy().convert()
    backgroundUpdate1 = schermo_temp.subsurface(pygame.Rect(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 3)).convert()
    backgroundUpdate2 = schermo_temp.subsurface(pygame.Rect(GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2.5)).convert()

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    voceMarcata = 2
    aggiornaSchermo = False

    while True:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        suTornaIndietro = False
        if GlobalHWVar.mouseVisibile:
            if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalHWVar.gsy // 18 * 9 <= yMouse <= GlobalHWVar.gsy // 18 * 12:
                if GlobalHWVar.gsx // 32 * 9.5 <= xMouse <= GlobalHWVar.gsx // 32 * 16:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalHWVar.gsx // 32 * 9.5
                    yp = GlobalHWVar.gsy // 18 * 10.3
                elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 22.5:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalHWVar.gsx // 32 * 17.5
                    yp = GlobalHWVar.gsy // 18 * 10.3
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            else:
                if not GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            return False, False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                return False, False
            else:
                if voceMarcata == 1:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    if conferma == 1:
                        return True, True
                    elif conferma == 2:
                        pygame.quit()
                        GlobalHWVar.quit()
                    elif conferma == 3:
                        return False, True
                elif voceMarcata == 2:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    return False, False
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == pygame.K_d or bottoneDown == pygame.K_a or bottoneDown == "padDestra" or bottoneDown == "padSinistra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 2:
                    voceMarcata -= 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = GlobalHWVar.gsx // 32 * 9.5
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1:
                    voceMarcata += 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = GlobalHWVar.gsx // 32 * 17.5
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2
            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaImmagineSuSchermo(background, (0, 0))
                if conferma == 1:
                    GenericFunc.messaggio(u"Tornare al menu principale?", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6.5, 120, centrale=True)
                elif conferma == 2:
                    GenericFunc.messaggio("Uscire dal gioco?", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6.5, 120, centrale=True)
                elif conferma == 3:
                    GenericFunc.messaggio("Iniziare una nuova partita?", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6.5, 120, centrale=True)
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(backgroundUpdate1, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaImmagineSuSchermo(backgroundUpdate2, (GlobalHWVar.gsx // 32 * 21, 0))
                if GlobalHWVar.mouseVisibile:
                    GenericFunc.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    GenericFunc.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    GenericFunc.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)
            GenericFunc.messaggio(u"Sì", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9.5, 120)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 16), int(GlobalHWVar.gpy * 9.3)), (int(GlobalHWVar.gpx * 16), int(GlobalHWVar.gpy * 11.6)), 2)
            GenericFunc.messaggio("No", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 9.5, 120)
            primoFrame = False
            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            GlobalHWVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def settaController():
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 5.1
    risposta = False
    voceMarcata = 1
    aggiornaSchermo = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8
    countdownAggiornamentoModulo = -1

    listaIdPadConfigModificata = []
    tastiPremutiPadConfig = []
    tastoDaConfigurare = 0
    ordineConfigTasti = ["croce", "cerchio", "quadrato", "triangolo", "l1", "r1", "start", "croceDir"]
    configurazioneTastiFatta = []

    precedentementeInizializzato = True
    numPadSelezionato = 0
    if len(GlobalHWVar.configPadConnessi) > 0:
        controllerDaConfigurare = False
        idController = GlobalHWVar.configPadConnessi[numPadSelezionato][0]
        nomeController = GlobalHWVar.configPadConnessi[numPadSelezionato][1]
        padInizialmeteConfigurato = False
        for pad in GlobalHWVar.listaPadConnessiConfigurati:
            if idController == pad.get_id():
                controllerDaConfigurare = pad
                padInizialmeteConfigurato = True
                break
        if not controllerDaConfigurare:
            for pad in GlobalHWVar.listaPadConnessiSconosciuti:
                if idController == pad.get_id():
                    controllerDaConfigurare = pad
                    padInizialmeteConfigurato = False
                    break
    else:
        controllerDaConfigurare = False
        idController = -1
        nomeController = "Nessun controller rilevato"
        padInizialmeteConfigurato = False

    configTemp = []
    impoControllerErrato, datiImpostazioniController = GlobalHWVar.caricaImpostazioniController()
    for confPad in datiImpostazioniController:
        impoPad = confPad.split("_")
        impoPad.pop(len(impoPad) - 1)
        if len(impoPad) > 0:
            configTemp.append(impoPad)

    configurando = False
    testando = False
    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        cursoreSuFrecciaSinistra = False
        cursoreSuFrecciaDestra = False
        suTornaIndietro = False
        xMouse, yMouse = pygame.mouse.get_pos()
        if GlobalHWVar.mouseVisibile:
            if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalHWVar.gsx // 32 * 4 <= xMouse <= GlobalHWVar.gsx // 32 * 8.5 and GlobalHWVar.gsy // 18 * 14.2 <= yMouse <= GlobalHWVar.gsy // 18 * 16.2 and not (configurando or testando):
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                voceMarcata = 6
                xp = GlobalHWVar.gsx // 32 * 4.4
                yp = GlobalHWVar.gsy // 18 * 14.9
            elif GlobalHWVar.gsx // 32 * 8.5 <= xMouse <= GlobalHWVar.gsx // 32 * 13 and GlobalHWVar.gsy // 18 * 14.2 <= yMouse <= GlobalHWVar.gsy // 18 * 16.2 and not (configurando or testando):
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                voceMarcata = 7
                xp = GlobalHWVar.gsx // 32 * 8.5
                yp = GlobalHWVar.gsy // 18 * 14.9
            elif GlobalHWVar.gsx // 32 * 1.8 <= xMouse <= GlobalHWVar.gsx // 32 * 2.7 and GlobalHWVar.gsy // 18 * 7.5 <= yMouse <= GlobalHWVar.gsy // 18 * 8.7 and not (configurando or testando):
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalHWVar.gsx // 32 * 14.3 <= xMouse <= GlobalHWVar.gsx // 32 * 15.2 and GlobalHWVar.gsy // 18 * 7.5 <= yMouse <= GlobalHWVar.gsy // 18 * 8.7 and not (configurando or testando):
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 4.7 <= yMouse <= GlobalHWVar.gsy // 18 * 6.2 and not (configurando or testando):
                voceMarcata = 1
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                xp = GlobalHWVar.gsx // 32 * 1
                yp = GlobalHWVar.gsy // 18 * 5.1
            elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 9.2 <= yMouse <= GlobalHWVar.gsy // 18 * 10.7 and not (configurando or testando):
                voceMarcata = 3
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                xp = GlobalHWVar.gsx // 32 * 1
                yp = GlobalHWVar.gsy // 18 * 9.6
            elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 10.7 <= yMouse <= GlobalHWVar.gsy // 18 * 12.2 and not (configurando or testando):
                voceMarcata = 4
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                xp = GlobalHWVar.gsx // 32 * 1
                yp = GlobalHWVar.gsy // 18 * 11.1
            elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 12.2 <= yMouse <= GlobalHWVar.gsy // 18 * 13.7 and not (configurando or testando):
                voceMarcata = 5
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                xp = GlobalHWVar.gsx // 32 * 1
                yp = GlobalHWVar.gsy // 18 * 12.6
            elif not GlobalHWVar.mouseBloccato:
                GlobalHWVar.configuraCursore(True)
            if GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 6.2 <= yMouse < GlobalHWVar.gsy // 18 * 9.2 and not (configurando or testando):
                voceMarcata = 2
                xp = GlobalHWVar.gsx // 32 * 1
                yp = GlobalHWVar.gsy // 18 * 6.6
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        padPassatoPerTestEConf = False
        tastiPremutiPadConfigVecchi = tastiPremutiPadConfig[:]
        tastiPremutiPadConfig = []
        if configurando or testando:
            padPassatoPerTestEConf = controllerDaConfigurare
            # trovo i tasti premuti dal pad che sto configurando
            buttons = controllerDaConfigurare.get_numbuttons()
            for idTasto in range(buttons):
                if controllerDaConfigurare.get_button(idTasto):
                    tastiPremutiPadConfig.append(idTasto)
            hats = controllerDaConfigurare.get_numhats()
            for idCroceDirezionale in range(hats):
                hat = controllerDaConfigurare.get_hat(idCroceDirezionale)
                direzioneX, direzioneY = hat
                if direzioneX != 0 or direzioneY != 0:
                    tastiPremutiPadConfig.append("croceDir:" + str(idCroceDirezionale))
            if configurando and len(tastiPremutiPadConfig) == 1:
                if not ((ordineConfigTasti[tastoDaConfigurare].startswith("croceDir") and not (type(tastiPremutiPadConfig[0]) is str and tastiPremutiPadConfig[0].startswith("croceDir"))) or (not ordineConfigTasti[tastoDaConfigurare].startswith("croceDir") and type(tastiPremutiPadConfig[0]) is str and tastiPremutiPadConfig[0].startswith("croceDir"))):
                    tastoGiaUsato = False
                    for tasto in configurazioneTastiFatta:
                        if tasto == tastiPremutiPadConfig[0]:
                            tastoGiaUsato = True
                    if not tastoGiaUsato:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        configurazioneTastiFatta.append(tastiPremutiPadConfig[0])
                        tastoDaConfigurare += 1
                        aggiornaSchermo = True
        if configurando and len(configurazioneTastiFatta) == 9:
            configurazioneSalvata = False
            i = 0
            while i < len(configTemp):
                if configTemp[i][0] == nomeController:
                    configTemp[i][1] = configurazioneTastiFatta[1]
                    configTemp[i][2] = configurazioneTastiFatta[2]
                    configTemp[i][3] = configurazioneTastiFatta[3]
                    configTemp[i][4] = configurazioneTastiFatta[4]
                    configTemp[i][5] = configurazioneTastiFatta[5]
                    configTemp[i][6] = configurazioneTastiFatta[6]
                    configTemp[i][7] = configurazioneTastiFatta[7]
                    configTemp[i][8] = int(configurazioneTastiFatta[8].split(":")[1])
                    configurazioneSalvata = True
                    break
                i += 1
            if not configurazioneSalvata:
                configurazioneTastiFatta[8] = int(configurazioneTastiFatta[8].split(":")[1])
                configTemp.append(configurazioneTastiFatta)
            if not precedentementeInizializzato:
                controllerDaConfigurare.quit()
            listaIdPadConfigModificata.append(idController)
            configurazioneTastiFatta = []
            configurando = False

        if tastiPremutiPadConfig != tastiPremutiPadConfigVecchi:
            aggiornaSchermo = True

        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput, padPassatoPerTestEConf)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            if configurando or testando:
                configurando = False
                testando = False
            else:
                risposta = True
            bottoneDown = False
        elif bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if not (bottoneDown == "mouseSinistro" and (cursoreSuFrecciaSinistra or cursoreSuFrecciaDestra)):
                if bottoneDown == "mouseSinistro" and suTornaIndietro:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    if configurando or testando:
                        if not precedentementeInizializzato:
                            controllerDaConfigurare.quit()
                        configurando = False
                        testando = False
                    else:
                        risposta = True
                # aggiorna lista controller
                elif voceMarcata == 1 and countdownAggiornamentoModulo <= 0:
                    countdownAggiornamentoModulo = 150
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    for pad in GlobalHWVar.listaPadConnessiConfigurati:
                        pad.quit()
                    if controllerDaConfigurare and controllerDaConfigurare.get_init():
                        controllerDaConfigurare.quit()
                    GlobalHWVar.inizializzaModuloJoistick()

                    numPadSelezionato = 0
                    if len(GlobalHWVar.configPadConnessi) > 0:
                        controllerDaConfigurare = False
                        idController = GlobalHWVar.configPadConnessi[numPadSelezionato][0]
                        nomeController = GlobalHWVar.configPadConnessi[numPadSelezionato][1]
                        padInizialmeteConfigurato = False
                        for pad in GlobalHWVar.listaPadConnessiConfigurati:
                            if idController == pad.get_id():
                                controllerDaConfigurare = pad
                                padInizialmeteConfigurato = True
                                break
                        if not controllerDaConfigurare:
                            for pad in GlobalHWVar.listaPadConnessiSconosciuti:
                                if idController == pad.get_id():
                                    controllerDaConfigurare = pad
                                    padInizialmeteConfigurato = False
                                    break
                    else:
                        controllerDaConfigurare = False
                        idController = -1
                        nomeController = "Nessun controller rilevato"
                        padInizialmeteConfigurato = False
                # inizia configurazione
                elif not configurando and voceMarcata == 3:
                    if controllerDaConfigurare and not controllerDaConfigurare.get_init():
                        precedentementeInizializzato = False
                        controllerDaConfigurare.init()
                    elif controllerDaConfigurare and controllerDaConfigurare.get_init():
                        precedentementeInizializzato = True
                    if controllerDaConfigurare and controllerDaConfigurare.get_init():
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        configurazioneTastiFatta = []
                        configurazioneTastiFatta.append(nomeController)
                        tastoDaConfigurare = 0
                        configurando = True
                        aggiornaSchermo = True
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                # canella configurazione
                elif voceMarcata == 4:
                    if controllerDaConfigurare:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        i = 0
                        while i < len(configTemp):
                            if configTemp[i][0] == nomeController:
                                del configTemp[i]
                                break
                            i += 1
                        i = 0
                        while i < len(listaIdPadConfigModificata):
                            if listaIdPadConfigModificata[i] == idController:
                                del listaIdPadConfigModificata[i]
                                break
                            i += 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                # testa controller
                elif not testando and voceMarcata == 5:
                    if controllerDaConfigurare and not controllerDaConfigurare.get_init():
                        precedentementeInizializzato = False
                        controllerDaConfigurare.init()
                    elif controllerDaConfigurare and controllerDaConfigurare.get_init():
                        precedentementeInizializzato = True
                    if controllerDaConfigurare and controllerDaConfigurare.get_init():
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        testando = True
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                # salva
                elif voceMarcata == 6:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    scrivi = GlobalHWVar.loadFile("Impostazioni/ImpoController.txt", "w")
                    for padConf in configTemp:
                        for elemento in padConf:
                            scrivi.write(str(elemento) + "_")
                        scrivi.write("\n")
                    scrivi.close()
                    for pad in GlobalHWVar.listaPadConnessiConfigurati:
                        pad.quit()
                    if controllerDaConfigurare and controllerDaConfigurare.get_init():
                        controllerDaConfigurare.quit()
                    GlobalHWVar.inizializzaModuloJoistick()

                    listaIdPadConfigModificata = []
                    numPadSelezionato = 0
                    if len(GlobalHWVar.configPadConnessi) > 0:
                        controllerDaConfigurare = False
                        idController = GlobalHWVar.configPadConnessi[numPadSelezionato][0]
                        nomeController = GlobalHWVar.configPadConnessi[numPadSelezionato][1]
                        padInizialmeteConfigurato = False
                        for pad in GlobalHWVar.listaPadConnessiConfigurati:
                            if idController == pad.get_id():
                                controllerDaConfigurare = pad
                                padInizialmeteConfigurato = True
                                break
                        if not controllerDaConfigurare:
                            for pad in GlobalHWVar.listaPadConnessiSconosciuti:
                                if idController == pad.get_id():
                                    controllerDaConfigurare = pad
                                    padInizialmeteConfigurato = False
                                    break
                    else:
                        controllerDaConfigurare = False
                        idController = -1
                        nomeController = "Nessun controller rilevato"
                        padInizialmeteConfigurato = False
                # esci
                elif voceMarcata == 7:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    risposta = True
                else:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
                bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == "mouseSinistro" or bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == "padGiu" or bottoneDown == "padSu" or ((voceMarcata == 2 or voceMarcata == 6 or voceMarcata == 7) and (bottoneDown == pygame.K_d or bottoneDown == pygame.K_a or bottoneDown == "padDestra" or bottoneDown == "padSinistra")):
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput or countdownAggiornamentoModulo == 0:
            if countdownAggiornamentoModulo == 0:
                countdownAggiornamentoModulo = -1
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if not (configurando or testando):
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if voceMarcata == 1:
                        voceMarcata += 5
                        xp = GlobalHWVar.gsx // 32 * 4.4
                        yp = GlobalHWVar.gsy // 18 * 14.9
                    elif voceMarcata == 2 or voceMarcata == 4 or voceMarcata == 5:
                        voceMarcata -= 1
                        yp = yp - GlobalHWVar.gsy // 18 * 1.5
                    elif voceMarcata == 3:
                        voceMarcata -= 1
                        yp = GlobalHWVar.gsy // 18 * 6.6
                    elif voceMarcata == 6:
                        voceMarcata -= 1
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 12.6
                    elif voceMarcata == 7:
                        voceMarcata -= 2
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 12.6
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento) and not (configurando or testando):
                if voceMarcata == 2:
                    if len(GlobalHWVar.configPadConnessi) > 1:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    numPadSelezionato -= 1
                    if numPadSelezionato < 0:
                        numPadSelezionato = len(GlobalHWVar.configPadConnessi) - 1
                    if len(GlobalHWVar.configPadConnessi) > 0:
                        controllerDaConfigurare = False
                        idController = GlobalHWVar.configPadConnessi[numPadSelezionato][0]
                        nomeController = GlobalHWVar.configPadConnessi[numPadSelezionato][1]
                        padInizialmeteConfigurato = False
                        for pad in GlobalHWVar.listaPadConnessiConfigurati:
                            if idController == pad.get_id():
                                controllerDaConfigurare = pad
                                padInizialmeteConfigurato = True
                                break
                        if not controllerDaConfigurare:
                            for pad in GlobalHWVar.listaPadConnessiSconosciuti:
                                if idController == pad.get_id():
                                    controllerDaConfigurare = pad
                                    padInizialmeteConfigurato = False
                                    break
                    else:
                        controllerDaConfigurare = False
                        idController = -1
                        nomeController = "Nessun controller rilevato"
                        padInizialmeteConfigurato = False
                elif voceMarcata == 6:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    voceMarcata += 1
                    xp = GlobalHWVar.gsx // 32 * 8.5
                elif voceMarcata == 7:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    voceMarcata -= 1
                    xp = GlobalHWVar.gsx // 32 * 4.5
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if not (configurando or testando):
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if voceMarcata == 1 or voceMarcata == 3 or voceMarcata == 4:
                        voceMarcata += 1
                        yp = yp + GlobalHWVar.gsy // 18 * 1.5
                    elif voceMarcata == 2:
                        voceMarcata += 1
                        yp = GlobalHWVar.gsy // 18 * 9.6
                    elif voceMarcata == 5:
                        voceMarcata += 1
                        xp = GlobalHWVar.gsx // 32 * 4.4
                        yp = GlobalHWVar.gsy // 18 * 14.9
                    elif voceMarcata == 6:
                        voceMarcata -= 5
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 5.1
                    elif voceMarcata == 7:
                        voceMarcata -= 6
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 5.1
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento) and not (configurando or testando):
                if voceMarcata == 2:
                    if len(GlobalHWVar.configPadConnessi) > 1:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    numPadSelezionato += 1
                    if numPadSelezionato > len(GlobalHWVar.configPadConnessi) - 1:
                        numPadSelezionato = 0
                    if len(GlobalHWVar.configPadConnessi) > 0:
                        controllerDaConfigurare = False
                        idController = GlobalHWVar.configPadConnessi[numPadSelezionato][0]
                        nomeController = GlobalHWVar.configPadConnessi[numPadSelezionato][1]
                        padInizialmeteConfigurato = False
                        for pad in GlobalHWVar.listaPadConnessiConfigurati:
                            if idController == pad.get_id():
                                controllerDaConfigurare = pad
                                padInizialmeteConfigurato = True
                                break
                        if not controllerDaConfigurare:
                            for pad in GlobalHWVar.listaPadConnessiSconosciuti:
                                if idController == pad.get_id():
                                    controllerDaConfigurare = pad
                                    padInizialmeteConfigurato = False
                                    break
                    else:
                        controllerDaConfigurare = False
                        idController = -1
                        nomeController = "Nessun controller rilevato"
                        padInizialmeteConfigurato = False
                elif voceMarcata == 6:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    voceMarcata += 1
                    xp = GlobalHWVar.gsx // 32 * 8.5
                elif voceMarcata == 7:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    voceMarcata -= 1
                    xp = GlobalHWVar.gsx // 32 * 4.5
            if bottoneDown == "mouseSinistro" and voceMarcata == 2 and cursoreSuFrecciaSinistra and (tastotempfps == 0 or primoMovimento):
                if len(GlobalHWVar.configPadConnessi) > 1:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                numPadSelezionato -= 1
                if numPadSelezionato < 0:
                    numPadSelezionato = len(GlobalHWVar.configPadConnessi) - 1
                if len(GlobalHWVar.configPadConnessi) > 0:
                    controllerDaConfigurare = False
                    idController = GlobalHWVar.configPadConnessi[numPadSelezionato][0]
                    nomeController = GlobalHWVar.configPadConnessi[numPadSelezionato][1]
                    padInizialmeteConfigurato = False
                    for pad in GlobalHWVar.listaPadConnessiConfigurati:
                        if idController == pad.get_id():
                            controllerDaConfigurare = pad
                            padInizialmeteConfigurato = True
                            break
                    if not controllerDaConfigurare:
                        for pad in GlobalHWVar.listaPadConnessiSconosciuti:
                            if idController == pad.get_id():
                                controllerDaConfigurare = pad
                                padInizialmeteConfigurato = False
                                break
                else:
                    controllerDaConfigurare = False
                    idController = -1
                    nomeController = "Nessun controller rilevato"
                    padInizialmeteConfigurato = False
            if bottoneDown == "mouseSinistro" and voceMarcata == 2 and cursoreSuFrecciaDestra and (tastotempfps == 0 or primoMovimento):
                if len(GlobalHWVar.configPadConnessi) > 1:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                numPadSelezionato += 1
                if numPadSelezionato > len(GlobalHWVar.configPadConnessi) - 1:
                    numPadSelezionato = 0
                if len(GlobalHWVar.configPadConnessi) > 0:
                    controllerDaConfigurare = False
                    idController = GlobalHWVar.configPadConnessi[numPadSelezionato][0]
                    nomeController = GlobalHWVar.configPadConnessi[numPadSelezionato][1]
                    padInizialmeteConfigurato = False
                    for pad in GlobalHWVar.listaPadConnessiConfigurati:
                        if idController == pad.get_id():
                            controllerDaConfigurare = pad
                            padInizialmeteConfigurato = True
                            break
                    if not controllerDaConfigurare:
                        for pad in GlobalHWVar.listaPadConnessiSconosciuti:
                            if idController == pad.get_id():
                                controllerDaConfigurare = pad
                                padInizialmeteConfigurato = False
                                break
                else:
                    controllerDaConfigurare = False
                    idController = -1
                    nomeController = "Nessun controller rilevato"
                    padInizialmeteConfigurato = False
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                GenericFunc.messaggio("Configura controller", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostazioniController, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                GenericFunc.messaggio("Seleziona il controller da configurare:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.5, 60)
                GenericFunc.messaggio("Inizia configurazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.5, 60)
                GenericFunc.messaggio("Cancella configurazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, 60)
                GenericFunc.messaggio("Testa configurazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.5, 60)

                GenericFunc.messaggio("Salva", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5.3, GlobalHWVar.gsy // 18 * 14.7, 70)
                GenericFunc.messaggio("Indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.4, GlobalHWVar.gsy // 18 * 14.7, 70)
            else:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 10))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.7, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 1.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 7.5, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 1.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 14.9, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 8.5, GlobalHWVar.gsy // 18 * 14.9, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 16.5, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostazioniController, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 22, 0, GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2.5))
                if GlobalHWVar.mouseVisibile:
                    GenericFunc.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    GenericFunc.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    GenericFunc.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gpx * 8.5) - 1, GlobalHWVar.gpy * 14.5), ((GlobalHWVar.gpx * 8.5) - 1, GlobalHWVar.gpy * 15.9), 2)

            if countdownAggiornamentoModulo <= 0:
                GenericFunc.messaggio("Aggiorna lista controller collegati", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, 60)
            else:
                GenericFunc.messaggio("Aggiorna lista controller collegati", GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, 60)
            if idController != -1:
                GenericFunc.messaggio("#" + str(idController) + " " + nomeController, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 8.5, GlobalHWVar.gsy // 18 * 7.8, 50, centrale=True, lungMax=11)
            else:
                GenericFunc.messaggio(nomeController, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 8.5, GlobalHWVar.gsy // 18 * 7.8, 50, centrale=True, lungMax=11)
            if voceMarcata == 2:
                if bottoneDown == pygame.K_a or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaSinistra) or bottoneDown == "padSinistra":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistraBloccato, (GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 7.6))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistra, (GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 7.6))
                if bottoneDown == pygame.K_d or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaDestra) or bottoneDown == "padDestra":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestraBloccato, (GlobalHWVar.gsx // 32 * 14.5, GlobalHWVar.gsy // 18 * 7.6))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestra, (GlobalHWVar.gsx // 32 * 14.5, GlobalHWVar.gsy // 18 * 7.6))

            if configurando:
                GenericFunc.messaggio("Clicca i tasti illuminati", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13.5, 40, centrale=True)
                if ordineConfigTasti[tastoDaConfigurare] == "croce":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerCroce, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "cerchio":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerCerchio, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "quadrato":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerQuadrato, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "triangolo":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerTriangolo, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "l1":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerL1, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "r1":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerR1, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "start":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerStart, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "croceDir":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerCroceDirezionale, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
            elif testando:
                configurazioneDaTestare = []
                for padConf in configTemp:
                    if padConf[0] == nomeController:
                        configurazioneDaTestare.append(int(padConf[1]))
                        configurazioneDaTestare.append(int(padConf[2]))
                        configurazioneDaTestare.append(int(padConf[3]))
                        configurazioneDaTestare.append(int(padConf[4]))
                        configurazioneDaTestare.append(int(padConf[5]))
                        configurazioneDaTestare.append(int(padConf[6]))
                        configurazioneDaTestare.append(int(padConf[7]))
                        configurazioneDaTestare.append("croceDir:" + str(padConf[8]))
                        break
                if len(configurazioneDaTestare) > 0:
                    if configurazioneDaTestare[0] in tastiPremutiPadConfig:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerCroce, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                    if configurazioneDaTestare[1] in tastiPremutiPadConfig:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerCerchio, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                    if configurazioneDaTestare[2] in tastiPremutiPadConfig:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerQuadrato, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                    if configurazioneDaTestare[3] in tastiPremutiPadConfig:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerTriangolo, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                    if configurazioneDaTestare[4] in tastiPremutiPadConfig:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerL1, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                    if configurazioneDaTestare[5] in tastiPremutiPadConfig:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerR1, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                    if configurazioneDaTestare[6] in tastiPremutiPadConfig:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerStart, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                    if configurazioneDaTestare[7] in tastiPremutiPadConfig:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerCroceDirezionale, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                GenericFunc.messaggio("Controlla che i tasti premuti corrispondano a quelli illuminati", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13.5, 40, centrale=True)
            else:
                if controllerDaConfigurare:
                    if padInizialmeteConfigurato:
                        GenericFunc.messaggio(u"Controller configurato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13.5, 40, centrale=True)
                    else:
                        GenericFunc.messaggio(u"Controller non configurato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13.5, 40, centrale=True)
                else:
                    GenericFunc.messaggio("Nessun controller rilevato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13.5, 40, centrale=True)
            padConfiguratoTemp = False
            for padConf in configTemp:
                if padConf[0] == nomeController:
                    padConfiguratoTemp = True
            if padInizialmeteConfigurato != padConfiguratoTemp:
                if padConfiguratoTemp:
                    GenericFunc.messaggio("Controller temporaneamente configurato", GlobalHWVar.verde, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14.5, 40, centrale=True)
                else:
                    GenericFunc.messaggio("Controller temporaneamente non configurato", GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14.5, 40, centrale=True)
            else:
                if idController in listaIdPadConfigModificata:
                    GenericFunc.messaggio("Configurazione temporaneamente modificata", GlobalHWVar.verde, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14.5, 40, centrale=True)

            if configurando or testando:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xp, yp))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        if countdownAggiornamentoModulo > 0:
            countdownAggiornamentoModulo -= 1
        pygame.event.pump()
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def menuImpostazioni(settaRisoluzione, dimezzaVolumeCanzone):
    puntatore = GlobalImgVar.puntatore
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 5.1
    risposta = False
    voceMarcata = 1
    aggiornaSchermo = False

    linguaTemp = GlobalHWVar.linguaImpostata
    volumeEffettiTemp = GlobalHWVar.volumeEffetti * 10
    volumeCanzoniTemp = GlobalHWVar.volumeCanzoni * 10
    gsxTemp = GlobalHWVar.gsx
    gsyTemp = GlobalHWVar.gsy
    schermoInteroTemp = GlobalHWVar.schermoIntero

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        cursoreSuFrecciaSinistra = False
        cursoreSuFrecciaDestra = False
        cursoreSuImpoController = False
        xMouse, yMouse = pygame.mouse.get_pos()
        suTornaIndietro = False
        if GlobalHWVar.mouseVisibile:
            if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalHWVar.gsx // 32 * 10 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 14.1 <= yMouse <= GlobalHWVar.gsy // 18 * 16.1:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                voceMarcata = 7
                xp = GlobalHWVar.gsx // 32 * 10.5
                yp = GlobalHWVar.gsy // 18 * 14.8
            elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 22 and GlobalHWVar.gsy // 18 * 14.1 <= yMouse <= GlobalHWVar.gsy // 18 * 16.1:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                voceMarcata = 8
                xp = GlobalHWVar.gsx // 32 * 16
                yp = GlobalHWVar.gsy // 18 * 14.8
            elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 16.9 and GlobalHWVar.gsy // 18 * 4.8 <= yMouse <= GlobalHWVar.gsy // 18 * 6:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalHWVar.gsx // 32 * 19.7 <= xMouse <= GlobalHWVar.gsx // 32 * 20.6 and GlobalHWVar.gsy // 18 * 4.8 <= yMouse <= GlobalHWVar.gsy // 18 * 6:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 16.9 and GlobalHWVar.gsy // 18 * 6.3 <= yMouse <= GlobalHWVar.gsy // 18 * 7.5:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalHWVar.gsx // 32 * 18 <= xMouse <= GlobalHWVar.gsx // 32 * 18.9 and GlobalHWVar.gsy // 18 * 6.3 <= yMouse <= GlobalHWVar.gsy // 18 * 7.5:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 16.9 and GlobalHWVar.gsy // 18 * 7.8 <= yMouse <= GlobalHWVar.gsy // 18 * 9:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalHWVar.gsx // 32 * 18 <= xMouse <= GlobalHWVar.gsx // 32 * 18.9 and GlobalHWVar.gsy // 18 * 7.8 <= yMouse <= GlobalHWVar.gsy // 18 * 9:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 21.2 and GlobalHWVar.gsy // 18 * 9.3 <= yMouse <= GlobalHWVar.gsy // 18 * 10.5:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuImpoController = True
            elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 16.9 and GlobalHWVar.gsy // 18 * 10.8 <= yMouse <= GlobalHWVar.gsy // 18 * 12:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalHWVar.gsx // 32 * 21.3 <= xMouse <= GlobalHWVar.gsx // 32 * 22.2 and GlobalHWVar.gsy // 18 * 10.8 <= yMouse <= GlobalHWVar.gsy // 18 * 12:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 16.9 and GlobalHWVar.gsy // 18 * 12.3 <= yMouse <= GlobalHWVar.gsy // 18 * 13.5:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalHWVar.gsx // 32 * 18.1 <= xMouse <= GlobalHWVar.gsx // 32 * 19 and GlobalHWVar.gsy // 18 * 12.3 <= yMouse <= GlobalHWVar.gsy // 18 * 13.5:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            else:
                if not GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(True)
            if GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 31:
                if GlobalHWVar.gsy // 18 * 4.6 <= yMouse <= GlobalHWVar.gsy // 18 * 6.1:
                    voceMarcata = 1
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 5.1
                elif GlobalHWVar.gsy // 18 * 6.1 <= yMouse <= GlobalHWVar.gsy // 18 * 7.6:
                    voceMarcata = 2
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 6.6
                elif GlobalHWVar.gsy // 18 * 7.6 <= yMouse <= GlobalHWVar.gsy // 18 * 9.1:
                    voceMarcata = 3
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 8.1
                elif GlobalHWVar.gsy // 18 * 9.1 <= yMouse <= GlobalHWVar.gsy // 18 * 10.6:
                    voceMarcata = 4
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 9.6
                elif GlobalHWVar.gsy // 18 * 10.6 <= yMouse <= GlobalHWVar.gsy // 18 * 12.1:
                    voceMarcata = 5
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 11.1
                elif GlobalHWVar.gsy // 18 * 12.1 <= yMouse <= GlobalHWVar.gsy // 18 * 13.6:
                    voceMarcata = 6
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 12.6
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            risposta = True
            bottoneDown = False
        elif bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if not (bottoneDown == "mouseSinistro" and (cursoreSuFrecciaSinistra or cursoreSuFrecciaDestra)):
                if bottoneDown == "mouseSinistro" and suTornaIndietro:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    risposta = True
                elif bottoneDown == "mouseSinistro" and cursoreSuImpoController and settaRisoluzione:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    settaController()
                    primoFrame = True
                elif voceMarcata == 4 and not bottoneDown == "mouseSinistro" and settaRisoluzione:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    settaController()
                    primoFrame = True
                elif voceMarcata == 7:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    GlobalHWVar.linguaImpostata = linguaTemp
                    GlobalHWVar.volumeEffetti = volumeEffettiTemp / 10 * 1.0
                    GlobalHWVar.volumeCanzoni = volumeCanzoniTemp / 10 * 1.0
                    GlobalHWVar.initVolumeSounds()
                    if dimezzaVolumeCanzone:
                        GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni / 2)
                        GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti / 2)
                    if GlobalHWVar.gsx != gsxTemp or GlobalHWVar.gsy != gsyTemp or GlobalHWVar.schermoIntero != schermoInteroTemp:
                        ricaricaImgs = False
                        if GlobalHWVar.gsx != gsxTemp or GlobalHWVar.gsy != gsyTemp:
                            ricaricaImgs = True
                        GlobalHWVar.schermoIntero = schermoInteroTemp
                        GlobalHWVar.gsx = gsxTemp
                        GlobalHWVar.gsy = gsyTemp
                        GlobalHWVar.gpx = GlobalHWVar.gsx // 32
                        GlobalHWVar.gpy = GlobalHWVar.gsy // 18
                        if GlobalHWVar.schermoIntero:
                            opzioni_schermo = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
                            GlobalHWVar.schermo = pygame.display.set_mode((GlobalHWVar.gsx, GlobalHWVar.gsy), opzioni_schermo)
                        else:
                            opzioni_schermo = pygame.DOUBLEBUF
                            GlobalHWVar.schermo = pygame.display.set_mode((GlobalHWVar.gsx, GlobalHWVar.gsy), opzioni_schermo)
                            pygame.display.set_caption(GlobalHWVar.titolo)
                            pygame.display.set_icon(GlobalHWVar.icona)
                        if ricaricaImgs:
                            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                            GenericFunc.messaggio("Cambio risoluzione in corso...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 7.5, 120, centrale=True)
                            GenericFunc.oscuraIlluminaSchermo(illumina=2)
                            GlobalGameVar.numImgCaricata = 0
                            GlobalImgVar.loadImgs(GlobalGameVar.numImgCaricata, cambioRisoluzione=True)
                    # salvo in un file la configurazione (ordine => lingua, volEffetti, volCanzoni, schermoIntero, gsx, gsy)
                    scrivi = GlobalHWVar.loadFile("Impostazioni/Impostazioni.txt", "w")
                    if GlobalHWVar.linguaImpostata == "italiano":
                        scrivi.write("0_")
                    elif GlobalHWVar.linguaImpostata == "inglese":
                        scrivi.write("1_")
                    scrivi.write(str(int(GlobalHWVar.volumeEffetti * 10)) + "_")
                    scrivi.write(str(int(GlobalHWVar.volumeCanzoni * 10)) + "_")
                    if GlobalHWVar.schermoIntero:
                        scrivi.write("1_")
                    else:
                        scrivi.write("0_")
                    scrivi.write(str(GlobalHWVar.gsx) + "_")
                    scrivi.write(str(GlobalHWVar.gsy) + "_")
                    scrivi.close()
                    puntatore = GlobalImgVar.puntatore
                    yp = GlobalHWVar.gsy // 18 * 14.8
                    xp = GlobalHWVar.gsx // 32 * 10.5
                    primoFrame = True
                elif voceMarcata == 8:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    risposta = True
                else:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
                bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == "mouseSinistro" or bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == "padGiu" or bottoneDown == "padSu" or (voceMarcata != 4 and (bottoneDown == pygame.K_d or bottoneDown == pygame.K_a or bottoneDown == "padDestra" or bottoneDown == "padSinistra")):
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 2 or voceMarcata == 3 or voceMarcata == 4 or voceMarcata == 5 or voceMarcata == 6:
                    voceMarcata -= 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = yp - GlobalHWVar.gsy // 18 * 1.5
                    xp = GlobalHWVar.gsx // 32 * 1
                elif voceMarcata == 7:
                    voceMarcata -= 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gsy // 18 * 12.6
                    xp = GlobalHWVar.gsx // 32 * 1
                elif voceMarcata == 8:
                    voceMarcata -= 2
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gsy // 18 * 12.6
                    xp = GlobalHWVar.gsx // 32 * 1
                elif voceMarcata == 1:
                    voceMarcata += 6
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gsy // 18 * 14.8
                    xp = GlobalHWVar.gsx // 32 * 10.5
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if linguaTemp == "italiano":
                        linguaTemp = "inglese"
                    elif linguaTemp == "inglese":
                        linguaTemp = "italiano"
                elif voceMarcata == 2:
                    if volumeEffettiTemp != 0:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        volumeEffettiTemp -= 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 3:
                    if volumeCanzoniTemp != 0:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        volumeCanzoniTemp -= 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 5:
                    if settaRisoluzione and GlobalHWVar.maxGsx > 800 and GlobalHWVar.maxGsy > 450:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if gsxTemp == 800 and gsyTemp == 450:
                            gsxTemp = GlobalHWVar.maxGsx
                            gsyTemp = GlobalHWVar.maxGsy
                        elif gsxTemp == 1024 and gsyTemp == 576:
                            gsxTemp = 800
                            gsyTemp = 450
                        elif gsxTemp == 1280 and gsyTemp == 720:
                            gsxTemp = 1024
                            gsyTemp = 576
                        elif gsxTemp == 1920 and gsyTemp == 1080:
                            gsxTemp = 1280
                            gsyTemp = 720
                        elif gsxTemp == GlobalHWVar.maxGsx and gsyTemp == GlobalHWVar.maxGsy:
                            if GlobalHWVar.maxGsx > 1920 and GlobalHWVar.maxGsy > 1080:
                                gsxTemp = 1920
                                gsyTemp = 1080
                            elif GlobalHWVar.maxGsx > 1280 and GlobalHWVar.maxGsy > 720:
                                gsxTemp = 1280
                                gsyTemp = 720
                            elif GlobalHWVar.maxGsx > 1024 and GlobalHWVar.maxGsy > 576:
                                gsxTemp = 1024
                                gsyTemp = 576
                            elif GlobalHWVar.maxGsx > 800 and GlobalHWVar.maxGsy > 450:
                                gsxTemp = 800
                                gsyTemp = 450
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 6:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if schermoInteroTemp:
                        schermoInteroTemp = False
                    else:
                        schermoInteroTemp = True
                elif voceMarcata == 7:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    voceMarcata += 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = GlobalHWVar.gsx // 32 * 16
                elif voceMarcata == 8:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    voceMarcata -= 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = GlobalHWVar.gsx // 32 * 10.5
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1 or voceMarcata == 2 or voceMarcata == 3 or voceMarcata == 4 or voceMarcata == 5:
                    voceMarcata += 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = yp + GlobalHWVar.gsy // 18 * 1.5
                elif voceMarcata == 6:
                    voceMarcata += 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gsy // 18 * 14.8
                    xp = GlobalHWVar.gsx // 32 * 10.5
                elif voceMarcata == 7:
                    voceMarcata -= 6
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gsy // 18 * 5.1
                    xp = GlobalHWVar.gsx // 32 * 1
                elif voceMarcata == 8:
                    voceMarcata -= 7
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gsy // 18 * 5.1
                    xp = GlobalHWVar.gsx // 32 * 1
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if linguaTemp == "italiano":
                        linguaTemp = "inglese"
                    elif linguaTemp == "inglese":
                        linguaTemp = "italiano"
                elif voceMarcata == 2:
                    if volumeEffettiTemp != 10:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        volumeEffettiTemp += 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 3:
                    if volumeCanzoniTemp != 10:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        volumeCanzoniTemp += 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 5:
                    if settaRisoluzione and GlobalHWVar.maxGsx > 800 and GlobalHWVar.maxGsy > 450:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if gsxTemp == 800 and gsyTemp == 450:
                            if GlobalHWVar.maxGsx > 1024 and GlobalHWVar.maxGsy > 576:
                                gsxTemp = 1024
                                gsyTemp = 576
                            else:
                                gsxTemp = GlobalHWVar.maxGsx
                                gsyTemp = GlobalHWVar.maxGsy
                        elif gsxTemp == 1024 and gsyTemp == 576:
                            if GlobalHWVar.maxGsx > 1280 and GlobalHWVar.maxGsy > 720:
                                gsxTemp = 1280
                                gsyTemp = 720
                            elif GlobalHWVar.maxGsx == 1024 and GlobalHWVar.maxGsy == 576:
                                gsxTemp = 800
                                gsyTemp = 450
                            else:
                                gsxTemp = GlobalHWVar.maxGsx
                                gsyTemp = GlobalHWVar.maxGsy
                        elif gsxTemp == 1280 and gsyTemp == 720:
                            if GlobalHWVar.maxGsx > 1920 and GlobalHWVar.maxGsy > 1080:
                                gsxTemp = 1920
                                gsyTemp = 1080
                            elif GlobalHWVar.maxGsx == 1280 and GlobalHWVar.maxGsy == 720:
                                gsxTemp = 800
                                gsyTemp = 450
                            else:
                                gsxTemp = GlobalHWVar.maxGsx
                                gsyTemp = GlobalHWVar.maxGsy
                        elif gsxTemp == 1920 and gsyTemp == 1080:
                            if GlobalHWVar.maxGsx > 1920 and GlobalHWVar.maxGsy > 1080:
                                gsxTemp = GlobalHWVar.maxGsx
                                gsyTemp = GlobalHWVar.maxGsy
                            else:
                                gsxTemp = 800
                                gsyTemp = 450
                        elif gsxTemp == GlobalHWVar.maxGsx and gsyTemp == GlobalHWVar.maxGsy:
                            if GlobalHWVar.maxGsx > 800 and GlobalHWVar.maxGsy > 450:
                                gsxTemp = 800
                                gsyTemp = 450
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 6:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if schermoInteroTemp:
                        schermoInteroTemp = False
                    else:
                        schermoInteroTemp = True
                elif voceMarcata == 7:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    voceMarcata += 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = GlobalHWVar.gsx // 32 * 16
                elif voceMarcata == 8:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    voceMarcata -= 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = GlobalHWVar.gsx // 32 * 10.5
            if bottoneDown == "mouseSinistro" and cursoreSuFrecciaSinistra and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if linguaTemp == "italiano":
                        linguaTemp = "inglese"
                    elif linguaTemp == "inglese":
                        linguaTemp = "italiano"
                elif voceMarcata == 2:
                    if volumeEffettiTemp != 0:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        volumeEffettiTemp -= 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 3:
                    if volumeCanzoniTemp != 0:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        volumeCanzoniTemp -= 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 5:
                    if settaRisoluzione and GlobalHWVar.maxGsx > 800 and GlobalHWVar.maxGsy > 450:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if gsxTemp == 800 and gsyTemp == 450:
                            gsxTemp = GlobalHWVar.maxGsx
                            gsyTemp = GlobalHWVar.maxGsy
                        elif gsxTemp == 1024 and gsyTemp == 576:
                            gsxTemp = 800
                            gsyTemp = 450
                        elif gsxTemp == 1280 and gsyTemp == 720:
                            gsxTemp = 1024
                            gsyTemp = 576
                        elif gsxTemp == 1920 and gsyTemp == 1080:
                            gsxTemp = 1280
                            gsyTemp = 720
                        elif gsxTemp == GlobalHWVar.maxGsx and gsyTemp == GlobalHWVar.maxGsy:
                            if GlobalHWVar.maxGsx > 1920 and GlobalHWVar.maxGsy > 1080:
                                gsxTemp = 1920
                                gsyTemp = 1080
                            elif GlobalHWVar.maxGsx > 1280 and GlobalHWVar.maxGsy > 720:
                                gsxTemp = 1280
                                gsyTemp = 720
                            elif GlobalHWVar.maxGsx > 1024 and GlobalHWVar.maxGsy > 576:
                                gsxTemp = 1024
                                gsyTemp = 576
                            elif GlobalHWVar.maxGsx > 800 and GlobalHWVar.maxGsy > 450:
                                gsxTemp = 800
                                gsyTemp = 450
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 6:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if schermoInteroTemp:
                        schermoInteroTemp = False
                    else:
                        schermoInteroTemp = True
            if bottoneDown == "mouseSinistro" and cursoreSuFrecciaDestra and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if linguaTemp == "italiano":
                        linguaTemp = "inglese"
                    elif linguaTemp == "inglese":
                        linguaTemp = "italiano"
                elif voceMarcata == 2:
                    if volumeEffettiTemp != 10:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        volumeEffettiTemp += 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 3:
                    if volumeCanzoniTemp != 10:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        volumeCanzoniTemp += 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 5:
                    if settaRisoluzione and GlobalHWVar.maxGsx > 800 and GlobalHWVar.maxGsy > 450:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if gsxTemp == 800 and gsyTemp == 450:
                            if GlobalHWVar.maxGsx > 1024 and GlobalHWVar.maxGsy > 576:
                                gsxTemp = 1024
                                gsyTemp = 576
                            else:
                                gsxTemp = GlobalHWVar.maxGsx
                                gsyTemp = GlobalHWVar.maxGsy
                        elif gsxTemp == 1024 and gsyTemp == 576:
                            if GlobalHWVar.maxGsx > 1280 and GlobalHWVar.maxGsy > 720:
                                gsxTemp = 1280
                                gsyTemp = 720
                            elif GlobalHWVar.maxGsx == 1024 and GlobalHWVar.maxGsy == 576:
                                gsxTemp = 800
                                gsyTemp = 450
                            else:
                                gsxTemp = GlobalHWVar.maxGsx
                                gsyTemp = GlobalHWVar.maxGsy
                        elif gsxTemp == 1280 and gsyTemp == 720:
                            if GlobalHWVar.maxGsx > 1920 and GlobalHWVar.maxGsy > 1080:
                                gsxTemp = 1920
                                gsyTemp = 1080
                            elif GlobalHWVar.maxGsx == 1280 and GlobalHWVar.maxGsy == 720:
                                gsxTemp = 800
                                gsyTemp = 450
                            else:
                                gsxTemp = GlobalHWVar.maxGsx
                                gsyTemp = GlobalHWVar.maxGsy
                        elif gsxTemp == 1920 and gsyTemp == 1080:
                            if GlobalHWVar.maxGsx > 1920 and GlobalHWVar.maxGsy > 1080:
                                gsxTemp = GlobalHWVar.maxGsx
                                gsyTemp = GlobalHWVar.maxGsy
                            else:
                                gsxTemp = 800
                                gsyTemp = 450
                        elif gsxTemp == GlobalHWVar.maxGsx and gsyTemp == GlobalHWVar.maxGsy:
                            if GlobalHWVar.maxGsx > 800 and GlobalHWVar.maxGsy > 450:
                                gsxTemp = 800
                                gsyTemp = 450
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 6:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if schermoInteroTemp:
                        schermoInteroTemp = False
                    else:
                        schermoInteroTemp = True
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                GenericFunc.messaggio("Impostazioni", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                GenericFunc.messaggio("Lingua", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, 60)
                GenericFunc.messaggio("Volume effetti", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.5, 60)
                GenericFunc.messaggio("Volume musica", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, 60)
                GenericFunc.messaggio("Controller", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.5, 60)
                GenericFunc.messaggio("Risoluzione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, 60)
                GenericFunc.messaggio("Schermo intero", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.5, 60)
                GenericFunc.messaggio("Salva", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 14.6, 70)
                GenericFunc.messaggio("Indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.5, GlobalHWVar.gsy // 18 * 14.6, 70)
            else:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 9.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5.9, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 0.4))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 7.4, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 0.4))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 8.9, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 0.4))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 10.4, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 0.4))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 11.9, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 0.4))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 13.4, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 0.4))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 9.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 14.8, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 14.8, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2.5))
                if GlobalHWVar.mouseVisibile:
                    GenericFunc.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    GenericFunc.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    GenericFunc.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gpx * 16) - 1, GlobalHWVar.gpy * 4.5), ((GlobalHWVar.gpx * 16) - 1, GlobalHWVar.gpy * 13.7), 2)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gpx * 16) - 1, GlobalHWVar.gpy * 14.4), ((GlobalHWVar.gpx * 16) - 1, GlobalHWVar.gpy * 15.8), 2)

            if linguaTemp == "italiano":
                GenericFunc.messaggio("Italiano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 5, 60)
            if linguaTemp == "inglese":
                GenericFunc.messaggio("English", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 5, 60)
            if voceMarcata == 1:
                if bottoneDown == pygame.K_a or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaSinistra) or bottoneDown == "padSinistra":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistraBloccato, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 4.9))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistra, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 4.9))
                if bottoneDown == pygame.K_d or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaDestra) or bottoneDown == "padDestra":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestraBloccato, (GlobalHWVar.gsx // 32 * 19.9, GlobalHWVar.gsy // 18 * 4.9))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestra, (GlobalHWVar.gsx // 32 * 19.9, GlobalHWVar.gsy // 18 * 4.9))
            GenericFunc.messaggio(str(int(volumeEffettiTemp)), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 6.5, 60)
            if voceMarcata == 2:
                if volumeEffettiTemp != 0:
                    if bottoneDown == pygame.K_a or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaSinistra) or bottoneDown == "padSinistra":
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistraBloccato, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 6.4))
                    else:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistra, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 6.4))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistraBloccato, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 6.4))
                if volumeEffettiTemp != 10:
                    if bottoneDown == pygame.K_d or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaDestra) or bottoneDown == "padDestra":
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestraBloccato, (GlobalHWVar.gsx // 32 * 18.2, GlobalHWVar.gsy // 18 * 6.4))
                    else:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestra, (GlobalHWVar.gsx // 32 * 18.2, GlobalHWVar.gsy // 18 * 6.4))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestraBloccato, (GlobalHWVar.gsx // 32 * 18.2, GlobalHWVar.gsy // 18 * 6.4))
            GenericFunc.messaggio(str(int(volumeCanzoniTemp)), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 8, 60)
            if voceMarcata == 3:
                if volumeCanzoniTemp != 0:
                    if bottoneDown == pygame.K_a or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaSinistra) or bottoneDown == "padSinistra":
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistraBloccato, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 7.9))
                    else:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistra, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 7.9))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistraBloccato, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 7.9))
                if volumeCanzoniTemp != 10:
                    if bottoneDown == pygame.K_d or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaDestra) or bottoneDown == "padDestra":
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestraBloccato, (GlobalHWVar.gsx // 32 * 18.2, GlobalHWVar.gsy // 18 * 7.9))
                    else:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestra, (GlobalHWVar.gsx // 32 * 18.2, GlobalHWVar.gsy // 18 * 7.9))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestraBloccato, (GlobalHWVar.gsx // 32 * 18.2, GlobalHWVar.gsy // 18 * 7.9))
            if settaRisoluzione:
                GenericFunc.messaggio("Configura", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 9.5, 60)
                GenericFunc.messaggio(str(gsxTemp) + "x" + str(gsyTemp), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 11, 60)
                if voceMarcata == 5:
                    if bottoneDown == pygame.K_a or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaSinistra) or bottoneDown == "padSinistra":
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistraBloccato, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 10.9))
                    else:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistra, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 10.9))
                    if bottoneDown == pygame.K_d or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaDestra) or bottoneDown == "padDestra":
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestraBloccato, (GlobalHWVar.gsx // 32 * 21.5, GlobalHWVar.gsy // 18 * 10.9))
                    else:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestra, (GlobalHWVar.gsx // 32 * 21.5, GlobalHWVar.gsy // 18 * 10.9))
            else:
                GenericFunc.messaggio("Configura", GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 9.5, 60)
                GenericFunc.messaggio("Configurabile solo dal menu principale", GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 30.3, GlobalHWVar.gsy // 18 * 9.8, 40, daDestra=True)
                GenericFunc.messaggio(str(gsxTemp) + "x" + str(gsyTemp), GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 11, 60)
                if voceMarcata == 5:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistraBloccato, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 10.9))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestraBloccato, (GlobalHWVar.gsx // 32 * 21.5, GlobalHWVar.gsy // 18 * 10.9))
                GenericFunc.messaggio("Configurabile solo dal menu principale", GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 30.3, GlobalHWVar.gsy // 18 * 11.3, 40, daDestra=True)
            if schermoInteroTemp:
                GenericFunc.messaggio(u"Sì", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 12.5, 60)
            else:
                GenericFunc.messaggio("No", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 12.5, 60)
            if voceMarcata == 6:
                if bottoneDown == pygame.K_a or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaSinistra) or bottoneDown == "padSinistra":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistraBloccato, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 12.4))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistra, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 12.4))
                if bottoneDown == pygame.K_d or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaDestra) or bottoneDown == "padDestra":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestraBloccato, (GlobalHWVar.gsx // 32 * 18.3, GlobalHWVar.gsy // 18 * 12.4))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestra, (GlobalHWVar.gsx // 32 * 18.3, GlobalHWVar.gsy // 18 * 12.4))

            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            if voceMarcata != 7 and voceMarcata != 8:
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xp + (int(GlobalHWVar.gpx * 0.5))), yp + (int(GlobalHWVar.gpy * 1))), (xp + (int(GlobalHWVar.gpx * 14.5)), yp + (int(GlobalHWVar.gpy * 1))), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xp + (int(GlobalHWVar.gpx * 15.5))), yp + (int(GlobalHWVar.gpy * 1))), (xp + (int(GlobalHWVar.gpx * 29.4)), yp + (int(GlobalHWVar.gpy * 1))), 2)
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def menuMappa(avanzamentoStoria):
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    imgOmbreggiaturaContorniMappaMenu = GlobalImgVar.imgOmbreggiaturaContorniMappaMenu
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 4.5
    risposta = False
    voceMarcata = 1
    voceMarcataSottoMenu = False
    aggiornaSchermo = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    # carico la mappa a seconda dell'avanzamento
    imgMappaA = GlobalImgVar.imgMappa1A
    imgMappaB = GlobalImgVar.imgMappa1B
    postiSbloccati = {"Casa": False, "Città": False, "Avamposto di Rod": False, "Castello": False, "Palazzo di Rod": False, "Vulcano": False, "Laboratorio": False, "Foresta cadetta": False, "Selva arida": False, "Labirinto": False, "Passo montano": False, "Caverna": False, "Tunnel di Rod": False, "Tunnel subacqueo": False}
    if avanzamentoStoria >= 0:
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCasa"]:
            postiSbloccati["Casa"] = True
            imgMappaA = GlobalImgVar.imgMappa1A
            imgMappaB = GlobalImgVar.imgMappa1B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaForestaCadetta"]:
            postiSbloccati["Foresta cadetta"] = True
            imgMappaA = GlobalImgVar.imgMappa2A
            imgMappaB = GlobalImgVar.imgMappa2B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCittà"]:
            postiSbloccati["Città"] = True
            imgMappaA = GlobalImgVar.imgMappa3A
            imgMappaB = GlobalImgVar.imgMappa3B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaSelvaArida"]:
            postiSbloccati["Selva arida"] = True
            imgMappaA = GlobalImgVar.imgMappa4A
            imgMappaB = GlobalImgVar.imgMappa4B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaAvampostoDiRod"]:
            postiSbloccati["Avamposto di Rod"] = True
            imgMappaA = GlobalImgVar.imgMappa5A
            imgMappaB = GlobalImgVar.imgMappa5B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaLabirinto"]:
            postiSbloccati["Labirinto"] = True
            imgMappaA = GlobalImgVar.imgMappa6A
            imgMappaB = GlobalImgVar.imgMappa6B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCastello"]:
            postiSbloccati["Castello"] = True
            imgMappaA = GlobalImgVar.imgMappa7A
            imgMappaB = GlobalImgVar.imgMappa7B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaPassoMontano"]:
            postiSbloccati["Passo montano"] = True
            imgMappaA = GlobalImgVar.imgMappa8A
            imgMappaB = GlobalImgVar.imgMappa8B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaPalazzoDiRod"]:
            postiSbloccati["Palazzo di Rod"] = True
            imgMappaA = GlobalImgVar.imgMappa9A
            imgMappaB = GlobalImgVar.imgMappa9B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCaverna"]:
            postiSbloccati["Caverna"] = True
            imgMappaA = GlobalImgVar.imgMappa10A
            imgMappaB = GlobalImgVar.imgMappa10B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaVulcano"]:
            postiSbloccati["Vulcano"] = True
            imgMappaA = GlobalImgVar.imgMappa10A
            imgMappaB = GlobalImgVar.imgMappa10B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaTunnelDiRod1"]:
            postiSbloccati["Tunnel di Rod"] = True# <- il tunnel di Rod è diviso in due parti
            imgMappaA = GlobalImgVar.imgMappa11A
            imgMappaB = GlobalImgVar.imgMappa11B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaTunnelDiRod2"]:
            postiSbloccati["Tunnel di Rod"] = True
            imgMappaA = GlobalImgVar.imgMappa12A
            imgMappaB = GlobalImgVar.imgMappa12B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaTunnelSubacqueo"]:
            postiSbloccati["Tunnel subacqueo"] = True
            imgMappaA = GlobalImgVar.imgMappa13A
            imgMappaB = GlobalImgVar.imgMappa13B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaLaboratorio"]:
            postiSbloccati["Laboratorio"] = True
            imgMappaA = GlobalImgVar.imgMappa14A
            imgMappaB = GlobalImgVar.imgMappa14B

    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoAperturaMappa)
    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        suTornaIndietro = False
        if GlobalHWVar.mouseVisibile:
            if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                suTornaIndietro = True
            elif not voceMarcataSottoMenu and GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 10:
                if GlobalHWVar.gsy // 18 * 4.3 <= yMouse <= GlobalHWVar.gsy // 18 * 5.1:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 4.5
                elif GlobalHWVar.gsy // 18 * 5.1 <= yMouse <= GlobalHWVar.gsy // 18 * 5.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 5.3
                elif GlobalHWVar.gsy // 18 * 5.9 <= yMouse <= GlobalHWVar.gsy // 18 * 6.7:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 6.1
                elif GlobalHWVar.gsy // 18 * 6.7 <= yMouse <= GlobalHWVar.gsy // 18 * 7.5:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 6.9
                elif GlobalHWVar.gsy // 18 * 7.5 <= yMouse <= GlobalHWVar.gsy // 18 * 8.3:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 7.7
                elif GlobalHWVar.gsy // 18 * 8.3 <= yMouse <= GlobalHWVar.gsy // 18 * 9.1:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 8.5
                elif GlobalHWVar.gsy // 18 * 9.1 <= yMouse <= GlobalHWVar.gsy // 18 * 9.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 9.3
                elif GlobalHWVar.gsy // 18 * 10.5 <= yMouse <= GlobalHWVar.gsy // 18 * 11.3:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 10.7
                elif GlobalHWVar.gsy // 18 * 11.3 <= yMouse <= GlobalHWVar.gsy // 18 * 12.1:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 11.5
                elif GlobalHWVar.gsy // 18 * 12.1 <= yMouse <= GlobalHWVar.gsy // 18 * 12.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 12.3
                elif GlobalHWVar.gsy // 18 * 12.9 <= yMouse <= GlobalHWVar.gsy // 18 * 13.7:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 13.1
                elif GlobalHWVar.gsy // 18 * 13.7 <= yMouse <= GlobalHWVar.gsy // 18 * 14.5:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 13.9
                elif GlobalHWVar.gsy // 18 * 14.5 <= yMouse <= GlobalHWVar.gsy // 18 * 15.3:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 14.7
                elif GlobalHWVar.gsy // 18 * 15.3 <= yMouse <= GlobalHWVar.gsy // 18 * 16.1:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 15.5
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            else:
                if not GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            if voceMarcataSottoMenu:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                voceMarcataSottoMenu = False
                primoFrame = True
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            primoFrame = True
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                if voceMarcataSottoMenu:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    voceMarcataSottoMenu = False
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    risposta = True
            elif not voceMarcataSottoMenu or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato):
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
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    voceMarcataSottoMenu = True
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == "padGiu" or bottoneDown == "padSu":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if not voceMarcataSottoMenu:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if voceMarcata == 1:
                        voceMarcata = 14
                        yp = GlobalHWVar.gsy // 18 * 15.5
                    elif voceMarcata == 8:
                        voceMarcata -= 1
                        yp = yp - GlobalHWVar.gpy * 1.4
                    else:
                        voceMarcata -= 1
                        yp = yp - GlobalHWVar.gpy * 0.8
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if not voceMarcataSottoMenu:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if voceMarcata == 14:
                        voceMarcata = 1
                        yp = GlobalHWVar.gsy // 18 * 4.5
                    elif voceMarcata == 7:
                        voceMarcata += 1
                        yp = yp + GlobalHWVar.gpy * 1.4
                    else:
                        voceMarcata += 1
                        yp = yp + GlobalHWVar.gpy * 0.8
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if not voceMarcataSottoMenu:
                if primoFrame:
                    aggiornaInterfacciaPerCambioInput = True
                    GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                    imgMappa = imgMappaA
                    GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2.5))
                    # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12.5))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15.5))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                else:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 11.6))
            else:
                if primoFrame:
                    aggiornaInterfacciaPerCambioInput = True
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscuPiuScu, (GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 16))
                    imgMappa = imgMappaB
                    if voceMarcata == 1:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-16), GlobalHWVar.gsy // 18 * 1))
                    if voceMarcata == 2:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-4.5), GlobalHWVar.gsy // 18 * (-1.5)))
                    if voceMarcata == 3:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (3), GlobalHWVar.gsy // 18 * (-9.5)))
                    if voceMarcata == 4:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (8.5), GlobalHWVar.gsy // 18 * (-17)))
                    if voceMarcata == 5:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (7.5), GlobalHWVar.gsy // 18 * (-0.5)))
                    if voceMarcata == 6:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (16), GlobalHWVar.gsy // 18 * (0)))
                    if voceMarcata == 7:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-8), GlobalHWVar.gsy // 18 * (-17)))
                    if voceMarcata == 8:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-13.5), GlobalHWVar.gsy // 18 * (-5)))
                    if voceMarcata == 9:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (0.5), GlobalHWVar.gsy // 18 * (-8)))
                    if voceMarcata == 10:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (4), GlobalHWVar.gsy // 18 * (-13)))
                    if voceMarcata == 11:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (3.5), GlobalHWVar.gsy // 18 * (-1.5)))
                    if voceMarcata == 12:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (11.5), GlobalHWVar.gsy // 18 * (0)))
                    if voceMarcata == 13:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (7), GlobalHWVar.gsy // 18 * (-6)))
                    if voceMarcata == 14:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-1.5), GlobalHWVar.gsy // 18 * (-18.5)))
                    GlobalHWVar.disegnaImmagineSuSchermo(imgOmbreggiaturaContorniMappaMenu, (0, 0))
                    # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12.5))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15.5))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 12.5))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 4))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15.5))
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xp, yp))
                    larghezzaTestoDescrizioni = GlobalHWVar.gpx * 9
                    spazioTraLeRigheTestoDescrizione = GlobalHWVar.gpy * 7 // 10
                    grandezzaScritteDescrizioni = 40
                    if voceMarcata == 1:
                        GenericFunc.messaggio("Casa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        GenericFunc.messaggio(u"È l'abitazione in cui ho vissuto con la mia famiglia fin'ora. È stata costruita da un mio vecchio antenato e, da allora, è sempre stata abitata dalle varie generazioni della mia famiglia. Secondo il babbo Hans sarà il prossimo proprietario e l'idea non lo entusiasma affatto: durante diverse discussioni Hans ha detto di non voler fare questo lavoro per tutta la vita come lui. Dice che è monotono, faticoso e anche instabile a causa delle enormi imposte e della spietata concorrenza.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 2:
                        GenericFunc.messaggio(u"Città", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        GenericFunc.messaggio(u"Da quando ne ho sentito parlare per la prima volta, ho sempre avuto il desiderio di viverci. Da quello che so, lì a tutti è concesso scegliere quale mansione svolgere nella vita. Questo è diventato possibile grazie ai nuovi strumenti di produzione che hanno reso possibile un sistema in cui poche persone riescono a produrre abbastanza anche per tutte le altre. La parte di popolazione \"impoduttiva\" può quindi dedicarsi ad altre attività come musica, teatro, studio, sport e chissà cos'altro.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 3:
                        GenericFunc.messaggio("Avamposto di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        GenericFunc.messaggio(u"Una piccola baracca che Rod esalta in maniera esagerata definendola \"avamposto\". Quella non è la sua abitazione ma, a suo dire, un luogo strategicamente fondamentale per la sopravvivenza dell'intero ecosistema cittadino. Rod non ispira molta fiducia ma tutti i suoi pensieri e ragionamenti mi sono sempre sembranti almeno sensati e coerenti... mi domando cosa nasconda quella baracca...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 4:
                        GenericFunc.messaggio("Castello", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        GenericFunc.messaggio(u"La più grande struttura che abbia mai visto fino ad ora. È un castello composto da un centinaio di stanze abitato dall'amico del bibliotecario e dai suoi numerosi servitori. Il vasto terreno su cui è stato costruito comprende anche l'intero labirinto che è stato appositamente elaborato per tenere lontani i visitatori indesiderati. Il silenzio e il comportamento dei servi creano un'atmosfera molto cupa...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 5:
                        GenericFunc.messaggio("Palazzo di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        GenericFunc.messaggio(u"La villa in cui dimora Rod. Risulta essere quasi sempre vuota e silenziosa dato che lui è costantemente fuori per lavoro o ricerche (mi domando ancora che cosa stia ricercando...). Il posto ricorda vagamente il castello di Norm ma in miniatura e con un passaggio montano al posto del labirinto per scoraggiare l'avvicinamento di viaggiatori sconosciuti.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 6:
                        GenericFunc.messaggio("Vulcano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        GenericFunc.messaggio(u"Un vulcano sommerso nelle montagne a ovest della città. È simile ad una montagna ma più grande e con un cratere sulla cima dal quale, a detta di Rod, fuoriesce del vapore incandescente. Chissà cosa c'è lì dentro...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 7:
                        GenericFunc.messaggio("Laboratorio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        GenericFunc.messaggio(u"Il laboratorio in cui Norm svolge le sue ricerche. È molto piccolo ma al suo interno è presente tutto ciò che serve, ossia un calcolatore di eventi, che si estende anche sotto il terreno, e diversi altri calcolatori che credo servano per gestire i sistemi di alimentazione e raffreddamento.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 8:
                        GenericFunc.messaggio("Foresta cadetta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        GenericFunc.messaggio(u"La foresta che mi ha sempre separata dalla città... non ho mai avuto il permesso di attraversarla perchè entrambi i miei genitori la ritenevano troppo pericolosa per me. Il nome deriva dal fatto che viene utilizzata come terreno di prova per selezionare, tra i giovani appartenenti alla nobiltà, i futuri ufficiali dell'esercito.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 9:
                        GenericFunc.messaggio("Selva arida", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        GenericFunc.messaggio(u"Denominata in questo modo perchè un tempo fitta e intricata ed ora composta soltanto da secchi abusti e funghi. Le ragioni di questo suo decadimento non sono note agli abitanti locali ma, diversi libri della biblioteca in città, sostenevano che ciò fosse dovuto ad un cambiamento climatico avvenuto circa 50 anni fa... strano... <br> Rod è solito attraversarla per tornare al suo avamposto.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 10:
                        GenericFunc.messaggio("Labirinto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        GenericFunc.messaggio(u"Un enorme terreno estremamente complicato da superare a causa delle innumerevoli strade percorribili al suo interno prive di punti di riferimento. Rod mi ha fornito una mappa che mostra nel dettaglio la sua struttura sconsigliandomi di procedere: è molto probabile non riuscire ad uscirne se non si ha un buon senso dell'orientamento.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 11:
                        GenericFunc.messaggio("Passo montano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        GenericFunc.messaggio(u"Un passaggio tra le alture a ovest della città. In città nessuno sembrava sapere di questo varco apparte Rod che lo utilizza per raggiungere il proprio palazzo da più di vent'anni.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 12:
                        GenericFunc.messaggio("Caverna", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        GenericFunc.messaggio(u"Una caverna in mezzo alle montagne che conduce ad un vulcano. All'interno vivono degli animali simili a Impo ma aggressivi. Rod è solito avventurarsi in quel posto per recuperare alimentazioni. Non mi spiego perché abbia deciso di viverci così vicino... forse ne è geloso e ne vuole controllare gli accessi?", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 13:
                        GenericFunc.messaggio("Tunnel di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        GenericFunc.messaggio(u"È un passaggio sicuro e veloce tra il palazzo di Rod e il suo avamposto. Rod lo utilizzava per trasportare direttamente le alimentazioni dalla caverna al castello di Norm. Adesso capisco l'importanza \"strategica\" di questi luoghi.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 14:
                        GenericFunc.messaggio("Tunnel subacqueo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        GenericFunc.messaggio(u"Un passaggio segreto nei sotterranei del castello di Norm che porta al suo laboratorio principale sul fondo del lago. Nonostante le pareti del tunnel siano fatte di un materiale trasparente simile al vetro, non si riesce ad osservare chiaramente il fondale del bacino a causa delle sostanze con cui questo è stato contaminato circa 50 anni fa.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2))
                if GlobalHWVar.mouseVisibile:
                    GenericFunc.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    GenericFunc.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    GenericFunc.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            if primoFrame:
                GenericFunc.messaggio("Mappa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                grandezzaScritteNormali = 45
                if postiSbloccati["Casa"]:
                    GenericFunc.messaggio("Casa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4.5, grandezzaScritteNormali)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4.5, grandezzaScritteNormali)
                if postiSbloccati["Città"]:
                    GenericFunc.messaggio(u"Città", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5.3, grandezzaScritteNormali)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5.3, grandezzaScritteNormali)
                if postiSbloccati["Avamposto di Rod"]:
                    GenericFunc.messaggio("Avamposto di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.1, grandezzaScritteNormali)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.1, grandezzaScritteNormali)
                if postiSbloccati["Castello"]:
                    GenericFunc.messaggio("Castello", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.9, grandezzaScritteNormali)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.9, grandezzaScritteNormali)
                if postiSbloccati["Palazzo di Rod"]:
                    GenericFunc.messaggio("Palazzo di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.7, grandezzaScritteNormali)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.7, grandezzaScritteNormali)
                if postiSbloccati["Vulcano"]:
                    GenericFunc.messaggio("Vulcano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.5, grandezzaScritteNormali)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.5, grandezzaScritteNormali)
                if postiSbloccati["Laboratorio"]:
                    GenericFunc.messaggio("Laboratorio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.3, grandezzaScritteNormali)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.3, grandezzaScritteNormali)
                if postiSbloccati["Foresta cadetta"]:
                    GenericFunc.messaggio("Foresta cadetta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.7, grandezzaScritteNormali)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.7, grandezzaScritteNormali)
                if postiSbloccati["Selva arida"]:
                    GenericFunc.messaggio("Selva arida", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.5, grandezzaScritteNormali)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.5, grandezzaScritteNormali)
                if postiSbloccati["Labirinto"]:
                    GenericFunc.messaggio("Labirinto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.3, grandezzaScritteNormali)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.3, grandezzaScritteNormali)
                if postiSbloccati["Passo montano"]:
                    GenericFunc.messaggio("Passo montano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.1, grandezzaScritteNormali)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.1, grandezzaScritteNormali)
                if postiSbloccati["Caverna"]:
                    GenericFunc.messaggio("Caverna", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.9, grandezzaScritteNormali)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.9, grandezzaScritteNormali)
                if postiSbloccati["Tunnel di Rod"]:
                    GenericFunc.messaggio("Tunnel di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.7, grandezzaScritteNormali)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.7, grandezzaScritteNormali)
                if postiSbloccati["Tunnel subacqueo"]:
                    GenericFunc.messaggio("Tunnel subacqueo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.5, grandezzaScritteNormali)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.5, grandezzaScritteNormali)

            if not voceMarcataSottoMenu:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def menuDiario(dati):
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 5.6
    xpv = xp
    ypv = yp
    risposta = False
    voceMarcata = 1
    voceMarcataSottoMenu = 0
    aggiornaSchermo = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        suTornaIndietro = False
        if GlobalHWVar.mouseVisibile:
            if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                suTornaIndietro = True
            else:
                if not GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            if voceMarcataSottoMenu != 0:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                voceMarcataSottoMenu = 0
                xp = xpv
                yp = ypv
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                if voceMarcataSottoMenu != 0:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    voceMarcataSottoMenu = 0
                    xp = xpv
                    yp = ypv
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    risposta = True
            elif voceMarcataSottoMenu == 0:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                voceMarcataSottoMenu = 1
                xpv = xp
                ypv = yp
                if voceMarcata == 4 or voceMarcata == 5 or voceMarcata == 6:
                    xp = GlobalHWVar.gsx // 32 * 10
                    yp = GlobalHWVar.gsy // 18 * 8
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == "padGiu" or bottoneDown == "padSu":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                if voceMarcataSottoMenu == 0:
                    if voceMarcata == 1:
                        voceMarcata += 5
                        yp = GlobalHWVar.gsy // 18 * 14.6
                    elif voceMarcata == 4:
                        voceMarcata -= 1
                        yp = GlobalHWVar.gsy // 18 * 8.6
                    else:
                        voceMarcata -= 1
                        yp = yp - GlobalHWVar.gpy * 1.5
                else:
                    if voceMarcata == 4 or voceMarcata == 5 or voceMarcata == 6:
                        if voceMarcataSottoMenu == 1:
                            voceMarcataSottoMenu += 2
                            yp = GlobalHWVar.gsy // 18 * 12
                        else:
                            voceMarcataSottoMenu -= 1
                            yp = yp - GlobalHWVar.gpy * 2
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                if voceMarcataSottoMenu == 0:
                    if voceMarcata == 6:
                        voceMarcata -= 5
                        yp = GlobalHWVar.gsy // 18 * 5.6
                    elif voceMarcata == 3:
                        voceMarcata += 1
                        yp = GlobalHWVar.gsy // 18 * 11.6
                    else:
                        voceMarcata += 1
                        yp = yp + GlobalHWVar.gpy * 1.5
                else:
                    if voceMarcata == 4 or voceMarcata == 5 or voceMarcata == 6:
                        if voceMarcataSottoMenu == 3:
                            voceMarcataSottoMenu -= 2
                            yp = GlobalHWVar.gsy // 18 * 8
                        else:
                            voceMarcataSottoMenu += 1
                            yp = yp + GlobalHWVar.gpy * 2
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))

                GenericFunc.messaggio("Diario", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                GenericFunc.messaggio("Oggetti speciali", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5.5, 55)
                GenericFunc.messaggio("Persone incontrate", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, 55)
                GenericFunc.messaggio("Nemici incontrati", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.5, 55)
                GenericFunc.messaggio("Guida tastiera", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.5, 55)
                GenericFunc.messaggio("Guida mouse", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, 55)
                GenericFunc.messaggio("Guida controller", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.5, 55)
            else:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5.6, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 10))
                if voceMarcataSottoMenu == 0:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2.5))
                if GlobalHWVar.mouseVisibile:
                    GenericFunc.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    GenericFunc.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    GenericFunc.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            if voceMarcataSottoMenu != 0:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xpv, ypv))
                if voceMarcata == 4 or voceMarcata == 5 or voceMarcata == 6:
                    GenericFunc.messaggio("Mod. movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7.9, 55)
                    GenericFunc.messaggio("Mod. interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9.9, 55)
                    GenericFunc.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11.9, 55)
                    if voceMarcata == 4:
                        if voceMarcataSottoMenu == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInGioco, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            GenericFunc.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 5.5, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 6.1), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 6.1), 2)
                            GenericFunc.messaggio("Cambia bersaglio inquadrato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 6.7, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 7.5), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 7.5), 2)
                            GenericFunc.messaggio("Deseleziona bersaglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 8.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8.9), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8.9), 2)
                            GenericFunc.messaggio(u"Modalità interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 9.5, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 10.3), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 10.3), 2)
                            GenericFunc.messaggio("Movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 11.5, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12.8), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12.8), 2)
                            GenericFunc.messaggio("Attiva o disattiva Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 13.4, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 14.2), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 14.2), 2)
                            GenericFunc.messaggio("Interagisci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 14.8, 35)
                        if voceMarcataSottoMenu == 2:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInGioco, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            GenericFunc.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 5.5, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 6.1), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 6.1), 2)
                            GenericFunc.messaggio("Punta sul prossimo bersaglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 6.7, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 7.5), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 7.5), 2)
                            GenericFunc.messaggio(u"Modalità movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 8.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8.9), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8.9), 2)
                            GenericFunc.messaggio("Inquadra bersaglio puntato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 9.5, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 10.3), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 10.3), 2)
                            GenericFunc.messaggio("Sposta puntatore", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 11.5, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12.8), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12.8), 2)
                            GenericFunc.messaggio("Attiva o disattiva Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 13.4, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 14.2), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 14.2), 2)
                            GenericFunc.messaggio("Attacca / Interagisci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 14.8, 35)
                        if voceMarcataSottoMenu == 3:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInMenu, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            GenericFunc.messaggio("Esci (dove specificato)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 6.9, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 7.5), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 7.5), 2)
                            GenericFunc.messaggio("Indietro / Esci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 8.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8.9), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8.9), 2)
                            GenericFunc.messaggio("Sposta puntatore", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 10.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 11.4), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 11.4), 2)
                            GenericFunc.messaggio("Cambia operazione (se consentito)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 12, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12.8), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12.8), 2)
                            GenericFunc.messaggio("Seleziona", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 13.4, 35)
                    if voceMarcata == 5:
                        if voceMarcataSottoMenu == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            GenericFunc.messaggio("Movimento (su casella libera) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 5.6, 35)
                            GenericFunc.messaggio("Interagisci (su casella interagibile) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 6.1, 35)
                            GenericFunc.messaggio("Attiva o disattiva Impo (su teleImpo) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 6.6, 35)
                            GenericFunc.messaggio("Menu (su stato personaggio) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 7.1, 35)
                            GenericFunc.messaggio(u"Modalità interazione (su stato nemico)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 7.6, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8.6), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8.6), 2)
                            GenericFunc.messaggio(u"Modalità interazione /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 9.9, 35)
                            GenericFunc.messaggio("Rimuovi selezione (su stato nemico)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 10.4, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12), 2)
                            GenericFunc.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 13.5, 35)
                        if voceMarcataSottoMenu == 2:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            GenericFunc.messaggio("Inquadra o attacca (su casella nemica) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 5.6, 35)
                            GenericFunc.messaggio("Interagisci (su casella interagibile) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 6.1, 35)
                            GenericFunc.messaggio("Attiva o disattiva Impo (su teleImpo) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 6.6, 35)
                            GenericFunc.messaggio("Menu (su stato personaggio) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 7.1, 35)
                            GenericFunc.messaggio(u"Modalità movimento (su stato nemico)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 7.6, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8.6), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8.6), 2)
                            GenericFunc.messaggio(u"Modalità movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 10.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12), 2)
                            GenericFunc.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 13.5, 35)
                        if voceMarcataSottoMenu == 3:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            GenericFunc.messaggio("Seleziona", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 6.6, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8.6), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8.6), 2)
                            GenericFunc.messaggio("Indietro / Esci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 10.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12), 2)
                            GenericFunc.messaggio("Cambia operazione (se consentito)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 13.5, 35)
                    if voceMarcata == 6:
                        if voceMarcataSottoMenu == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInGioco, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            GenericFunc.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 5.5, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 6.4), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 6.4), 2)
                            GenericFunc.messaggio("Cambia bersaglio inquadrato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 7.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8), 2)
                            GenericFunc.messaggio("Deseleziona bersaglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 8.65, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 9.55), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 9.55), 2)
                            GenericFunc.messaggio(u"Modalità interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 10.2, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 11.1), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 11.1), 2)
                            GenericFunc.messaggio("Movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 11.75, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12.65), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12.65), 2)
                            GenericFunc.messaggio("Attiva o disattiva Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 13.3, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 14.2), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 14.2), 2)
                            GenericFunc.messaggio("Interagisci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 14.9, 35)
                        if voceMarcataSottoMenu == 2:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInGioco, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            GenericFunc.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 5.5, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 6.4), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 6.4), 2)
                            GenericFunc.messaggio("Punta sul prossimo bersaglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 7.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8), 2)
                            GenericFunc.messaggio(u"Modalità movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 8.65, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 9.55), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 9.55), 2)
                            GenericFunc.messaggio("Inquadra bersaglio puntato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 10.2, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 11.1), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 11.1), 2)
                            GenericFunc.messaggio("Sposta puntatore", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 11.75, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12.65), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12.65), 2)
                            GenericFunc.messaggio("Attiva o disattiva Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 13.3, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 14.2), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 14.2), 2)
                            GenericFunc.messaggio("Attacca / Interagisci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 14.9, 35)
                        if voceMarcataSottoMenu == 3:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInMenu, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            GenericFunc.messaggio("Esci (dove specificato)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 7.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8), 2)
                            GenericFunc.messaggio("Indietro / Esci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 8.65, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 9.55), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 9.55), 2)
                            GenericFunc.messaggio("Sposta puntatore", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 10.2, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 11.1), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 11.1), 2)
                            GenericFunc.messaggio("Cambia operazione (se consentito)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 11.75, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12.65), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12.65), 2)
                            GenericFunc.messaggio("Seleziona", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 13.3, 35)

            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
