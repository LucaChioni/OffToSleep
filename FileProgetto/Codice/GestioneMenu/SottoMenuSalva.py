# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto
import Codice.FunzioniGeneriche.CaricaSalvaPartita as CaricaSalvaPartita
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche


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
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robograf2, (GlobalHWVar.gpx * 7, int(-GlobalHWVar.gpy * 4.45)))
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.nero, (GlobalHWVar.gpx * 10, int(GlobalHWVar.gpy * 13.5)), (GlobalHWVar.gpx * 22, int(GlobalHWVar.gpy * 13.5)), 2)
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)
                FunzioniGraficheGeneriche.messaggio("Slot di memoria vuoto...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 8.5, GlobalHWVar.gsy // 18 * 14, 100)
                GlobalHWVar.aggiornaSchermo()

            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
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
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robograf4, (GlobalHWVar.gpx * 7, -GlobalHWVar.gpy * 4.45))
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.nero, (GlobalHWVar.gpx * 10, int(GlobalHWVar.gpy * 13.5)), (GlobalHWVar.gpx * 22, int(GlobalHWVar.gpy * 13.5)), 2)
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)
                FunzioniGraficheGeneriche.messaggio("Slot di memoria danneggiato...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 6.5, GlobalHWVar.gsy // 18 * 14, 100)
                GlobalHWVar.aggiornaSchermo()

            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
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
                            FunzioniGraficheGeneriche.messaggio("Salvando...", GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 6.7) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 13.7, 80, centrale=True)
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
                            FunzioniGraficheGeneriche.messaggio("Cancellando...", GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 6.7) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 13.7, 80, centrale=True)
                            GlobalHWVar.aggiornaSchermo()
                            leggi = CaricaFileProgetto.loadFile("DatiSalvati/Salvataggi/Salvataggio%i.txt" % n, "w")
                            leggi.close()
                            leggi = CaricaFileProgetto.loadFile("DatiSalvati/Salvataggi/Salvataggio%i-backup.txt" % n, "w")
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
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
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
                    FunzioniGraficheGeneriche.messaggio("Carica partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                if cosa == 2:
                    FunzioniGraficheGeneriche.messaggio("Cancella partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                if cosa == 3:
                    FunzioniGraficheGeneriche.messaggio("Salva partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)

                contasalva = 1
                while contasalva <= len(GlobalGameVar.vetDatiSalvataggi):
                    vetTemp = GlobalGameVar.vetDatiSalvataggi[contasalva - 1]
                    dati = vetTemp[0]
                    errore = vetTemp[2]
                    if errore == 1:
                        FunzioniGraficheGeneriche.messaggio("Slot vuoto", GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 6.5) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 8.2, 60)
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
                            FunzioniGraficheGeneriche.messaggio("Livello: " + str(dati[4]), GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 8.3) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 11, 60, centrale=True)
                            GlobalHWVar.disegnaImmagineSuSchermo(arcsalva, ((GlobalHWVar.gpx * 5.8) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.5))
                            GlobalHWVar.disegnaImmagineSuSchermo(persalva, ((GlobalHWVar.gpx * 5.8) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.5))
                            GlobalHWVar.disegnaImmagineSuSchermo(persSalvaBraccia, ((GlobalHWVar.gpx * 5.8) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.5))
                            GlobalHWVar.disegnaImmagineSuSchermo(armsalva, ((GlobalHWVar.gpx * 5.8) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.5))
                            GlobalHWVar.disegnaImmagineSuSchermo(colsalva, ((GlobalHWVar.gpx * 5.8) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.5))
                            GlobalHWVar.disegnaImmagineSuSchermo(spasalva, ((GlobalHWVar.gpx * 5.8) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.5))
                            GlobalHWVar.disegnaImmagineSuSchermo(guasalva, ((GlobalHWVar.gpx * 5.8) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.5))
                            GlobalHWVar.disegnaImmagineSuSchermo(scusalva, ((GlobalHWVar.gpx * 5.8) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.5))
                        else:
                            FunzioniGraficheGeneriche.messaggio("Slot corrotto", GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 6.2) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 8.2, 60)
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
                        FunzioniGraficheGeneriche.messaggio("Tasto centrale: cancella partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 16.8, 50)
                    elif GlobalHWVar.usandoIlController:
                        FunzioniGraficheGeneriche.messaggio("Triangolo: cancella partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 16.8, 50)
                    else:
                        FunzioniGraficheGeneriche.messaggio("SHIFT: cancella partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 16.8, 50)
                if cosa == 2:
                    if possibileSalvare:
                        if GlobalHWVar.mouseVisibile:
                            FunzioniGraficheGeneriche.messaggio("Tasto centrale: salva partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 16.8, 50)
                        elif GlobalHWVar.usandoIlController:
                            FunzioniGraficheGeneriche.messaggio("Triangolo: salva partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 16.8, 50)
                        else:
                            FunzioniGraficheGeneriche.messaggio("SHIFT: salva partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 16.8, 50)
                    else:
                        if GlobalHWVar.mouseVisibile:
                            FunzioniGraficheGeneriche.messaggio("Tasto centrale: carica partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 16.8, 50)
                        elif GlobalHWVar.usandoIlController:
                            FunzioniGraficheGeneriche.messaggio("Triangolo: carica partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 16.8, 50)
                        else:
                            FunzioniGraficheGeneriche.messaggio("SHIFT: carica partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 16.8, 50)
                if cosa == 3:
                    if GlobalHWVar.mouseVisibile:
                        FunzioniGraficheGeneriche.messaggio("Tasto centrale: carica partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 16.8, 50)
                    elif GlobalHWVar.usandoIlController:
                        FunzioniGraficheGeneriche.messaggio("Triangolo: carica partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 16.8, 50)
                    else:
                        FunzioniGraficheGeneriche.messaggio("SHIFT: carica partita", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 16.8, 50)
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

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
                FunzioniGraficheGeneriche.messaggio("Confermi?", GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 4.5) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 13, 70)
                FunzioniGraficheGeneriche.messaggio(u"Sì", GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 4.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 14.5, 70)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gsx // 32 * 6.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3) - 1, GlobalHWVar.gsy // 18 * 14.3), ((GlobalHWVar.gsx // 32 * 6.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3) - 1, GlobalHWVar.gsy // 18 * 15.7), 2)
                FunzioniGraficheGeneriche.messaggio("No", GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 7.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 14.5, 70)
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (vxp, vyp))

            primoFrame = False
            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
