# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche


def mostraEnigma(tipoPersonaggio):
    FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False)

    if tipoPersonaggio == "OggettoEnigmaBiblioteca":
        enigmaBiblioteca()
    elif tipoPersonaggio == "OggettoEnigmaLabirinto":
        enigmaLabirinto()


def enigmaBiblioteca():
    GlobalHWVar.canaleSoundPassiRallo.stop()
    GenericFunc.cambiaVolumeCanale(GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.volumeEffetti / 2)

    primoframe = True
    esci = False
    bottoneDown = False
    primoFrame = True
    fattoCLickSulFoglio = False
    cambiatoStrumento = True
    aggiornaInterfacciaPerCambioInput = False

    cursoreSulFoglio = True
    cursoreSuTornaIndietro = False
    cursoreSuCancellaTutto = False
    strumentoMarcato = False
    cancellaTutto = False
    xInizioFoglio = GlobalHWVar.gpx * 1
    xFineFoglio = GlobalHWVar.gpx * 31
    yInizioFoglio = GlobalHWVar.gpy * 5
    yFineFoglio = GlobalHWVar.gpy * 17
    strumentoInUso = "matita"
    xStrumento = GlobalHWVar.gpx * 16
    yStrumento = GlobalHWVar.gpy * 9
    xStrumentoVecchia = xStrumento
    yStrumentoVecchia = yStrumento
    dimensioneTrattoMatita = GlobalHWVar.gpx // 10
    dimensioneTrattoGomma = GlobalHWVar.gpx // 3
    unitaSpostamentoCursore = GlobalHWVar.gpx // 15

    # carico tutte le img necessarie per questo "menu"
    pathImgEnigma = "Risorse/Immagini/DecorazioniMenu/SchermateEnigmi/EnigmaBiblioteca/"
    cursoreMatita = CaricaFileProgetto.loadImage(pathImgEnigma + "CursoreMatita.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, True, True)
    cursoreGomma = CaricaFileProgetto.loadImage(pathImgEnigma + "CursoreGomma.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, True, True)
    sfondoUsandoMatita = CaricaFileProgetto.loadImage(pathImgEnigma + "Schermata-usandoMatita.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False, True)
    sfondoUsandoGomma = CaricaFileProgetto.loadImage(pathImgEnigma + "Schermata-usandoGomma.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False, True)
    if GlobalGameVar.datiEnigmaBibliotecario["velocità"] == 1:
        imgDatiVel = CaricaFileProgetto.loadImage(pathImgEnigma + "Schermata-vel1.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False, True)
    elif GlobalGameVar.datiEnigmaBibliotecario["velocità"] == 2:
        imgDatiVel = CaricaFileProgetto.loadImage(pathImgEnigma + "Schermata-vel2.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False, True)
    elif GlobalGameVar.datiEnigmaBibliotecario["velocità"] == 3:
        imgDatiVel = CaricaFileProgetto.loadImage(pathImgEnigma + "Schermata-vel3.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False, True)
    elif GlobalGameVar.datiEnigmaBibliotecario["velocità"] == 4:
        imgDatiVel = CaricaFileProgetto.loadImage(pathImgEnigma + "Schermata-vel4.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False, True)
    elif GlobalGameVar.datiEnigmaBibliotecario["velocità"] == 5:
        imgDatiVel = CaricaFileProgetto.loadImage(pathImgEnigma + "Schermata-vel5.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False, True)
    else:
        imgDatiVel = False

    GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
    GlobalHWVar.disegnaImmagineSuSchermo(sfondoUsandoMatita, (0, 0))
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.gialloCarta, (0, yInizioFoglio - GlobalHWVar.gpy, GlobalHWVar.gsx, GlobalHWVar.gsy - GlobalHWVar.gpy * 4))
    sfondoEnigma = GlobalHWVar.schermo.copy().convert()
    superficieDisegni = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)

    while not esci:
        spostandoCursore = False
        utilizzandoStrumento = False

        if GlobalHWVar.mouseVisibile:
            xMouse, yMouse = pygame.mouse.get_pos()
            cursoreSuTornaIndietro = False
            cursoreSuCancellaTutto = False
            strumentoMarcato = False
            if xInizioFoglio - GlobalHWVar.gpx <= xMouse <= xFineFoglio + GlobalHWVar.gpx and yInizioFoglio - GlobalHWVar.gpy <= yMouse <= yFineFoglio + GlobalHWVar.gpy:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSulFoglio = True
                xStrumento = xMouse
                yStrumento = yMouse
                if xStrumento < xInizioFoglio:
                    xStrumento = xInizioFoglio
                elif xStrumento > xFineFoglio:
                    xStrumento = xFineFoglio
                if yStrumento < yInizioFoglio:
                    yStrumento = yInizioFoglio
                elif yStrumento > yFineFoglio:
                    yStrumento = yFineFoglio
                if xStrumentoVecchia != xStrumento or yStrumentoVecchia != yStrumento:
                    spostandoCursore = True
            else:
                cursoreSulFoglio = False
                if 0 <= yMouse <= GlobalHWVar.gpy * 2 and GlobalHWVar.gpx * 21.5 <= xMouse <= GlobalHWVar.gpx * 32:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    cursoreSuTornaIndietro = True
                elif GlobalHWVar.gpy * 2 <= yMouse <= GlobalHWVar.gpy * 4 and GlobalHWVar.gpx * 21.5 <= xMouse <= GlobalHWVar.gpx * 32:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    cursoreSuCancellaTutto = True
                elif 0 <= yMouse <= GlobalHWVar.gpy * 4 and 0 <= xMouse <= GlobalHWVar.gpx * 6 and strumentoInUso != "matita":
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    strumentoMarcato = "matita"
                elif 0 <= yMouse <= GlobalHWVar.gpy * 4 and GlobalHWVar.gpx * 6 <= xMouse <= GlobalHWVar.gpx * 12 and strumentoInUso != "gomma":
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    strumentoMarcato = "gomma"
                elif not GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(True)

        # gestione degli input
        if not primoframe:
            aggiornaInterfacciaPerCambioInput = False
            bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            esci = True
            bottoneDown = False
        if pygame.K_w in GlobalHWVar.listaTastiPremuti or "padSu" in GlobalHWVar.listaTastiPremuti:
            spostandoCursore = True
            yStrumento -= unitaSpostamentoCursore
            if yStrumento < yInizioFoglio:
                yStrumento = yInizioFoglio
        if pygame.K_a in GlobalHWVar.listaTastiPremuti or "padSinistra" in GlobalHWVar.listaTastiPremuti:
            spostandoCursore = True
            xStrumento -= unitaSpostamentoCursore
            if xStrumento < xInizioFoglio:
                xStrumento = xInizioFoglio
        if pygame.K_s in GlobalHWVar.listaTastiPremuti or "padGiu" in GlobalHWVar.listaTastiPremuti:
            spostandoCursore = True
            yStrumento += unitaSpostamentoCursore
            if yStrumento > yFineFoglio:
                yStrumento = yFineFoglio
        if pygame.K_d in GlobalHWVar.listaTastiPremuti or "padDestra" in GlobalHWVar.listaTastiPremuti:
            spostandoCursore = True
            xStrumento += unitaSpostamentoCursore
            if xStrumento > xFineFoglio:
                xStrumento = xFineFoglio
        if bottoneDown == pygame.K_2 or bottoneDown == pygame.K_KP2 or bottoneDown == "padL1":
            if strumentoInUso != "matita":
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                strumentoInUso = "matita"
                cambiatoStrumento = True
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if bottoneDown == pygame.K_3 or bottoneDown == pygame.K_KP3 or bottoneDown == "padR1":
            if strumentoInUso != "gomma":
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                strumentoInUso = "gomma"
                cambiatoStrumento = True
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if bottoneDown == pygame.K_LSHIFT or bottoneDown == pygame.K_RSHIFT or bottoneDown == "mouseCentrale" or bottoneDown == "padTriangolo":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.rumoreCancellaTuttoEnigmi)
            cancellaTutto = True
            bottoneDown = False
        if not aggiornaInterfacciaPerCambioInput and (pygame.K_SPACE in GlobalHWVar.listaTastiPremuti or (cursoreSulFoglio and "mouseSinistro" in GlobalHWVar.listaTastiPremuti) or (not cursoreSulFoglio and bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or "padCroce" in GlobalHWVar.listaTastiPremuti):
            if (GlobalHWVar.mouseVisibile and cursoreSulFoglio) or pygame.K_SPACE in GlobalHWVar.listaTastiPremuti or "padCroce" in GlobalHWVar.listaTastiPremuti:
                if GlobalHWVar.mouseVisibile and bottoneDown == "mouseSinistro" and cursoreSulFoglio:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAppoggioStrumentoEnigmi)
                    fattoCLickSulFoglio = True
                    utilizzandoStrumento = True
                elif GlobalHWVar.mouseVisibile and "mouseSinistro" in GlobalHWVar.listaTastiPremuti and cursoreSulFoglio and fattoCLickSulFoglio:
                    utilizzandoStrumento = True
                elif not GlobalHWVar.mouseVisibile and (bottoneDown == pygame.K_SPACE or bottoneDown == "padCroce"):
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAppoggioStrumentoEnigmi)
                    fattoCLickSulFoglio = True
                    utilizzandoStrumento = True
                elif not GlobalHWVar.mouseVisibile and (pygame.K_SPACE in GlobalHWVar.listaTastiPremuti or "padCroce" in GlobalHWVar.listaTastiPremuti) and fattoCLickSulFoglio:
                    utilizzandoStrumento = True
            else:
                if cursoreSuTornaIndietro:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    esci = True
                elif cursoreSuCancellaTutto:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.rumoreCancellaTuttoEnigmi)
                    cancellaTutto = True
                elif strumentoMarcato == "matita":
                    if strumentoInUso != "matita":
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        strumentoInUso = "matita"
                        cambiatoStrumento = True
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif strumentoMarcato == "gomma":
                    if strumentoInUso != "gomma":
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        strumentoInUso = "gomma"
                        cambiatoStrumento = True
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if GlobalHWVar.mouseVisibile and not "mouseSinistro" in GlobalHWVar.listaTastiPremuti:
            fattoCLickSulFoglio = False
        elif not GlobalHWVar.mouseVisibile and not (pygame.K_SPACE in GlobalHWVar.listaTastiPremuti or "padCroce" in GlobalHWVar.listaTastiPremuti):
            fattoCLickSulFoglio = False

        if utilizzandoStrumento:
            if not GlobalHWVar.canaleSoundInterazioni.get_busy():
                if strumentoInUso == "matita":
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreScorrimentoMatitaEnigmi, -1)
                elif strumentoInUso == "gomma":
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreScorrimentoGommaEnigmi, -1)
        else:
            GlobalHWVar.canaleSoundInterazioni.stop()

        if utilizzandoStrumento or spostandoCursore or primoFrame or cambiatoStrumento or cancellaTutto or aggiornaInterfacciaPerCambioInput:
            if primoFrame or aggiornaInterfacciaPerCambioInput or cancellaTutto or cambiatoStrumento:
                if primoFrame or cancellaTutto:
                    superficieDisegni = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
                if strumentoInUso == "matita":
                    GlobalHWVar.disegnaImmagineSuSchermo(sfondoUsandoMatita, (0, 0))
                elif strumentoInUso == "gomma":
                    GlobalHWVar.disegnaImmagineSuSchermo(sfondoUsandoGomma, (0, 0))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.gialloCarta, (0, yInizioFoglio - GlobalHWVar.gpy, GlobalHWVar.gsx, GlobalHWVar.gsy - GlobalHWVar.gpy * 4))
                if imgDatiVel:
                    GlobalHWVar.disegnaImmagineSuSchermo(imgDatiVel, (0, 0))
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                    FunzioniGraficheGeneriche.messaggio("Tasto centrale: cancella tutto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.3, GlobalHWVar.gsy // 18 * 2.5, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("L1:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 0.5, 60)
                    FunzioniGraficheGeneriche.messaggio("R1:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 6.5, GlobalHWVar.gsy // 18 * 0.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.1, GlobalHWVar.gsy // 18 * 1, 50)
                    FunzioniGraficheGeneriche.messaggio("Triangolo: cancella tutto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.9, GlobalHWVar.gsy // 18 * 2.5, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("2:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 0.5, 60)
                    FunzioniGraficheGeneriche.messaggio("3:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 6.5, GlobalHWVar.gsy // 18 * 0.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.8, GlobalHWVar.gsy // 18 * 1, 50)
                    FunzioniGraficheGeneriche.messaggio("SHIFT: cancella tutto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.3, GlobalHWVar.gsy // 18 * 2.5, 50)
                sfondoEnigma = GlobalHWVar.schermo.copy().convert()

            dimXBackground = GlobalHWVar.gpx * 2
            dimYBackground = GlobalHWVar.gpy * 2
            if xStrumentoVecchia + dimXBackground >= GlobalHWVar.gsx:
                dimXBackground = GlobalHWVar.gsx - xStrumentoVecchia
            if yStrumentoVecchia < 0:
                yStrumentoVecchia = 0
            backgroundStrumento = sfondoEnigma.subsurface(pygame.Rect(xStrumentoVecchia, yStrumentoVecchia - GlobalHWVar.gpy * 2, dimXBackground, dimYBackground))
            GlobalHWVar.disegnaImmagineSuSchermo(backgroundStrumento, (xStrumentoVecchia, yStrumentoVecchia - GlobalHWVar.gpy * 2))

            if utilizzandoStrumento:
                if strumentoInUso == "matita":
                    if xStrumentoVecchia == xStrumento and yStrumentoVecchia == yStrumento:
                        GlobalHWVar.disegnaCerchioSuSchermo(superficieDisegni, GlobalHWVar.grigioscuPiuScu, (xStrumento, yStrumento), dimensioneTrattoMatita // 2)
                    else:
                        GlobalHWVar.disegnaLineaSuSchermo(superficieDisegni, GlobalHWVar.grigioscuPiuScu, (xStrumentoVecchia, yStrumentoVecchia), (xStrumento, yStrumento), dimensioneTrattoMatita)
                elif strumentoInUso == "gomma":
                    if xStrumentoVecchia == xStrumento and yStrumentoVecchia == yStrumento:
                        GlobalHWVar.disegnaCerchioSuSchermo(superficieDisegni, GlobalHWVar.gialloCarta, (xStrumento, yStrumento), dimensioneTrattoGomma // 2)
                    else:
                        GlobalHWVar.disegnaLineaSuSchermo(superficieDisegni, GlobalHWVar.gialloCarta, (xStrumentoVecchia, yStrumentoVecchia), (xStrumento, yStrumento), dimensioneTrattoGomma)
            GlobalHWVar.disegnaImmagineSuSchermo(superficieDisegni, (0, 0))
            if strumentoInUso == "matita":
                GlobalHWVar.disegnaImmagineSuSchermo(cursoreMatita, (xStrumento, yStrumento - GlobalHWVar.gpy * 2))
            elif strumentoInUso == "gomma":
                GlobalHWVar.disegnaImmagineSuSchermo(cursoreGomma, (xStrumento, yStrumento - GlobalHWVar.gpy * 2))

            xStrumentoVecchia = xStrumento
            yStrumentoVecchia = yStrumento
            cancellaTutto = False
            cambiatoStrumento = False

            if primoFrame:
                FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=1)
            else:
                GlobalHWVar.aggiornaSchermo()
            primoFrame = False

        primoframe = False
        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockDisegno.tick(GlobalHWVar.fpsDisegno)
    GenericFunc.cambiaVolumeCanale(GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.volumeEffetti)
    GlobalHWVar.configuraCursore(False)


def enigmaLabirinto():
    GlobalHWVar.canaleSoundPassiRallo.stop()
    GenericFunc.cambiaVolumeCanale(GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.volumeEffetti / 2)

    primoframe = True
    esci = False
    bottoneDown = False
    primoFrame = True
    fattoCLickSulFoglio = False
    cambiatoStrumento = True
    aggiornaInterfacciaPerCambioInput = False

    cursoreSulFoglio = True
    cursoreSuTornaIndietro = False
    cursoreSuCancellaTutto = False
    strumentoMarcato = False
    cancellaTutto = False
    xInizioFoglio = GlobalHWVar.gpx * 1
    xFineFoglio = GlobalHWVar.gpx * 31
    yInizioFoglio = GlobalHWVar.gpy * 5
    yFineFoglio = GlobalHWVar.gpy * 17
    strumentoInUso = "matita"
    xStrumento = GlobalHWVar.gpx * 16
    yStrumento = GlobalHWVar.gpy * 9
    xStrumentoVecchia = xStrumento
    yStrumentoVecchia = yStrumento
    dimensioneTrattoMatita = GlobalHWVar.gpx // 10
    dimensioneTrattoGomma = GlobalHWVar.gpx // 3
    unitaSpostamentoCursore = GlobalHWVar.gpx // 15
    coloreMatita = (183, 117, 81)
    coloreGomma = (154, 95, 63)

    # carico tutte le img necessarie per questo "menu"
    pathImgEnigma = "Risorse/Immagini/DecorazioniMenu/SchermateEnigmi/EnigmaLabirinto/"
    cursoreMatita = CaricaFileProgetto.loadImage(pathImgEnigma + "CursoreMatita.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, True, True)
    cursoreGomma = CaricaFileProgetto.loadImage(pathImgEnigma + "CursoreGomma.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, True, True)
    imgComandiUsandoMatita = CaricaFileProgetto.loadImage(pathImgEnigma + "Schermata-usandoMatita.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False, True)
    imgComandiUsandoGomma = CaricaFileProgetto.loadImage(pathImgEnigma + "Schermata-usandoGomma.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False, True)
    sfondoUsandoMatita = CaricaFileProgetto.loadImage(pathImgEnigma + "SchermataMappa.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False, True)
    sfondoUsandoGomma = CaricaFileProgetto.loadImage(pathImgEnigma + "SchermataMappa.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False, True)
    GlobalHWVar.disegnaImmagineSuSchermo(imgComandiUsandoMatita, (0, 0), superficie=sfondoUsandoMatita)
    GlobalHWVar.disegnaImmagineSuSchermo(imgComandiUsandoGomma, (0, 0), superficie=sfondoUsandoGomma)

    GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, coloreGomma)
    GlobalHWVar.disegnaImmagineSuSchermo(sfondoUsandoMatita, (0, 0))
    sfondoEnigma = GlobalHWVar.schermo.copy().convert()
    superficieDisegni = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)

    while not esci:
        spostandoCursore = False
        utilizzandoStrumento = False

        if GlobalHWVar.mouseVisibile:
            xMouse, yMouse = pygame.mouse.get_pos()
            cursoreSuTornaIndietro = False
            cursoreSuCancellaTutto = False
            strumentoMarcato = False
            if xInizioFoglio - GlobalHWVar.gpx <= xMouse <= xFineFoglio + GlobalHWVar.gpx and yInizioFoglio - GlobalHWVar.gpy <= yMouse <= yFineFoglio + GlobalHWVar.gpy:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSulFoglio = True
                xStrumento = xMouse
                yStrumento = yMouse
                if xStrumento < xInizioFoglio:
                    xStrumento = xInizioFoglio
                elif xStrumento > xFineFoglio:
                    xStrumento = xFineFoglio
                if yStrumento < yInizioFoglio:
                    yStrumento = yInizioFoglio
                elif yStrumento > yFineFoglio:
                    yStrumento = yFineFoglio
                if xStrumentoVecchia != xStrumento or yStrumentoVecchia != yStrumento:
                    spostandoCursore = True
            else:
                cursoreSulFoglio = False
                if 0 <= yMouse <= GlobalHWVar.gpy * 2 and GlobalHWVar.gpx * 21.5 <= xMouse <= GlobalHWVar.gpx * 32:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    cursoreSuTornaIndietro = True
                elif GlobalHWVar.gpy * 2 <= yMouse <= GlobalHWVar.gpy * 4 and GlobalHWVar.gpx * 21.5 <= xMouse <= GlobalHWVar.gpx * 32:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    cursoreSuCancellaTutto = True
                elif 0 <= yMouse <= GlobalHWVar.gpy * 4 and 0 <= xMouse <= GlobalHWVar.gpx * 6 and strumentoInUso != "matita":
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    strumentoMarcato = "matita"
                elif 0 <= yMouse <= GlobalHWVar.gpy * 4 and GlobalHWVar.gpx * 6 <= xMouse <= GlobalHWVar.gpx * 12 and strumentoInUso != "gomma":
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    strumentoMarcato = "gomma"
                elif not GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(True)

        # gestione degli input
        if not primoframe:
            aggiornaInterfacciaPerCambioInput = False
            bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            esci = True
            bottoneDown = False
        if pygame.K_w in GlobalHWVar.listaTastiPremuti or "padSu" in GlobalHWVar.listaTastiPremuti:
            spostandoCursore = True
            yStrumento -= unitaSpostamentoCursore
            if yStrumento < yInizioFoglio:
                yStrumento = yInizioFoglio
        if pygame.K_a in GlobalHWVar.listaTastiPremuti or "padSinistra" in GlobalHWVar.listaTastiPremuti:
            spostandoCursore = True
            xStrumento -= unitaSpostamentoCursore
            if xStrumento < xInizioFoglio:
                xStrumento = xInizioFoglio
        if pygame.K_s in GlobalHWVar.listaTastiPremuti or "padGiu" in GlobalHWVar.listaTastiPremuti:
            spostandoCursore = True
            yStrumento += unitaSpostamentoCursore
            if yStrumento > yFineFoglio:
                yStrumento = yFineFoglio
        if pygame.K_d in GlobalHWVar.listaTastiPremuti or "padDestra" in GlobalHWVar.listaTastiPremuti:
            spostandoCursore = True
            xStrumento += unitaSpostamentoCursore
            if xStrumento > xFineFoglio:
                xStrumento = xFineFoglio
        if bottoneDown == pygame.K_2 or bottoneDown == pygame.K_KP2 or bottoneDown == "padL1":
            if strumentoInUso != "matita":
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                strumentoInUso = "matita"
                cambiatoStrumento = True
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if bottoneDown == pygame.K_3 or bottoneDown == pygame.K_KP3 or bottoneDown == "padR1":
            if strumentoInUso != "gomma":
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                strumentoInUso = "gomma"
                cambiatoStrumento = True
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if bottoneDown == pygame.K_LSHIFT or bottoneDown == pygame.K_RSHIFT or bottoneDown == "mouseCentrale" or bottoneDown == "padTriangolo":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.rumoreCancellaTuttoEnigmi)
            cancellaTutto = True
            bottoneDown = False
        if not aggiornaInterfacciaPerCambioInput and (pygame.K_SPACE in GlobalHWVar.listaTastiPremuti or (cursoreSulFoglio and "mouseSinistro" in GlobalHWVar.listaTastiPremuti) or (not cursoreSulFoglio and bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or "padCroce" in GlobalHWVar.listaTastiPremuti):
            if (GlobalHWVar.mouseVisibile and cursoreSulFoglio) or pygame.K_SPACE in GlobalHWVar.listaTastiPremuti or "padCroce" in GlobalHWVar.listaTastiPremuti:
                if GlobalHWVar.mouseVisibile and bottoneDown == "mouseSinistro" and cursoreSulFoglio:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAppoggioStrumentoEnigmi)
                    fattoCLickSulFoglio = True
                    utilizzandoStrumento = True
                elif GlobalHWVar.mouseVisibile and "mouseSinistro" in GlobalHWVar.listaTastiPremuti and cursoreSulFoglio and fattoCLickSulFoglio:
                    utilizzandoStrumento = True
                elif not GlobalHWVar.mouseVisibile and (bottoneDown == pygame.K_SPACE or bottoneDown == "padCroce"):
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAppoggioStrumentoEnigmi)
                    fattoCLickSulFoglio = True
                    utilizzandoStrumento = True
                elif not GlobalHWVar.mouseVisibile and (pygame.K_SPACE in GlobalHWVar.listaTastiPremuti or "padCroce" in GlobalHWVar.listaTastiPremuti) and fattoCLickSulFoglio:
                    utilizzandoStrumento = True
            else:
                if cursoreSuTornaIndietro:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    esci = True
                elif cursoreSuCancellaTutto:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.rumoreCancellaTuttoEnigmi)
                    cancellaTutto = True
                elif strumentoMarcato == "matita":
                    if strumentoInUso != "matita":
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        strumentoInUso = "matita"
                        cambiatoStrumento = True
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif strumentoMarcato == "gomma":
                    if strumentoInUso != "gomma":
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        strumentoInUso = "gomma"
                        cambiatoStrumento = True
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if GlobalHWVar.mouseVisibile and not "mouseSinistro" in GlobalHWVar.listaTastiPremuti:
            fattoCLickSulFoglio = False
        elif not GlobalHWVar.mouseVisibile and not (pygame.K_SPACE in GlobalHWVar.listaTastiPremuti or "padCroce" in GlobalHWVar.listaTastiPremuti):
            fattoCLickSulFoglio = False

        if utilizzandoStrumento:
            if not GlobalHWVar.canaleSoundInterazioni.get_busy():
                if strumentoInUso == "matita":
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreScorrimentoMatitaEnigmi, -1)
                elif strumentoInUso == "gomma":
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreScorrimentoGommaEnigmi, -1)
        else:
            GlobalHWVar.canaleSoundInterazioni.stop()

        if utilizzandoStrumento or spostandoCursore or primoFrame or cambiatoStrumento or cancellaTutto or aggiornaInterfacciaPerCambioInput:
            if primoFrame or aggiornaInterfacciaPerCambioInput or cancellaTutto or cambiatoStrumento:
                if primoFrame or cancellaTutto:
                    superficieDisegni = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, coloreGomma)
                if strumentoInUso == "matita":
                    GlobalHWVar.disegnaImmagineSuSchermo(sfondoUsandoMatita, (0, 0))
                elif strumentoInUso == "gomma":
                    GlobalHWVar.disegnaImmagineSuSchermo(sfondoUsandoGomma, (0, 0))

                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                    FunzioniGraficheGeneriche.messaggio("Tasto centrale: cancella tutto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.3, GlobalHWVar.gsy // 18 * 2.5, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("L1:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 0.5, 60)
                    FunzioniGraficheGeneriche.messaggio("R1:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 6.5, GlobalHWVar.gsy // 18 * 0.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.1, GlobalHWVar.gsy // 18 * 1, 50)
                    FunzioniGraficheGeneriche.messaggio("Triangolo: cancella tutto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.9, GlobalHWVar.gsy // 18 * 2.5, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("2:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 0.5, 60)
                    FunzioniGraficheGeneriche.messaggio("3:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 6.5, GlobalHWVar.gsy // 18 * 0.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.8, GlobalHWVar.gsy // 18 * 1, 50)
                    FunzioniGraficheGeneriche.messaggio("SHIFT: cancella tutto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.3, GlobalHWVar.gsy // 18 * 2.5, 50)
                sfondoEnigma = GlobalHWVar.schermo.copy().convert()

            dimXBackground = GlobalHWVar.gpx * 2
            dimYBackground = GlobalHWVar.gpy * 2
            if xStrumentoVecchia + dimXBackground >= GlobalHWVar.gsx:
                dimXBackground = GlobalHWVar.gsx - xStrumentoVecchia
            if yStrumentoVecchia < 0:
                yStrumentoVecchia = 0
            backgroundStrumento = sfondoEnigma.subsurface(pygame.Rect(xStrumentoVecchia, yStrumentoVecchia - GlobalHWVar.gpy * 2, dimXBackground, dimYBackground))
            GlobalHWVar.disegnaImmagineSuSchermo(backgroundStrumento, (xStrumentoVecchia, yStrumentoVecchia - GlobalHWVar.gpy * 2))

            if utilizzandoStrumento:
                if strumentoInUso == "matita":
                    if xStrumentoVecchia == xStrumento and yStrumentoVecchia == yStrumento:
                        GlobalHWVar.disegnaCerchioSuSchermo(superficieDisegni, coloreMatita, (xStrumento, yStrumento), dimensioneTrattoMatita // 2)
                    else:
                        GlobalHWVar.disegnaLineaSuSchermo(superficieDisegni, coloreMatita, (xStrumentoVecchia, yStrumentoVecchia), (xStrumento, yStrumento), dimensioneTrattoMatita)
                elif strumentoInUso == "gomma":
                    if xStrumentoVecchia == xStrumento and yStrumentoVecchia == yStrumento:
                        GlobalHWVar.disegnaCerchioSuSchermo(superficieDisegni, coloreGomma, (xStrumento, yStrumento), dimensioneTrattoGomma // 2)
                    else:
                        GlobalHWVar.disegnaLineaSuSchermo(superficieDisegni, coloreGomma, (xStrumentoVecchia, yStrumentoVecchia), (xStrumento, yStrumento), dimensioneTrattoGomma)
            GlobalHWVar.disegnaImmagineSuSchermo(superficieDisegni, (0, 0))

            if strumentoInUso == "matita":
                GlobalHWVar.disegnaImmagineSuSchermo(cursoreMatita, (xStrumento, yStrumento - GlobalHWVar.gpy * 2))
            elif strumentoInUso == "gomma":
                GlobalHWVar.disegnaImmagineSuSchermo(cursoreGomma, (xStrumento, yStrumento - GlobalHWVar.gpy * 2))

            xStrumentoVecchia = xStrumento
            yStrumentoVecchia = yStrumento
            cancellaTutto = False
            cambiatoStrumento = False

            if primoFrame:
                FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=1)
            else:
                GlobalHWVar.aggiornaSchermo()
            primoFrame = False

        primoframe = False
        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockDisegno.tick(GlobalHWVar.fpsDisegno)
    GenericFunc.cambiaVolumeCanale(GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.volumeEffetti)
    GlobalHWVar.configuraCursore(False)
