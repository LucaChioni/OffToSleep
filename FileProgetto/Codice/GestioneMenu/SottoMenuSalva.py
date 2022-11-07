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
import Codice.SettaggiLivelli.SetImgOggettiMappaPersonaggi as SetImgOggettiMappaPersonaggi
import Codice.Localizzazione.LocalizInterfaccia as LI


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
        # print ("Slot vuoto")
        aggiornaSchermata = True
        bottoneDown = False
        aggiornaInterfacciaPerCambioInput = True
        indietro = False
        while not indietro:
            xMouse, yMouse = pygame.mouse.get_pos()
            if GlobalHWVar.mouseVisibile:
                if GlobalHWVar.gsx // 32 * 22.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)

            # gestione degli input
            bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
            if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["Q"] or bottoneDown == "mouseDestro" or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCerchio":
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
                    FunzioniGraficheGeneriche.messaggio(LI.TAS_DES_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio(LI.B_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio(LI.Q_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                FunzioniGraficheGeneriche.messaggio(LI.SLO_DI_MEM_VUO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 14, 100, centrale=True)
                GlobalHWVar.aggiornaSchermo()

            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    if errore == 2:
        # print ("Dati corrotti")
        aggiornaSchermata = True
        bottoneDown = False
        aggiornaInterfacciaPerCambioInput = True
        indietro = False
        while not indietro:
            xMouse, yMouse = pygame.mouse.get_pos()
            if GlobalHWVar.mouseVisibile:
                if GlobalHWVar.gsx // 32 * 22.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)

            # gestione degli input
            bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
            if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["Q"] or bottoneDown == "mouseDestro" or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCerchio":
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
                    FunzioniGraficheGeneriche.messaggio(LI.TAS_DES_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio(LI.B_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio(LI.Q_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                FunzioniGraficheGeneriche.messaggio(LI.SLO_DI_MEM_DAN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 14, 100, centrale=True)
                GlobalHWVar.aggiornaSchermo()

            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def scegli_sal(possibileSalvare, lunghezzadati, lunghezzadatiPorte, lunghezzadatiCofanetti, porteAttuali, cofanettiAttuali, vitaescaAttuali, vettoreDenaroAttuali, datiAttuali, listaNemiciTotaliAttuali, stanzeGiaVisitateAttuali, listaPersonaggiTotaliAttuali, listaAvanzamentoDialoghi, oggettiRimastiAHansAttuali, ultimoObbiettivoColco, obbiettivoCasualeColco, fineDelGioco=False):
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
    confermaSalvataggioCancellazione = False

    primissimoFrame = True

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
                if GlobalHWVar.gsx // 32 * 22.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2 and not fineDelGioco:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    suTornaIndietro = True
                elif 0 <= xMouse <= GlobalHWVar.gsx // 32 * 10 and GlobalHWVar.gsy // 18 * 16.2 <= yMouse <= GlobalHWVar.gsy and not fineDelGioco:
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
                if GlobalHWVar.gsx // 32 * 22.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    suTornaIndietro = True
                elif 0 <= xMouse <= GlobalHWVar.gsx // 32 * 10 and GlobalHWVar.gsy // 18 * 16.2 <= yMouse <= GlobalHWVar.gsy:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    suCambiaOperazione = True
                elif GlobalHWVar.gsy // 18 * 14.1 <= yMouse <= GlobalHWVar.gsy // 18 * 16:
                    if (GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3) <= xMouse <= (GlobalHWVar.gsx // 32 * 6.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3):
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 1
                        xp = (GlobalHWVar.gsx // 32 * 3.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3)
                        yp = GlobalHWVar.gsy // 18 * 14.8
                    elif (GlobalHWVar.gsx // 32 * 6.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3) <= xMouse <= (GlobalHWVar.gsx // 32 * 11.3) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3):
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 2
                        xp = (GlobalHWVar.gsx // 32 * 6.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3)
                        yp = GlobalHWVar.gsy // 18 * 14.8
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
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["Q"] or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            if conferma:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                xp = vxp
                yp = vyp
                conferma = False
            elif not fineDelGioco:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                n = -1
                return n, cosa
            else:
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False
        if (bottoneDown == pygame.K_LSHIFT or bottoneDown == pygame.K_RSHIFT or bottoneDown == "mouseCentrale" or bottoneDown == "padTriangolo") and not fineDelGioco:
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
            if bottoneDown == "mouseSinistro" and suTornaIndietro and not fineDelGioco:
                if conferma:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    xp = vxp
                    yp = vyp
                    conferma = False
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    n = -1
                    return n, cosa
            elif bottoneDown == "mouseSinistro" and suCambiaOperazione and not fineDelGioco:
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
                            FunzioniGraficheGeneriche.messaggio(LI.SALVANDO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 6.7) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 13.7, 80, centrale=True)
                            GlobalHWVar.aggiornaSchermo()
                            datiAttualiTotali = [datiAttuali, porteAttuali, cofanettiAttuali, listaNemiciTotaliAttuali, vitaescaAttuali, vettoreDenaroAttuali, stanzeGiaVisitateAttuali, listaPersonaggiTotaliAttuali, listaAvanzamentoDialoghi, oggettiRimastiAHansAttuali, ultimoObbiettivoColco, obbiettivoCasualeColco]
                            datiGameoverTotali = [GlobalGameVar.vetDatiSalvataggioGameOver[0], GlobalGameVar.vetDatiSalvataggioGameOver[1], GlobalGameVar.vetDatiSalvataggioGameOver[2], GlobalGameVar.vetDatiSalvataggioGameOver[3], GlobalGameVar.vetDatiSalvataggioGameOver[4], GlobalGameVar.vetDatiSalvataggioGameOver[5], GlobalGameVar.vetDatiSalvataggioGameOver[6], GlobalGameVar.vetDatiSalvataggioGameOver[7], GlobalGameVar.vetDatiSalvataggioGameOver[8], GlobalGameVar.vetDatiSalvataggioGameOver[9], GlobalGameVar.vetDatiSalvataggioGameOver[10], GlobalGameVar.vetDatiSalvataggioGameOver[11]]
                            CaricaSalvaPartita.salvataggio(n, datiAttualiTotali, datiGameoverTotali)
                            GlobalGameVar.numSalvataggioCaricato = n
                            # ricarico il salvataggio
                            ricaricaSalvataggi(lunghezzadati, lunghezzadatiPorte, lunghezzadatiCofanetti, numSalvataggio=n)
                            confermaSalvataggioCancellazione = 1

                            xp = vxp
                            yp = vyp
                            conferma = False
                            primoFrame = True
                        elif cosa == 2:
                            GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.rossoScuroPiuScuro, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 12.5, GlobalHWVar.gsx // 32 * 9.3, GlobalHWVar.gsy // 18 * 3.5))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.rossoScuroPiuScuro, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 12.5) - 1), ((GlobalHWVar.gsx // 32 * 11.3) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 12.5) - 1), 2)
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 15))
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, ((GlobalHWVar.gsx // 32 * 10.3) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 15))
                            FunzioniGraficheGeneriche.messaggio(LI.CANCELLANDO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 6.7) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 13.7, 80, centrale=True)
                            GlobalHWVar.aggiornaSchermo()
                            leggi = CaricaFileProgetto.loadFile("DatiSalvati/Salvataggi/Salvataggio%i.txt" % n, "w")
                            leggi.close()
                            leggi = CaricaFileProgetto.loadFile("DatiSalvati/Salvataggi/Salvataggio%i-backup.txt" % n, "w")
                            leggi.close()
                            # ricarico il salvataggio
                            ricaricaSalvataggi(lunghezzadati, lunghezzadatiPorte, lunghezzadatiCofanetti, numSalvataggio=n)
                            confermaSalvataggioCancellazione = 2

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
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["D"] or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["A"] or bottoneDown == "padDestra" or bottoneDown == "padSinistra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or salMarcatoVecchio != salMarcato or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["A"] or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
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
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["D"] or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
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
                FunzioniGraficheGeneriche.messaggio("1", GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 1.8, GlobalHWVar.gsy // 18 * 3.1, 600)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gsx // 32 * 11.3) - 1, GlobalHWVar.gsy // 18 * 5), ((GlobalHWVar.gsx // 32 * 11.3) - 1, GlobalHWVar.gsy // 18 * 12), 2)
                FunzioniGraficheGeneriche.messaggio("2", GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 11.1, GlobalHWVar.gsy // 18 * 3.1, 600)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gsx // 32 * 20.6) - 1, GlobalHWVar.gsy // 18 * 5), ((GlobalHWVar.gsx // 32 * 20.6) - 1, GlobalHWVar.gsy // 18 * 12), 2)
                FunzioniGraficheGeneriche.messaggio("3", GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 20.4, GlobalHWVar.gsy // 18 * 3.1, 600)
                if cosa == 1:
                    FunzioniGraficheGeneriche.messaggio(LI.CARICA_PARTITA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                if cosa == 2:
                    FunzioniGraficheGeneriche.messaggio(LI.CANCELLA_PARTITA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                if cosa == 3:
                    FunzioniGraficheGeneriche.messaggio(LI.SALVA_PARTITA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)

                contasalva = 1
                while contasalva <= len(GlobalGameVar.vetDatiSalvataggi):
                    vetTemp = GlobalGameVar.vetDatiSalvataggi[contasalva - 1]
                    dati = vetTemp[0]
                    errore = vetTemp[2]
                    if errore == 1:
                        FunzioniGraficheGeneriche.messaggio(LI.SLOT_VUOTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 8.6) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 8, 60, centrale=True)
                    else:
                        if not errore:
                            persalva, persSalvaBraccia = SetImgOggettiMappaPersonaggi.setImgMenuSalvaProtagonista(dati[0], dati[144])

                            spasalva = GlobalImgVar.vetImgSpadePixellate[dati[6]]
                            arcsalva = GlobalImgVar.vetImgArchiPixellate[dati[128]]
                            armsalva = GlobalImgVar.vetImgArmaturePixellate[dati[8]]
                            scusalva = GlobalImgVar.vetImgScudiPixellate[dati[7]]
                            guasalva = GlobalImgVar.vetImgGuantiPixellate[dati[129]]
                            colsalva = GlobalImgVar.vetImgCollanePixellate[dati[130]]
                            FunzioniGraficheGeneriche.messaggio(LI.LIVELLO_[GlobalHWVar.linguaImpostata] + str(dati[4]), GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 8.6) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 10.4, 60, centrale=True)
                            tempoGioco_secondi = dati[146]
                            hours = str(int(tempoGioco_secondi // 3600)).zfill(2)
                            minutes = str(int((tempoGioco_secondi % 3600) // 60)).zfill(2)
                            seconds = str(int(tempoGioco_secondi % 60)).zfill(2)
                            tempoGioco = str(hours) + ":" + str(minutes) + ":" + str(seconds)
                            FunzioniGraficheGeneriche.messaggio(tempoGioco, GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 8.6) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 11.2, 60, centrale=True)
                            GlobalHWVar.disegnaImmagineSuSchermo(arcsalva, ((GlobalHWVar.gpx * 6.1) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.1))
                            GlobalHWVar.disegnaImmagineSuSchermo(persalva, ((GlobalHWVar.gpx * 6.1) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.1))
                            GlobalHWVar.disegnaImmagineSuSchermo(persSalvaBraccia, ((GlobalHWVar.gpx * 6.1) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.1))
                            GlobalHWVar.disegnaImmagineSuSchermo(armsalva, ((GlobalHWVar.gpx * 6.1) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.1))
                            GlobalHWVar.disegnaImmagineSuSchermo(colsalva, ((GlobalHWVar.gpx * 6.1) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.1))
                            GlobalHWVar.disegnaImmagineSuSchermo(spasalva, ((GlobalHWVar.gpx * 6.1) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.1))
                            GlobalHWVar.disegnaImmagineSuSchermo(guasalva, ((GlobalHWVar.gpx * 6.1) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.1))
                            GlobalHWVar.disegnaImmagineSuSchermo(scusalva, ((GlobalHWVar.gpx * 6.1) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gpy * 5.1))
                        else:
                            FunzioniGraficheGeneriche.messaggio(LI.SLOT_CORROTTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 8.6) + ((contasalva - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 8, 60, centrale=True)
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
            if aggiornaInterfacciaPerCambioInput and not fineDelGioco:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (0, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2))
                if cosa == 1:
                    if GlobalHWVar.mouseVisibile:
                        FunzioniGraficheGeneriche.messaggio(LI.TAS_CEN_CAN_PAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 16.8, 50, centrale=True)
                    elif GlobalHWVar.usandoIlController:
                        FunzioniGraficheGeneriche.messaggio(LI.Y_CAN_PAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 16.8, 50, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio(LI.SHI_CAN_PAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 16.8, 50, centrale=True)
                if cosa == 2:
                    if possibileSalvare:
                        if GlobalHWVar.mouseVisibile:
                            FunzioniGraficheGeneriche.messaggio(LI.TAS_CEN_SAL_PAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 16.8, 50, centrale=True)
                        elif GlobalHWVar.usandoIlController:
                            FunzioniGraficheGeneriche.messaggio(LI.Y_SAL_PAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 16.8, 50, centrale=True)
                        else:
                            FunzioniGraficheGeneriche.messaggio(LI.SHI_SAL_PAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 16.8, 50, centrale=True)
                    else:
                        if GlobalHWVar.mouseVisibile:
                            FunzioniGraficheGeneriche.messaggio(LI.TAS_CEN_CAR_PAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 16.8, 50, centrale=True)
                        elif GlobalHWVar.usandoIlController:
                            FunzioniGraficheGeneriche.messaggio(LI.Y_CAR_PAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 16.8, 50, centrale=True)
                        else:
                            FunzioniGraficheGeneriche.messaggio(LI.SHI_CAR_PAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 16.8, 50, centrale=True)
                if cosa == 3:
                    if GlobalHWVar.mouseVisibile:
                        FunzioniGraficheGeneriche.messaggio(LI.TAS_CEN_CAR_PAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 16.8, 50, centrale=True)
                    elif GlobalHWVar.usandoIlController:
                        FunzioniGraficheGeneriche.messaggio(LI.Y_CAR_PAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 16.8, 50, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio(LI.SHI_CAR_PAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 16.8, 50, centrale=True)
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio(LI.TAS_DES_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio(LI.B_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio(LI.Q_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)

            if conferma:
                if primaconf:
                    vxp = xp
                    vyp = yp
                    xp = (GlobalHWVar.gsx // 32 * 6.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3)
                    yp = GlobalHWVar.gsy // 18 * 14.8
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
                FunzioniGraficheGeneriche.messaggio(LI.CONFERMI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 6.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 12.9, 70, centrale=True)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gsx // 32 * 2.5) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 14.1) - 1), ((GlobalHWVar.gsx // 32 * 10.75) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 14.1) - 1), 2)
                FunzioniGraficheGeneriche.messaggio(LI.SI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 5.1) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 14.6, 70, centrale=True)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gsx // 32 * 6.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3) - 1, GlobalHWVar.gsy // 18 * 14.4), ((GlobalHWVar.gsx // 32 * 6.6) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3) - 1, GlobalHWVar.gsy // 18 * 15.7), 2)
                FunzioniGraficheGeneriche.messaggio(LI.NO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 8.1) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 14.6, 70, centrale=True)
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (vxp, vyp))
            elif confermaSalvataggioCancellazione:
                if confermaSalvataggioCancellazione == 1:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.verdeScuroPiuScuro, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 12.5, GlobalHWVar.gsx // 32 * 9.3, GlobalHWVar.gsy // 18 * 3.5))
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.verdeScuroPiuScuro, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 12.5) - 1), ((GlobalHWVar.gsx // 32 * 11.3) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 12.5) - 1), 2)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 15))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, ((GlobalHWVar.gsx // 32 * 10.3) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 15))
                    FunzioniGraficheGeneriche.messaggio(LI.SALVATO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 6.7) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 13.7, 80, centrale=True)
                elif confermaSalvataggioCancellazione == 2:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.rossoScuroPiuScuro, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 12.5, GlobalHWVar.gsx // 32 * 9.3, GlobalHWVar.gsy // 18 * 3.5))
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.rossoScuroPiuScuro, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 12.5) - 1), ((GlobalHWVar.gsx // 32 * 11.3) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), (GlobalHWVar.gsy // 18 * 12.5) - 1), 2)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, ((GlobalHWVar.gsx // 32 * 2) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 15))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, ((GlobalHWVar.gsx // 32 * 10.3) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 15))
                    FunzioniGraficheGeneriche.messaggio(LI.CANCELLATO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 6.7) + ((salMarcato - 1) * GlobalHWVar.gsx // 32 * 9.3), GlobalHWVar.gsy // 18 * 13.7, 80, centrale=True)
                GlobalHWVar.aggiornaSchermo()
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                rispostaSottoMenu = False
                bottoneDownSottoMenu = False
                while not rispostaSottoMenu:
                    # gestione degli input
                    bottoneDownSottoMenu, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDownSottoMenu, False)
                    if bottoneDownSottoMenu == pygame.K_SPACE or bottoneDownSottoMenu == GlobalHWVar.tastiConfiguratiTastiera["Q"] or bottoneDownSottoMenu == "mouseSinistro" or bottoneDownSottoMenu == "mouseDestro" or bottoneDownSottoMenu == "padCroce" or bottoneDownSottoMenu == "padCerchio":
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        rispostaSottoMenu = True
                        bottoneDownSottoMenu = False
                    if bottoneDownSottoMenu:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        bottoneDownSottoMenu = False
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
                confermaSalvataggioCancellazione = False
                aggiornaSchermo = True
                if fineDelGioco:
                    risposta = True

            if primissimoFrame and fineDelGioco:
                GlobalHWVar.nonAggiornareSchermo = False
                imgOscuramentoSchermo = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
                screen = GlobalHWVar.schermo.copy().convert()
                i = 0
                while i <= 50:
                    GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                    imgOscuramentoSchermo.fill((0, 0, 0, 255 - (i * 5)))
                    GlobalHWVar.disegnaImmagineSuSchermo(imgOscuramentoSchermo, (0, 0))
                    GlobalHWVar.aggiornaSchermo()
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                    i += 1
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                GlobalHWVar.aggiornaSchermo()

            primissimoFrame = False
            primoFrame = False
            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
