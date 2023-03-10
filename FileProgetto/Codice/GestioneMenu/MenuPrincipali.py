# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.FunzioniGeneriche.CaricaSalvaPartita as CaricaSalvaPartita
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche
import Codice.GestioneMenu.SottoMenuEquip as SottoMenuEquip
import Codice.GestioneMenu.SottoMenuImpostazioni as SottoMenuImpostazioni
import Codice.GestioneMenu.SottoMenuRobo as SottoMenuRobo
import Codice.GestioneMenu.SottoMenuSalva as SottoMenuSalva
import Codice.GestioneMenu.SottoMenuMapDiario as SottoMenuMapDiario
import Codice.Localizzazione.LocalizInterfaccia as LI


def chiediconferma(conferma):
    puntatore = GlobalImgVar.puntatore
    xp = GlobalHWVar.gsx // 32 * 17.5
    yp = GlobalHWVar.gsy // 18 * 10.2
    schermo_temp = GlobalHWVar.schermo.copy()
    background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalHWVar.gsx, GlobalHWVar.gsy)).convert()
    dark = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
    dark.fill((0, 0, 0, 180))
    GlobalHWVar.disegnaImmagineSuSchermo(background, (0, 0))
    GlobalHWVar.disegnaImmagineSuSchermo(dark, (0, 0))

    schermo_temp = GlobalHWVar.schermo.copy()
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
            if GlobalHWVar.gsx // 32 * 22.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalHWVar.gsy // 18 * 8.8 <= yMouse <= GlobalHWVar.gsy // 18 * 12:
                if GlobalHWVar.gsx // 32 * 9.5 <= xMouse <= GlobalHWVar.gsx // 32 * 16:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalHWVar.gsx // 32 * 10.5
                    yp = GlobalHWVar.gsy // 18 * 10.2
                elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 22.5:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalHWVar.gsx // 32 * 17.5
                    yp = GlobalHWVar.gsy // 18 * 10.2
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
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["Q"] or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
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
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["D"] or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["A"] or bottoneDown == "padDestra" or bottoneDown == "padSinistra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["A"] or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 2:
                    voceMarcata -= 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = GlobalHWVar.gsx // 32 * 10.5
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["D"] or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
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
                GlobalHWVar.disegnaImmagineSuSchermo(dark, (0, 0))
                if conferma == 1:
                    FunzioniGraficheGeneriche.messaggio(LI.TOR_AL_MEN_PRI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6.5, 120, centrale=True)
                elif conferma == 2:
                    FunzioniGraficheGeneriche.messaggio(LI.USC_DAL_GIO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16.1, GlobalHWVar.gsy // 18 * 6.5, 120, centrale=True)
                elif conferma == 3:
                    FunzioniGraficheGeneriche.messaggio(LI.INI_UNA_NUO_PAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6.5, 120, centrale=True)
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(backgroundUpdate1, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaImmagineSuSchermo(backgroundUpdate2, (GlobalHWVar.gsx // 32 * 21, 0))
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio(LI.TAS_DES_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio(LI.B_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio(LI.Q_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 4.5, GlobalHWVar.gsy // 18 * 8.8), (GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 8.8), 1)
            FunzioniGraficheGeneriche.messaggio(LI.SI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 12.5, GlobalHWVar.gsy // 18 * 9.5, 120, centrale=True)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 16), int(GlobalHWVar.gpy * 9.3)), (int(GlobalHWVar.gpx * 16), int(GlobalHWVar.gpy * 11.6)), 1)
            FunzioniGraficheGeneriche.messaggio(LI.NO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.5, GlobalHWVar.gsy // 18 * 9.5, 120, centrale=True)
            primoFrame = False
            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def menu(caricaSalvataggio, gameover):
    xInizialie = 0
    yInizialie = 0
    rxInizialie = 0
    ryInizialie = 0
    pvIniziali = GlobalGameVar.statistichePerLivello[0][0]
    # dimensione: 0-146 (=> 147 variabili)
    # progresso - stanza - x - y - liv - pv - spada - scudo - armatura - armrob - energiarob - tecniche(20) - oggetti(10) - equipaggiamento(30) - batterie(10) - condizioni(20) - gambit(20) -
    # veleno - surriscalda - attp - difp - velp(x2) - efficienza - esperienza - arco - guanti - collana - monete - frecce - faretra -
    # rx - ry - raffredda - autoRic1 - autoRic2 - mosseRimasteRob - npers - nrob - chiaverob - pazzoStrabico - cambiataCastello - moneteSpeseDaRod - tempo di gioco
    datiIniziali = [0, 1, xInizialie, yInizialie, 1, pvIniziali, 0, 0, 0, 0, 0,  # <- statistiche
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # <- tecniche
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  # <- oggetti
        2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0,  # <- equpaggiamento
        2, 0, 0, 0, 0, -1, -1, -1, -1, -1,  # <- batterie (sono utilizzati solo i primi 5)
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # <- condizioni
        0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1,  # <- gambit
        False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # <- altre statistiche
        rxInizialie, ryInizialie, -1, -1, -1, 0, 1, 3, False,  # <- info aggiunte per poter salvare ovunque
        False, False, 0, 0  # <- pazzoStrabico, cambiataCastello, moneteSpeseDaRod e tempo di gioco
        ]

    # posizione porte e cofanetti nel vettore dati
    tuttePorte = GlobalGameVar.initVetPorteGlobale[:]
    tuttiCofanetti = GlobalGameVar.initVetCofanettiGlobale[:]

    lunghezzadati = len(datiIniziali)
    lunghezzadatiPorte = len(tuttePorte)
    lunghezzadatiCofanetti = len(tuttiCofanetti)

    if gameover:
        dati = GlobalGameVar.vetDatiSalvataggioGameOver[0][:]
        tuttePorte = GlobalGameVar.vetDatiSalvataggioGameOver[1][:]
        tuttiCofanetti = GlobalGameVar.vetDatiSalvataggioGameOver[2][:]
        listaNemiciTotali = GenericFunc.copiaListaDiOggettiConImmagini(GlobalGameVar.vetDatiSalvataggioGameOver[3], True)
        listaEsche = GlobalGameVar.vetDatiSalvataggioGameOver[4][:]
        listaMonete = GlobalGameVar.vetDatiSalvataggioGameOver[5][:]
        stanzeGiaVisitate = GlobalGameVar.vetDatiSalvataggioGameOver[6][:]
        listaPersonaggiTotali = GenericFunc.copiaListaDiOggettiConImmagini(GlobalGameVar.vetDatiSalvataggioGameOver[7], False)
        listaAvanzamentoDialoghi = GlobalGameVar.vetDatiSalvataggioGameOver[8][:]
        oggettiRimastiAHans = GlobalGameVar.vetDatiSalvataggioGameOver[9][:]
        ultimoObbiettivoColco = GlobalGameVar.vetDatiSalvataggioGameOver[10][:]
        obbiettivoCasualeColco = GenericFunc.copiaNemico(GlobalGameVar.vetDatiSalvataggioGameOver[11])
        idDialoghiLettiTemp = GlobalGameVar.idDialoghiLettiGameOver[:]
        GlobalGameVar.inizializzaVariabiliGlobali()
        GlobalGameVar.idDialoghiLetti = idDialoghiLettiTemp
        GlobalGameVar.idDialoghiLettiGameOver = idDialoghiLettiTemp[:]
        return dati, tuttePorte, tuttiCofanetti, listaNemiciTotali, listaEsche, listaMonete, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco

    if caricaSalvataggio:
        GlobalGameVar.inizializzaVariabiliGlobali()
        datiTotaliAttuali, datiTotaliGameover, errore = CaricaSalvaPartita.caricaPartita(caricaSalvataggio, lunghezzadati, lunghezzadatiPorte, lunghezzadatiCofanetti, False)
        dati = datiTotaliAttuali[0]
        tuttePorte = datiTotaliAttuali[1]
        tuttiCofanetti = datiTotaliAttuali[2]
        listaNemiciTotali = datiTotaliAttuali[3]
        listaEsche = datiTotaliAttuali[4]
        listaMonete = datiTotaliAttuali[5]
        stanzeGiaVisitate = datiTotaliAttuali[6]
        listaPersonaggiTotali = datiTotaliAttuali[7]
        listaAvanzamentoDialoghi = datiTotaliAttuali[8]
        oggettiRimastiAHans = datiTotaliAttuali[9]
        ultimoObbiettivoColco = datiTotaliAttuali[10]
        obbiettivoCasualeColco = datiTotaliAttuali[11]
        GlobalGameVar.idDialoghiLetti = datiTotaliAttuali[12]
        datiGameover = datiTotaliGameover[0]
        tutteporteGameover = datiTotaliGameover[1]
        tutticofanettiGameover = datiTotaliGameover[2]
        listaNemiciTotaliGameover = datiTotaliGameover[3]
        listaEscheGameover = datiTotaliGameover[4]
        listaMoneteGameover = datiTotaliGameover[5]
        stanzeGiaVisitateGameover = datiTotaliGameover[6]
        listaPersonaggiTotaliGameover = datiTotaliGameover[7]
        listaAvanzamentoDialoghiGameover = datiTotaliGameover[8]
        oggettiRimastiAHansGameover = datiTotaliGameover[9]
        ultimoObbiettivoColcoGameover = datiTotaliGameover[10]
        obbiettivoCasualeColcoGameover = datiTotaliGameover[11]
        GlobalGameVar.idDialoghiLettiGameOver = datiTotaliGameover[12]

        GlobalGameVar.vetDatiSalvataggioGameOver = [datiGameover, tutteporteGameover, tutticofanettiGameover, listaNemiciTotaliGameover, listaEscheGameover, listaMoneteGameover, stanzeGiaVisitateGameover, listaPersonaggiTotaliGameover, listaAvanzamentoDialoghiGameover, oggettiRimastiAHansGameover, ultimoObbiettivoColcoGameover, obbiettivoCasualeColcoGameover]
        GlobalGameVar.numSalvataggioCaricato = caricaSalvataggio
        return dati, tuttePorte, tuttiCofanetti, listaNemiciTotali, listaEsche, listaMonete, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco

    # carico subito tutti i salvataggi
    SottoMenuSalva.ricaricaSalvataggi(lunghezzadati, lunghezzadatiPorte, lunghezzadatiCofanetti)

    if not GlobalHWVar.canaleSoundCanzone.get_busy() or GlobalGameVar.canzoneAttuale != "00-Menu":
        GlobalGameVar.canzoneAttuale = "00-Menu"
        canzone = CaricaFileProgetto.loadSound("Risorse/Audio/Canzoni/" + GlobalGameVar.canzoneAttuale + ".wav")
        GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
    illuminaScritteDopoCaricamento = False
    illuminaTuttoLoSchermo = False
    if GlobalHWVar.primoAvvio:
        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
        GlobalHWVar.primoAvvio = False
        illuminaScritteDopoCaricamento = True
    else:
        illuminaTuttoLoSchermo = True

    xp = GlobalHWVar.gsx // 32 * 1.5
    yp = GlobalHWVar.gsy // 18 * 2.5
    voceMarcata = 1
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    mostraTutorial = False
    imgOscuraPuntatore = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8
    while True:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        suTutorial = False
        suTogliTutorial = False
        if GlobalHWVar.mouseVisibile:
            if not mostraTutorial:
                if 0 <= xMouse <= GlobalHWVar.gsx // 32 * 7.7 and GlobalHWVar.gsy // 18 * 16.2 <= yMouse <= GlobalHWVar.gsy:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    suTutorial = True
                elif 0 <= xMouse <= GlobalHWVar.gsx // 32 * 11:
                    if GlobalHWVar.gsy // 18 * 1.5 <= yMouse <= GlobalHWVar.gsy // 18 * 4:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalHWVar.gsx // 32 * 1.5
                        yp = GlobalHWVar.gsy // 18 * 2.5
                    elif GlobalHWVar.gsy // 18 * 4 <= yMouse <= GlobalHWVar.gsy // 18 * 6.5:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalHWVar.gsx // 32 * 1.5
                        yp = GlobalHWVar.gsy // 18 * 5
                    elif GlobalHWVar.gsy // 18 * 6.5 <= yMouse <= GlobalHWVar.gsy // 18 * 9:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 3
                        xp = GlobalHWVar.gsx // 32 * 1.5
                        yp = GlobalHWVar.gsy // 18 * 7.5
                    elif GlobalHWVar.gsy // 18 * 11.5 <= yMouse <= GlobalHWVar.gsy // 18 * 14:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 4
                        xp = GlobalHWVar.gsx // 32 * 1.5
                        yp = GlobalHWVar.gsy // 18 * 12.5
                    else:
                        if not GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(True)
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            else:
                if GlobalHWVar.gsx // 32 * 22 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    suTogliTutorial = True
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)

        # gestione degli input
        menuConferma = False
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["Q"] or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio") and mostraTutorial:
            if mostraTutorial:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                mostraTutorial = False
                primoFrame = True
            bottoneDown = False
        if bottoneDown == pygame.K_ESCAPE or bottoneDown == "mouseCentrale" or bottoneDown == "padStart":
            if not mostraTutorial:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                mostraTutorial = True
                primoFrame = True
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                mostraTutorial = False
                primoFrame = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if suTutorial and bottoneDown == "mouseSinistro":
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                mostraTutorial = True
                primoFrame = True
            else:
                if not mostraTutorial:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    # nuova partita
                    if voceMarcata == 1:
                        menuConferma = "inizia"

                    # carica partita
                    if voceMarcata == 2:
                        n, inutile = SottoMenuSalva.scegli_sal(False, lunghezzadati, lunghezzadatiPorte, lunghezzadatiCofanetti, [], [], [], [], [], [], [], [], [], [], [], False)

                        # lettura salvataggio
                        if n != -1:
                            FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False)
                            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone, GlobalHWVar.canaliSoundSottofondoAmbientale], [0, 0], False, posizioneCanaleMusica=0)
                            GlobalHWVar.canaleSoundCanzone.stop()
                            GlobalHWVar.canaliSoundSottofondoAmbientale.arresta()
                            GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
                            GlobalHWVar.canaliSoundSottofondoAmbientale.settaVolume(GlobalHWVar.volumeEffetti)
                            GlobalGameVar.inizializzaVariabiliGlobali()
                            datiTotaliAttuali, datiTotaliGameover, errore = CaricaSalvaPartita.caricaPartita(n, lunghezzadati, lunghezzadatiPorte, lunghezzadatiCofanetti, False)
                            dati = datiTotaliAttuali[0]
                            tuttePorte = datiTotaliAttuali[1]
                            tuttiCofanetti = datiTotaliAttuali[2]
                            datiNemici = datiTotaliAttuali[3]
                            datiEsche = datiTotaliAttuali[4]
                            datiMonete = datiTotaliAttuali[5]
                            stanzeGiaVisitate = datiTotaliAttuali[6]
                            listaPersonaggiTotali = datiTotaliAttuali[7]
                            listaAvanzamentoDialoghi = datiTotaliAttuali[8]
                            oggettiRimastiAHans = datiTotaliAttuali[9]
                            ultimoObbiettivoColco = datiTotaliAttuali[10]
                            obbiettivoCasualeColco = datiTotaliAttuali[11]
                            GlobalGameVar.idDialoghiLetti = datiTotaliAttuali[12]
                            datiGameover = datiTotaliGameover[0]
                            tutteporteGameover = datiTotaliGameover[1]
                            tutticofanettiGameover = datiTotaliGameover[2]
                            listaNemiciTotaliGameover = datiTotaliGameover[3]
                            listaEscheGameover = datiTotaliGameover[4]
                            listaMoneteGameover = datiTotaliGameover[5]
                            stanzeGiaVisitateGameover = datiTotaliGameover[6]
                            listaPersonaggiTotaliGameover = datiTotaliGameover[7]
                            listaAvanzamentoDialoghiGameover = datiTotaliGameover[8]
                            oggettiRimastiAHansGameover = datiTotaliGameover[9]
                            ultimoObbiettivoColcoGameover = datiTotaliGameover[10]
                            obbiettivoCasualeColcoGameover = datiTotaliGameover[11]
                            GlobalGameVar.idDialoghiLettiGameOver = datiTotaliGameover[12]

                            GlobalGameVar.vetDatiSalvataggioGameOver = [datiGameover, tutteporteGameover, tutticofanettiGameover, listaNemiciTotaliGameover, listaEscheGameover, listaMoneteGameover, stanzeGiaVisitateGameover, listaPersonaggiTotaliGameover, listaAvanzamentoDialoghiGameover, oggettiRimastiAHansGameover, ultimoObbiettivoColcoGameover, obbiettivoCasualeColcoGameover]
                            if dati:
                                GlobalGameVar.numSalvataggioCaricato = n
                                return dati, tuttePorte, tuttiCofanetti, datiNemici, datiEsche, datiMonete, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco
                        primoFrame = True

                    # Impostazioni
                    if voceMarcata == 3:
                        inutile = SottoMenuImpostazioni.menuImpostazioni(True, False, False, False)
                        primoFrame = True

                    # esci dal gioco
                    if voceMarcata == 4:
                        menuConferma = "esci"
                else:
                    if suTogliTutorial and bottoneDown == "mouseSinistro":
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                        mostraTutorial = False
                        primoFrame = True
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if not mostraTutorial and (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == "padGiu" or bottoneDown == "padSu"):
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if primoMovimento or primoFrame or (tastoMovimentoPremuto and tastotempfps == 0) or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            if not mostraTutorial:
                if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                    if voceMarcata != 4:
                        if voceMarcata == 1:
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = GlobalHWVar.gsy // 18 * 5
                        elif voceMarcata == 2:
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = GlobalHWVar.gsy // 18 * 7.5
                        elif voceMarcata == 3:
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = GlobalHWVar.gsy // 18 * 12.5
                        voceMarcata += 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = GlobalHWVar.gsy // 18 * 2.5
                        voceMarcata -= 3
                if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                    if voceMarcata != 1:
                        if voceMarcata == 2:
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = GlobalHWVar.gsy // 18 * 2.5
                        elif voceMarcata == 3:
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = GlobalHWVar.gsy // 18 * 5
                        elif voceMarcata == 4:
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = GlobalHWVar.gsy // 18 * 7.5
                        voceMarcata -= 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = GlobalHWVar.gsy // 18 * 12.5
                        voceMarcata += 3
                if not primoMovimento and tastoMovimentoPremuto:
                    tastotempfps = 2

                # per ottimizzare
                if primoFrame:
                    primoFrame = False
                    aggiornaInterfacciaPerCambioInput = True
                    puntatore = GlobalImgVar.puntatore
                    xp = GlobalHWVar.gsx // 32 * 1.5
                    if voceMarcata == 1:
                        yp = GlobalHWVar.gsy // 18 * 2.5
                    if voceMarcata == 2:
                        yp = GlobalHWVar.gsy // 18 * 5
                    if voceMarcata == 3:
                        yp = GlobalHWVar.gsy // 18 * 7.5
                    if voceMarcata == 4:
                        yp = GlobalHWVar.gsy // 18 * 12.5
                    GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
                    FunzioniGraficheGeneriche.messaggio(LI.OFF[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscurino, GlobalHWVar.gsx // 32 * 1.6, (GlobalHWVar.gsy // 18 * 1.5) + (GlobalHWVar.gpy // 8), 210)
                    FunzioniGraficheGeneriche.messaggio(LI.TO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscurino, GlobalHWVar.gsx // 32 * 1.6, (GlobalHWVar.gsy // 18 * 4.5) + (GlobalHWVar.gpy // 8), 210)
                    FunzioniGraficheGeneriche.messaggio(LI.SLEEP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscurino, GlobalHWVar.gsx // 32 * 1.6, (GlobalHWVar.gsy // 18 * 7.5) + (GlobalHWVar.gpy // 8), 210)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalGameVar.schemataDiCaricamento, (0, 0))
                    FunzioniGraficheGeneriche.messaggio(LI.INIZIA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2.5, GlobalHWVar.gsy // 18 * 2, 90)
                    FunzioniGraficheGeneriche.messaggio(LI.CONTINUA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2.5, GlobalHWVar.gsy // 18 * 4.5, 90)
                    FunzioniGraficheGeneriche.messaggio(LI.IMPOSTAZIONI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2.5, GlobalHWVar.gsy // 18 * 7, 90)
                    FunzioniGraficheGeneriche.messaggio(LI.ESCI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2.5, GlobalHWVar.gsy // 18 * 12, 90)
                    sreen_temp = GlobalHWVar.schermo.copy()
                    imgOscuraPuntatore = sreen_temp.subsurface(pygame.Rect(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 11.5)).convert()
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(imgOscuraPuntatore, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 2))
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 1.5) - 1, int(GlobalHWVar.gpy * 1.5)), (int(GlobalHWVar.gpx * 1.5) - 1, int(GlobalHWVar.gpy * 14)), 2)
                if aggiornaInterfacciaPerCambioInput:
                    aggiornaInterfacciaPerCambioInput = False
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (0, GlobalHWVar.gsy // 18 * 16.5, GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2))
                    if GlobalHWVar.mouseVisibile:
                        FunzioniGraficheGeneriche.messaggio(LI.TAS_CEN_COM[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 16.8, 50, centrale=True)
                    elif GlobalHWVar.usandoIlController:
                        FunzioniGraficheGeneriche.messaggio(LI.MENU_COMANDI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 16.8, 50, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio(LI.ESC_COMANDI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 16.8, 50, centrale=True)

                if menuConferma:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xp, yp))
                    schermo_temp = GlobalHWVar.schermo.copy()
                    background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalHWVar.gsx, GlobalHWVar.gsy)).convert()
                    if menuConferma == "inizia":
                        inutile, conferma = chiediconferma(3)
                        if conferma:
                            FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False)
                            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone, GlobalHWVar.canaliSoundSottofondoAmbientale], [0, 0], False, posizioneCanaleMusica=0)
                            GlobalHWVar.canaleSoundCanzone.stop()
                            GlobalHWVar.canaliSoundSottofondoAmbientale.arresta()
                            GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
                            GlobalHWVar.canaliSoundSottofondoAmbientale.settaVolume(GlobalHWVar.volumeEffetti)
                            GlobalGameVar.inizializzaVariabiliGlobali()
                            dati = datiIniziali
                            xInizialie = GlobalHWVar.gsx // 32 * 15
                            yInizialie = GlobalHWVar.gsy // 18 * 7
                            rxInizialie = xInizialie
                            ryInizialie = yInizialie
                            dati[2] = xInizialie
                            dati[3] = yInizialie
                            dati[134] = rxInizialie
                            dati[135] = ryInizialie
                            datiNemici = []
                            datiEsche = []
                            datiMonete = []
                            stanzeGiaVisitate = []
                            listaPersonaggiTotali = []
                            listaAvanzamentoDialoghi = []
                            oggettiRimastiAHans = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                            ultimoObbiettivoColco = []
                            obbiettivoCasualeColco = False
                            i = 0
                            while i < len(tuttePorte):
                                tuttePorte[i + 1] = tuttePorte[i + 1] * GlobalHWVar.gpx
                                tuttePorte[i + 2] = tuttePorte[i + 2] * GlobalHWVar.gpy
                                i += 4
                            i = 0
                            while i < len(tuttiCofanetti):
                                tuttiCofanetti[i + 1] = tuttiCofanetti[i + 1] * GlobalHWVar.gpx
                                tuttiCofanetti[i + 2] = tuttiCofanetti[i + 2] * GlobalHWVar.gpy
                                i += 4
                            GlobalGameVar.numSalvataggioCaricato = 0
                            return dati, tuttePorte, tuttiCofanetti, datiNemici, datiEsche, datiMonete, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco
                        else:
                            GlobalHWVar.disegnaImmagineSuSchermo(background, (0, 0))
                    else:
                        inizio, inutile = chiediconferma(2)
                        if not inizio:
                            GlobalHWVar.disegnaImmagineSuSchermo(background, (0, 0))
                    aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            elif primoFrame or aggiornaInterfacciaPerCambioInput:
                primoFrame = False
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio(LI.COMANDI_MOUSE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (GlobalHWVar.gsx // 32 * 0.4, GlobalHWVar.gsy // 18 * 6))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 6))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (GlobalHWVar.gsx // 32 * 21.4, GlobalHWVar.gsy // 18 * 6))

                    FunzioniGraficheGeneriche.messaggio(LI.SU_CAS_LIB__MOV[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 6.7, 35)
                    FunzioniGraficheGeneriche.messaggio(LI.SU_CAS_INT__INT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 7.2, 35)
                    FunzioniGraficheGeneriche.messaggio(LI.SU_IMP__ATT__DIS_IMP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 7.7, 35)
                    FunzioniGraficheGeneriche.messaggio(LI.SU_STA_PER__MEN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 8.2, 35)
                    FunzioniGraficheGeneriche.messaggio(LI.SU_ICO_LE__MOD_INT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 8.7, 35)
                    FunzioniGraficheGeneriche.messaggio(LI.SU_ICO_SA__SAL_TUR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 9.2, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 9.8), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 9.8), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.MODALIT_INTERAZIONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 11.1, 35)
                    FunzioniGraficheGeneriche.messaggio(LI.SU_ICO_LE__RIM_SEL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 11.6, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 13.2), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 13.2), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 14.7, 35)

                    FunzioniGraficheGeneriche.messaggio(LI.SU_CAS_NEM__INQ__ATT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 6.7, 35)
                    FunzioniGraficheGeneriche.messaggio(LI.SU_CAS_INT__INT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 7.2, 35)
                    FunzioniGraficheGeneriche.messaggio(LI.SU_IMP__ATT__DIS_IMP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 7.7, 35)
                    FunzioniGraficheGeneriche.messaggio(LI.SU_STA_PER__MEN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 8.2, 35)
                    FunzioniGraficheGeneriche.messaggio(LI.SU_ICO_LE__MOD_MOV[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 8.7, 35)
                    FunzioniGraficheGeneriche.messaggio(LI.SU_ICO_SA__SAL_TUR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 9.2, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 9.8), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 9.8), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.MODALIT_MOVIMENTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 11.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 13.2), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 13.2), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 14.7, 35)

                    FunzioniGraficheGeneriche.messaggio(LI.SELEZIONA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 7.8, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 9.8), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 9.8), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.IND__ESC[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 11.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 13.2), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 13.2), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.CAM_OPE_SE_CON[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 14.5, 35)
                    FunzioniGraficheGeneriche.messaggio(LI.ESC_SE_CON[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 15, 35)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio(LI.COMANDI_CONTROLLER[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInGioco, (GlobalHWVar.gsx // 32 * 0.4, GlobalHWVar.gsy // 18 * 6))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInGioco, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 6))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInMenu, (GlobalHWVar.gsx // 32 * 21.4, GlobalHWVar.gsy // 18 * 6))

                    FunzioniGraficheGeneriche.messaggio(LI.MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 6.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 7.5), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 7.5), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.CAM_BER_INQ[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 8.05, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 8.85), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 8.85), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.DESELEZIONA_BERSAGLIO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 9.4, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 10.2), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 10.2), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.MODALIT_INTERAZIONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 10.75, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 11.55), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 11.55), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.MOVIMENTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 12.1, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 12.9), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 12.9), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.ATT__DIS_IMP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 13.45, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 14.25), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 14.25), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.SALTA_TURNO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 14.8, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 15.6), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 15.6), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.INTERAGISCI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 16.15, 35)

                    FunzioniGraficheGeneriche.messaggio(LI.MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 6.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 7.5), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 7.5), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.PUN_SUL_PRO_BER[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 8.05, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 8.85), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 8.85), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.MODALIT_MOVIMENTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 9.4, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 10.2), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 10.2), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.INQ_BER_PUN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 10.75, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 11.55), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 11.55), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.SPOSTA_PUNTATORE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 12.1, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 12.9), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 12.9), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.ATT__DIS_IMP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 13.45, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 14.25), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 14.25), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.SALTA_TURNO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 14.8, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 15.6), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 15.6), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.ATT__INT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 16.15, 35)

                    FunzioniGraficheGeneriche.messaggio(LI.ESC_SE_CON[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 8.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 9.2), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 9.2), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.IND__ESC[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 9.85, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 10.75), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 10.75), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.SPOSTA_PUNTATORE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 11.4, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 12.3), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 12.3), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.CAM_OPE_SE_CON[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 12.95, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 13.85), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 13.85), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.SELEZIONA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 14.5, 35)
                else:
                    FunzioniGraficheGeneriche.messaggio(LI.COMANDI_TASTIERA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInGioco, (GlobalHWVar.gsx // 32 * 0.4, GlobalHWVar.gsy // 18 * 6))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInGioco, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 6))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInMenu, (GlobalHWVar.gsx // 32 * 21.4, GlobalHWVar.gsy // 18 * 6))

                    FunzioniGraficheGeneriche.messaggio(LI.MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 6.6, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 7.2), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 7.2), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.CAM_BER_INQ[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 7.73, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 8.43), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 8.43), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.DESELEZIONA_BERSAGLIO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 8.96, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 9.66), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 9.66), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.MODALIT_INTERAZIONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 10.19, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 10.89), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 10.89), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.MOVIMENTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 11.9, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 13.2), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 13.2), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.ATT__DIS_IMP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 13.73, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 14.43), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 14.43), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.SALTA_TURNO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 14.96, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 15.66), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 15.66), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.INTERAGISCI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 16.19, 35)

                    FunzioniGraficheGeneriche.messaggio(LI.MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 6.6, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 7.2), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 7.2), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.PUN_SUL_PRO_BER[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 7.73, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 8.43), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 8.43), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.MODALIT_MOVIMENTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 8.96, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 9.66), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 9.66), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.INQ_BER_PUN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 10.19, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 10.89), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 10.89), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.SPOSTA_PUNTATORE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 11.9, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 13.2), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 13.2), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.ATT__DIS_IMP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 13.73, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 14.43), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 14.43), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.SALTA_TURNO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 14.96, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 15.66), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 15.66), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.ATT__INT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 16.19, 35)

                    FunzioniGraficheGeneriche.messaggio(LI.ESC_SE_CON[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 8.05, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 8.7), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 8.7), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.IND__ESC[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 9.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 10.1), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 10.1), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.SPOSTA_PUNTATORE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 11.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 12.6), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 12.6), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.CAM_OPE_SE_CON[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 13.2, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 14), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 14), 2)
                    FunzioniGraficheGeneriche.messaggio(LI.SELEZIONA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 14.6, 35)
                FunzioniGraficheGeneriche.messaggio(LI.MOD_MOVIMENTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                FunzioniGraficheGeneriche.messaggio(LI.MOD_INTERAZIONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                FunzioniGraficheGeneriche.messaggio(LI.MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 26.5, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 5.8), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 5.8), 1)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 4), (GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 5.4), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 6.2), (GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 17), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 4), (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 5.4), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 6.2), (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 17), 2)
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio(LI.TAS_DES__CEN_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio(LI.MEN__B_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio(LI.ESC__Q_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
            if not illuminaScritteDopoCaricamento:
                if illuminaTuttoLoSchermo:
                    illuminaTuttoLoSchermo = False
                    FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=2)
                else:
                    GlobalHWVar.aggiornaSchermo()

        if illuminaScritteDopoCaricamento:
            illuminaScritteDopoCaricamento = False

            vetImg = []
            screen = GlobalHWVar.schermo.copy().convert()
            rect = pygame.display.get_surface().get_rect()
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((50, 50, 50, 250))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((50, 50, 50, 200))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((50, 50, 50, 150))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((50, 50, 50, 100))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((50, 50, 50, 60))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((50, 50, 50, 20))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            i = 0
            while i <= 5:
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(vetImg[i], (0, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalGameVar.schemataDiCaricamento, (0, 0))
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 1.5) - 1, int(GlobalHWVar.gpy * 1.5)), (int(GlobalHWVar.gpx * 1.5) - 1, int(GlobalHWVar.gpy * 14)), 2)
                GlobalHWVar.aggiornaSchermo()
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                i += 1
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalGameVar.schemataDiCaricamento, (0, 0))
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 1.5) - 1, int(GlobalHWVar.gpy * 1.5)), (int(GlobalHWVar.gpx * 1.5) - 1, int(GlobalHWVar.gpy * 14)), 2)
            GlobalHWVar.aggiornaSchermo()
        else:
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def start(dati, tutteporte, tutticofanetti, listaNemiciTotali, vettoreEsche, vettoreDenaro, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco, colcoInCasellaVista):
    robosta = GlobalImgVar.robograf1
    puntatore = GlobalImgVar.puntatore
    puntatoreVecchio = GlobalImgVar.puntatorevecchio
    avvelenatosta = GlobalImgVar.avvelenatoMenu
    surriscaldatosta = GlobalImgVar.surriscaldatoMenu
    attaccopiusta = GlobalImgVar.attaccopiuMenu
    difesapiusta = GlobalImgVar.difesapiuMenu
    velocitapiusta = GlobalImgVar.velocitapiuMenu
    efficienzapiusta = GlobalImgVar.efficienzapiuMenu
    usandoRod = False
    if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= dati[0] < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
        usandoRod = True
    usandoCalcolatore = False
    if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= dati[0] < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
        usandoCalcolatore = True
    if dati[133] == 0 or usandoRod:
        faretraFrecceStart = GlobalImgVar.faretraFrecceStart0
    elif dati[133] == 1:
        faretraFrecceStart = GlobalImgVar.faretraFrecceStart1
    elif dati[133] == 2:
        faretraFrecceStart = GlobalImgVar.faretraFrecceStart2
    elif dati[133] == 3:
        faretraFrecceStart = GlobalImgVar.faretraFrecceStart3
    else:
        faretraFrecceStart = 0
    maxFrecce = GlobalGameVar.frecceMaxPerFaretra[dati[133]]
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 5
    carim = True
    risposta = False
    attacco = 0
    conferma = 0
    inizio = False
    voceMarcata = 1
    caricaSalvataggio = False
    aperturaSettaColcoNonRiuscita = False
    cambiatoRisoluzione = False
    # faccio in modo di poter accedere al menu "setta impo" alla fine del gioco solo quando sei nel laboratorio segreto
    mostraImpoFineGioco = False
    if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"] and dati[1] == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        colcoInCasellaVista = True
        mostraImpoFineGioco = True

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone, GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeCanzoni / 2.0, GlobalHWVar.volumeEffetti / 3.0], True, posizioneCanaleMusica=0)

    if GlobalGameVar.dictStanze["labirinto1"] <= dati[1] <= GlobalGameVar.dictStanze["labirinto23"]:
        risposta = SottoMenuMapDiario.menuMappa(dati[0], tutticofanetti, apriLabirinto=True)
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
            if GlobalHWVar.gsx // 32 * 22 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 11:
                if GlobalHWVar.gsy // 18 * 4.8 <= yMouse <= GlobalHWVar.gsy // 18 * 5.8:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 5
                elif GlobalHWVar.gsy // 18 * 5.8 <= yMouse <= GlobalHWVar.gsy // 18 * 6.8:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 6
                elif dati[0] >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"] and GlobalHWVar.gsy // 18 * 6.8 <= yMouse <= GlobalHWVar.gsy // 18 * 7.8:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 7
                elif dati[0] >= GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"] and GlobalHWVar.gsy // 18 * 7.8 <= yMouse <= GlobalHWVar.gsy // 18 * 8.8:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 8
                elif dati[0] >= GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"] and GlobalHWVar.gsy // 18 * 8.8 <= yMouse <= GlobalHWVar.gsy // 18 * 9.8:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 9
                elif GlobalHWVar.gsy // 18 * 12.8 <= yMouse <= GlobalHWVar.gsy // 18 * 13.8:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 13
                elif GlobalHWVar.gsy // 18 * 13.8 <= yMouse <= GlobalHWVar.gsy // 18 * 14.8:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 14
                elif GlobalHWVar.gsy // 18 * 14.8 <= yMouse <= GlobalHWVar.gsy // 18 * 15.8:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 15
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
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["Q"] or bottoneDown == pygame.K_ESCAPE or bottoneDown == "mouseDestro" or bottoneDown == "mouseCentrale" or bottoneDown == "padCerchio" or bottoneDown == "padStart":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if suTornaIndietro and bottoneDown == "mouseSinistro":
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                risposta = True
            else:
                # non far cliccare su "Setta Colco" se Colco non ?? in una casella vista
                if voceMarcata == 3 and not colcoInCasellaVista:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if not usandoRod and not usandoCalcolatore:
                        aperturaSettaColcoNonRiuscita = True
                elif (voceMarcata == 2 or voceMarcata == 4 or voceMarcata == 5) and usandoRod:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif (voceMarcata == 1 or voceMarcata == 2 or voceMarcata == 4 or voceMarcata == 5) and usandoCalcolatore:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    primoFrame = True
                    # oggetti
                    if voceMarcata == 1:
                        dati, attacco, risposta = SottoMenuEquip.oggetti(dati, colcoInCasellaVista)
                        if attacco != 0:
                            risposta = True
                        carim = True
                    # equip pers
                    if voceMarcata == 2:
                        dati, risposta = SottoMenuEquip.equip(dati)
                        carim = True
                    # equip robot
                    if voceMarcata == 3:
                        dati, risposta = SottoMenuRobo.equiprobo(dati)
                        carim = True
                    # mappa
                    if voceMarcata == 4:
                        risposta = SottoMenuMapDiario.menuMappa(dati[0], tutticofanetti)
                    # diario
                    if voceMarcata == 5:
                        risposta = SottoMenuMapDiario.menuDiario(dati[0], listaAvanzamentoDialoghi)
                    # salva
                    if voceMarcata == 6:
                        # azioneFatta contiene 3 se ?? stato fatto un salvataggio, altrimenti 1 se ?? stato caricato un salvataggio
                        n, azioneFatta = SottoMenuSalva.scegli_sal(True, len(dati), len(tutteporte), len(tutticofanetti), tutteporte, tutticofanetti, vettoreEsche, vettoreDenaro, dati, listaNemiciTotali, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco)
                        if n != -1 and azioneFatta == 1:
                            FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False)
                            caricaSalvataggio = n
                            risposta = True
                    # impostazioni
                    if voceMarcata == 7:
                        gpxPreCambioRisoluzione = GlobalHWVar.gpx
                        gpyPreCambioRisoluzione = GlobalHWVar.gpy
                        cambiatoRisoluzione = SottoMenuImpostazioni.menuImpostazioni(False, True, dati[0], cambiatoRisoluzione)
                        if cambiatoRisoluzione:
                            dati, tutteporte, tutticofanetti, listaNemiciTotali, vettoreEsche, vettoreDenaro, listaPersonaggiTotali, ultimoObbiettivoColco, obbiettivoCasualeColco = GenericFunc.sistemaImgPerCambioRisoluzione(dati, tutteporte, tutticofanetti, listaNemiciTotali, vettoreEsche, vettoreDenaro, listaPersonaggiTotali, ultimoObbiettivoColco, obbiettivoCasualeColco, gpxPreCambioRisoluzione, gpyPreCambioRisoluzione)
                            GlobalGameVar.vetDatiSalvataggioGameOver[0], GlobalGameVar.vetDatiSalvataggioGameOver[1], GlobalGameVar.vetDatiSalvataggioGameOver[2], GlobalGameVar.vetDatiSalvataggioGameOver[3], GlobalGameVar.vetDatiSalvataggioGameOver[4], GlobalGameVar.vetDatiSalvataggioGameOver[5], GlobalGameVar.vetDatiSalvataggioGameOver[7], GlobalGameVar.vetDatiSalvataggioGameOver[10], GlobalGameVar.vetDatiSalvataggioGameOver[11] = GenericFunc.sistemaImgPerCambioRisoluzione(GlobalGameVar.vetDatiSalvataggioGameOver[0], GlobalGameVar.vetDatiSalvataggioGameOver[1], GlobalGameVar.vetDatiSalvataggioGameOver[2], GlobalGameVar.vetDatiSalvataggioGameOver[3], GlobalGameVar.vetDatiSalvataggioGameOver[4], GlobalGameVar.vetDatiSalvataggioGameOver[5], GlobalGameVar.vetDatiSalvataggioGameOver[7], GlobalGameVar.vetDatiSalvataggioGameOver[10], GlobalGameVar.vetDatiSalvataggioGameOver[11], gpxPreCambioRisoluzione, gpyPreCambioRisoluzione)

                            xp = GlobalHWVar.gsx // 32 * 1
                            yp = GlobalHWVar.gsy // 18 * 14
                            robosta = GlobalImgVar.robograf1
                            puntatore = GlobalImgVar.puntatore
                            puntatoreVecchio = GlobalImgVar.puntatorevecchio
                            avvelenatosta = GlobalImgVar.avvelenatoMenu
                            surriscaldatosta = GlobalImgVar.surriscaldatoMenu
                            attaccopiusta = GlobalImgVar.attaccopiuMenu
                            difesapiusta = GlobalImgVar.difesapiuMenu
                            velocitapiusta = GlobalImgVar.velocitapiuMenu
                            efficienzapiusta = GlobalImgVar.efficienzapiuMenu
                            if dati[133] == 0 or usandoRod:
                                faretraFrecceStart = GlobalImgVar.faretraFrecceStart0
                            elif dati[133] == 1:
                                faretraFrecceStart = GlobalImgVar.faretraFrecceStart1
                            elif dati[133] == 2:
                                faretraFrecceStart = GlobalImgVar.faretraFrecceStart2
                            elif dati[133] == 3:
                                faretraFrecceStart = GlobalImgVar.faretraFrecceStart3
                            else:
                                faretraFrecceStart = 0
                    # menu principale
                    if voceMarcata == 8:
                        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 11.5))
                        GlobalHWVar.disegnaImmagineSuSchermo(puntatoreVecchio, (xp, yp))
                        conferma = 1
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == "padGiu" or bottoneDown == "padSu":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if primoMovimento or primoFrame or (tastoMovimentoPremuto and tastotempfps == 0) or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if dati[0] < GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"] and voceMarcata == 2:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = yp + GlobalHWVar.gsy // 18 * 7
                    voceMarcata += 4
                elif dati[0] < GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"] and voceMarcata == 2:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = yp + GlobalHWVar.gsy // 18 * 2
                    voceMarcata += 2
                elif voceMarcata != 5 and voceMarcata != 8:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = yp + GlobalHWVar.gsy // 18 * 1
                    voceMarcata += 1
                else:
                    if voceMarcata == 5:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = yp + GlobalHWVar.gsy // 18 * 4
                        voceMarcata += 1
                    elif voceMarcata == 8:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = GlobalHWVar.gsy // 18 * 5
                        voceMarcata = 1
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if dati[0] < GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"] and voceMarcata == 6:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = yp - GlobalHWVar.gsy // 18 * 7
                    voceMarcata -= 4
                elif dati[0] < GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"] and voceMarcata == 4:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = yp - GlobalHWVar.gsy // 18 * 2
                    voceMarcata -= 2
                elif voceMarcata != 6 and voceMarcata != 1:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = yp - GlobalHWVar.gsy // 18 * 1
                    voceMarcata -= 1
                else:
                    if voceMarcata == 6:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = yp - GlobalHWVar.gsy // 18 * 4
                        voceMarcata -= 1
                    elif voceMarcata == 1:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = GlobalHWVar.gsy // 18 * 15
                        voceMarcata = 8
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2
            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati)

            # chiedere conferma per uscire
            if conferma != 0:
                inizio, risposta = chiediconferma(conferma)
                if inizio:
                    break
                else:
                    conferma = 0

            if not risposta:
                if primoFrame:
                    primoFrame = False
                    aggiornaInterfacciaPerCambioInput = True
                    GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
                    # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 12.5))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15.5))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                    FunzioniGraficheGeneriche.messaggio(LI.MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                    if not usandoCalcolatore:
                        FunzioniGraficheGeneriche.messaggio(LI.OGGETTI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, 50)
                    else:
                        FunzioniGraficheGeneriche.messaggio(LI.OGGETTI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, 50)
                    if not usandoRod and not usandoCalcolatore:
                        FunzioniGraficheGeneriche.messaggio(LI.EQUIPAGGIAMENTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, 50)
                    else:
                        FunzioniGraficheGeneriche.messaggio(LI.EQUIPAGGIAMENTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, 50)
                    if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
                        if colcoInCasellaVista:
                            FunzioniGraficheGeneriche.messaggio(LI.SETTA_IMPO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, 50)
                        else:
                            FunzioniGraficheGeneriche.messaggio(LI.SETTA_IMPO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, 50)
                    if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
                        if not usandoRod and not usandoCalcolatore:
                            FunzioniGraficheGeneriche.messaggio(LI.MAPPA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, 50)
                            FunzioniGraficheGeneriche.messaggio(LI.DIARIO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, 50)
                        else:
                            FunzioniGraficheGeneriche.messaggio(LI.MAPPA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, 50)
                            FunzioniGraficheGeneriche.messaggio(LI.DIARIO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, 50)
                    FunzioniGraficheGeneriche.messaggio(LI.SALVA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, 50)
                    FunzioniGraficheGeneriche.messaggio(LI.IMPOSTAZIONI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, 50)
                    FunzioniGraficheGeneriche.messaggio(LI.MENU_PRINCIPALE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, 50)
                    if carim:
                        if dati[10] <= 0:
                            robosta = GlobalImgVar.robograf2b
                        else:
                            robosta = GlobalImgVar.robograf1
                        carim = False

                    # vita-status personaggio
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[4] < 100:
                        FunzioniGraficheGeneriche.messaggio(LI.LV___STR______ESP___STR____[GlobalHWVar.linguaImpostata] %(dati[4], dati[127], esptot), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16.4, GlobalHWVar.gsy // 18 * 12.9, 50, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio(LI.LV___STR______ESP___[GlobalHWVar.linguaImpostata] %dati[4], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16.4, GlobalHWVar.gsy // 18 * 12.9, 50, centrale=True)
                    FunzioniGraficheGeneriche.messaggio(LI.PV____STR____[GlobalHWVar.linguaImpostata] %(dati[5], pvtot), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16.4, GlobalHWVar.gsy // 18 * 13.7, 50, centrale=True)
                    FunzioniGraficheGeneriche.messaggio(LI.STATUS_ALTERATI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16.4, GlobalHWVar.gsy // 18 * 14.5, 50, centrale=True)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 12), int(GlobalHWVar.gpy * 16.5)), (int(GlobalHWVar.gpx * 21), int(GlobalHWVar.gpy * 16.5)), 2)
                    if dati[121]:
                        GlobalHWVar.disegnaImmagineSuSchermo(avvelenatosta, (GlobalHWVar.gsx // 32 * 14.4, GlobalHWVar.gsy // 18 * 15.2))
                    if dati[123] > 0:
                        GlobalHWVar.disegnaImmagineSuSchermo(attaccopiusta, ((GlobalHWVar.gsx // 32 * 14.4) + (2 * GlobalHWVar.gpx // 4 * 3), GlobalHWVar.gsy // 18 * 15.2))
                    if dati[124] > 0:
                        GlobalHWVar.disegnaImmagineSuSchermo(difesapiusta, ((GlobalHWVar.gsx // 32 * 14.4) + (4 * GlobalHWVar.gpx // 4 * 3), GlobalHWVar.gsy // 18 * 15.2))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgPersonaggioStart"], (GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 2.5))
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 12), int(GlobalHWVar.gpy * 12.5)), (int(GlobalHWVar.gpx * 21), int(GlobalHWVar.gpy * 12.5)), 2)

                    if GlobalGameVar.impoPresente or mostraImpoFineGioco:
                        if mostraImpoFineGioco:
                            dati[122] = 0
                            dati[125] = 0
                            dati[126] = 0
                        # vita-status robo
                        if dati[10] < 0:
                            dati[10] = 0
                        FunzioniGraficheGeneriche.messaggio(LI.PE____STR____[GlobalHWVar.linguaImpostata] %(dati[10], entot), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 13.3, 50, centrale=True)
                        FunzioniGraficheGeneriche.messaggio(LI.STATUS_ALTERATI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 14.1, 50, centrale=True)
                        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 21), int(GlobalHWVar.gpy * 16.5)), (int(GlobalHWVar.gpx * 30), int(GlobalHWVar.gpy * 16.5)), 2)
                        if dati[122] > 0:
                            GlobalHWVar.disegnaImmagineSuSchermo(surriscaldatosta, (GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14.8))
                        if dati[125] > 0:
                            GlobalHWVar.disegnaImmagineSuSchermo(velocitapiusta, ((GlobalHWVar.gsx // 32 * 24) + (2 * GlobalHWVar.gpx // 4 * 3), GlobalHWVar.gsy // 18 * 14.8))
                        if dati[126] > 0:
                            GlobalHWVar.disegnaImmagineSuSchermo(efficienzapiusta, ((GlobalHWVar.gsx // 32 * 24) + (4 * GlobalHWVar.gpx // 4 * 3), GlobalHWVar.gsy // 18 * 14.8))
                        GlobalHWVar.disegnaImmagineSuSchermo(robosta, (GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2.5))
                        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 21), int(GlobalHWVar.gpy * 12.5)), (int(GlobalHWVar.gpx * 30), int(GlobalHWVar.gpy * 12.5)), 2)

                    if faretraFrecceStart != 0:
                        GlobalHWVar.disegnaImmagineSuSchermo(faretraFrecceStart, (GlobalHWVar.gsx // 32 * 21.5, GlobalHWVar.gsy // 18 * 2.7))
                        numFrecce = dati[132]
                        if usandoRod:
                            numFrecce = 0
                            maxFrecce = 0
                        FunzioniGraficheGeneriche.messaggio(LI.FRE___STR____[GlobalHWVar.linguaImpostata] %(numFrecce, maxFrecce), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.45, GlobalHWVar.gsy // 18 * 6.2, 50, centrale=True)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 26), int(GlobalHWVar.gpy * 3)), (int(GlobalHWVar.gpx * 26), int(GlobalHWVar.gpy * 6.7)), 2)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sacchettoDenaroStart, (GlobalHWVar.gsx // 32 * 26.5, GlobalHWVar.gsy // 18 * 2.7))
                    numMonete = dati[131]
                    if usandoRod:
                        numMonete = dati[145] + GlobalGameVar.monetePerEntrareNellaConfraternita + GlobalGameVar.monetePerLaMappaDelLabirinto + GlobalGameVar.monetePerGliStumentiPerNeil
                    FunzioniGraficheGeneriche.messaggio(LI.MONETE_[GlobalHWVar.linguaImpostata] + str(numMonete), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 28.45, GlobalHWVar.gsy // 18 * 6.2, 50, centrale=True)
                else:
                    if aperturaSettaColcoNonRiuscita:
                        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 0.6))
                        FunzioniGraficheGeneriche.messaggio(LI.IMP__IRR[GlobalHWVar.linguaImpostata], GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 7.1, 40, daDestra=True)
                        aperturaSettaColcoNonRiuscita = False
                    elif voceMarcataVecchia != voceMarcata:
                        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 0.6))
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 11.5))
                if aggiornaInterfacciaPerCambioInput:
                    aggiornaInterfacciaPerCambioInput = False
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 19, 0, GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2))
                    if GlobalHWVar.mouseVisibile:
                        FunzioniGraficheGeneriche.messaggio(LI.TAS_DES__CEN_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                    elif GlobalHWVar.usandoIlController:
                        FunzioniGraficheGeneriche.messaggio(LI.MEN__B_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio(LI.ESC__Q_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)

                GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
                GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    if not inizio and not caricaSalvataggio:
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone, GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeCanzoni, GlobalHWVar.volumeEffetti], True, posizioneCanaleMusica=0)
    return dati, inizio, attacco, caricaSalvataggio, cambiatoRisoluzione


def startBattaglia(dati, animaOggetto, x, y, npers, rx, ry, inizio, tutteporte, tutticofanetti, listaNemiciTotali, vettoreEsche, vettoreDenaro, listaPersonaggiTotali, ultimoObbiettivoColco, obbiettivoCasualeColco):
    xp = GlobalHWVar.gpx * 0.9
    yp = GlobalHWVar.gpy * 13.3
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    sconosciutoOggetto = GlobalImgVar.sconosciutoOggettoMenu1
    sconosciutoOggettoIco = GlobalImgVar.sconosciutoOggettoIcoMenu

    schermo_temp = GlobalHWVar.schermo.copy()
    background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalHWVar.gsx, GlobalHWVar.gsy)).convert()
    dark = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
    dark.fill((0, 0, 0, 80))
    background.blit(dark, (0, 0))
    GlobalHWVar.disegnaImmagineSuSchermo(background, (0, 0))
    usandoRod = False
    if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= dati[0] < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
        usandoRod = True
    qtaOggettiDiRod = 99

    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati)

    attacco = 0
    risposta = False
    voceMarcata = 1
    voceMarcataOggetto = voceMarcata
    cambiatoRisoluzione = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8
    sposta = False

    oggetton = 1
    vettoreOggettiGraf = []
    vettoreOggettiIco = []
    while oggetton <= 10:
        if dati[oggetton + 30] >= 0:
            vettoreOggettiGraf.append(GlobalImgVar.vetImgOggettiStart[oggetton - 1])
            vettoreOggettiIco.append(GlobalImgVar.vetIcoOggettiMenu[oggetton - 1])
        else:
            vettoreOggettiGraf.append(sconosciutoOggetto)
            vettoreOggettiIco.append(sconosciutoOggettoIco)
        oggetton += 1

    GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone, GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeCanzoni / 2.0, GlobalHWVar.volumeEffetti / 3.0], True, posizioneCanaleMusica=0)
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
            if GlobalHWVar.gsy // 18 * 15.6 <= yMouse <= GlobalHWVar.gsy // 18 * 17 and 0 <= xMouse < GlobalHWVar.gsx // 32 * 4.2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                xp = 0
                yp = GlobalHWVar.gsy // 18 * 16.05
                voceMarcata = -1
            elif GlobalHWVar.gsy // 18 * 15.6 <= yMouse <= GlobalHWVar.gsy // 18 * 17 and GlobalHWVar.gsx // 32 * 4.2 <= xMouse <= GlobalHWVar.gsx // 32 * 6.8:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                xp = GlobalHWVar.gsx // 32 * 4.2
                yp = GlobalHWVar.gsy // 18 * 16.05
                voceMarcata = -2
            elif GlobalHWVar.gsy // 18 * 17 <= yMouse <= GlobalHWVar.gsy and GlobalHWVar.gsx // 32 * 0 <= xMouse <= GlobalHWVar.gsx // 32 * 8:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalHWVar.gsy // 18 * 13.3 <= yMouse <= GlobalHWVar.gsy // 18 * 14.3:
                if GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalHWVar.gsx // 32 * 0.9
                    yp = GlobalHWVar.gsy // 18 * 13.3
                elif GlobalHWVar.gsx // 32 * 2 <= xMouse <= GlobalHWVar.gsx // 32 * 3:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalHWVar.gsx // 32 * 1.9
                    yp = GlobalHWVar.gsy // 18 * 13.3
                elif GlobalHWVar.gsx // 32 * 3 <= xMouse <= GlobalHWVar.gsx // 32 * 4:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalHWVar.gsx // 32 * 2.9
                    yp = GlobalHWVar.gsy // 18 * 13.3
                elif GlobalHWVar.gsx // 32 * 4 <= xMouse <= GlobalHWVar.gsx // 32 * 5:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalHWVar.gsx // 32 * 3.9
                    yp = GlobalHWVar.gsy // 18 * 13.3
                elif GlobalHWVar.gsx // 32 * 5 <= xMouse <= GlobalHWVar.gsx // 32 * 6:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalHWVar.gsx // 32 * 4.9
                    yp = GlobalHWVar.gsy // 18 * 13.3
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            elif GlobalHWVar.gsy // 18 * 14.3 <= yMouse <= GlobalHWVar.gsy // 18 * 15.3:
                if GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalHWVar.gsx // 32 * 0.9
                    yp = GlobalHWVar.gsy // 18 * 14.3
                elif GlobalHWVar.gsx // 32 * 2 <= xMouse <= GlobalHWVar.gsx // 32 * 3:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalHWVar.gsx // 32 * 1.9
                    yp = GlobalHWVar.gsy // 18 * 14.3
                elif GlobalHWVar.gsx // 32 * 3 <= xMouse <= GlobalHWVar.gsx // 32 * 4:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalHWVar.gsx // 32 * 2.9
                    yp = GlobalHWVar.gsy // 18 * 14.3
                elif GlobalHWVar.gsx // 32 * 4 <= xMouse <= GlobalHWVar.gsx // 32 * 5:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalHWVar.gsx // 32 * 3.9
                    yp = GlobalHWVar.gsy // 18 * 14.3
                elif GlobalHWVar.gsx // 32 * 5 <= xMouse <= GlobalHWVar.gsx // 32 * 6:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalHWVar.gsx // 32 * 4.9
                    yp = GlobalHWVar.gsy // 18 * 14.3
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            else:
                if not GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)

        # gestione degli input
        menuConferma = False
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["Q"] or bottoneDown == pygame.K_ESCAPE or bottoneDown == "mouseDestro" or bottoneDown == "mouseCentrale" or bottoneDown == "padCerchio" or bottoneDown == "padStart":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                risposta = True
            elif voceMarcata < 0:
                if voceMarcata == -1:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xp, yp))
                    schermo_temp = GlobalHWVar.schermo.copy()
                    background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalHWVar.gsx, GlobalHWVar.gsy)).convert()

                    gpxPreCambioRisoluzione = GlobalHWVar.gpx
                    gpyPreCambioRisoluzione = GlobalHWVar.gpy
                    cambiatoRisoluzione = SottoMenuImpostazioni.menuImpostazioni(False, True, dati[0], cambiatoRisoluzione)
                    if cambiatoRisoluzione:
                        dati, tutteporte, tutticofanetti, listaNemiciTotali, vettoreEsche, vettoreDenaro, listaPersonaggiTotali, ultimoObbiettivoColco, obbiettivoCasualeColco = GenericFunc.sistemaImgPerCambioRisoluzione(dati, tutteporte, tutticofanetti, listaNemiciTotali, vettoreEsche, vettoreDenaro, listaPersonaggiTotali, ultimoObbiettivoColco, obbiettivoCasualeColco, gpxPreCambioRisoluzione, gpyPreCambioRisoluzione)
                        GlobalGameVar.vetDatiSalvataggioGameOver[0], GlobalGameVar.vetDatiSalvataggioGameOver[1], GlobalGameVar.vetDatiSalvataggioGameOver[2], GlobalGameVar.vetDatiSalvataggioGameOver[3], GlobalGameVar.vetDatiSalvataggioGameOver[4], GlobalGameVar.vetDatiSalvataggioGameOver[5], GlobalGameVar.vetDatiSalvataggioGameOver[7], GlobalGameVar.vetDatiSalvataggioGameOver[10], GlobalGameVar.vetDatiSalvataggioGameOver[11] = GenericFunc.sistemaImgPerCambioRisoluzione(GlobalGameVar.vetDatiSalvataggioGameOver[0], GlobalGameVar.vetDatiSalvataggioGameOver[1], GlobalGameVar.vetDatiSalvataggioGameOver[2], GlobalGameVar.vetDatiSalvataggioGameOver[3], GlobalGameVar.vetDatiSalvataggioGameOver[4], GlobalGameVar.vetDatiSalvataggioGameOver[5], GlobalGameVar.vetDatiSalvataggioGameOver[7], GlobalGameVar.vetDatiSalvataggioGameOver[10], GlobalGameVar.vetDatiSalvataggioGameOver[11], gpxPreCambioRisoluzione, gpyPreCambioRisoluzione)
                        xp = 0
                        yp = GlobalHWVar.gsy // 18 * 16.05
                        puntatore = GlobalImgVar.puntatore
                        puntatorevecchio = GlobalImgVar.puntatorevecchio
                        sconosciutoOggetto = GlobalImgVar.sconosciutoOggettoMenu1
                        sconosciutoOggettoIco = GlobalImgVar.sconosciutoOggettoIcoMenu
                        oggetton = 1
                        vettoreOggettiGraf = []
                        vettoreOggettiIco = []
                        while oggetton <= 10:
                            if dati[oggetton + 30] >= 0:
                                vettoreOggettiGraf.append(GlobalImgVar.vetImgOggettiStart[oggetton - 1])
                                vettoreOggettiIco.append(GlobalImgVar.vetIcoOggettiMenu[oggetton - 1])
                            else:
                                vettoreOggettiGraf.append(sconosciutoOggetto)
                                vettoreOggettiIco.append(sconosciutoOggettoIco)
                            oggetton += 1
                        background = pygame.transform.smoothscale(background, (GlobalHWVar.gsx, GlobalHWVar.gsy))

                    GlobalHWVar.disegnaImmagineSuSchermo(background, (0, 0))
                elif voceMarcata == -2:
                    menuConferma = True
            else:
                # pozione
                if voceMarcata == 1 and (dati[31] > 0 or usandoRod):
                    animaOggetto[0] = "pozione"
                    dati[5] = dati[5] + GlobalGameVar.curaOggetti[0]
                    if dati[5] > pvtot:
                        dati[5] = pvtot
                    if not usandoRod:
                        dati[31] -= 1
                    sposta = True
                    risposta = True
                # carica batt
                if voceMarcata == 2 and (dati[32] > 0 or usandoRod) and GlobalGameVar.impoPresente and (abs(x - rx) + abs(y - ry)) <= GlobalHWVar.gpx:
                    animaOggetto[0] = "caricaBatterie"
                    dati[10] = dati[10] + GlobalGameVar.curaOggetti[1]
                    if dati[10] > entot:
                        dati[10] = entot
                    if not usandoRod:
                        dati[32] -= 1
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
                if voceMarcata == 3 and (dati[33] > 0 or usandoRod):
                    animaOggetto[0] = "medicina"
                    dati[121] = 0
                    if not usandoRod:
                        dati[33] -= 1
                    sposta = True
                    risposta = True
                # super pozione
                if voceMarcata == 4 and (dati[34] > 0 or usandoRod):
                    animaOggetto[0] = "superPozione"
                    dati[5] = dati[5] + GlobalGameVar.curaOggetti[3]
                    if dati[5] > pvtot:
                        dati[5] = pvtot
                    if not usandoRod:
                        dati[34] -= 1
                    sposta = True
                    risposta = True
                # carica migliorato
                if voceMarcata == 5 and (dati[35] > 0 or usandoRod) and GlobalGameVar.impoPresente and (abs(x - rx) + abs(y - ry)) <= GlobalHWVar.gpx:
                    animaOggetto[0] = "caricaBatterieMigliorato"
                    dati[10] = dati[10] + GlobalGameVar.curaOggetti[4]
                    if dati[10] > entot:
                        dati[10] = entot
                    if not usandoRod:
                        dati[35] -= 1
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
                # bomba
                if voceMarcata == 6 and (dati[36] > 0 or usandoRod):
                    attacco = 2
                    risposta = True
                # bomba veleno
                if voceMarcata == 7 and (dati[37] > 0 or usandoRod):
                    attacco = 3
                    risposta = True
                # esca
                if voceMarcata == 8 and (dati[38] > 0 or usandoRod):
                    attacco = 4
                    risposta = True
                # bomba appiccicosa
                if voceMarcata == 9 and (dati[39] > 0 or usandoRod):
                    attacco = 5
                    risposta = True
                # bomba potenziata
                if voceMarcata == 10 and (dati[40] > 0 or usandoRod):
                    attacco = 6
                    risposta = True
                if risposta:
                    if 6 <= voceMarcata <= 10:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["A"] or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["D"] or bottoneDown == "padGiu" or bottoneDown == "padSu" or bottoneDown == "padSinistra" or bottoneDown == "padDestra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if not inizio and (primoMovimento or primoFrame or (tastoMovimentoPremuto and tastotempfps == 0) or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput):
            aggiornaInterfacciaPerCambioInput = False
            primoFrame = False
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata < 0:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if voceMarcata == -1:
                        xp = GlobalHWVar.gpx * 0.9
                        yp = GlobalHWVar.gpy * 14.3
                        voceMarcata = 6
                    elif voceMarcata == -2:
                        xp = GlobalHWVar.gpx * 3.9
                        yp = GlobalHWVar.gpy * 14.3
                        voceMarcata = 9
                elif 6 <= voceMarcata <= 10:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gpy * 13.3
                    voceMarcata -= 5
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["A"] or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata < 0:
                    if voceMarcata == -2:
                        voceMarcata += 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = 0
                    else:
                        voceMarcata -= 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 4.2
                elif voceMarcata == 1 or voceMarcata == 6:
                    voceMarcata += 4
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = GlobalHWVar.gpx * 4.9
                else:
                    voceMarcata -= 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = xp - GlobalHWVar.gpx
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if 1 <= voceMarcata <= 5:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gpy * 14.3
                    voceMarcata += 5
                elif voceMarcata >= 6:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if voceMarcata <= 8:
                        xp = 0
                        yp = GlobalHWVar.gsy // 18 * 16.05
                        voceMarcata = -1
                    else:
                        xp = GlobalHWVar.gsx // 32 * 4.2
                        yp = GlobalHWVar.gsy // 18 * 16.05
                        voceMarcata = -2
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["D"] or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata < 0:
                    if voceMarcata == -1:
                        voceMarcata -= 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 4.2
                    else:
                        voceMarcata += 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = 0
                elif voceMarcata == 5 or voceMarcata == 10:
                    voceMarcata -= 4
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = GlobalHWVar.gpx * 0.9
                else:
                    voceMarcata += 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = xp + GlobalHWVar.gpx
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if voceMarcata >= 0:
                voceMarcataOggetto = voceMarcata

            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoStartBattaglia, (0, GlobalHWVar.gsy // 18 * 8))
            FunzioniGraficheGeneriche.messaggio(LI.IMPOSTAZIONI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, int(GlobalHWVar.gpx * 2.2), int(GlobalHWVar.gpy * 16.05), 45, centrale=True)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 4.2) - 1, int(GlobalHWVar.gpy * 15.8)), (int(GlobalHWVar.gpx * 4.2) - 1, int(GlobalHWVar.gpy * 16.8)), 2)
            FunzioniGraficheGeneriche.messaggio(LI.ESCI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, int(GlobalHWVar.gpx * 4.9), int(GlobalHWVar.gpy * 16.05), 45)

            disegnoOggetto = voceMarcataOggetto - 1
            GlobalHWVar.disegnaImmagineSuSchermo(vettoreOggettiGraf[disegnoOggetto], (GlobalHWVar.gpx // 2, GlobalHWVar.gpy * 9.2))
            if usandoRod:
                qta = qtaOggettiDiRod
            elif dati[disegnoOggetto + 31] >= 0:
                qta = dati[disegnoOggetto + 31]
            else:
                qta = 0
            if voceMarcata < 0:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            else:
                if not usandoRod and (dati[disegnoOggetto + 31] <= 0 or ((disegnoOggetto == 1 or disegnoOggetto == 4) and abs(x - rx) + abs(y - ry) > GlobalHWVar.gpx)):
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatOut, (xp, yp))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatIn, (xp, yp))
            FunzioniGraficheGeneriche.messaggio(u"??%i" % qta, GlobalHWVar.grigiochi, (GlobalHWVar.gpx * 4) + (GlobalHWVar.gpx // 2), GlobalHWVar.gpy * 10.7, 80)
            i = 0
            while i < 5:
                GlobalHWVar.disegnaImmagineSuSchermo(vettoreOggettiIco[i], (GlobalHWVar.gpx * (i + 0.9), GlobalHWVar.gpy * 13.3))
                i += 1
            i = 0
            while i < 5:
                GlobalHWVar.disegnaImmagineSuSchermo(vettoreOggettiIco[i + 5], (GlobalHWVar.gpx * (i + 0.9), GlobalHWVar.gpy * 14.3))
                i += 1
            posizioneXNomiOggetti = GlobalHWVar.gpx * 3.4
            posizioneYNomiOggetti = GlobalHWVar.gpy * 8.4
            if voceMarcata == 1 or voceMarcataOggetto == 1:
                if dati[31] >= 0:
                    FunzioniGraficheGeneriche.messaggio(LI.POZIONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
            if voceMarcata == 2 or voceMarcataOggetto == 2:
                if dati[32] >= 0:
                    FunzioniGraficheGeneriche.messaggio(LI.IMPOFRUTTO_PICCOLO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
            if voceMarcata == 3 or voceMarcataOggetto == 3:
                if dati[33] >= 0:
                    FunzioniGraficheGeneriche.messaggio(LI.MEDICINA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
            if voceMarcata == 4 or voceMarcataOggetto == 4:
                if dati[34] >= 0:
                    FunzioniGraficheGeneriche.messaggio(LI.SUPER_POZIONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
            if voceMarcata == 5 or voceMarcataOggetto == 5:
                if dati[35] >= 0:
                    FunzioniGraficheGeneriche.messaggio(LI.IMPOFRUTTO_GRANDE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
            if voceMarcata == 6 or voceMarcataOggetto == 6:
                if dati[36] >= 0:
                    FunzioniGraficheGeneriche.messaggio(LI.BOMBA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
            if voceMarcata == 7 or voceMarcataOggetto == 7:
                if dati[37] >= 0:
                    FunzioniGraficheGeneriche.messaggio(LI.BOMBA_VELENOSA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
            if voceMarcata == 8 or voceMarcataOggetto == 8:
                if dati[38] >= 0:
                    FunzioniGraficheGeneriche.messaggio(LI.ESCA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
            if voceMarcata == 9 or voceMarcataOggetto == 9:
                if dati[39] >= 0:
                    FunzioniGraficheGeneriche.messaggio(LI.BOMBA_APPICCICOSA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
            if voceMarcata == 10 or voceMarcataOggetto == 10:
                if dati[40] >= 0:
                    FunzioniGraficheGeneriche.messaggio(LI.BOMBA_POTENZIATA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, posizioneXNomiOggetti, posizioneYNomiOggetti, 55, centrale=True)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 0.3), int(GlobalHWVar.gpy * 9.2)), (int(GlobalHWVar.gpx * 6.5), int(GlobalHWVar.gpy * 9.2)), 1)

            # vita-status rallo
            FunzioniGraficheGeneriche.disegnaVitaRallo(dati[5], pvtot, dati[132], dati[121], dati[123], dati[124], dati[0])

            if menuConferma:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xp, yp))
                schermo_temp = GlobalHWVar.schermo.copy()
                background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalHWVar.gsx, GlobalHWVar.gsy)).convert()
                inizio, risposta = chiediconferma(1)
                if not inizio:
                    GlobalHWVar.disegnaImmagineSuSchermo(background, (0, 0))
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))

            if not risposta:
                GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    if not inizio:
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone, GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeCanzoni, GlobalHWVar.volumeEffetti], True, posizioneCanaleMusica=0)
    return dati, attacco, sposta, animaOggetto, npers, inizio, cambiatoRisoluzione
