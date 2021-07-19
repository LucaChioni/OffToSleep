# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche


def mostraEnigma(tipoPersonaggio, avanzamentoStoria):
    FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False)

    if tipoPersonaggio == "OggettoEnigmaBiblioteca":
        enigmaBiblioteca()
    elif tipoPersonaggio == "OggettoEnigmaLabirinto":
        avanzamentoStoria = enigmaLabirinto(avanzamentoStoria)

    return avanzamentoStoria


def enigmaBiblioteca():
    GlobalHWVar.canaleSoundPassiRallo.stop()
    GenericFunc.cambiaVolumeCanale(GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.volumeEffetti / 2)

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
        if not primoFrame:
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
        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockDisegno.tick(GlobalHWVar.fpsDisegno)
    GenericFunc.cambiaVolumeCanale(GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.volumeEffetti)
    GlobalHWVar.configuraCursore(False)


def enigmaLabirinto(avanzamentoStoria):
    GlobalHWVar.canaleSoundPassiRallo.stop()
    GenericFunc.cambiaVolumeCanale(GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.volumeEffetti / 2)

    tastotempfps = 8
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
    utilizzandoStrumento = False
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

    # i quadretti vengono disegnati su una superfice 224x126 che viene scalata alla risoluzione del gioco ogni volta che deve essere disegnata su schermo
    numQuadrettiX = 224
    numQuadrettiY = 126
    gpxSupDisegnabile = numQuadrettiX // 32
    gpySupDisegnabile = numQuadrettiY // 18

    xStrumento = numQuadrettiX // 2
    yStrumento = numQuadrettiY // 2
    xStrumentoVecchia = xStrumento
    yStrumentoVecchia = yStrumento
    dimensioneTrattoMatita = 1
    dimensioneTrattoGomma = 1
    unitaSpostamentoCursore = 1
    xInizioFoglioSupDisegnabile = gpxSupDisegnabile * 1
    xFineFoglioSupDisegnabile = gpxSupDisegnabile * 31
    yInizioFoglioSupDisegnabile = gpySupDisegnabile * 5
    yFineFoglioSupDisegnabile = gpySupDisegnabile * 17

    xPrimoQuadrettoLabirinto = 57
    yPrimoQuadrettoLabirinto = 35
    xUltimoQuadrettoLabirinto = 166
    yUltimoQuadrettoLabirinto = 118
    # quadrettiColorati[[x, y, Flag], [x, y, Flag], ...] / Flag==True quando è colorato
    quadrettiColorati = []
    xQuadretto = xPrimoQuadrettoLabirinto
    while xQuadretto <= xUltimoQuadrettoLabirinto:
        yQuadretto = yPrimoQuadrettoLabirinto
        while yQuadretto <= yUltimoQuadrettoLabirinto:
            quadrettiColorati.append([xQuadretto, yQuadretto, False])
            yQuadretto += 1
        xQuadretto += 1
    # quadrettiColorabili contiene la lista di quadretti (solo x e y) che è possibile colorare
    quadrettiColorabili = [[45, 2], [44, 2], [43, 2], [42, 2], [41, 2], [40, 2], [39, 2], [38, 2], [37, 2], [36, 2], [35, 2], [34, 2], [33, 2], [33, 3], [33, 4], [33, 5], [33, 6], [33, 7], [33, 8], [33, 9], [33, 10], [33, 11], [33, 12], [33, 13], [33, 14], [33, 15], [32, 13], [31, 13], [30, 13], [29, 13], [29, 14], [29, 15], [29, 16], [29, 17], [29, 18], [29, 19], [30, 19], [31, 19], [43, 3], [43, 4], [43, 5], [43, 6], [45, 3], [45, 4], [45, 5], [45, 6], [45, 7], [45, 8], [44, 8], [43, 8], [42, 8], [41, 8], [41, 7], [41, 6], [41, 5], [41, 4], [40, 4], [39, 4], [38, 4], [37, 4], [36, 4], [35, 4], [34, 6], [35, 6], [36, 6], [37, 6], [38, 6], [39, 6], [39, 7], [39, 8], [39, 9], [39, 10], [40, 10], [41, 10], [42, 10], [43, 10], [44, 10], [45, 10], [46, 10], [47, 10], [47, 11], [47, 12], [46, 12], [45, 12], [44, 12], [43, 12], [42, 12], [41, 12], [40, 12], [39, 12], [38, 12], [37, 12], [37, 11], [37, 10], [37, 9], [37, 8], [36, 8], [35, 8], [35, 9], [35, 10], [35, 11], [35, 12], [35, 13], [35, 14], [36, 14], [37, 14], [38, 14], [39, 14], [40, 14], [41, 14], [42, 14], [43, 14], [44, 14], [45, 14], [46, 14], [47, 14], [39, 15], [39, 16], [38, 16], [37, 16], [36, 16], [35, 16], [35, 17], [34, 17], [33, 17], [32, 17], [31, 17], [31, 16], [31, 15], [40, 16], [41, 16], [42, 16], [43, 16], [43, 17], [43, 18], [42, 18], [41, 18], [40, 18], [39, 18], [38, 18], [37, 18], [47, 2], [47, 3], [47, 4], [47, 5], [47, 6], [47, 7], [47, 8], [47, 9], [48, 4], [49, 4], [49, 5], [49, 6], [49, 7], [49, 8], [49, 9], [49, 10], [49, 11], [49, 12], [49, 13], [49, 14], [49, 15], [49, 16], [48, 16], [47, 16], [46, 16], [45, 16], [50, 4], [51, 4], [52, 4], [53, 4], [53, 5], [53, 6], [53, 7], [54, 7], [55, 7], [56, 7], [57, 7], [57, 6], [57, 5], [57, 4], [58, 4], [59, 4], [60, 4], [61, 4], [62, 4], [62, 5], [62, 6], [61, 6], [60, 6], [59, 6], [59, 7], [59, 8], [59, 9], [58, 9], [57, 9], [56, 9], [55, 9], [54, 9], [53, 9], [52, 9], [51, 9], [51, 8], [51, 7], [51, 6], [51, 10], [51, 11], [51, 12], [51, 13], [51, 14], [51, 15], [51, 16], [52, 16], [53, 16], [54, 16], [55, 16], [55, 15], [55, 14], [55, 13], [54, 13], [53, 13], [53, 14], [56, 16], [57, 16], [58, 16], [57, 14], [57, 13], [57, 12], [57, 11], [56, 11], [55, 11], [54, 11], [53, 11], [52, 11], [59, 10], [60, 10], [61, 10], [62, 10], [62, 9], [62, 8], [61, 8], [62, 11], [62, 12], [61, 12], [60, 12], [59, 12], [59, 13], [59, 14], [60, 14], [60, 15], [60, 16], [62, 13], [62, 14], [62, 15], [62, 16], [63, 13], [64, 13], [64, 12], [64, 11], [64, 10], [64, 9], [64, 8], [64, 7], [64, 6], [64, 5], [64, 4], [65, 4], [66, 4], [67, 4], [68, 4], [68, 3], [68, 2], [67, 2], [66, 2], [65, 2], [64, 2], [63, 2], [62, 2], [61, 2], [60, 2], [59, 2], [58, 2], [57, 2], [56, 2], [55, 2], [54, 2], [53, 2], [52, 2], [51, 2], [50, 2], [49, 2], [55, 3], [55, 4], [55, 5], [66, 1], [68, 5], [68, 6], [68, 7], [68, 8], [68, 9], [68, 10], [68, 11], [67, 11], [66, 11], [66, 10], [66, 9], [66, 8], [66, 7], [66, 6], [65, 13], [66, 13], [67, 13], [68, 13], [69, 13], [70, 13], [70, 12], [70, 11], [70, 10], [70, 9], [70, 8], [70, 7], [70, 6], [74, 6], [74, 7], [74, 8], [74, 9], [74, 10], [74, 11], [73, 6], [72, 6], [72, 7], [72, 8], [72, 9], [72, 10], [72, 11], [72, 12], [72, 13], [71, 13], [73, 13], [74, 13], [74, 14], [74, 15], [74, 16], [74, 17], [74, 18], [74, 19], [75, 19], [76, 19], [76, 18], [76, 17], [76, 16], [76, 15], [76, 14], [76, 13], [76, 12], [76, 11], [76, 10], [76, 9], [76, 8], [76, 7], [76, 6], [76, 5], [76, 4], [76, 3], [76, 2], [75, 2], [74, 2], [73, 2], [72, 2], [71, 2], [70, 2], [70, 3], [70, 4], [71, 4], [72, 4], [73, 4], [74, 4], [68, 14], [68, 15], [68, 16], [68, 17], [68, 18], [67, 18], [66, 18], [66, 17], [66, 16], [66, 15], [65, 15], [64, 15], [64, 16], [64, 17], [64, 18], [63, 18], [62, 18], [61, 18], [60, 18], [59, 18], [58, 18], [57, 18], [56, 18], [55, 18], [54, 18], [53, 18], [52, 18], [51, 18], [50, 18], [49, 18], [48, 18], [47, 18], [46, 18], [45, 18], [45, 19], [45, 20], [44, 20], [43, 20], [42, 20], [41, 20], [40, 20], [39, 20], [45, 21], [45, 22], [45, 23], [45, 24], [44, 24], [43, 24], [42, 24], [41, 24], [40, 24], [39, 24], [39, 23], [39, 22], [40, 22], [41, 22], [42, 22], [43, 22], [68, 19], [68, 20], [67, 20], [66, 20], [65, 20], [64, 20], [63, 20], [62, 20], [61, 20], [60, 20], [59, 20], [58, 20], [57, 20], [56, 20], [55, 20], [54, 20], [53, 20], [52, 20], [51, 20], [50, 20], [49, 20], [49, 21], [49, 22], [49, 23], [49, 24], [50, 24], [51, 24], [52, 24], [53, 24], [53, 25], [53, 26], [52, 26], [51, 26], [50, 26], [49, 26], [48, 26], [47, 26], [47, 25], [47, 24], [47, 23], [47, 22], [47, 21], [47, 20], [46, 26], [45, 26], [44, 26], [43, 26], [42, 26], [41, 26], [40, 26], [39, 26], [38, 26], [37, 26], [37, 25], [37, 27], [37, 28], [37, 29], [37, 30], [37, 31], [38, 28], [39, 28], [40, 28], [41, 28], [42, 28], [43, 28], [44, 28], [45, 28], [39, 29], [39, 30], [40, 30], [41, 30], [54, 26], [55, 26], [56, 26], [57, 26], [58, 26], [59, 26], [60, 26], [61, 26], [62, 26], [62, 27], [62, 28], [61, 28], [60, 28], [59, 28], [58, 28], [57, 28], [56, 28], [55, 28], [54, 28], [53, 28], [52, 28], [51, 28], [50, 28], [49, 28], [48, 28], [47, 28], [47, 29], [47, 30], [47, 31], [47, 32], [47, 33], [47, 34], [47, 35], [46, 35], [45, 35], [45, 34], [45, 33], [45, 32], [45, 31], [45, 30], [44, 30], [43, 30], [43, 31], [43, 32], [63, 26], [64, 26], [65, 26], [66, 26], [67, 26], [67, 27], [67, 28], [67, 29], [67, 30], [67, 31], [67, 32], [68, 32], [69, 32], [70, 32], [71, 32], [72, 32], [73, 32], [74, 32], [75, 32], [76, 32], [77, 32], [78, 32], [78, 31], [78, 30], [78, 29], [78, 28], [77, 28], [76, 28], [75, 28], [74, 28], [73, 28], [77, 19], [78, 19], [79, 19], [80, 19], [81, 19], [82, 19], [83, 19], [84, 19], [85, 19], [86, 19], [87, 19], [88, 19], [89, 19], [89, 20], [89, 21], [88, 21], [87, 21], [86, 21], [85, 21], [84, 21], [83, 21], [82, 21], [81, 21], [80, 21], [79, 21], [78, 21], [77, 21], [76, 21], [76, 22], [76, 23], [76, 24], [75, 24], [74, 24], [73, 24], [72, 24], [71, 24], [70, 24], [69, 24], [69, 25], [69, 26], [69, 27], [69, 28], [70, 15], [70, 16], [70, 17], [70, 18], [70, 19], [70, 20], [71, 15], [72, 15], [72, 16], [72, 17], [72, 18], [72, 19], [72, 20], [72, 21], [73, 21], [74, 21], [74, 22], [74, 23], [72, 22], [71, 22], [70, 22], [69, 22], [68, 22], [67, 22], [66, 22], [65, 22], [64, 22], [63, 22], [62, 22], [61, 22], [60, 22], [59, 22], [58, 22], [57, 22], [56, 22], [55, 22], [54, 22], [53, 22], [52, 22], [51, 22], [55, 23], [55, 24], [56, 24], [57, 24], [58, 24], [59, 24], [60, 24], [61, 24], [62, 24], [63, 24], [64, 24], [65, 24], [66, 24], [67, 24], [48, 32], [49, 32], [50, 32], [51, 32], [52, 32], [53, 32], [53, 33], [53, 34], [54, 34], [55, 34], [56, 34], [57, 34], [53, 35], [53, 36], [53, 37], [48, 30], [49, 30], [50, 30], [51, 30], [52, 30], [53, 30], [54, 30], [55, 30], [56, 30], [57, 30], [58, 30], [59, 30], [60, 30], [61, 30], [62, 30], [63, 30], [63, 31], [63, 32], [62, 32], [61, 32], [60, 32], [59, 32], [58, 32], [57, 32], [56, 32], [55, 32], [59, 33], [59, 34], [59, 35], [59, 36], [59, 37], [59, 38], [60, 38], [61, 38], [61, 37], [61, 36], [61, 35], [61, 34], [62, 36], [63, 36], [64, 36], [65, 36], [66, 36], [64, 28], [65, 28], [65, 29], [65, 30], [65, 31], [65, 32], [65, 33], [65, 34], [64, 34], [63, 34], [63, 33], [66, 34], [67, 34], [68, 34], [69, 34], [70, 34], [71, 34], [72, 34], [73, 34], [74, 34], [75, 34], [76, 34], [77, 34], [78, 34], [79, 34], [80, 34], [80, 33], [80, 32], [80, 31], [80, 30], [80, 29], [80, 28], [80, 27], [80, 26], [80, 25], [81, 25], [82, 25], [83, 25], [84, 25], [85, 25], [86, 25], [87, 25], [88, 25], [89, 25], [89, 24], [89, 23], [88, 23], [87, 23], [86, 23], [85, 23], [84, 23], [83, 23], [82, 23], [81, 23], [80, 23], [79, 23], [78, 23], [78, 24], [78, 25], [78, 26], [77, 26], [76, 26], [75, 26], [74, 26], [73, 26], [72, 26], [71, 26], [71, 27], [71, 28], [71, 29], [71, 30], [70, 30], [69, 30], [72, 30], [73, 30], [74, 30], [75, 30], [76, 30], [82, 27], [81, 27], [82, 28], [82, 29], [82, 30], [82, 31], [82, 32], [82, 33], [82, 34], [82, 35], [82, 36], [81, 36], [80, 36], [79, 36], [78, 36], [77, 36], [76, 36], [75, 36], [74, 36], [73, 36], [72, 36], [71, 36], [70, 36], [70, 37], [70, 38], [71, 38], [72, 38], [73, 38], [74, 38], [75, 38], [76, 38], [77, 38], [78, 38], [79, 38], [80, 38], [81, 38], [82, 38], [83, 38], [84, 38], [85, 38], [85, 37], [85, 36], [85, 35], [84, 35], [84, 34], [84, 33], [84, 32], [84, 31], [84, 30], [84, 29], [84, 28], [84, 27], [85, 27], [86, 27], [87, 27], [87, 28], [87, 29], [86, 29], [89, 26], [89, 27], [89, 28], [89, 29], [90, 29], [91, 29], [92, 29], [93, 29], [93, 30], [93, 31], [93, 32], [93, 33], [92, 33], [91, 33], [91, 32], [91, 31], [94, 33], [95, 33], [96, 33], [97, 33], [98, 33], [99, 33], [100, 33], [101, 33], [101, 32], [101, 31], [100, 31], [99, 31], [98, 31], [97, 31], [96, 31], [95, 31], [95, 30], [95, 29], [96, 29], [97, 29], [98, 29], [99, 29], [100, 29], [101, 29], [102, 29], [103, 29], [104, 29], [105, 29], [106, 29], [107, 29], [103, 30], [103, 31], [104, 31], [105, 31], [106, 31], [107, 31], [89, 30], [89, 31], [89, 32], [89, 33], [89, 34], [89, 35], [90, 35], [91, 35], [92, 35], [93, 35], [94, 35], [95, 35], [96, 35], [97, 35], [98, 35], [99, 35], [100, 35], [101, 35], [101, 36], [101, 37], [101, 38], [101, 39], [101, 40], [101, 41], [101, 42], [101, 43], [101, 44], [101, 45], [101, 46], [101, 47], [101, 48], [101, 49], [101, 50], [102, 50], [103, 50], [104, 50], [105, 50], [105, 49], [105, 48], [104, 48], [103, 48], [103, 47], [103, 46], [103, 45], [102, 33], [103, 33], [104, 33], [105, 33], [106, 33], [107, 33], [107, 34], [107, 35], [107, 36], [107, 37], [107, 38], [107, 39], [107, 40], [107, 41], [103, 34], [103, 35], [103, 36], [103, 37], [103, 38], [103, 39], [99, 36], [99, 37], [98, 37], [97, 37], [96, 37], [95, 37], [94, 37], [93, 37], [92, 37], [91, 37], [90, 37], [89, 37], [88, 37], [87, 37], [87, 36], [87, 35], [87, 34], [87, 33], [86, 33], [86, 32], [86, 31], [87, 31], [99, 38], [99, 39], [98, 39], [97, 39], [96, 39], [95, 39], [94, 39], [93, 39], [92, 39], [91, 39], [90, 39], [89, 39], [88, 39], [87, 39], [87, 40], [87, 41], [87, 42], [86, 42], [85, 42], [84, 42], [83, 42], [82, 42], [81, 42], [80, 42], [88, 42], [89, 42], [89, 41], [90, 41], [91, 41], [92, 41], [93, 41], [94, 41], [95, 41], [96, 41], [97, 41], [98, 41], [99, 41], [99, 42], [99, 43], [99, 44], [99, 45], [99, 46], [99, 47], [98, 46], [97, 46], [96, 46], [95, 46], [95, 45], [99, 48], [98, 48], [97, 48], [96, 48], [95, 48], [94, 48], [93, 48], [93, 47], [93, 46], [93, 45], [93, 44], [93, 43], [94, 43], [95, 43], [96, 43], [97, 43], [97, 44], [92, 46], [91, 46], [90, 46], [89, 46], [88, 46], [87, 46], [86, 46], [85, 46], [91, 47], [91, 48], [91, 49], [91, 50], [91, 51], [91, 52], [92, 52], [93, 52], [94, 52], [95, 52], [96, 52], [97, 52], [90, 52], [89, 52], [88, 52], [87, 52], [87, 50], [88, 50], [89, 50], [87, 51], [101, 51], [101, 52], [102, 52], [103, 52], [104, 52], [105, 52], [106, 52], [107, 52], [107, 51], [107, 50], [107, 49], [107, 48], [107, 47], [107, 46], [107, 45], [107, 44], [107, 43], [106, 43], [105, 43], [105, 44], [105, 45], [105, 46], [104, 43], [103, 43], [103, 42], [103, 41], [104, 41], [105, 41], [105, 40], [105, 39], [105, 38], [105, 37], [105, 36], [105, 35], [107, 53], [107, 54], [107, 55], [107, 56], [107, 57], [107, 58], [107, 59], [107, 60], [107, 61], [107, 62], [107, 63], [107, 64], [107, 65], [107, 66], [107, 67], [107, 68], [106, 68], [105, 68], [104, 68], [103, 68], [102, 68], [101, 68], [100, 68], [100, 69], [100, 70], [100, 71], [100, 72], [100, 73], [100, 74], [100, 75], [100, 76], [100, 77], [100, 78], [100, 79], [100, 80], [99, 76], [98, 76], [97, 76], [96, 76], [95, 76], [95, 77], [95, 78], [95, 79], [95, 80], [96, 80], [97, 80], [98, 80], [98, 79], [98, 78], [97, 78], [94, 76], [93, 76], [93, 77], [93, 78], [93, 79], [93, 80], [92, 80], [91, 80], [90, 80], [89, 80], [88, 80], [86, 80], [86, 79], [86, 78], [87, 78], [88, 78], [89, 78], [90, 78], [91, 78], [92, 78], [99, 70], [98, 70], [97, 70], [96, 70], [95, 70], [94, 70], [93, 70], [92, 70], [99, 68], [98, 68], [97, 68], [96, 68], [95, 68], [94, 68], [93, 68], [92, 68], [91, 68], [90, 68], [90, 69], [90, 70], [90, 67], [89, 67], [88, 67], [87, 67], [86, 67], [85, 67], [84, 67], [83, 67], [82, 67], [82, 68], [82, 69], [82, 70], [82, 71], [82, 72], [82, 73], [82, 74], [82, 75], [82, 76], [82, 77], [82, 78], [92, 67], [92, 66], [92, 65], [91, 65], [90, 65], [89, 65], [88, 65], [87, 65], [86, 65], [85, 65], [84, 65], [83, 65], [82, 65], [81, 65], [80, 65], [80, 66], [80, 67], [80, 68], [80, 69], [80, 70], [80, 71], [80, 72], [80, 73], [80, 74], [80, 75], [80, 76], [80, 77], [80, 78], [80, 79], [80, 80], [81, 80], [82, 80], [83, 80], [84, 80], [84, 79], [84, 78], [84, 77], [84, 76], [84, 75], [84, 74], [84, 73], [84, 72], [84, 71], [84, 70], [84, 69], [85, 69], [86, 69], [86, 70], [86, 71], [86, 72], [86, 73], [86, 74], [86, 75], [86, 76], [87, 76], [88, 76], [89, 76], [90, 76], [91, 76], [91, 75], [91, 74], [92, 74], [93, 74], [94, 74], [95, 74], [96, 74], [97, 74], [98, 74], [98, 73], [98, 72], [97, 72], [96, 72], [95, 72], [94, 72], [93, 72], [92, 72], [91, 72], [90, 72], [89, 72], [88, 72], [88, 71], [88, 70], [88, 69], [88, 73], [88, 74], [89, 74], [93, 66], [94, 66], [95, 66], [96, 66], [97, 66], [97, 65], [94, 65], [94, 64], [94, 63], [93, 63], [93, 62], [93, 61], [93, 60], [92, 63], [91, 63], [90, 63], [89, 63], [88, 63], [87, 63], [86, 63], [85, 63], [84, 63], [83, 63], [85, 59], [84, 59], [83, 59], [83, 60], [83, 61], [84, 61], [85, 61], [86, 61], [87, 61], [88, 61], [89, 61], [90, 61], [91, 61], [91, 60], [91, 59], [91, 58], [92, 58], [93, 58], [94, 58], [95, 58], [95, 59], [95, 60], [95, 61], [95, 62], [95, 63], [96, 58], [97, 58], [97, 59], [97, 60], [97, 61], [97, 62], [97, 63], [98, 63], [99, 63], [100, 63], [101, 63], [101, 64], [101, 65], [101, 66], [100, 66], [99, 66], [99, 65], [106, 54], [105, 54], [104, 54], [103, 54], [102, 54], [101, 54], [100, 54], [99, 54], [99, 53], [99, 52], [99, 51], [99, 50], [98, 50], [97, 50], [96, 50], [95, 50], [94, 50], [93, 50], [98, 54], [97, 54], [96, 54], [95, 54], [94, 54], [93, 54], [92, 54], [91, 54], [90, 54], [89, 54], [88, 54], [87, 54], [87, 55], [87, 56], [87, 57], [86, 57], [85, 57], [84, 57], [83, 57], [87, 58], [87, 59], [88, 59], [89, 59], [89, 58], [89, 57], [89, 56], [90, 56], [91, 56], [92, 56], [93, 56], [94, 56], [95, 56], [96, 56], [97, 56], [98, 56], [99, 56], [100, 56], [101, 56], [102, 56], [103, 56], [104, 56], [105, 56], [101, 57], [101, 58], [101, 59], [102, 58], [103, 58], [104, 58], [105, 58], [105, 59], [105, 60], [105, 61], [105, 62], [105, 63], [105, 64], [103, 59], [103, 60], [103, 61], [103, 62], [103, 63], [103, 64], [103, 65], [103, 66], [104, 66], [105, 66], [102, 61], [101, 61], [100, 61], [99, 61], [99, 60], [99, 59], [99, 58], [91, 42], [91, 43], [91, 44], [90, 44], [89, 44], [88, 44], [87, 44], [86, 44], [85, 44], [84, 44], [83, 44], [83, 45], [83, 46], [83, 47], [83, 48], [83, 49], [83, 50], [83, 51], [82, 49], [81, 49], [81, 48], [81, 47], [81, 46], [81, 45], [81, 44], [80, 44], [79, 44], [79, 45], [79, 46], [79, 47], [79, 48], [79, 49], [78, 49], [77, 49], [77, 48], [77, 47], [77, 46], [77, 45], [77, 44], [77, 50], [77, 51], [77, 52], [77, 53], [77, 54], [77, 55], [77, 56], [79, 78], [78, 78], [77, 78], [76, 78], [75, 78], [74, 78], [73, 78], [73, 77], [73, 76], [73, 75], [73, 74], [73, 73], [73, 72], [73, 71], [73, 70], [74, 70], [75, 70], [76, 70], [75, 71], [75, 72], [76, 72], [77, 72], [78, 72], [78, 71], [78, 70], [78, 69], [78, 68], [77, 68], [76, 68], [75, 68], [74, 68], [73, 68], [73, 67], [73, 66], [74, 66], [75, 66], [76, 66], [66, 62], [66, 63], [67, 62], [68, 62], [69, 62], [70, 62], [71, 62], [72, 62], [73, 62], [73, 63], [73, 64], [73, 65], [76, 74], [75, 74], [74, 74], [78, 74], [78, 75], [78, 76], [77, 76], [76, 76], [75, 76], [75, 77], [79, 80], [78, 80], [77, 80], [76, 80], [75, 80], [74, 80], [73, 80], [72, 80], [71, 80], [70, 80], [69, 80], [68, 80], [67, 80], [67, 81], [66, 81], [65, 81], [64, 81], [63, 81], [59, 75], [60, 75], [61, 75], [62, 75], [63, 75], [64, 75], [65, 75], [66, 75], [67, 75], [67, 76], [67, 77], [67, 78], [67, 79], [65, 76], [65, 77], [65, 78], [65, 79], [64, 79], [63, 79], [62, 79], [61, 79], [60, 79], [59, 79], [59, 78], [59, 77], [60, 77], [61, 77], [62, 77], [63, 77], [58, 78], [57, 78], [56, 78], [55, 78], [54, 78], [54, 77], [54, 76], [55, 76], [56, 76], [57, 76], [57, 75], [57, 74], [57, 73], [58, 73], [59, 73], [60, 73], [61, 73], [62, 73], [63, 73], [64, 73], [65, 73], [66, 73], [67, 73], [71, 64], [71, 65], [71, 66], [71, 67], [71, 68], [71, 69], [71, 70], [71, 71], [71, 72], [71, 73], [71, 74], [71, 75], [71, 76], [71, 77], [71, 78], [71, 79], [70, 64], [69, 64], [69, 65], [69, 66], [69, 67], [69, 68], [69, 69], [68, 69], [67, 69], [66, 69], [65, 69], [64, 69], [63, 69], [62, 69], [61, 69], [60, 69], [60, 68], [60, 70], [60, 71], [59, 71], [58, 71], [57, 71], [56, 71], [55, 71], [55, 70], [55, 69], [56, 69], [57, 69], [58, 69], [58, 68], [61, 71], [62, 71], [63, 71], [64, 71], [65, 71], [66, 71], [67, 71], [68, 71], [69, 71], [69, 72], [69, 73], [69, 74], [69, 75], [69, 76], [69, 77], [69, 78], [68, 67], [67, 67], [66, 67], [65, 67], [64, 67], [63, 67], [62, 67], [62, 66], [61, 66], [60, 66], [59, 66], [58, 66], [58, 65], [58, 64], [58, 63], [57, 63], [56, 63], [55, 63], [54, 63], [53, 63], [52, 63], [51, 63], [50, 63], [49, 63], [49, 64], [62, 64], [62, 65], [62, 63], [62, 62], [62, 61], [62, 60], [62, 59], [62, 58], [62, 57], [62, 56], [62, 55], [62, 54], [62, 53], [62, 52], [62, 51], [62, 50], [61, 50], [60, 50], [60, 51], [60, 52], [60, 53], [60, 54], [60, 55], [60, 56], [60, 57], [60, 58], [60, 59], [60, 60], [60, 61], [60, 62], [60, 63], [60, 64], [59, 50], [58, 50], [57, 50], [56, 50], [55, 50], [54, 50], [53, 50], [52, 50], [51, 50], [50, 50], [50, 49], [50, 48], [51, 48], [52, 48], [53, 48], [54, 48], [55, 48], [56, 48], [57, 48], [58, 48], [59, 48], [60, 48], [52, 46], [52, 47], [62, 48], [62, 49], [54, 46], [55, 46], [56, 46], [57, 46], [58, 46], [59, 46], [60, 46], [61, 46], [62, 46], [63, 46], [64, 46], [65, 46], [66, 46], [67, 46], [68, 46], [69, 46], [69, 47], [69, 48], [68, 48], [67, 48], [66, 48], [65, 48], [64, 48], [63, 48], [50, 51], [50, 52], [49, 52], [48, 52], [48, 53], [48, 54], [48, 55], [47, 55], [47, 56], [47, 57], [51, 52], [52, 52], [53, 52], [54, 52], [55, 52], [56, 52], [56, 53], [56, 54], [56, 55], [56, 56], [56, 57], [49, 57], [50, 57], [50, 56], [50, 55], [50, 54], [52, 54], [52, 55], [52, 56], [52, 57], [51, 57], [53, 54], [54, 54], [54, 55], [54, 56], [54, 57], [54, 58], [54, 59], [53, 59], [52, 59], [51, 59], [50, 59], [49, 59], [48, 59], [47, 59], [55, 59], [56, 59], [57, 59], [58, 59], [58, 58], [58, 57], [58, 56], [58, 55], [58, 54], [58, 53], [58, 52], [58, 60], [58, 61], [57, 61], [56, 61], [55, 61], [54, 61], [53, 61], [52, 61], [51, 61], [50, 61], [49, 61], [48, 61], [47, 61], [47, 62], [47, 63], [47, 64], [46, 64], [45, 64], [45, 63], [45, 62], [45, 61], [45, 60], [45, 59], [45, 58], [45, 57], [45, 56], [45, 55], [44, 55], [43, 55], [43, 54], [43, 53], [44, 53], [45, 53], [46, 53], [46, 52], [67, 65], [67, 66], [66, 65], [65, 65], [64, 65], [64, 64], [64, 63], [64, 62], [64, 61], [64, 60], [65, 60], [66, 60], [67, 60], [68, 60], [69, 60], [70, 60], [71, 60], [72, 60], [73, 60], [74, 60], [75, 60], [76, 60], [77, 60], [77, 61], [77, 62], [76, 62], [75, 62], [75, 63], [75, 64], [77, 63], [77, 64], [78, 64], [78, 65], [78, 66], [63, 50], [64, 50], [64, 51], [64, 52], [65, 52], [66, 52], [67, 52], [68, 52], [69, 52], [70, 52], [71, 52], [66, 53], [66, 54], [65, 54], [64, 54], [64, 55], [64, 56], [65, 56], [66, 56], [67, 56], [68, 56], [69, 56], [70, 56], [71, 56], [71, 57], [71, 58], [70, 58], [69, 58], [68, 58], [67, 58], [66, 58], [65, 58], [64, 58], [72, 58], [73, 58], [74, 58], [75, 58], [76, 58], [77, 58], [78, 58], [79, 58], [79, 59], [79, 60], [79, 61], [79, 62], [79, 51], [79, 52], [79, 53], [79, 54], [79, 55], [79, 56], [79, 57], [80, 51], [81, 51], [81, 52], [81, 53], [81, 54], [81, 55], [81, 56], [81, 57], [81, 58], [81, 59], [81, 60], [81, 61], [81, 62], [81, 63], [82, 55], [83, 55], [84, 55], [85, 55], [83, 53], [84, 53], [85, 53], [85, 54], [85, 48], [86, 48], [87, 48], [88, 48], [89, 48], [85, 49], [85, 50], [85, 51], [85, 52], [65, 50], [66, 50], [67, 50], [68, 50], [69, 50], [70, 50], [71, 50], [71, 49], [71, 48], [71, 47], [71, 46], [71, 45], [71, 44], [70, 44], [69, 44], [68, 44], [67, 44], [66, 44], [65, 44], [64, 44], [63, 44], [62, 44], [61, 44], [60, 44], [59, 44], [58, 44], [57, 44], [56, 44], [55, 44], [54, 44], [53, 44], [52, 44], [51, 44], [50, 44], [50, 45], [50, 46], [49, 46], [48, 46], [47, 46], [46, 46], [45, 46], [44, 46], [44, 47], [44, 48], [45, 48], [46, 48], [47, 48], [48, 48], [48, 49], [48, 50], [47, 50], [46, 50], [45, 50], [44, 50], [44, 51], [43, 51], [42, 51], [41, 51], [40, 51], [39, 51], [38, 51], [38, 50], [38, 49], [38, 48], [39, 48], [40, 48], [40, 49], [57, 43], [57, 42], [56, 42], [55, 42], [54, 42], [53, 42], [52, 42], [51, 42], [50, 42], [50, 41], [54, 41], [54, 40], [54, 39], [55, 39], [55, 38], [55, 37], [55, 36], [56, 36], [57, 36], [57, 37], [57, 38], [57, 39], [57, 40], [58, 40], [59, 40], [60, 40], [61, 40], [62, 40], [63, 40], [63, 39], [63, 38], [64, 38], [65, 38], [66, 38], [67, 38], [68, 38], [68, 37], [68, 36], [58, 42], [59, 42], [60, 42], [61, 42], [62, 42], [63, 42], [64, 42], [65, 42], [66, 42], [67, 42], [68, 42], [69, 42], [70, 42], [71, 42], [72, 42], [73, 42], [73, 43], [73, 44], [73, 45], [73, 46], [73, 47], [73, 48], [73, 49], [73, 50], [73, 51], [73, 52], [73, 53], [73, 54], [72, 54], [71, 54], [70, 54], [69, 54], [68, 54], [73, 55], [73, 56], [74, 56], [75, 56], [75, 55], [75, 54], [75, 53], [75, 52], [75, 51], [75, 50], [75, 49], [75, 48], [75, 47], [75, 46], [75, 45], [75, 44], [75, 43], [75, 42], [76, 42], [77, 42], [78, 42], [85, 40], [84, 40], [83, 40], [82, 40], [81, 40], [80, 40], [79, 40], [78, 40], [77, 40], [76, 40], [75, 40], [74, 40], [73, 40], [72, 40], [71, 40], [70, 40], [69, 40], [68, 40], [67, 40], [66, 40], [65, 40], [65, 41], [49, 44], [48, 44], [47, 44], [46, 44], [45, 44], [44, 44], [43, 44], [42, 44], [42, 45], [42, 46], [42, 47], [42, 48], [42, 49], [41, 46], [40, 46], [39, 46], [38, 46], [37, 46], [36, 46], [35, 46], [34, 46], [33, 46], [32, 46], [32, 47], [32, 48], [32, 49], [32, 50], [32, 51], [33, 51], [34, 51], [36, 51], [36, 50], [36, 49], [36, 48], [36, 47], [35, 49], [34, 49], [34, 48], [41, 44], [40, 44], [39, 44], [39, 43], [39, 42], [40, 42], [41, 42], [42, 42], [43, 42], [44, 42], [44, 41], [45, 42], [46, 42], [47, 42], [48, 42], [48, 41], [48, 40], [48, 39], [49, 39], [49, 38], [49, 37], [49, 36], [49, 35], [49, 34], [50, 34], [51, 34], [51, 35], [51, 36], [51, 37], [51, 38], [51, 39], [52, 39], [52, 40], [43, 56], [43, 57], [43, 58], [43, 59], [43, 60], [43, 61], [43, 62], [43, 63], [43, 64], [43, 65], [43, 66], [42, 66], [41, 66], [40, 66], [39, 66], [38, 66], [37, 66], [37, 67], [37, 68], [38, 68], [39, 68], [40, 68], [41, 68], [42, 68], [43, 68], [44, 68], [45, 68], [46, 68], [47, 68], [48, 68], [49, 68], [50, 68], [51, 68], [52, 68], [53, 68], [53, 67], [54, 67], [55, 67], [56, 67], [56, 66], [56, 65], [55, 65], [54, 65], [53, 65], [52, 65], [51, 65], [51, 66], [50, 66], [49, 66], [48, 66], [47, 66], [46, 66], [45, 66], [48, 69], [48, 70], [48, 71], [48, 72], [47, 72], [46, 72], [46, 73], [46, 74], [46, 75], [46, 76], [46, 77], [46, 78], [45, 78], [44, 78], [44, 77], [44, 76], [44, 75], [44, 74], [43, 74], [42, 74], [41, 74], [40, 74], [39, 74], [42, 75], [42, 76], [48, 73], [48, 74], [48, 75], [48, 76], [48, 77], [48, 78], [48, 79], [48, 80], [61, 81], [60, 81], [59, 81], [58, 81], [57, 81], [57, 80], [56, 80], [55, 80], [54, 80], [53, 80], [52, 80], [52, 79], [52, 78], [52, 77], [52, 76], [52, 75], [52, 74], [53, 74], [54, 74], [55, 74], [55, 73], [52, 73], [52, 72], [53, 72], [53, 71], [53, 70], [52, 70], [51, 70], [50, 70], [50, 71], [50, 72], [50, 73], [50, 74], [50, 75], [50, 76], [50, 77], [50, 78], [50, 79], [50, 80], [49, 80], [47, 80], [46, 80], [45, 80], [44, 80], [43, 80], [42, 80], [41, 80], [40, 80], [39, 80], [38, 80], [37, 80], [36, 80], [35, 80], [35, 79], [35, 78], [36, 78], [37, 78], [38, 78], [39, 78], [40, 78], [41, 78], [42, 78], [39, 76], [40, 76], [38, 76], [37, 76], [37, 77], [35, 77], [35, 76], [35, 75], [35, 74], [34, 74], [36, 68], [35, 68], [34, 68], [33, 68], [32, 68], [31, 68], [30, 68], [30, 69], [30, 70], [30, 71], [30, 72], [31, 72], [32, 72], [32, 71], [32, 70], [33, 70], [34, 70], [35, 70], [36, 70], [37, 70], [38, 70], [39, 70], [40, 70], [41, 70], [42, 70], [43, 70], [44, 70], [45, 70], [46, 70], [44, 71], [44, 72], [42, 71], [42, 72], [41, 72], [40, 72], [39, 72], [38, 72], [37, 72], [36, 72], [35, 72], [34, 72], [37, 73], [37, 74], [29, 72], [28, 72], [27, 72], [26, 72], [25, 72], [24, 72], [23, 72], [22, 72], [21, 72], [20, 72], [19, 72], [18, 72], [17, 72], [16, 72], [16, 71], [16, 70], [16, 69], [16, 68], [16, 67], [16, 66], [17, 66], [18, 66], [19, 66], [20, 66], [21, 66], [22, 66], [23, 66], [24, 66], [25, 66], [26, 66], [27, 66], [28, 66], [28, 67], [28, 68], [28, 69], [28, 70], [27, 70], [26, 70], [25, 70], [24, 70], [23, 70], [22, 70], [21, 70], [20, 70], [19, 70], [18, 70], [18, 69], [18, 68], [19, 68], [20, 68], [21, 68], [22, 68], [23, 68], [24, 68], [25, 68], [26, 68], [16, 65], [16, 64], [17, 64], [18, 64], [19, 64], [20, 64], [21, 64], [22, 64], [23, 64], [24, 64], [25, 64], [26, 64], [27, 64], [28, 64], [29, 64], [29, 63], [29, 62], [29, 61], [29, 60], [29, 59], [29, 58], [29, 57], [30, 57], [31, 57], [32, 57], [33, 57], [33, 58], [33, 59], [33, 60], [33, 61], [33, 62], [34, 62], [35, 62], [35, 61], [35, 60], [35, 59], [35, 58], [35, 57], [36, 57], [37, 57], [37, 58], [37, 59], [37, 60], [37, 61], [37, 62], [37, 63], [37, 64], [38, 64], [39, 64], [29, 66], [30, 66], [31, 66], [32, 66], [33, 66], [34, 66], [35, 66], [35, 65], [35, 64], [34, 64], [33, 64], [32, 64], [31, 64], [31, 63], [31, 62], [31, 61], [31, 60], [31, 59], [28, 57], [27, 57], [27, 58], [27, 59], [27, 60], [27, 61], [27, 62], [26, 60], [25, 60], [24, 60], [24, 59], [26, 57], [25, 57], [24, 57], [23, 57], [22, 57], [21, 57], [20, 57], [19, 57], [18, 57], [17, 57], [16, 57], [16, 58], [16, 59], [16, 60], [17, 60], [18, 60], [18, 59], [15, 57], [14, 57], [13, 57], [12, 57], [11, 57], [10, 57], [9, 57], [8, 57], [7, 57], [6, 57], [5, 57], [4, 57], [3, 57], [2, 57], [2, 56], [2, 55], [2, 54], [2, 53], [2, 52], [2, 51], [2, 50], [2, 49], [3, 49], [3, 48], [3, 47], [3, 46], [3, 45], [3, 44], [3, 43], [3, 42], [3, 41], [3, 40], [3, 39], [4, 39], [5, 39], [6, 39], [7, 39], [8, 39], [9, 39], [9, 40], [9, 41], [9, 42], [9, 43], [5, 41], [5, 42], [5, 43], [5, 44], [5, 45], [5, 46], [5, 47], [5, 48], [5, 49], [5, 50], [5, 51], [4, 51], [4, 52], [4, 53], [4, 54], [4, 55], [4, 56], [6, 51], [7, 51], [8, 51], [9, 51], [10, 51], [11, 51], [12, 51], [12, 52], [12, 53], [11, 53], [10, 53], [9, 53], [8, 53], [7, 53], [6, 53], [6, 54], [6, 55], [7, 55], [8, 55], [9, 55], [10, 55], [11, 55], [12, 55], [13, 55], [14, 55], [14, 54], [14, 53], [15, 53], [16, 53], [17, 53], [18, 53], [19, 53], [20, 53], [21, 53], [22, 53], [22, 54], [22, 55], [21, 55], [20, 55], [19, 55], [18, 55], [17, 55], [16, 55], [23, 55], [24, 55], [25, 55], [26, 55], [27, 55], [28, 55], [29, 55], [30, 55], [31, 55], [32, 55], [33, 55], [34, 55], [35, 55], [36, 55], [37, 55], [38, 55], [39, 55], [39, 56], [39, 57], [39, 58], [39, 59], [39, 60], [39, 61], [39, 62], [13, 51], [14, 51], [15, 51], [16, 51], [17, 51], [18, 51], [19, 51], [20, 51], [21, 51], [22, 51], [23, 51], [24, 51], [24, 52], [24, 53], [25, 53], [26, 53], [27, 53], [28, 53], [29, 53], [30, 53], [31, 53], [32, 53], [33, 53], [34, 53], [35, 53], [36, 53], [37, 53], [38, 53], [39, 53], [40, 53], [41, 53], [41, 54], [41, 55], [41, 56], [41, 57], [41, 58], [41, 59], [41, 60], [41, 61], [41, 62], [41, 63], [41, 64], [15, 39], [16, 39], [17, 39], [18, 39], [19, 39], [20, 39], [21, 39], [21, 40], [21, 41], [21, 42], [21, 43], [21, 44], [21, 45], [21, 46], [21, 47], [22, 47], [22, 48], [22, 49], [22, 50], [22, 41], [23, 41], [24, 41], [25, 41], [26, 41], [7, 41], [6, 41], [7, 42], [7, 43], [7, 44], [7, 45], [7, 46], [7, 47], [7, 48], [7, 49], [8, 49], [9, 49], [10, 49], [11, 49], [12, 49], [13, 49], [14, 49], [15, 49], [15, 48], [15, 47], [14, 47], [13, 47], [12, 47], [11, 47], [10, 47], [9, 47], [13, 46], [13, 45], [13, 44], [13, 43], [13, 42], [13, 41], [13, 40], [13, 39], [19, 41], [18, 41], [17, 41], [16, 41], [15, 41], [15, 42], [15, 43], [15, 44], [15, 45], [16, 45], [17, 45], [17, 46], [17, 47], [17, 48], [17, 49], [16, 49], [18, 49], [19, 49], [20, 49], [19, 48], [19, 47], [19, 46], [19, 45], [19, 44], [19, 43], [18, 43], [17, 43], [38, 44], [37, 44], [36, 44], [35, 44], [34, 44], [33, 44], [32, 44], [31, 44], [30, 44], [30, 45], [30, 46], [30, 47], [30, 48], [30, 49], [30, 50], [30, 51], [29, 51], [28, 51], [27, 51], [26, 51], [26, 50], [26, 49], [27, 49], [28, 49], [28, 46], [28, 47], [29, 47], [27, 47], [26, 47], [25, 47], [24, 47], [24, 48], [24, 49], [28, 41], [28, 42], [28, 43], [27, 43], [26, 43], [25, 43], [24, 43], [23, 43], [23, 44], [23, 45], [24, 45], [25, 45], [26, 45], [27, 45], [28, 45], [38, 38], [39, 38], [40, 38], [40, 37], [41, 37], [42, 37], [43, 37], [43, 36], [43, 35], [43, 34], [44, 37], [45, 37], [46, 37], [47, 37], [46, 38], [46, 39], [46, 40], [45, 39], [44, 39], [43, 39], [42, 39], [42, 40], [41, 40], [40, 40], [39, 40], [38, 40], [37, 40], [37, 41], [37, 42], [37, 43], [36, 40], [36, 39], [36, 38], [36, 37], [36, 36], [36, 35], [36, 34], [36, 33], [37, 33], [38, 33], [39, 33], [39, 32], [40, 32], [41, 32], [41, 33], [41, 34], [41, 35], [40, 35], [39, 35], [38, 35], [38, 36], [35, 35], [34, 35], [33, 35], [32, 35], [31, 35], [30, 35], [29, 35], [28, 35], [27, 35], [26, 35], [25, 35], [24, 35], [23, 35], [22, 35], [21, 35], [21, 34], [21, 33], [21, 32], [21, 31], [21, 30], [21, 29], [28, 36], [28, 37], [27, 37], [26, 37], [25, 37], [24, 37], [23, 37], [23, 38], [23, 39], [24, 39], [25, 39], [26, 39], [27, 39], [28, 39], [29, 39], [30, 39], [30, 38], [30, 37], [30, 40], [31, 40], [32, 40], [32, 39], [32, 38], [32, 37], [33, 37], [34, 37], [34, 38], [34, 39], [34, 40], [34, 41], [34, 42], [35, 42], [33, 42], [32, 42], [31, 42], [30, 42], [35, 33], [34, 33], [33, 33], [32, 33], [31, 33], [30, 33], [29, 33], [28, 33], [27, 33], [26, 33], [25, 33], [24, 33], [23, 33], [23, 32], [23, 31], [23, 30], [23, 29], [23, 28], [23, 27], [22, 27], [21, 27], [24, 27], [25, 27], [25, 26], [25, 25], [25, 24], [25, 23], [25, 22], [25, 28], [25, 29], [25, 30], [25, 31], [27, 31], [27, 32], [28, 31], [29, 31], [29, 30], [29, 29], [29, 28], [29, 27], [29, 26], [29, 25], [29, 24], [29, 23], [29, 22], [29, 21], [30, 21], [31, 21], [31, 22], [31, 23], [31, 24], [31, 25], [31, 26], [31, 27], [31, 28], [31, 29], [31, 30], [31, 31], [32, 31], [33, 31], [33, 30], [33, 29], [33, 28], [33, 27], [33, 26], [33, 25], [33, 24], [33, 23], [33, 22], [33, 21], [33, 20], [33, 19], [34, 19], [35, 19], [34, 21], [35, 21], [36, 21], [37, 21], [37, 20], [37, 22], [37, 23], [36, 23], [35, 23], [35, 24], [35, 25], [35, 26], [35, 27], [35, 28], [35, 29], [35, 30], [35, 31], [33, 74], [33, 75], [33, 76], [32, 76], [31, 76], [30, 76], [29, 76], [28, 76], [33, 77], [33, 78], [33, 79], [33, 80], [32, 80], [31, 80], [31, 79], [31, 78], [30, 78], [29, 78], [28, 78], [30, 80], [29, 80], [28, 80], [27, 80], [26, 80], [25, 80], [24, 80], [23, 80], [22, 80], [21, 80], [20, 80], [32, 74], [31, 74], [30, 74], [29, 74], [28, 74], [27, 74], [26, 74], [25, 74], [24, 74], [23, 74], [22, 74], [21, 74], [20, 74], [19, 74], [18, 74], [17, 74], [16, 74], [15, 74], [14, 74], [13, 74], [12, 74], [11, 74], [10, 74], [9, 74], [8, 74], [8, 73], [8, 72], [8, 71], [8, 70], [8, 69], [8, 68], [8, 67], [8, 66], [9, 66], [10, 66], [10, 67], [10, 68], [10, 69], [10, 70], [14, 70], [14, 71], [14, 72], [14, 73], [14, 69], [14, 68], [14, 67], [14, 66], [14, 65], [14, 64], [14, 63], [14, 62], [14, 61], [14, 60], [14, 59], [15, 62], [16, 62], [17, 62], [18, 62], [19, 62], [20, 62], [20, 61], [20, 60], [20, 59], [21, 59], [22, 59], [22, 60], [22, 61], [22, 62], [23, 62], [24, 62], [25, 62], [13, 59], [12, 59], [11, 59], [10, 59], [10, 60], [10, 61], [10, 62], [9, 62], [8, 62], [8, 61], [8, 60], [8, 59], [12, 60], [12, 61], [12, 62], [12, 63], [12, 64], [12, 65], [12, 66], [12, 67], [12, 68], [12, 69], [12, 70], [12, 71], [12, 72], [11, 72], [10, 72], [10, 64], [9, 64], [11, 64], [8, 64], [7, 64], [6, 64], [6, 63], [6, 62], [6, 61], [5, 61], [4, 61], [4, 62], [4, 63], [4, 64], [4, 65], [4, 66], [4, 67], [4, 68], [4, 69], [5, 66], [6, 66], [6, 67], [6, 68], [6, 69], [6, 70], [6, 71], [6, 72], [6, 73], [6, 74], [6, 60], [6, 59], [5, 59], [4, 59], [3, 59], [2, 59], [2, 60], [2, 61], [2, 62], [2, 63], [2, 64], [2, 65], [2, 66], [2, 67], [2, 68], [2, 69], [2, 70], [2, 71], [2, 72], [2, 73], [2, 74], [2, 75], [2, 76], [2, 77], [2, 78], [3, 78], [4, 78], [5, 78], [6, 78], [7, 78], [8, 78], [9, 78], [10, 78], [10, 77], [10, 76], [9, 76], [8, 76], [7, 76], [6, 76], [5, 76], [4, 76], [4, 75], [4, 74], [4, 73], [4, 72], [4, 71], [2, 79], [2, 80], [3, 80], [4, 80], [5, 80], [6, 80], [7, 80], [8, 80], [27, 30], [27, 29], [27, 28], [27, 27], [27, 26], [27, 25], [27, 24], [27, 23], [27, 22], [27, 21], [27, 20], [27, 19], [27, 18], [27, 17], [27, 16], [27, 15], [26, 15], [25, 15], [25, 16], [25, 17], [25, 18], [25, 19], [25, 20], [24, 20], [23, 20], [23, 21], [23, 22], [23, 23], [23, 24], [23, 25], [22, 25], [21, 25], [21, 24], [21, 23], [27, 14], [27, 13], [26, 13], [25, 13], [24, 13], [23, 13], [22, 13], [21, 13], [20, 13], [19, 13], [18, 13], [17, 13], [16, 13], [15, 13], [15, 14], [15, 15], [15, 16], [15, 17], [15, 18], [16, 18], [17, 18], [17, 17], [17, 16], [17, 15], [18, 15], [19, 15], [20, 15], [21, 15], [22, 15], [23, 15], [23, 16], [23, 17], [23, 18], [22, 18], [21, 18], [21, 17], [20, 17], [19, 17], [19, 18], [19, 19], [19, 20], [19, 21], [20, 21], [21, 21], [21, 19], [17, 19], [17, 20], [17, 21], [15, 19], [15, 20], [15, 21], [15, 22], [15, 23], [15, 24], [15, 25], [15, 26], [15, 27], [15, 28], [14, 13], [13, 13], [13, 14], [13, 15], [13, 16], [13, 17], [13, 18], [13, 19], [13, 20], [13, 21], [13, 22], [13, 23], [13, 24], [13, 25], [13, 26], [13, 27], [13, 28], [13, 29], [13, 30], [14, 30], [15, 30], [16, 30], [17, 30], [17, 31], [17, 32], [17, 33], [17, 29], [17, 28], [17, 27], [17, 26], [17, 25], [17, 24], [17, 23], [18, 23], [19, 23], [19, 24], [19, 25], [19, 26], [19, 27], [19, 28], [19, 29], [13, 31], [13, 32], [13, 33], [12, 33], [11, 33], [11, 32], [11, 31], [11, 30], [11, 29], [11, 28], [11, 27], [9, 27], [9, 28], [9, 29], [9, 30], [9, 31], [10, 31], [10, 33], [9, 33], [8, 33], [7, 33], [7, 32], [7, 31], [7, 30], [7, 29], [7, 28], [7, 27], [6, 27], [5, 27], [4, 27], [3, 27], [3, 28], [3, 29], [3, 30], [3, 31], [3, 32], [3, 33], [3, 34], [3, 35], [3, 36], [3, 37], [5, 37], [5, 36], [5, 35], [5, 34], [5, 33], [5, 32], [5, 31], [5, 30], [5, 29], [5, 28], [21, 37], [20, 37], [19, 37], [19, 36], [19, 35], [19, 34], [19, 33], [19, 32], [19, 31], [15, 32], [15, 33], [15, 34], [15, 35], [16, 35], [17, 35], [14, 35], [13, 35], [12, 35], [11, 35], [10, 35], [9, 35], [8, 35], [7, 35], [14, 36], [14, 37], [15, 37], [16, 37], [17, 37], [18, 37], [13, 37], [12, 37], [11, 37], [10, 37], [9, 37], [8, 37], [7, 37], [6, 37], [11, 39], [11, 38], [11, 40], [11, 41], [11, 42], [11, 43], [11, 44], [11, 45], [10, 45], [9, 45], [8, 45], [9, 80], [10, 80], [11, 80], [12, 80], [13, 80], [14, 80], [15, 80], [16, 80], [17, 80], [18, 80], [18, 79], [18, 78], [17, 78], [16, 78], [15, 78], [14, 78], [19, 78], [20, 78], [21, 78], [22, 78], [23, 78], [24, 78], [25, 78], [26, 78], [26, 77], [26, 76], [25, 76], [24, 76], [23, 76], [22, 76], [21, 76], [20, 76], [19, 76], [18, 76], [17, 76], [16, 76], [15, 76], [14, 76], [13, 76], [12, 76], [12, 77], [12, 78], [10, 81]]
    for quadretto in quadrettiColorabili:
        quadretto[0] = quadretto[0] + xPrimoQuadrettoLabirinto
        quadretto[1] = quadretto[1] + yPrimoQuadrettoLabirinto
    # quadrettiDaColorare contiene la lista di quadretti (solo x e y) da colorare per risolvere l'enigma
    quadrettiDaColorare = [[66, 2], [67, 2], [68, 2], [66, 1], [68, 3], [68, 4], [67, 4], [66, 4], [65, 4], [64, 4], [64, 5], [64, 6], [64, 7], [64, 8], [64, 9], [64, 10], [64, 11], [64, 12], [64, 13], [65, 13], [66, 13], [67, 13], [68, 13], [68, 14], [68, 15], [68, 16], [68, 17], [68, 18], [68, 19], [68, 20], [67, 20], [66, 20], [65, 20], [64, 20], [63, 20], [62, 20], [61, 20], [60, 20], [59, 20], [58, 20], [57, 20], [56, 20], [55, 20], [54, 20], [53, 20], [52, 20], [51, 20], [50, 20], [49, 20], [49, 21], [49, 22], [49, 23], [49, 24], [50, 24], [51, 24], [52, 24], [53, 24], [53, 25], [53, 26], [54, 26], [55, 26], [56, 26], [57, 26], [58, 26], [59, 26], [60, 26], [61, 26], [62, 26], [62, 27], [62, 28], [61, 28], [60, 28], [59, 28], [58, 28], [57, 28], [56, 28], [55, 28], [54, 28], [53, 28], [52, 28], [51, 28], [50, 28], [49, 28], [48, 28], [47, 28], [47, 29], [47, 30], [48, 30], [49, 30], [50, 30], [51, 30], [52, 30], [53, 30], [54, 30], [55, 30], [56, 30], [57, 30], [58, 30], [59, 30], [60, 30], [61, 30], [62, 30], [63, 30], [63, 31], [63, 32], [63, 33], [63, 34], [64, 34], [65, 34], [66, 34], [67, 34], [68, 34], [69, 34], [70, 34], [71, 34], [72, 34], [73, 34], [74, 34], [75, 34], [76, 34], [77, 34], [78, 34], [79, 34], [80, 34], [80, 33], [80, 32], [80, 31], [80, 30], [80, 29], [80, 28], [80, 27], [80, 25], [80, 26], [81, 25], [82, 25], [83, 25], [84, 25], [85, 25], [86, 25], [87, 25], [88, 25], [89, 25], [89, 26], [89, 27], [89, 28], [89, 29], [89, 30], [89, 31], [89, 32], [89, 33], [89, 34], [89, 35], [90, 35], [91, 35], [92, 35], [93, 35], [94, 35], [95, 35], [96, 35], [97, 35], [98, 35], [99, 35], [100, 35], [101, 35], [101, 36], [101, 37], [101, 38], [101, 39], [101, 40], [101, 41], [101, 42], [101, 43], [101, 44], [101, 45], [101, 46], [101, 47], [101, 48], [101, 49], [101, 50], [101, 51], [101, 52], [102, 52], [103, 52], [104, 52], [105, 52], [106, 52], [107, 52], [107, 53], [107, 54], [107, 55], [107, 56], [107, 57], [107, 58], [107, 59], [107, 60], [107, 61], [107, 62], [107, 63], [107, 64], [107, 65], [107, 66], [107, 67], [107, 68], [106, 68], [105, 68], [104, 68], [103, 68], [102, 68], [101, 68], [100, 68], [99, 68], [98, 68], [97, 68], [96, 68], [95, 68], [94, 68], [93, 68], [92, 68], [92, 67], [92, 66], [92, 65], [91, 65], [90, 65], [89, 65], [88, 65], [87, 65], [86, 65], [85, 65], [84, 65], [83, 65], [82, 65], [81, 65], [80, 65], [80, 66], [80, 67], [80, 68], [80, 69], [80, 70], [80, 71], [80, 72], [80, 73], [80, 74], [80, 75], [80, 76], [80, 77], [80, 78], [80, 79], [80, 80], [79, 80], [78, 80], [77, 80], [76, 80], [75, 80], [74, 80], [73, 80], [72, 80], [71, 80], [71, 79], [71, 78], [71, 77], [71, 76], [71, 75], [71, 74], [71, 73], [71, 72], [71, 71], [71, 70], [71, 69], [71, 68], [71, 67], [71, 66], [71, 65], [71, 64], [70, 64], [69, 64], [69, 65], [69, 66], [69, 67], [68, 67], [67, 67], [66, 67], [65, 67], [64, 67], [63, 67], [62, 67], [62, 66], [62, 65], [62, 64], [62, 63], [62, 62], [62, 61], [62, 60], [62, 59], [62, 58], [62, 57], [62, 56], [62, 55], [62, 54], [62, 53], [62, 52], [62, 51], [62, 50], [63, 50], [64, 50], [65, 50], [66, 50], [67, 50], [68, 50], [69, 50], [70, 50], [71, 50], [71, 49], [71, 48], [71, 47], [71, 46], [71, 45], [71, 44], [70, 44], [69, 44], [68, 44], [67, 44], [66, 44], [65, 44], [64, 44], [63, 44], [62, 44], [61, 44], [60, 44], [59, 44], [58, 44], [57, 44], [56, 44], [55, 44], [54, 44], [53, 44], [52, 44], [51, 44], [50, 44], [49, 44], [48, 44], [47, 44], [46, 44], [45, 44], [44, 44], [43, 44], [42, 44], [41, 44], [40, 44], [39, 44], [38, 44], [37, 44], [37, 43], [37, 42], [37, 41], [37, 40], [36, 40], [36, 39], [36, 38], [36, 37], [36, 36], [36, 35], [36, 34], [36, 33], [35, 33], [34, 33], [33, 33], [32, 33], [31, 33], [30, 33], [29, 33], [28, 33], [27, 33], [27, 32], [27, 31], [27, 30], [27, 29], [27, 28], [27, 27], [27, 26], [27, 25], [27, 24], [27, 23], [27, 22], [27, 21], [27, 20], [27, 19], [27, 18], [27, 17], [27, 16], [27, 15], [27, 14], [27, 13], [26, 13], [25, 13], [24, 13], [23, 13], [22, 13], [21, 13], [20, 13], [19, 13], [18, 13], [17, 13], [16, 13], [15, 13], [14, 13], [13, 13], [13, 14], [13, 15], [13, 16], [13, 17], [13, 18], [13, 19], [13, 20], [13, 21], [13, 22], [13, 23], [13, 24], [13, 25], [13, 26], [13, 27], [13, 28], [13, 29], [13, 30], [13, 31], [13, 32], [13, 33], [12, 33], [11, 33], [10, 33], [9, 33], [8, 33], [7, 33], [7, 32], [7, 31], [7, 30], [7, 29], [7, 28], [7, 27], [6, 27], [5, 27], [5, 28], [5, 29], [5, 30], [5, 31], [5, 32], [5, 33], [5, 34], [5, 35], [5, 36], [5, 37], [6, 37], [7, 37], [8, 37], [9, 37], [10, 37], [11, 37], [11, 38], [11, 39], [11, 40], [11, 41], [11, 42], [11, 43], [11, 44], [11, 45], [10, 45], [9, 45], [8, 45], [7, 45], [7, 44], [7, 43], [7, 42], [7, 41], [6, 41], [5, 41], [5, 42], [5, 43], [5, 44], [5, 45], [5, 46], [5, 47], [5, 48], [5, 49], [5, 50], [5, 51], [4, 51], [4, 52], [4, 53], [4, 54], [4, 55], [4, 56], [4, 57], [5, 57], [6, 57], [7, 57], [8, 57], [9, 57], [10, 57], [11, 57], [12, 57], [13, 57], [14, 57], [15, 57], [16, 57], [17, 57], [18, 57], [19, 57], [20, 57], [21, 57], [22, 57], [23, 57], [24, 57], [25, 57], [26, 57], [27, 57], [28, 57], [29, 57], [29, 58], [29, 59], [29, 60], [29, 61], [29, 62], [29, 63], [29, 64], [28, 64], [27, 64], [26, 64], [25, 64], [24, 64], [23, 64], [22, 64], [21, 64], [20, 64], [19, 64], [18, 64], [17, 64], [16, 64], [16, 65], [16, 66], [16, 67], [16, 68], [16, 69], [16, 70], [16, 71], [16, 72], [17, 72], [18, 72], [19, 72], [20, 72], [21, 72], [22, 72], [23, 72], [24, 72], [25, 72], [26, 72], [27, 72], [28, 72], [29, 72], [30, 72], [30, 71], [30, 70], [30, 69], [30, 68], [31, 68], [32, 68], [33, 68], [34, 68], [35, 68], [36, 68], [37, 68], [38, 68], [39, 68], [40, 68], [41, 68], [42, 68], [43, 68], [44, 68], [45, 68], [46, 68], [47, 68], [48, 68], [48, 69], [48, 70], [48, 71], [48, 72], [48, 73], [48, 74], [48, 75], [48, 76], [48, 77], [48, 78], [48, 79], [48, 80], [47, 80], [46, 80], [45, 80], [44, 80], [43, 80], [42, 80], [41, 80], [40, 80], [39, 80], [38, 80], [37, 80], [36, 80], [35, 80], [35, 79], [35, 78], [35, 77], [35, 76], [35, 75], [35, 74], [34, 74], [33, 74], [32, 74], [31, 74], [30, 74], [29, 74], [28, 74], [27, 74], [26, 74], [25, 74], [24, 74], [23, 74], [22, 74], [21, 74], [20, 74], [19, 74], [18, 74], [17, 74], [16, 74], [15, 74], [14, 74], [14, 73], [14, 72], [14, 71], [14, 70], [14, 69], [14, 68], [14, 67], [14, 66], [14, 65], [14, 64], [14, 63], [14, 62], [14, 61], [14, 60], [14, 59], [13, 59], [12, 59], [12, 60], [12, 61], [12, 62], [12, 63], [12, 64], [11, 64], [10, 64], [9, 64], [8, 64], [7, 64], [6, 64], [6, 63], [6, 62], [6, 61], [6, 60], [6, 59], [5, 59], [4, 59], [3, 59], [2, 59], [2, 60], [2, 61], [2, 62], [2, 63], [2, 64], [2, 65], [2, 66], [2, 67], [2, 68], [2, 69], [2, 70], [2, 71], [2, 72], [2, 73], [2, 74], [2, 75], [2, 76], [2, 77], [2, 78], [2, 79], [2, 80], [3, 80], [4, 80], [5, 80], [6, 80], [7, 80], [8, 80], [9, 80], [10, 80], [10, 81]]
    for quadretto in quadrettiDaColorare:
        quadretto[0] = quadretto[0] + xPrimoQuadrettoLabirinto
        quadretto[1] = quadretto[1] + yPrimoQuadrettoLabirinto

    xStrumentoInSuperficeNormale = (xStrumento * GlobalHWVar.gsx // numQuadrettiX) + (GlobalHWVar.gsx // numQuadrettiX // 2)
    yStrumentoInSuperficeNormale = (yStrumento * GlobalHWVar.gsy // numQuadrettiY) + (GlobalHWVar.gsy // numQuadrettiY // 2)
    xStrumentoInSuperficeNormaleVecchia = xStrumentoInSuperficeNormale
    yStrumentoInSuperficeNormaleVecchia = yStrumentoInSuperficeNormale

    superficieDisegni = pygame.Surface((numQuadrettiX, numQuadrettiY), flags=pygame.SRCALPHA)
    GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, coloreGomma)
    GlobalHWVar.disegnaImmagineSuSchermo(sfondoUsandoMatita, (0, 0))
    for quadretto in quadrettiColorabili:
        GlobalHWVar.disegnaRettangoloSuSchermo(superficieDisegni, coloreGomma, (quadretto[0], quadretto[1], dimensioneTrattoGomma, dimensioneTrattoGomma))
    sfondoEnigma = GlobalHWVar.schermo.copy().convert()

    while not esci:
        spostandoCursore = False
        utilizzandoStrumentoInizioCiclo = utilizzandoStrumento
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
                xStrumento = xMouse * numQuadrettiX / GlobalHWVar.gsx
                yStrumento = yMouse * numQuadrettiY / GlobalHWVar.gsy
                if xStrumento < xInizioFoglioSupDisegnabile:
                    xStrumento = xInizioFoglioSupDisegnabile
                elif xStrumento > xFineFoglioSupDisegnabile:
                    xStrumento = xFineFoglioSupDisegnabile
                if yStrumento < yInizioFoglioSupDisegnabile:
                    yStrumento = yInizioFoglioSupDisegnabile
                elif yStrumento > yFineFoglioSupDisegnabile:
                    yStrumento = yFineFoglioSupDisegnabile
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
        if not primoFrame:
            aggiornaInterfacciaPerCambioInput = False
            bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            esci = True
            bottoneDown = False

        if bottoneDown == pygame.K_w or bottoneDown == pygame.K_a or bottoneDown == pygame.K_s or bottoneDown == pygame.K_d:
            tastotempfps = 8
        if pygame.K_w in GlobalHWVar.listaTastiPremuti or "padSu" in GlobalHWVar.listaTastiPremuti:
            if tastotempfps == 0 or tastotempfps == 8:
                spostandoCursore = True
                yStrumento -= unitaSpostamentoCursore
                if yStrumento < yInizioFoglioSupDisegnabile:
                    yStrumento = yInizioFoglioSupDisegnabile
                if tastotempfps == 0:
                    tastotempfps = 2
                else:
                    tastotempfps -= 1
            else:
                spostandoCursore = False
                tastotempfps -= 1
            bottoneDown = False
        if pygame.K_a in GlobalHWVar.listaTastiPremuti or "padSinistra" in GlobalHWVar.listaTastiPremuti:
            if tastotempfps == 0 or tastotempfps == 8:
                spostandoCursore = True
                xStrumento -= unitaSpostamentoCursore
                if xStrumento < xInizioFoglioSupDisegnabile:
                    xStrumento = xInizioFoglioSupDisegnabile
                if tastotempfps == 0:
                    tastotempfps = 2
                else:
                    tastotempfps -= 1
            else:
                spostandoCursore = False
                tastotempfps -= 1
            bottoneDown = False
        if pygame.K_s in GlobalHWVar.listaTastiPremuti or "padGiu" in GlobalHWVar.listaTastiPremuti:
            if tastotempfps == 0 or tastotempfps == 8:
                spostandoCursore = True
                yStrumento += unitaSpostamentoCursore
                if yStrumento > yFineFoglioSupDisegnabile:
                    yStrumento = yFineFoglioSupDisegnabile
                if tastotempfps == 0:
                    tastotempfps = 2
                else:
                    tastotempfps -= 1
            else:
                spostandoCursore = False
                tastotempfps -= 1
            bottoneDown = False
        if pygame.K_d in GlobalHWVar.listaTastiPremuti or "padDestra" in GlobalHWVar.listaTastiPremuti:
            if tastotempfps == 0 or tastotempfps == 8:
                spostandoCursore = True
                xStrumento += unitaSpostamentoCursore
                if xStrumento > xFineFoglioSupDisegnabile:
                    xStrumento = xFineFoglioSupDisegnabile
                if tastotempfps == 0:
                    tastotempfps = 2
                else:
                    tastotempfps -= 1
            else:
                spostandoCursore = False
                tastotempfps -= 1
            bottoneDown = False
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
                if [xStrumento, yStrumento] in quadrettiColorabili:
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
                    if bottoneDown or fattoCLickSulFoglio:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    fattoCLickSulFoglio = False
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

        if utilizzandoStrumento and not esci:
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
                    superficieDisegni = pygame.Surface((numQuadrettiX, numQuadrettiY), flags=pygame.SRCALPHA)
                if cancellaTutto:
                    for quadretto in quadrettiColorati:
                        quadretto[2] = False

                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, coloreGomma)
                if strumentoInUso == "matita":
                    GlobalHWVar.disegnaImmagineSuSchermo(sfondoUsandoMatita, (0, 0))
                elif strumentoInUso == "gomma":
                    GlobalHWVar.disegnaImmagineSuSchermo(sfondoUsandoGomma, (0, 0))
                for quadretto in quadrettiColorabili:
                    GlobalHWVar.disegnaRettangoloSuSchermo(superficieDisegni, coloreGomma, (quadretto[0], quadretto[1], dimensioneTrattoGomma, dimensioneTrattoGomma))
                for quadretto in quadrettiColorati:
                    if quadretto[2]:
                        GlobalHWVar.disegnaRettangoloSuSchermo(superficieDisegni, coloreMatita, (quadretto[0], quadretto[1], dimensioneTrattoGomma, dimensioneTrattoGomma))

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

            xStrumentoInSuperficeNormale = (xStrumento * GlobalHWVar.gsx // numQuadrettiX) + (GlobalHWVar.gsx // numQuadrettiX // 2)
            yStrumentoInSuperficeNormale = (yStrumento * GlobalHWVar.gsy // numQuadrettiY) + (GlobalHWVar.gsy // numQuadrettiY // 2)

            dimXBackground = GlobalHWVar.gpx * 2
            dimYBackground = GlobalHWVar.gpy * 2
            if xStrumentoInSuperficeNormaleVecchia + dimXBackground >= GlobalHWVar.gsx:
                dimXBackground = GlobalHWVar.gsx - xStrumentoInSuperficeNormaleVecchia
            if yStrumentoInSuperficeNormaleVecchia < 0:
                yStrumentoInSuperficeNormaleVecchia = 0
            backgroundStrumento = sfondoEnigma.subsurface(pygame.Rect(xStrumentoInSuperficeNormaleVecchia, yStrumentoInSuperficeNormaleVecchia - GlobalHWVar.gpy * 2, dimXBackground, dimYBackground))
            GlobalHWVar.disegnaImmagineSuSchermo(backgroundStrumento, (xStrumentoInSuperficeNormaleVecchia, yStrumentoInSuperficeNormaleVecchia - GlobalHWVar.gpy * 2))

            if utilizzandoStrumento:
                if strumentoInUso == "matita":
                    GlobalHWVar.disegnaRettangoloSuSchermo(superficieDisegni, coloreMatita, (xStrumento, yStrumento, dimensioneTrattoMatita, dimensioneTrattoMatita))
                    for quadretto in quadrettiColorati:
                        if quadretto[0] == xStrumento and quadretto[1] == yStrumento:
                            quadretto[2] = True
                            break
                elif strumentoInUso == "gomma":
                    GlobalHWVar.disegnaRettangoloSuSchermo(superficieDisegni, coloreGomma, (xStrumento, yStrumento, dimensioneTrattoGomma, dimensioneTrattoGomma))
                    for quadretto in quadrettiColorati:
                        if quadretto[0] == xStrumento and quadretto[1] == yStrumento:
                            quadretto[2] = False
                            break

            superficieDisegniScalata = pygame.transform.scale(superficieDisegni, (GlobalHWVar.gsx, GlobalHWVar.gsy))
            GlobalHWVar.disegnaImmagineSuSchermo(superficieDisegniScalata, (0, 0))

            if strumentoInUso == "matita":
                GlobalHWVar.disegnaImmagineSuSchermo(cursoreMatita, (xStrumentoInSuperficeNormale, yStrumentoInSuperficeNormale - GlobalHWVar.gpx * 2))
            elif strumentoInUso == "gomma":
                GlobalHWVar.disegnaImmagineSuSchermo(cursoreGomma, (xStrumentoInSuperficeNormale, yStrumentoInSuperficeNormale - GlobalHWVar.gpy * 2))

            xStrumentoVecchia = xStrumento
            yStrumentoVecchia = yStrumento
            xStrumentoInSuperficeNormaleVecchia = xStrumentoInSuperficeNormale
            yStrumentoInSuperficeNormaleVecchia = yStrumentoInSuperficeNormale
            cancellaTutto = False
            cambiatoStrumento = False

            if primoFrame:
                FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=1)
            else:
                GlobalHWVar.aggiornaSchermo()

        if utilizzandoStrumentoInizioCiclo and not utilizzandoStrumento:
            percorsoNonCorretto = False
            for quadretto in quadrettiColorati:
                if (quadretto[2] and [quadretto[0], quadretto[1]] not in quadrettiDaColorare) or (
                        not quadretto[2] and [quadretto[0], quadretto[1]] in quadrettiDaColorare):
                    percorsoNonCorretto = True
                    break
            if not percorsoNonCorretto:
                GlobalHWVar.canaleSoundInterazioni.stop()
                avanzamentoStoria += 1
                esci = True

        primoFrame = False
        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockDisegno.tick(GlobalHWVar.fpsDisegno)
    GenericFunc.cambiaVolumeCanale(GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.volumeEffetti)
    GlobalHWVar.configuraCursore(False)

    return avanzamentoStoria
