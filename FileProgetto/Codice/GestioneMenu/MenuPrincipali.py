# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.FunzioniGeneriche.CaricaSalvaPartita as CaricaSalvaPartita
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche
import SottoMenuEquip
import SottoMenuImpo
import SottoMenuRobo
import SottoMenuSalva
import SottoMenuMapDiario


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
                    FunzioniGraficheGeneriche.messaggio(u"Tornare al menu principale?", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6.5, 120, centrale=True)
                elif conferma == 2:
                    FunzioniGraficheGeneriche.messaggio("Uscire dal gioco?", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6.5, 120, centrale=True)
                elif conferma == 3:
                    FunzioniGraficheGeneriche.messaggio("Iniziare una nuova partita?", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6.5, 120, centrale=True)
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(backgroundUpdate1, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaImmagineSuSchermo(backgroundUpdate2, (GlobalHWVar.gsx // 32 * 21, 0))
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)
            FunzioniGraficheGeneriche.messaggio(u"Sì", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9.5, 120)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 16), int(GlobalHWVar.gpy * 9.3)), (int(GlobalHWVar.gpx * 16), int(GlobalHWVar.gpy * 11.6)), 2)
            FunzioniGraficheGeneriche.messaggio("No", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 9.5, 120)
            primoFrame = False
            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def menu(caricaSalvataggio, gameover):
    # per aggiungere porte e cofanetti => aggiungi "numStanza, x, y, False"
    xInizialie = 0
    yInizialie = 0
    rxInizialie = 0
    ryInizialie = 0
    # progresso - stanza - x - y - liv - pv - spada - scudo - armatura - armrob - energiarob - tecniche(20) - oggetti(10) - equipaggiamento(30) - batterie(10) - condizioni(20) - gambit(20) -
    # veleno - surriscalda - attp - difp - velp(x2) - efficienza - esperienza - arco - guanti - collana - monete - frecce - faretra -
    # rx - ry - raffredda - autoRic1 - autoRic2 - mosseRimasteRob - npers - nrob - chiaverob
    # porte(143-?) - cofanetti(?-?) // dimensione: 0-142 (=> 143 variabili) + porte e cofanetti
    datiIniziali = [0, 1, xInizialie, yInizialie, 1, 55, 0, 0, 0, 0, 0,  # <- statistiche
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # <- tecniche
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  # <- oggetti
        2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0,  # <- equpaggiamento
        2, 0, 0, 0, 0, -1, -1, -1, -1, -1,  # <- batterie (sono utilizzati solo i primi 5)
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # <- condizioni
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  # <- gambit
        False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # <- altre statistiche
        rxInizialie, ryInizialie, -1, -1, -1, 0, 4, 3, False  # <- info aggiunte per poter salvare ovunque
        ]

    # posizione porte e cofanetti nel vettore dati
    tuttePorte = GlobalGameVar.initVetPorteGlobale[:]
    tuttiCofanetti = GlobalGameVar.initVetCofanettiGlobale[:]

    lunghezzadati = len(datiIniziali)
    lunghezzadatiPorte = len(tuttePorte)
    lunghezzadatiCofanetti = len(tuttiCofanetti)

    if gameover:
        dati = GlobalGameVar.vetDatiSalvataggioGameOver[0]
        tuttePorte = GlobalGameVar.vetDatiSalvataggioGameOver[1]
        tuttiCofanetti = GlobalGameVar.vetDatiSalvataggioGameOver[2]
        listaNemiciTotali = GlobalGameVar.vetDatiSalvataggioGameOver[3]
        listaEsche = GlobalGameVar.vetDatiSalvataggioGameOver[4]
        listaMonete = GlobalGameVar.vetDatiSalvataggioGameOver[5]
        stanzeGiaVisitate = GlobalGameVar.vetDatiSalvataggioGameOver[6]
        listaPersonaggiTotali = GlobalGameVar.vetDatiSalvataggioGameOver[7]
        listaAvanzamentoDialoghi = GlobalGameVar.vetDatiSalvataggioGameOver[8]
        oggettiRimastiAHans = GlobalGameVar.vetDatiSalvataggioGameOver[9]
        ultimoObbiettivoColco = GlobalGameVar.vetDatiSalvataggioGameOver[10]
        obbiettivoCasualeColco = GlobalGameVar.vetDatiSalvataggioGameOver[11]
        return dati, tuttePorte, tuttiCofanetti, listaNemiciTotali, listaEsche, listaMonete, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco

    if caricaSalvataggio:
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

        GlobalGameVar.vetDatiSalvataggioGameOver = [datiGameover, tutteporteGameover, tutticofanettiGameover, listaNemiciTotaliGameover, listaEscheGameover, listaMoneteGameover, stanzeGiaVisitateGameover, listaPersonaggiTotaliGameover, listaAvanzamentoDialoghiGameover, oggettiRimastiAHansGameover, ultimoObbiettivoColcoGameover, obbiettivoCasualeColcoGameover]
        GlobalGameVar.numSalvataggioCaricato = caricaSalvataggio
        return dati, tuttePorte, tuttiCofanetti, listaNemiciTotali, listaEsche, listaMonete, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco

    # carico subito tutti i salvataggi
    SottoMenuSalva.ricaricaSalvataggi(lunghezzadati, lunghezzadatiPorte, lunghezzadatiCofanetti)

    GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.schemataDiCaricamento, (0, 0))
    sreen_temp = GlobalHWVar.schermo.copy().convert()
    imgOscuraPuntatore = sreen_temp.subsurface(pygame.Rect(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 11.5)).convert()

    canzone = GlobalGameVar.canzoneMenuPrincipale
    if not GlobalHWVar.canaleSoundCanzone.get_busy():
        GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
    if not GlobalHWVar.primoAvvio:
        FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=2)
    else:
        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
        GlobalHWVar.primoAvvio = False
    illuminaSchermoDopoVideo = True

    xp = GlobalHWVar.gsx // 32 * 1.5
    yp = GlobalHWVar.gsy // 18 * 2.5
    voceMarcata = 1
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    mostraTutorial = False

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
                if GlobalHWVar.gsx // 32 * 20.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
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
        if (bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio") and mostraTutorial:
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
                            i = GlobalHWVar.volumeCanzoni
                            j = GlobalHWVar.volumeEffetti
                            while i > 0 or j > 0:
                                GlobalHWVar.canaleSoundCanzone.set_volume(i)
                                GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(j)
                                i -= GlobalHWVar.volumeCanzoni / 10
                                j -= GlobalHWVar.volumeEffetti / 10
                                pygame.time.wait(30)
                                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                            GlobalHWVar.canaleSoundCanzone.stop()
                            GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
                            GlobalHWVar.canaleSoundSottofondoAmbientale.stop()
                            GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti)
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

                            GlobalGameVar.vetDatiSalvataggioGameOver = [datiGameover, tutteporteGameover, tutticofanettiGameover, listaNemiciTotaliGameover, listaEscheGameover, listaMoneteGameover, stanzeGiaVisitateGameover, listaPersonaggiTotaliGameover, listaAvanzamentoDialoghiGameover, oggettiRimastiAHansGameover, ultimoObbiettivoColcoGameover, obbiettivoCasualeColcoGameover]
                            if dati:
                                GlobalGameVar.numSalvataggioCaricato = n
                                return dati, tuttePorte, tuttiCofanetti, datiNemici, datiEsche, datiMonete, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco
                        primoFrame = True

                    # Impostazioni
                    if voceMarcata == 3:
                        SottoMenuImpo.menuImpostazioni(True, False)
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
        if not mostraTutorial and (bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == "padGiu" or bottoneDown == "padSu"):
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if primoMovimento or primoFrame or (tastoMovimentoPremuto and tastotempfps == 0) or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            if not mostraTutorial:
                if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
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
                if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
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
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.schemataDiCaricamento, (0, 0))
                    FunzioniGraficheGeneriche.messaggio("Inizia", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2.5, GlobalHWVar.gsy // 18 * 2, 90)
                    FunzioniGraficheGeneriche.messaggio("Continua", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2.5, GlobalHWVar.gsy // 18 * 4.5, 90)
                    FunzioniGraficheGeneriche.messaggio("Impostazioni", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2.5, GlobalHWVar.gsy // 18 * 7, 90)
                    FunzioniGraficheGeneriche.messaggio("Esci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2.5, GlobalHWVar.gsy // 18 * 12, 90)
                    sreen_temp = GlobalHWVar.schermo.copy().convert()
                    imgOscuraPuntatore = sreen_temp.subsurface(pygame.Rect(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 11.5)).convert()
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(imgOscuraPuntatore, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 2))
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 1.5) - 1, int(GlobalHWVar.gpy * 1.5)), (int(GlobalHWVar.gpx * 1.5) - 1, int(GlobalHWVar.gpy * 14)), 2)
                if aggiornaInterfacciaPerCambioInput:
                    aggiornaInterfacciaPerCambioInput = False
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (0, GlobalHWVar.gsy // 18 * 16.5, GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2))
                    if GlobalHWVar.mouseVisibile:
                        FunzioniGraficheGeneriche.messaggio("Tasto centrale: comandi", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 0.8, GlobalHWVar.gsy // 18 * 16.8, 50)
                    elif GlobalHWVar.usandoIlController:
                        FunzioniGraficheGeneriche.messaggio("Start: comandi", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 16.8, 50)
                    else:
                        FunzioniGraficheGeneriche.messaggio("Esc: comandi", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1.7, GlobalHWVar.gsy // 18 * 16.8, 50)

                if menuConferma:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xp, yp))
                    schermo_temp = GlobalHWVar.schermo.copy().convert()
                    background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalHWVar.gsx, GlobalHWVar.gsy)).convert()
                    if menuConferma == "inizia":
                        inutile, conferma = chiediconferma(3)
                        if conferma:
                            FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False)
                            i = GlobalHWVar.volumeCanzoni
                            j = GlobalHWVar.volumeEffetti
                            while i > 0 or j > 0:
                                GlobalHWVar.canaleSoundCanzone.set_volume(i)
                                GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(j)
                                i -= GlobalHWVar.volumeCanzoni / 10
                                j -= GlobalHWVar.volumeEffetti / 10
                                pygame.time.wait(30)
                                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                            GlobalHWVar.canaleSoundCanzone.stop()
                            GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
                            GlobalHWVar.canaleSoundSottofondoAmbientale.stop()
                            GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti)
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
                    FunzioniGraficheGeneriche.messaggio("Comandi mouse", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)

                    FunzioniGraficheGeneriche.messaggio("Mod. movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (GlobalHWVar.gsx // 32 * 0.4, GlobalHWVar.gsy // 18 * 6))
                    FunzioniGraficheGeneriche.messaggio("Movimento (su casella libera) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 6.8, 35)
                    FunzioniGraficheGeneriche.messaggio("Interagisci (su casella interagibile) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 7.3, 35)
                    FunzioniGraficheGeneriche.messaggio("Attiva o disattiva Impo (su PietraImpo) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 7.8, 35)
                    FunzioniGraficheGeneriche.messaggio("Menu (su stato personaggio) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 8.3, 35)
                    FunzioniGraficheGeneriche.messaggio(u"Modalità interazione (su stato nemico)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 8.8, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 9.8), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 9.8), 2)
                    FunzioniGraficheGeneriche.messaggio(u"Modalità interazione /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 11.1, 35)
                    FunzioniGraficheGeneriche.messaggio("Rimuovi selezione (su stato nemico)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 11.6, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 13.2), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 13.2), 2)
                    FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 14.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 4), (GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 17), 2)

                    FunzioniGraficheGeneriche.messaggio("Mod. interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 6))
                    FunzioniGraficheGeneriche.messaggio("Inquadra o attacca (su casella nemica) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 6.8, 35)
                    FunzioniGraficheGeneriche.messaggio("Interagisci (su casella interagibile) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 7.3, 35)
                    FunzioniGraficheGeneriche.messaggio("Attiva o disattiva Impo (su PietraImpo) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 7.8, 35)
                    FunzioniGraficheGeneriche.messaggio("Menu (su stato personaggio) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 8.3, 35)
                    FunzioniGraficheGeneriche.messaggio(u"Modalità movimento (su stato nemico)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 8.8, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 9.8), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 9.8), 2)
                    FunzioniGraficheGeneriche.messaggio(u"Modalità movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 11.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 13.2), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 13.2), 2)
                    FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 14.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 4), (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 17), 2)

                    FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 26.5, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (GlobalHWVar.gsx // 32 * 21.4, GlobalHWVar.gsy // 18 * 6))
                    FunzioniGraficheGeneriche.messaggio("Seleziona", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 7.8, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 9.8), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 9.8), 2)
                    FunzioniGraficheGeneriche.messaggio("Indietro / Esci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 11.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 13.2), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 13.2), 2)
                    FunzioniGraficheGeneriche.messaggio("Cambia operazione (se consentito)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 14.7, 35)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("Comandi controller", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)

                    FunzioniGraficheGeneriche.messaggio("Mod. movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInGioco, (GlobalHWVar.gsx // 32 * 0.4, GlobalHWVar.gsy // 18 * 6))
                    FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 6.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 7.6), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 7.6), 2)
                    FunzioniGraficheGeneriche.messaggio("Cambia bersaglio inquadrato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 8.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 9.2), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 9.2), 2)
                    FunzioniGraficheGeneriche.messaggio("Deseleziona bersaglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 9.85, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 10.75), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 10.75), 2)
                    FunzioniGraficheGeneriche.messaggio(u"Modalità interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 11.4, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 12.3), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 12.3), 2)
                    FunzioniGraficheGeneriche.messaggio("Movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 12.95, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 13.85), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 13.85), 2)
                    FunzioniGraficheGeneriche.messaggio("Attiva o disattiva Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 14.5, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 15.4), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 15.4), 2)
                    FunzioniGraficheGeneriche.messaggio("Interagisci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 16.1, 35)

                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 4), (GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 17), 2)
                    FunzioniGraficheGeneriche.messaggio("Mod. interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInGioco, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 6))
                    FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 6.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 7.6), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 7.6), 2)
                    FunzioniGraficheGeneriche.messaggio("Punta sul prossimo bersaglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 8.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 9.2), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 9.2), 2)
                    FunzioniGraficheGeneriche.messaggio(u"Modalità movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 9.85, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 10.75), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 10.75), 2)
                    FunzioniGraficheGeneriche.messaggio("Inquadra bersaglio puntato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 11.4, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 12.3), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 12.3), 2)
                    FunzioniGraficheGeneriche.messaggio("Sposta puntatore", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 12.95, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 13.85), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 13.85), 2)
                    FunzioniGraficheGeneriche.messaggio("Attiva o disattiva Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 14.5, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 15.4), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 15.4), 2)
                    FunzioniGraficheGeneriche.messaggio("Attacca / Interagisci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 16.1, 35)

                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 4), (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 17), 2)
                    FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 26.5, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInMenu, (GlobalHWVar.gsx // 32 * 21.4, GlobalHWVar.gsy // 18 * 6))
                    FunzioniGraficheGeneriche.messaggio("Esci (dove specificato)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 8.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 9.2), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 9.2), 2)
                    FunzioniGraficheGeneriche.messaggio("Indietro / Esci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 9.85, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 10.75), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 10.75), 2)
                    FunzioniGraficheGeneriche.messaggio("Sposta puntatore", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 11.4, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 12.3), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 12.3), 2)
                    FunzioniGraficheGeneriche.messaggio("Cambia operazione (se consentito)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 12.95, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 13.85), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 13.85), 2)
                    FunzioniGraficheGeneriche.messaggio("Seleziona", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 14.5, 35)
                else:
                    FunzioniGraficheGeneriche.messaggio("Comandi tastiera", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)

                    FunzioniGraficheGeneriche.messaggio("Mod. movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInGioco, (GlobalHWVar.gsx // 32 * 0.4, GlobalHWVar.gsy // 18 * 6))
                    FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 6.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 7.3), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 7.3), 2)
                    FunzioniGraficheGeneriche.messaggio("Cambia bersaglio inquadrato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 7.9, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 8.7), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 8.7), 2)
                    FunzioniGraficheGeneriche.messaggio("Deseleziona bersaglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 9.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 10.1), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 10.1), 2)
                    FunzioniGraficheGeneriche.messaggio(u"Modalità interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 10.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 11.5), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 11.5), 2)
                    FunzioniGraficheGeneriche.messaggio("Movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 12.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 14), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 14), 2)
                    FunzioniGraficheGeneriche.messaggio("Attiva o disattiva Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 14.6, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 15.4), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 15.4), 2)
                    FunzioniGraficheGeneriche.messaggio("Interagisci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 16, 35)

                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 4), (GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 17), 2)
                    FunzioniGraficheGeneriche.messaggio("Mod. interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInGioco, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 6))
                    FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 6.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 7.3), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 7.3), 2)
                    FunzioniGraficheGeneriche.messaggio("Punta sul prossimo bersaglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 7.9, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 8.7), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 8.7), 2)
                    FunzioniGraficheGeneriche.messaggio(u"Modalità movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 9.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 10.1), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 10.1), 2)
                    FunzioniGraficheGeneriche.messaggio("Inquadra bersaglio puntato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 10.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 11.5), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 11.5), 2)
                    FunzioniGraficheGeneriche.messaggio("Sposta puntatore", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 12.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 14), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 14), 2)
                    FunzioniGraficheGeneriche.messaggio("Attiva o disattiva Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 14.6, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 15.4), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 15.4), 2)
                    FunzioniGraficheGeneriche.messaggio("Attacca / Interagisci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 16, 35)

                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 4), (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 17), 2)
                    FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 26.5, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInMenu, (GlobalHWVar.gsx // 32 * 21.4, GlobalHWVar.gsy // 18 * 6))
                    FunzioniGraficheGeneriche.messaggio("Esci (dove specificato)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 8.1, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 8.7), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 8.7), 2)
                    FunzioniGraficheGeneriche.messaggio("Indietro / Esci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 9.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 10.1), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 10.1), 2)
                    FunzioniGraficheGeneriche.messaggio("Sposta puntatore", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 11.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 12.6), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 12.6), 2)
                    FunzioniGraficheGeneriche.messaggio("Cambia operazione (se consentito)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 13.2, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 14), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 14), 2)
                    FunzioniGraficheGeneriche.messaggio("Seleziona", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 14.6, 35)
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio("Tasto destro / centrale: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("Start / Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.3, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("Esc / Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.3, GlobalHWVar.gsy // 18 * 1, 50)
            if not illuminaSchermoDopoVideo:
                GlobalHWVar.aggiornaSchermo()

        if illuminaSchermoDopoVideo:
            illuminaSchermoDopoVideo = False

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
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.schemataDiCaricamento, (0, 0))
                GlobalHWVar.aggiornaSchermo()
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                i += 1
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.schemataDiCaricamento, (0, 0))
            GlobalHWVar.aggiornaSchermo()
        else:
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def start(dati, tutteporte, tutticofanetti, listaNemiciTotali, vettoreEsche, vettoreDenaro, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco, colcoInCasellaVista):
    if dati[0] < GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
        perssta = GlobalImgVar.lucy1GrafMenu
    elif GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= dati[0] < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
        perssta = GlobalImgVar.fraMaggioreGrafMenu
    elif dati[0] < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
        perssta = GlobalImgVar.lucy1GrafMenu
    else:
        perssta = GlobalImgVar.lucy2GrafMenu
    robosta = GlobalImgVar.robograf1b
    puntatore = GlobalImgVar.puntatore
    puntatoreVecchio = GlobalImgVar.puntatorevecchio
    avvelenatosta = GlobalImgVar.avvelenatoMenu
    surriscaldatosta = GlobalImgVar.surriscaldatoMenu
    attaccopiusta = GlobalImgVar.attaccopiuMenu
    difesapiusta = GlobalImgVar.difesapiuMenu
    velocitapiusta = GlobalImgVar.velocitapiuMenu
    efficienzapiusta = GlobalImgVar.efficienzapiuMenu
    if dati[133] == 0:
        faretraFrecceStart = GlobalImgVar.faretraFrecceStart0
        maxFrecce = 1
    elif dati[133] == 1:
        faretraFrecceStart = GlobalImgVar.faretraFrecceStart1
        maxFrecce = 5
    elif dati[133] == 2:
        faretraFrecceStart = GlobalImgVar.faretraFrecceStart2
        maxFrecce = 20
    elif dati[133] == 3:
        faretraFrecceStart = GlobalImgVar.faretraFrecceStart3
        maxFrecce = 60
    else:
        faretraFrecceStart = 0
        maxFrecce = 0
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

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni / 2)
    GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti / 2)
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
            if GlobalHWVar.gsx // 32 * 19 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
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
        if bottoneDown == pygame.K_q or bottoneDown == pygame.K_ESCAPE or bottoneDown == "mouseDestro" or bottoneDown == "mouseCentrale" or bottoneDown == "padCerchio" or bottoneDown == "padStart":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if suTornaIndietro and bottoneDown == "mouseSinistro":
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                risposta = True
            else:
                # non far cliccare su "Setta Colco" se Colco non è in una casella vista
                if voceMarcata == 3 and not colcoInCasellaVista:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    aperturaSettaColcoNonRiuscita = True
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    primoFrame = True
                    # oggetti
                    if voceMarcata == 1:
                        dati, attacco = SottoMenuEquip.oggetti(dati, colcoInCasellaVista)
                        if attacco != 0:
                            risposta = True
                        carim = True
                    # equip pers
                    if voceMarcata == 2:
                        dati = SottoMenuEquip.equip(dati)
                        carim = True
                    # equip robot
                    if voceMarcata == 3:
                        dati = SottoMenuRobo.equiprobo(dati)
                        carim = True
                    # mappa
                    if voceMarcata == 4:
                        SottoMenuMapDiario.menuMappa(dati[0])
                    # diario
                    if voceMarcata == 5:
                        SottoMenuMapDiario.menuDiario(dati)
                    # salva
                    if voceMarcata == 6:
                        # azioneFatta contiene 3 se è stato fatto un salvataggio, altrimenti 1 se è stato caricato un salvataggio
                        n, azioneFatta = SottoMenuSalva.scegli_sal(True, len(dati), len(tutteporte), len(tutticofanetti), tutteporte, tutticofanetti, vettoreEsche, vettoreDenaro, dati, listaNemiciTotali, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco)
                        if n != -1 and azioneFatta == 1:
                            FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False)
                            caricaSalvataggio = n
                            risposta = True
                    # impostazioni
                    if voceMarcata == 7:
                        SottoMenuImpo.menuImpostazioni(False, True)
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
        if bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == "padGiu" or bottoneDown == "padSu":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if primoMovimento or primoFrame or (tastoMovimentoPremuto and tastotempfps == 0) or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
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
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
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
                    FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                    FunzioniGraficheGeneriche.messaggio("Oggetti", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, 50)
                    FunzioniGraficheGeneriche.messaggio("Equipaggiamento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, 50)
                    if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
                        if colcoInCasellaVista:
                            FunzioniGraficheGeneriche.messaggio("Setta Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, 50)
                        else:
                            FunzioniGraficheGeneriche.messaggio("Setta Impo", GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, 50)
                    if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
                        FunzioniGraficheGeneriche.messaggio("Mappa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, 50)
                        FunzioniGraficheGeneriche.messaggio("Diario", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, 50)
                    FunzioniGraficheGeneriche.messaggio("Salva", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, 50)
                    FunzioniGraficheGeneriche.messaggio("Impostazioni", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, 50)
                    FunzioniGraficheGeneriche.messaggio("Menu principale", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, 50)
                    if carim:
                        if dati[10] <= 0:
                            robosta = GlobalImgVar.robograf2b
                        else:
                            robosta = GlobalImgVar.robograf1b
                        carim = False

                    # vita-status personaggio
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[4] < 100:
                        FunzioniGraficheGeneriche.messaggio("Lv: " + str(dati[4]) + "    Esp: " + str(dati[127]) + " / " + str(esptot), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16.4, GlobalHWVar.gsy // 18 * 12.9, 50, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio("Lv: " + str(dati[4]) + "    Esp: -- / --", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16.4, GlobalHWVar.gsy // 18 * 12.9, 50, centrale=True)
                    FunzioniGraficheGeneriche.messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16.4, GlobalHWVar.gsy // 18 * 13.7, 50, centrale=True)
                    FunzioniGraficheGeneriche.messaggio("Status alterati:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16.4, GlobalHWVar.gsy // 18 * 14.5, 50, centrale=True)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 12), int(GlobalHWVar.gpy * 16.5)), (int(GlobalHWVar.gpx * 21), int(GlobalHWVar.gpy * 16.5)), 2)
                    if dati[121]:
                        GlobalHWVar.disegnaImmagineSuSchermo(avvelenatosta, (GlobalHWVar.gsx // 32 * 14.4, GlobalHWVar.gsy // 18 * 15.2))
                    if dati[123] > 0:
                        GlobalHWVar.disegnaImmagineSuSchermo(attaccopiusta, ((GlobalHWVar.gsx // 32 * 14.4) + (2 * GlobalHWVar.gpx // 4 * 3), GlobalHWVar.gsy // 18 * 15.2))
                    if dati[124] > 0:
                        GlobalHWVar.disegnaImmagineSuSchermo(difesapiusta, ((GlobalHWVar.gsx // 32 * 14.4) + (4 * GlobalHWVar.gpx // 4 * 3), GlobalHWVar.gsy // 18 * 15.2))
                    GlobalHWVar.disegnaImmagineSuSchermo(perssta, (GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 2.5))
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 12), int(GlobalHWVar.gpy * 12.5)), (int(GlobalHWVar.gpx * 21), int(GlobalHWVar.gpy * 12.5)), 2)

                    if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
                        # vita-status robo
                        if dati[10] < 0:
                            dati[10] = 0
                        FunzioniGraficheGeneriche.messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 13.3, 50, centrale=True)
                        FunzioniGraficheGeneriche.messaggio("Status alterati:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 14.1, 50, centrale=True)
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
                        FunzioniGraficheGeneriche.messaggio("Frecce: " + str(dati[132]) + " / " + str(maxFrecce), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 6.2, 50, centrale=True)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 26), int(GlobalHWVar.gpy * 3)), (int(GlobalHWVar.gpx * 26), int(GlobalHWVar.gpy * 6.7)), 2)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sacchettoDenaroStart, (GlobalHWVar.gsx // 32 * 26.5, GlobalHWVar.gsy // 18 * 2.7))
                    FunzioniGraficheGeneriche.messaggio("Monete: " + str(dati[131]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 28.4, GlobalHWVar.gsy // 18 * 6.2, 50, centrale=True)
                else:
                    if aperturaSettaColcoNonRiuscita:
                        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 0.6))
                        FunzioniGraficheGeneriche.messaggio(u"Impo è irraggiungibile!", GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 7.1, 40)
                        aperturaSettaColcoNonRiuscita = False
                    elif voceMarcataVecchia != voceMarcata:
                        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 0.6))
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 11.5))
                if aggiornaInterfacciaPerCambioInput:
                    aggiornaInterfacciaPerCambioInput = False
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 19, 0, GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2))
                    if GlobalHWVar.mouseVisibile:
                        FunzioniGraficheGeneriche.messaggio("Tasto destro / centrale: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 1, 50)
                    elif GlobalHWVar.usandoIlController:
                        FunzioniGraficheGeneriche.messaggio("Start / Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.1, GlobalHWVar.gsy // 18 * 1, 50)
                    else:
                        FunzioniGraficheGeneriche.messaggio("Esc / Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 1, 50)

                GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
                GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    if not inizio and not caricaSalvataggio:
        GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
        GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti)
    return dati, inizio, attacco, caricaSalvataggio


def startBattaglia(dati, animaOggetto, x, y, npers, rx, ry, inizio):
    xp = GlobalHWVar.gpx * 1
    yp = GlobalHWVar.gpy * 13.8
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    sconosciutoOggetto = GlobalImgVar.sconosciutoOggettoMenu1
    sconosciutoOggettoIco = GlobalImgVar.sconosciutoOggettoIcoMenu

    schermo_temp = GlobalHWVar.schermo.copy().convert()
    background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalHWVar.gsx, GlobalHWVar.gsy)).convert()
    dark = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
    dark.fill((0, 0, 0, 80))
    background.blit(dark, (0, 0))
    GlobalHWVar.disegnaImmagineSuSchermo(background, (0, 0))

    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati)

    attacco = 0
    disegnoOggetto = 0
    risposta = False
    voceMarcata = 1
    voceMarcataOggetto = voceMarcata

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    difensivi = True
    offensivi = False
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

    GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni / 2)
    GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti / 2)
    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        mouseInquadraFreccia = False
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
            elif GlobalHWVar.gsy // 18 * 17 <= yMouse <= GlobalHWVar.gsy and GlobalHWVar.gsx // 32 * 0 <= xMouse <= GlobalHWVar.gsx // 32 * 7:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                suTornaIndietro = True
            elif difensivi:
                if GlobalHWVar.gsy // 18 * 14.8 <= yMouse <= GlobalHWVar.gsy // 18 * 15.3 and GlobalHWVar.gsx // 32 * 3 <= xMouse <= GlobalHWVar.gsx // 32 * 4:
                    mouseInquadraFreccia = True
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                elif GlobalHWVar.gsy // 18 * 13.8 <= yMouse <= GlobalHWVar.gsy // 18 * 14.8:
                    if GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 2:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 13.8
                    elif GlobalHWVar.gsx // 32 * 2 <= xMouse <= GlobalHWVar.gsx // 32 * 3:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalHWVar.gsx // 32 * 2
                        yp = GlobalHWVar.gsy // 18 * 13.8
                    elif GlobalHWVar.gsx // 32 * 3 <= xMouse <= GlobalHWVar.gsx // 32 * 4:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 3
                        xp = GlobalHWVar.gsx // 32 * 3
                        yp = GlobalHWVar.gsy // 18 * 13.8
                    elif GlobalHWVar.gsx // 32 * 4 <= xMouse <= GlobalHWVar.gsx // 32 * 5:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 4
                        xp = GlobalHWVar.gsx // 32 * 4
                        yp = GlobalHWVar.gsy // 18 * 13.8
                    elif GlobalHWVar.gsx // 32 * 5 <= xMouse <= GlobalHWVar.gsx // 32 * 6:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 5
                        xp = GlobalHWVar.gsx // 32 * 5
                        yp = GlobalHWVar.gsy // 18 * 13.8
                    else:
                        if not GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(True)
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            elif offensivi:
                if GlobalHWVar.gsy // 18 * 13.8 <= yMouse <= GlobalHWVar.gsy // 18 * 14.3 and GlobalHWVar.gsx // 32 * 3 <= xMouse <= GlobalHWVar.gsx // 32 * 4:
                    mouseInquadraFreccia = True
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                elif GlobalHWVar.gsy // 18 * 14.3 <= yMouse <= GlobalHWVar.gsy // 18 * 15.3:
                    if GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 2:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 14.3
                    elif GlobalHWVar.gsx // 32 * 2 <= xMouse <= GlobalHWVar.gsx // 32 * 3:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalHWVar.gsx // 32 * 2
                        yp = GlobalHWVar.gsy // 18 * 14.3
                    elif GlobalHWVar.gsx // 32 * 3 <= xMouse <= GlobalHWVar.gsx // 32 * 4:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 3
                        xp = GlobalHWVar.gsx // 32 * 3
                        yp = GlobalHWVar.gsy // 18 * 14.3
                    elif GlobalHWVar.gsx // 32 * 4 <= xMouse <= GlobalHWVar.gsx // 32 * 5:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 4
                        xp = GlobalHWVar.gsx // 32 * 4
                        yp = GlobalHWVar.gsy // 18 * 14.3
                    elif GlobalHWVar.gsx // 32 * 5 <= xMouse <= GlobalHWVar.gsx // 32 * 6:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 5
                        xp = GlobalHWVar.gsx // 32 * 5
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
        if bottoneDown == pygame.K_q or bottoneDown == pygame.K_ESCAPE or bottoneDown == "mouseDestro" or bottoneDown == "mouseCentrale" or bottoneDown == "padCerchio" or bottoneDown == "padStart":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                risposta = True
            elif bottoneDown == "mouseSinistro" and mouseInquadraFreccia:
                if difensivi:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gpy * 14.3
                    difensivi = False
                    offensivi = True
                elif offensivi:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gpy * 13.8
                    offensivi = False
                    difensivi = True
            elif voceMarcata < 0:
                if voceMarcata == -1:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xp, yp))
                    schermo_temp = GlobalHWVar.schermo.copy().convert()
                    background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalHWVar.gsx, GlobalHWVar.gsy)).convert()
                    SottoMenuImpo.menuImpostazioni(False, True)
                    GlobalHWVar.disegnaImmagineSuSchermo(background, (0, 0))
                elif voceMarcata == -2:
                    menuConferma = True
            else:
                if difensivi:
                    # pozione
                    if voceMarcata == 1 and dati[31] > 0:
                        animaOggetto[0] = "pozione"
                        dati[5] = dati[5] + 100
                        if dati[5] > pvtot:
                            dati[5] = pvtot
                        dati[31] = dati[31] - 1
                        sposta = True
                        risposta = True
                    # carica batt
                    if voceMarcata == 2 and dati[32] > 0 and dati[0] >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"] and (abs(x - rx) + abs(y - ry)) <= GlobalHWVar.gpx:
                        animaOggetto[0] = "caricaBatterie"
                        dati[10] = dati[10] + 250
                        if dati[10] > entot:
                            dati[10] = entot
                        dati[32] = dati[32] - 1
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
                    if voceMarcata == 3 and dati[33] > 0:
                        animaOggetto[0] = "medicina"
                        dati[121] = 0
                        dati[33] = dati[33] - 1
                        sposta = True
                        risposta = True
                    # super pozione
                    if voceMarcata == 4 and dati[34] > 0:
                        animaOggetto[0] = "superPozione"
                        dati[5] = dati[5] + 300
                        if dati[5] > pvtot:
                            dati[5] = pvtot
                        dati[34] = dati[34] - 1
                        sposta = True
                        risposta = True
                    # carica migliorato
                    if voceMarcata == 5 and dati[35] > 0 and dati[0] >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"] and (abs(x - rx) + abs(y - ry)) <= GlobalHWVar.gpx:
                        animaOggetto[0] = "caricaBatterieMigliorato"
                        dati[10] = dati[10] + 600
                        if dati[10] > entot:
                            dati[10] = entot
                        dati[35] = dati[35] - 1
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
                elif offensivi:
                    # bomba
                    if voceMarcata == 1 and dati[36] > 0:
                        attacco = 2
                        risposta = True
                    # bomba veleno
                    if voceMarcata == 2 and dati[37] > 0:
                        attacco = 3
                        risposta = True
                    # esca
                    if voceMarcata == 3 and dati[38] > 0:
                        attacco = 4
                        risposta = True
                    # bomba appiccicosa
                    if voceMarcata == 4 and dati[39] > 0:
                        attacco = 5
                        risposta = True
                    # bomba potenziata
                    if voceMarcata == 5 and dati[40] > 0:
                        attacco = 6
                        risposta = True
                if risposta:
                    if offensivi:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == pygame.K_a or bottoneDown == pygame.K_d or bottoneDown == "padGiu" or bottoneDown == "padSu" or bottoneDown == "padSinistra" or bottoneDown == "padDestra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if not inizio and (primoMovimento or primoFrame or (tastoMovimentoPremuto and tastotempfps == 0) or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput):
            aggiornaInterfacciaPerCambioInput = False
            primoFrame = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata < 0:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    offensivi = True
                    difensivi = False
                    if voceMarcata == -1:
                        xp = GlobalHWVar.gpx * 1
                        yp = GlobalHWVar.gpy * 14.3
                        voceMarcata = 1
                    elif voceMarcata == -2:
                        xp = GlobalHWVar.gpx * 4
                        yp = GlobalHWVar.gpy * 14.3
                        voceMarcata = 4
                elif offensivi:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gpy * 13.8
                    offensivi = False
                    difensivi = True
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata < 0:
                    if voceMarcata == -2:
                        voceMarcata += 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = 0
                    else:
                        voceMarcata -= 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 4.2
                elif voceMarcata != 1:
                    voceMarcata -= 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = xp - GlobalHWVar.gpx
                else:
                    voceMarcata += 4
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = GlobalHWVar.gpx * 5
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if difensivi:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gpy * 14.3
                    difensivi = False
                    offensivi = True
                elif voceMarcata >= 0:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if voceMarcata <= 3:
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
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata < 0:
                    if voceMarcata == -1:
                        voceMarcata -= 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 4.2
                    else:
                        voceMarcata += 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = 0
                elif voceMarcata != 5:
                    voceMarcata += 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = xp + GlobalHWVar.gpx
                else:
                    voceMarcata -= 4
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = GlobalHWVar.gpx * 1
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if voceMarcata >= 0:
                voceMarcataOggetto = voceMarcata

            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoStartBattaglia, (0, GlobalHWVar.gsy // 18 * 8))
            FunzioniGraficheGeneriche.messaggio("Impostazioni", GlobalHWVar.grigiochi, int(GlobalHWVar.gpx * 0.7), int(GlobalHWVar.gpy * 16.05), 45)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 4.2) - 1, int(GlobalHWVar.gpy * 15.8)), (int(GlobalHWVar.gpx * 4.2) - 1, int(GlobalHWVar.gpy * 16.8)), 2)
            FunzioniGraficheGeneriche.messaggio("Esci", GlobalHWVar.grigiochi, int(GlobalHWVar.gpx * 4.9), int(GlobalHWVar.gpy * 16.05), 45)
            if difensivi:
                if voceMarcata == 1:
                    disegnoOggetto = 0
                if voceMarcata == 2:
                    disegnoOggetto = 1
                if voceMarcata == 3:
                    disegnoOggetto = 2
                if voceMarcata == 4:
                    disegnoOggetto = 3
                if voceMarcata == 5:
                    disegnoOggetto = 4
            elif offensivi:
                if voceMarcata == 1:
                    disegnoOggetto = 5
                if voceMarcata == 2:
                    disegnoOggetto = 6
                if voceMarcata == 3:
                    disegnoOggetto = 7
                if voceMarcata == 4:
                    disegnoOggetto = 8
                if voceMarcata == 5:
                    disegnoOggetto = 9
            GlobalHWVar.disegnaImmagineSuSchermo(vettoreOggettiGraf[disegnoOggetto], (GlobalHWVar.gpx // 2, GlobalHWVar.gpy * 9.7))
            if dati[disegnoOggetto + 31] <= 0:
                if voceMarcata < 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatOut, (xp, yp))
                qta = 0
            elif (disegnoOggetto == 1 or disegnoOggetto == 4) and abs(x - rx) + abs(y - ry) > GlobalHWVar.gpx:
                if voceMarcata < 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatOut, (xp, yp))
                qta = dati[disegnoOggetto + 31]
            else:
                if voceMarcata < 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatIn, (xp, yp))
                qta = dati[disegnoOggetto + 31]
            FunzioniGraficheGeneriche.messaggio("x%i" % qta, GlobalHWVar.grigiochi, (GlobalHWVar.gpx * 4) + (GlobalHWVar.gpx // 2), GlobalHWVar.gpy * 11.2, 80)
            disegnati = 0
            i = 0
            while i < 10:
                if difensivi and (i == 0 or i == 1 or i == 2 or i == 3 or i == 4):
                    GlobalHWVar.disegnaImmagineSuSchermo(vettoreOggettiIco[i], (GlobalHWVar.gpx * (disegnati + 1), GlobalHWVar.gpy * 13.8))
                    disegnati += 1
                if offensivi and (i == 5 or i == 6 or i == 7 or i == 8 or i == 9):
                    GlobalHWVar.disegnaImmagineSuSchermo(vettoreOggettiIco[i], (GlobalHWVar.gpx * (disegnati + 1), (GlobalHWVar.gpy * 13.8) + (GlobalHWVar.gpy // 2)))
                    disegnati += 1
                i += 1
            if difensivi:
                if voceMarcata == 1 or voceMarcataOggetto == 1:
                    if dati[31] >= 0:
                        FunzioniGraficheGeneriche.messaggio("Pozione", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                if voceMarcata == 2 or voceMarcataOggetto == 2:
                    if dati[32] >= 0:
                        FunzioniGraficheGeneriche.messaggio("Alimentaz. 100gr", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                if voceMarcata == 3 or voceMarcataOggetto == 3:
                    if dati[33] >= 0:
                        FunzioniGraficheGeneriche.messaggio("Medicina", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                if voceMarcata == 4 or voceMarcataOggetto == 4:
                    if dati[34] >= 0:
                        FunzioniGraficheGeneriche.messaggio("Super pozione", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                if voceMarcata == 5 or voceMarcataOggetto == 5:
                    if dati[35] >= 0:
                        FunzioniGraficheGeneriche.messaggio("Alimentaz. 250gr", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriGiu, (GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 14.8))
            if offensivi:
                if voceMarcata == 1 or voceMarcataOggetto == 1:
                    if dati[36] >= 0:
                        FunzioniGraficheGeneriche.messaggio("Bomba", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                if voceMarcata == 2 or voceMarcataOggetto == 2:
                    if dati[37] >= 0:
                        FunzioniGraficheGeneriche.messaggio("Bomba velenosa", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                if voceMarcata == 3 or voceMarcataOggetto == 3:
                    if dati[38] >= 0:
                        FunzioniGraficheGeneriche.messaggio("Esca", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                if voceMarcata == 4 or voceMarcataOggetto == 4:
                    if dati[39] >= 0:
                        FunzioniGraficheGeneriche.messaggio("Bomba appiccicosa", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                if voceMarcata == 5 or voceMarcataOggetto == 5:
                    if dati[40] >= 0:
                        FunzioniGraficheGeneriche.messaggio("Bomba potenziata", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSu, (GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 13.3))

            # vita-status rallo
            lungvitatot = int(((GlobalHWVar.gpx * pvtot) / float(4)) // 5)
            lungvita = (lungvitatot * dati[5]) // pvtot
            if lungvita < 0:
                lungvita = 0
            indvitapers = pygame.transform.smoothscale(GlobalImgVar.indvita, (lungvitatot, GlobalHWVar.gpy // 4))
            fineindvitapers = GlobalImgVar.fineindvita
            vitaral = pygame.transform.smoothscale(GlobalImgVar.vitapersonaggio, (lungvita, GlobalHWVar.gpy // 4))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoRallo, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
            GlobalHWVar.disegnaImmagineSuSchermo(indvitapers, (GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy // 18 * 17) + (GlobalHWVar.gpy // 4 * 3)))
            GlobalHWVar.disegnaImmagineSuSchermo(fineindvitapers, ((GlobalHWVar.gsx // 32 * 1) + lungvitatot, (GlobalHWVar.gsy // 18 * 17) + (GlobalHWVar.gpy // 4 * 3)))
            GlobalHWVar.disegnaImmagineSuSchermo(vitaral, (GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy // 18 * 17) + (GlobalHWVar.gpy // 4 * 3)))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perss, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssb, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgNumFrecce, (int(GlobalHWVar.gsx // 32 * 1.2), GlobalHWVar.gsy // 18 * 17))
            FunzioniGraficheGeneriche.messaggio(" x" + str(dati[132]), GlobalHWVar.grigiochi, int(GlobalHWVar.gsx // 32 * 1.8), int(GlobalHWVar.gsy // 18 * 17.3), 40)
            if dati[121]:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.avvelenato, (GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 17))
            if dati[123] > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.attaccopiu, (GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 17))
            if dati[124] > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.difesapiu, (GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 17))

            if menuConferma:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xp, yp))
                schermo_temp = GlobalHWVar.schermo.copy().convert()
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
        GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
        GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti)
    return dati, attacco, sposta, animaOggetto, npers, inizio
