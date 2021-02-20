# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import GlobalImgVar
import GlobalSndVar
import GlobalGameVar
import GestioneInput
import GenericFunc
import CaricaSalvaPartita
import SottoMenuA
import SottoMenuB


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
    SottoMenuB.ricaricaSalvataggi(lunghezzadati, lunghezzadatiPorte, lunghezzadatiCofanetti)

    GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.schemataDiCaricamento, (0, 0))

    canzone = GlobalGameVar.canzoneMenuPrincipale
    if not GlobalHWVar.canaleSoundCanzone.get_busy():
        GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
    if not GlobalHWVar.primoAvvio:
        GenericFunc.oscuraIlluminaSchermo(illumina=2)
    else:
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
                        n, inutile = SottoMenuB.scegli_sal(False, lunghezzadati, lunghezzadatiPorte, lunghezzadatiCofanetti, [], [], [], [], [], [], [], [], [], [], [], False)

                        # lettura salvataggio
                        if n != -1:
                            GenericFunc.oscuraIlluminaSchermo(illumina=False)
                            i = GlobalHWVar.volumeCanzoni
                            j = GlobalHWVar.volumeEffetti
                            while i > 0 or j > 0:
                                GlobalHWVar.canaleSoundCanzone.set_volume(i)
                                GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(j)
                                i -= GlobalHWVar.volumeCanzoni / 10
                                j -= GlobalHWVar.volumeEffetti / 10
                                pygame.time.wait(30)
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
                        SottoMenuB.menuImpostazioni(True, False)
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
                    GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.schemataDiCaricamento, (0, 0))
                    GenericFunc.messaggio("Inizia", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2.5, GlobalHWVar.gsy // 18 * 2, 90)
                    GenericFunc.messaggio("Continua", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2.5, GlobalHWVar.gsy // 18 * 4.5, 90)
                    GenericFunc.messaggio("Impostazioni", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2.5, GlobalHWVar.gsy // 18 * 7, 90)
                    GenericFunc.messaggio("Esci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2.5, GlobalHWVar.gsy // 18 * 12, 90)
                else:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 2.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 10.5))
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 1.5) - 1, int(GlobalHWVar.gpy * 1.5)), (int(GlobalHWVar.gpx * 1.5) - 1, int(GlobalHWVar.gpy * 14)), 2)
                if aggiornaInterfacciaPerCambioInput:
                    aggiornaInterfacciaPerCambioInput = False
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (0, GlobalHWVar.gsy // 18 * 16.5, GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2))
                    if GlobalHWVar.mouseVisibile:
                        GenericFunc.messaggio("Tasto centrale: comandi", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 0.8, GlobalHWVar.gsy // 18 * 16.8, 50)
                    elif GlobalHWVar.usandoIlController:
                        GenericFunc.messaggio("Start: comandi", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 16.8, 50)
                    else:
                        GenericFunc.messaggio("Esc: comandi", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1.7, GlobalHWVar.gsy // 18 * 16.8, 50)

                if menuConferma:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xp, yp))
                    schermo_temp = GlobalHWVar.schermo.copy().convert()
                    background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalHWVar.gsx, GlobalHWVar.gsy)).convert()
                    if menuConferma == "inizia":
                        inutile, conferma = SottoMenuB.chiediconferma(3)
                        if conferma:
                            GenericFunc.oscuraIlluminaSchermo(illumina=False)
                            i = GlobalHWVar.volumeCanzoni
                            j = GlobalHWVar.volumeEffetti
                            while i > 0 or j > 0:
                                GlobalHWVar.canaleSoundCanzone.set_volume(i)
                                GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(j)
                                i -= GlobalHWVar.volumeCanzoni / 10
                                j -= GlobalHWVar.volumeEffetti / 10
                                pygame.time.wait(30)
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
                        inizio, inutile = SottoMenuB.chiediconferma(2)
                        if not inizio:
                            GlobalHWVar.disegnaImmagineSuSchermo(background, (0, 0))
                    aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            elif primoFrame or aggiornaInterfacciaPerCambioInput:
                primoFrame = False
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                if GlobalHWVar.mouseVisibile:
                    GenericFunc.messaggio("Comandi mouse", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)

                    GenericFunc.messaggio("Mod. movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (GlobalHWVar.gsx // 32 * 0.4, GlobalHWVar.gsy // 18 * 6))
                    GenericFunc.messaggio("Movimento (su casella libera) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 6.8, 35)
                    GenericFunc.messaggio("Interagisci (su casella interagibile) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 7.3, 35)
                    GenericFunc.messaggio("Attiva o disattiva Impo (su teleImpo) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 7.8, 35)
                    GenericFunc.messaggio("Menu (su stato personaggio) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 8.3, 35)
                    GenericFunc.messaggio(u"Modalità interazione (su stato nemico)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 8.8, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 9.8), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 9.8), 2)
                    GenericFunc.messaggio(u"Modalità interazione /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 11.1, 35)
                    GenericFunc.messaggio("Rimuovi selezione (su stato nemico)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 11.6, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 13.2), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 13.2), 2)
                    GenericFunc.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.2, GlobalHWVar.gsy // 18 * 14.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 4), (GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 17), 2)

                    GenericFunc.messaggio("Mod. interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 6))
                    GenericFunc.messaggio("Inquadra o attacca (su casella nemica) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 6.8, 35)
                    GenericFunc.messaggio("Interagisci (su casella interagibile) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 7.3, 35)
                    GenericFunc.messaggio("Attiva o disattiva Impo (su teleImpo) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 7.8, 35)
                    GenericFunc.messaggio("Menu (su stato personaggio) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 8.3, 35)
                    GenericFunc.messaggio(u"Modalità movimento (su stato nemico)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 8.8, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 9.8), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 9.8), 2)
                    GenericFunc.messaggio(u"Modalità movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 11.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 13.2), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 13.2), 2)
                    GenericFunc.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.7, GlobalHWVar.gsy // 18 * 14.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 4), (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 17), 2)

                    GenericFunc.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 26.5, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (GlobalHWVar.gsx // 32 * 21.4, GlobalHWVar.gsy // 18 * 6))
                    GenericFunc.messaggio("Seleziona", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 7.8, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 9.8), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 9.8), 2)
                    GenericFunc.messaggio("Indietro / Esci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 11.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 13.2), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 13.2), 2)
                    GenericFunc.messaggio("Cambia operazione (se consentito)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 14.7, 35)
                elif GlobalHWVar.usandoIlController:
                    GenericFunc.messaggio("Comandi controller", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)

                    GenericFunc.messaggio("Mod. movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInGioco, (GlobalHWVar.gsx // 32 * 0.4, GlobalHWVar.gsy // 18 * 6))
                    GenericFunc.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 6.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 7.6), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 7.6), 2)
                    GenericFunc.messaggio("Cambia bersaglio inquadrato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 8.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 9.2), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 9.2), 2)
                    GenericFunc.messaggio("Deseleziona bersaglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 9.85, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 10.75), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 10.75), 2)
                    GenericFunc.messaggio(u"Modalità interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 11.4, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 12.3), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 12.3), 2)
                    GenericFunc.messaggio("Movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 12.95, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 13.85), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 13.85), 2)
                    GenericFunc.messaggio("Attiva o disattiva Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 14.5, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 15.4), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 15.4), 2)
                    GenericFunc.messaggio("Interagisci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 16.1, 35)

                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 4), (GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 17), 2)
                    GenericFunc.messaggio("Mod. interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInGioco, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 6))
                    GenericFunc.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 6.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 7.6), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 7.6), 2)
                    GenericFunc.messaggio("Punta sul prossimo bersaglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 8.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 9.2), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 9.2), 2)
                    GenericFunc.messaggio(u"Modalità movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 9.85, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 10.75), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 10.75), 2)
                    GenericFunc.messaggio("Inquadra bersaglio puntato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 11.4, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 12.3), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 12.3), 2)
                    GenericFunc.messaggio("Sposta puntatore", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 12.95, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 13.85), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 13.85), 2)
                    GenericFunc.messaggio("Attiva o disattiva Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 14.5, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 15.4), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 15.4), 2)
                    GenericFunc.messaggio("Attacca / Interagisci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 16.1, 35)

                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 4), (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 17), 2)
                    GenericFunc.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 26.5, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInMenu, (GlobalHWVar.gsx // 32 * 21.4, GlobalHWVar.gsy // 18 * 6))
                    GenericFunc.messaggio("Esci (dove specificato)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 8.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 9.2), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 9.2), 2)
                    GenericFunc.messaggio("Indietro / Esci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 9.85, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 10.75), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 10.75), 2)
                    GenericFunc.messaggio("Sposta puntatore", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 11.4, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 12.3), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 12.3), 2)
                    GenericFunc.messaggio("Cambia operazione (se consentito)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 12.95, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 13.85), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 13.85), 2)
                    GenericFunc.messaggio("Seleziona", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 14.5, 35)
                else:
                    GenericFunc.messaggio("Comandi tastiera", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)

                    GenericFunc.messaggio("Mod. movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInGioco, (GlobalHWVar.gsx // 32 * 0.4, GlobalHWVar.gsy // 18 * 6))
                    GenericFunc.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 6.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 7.3), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 7.3), 2)
                    GenericFunc.messaggio("Cambia bersaglio inquadrato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 7.9, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 8.7), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 8.7), 2)
                    GenericFunc.messaggio("Deseleziona bersaglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 9.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 10.1), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 10.1), 2)
                    GenericFunc.messaggio(u"Modalità interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 10.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 11.5), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 11.5), 2)
                    GenericFunc.messaggio("Movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 12.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 14), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 14), 2)
                    GenericFunc.messaggio("Attiva o disattiva Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 14.6, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 0.7, GlobalHWVar.gsy // 18 * 15.4), (GlobalHWVar.gsx // 32 * 10.2, GlobalHWVar.gsy // 18 * 15.4), 2)
                    GenericFunc.messaggio("Interagisci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 16, 35)

                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 4), (GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 17), 2)
                    GenericFunc.messaggio("Mod. interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInGioco, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 6))
                    GenericFunc.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 6.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 7.3), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 7.3), 2)
                    GenericFunc.messaggio("Punta sul prossimo bersaglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 7.9, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 8.7), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 8.7), 2)
                    GenericFunc.messaggio(u"Modalità movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 9.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 10.1), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 10.1), 2)
                    GenericFunc.messaggio("Inquadra bersaglio puntato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 10.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 11.5), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 11.5), 2)
                    GenericFunc.messaggio("Sposta puntatore", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 12.7, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 14), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 14), 2)
                    GenericFunc.messaggio("Attiva o disattiva Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 14.6, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11.2, GlobalHWVar.gsy // 18 * 15.4), (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 15.4), 2)
                    GenericFunc.messaggio("Attacca / Interagisci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.9, GlobalHWVar.gsy // 18 * 16, 35)

                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 4), (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 17), 2)
                    GenericFunc.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 26.5, GlobalHWVar.gsy // 18 * 4.2, 80, centrale=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInMenu, (GlobalHWVar.gsx // 32 * 21.4, GlobalHWVar.gsy // 18 * 6))
                    GenericFunc.messaggio("Esci (dove specificato)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 8.1, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 8.7), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 8.7), 2)
                    GenericFunc.messaggio("Indietro / Esci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 9.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 10.1), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 10.1), 2)
                    GenericFunc.messaggio("Sposta puntatore", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 11.3, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 12.6), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 12.6), 2)
                    GenericFunc.messaggio("Cambia operazione (se consentito)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 13.2, 35)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 21.7, GlobalHWVar.gsy // 18 * 14), (GlobalHWVar.gsx // 32 * 31.2, GlobalHWVar.gsy // 18 * 14), 2)
                    GenericFunc.messaggio("Seleziona", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25.4, GlobalHWVar.gsy // 18 * 14.6, 35)
                if GlobalHWVar.mouseVisibile:
                    GenericFunc.messaggio("Tasto destro / centrale: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    GenericFunc.messaggio("Start / Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.3, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    GenericFunc.messaggio("Esc / Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.3, GlobalHWVar.gsy // 18 * 1, 50)
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
                pygame.event.pump()
                GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                i += 1
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.schemataDiCaricamento, (0, 0))
            GlobalHWVar.aggiornaSchermo()
        else:
            pygame.event.pump()
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
                elif dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] and GlobalHWVar.gsy // 18 * 6.8 <= yMouse <= GlobalHWVar.gsy // 18 * 7.8:
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
                        dati, attacco = SottoMenuA.oggetti(dati, colcoInCasellaVista)
                        if attacco != 0:
                            risposta = True
                        carim = True
                    # equip pers
                    if voceMarcata == 2:
                        dati = SottoMenuA.equip(dati)
                        carim = True
                    # equip robot
                    if voceMarcata == 3:
                        dati = SottoMenuA.equiprobo(dati)
                        carim = True
                    # mappa
                    if voceMarcata == 4:
                        SottoMenuB.menuMappa(dati[0])
                    # diario
                    if voceMarcata == 5:
                        SottoMenuB.menuDiario(dati)
                    # salva
                    if voceMarcata == 6:
                        # azioneFatta contiene 3 se è stato fatto un salvataggio, altrimenti 1 se è stato caricato un salvataggio
                        n, azioneFatta = SottoMenuB.scegli_sal(True, len(dati), len(tutteporte), len(tutticofanetti), tutteporte, tutticofanetti, vettoreEsche, vettoreDenaro, dati, listaNemiciTotali, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco)
                        if n != -1 and azioneFatta == 1:
                            GenericFunc.oscuraIlluminaSchermo(illumina=False)
                            caricaSalvataggio = n
                            risposta = True
                    # impostazioni
                    if voceMarcata == 7:
                        SottoMenuB.menuImpostazioni(False, True)
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
                elif dati[0] < GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] and voceMarcata == 2:
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
                elif dati[0] < GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] and voceMarcata == 4:
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
                inizio, risposta = SottoMenuB.chiediconferma(conferma)
                if inizio:
                    break
                else:
                    conferma = 0

            if not risposta:
                if primoFrame:
                    primoFrame = False
                    aggiornaInterfacciaPerCambioInput = True
                    GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                    # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 12.5))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15.5))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                    GenericFunc.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                    GenericFunc.messaggio("Oggetti", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, 50)
                    GenericFunc.messaggio("Equipaggiamento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, 50)
                    if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"]:
                        if colcoInCasellaVista:
                            GenericFunc.messaggio("Setta Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, 50)
                        else:
                            GenericFunc.messaggio("Setta Impo", GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, 50)
                    if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
                        GenericFunc.messaggio("Mappa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, 50)
                        GenericFunc.messaggio("Diario", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, 50)
                    GenericFunc.messaggio("Salva", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, 50)
                    GenericFunc.messaggio("Impostazioni", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, 50)
                    GenericFunc.messaggio("Menu principale", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, 50)
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
                        GenericFunc.messaggio("Lv: " + str(dati[4]) + "    Esp: " + str(dati[127]) + " / " + str(esptot), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16.4, GlobalHWVar.gsy // 18 * 12.9, 50, centrale=True)
                    else:
                        GenericFunc.messaggio("Lv: " + str(dati[4]) + "    Esp: -- / --", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16.4, GlobalHWVar.gsy // 18 * 12.9, 50, centrale=True)
                    GenericFunc.messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16.4, GlobalHWVar.gsy // 18 * 13.7, 50, centrale=True)
                    GenericFunc.messaggio("Status alterati:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16.4, GlobalHWVar.gsy // 18 * 14.5, 50, centrale=True)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 12), int(GlobalHWVar.gpy * 16.5) - 2), (int(GlobalHWVar.gpx * 21), int(GlobalHWVar.gpy * 16.5) - 2), 2)
                    if dati[121]:
                        GlobalHWVar.disegnaImmagineSuSchermo(avvelenatosta, (GlobalHWVar.gsx // 32 * 14.4, GlobalHWVar.gsy // 18 * 15.2))
                    if dati[123] > 0:
                        GlobalHWVar.disegnaImmagineSuSchermo(attaccopiusta, ((GlobalHWVar.gsx // 32 * 14.4) + (2 * GlobalHWVar.gpx // 4 * 3), GlobalHWVar.gsy // 18 * 15.2))
                    if dati[124] > 0:
                        GlobalHWVar.disegnaImmagineSuSchermo(difesapiusta, ((GlobalHWVar.gsx // 32 * 14.4) + (4 * GlobalHWVar.gpx // 4 * 3), GlobalHWVar.gsy // 18 * 15.2))
                    GlobalHWVar.disegnaImmagineSuSchermo(perssta, (GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 2.5))
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 12), int(GlobalHWVar.gpy * 12.5)), (int(GlobalHWVar.gpx * 21), int(GlobalHWVar.gpy * 12.5)), 2)

                    if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"]:
                        # vita-status robo
                        if dati[10] < 0:
                            dati[10] = 0
                        GenericFunc.messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 13.3, 50, centrale=True)
                        GenericFunc.messaggio("Status alterati:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 14.1, 50, centrale=True)
                        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 21), int(GlobalHWVar.gpy * 16.5) - 2), (int(GlobalHWVar.gpx * 30), int(GlobalHWVar.gpy * 16.5) - 2), 2)
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
                        GenericFunc.messaggio("Frecce: " + str(dati[132]) + " / " + str(maxFrecce), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 6.2, 50, centrale=True)
                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 26), int(GlobalHWVar.gpy * 3)), (int(GlobalHWVar.gpx * 26), int(GlobalHWVar.gpy * 6.7)), 2)
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sacchettoDenaroStart, (GlobalHWVar.gsx // 32 * 26.5, GlobalHWVar.gsy // 18 * 2.7))
                    GenericFunc.messaggio("Monete: " + str(dati[131]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 28.4, GlobalHWVar.gsy // 18 * 6.2, 50, centrale=True)
                else:
                    if aperturaSettaColcoNonRiuscita:
                        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 0.6))
                        GenericFunc.messaggio(u"Impo è irraggiungibile!", GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 7.1, 40)
                        aperturaSettaColcoNonRiuscita = False
                    elif voceMarcataVecchia != voceMarcata:
                        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 0.6))
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 11.5))
                if aggiornaInterfacciaPerCambioInput:
                    aggiornaInterfacciaPerCambioInput = False
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 19, 0, GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2))
                    if GlobalHWVar.mouseVisibile:
                        GenericFunc.messaggio("Tasto destro / centrale: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 1, 50)
                    elif GlobalHWVar.usandoIlController:
                        GenericFunc.messaggio("Start / Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.1, GlobalHWVar.gsy // 18 * 1, 50)
                    else:
                        GenericFunc.messaggio("Esc / Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 1, 50)

                GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
                GlobalHWVar.aggiornaSchermo()

        pygame.event.pump()
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
                    SottoMenuB.menuImpostazioni(False, True)
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
                    if voceMarcata == 2 and dati[32] > 0 and dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] and (abs(x - rx) + abs(y - ry)) <= GlobalHWVar.gpx:
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
                    if voceMarcata == 5 and dati[35] > 0 and dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] and (abs(x - rx) + abs(y - ry)) <= GlobalHWVar.gpx:
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
            GenericFunc.messaggio("Impostazioni", GlobalHWVar.grigiochi, int(GlobalHWVar.gpx * 0.7), int(GlobalHWVar.gpy * 16.05), 45)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 4.2) - 1, int(GlobalHWVar.gpy * 15.8)), (int(GlobalHWVar.gpx * 4.2) - 1, int(GlobalHWVar.gpy * 16.8)), 2)
            GenericFunc.messaggio("Esci", GlobalHWVar.grigiochi, int(GlobalHWVar.gpx * 4.9), int(GlobalHWVar.gpy * 16.05), 45)
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
            GenericFunc.messaggio("x%i" % qta, GlobalHWVar.grigiochi, (GlobalHWVar.gpx * 4) + (GlobalHWVar.gpx // 2), GlobalHWVar.gpy * 11.2, 80)
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
                        GenericFunc.messaggio("Pozione", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                if voceMarcata == 2 or voceMarcataOggetto == 2:
                    if dati[32] >= 0:
                        GenericFunc.messaggio("Alimentaz. 100gr", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                if voceMarcata == 3 or voceMarcataOggetto == 3:
                    if dati[33] >= 0:
                        GenericFunc.messaggio("Medicina", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                if voceMarcata == 4 or voceMarcataOggetto == 4:
                    if dati[34] >= 0:
                        GenericFunc.messaggio("Super pozione", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                if voceMarcata == 5 or voceMarcataOggetto == 5:
                    if dati[35] >= 0:
                        GenericFunc.messaggio("Alimentaz. 250gr", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriGiu, (GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 14.8))
            if offensivi:
                if voceMarcata == 1 or voceMarcataOggetto == 1:
                    if dati[36] >= 0:
                        GenericFunc.messaggio("Bomba", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                if voceMarcata == 2 or voceMarcataOggetto == 2:
                    if dati[37] >= 0:
                        GenericFunc.messaggio("Bomba velenosa", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                if voceMarcata == 3 or voceMarcataOggetto == 3:
                    if dati[38] >= 0:
                        GenericFunc.messaggio("Esca", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                if voceMarcata == 4 or voceMarcataOggetto == 4:
                    if dati[39] >= 0:
                        GenericFunc.messaggio("Bomba appiccicosa", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                if voceMarcata == 5 or voceMarcataOggetto == 5:
                    if dati[40] >= 0:
                        GenericFunc.messaggio("Bomba potenziata", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
                    else:
                        GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gpx // 3, int(GlobalHWVar.gpy * 8.9), 55)
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
            GenericFunc.messaggio(" x" + str(dati[132]), GlobalHWVar.grigiochi, int(GlobalHWVar.gsx // 32 * 1.8), int(GlobalHWVar.gsy // 18 * 17.3), 40)
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
                inizio, risposta = SottoMenuB.chiediconferma(1)
                if not inizio:
                    GlobalHWVar.disegnaImmagineSuSchermo(background, (0, 0))
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))

            if not risposta:
                GlobalHWVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    if not inizio:
        GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
        GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti)
    return dati, attacco, sposta, animaOggetto, npers, inizio


def menuMercante(dati):
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    sconosciutoOggetto = GlobalImgVar.sconosciutoOggettoMenu2
    xp = GlobalHWVar.gsx // 32 * 10.5
    yp = GlobalHWVar.gsy // 18 * 6.1
    xpv = xp
    ypv = yp
    usauno = False
    confermaOggettoDaAcquistare = 0
    risposta = False
    oggetton = 0
    voceMarcata = 0
    numeroOggettiAcquistati = 1
    moneteInsufficienti = False
    inventarioPieno = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    maxFrecce = 1
    if dati[133] == 1:
        maxFrecce = 5
    elif dati[133] == 2:
        maxFrecce = 20
    elif dati[133] == 3:
        maxFrecce = 60

    imgOggetti = []
    i = 1
    while i <= 10:
        if (i == 1 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercantePozione"]) or (i == 2 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteAlimantaz"]) or (i == 3 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteMedicina"]) or (i == 4 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteSuperPoz"]) or (i == 5 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteAlimMiglio"]) or (i == 6 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteBomba"]) or (i == 7 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteBomVele"]) or (i == 8 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteEsca"]) or (i == 9 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteBomAppi"]) or (i == 10 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteBomPote"]):
            imgOggetti.append(GlobalImgVar.vetImgOggettiMercante[i - 1])
        else:
            imgOggetti.append(sconosciutoOggetto)
        i += 1

    GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni / 2)
    GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti / 2)
    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        oggettonVecchio = oggetton
        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        mouseInquadraFrecciaSu = False
        mouseInquadraFrecciaGiu = False
        suTornaIndietro = False
        if GlobalHWVar.mouseVisibile:
            if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                suTornaIndietro = True
            elif voceMarcata == 0:
                if GlobalHWVar.gsx // 32 * 10.5 <= xMouse <= GlobalHWVar.gsx // 32 * 21.5:
                    if GlobalHWVar.gsy // 18 * 6 <= yMouse <= GlobalHWVar.gsy // 18 * 6.8:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 0
                        xp = GlobalHWVar.gsx // 32 * 10.5
                        yp = GlobalHWVar.gsy // 18 * 6.1
                    elif GlobalHWVar.gsy // 18 * 6.8 <= yMouse <= GlobalHWVar.gsy // 18 * 7.7:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 1
                        xp = GlobalHWVar.gsx // 32 * 10.5
                        yp = GlobalHWVar.gsy // 18 * 7
                    elif GlobalHWVar.gsy // 18 * 7.7 <= yMouse <= GlobalHWVar.gsy // 18 * 8.6:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 2
                        xp = GlobalHWVar.gsx // 32 * 10.5
                        yp = GlobalHWVar.gsy // 18 * 7.9
                    elif GlobalHWVar.gsy // 18 * 8.6 <= yMouse <= GlobalHWVar.gsy // 18 * 9.5:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 3
                        xp = GlobalHWVar.gsx // 32 * 10.5
                        yp = GlobalHWVar.gsy // 18 * 8.8
                    elif GlobalHWVar.gsy // 18 * 9.5 <= yMouse <= GlobalHWVar.gsy // 18 * 10.4:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 4
                        xp = GlobalHWVar.gsx // 32 * 10.5
                        yp = GlobalHWVar.gsy // 18 * 9.7
                    elif GlobalHWVar.gsy // 18 * 10.4 <= yMouse <= GlobalHWVar.gsy // 18 * 11.3:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 5
                        xp = GlobalHWVar.gsx // 32 * 10.5
                        yp = GlobalHWVar.gsy // 18 * 10.6
                    elif GlobalHWVar.gsy // 18 * 11.3 <= yMouse <= GlobalHWVar.gsy // 18 * 12.2:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 6
                        xp = GlobalHWVar.gsx // 32 * 10.5
                        yp = GlobalHWVar.gsy // 18 * 11.5
                    elif GlobalHWVar.gsy // 18 * 12.2 <= yMouse <= GlobalHWVar.gsy // 18 * 13.1:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 7
                        xp = GlobalHWVar.gsx // 32 * 10.5
                        yp = GlobalHWVar.gsy // 18 * 12.4
                    elif GlobalHWVar.gsy // 18 * 13.1 <= yMouse <= GlobalHWVar.gsy // 18 * 14:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 8
                        xp = GlobalHWVar.gsx // 32 * 10.5
                        yp = GlobalHWVar.gsy // 18 * 13.3
                    elif GlobalHWVar.gsy // 18 * 14 <= yMouse <= GlobalHWVar.gsy // 18 * 14.9:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 9
                        xp = GlobalHWVar.gsx // 32 * 10.5
                        yp = GlobalHWVar.gsy // 18 * 14.2
                    elif GlobalHWVar.gsy // 18 * 14.9 <= yMouse <= GlobalHWVar.gsy // 18 * 15.8:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 10
                        xp = GlobalHWVar.gsx // 32 * 10.5
                        yp = GlobalHWVar.gsy // 18 * 15.1
                    elif GlobalHWVar.gsy // 18 * 15.8 <= yMouse <= GlobalHWVar.gsy // 18 * 16.7:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 11
                        xp = GlobalHWVar.gsx // 32 * 10.5
                        yp = GlobalHWVar.gsy // 18 * 16
                    else:
                        if not GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(True)
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            else:
                if GlobalHWVar.gsy // 18 * 4.3 <= yMouse <= GlobalHWVar.gsy // 18 * 4.8 and GlobalHWVar.gsx // 32 * 8.5 <= xMouse <= GlobalHWVar.gsx // 32 * 9.5:
                    mouseInquadraFrecciaSu = True
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                elif GlobalHWVar.gsy // 18 * 4.8 <= yMouse <= GlobalHWVar.gsy // 18 * 5.3 and GlobalHWVar.gsx // 32 * 8.5 <= xMouse <= GlobalHWVar.gsx // 32 * 9.5:
                    mouseInquadraFrecciaGiu = True
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                elif GlobalHWVar.gsy // 18 * 6.5 <= yMouse <= GlobalHWVar.gsy // 18 * 7.9:
                    if GlobalHWVar.gsx // 32 * 0.5 <= xMouse <= GlobalHWVar.gsx // 32 * 5.3:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalHWVar.gsx // 32 * 1.3
                        yp = GlobalHWVar.gsy // 18 * 6.9
                    elif GlobalHWVar.gsx // 32 * 5.3 <= xMouse <= GlobalHWVar.gsx // 32 * 10:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalHWVar.gsx // 32 * 5.3
                        yp = GlobalHWVar.gsy // 18 * 6.9
                    else:
                        if not GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(True)
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            if (oggettonVecchio != oggetton or voceMarcataVecchia != voceMarcata) and not primoFrame:
                inventarioPieno = False
                moneteInsufficienti = False
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            moneteInsufficienti = False
            inventarioPieno = False
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            numeroOggettiAcquistati = 1
            voceMarcata = 0
            if confermaOggettoDaAcquistare != 0:
                xp = GlobalHWVar.gsx // 32 * 10.5
                if confermaOggettoDaAcquistare == -1:
                    yp = GlobalHWVar.gsy // 18 * 6.1
                if confermaOggettoDaAcquistare == 1:
                    yp = GlobalHWVar.gsy // 18 * 7
                if confermaOggettoDaAcquistare == 2:
                    yp = GlobalHWVar.gsy // 18 * 7.9
                if confermaOggettoDaAcquistare == 3:
                    yp = GlobalHWVar.gsy // 18 * 8.8
                if confermaOggettoDaAcquistare == 4:
                    yp = GlobalHWVar.gsy // 18 * 9.7
                if confermaOggettoDaAcquistare == 5:
                    yp = GlobalHWVar.gsy // 18 * 10.6
                if confermaOggettoDaAcquistare == 6:
                    yp = GlobalHWVar.gsy // 18 * 11.5
                if confermaOggettoDaAcquistare == 7:
                    yp = GlobalHWVar.gsy // 18 * 12.4
                if confermaOggettoDaAcquistare == 8:
                    yp = GlobalHWVar.gsy // 18 * 13.3
                if confermaOggettoDaAcquistare == 9:
                    yp = GlobalHWVar.gsy // 18 * 14.2
                if confermaOggettoDaAcquistare == 10:
                    yp = GlobalHWVar.gsy // 18 * 15.1
                if confermaOggettoDaAcquistare == 11:
                    yp = GlobalHWVar.gsy // 18 * 16
                confermaOggettoDaAcquistare = 0
            else:
                risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if not (bottoneDown == "mouseSinistro" and (mouseInquadraFrecciaSu or mouseInquadraFrecciaGiu)):
                procediAllAcquisto = True
                # confermaOggettoDaAcquistare?
                if voceMarcata == 1 and not (bottoneDown == "mouseSinistro" and suTornaIndietro):
                    if 0 <= oggetton <= 10 and GlobalGameVar.costoOggetti[oggetton] * numeroOggettiAcquistati <= dati[131]:
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAcquisto)
                        primoFrame = True
                        dati[131] -= GlobalGameVar.costoOggetti[oggetton] * numeroOggettiAcquistati
                        voceMarcata = 0
                        xp = GlobalHWVar.gsx // 32 * 10.5
                        # freccia
                        if confermaOggettoDaAcquistare == -1:
                            dati[132] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 6.1
                        # pozione
                        if confermaOggettoDaAcquistare == 1:
                            dati[31] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 7
                        # carica batt
                        if confermaOggettoDaAcquistare == 2:
                            dati[32] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 7.9
                        # antidoto
                        if confermaOggettoDaAcquistare == 3:
                            dati[33] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 8.8
                        # super pozione
                        if confermaOggettoDaAcquistare == 4:
                            dati[34] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 9.7
                        # carica migliorato
                        if confermaOggettoDaAcquistare == 5:
                            dati[35] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 10.6
                        # bomba
                        if confermaOggettoDaAcquistare == 6:
                            dati[36] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 11.5
                        # bomba veleno
                        if confermaOggettoDaAcquistare == 7:
                            dati[37] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 12.4
                        # esca
                        if confermaOggettoDaAcquistare == 8:
                            dati[38] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 13.3
                        # bomba appiccicosa
                        if confermaOggettoDaAcquistare == 9:
                            dati[39] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 14.2
                        # bomba potenziata
                        if confermaOggettoDaAcquistare == 10:
                            dati[40] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 15.1
                        confermaOggettoDaAcquistare = 0
                        procediAllAcquisto = False
                    elif oggetton == 11:
                        if dati[133] == 0 and GlobalGameVar.costoOggetti[oggetton] * numeroOggettiAcquistati <= dati[131]:
                            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAcquisto)
                            primoFrame = True
                            dati[131] -= GlobalGameVar.costoOggetti[oggetton] * numeroOggettiAcquistati
                            voceMarcata = 0
                            xp = GlobalHWVar.gsx // 32 * 10.5
                            # faretra
                            if confermaOggettoDaAcquistare == 11:
                                dati[133] += numeroOggettiAcquistati
                                yp = GlobalHWVar.gsy // 18 * 16
                            confermaOggettoDaAcquistare = 0
                            procediAllAcquisto = False
                        elif dati[133] == 1 and GlobalGameVar.costoOggetti[oggetton + 1] * numeroOggettiAcquistati <= dati[131]:
                            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAcquisto)
                            primoFrame = True
                            dati[131] -= GlobalGameVar.costoOggetti[oggetton + 1] * numeroOggettiAcquistati
                            voceMarcata = 0
                            xp = GlobalHWVar.gsx // 32 * 10.5
                            # faretra
                            if confermaOggettoDaAcquistare == 11:
                                dati[133] += numeroOggettiAcquistati
                                yp = GlobalHWVar.gsy // 18 * 16
                            confermaOggettoDaAcquistare = 0
                            procediAllAcquisto = False
                        elif dati[133] == 2 and GlobalGameVar.costoOggetti[oggetton + 2] * numeroOggettiAcquistati <= dati[131]:
                            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAcquisto)
                            primoFrame = True
                            dati[131] -= GlobalGameVar.costoOggetti[oggetton + 2] * numeroOggettiAcquistati
                            voceMarcata = 0
                            xp = GlobalHWVar.gsx // 32 * 10.5
                            # faretra
                            if confermaOggettoDaAcquistare == 11:
                                dati[133] += numeroOggettiAcquistati
                                yp = GlobalHWVar.gsy // 18 * 16
                            confermaOggettoDaAcquistare = 0
                            procediAllAcquisto = False
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                            moneteInsufficienti = True
                            procediAllAcquisto = False
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        moneteInsufficienti = True
                        procediAllAcquisto = False
                elif voceMarcata == 2 or (voceMarcata == 1 and bottoneDown == "mouseSinistro" and suTornaIndietro):
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    voceMarcata = 0
                    numeroOggettiAcquistati = 1
                    xp = GlobalHWVar.gsx // 32 * 10.5
                    if confermaOggettoDaAcquistare == -1:
                        yp = GlobalHWVar.gsy // 18 * 6.1
                    if confermaOggettoDaAcquistare == 1:
                        yp = GlobalHWVar.gsy // 18 * 7
                    if confermaOggettoDaAcquistare == 2:
                        yp = GlobalHWVar.gsy // 18 * 7.9
                    if confermaOggettoDaAcquistare == 3:
                        yp = GlobalHWVar.gsy // 18 * 8.8
                    if confermaOggettoDaAcquistare == 4:
                        yp = GlobalHWVar.gsy // 18 * 9.7
                    if confermaOggettoDaAcquistare == 5:
                        yp = GlobalHWVar.gsy // 18 * 10.6
                    if confermaOggettoDaAcquistare == 6:
                        yp = GlobalHWVar.gsy // 18 * 11.5
                    if confermaOggettoDaAcquistare == 7:
                        yp = GlobalHWVar.gsy // 18 * 12.4
                    if confermaOggettoDaAcquistare == 8:
                        yp = GlobalHWVar.gsy // 18 * 13.3
                    if confermaOggettoDaAcquistare == 9:
                        yp = GlobalHWVar.gsy // 18 * 14.2
                    if confermaOggettoDaAcquistare == 10:
                        yp = GlobalHWVar.gsy // 18 * 15.1
                    if confermaOggettoDaAcquistare == 11:
                        yp = GlobalHWVar.gsy // 18 * 16
                    confermaOggettoDaAcquistare = 0
                    procediAllAcquisto = False
                elif voceMarcata == 0 and bottoneDown == "mouseSinistro" and suTornaIndietro:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    risposta = True
                    procediAllAcquisto = False

                # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                if procediAllAcquisto:
                    numeroOggettiAcquistati = 1
                    numOggettiPosseduti = dati[30 + oggetton]
                    if numOggettiPosseduti < 0:
                        numOggettiPosseduti = 0
                    if 1 <= oggetton <= 10 and numOggettiPosseduti < 99:
                        if oggetton == 1:
                            if imgOggetti[0] != sconosciutoOggetto:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                                confermaOggettoDaAcquistare = 1
                                usauno = True
                            else:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        if oggetton == 2:
                            if imgOggetti[1] != sconosciutoOggetto:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                                confermaOggettoDaAcquistare = 2
                                usauno = True
                            else:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        if oggetton == 3:
                            if imgOggetti[2] != sconosciutoOggetto:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                                confermaOggettoDaAcquistare = 3
                                usauno = True
                            else:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        if oggetton == 4:
                            if imgOggetti[3] != sconosciutoOggetto:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                                confermaOggettoDaAcquistare = 4
                                usauno = True
                            else:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        if oggetton == 5:
                            if imgOggetti[4] != sconosciutoOggetto:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                                confermaOggettoDaAcquistare = 5
                                usauno = True
                            else:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        if oggetton == 6:
                            if imgOggetti[5] != sconosciutoOggetto:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                                confermaOggettoDaAcquistare = 6
                                usauno = True
                            else:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        if oggetton == 7:
                            if imgOggetti[6] != sconosciutoOggetto:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                                confermaOggettoDaAcquistare = 7
                                usauno = True
                            else:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        if oggetton == 8:
                            if imgOggetti[7] != sconosciutoOggetto:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                                confermaOggettoDaAcquistare = 8
                                usauno = True
                            else:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        if oggetton == 9:
                            if imgOggetti[8] != sconosciutoOggetto:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                                confermaOggettoDaAcquistare = 9
                                usauno = True
                            else:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        if oggetton == 10:
                            if imgOggetti[9] != sconosciutoOggetto:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                                confermaOggettoDaAcquistare = 10
                                usauno = True
                            else:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    elif oggetton == 0 and dati[132] < maxFrecce:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        confermaOggettoDaAcquistare = -1
                        usauno = True
                    elif oggetton == 11 and dati[133] != 3:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        confermaOggettoDaAcquistare = 11
                        usauno = True
                    else:
                        inventarioPieno = True
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)

                bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == "mouseSinistro" or bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == pygame.K_a or bottoneDown == pygame.K_d or bottoneDown == "padGiu" or bottoneDown == "padSu" or bottoneDown == "padSinistra" or bottoneDown == "padDestra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or oggettonVecchio != oggetton or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 0:
                    if oggetton != 0:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        oggetton = oggetton - 1
                        yp = yp - GlobalHWVar.gsy // 18 * 0.9
                    elif oggetton == 0:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = GlobalHWVar.gsy // 18 * 16
                        oggetton = 11
                elif voceMarcata != 0:
                    if oggetton != 11:
                        numOggettiPosseduti = dati[30 + oggetton]
                        if numOggettiPosseduti < 0:
                            numOggettiPosseduti = 0
                        if (1 <= oggetton <= 10 and numOggettiPosseduti == 98) or (oggetton == 0 and dati[132] == maxFrecce - 1):
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if 1 <= oggetton <= 10 and numeroOggettiAcquistati + numOggettiPosseduti >= 99:
                            numeroOggettiAcquistati = 1
                        elif oggetton == 0 and numeroOggettiAcquistati + dati[132] >= maxFrecce:
                            numeroOggettiAcquistati = 1
                        else:
                            numeroOggettiAcquistati += 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        numeroOggettiAcquistati = 1
                        bottoneDown = False
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 2:
                    voceMarcata -= 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = xp - GlobalHWVar.gsx // 32 * 4
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 0:
                    if oggetton != 11:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        oggetton = oggetton + 1
                        yp = yp + GlobalHWVar.gsy // 18 * 0.9
                    elif oggetton == 11:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = GlobalHWVar.gsy // 18 * 6.1
                        oggetton = 0
                elif voceMarcata != 0:
                    if oggetton != 11:
                        numOggettiPosseduti = dati[30 + oggetton]
                        if numOggettiPosseduti < 0:
                            numOggettiPosseduti = 0
                        if (1 <= oggetton <= 10 and numOggettiPosseduti == 98) or (oggetton == 0 and dati[132] == maxFrecce - 1):
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if 1 <= oggetton <= 10 and numeroOggettiAcquistati == 1:
                            numeroOggettiAcquistati = 99 - numOggettiPosseduti
                        elif oggetton == 0 and numeroOggettiAcquistati == 1:
                            numeroOggettiAcquistati = maxFrecce - dati[132]
                        else:
                            numeroOggettiAcquistati -= 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        numeroOggettiAcquistati = 1
                        bottoneDown = False
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1:
                    voceMarcata += 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = xp + GlobalHWVar.gsx // 32 * 4
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if bottoneDown == "mouseSinistro" and (mouseInquadraFrecciaSu or mouseInquadraFrecciaGiu):
                if mouseInquadraFrecciaSu:
                    if voceMarcata != 0:
                        if oggetton != 11:
                            numOggettiPosseduti = dati[30 + oggetton]
                            if numOggettiPosseduti < 0:
                                numOggettiPosseduti = 0
                            if (1 <= oggetton <= 10 and numOggettiPosseduti == 98) or (oggetton == 0 and dati[132] == maxFrecce - 1):
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                            else:
                                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            if 1 <= oggetton <= 10 and numeroOggettiAcquistati + numOggettiPosseduti >= 99:
                                numeroOggettiAcquistati = 1
                            elif oggetton == 0 and numeroOggettiAcquistati + dati[132] >= maxFrecce:
                                numeroOggettiAcquistati = 1
                            else:
                                numeroOggettiAcquistati += 1
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                            numeroOggettiAcquistati = 1
                elif mouseInquadraFrecciaGiu:
                    if voceMarcata != 0:
                        if oggetton != 11:
                            numOggettiPosseduti = dati[30 + oggetton]
                            if numOggettiPosseduti < 0:
                                numOggettiPosseduti = 0
                            if (1 <= oggetton <= 10 and numOggettiPosseduti == 98) or (oggetton == 0 and dati[132] == maxFrecce - 1):
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                            else:
                                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            if 1 <= oggetton <= 10 and numeroOggettiAcquistati == 1:
                                numeroOggettiAcquistati = 99 - numOggettiPosseduti
                            elif oggetton == 0 and numeroOggettiAcquistati == 1:
                                numeroOggettiAcquistati = maxFrecce - dati[132]
                            else:
                                numeroOggettiAcquistati -= 1
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                            numeroOggettiAcquistati = 1
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            maxFrecce = 1
            if dati[133] == 1:
                maxFrecce = 5
            elif dati[133] == 2:
                maxFrecce = 20
            elif dati[133] == 3:
                maxFrecce = 60

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 16.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 16.5))

                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sacchettoDenaroMercante, (GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 14))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.mercanteMenu, (GlobalHWVar.gsx // 32 * (-1), GlobalHWVar.gsy // 18 * 8))

                GenericFunc.messaggio("Acquista oggetti", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                GenericFunc.messaggio("Oggetti acquistabili", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.5, GlobalHWVar.gsy // 18 * 4.7, 45, centrale=True)
                GenericFunc.messaggio("Costo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 4.7, 45, centrale=True)
                GenericFunc.messaggio("Posseduti", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 4.7, 45, centrale=True)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 11), int(GlobalHWVar.gpy * 5.5)), (int(GlobalHWVar.gpx * 20.9), int(GlobalHWVar.gpy * 5.5)), 1)

                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 16.2) - 1, int(GlobalHWVar.gpy * 4.5)), (int(GlobalHWVar.gpx * 16.2) - 1, int(GlobalHWVar.gpy * 5.3)), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 16.2) - 1, int(GlobalHWVar.gpy * 5.7)), (int(GlobalHWVar.gpx * 16.2) - 1, int(GlobalHWVar.gpy * 17)), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 18.2) - 1, int(GlobalHWVar.gpy * 4.5)), (int(GlobalHWVar.gpx * 18.2) - 1, int(GlobalHWVar.gpy * 5.3)), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 18.2) - 1, int(GlobalHWVar.gpy * 5.7)), (int(GlobalHWVar.gpx * 18.2) - 1, int(GlobalHWVar.gpy * 17)), 2)

                GenericFunc.messaggio("Freccia", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 6.2, 40)
                GenericFunc.messaggio(str(GlobalGameVar.costoOggetti[0]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 6.2, 40, centrale=True)
                GenericFunc.messaggio("x%i" % dati[132], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 6.2, 40, centrale=True)
                if imgOggetti[0] != sconosciutoOggetto:
                    GenericFunc.messaggio("Pozione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 7.1, 40)
                    GenericFunc.messaggio(str(GlobalGameVar.costoOggetti[1]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 7.1, 40, centrale=True)
                    if dati[31] < 0:
                        GenericFunc.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 7.1, 40, centrale=True)
                    else:
                        GenericFunc.messaggio("x%i" % dati[31], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 7.1, 40, centrale=True)
                else:
                    GenericFunc.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 7.1, 40)
                if imgOggetti[1] != sconosciutoOggetto:
                    GenericFunc.messaggio("Alimentazione 100gr", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 8, 40)
                    GenericFunc.messaggio(str(GlobalGameVar.costoOggetti[2]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 8, 40, centrale=True)
                    if dati[32] < 0:
                        GenericFunc.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 8, 40, centrale=True)
                    else:
                        GenericFunc.messaggio("x%i" % dati[32], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 8, 40, centrale=True)
                else:
                    GenericFunc.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 8, 40)
                if imgOggetti[2] != sconosciutoOggetto:
                    GenericFunc.messaggio("Medicina", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 8.9, 40)
                    GenericFunc.messaggio(str(GlobalGameVar.costoOggetti[3]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 8.9, 40, centrale=True)
                    if dati[33] < 0:
                        GenericFunc.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 8.9, 40, centrale=True)
                    else:
                        GenericFunc.messaggio("x%i" % dati[33], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 8.9, 40, centrale=True)
                else:
                    GenericFunc.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 8.9, 40)
                if imgOggetti[3] != sconosciutoOggetto:
                    GenericFunc.messaggio("Super pozione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 9.8, 40)
                    GenericFunc.messaggio(str(GlobalGameVar.costoOggetti[4]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 9.8, 40, centrale=True)
                    if dati[34] < 0:
                        GenericFunc.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 9.8, 40, centrale=True)
                    else:
                        GenericFunc.messaggio("x%i" % dati[34], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 9.8, 40, centrale=True)
                else:
                    GenericFunc.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 9.8, 40)
                if imgOggetti[4] != sconosciutoOggetto:
                    GenericFunc.messaggio("Alimentazione 250gr", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 10.7, 40)
                    GenericFunc.messaggio(str(GlobalGameVar.costoOggetti[5]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 10.7, 40, centrale=True)
                    if dati[35] < 0:
                        GenericFunc.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 10.7, 40, centrale=True)
                    else:
                        GenericFunc.messaggio("x%i" % dati[35], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 10.7, 40, centrale=True)
                else:
                    GenericFunc.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 10.7, 40)
                if imgOggetti[5] != sconosciutoOggetto:
                    GenericFunc.messaggio("Bomba", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 11.6, 40)
                    GenericFunc.messaggio(str(GlobalGameVar.costoOggetti[6]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 11.6, 40, centrale=True)
                    if dati[36] < 0:
                        GenericFunc.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 11.6, 40, centrale=True)
                    else:
                        GenericFunc.messaggio("x%i" % dati[36], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 11.6, 40, centrale=True)
                else:
                    GenericFunc.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 11.6, 40)
                if imgOggetti[6] != sconosciutoOggetto:
                    GenericFunc.messaggio("Bomba velenosa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 12.5, 40)
                    GenericFunc.messaggio(str(GlobalGameVar.costoOggetti[7]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 12.5, 40, centrale=True)
                    if dati[37] < 0:
                        GenericFunc.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 12.5, 40, centrale=True)
                    else:
                        GenericFunc.messaggio("x%i" % dati[37], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 12.5, 40, centrale=True)
                else:
                    GenericFunc.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 12.5, 40)
                if imgOggetti[7] != sconosciutoOggetto:
                    GenericFunc.messaggio("Esca", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 13.4, 40)
                    GenericFunc.messaggio(str(GlobalGameVar.costoOggetti[8]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 13.4, 40, centrale=True)
                    if dati[38] < 0:
                        GenericFunc.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 13.4, 40, centrale=True)
                    else:
                        GenericFunc.messaggio("x%i" % dati[38], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 13.4, 40, centrale=True)
                else:
                    GenericFunc.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 13.4, 40)
                if imgOggetti[8] != sconosciutoOggetto:
                    GenericFunc.messaggio("Bomba appiccicosa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 14.3, 40)
                    GenericFunc.messaggio(str(GlobalGameVar.costoOggetti[9]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 14.3, 40, centrale=True)
                    if dati[39] < 0:
                        GenericFunc.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 14.3, 40, centrale=True)
                    else:
                        GenericFunc.messaggio("x%i" % dati[39], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 14.3, 40, centrale=True)
                else:
                    GenericFunc.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 14.3, 40)
                if imgOggetti[9] != sconosciutoOggetto:
                    GenericFunc.messaggio("Bomba potenziata", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 15.2, 40)
                    GenericFunc.messaggio(str(GlobalGameVar.costoOggetti[10]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 15.2, 40, centrale=True)
                    if dati[40] < 0:
                        GenericFunc.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 15.2, 40, centrale=True)
                    else:
                        GenericFunc.messaggio("x%i" % dati[40], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 15.2, 40, centrale=True)
                else:
                    GenericFunc.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 15.2, 40)
                GenericFunc.messaggio("Faretra", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 16.1, 40)
                if dati[133] == 0:
                    GenericFunc.messaggio(str(GlobalGameVar.costoOggetti[11]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 16.1, 40, centrale=True)
                if dati[133] == 1:
                    GenericFunc.messaggio(str(GlobalGameVar.costoOggetti[12]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 16.1, 40, centrale=True)
                if dati[133] >= 2:
                    GenericFunc.messaggio(str(GlobalGameVar.costoOggetti[13]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 16.1, 40, centrale=True)
                if dati[133] == 3:
                    GenericFunc.messaggio("x1", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 16.1, 40, centrale=True)
                else:
                    GenericFunc.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 16.1, 40, centrale=True)
            elif confermaOggettoDaAcquistare == 0 and (oggettonVecchio != oggetton or voceMarcataVecchia != voceMarcata):
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.1, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 10.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 6.7, GlobalHWVar.gsx // 32 * 5.2, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 16.3, GlobalHWVar.gsy // 18 * 6.7, GlobalHWVar.gsx // 32 * 1.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 18.3, GlobalHWVar.gsy // 18 * 6.7, GlobalHWVar.gsx // 32 * 2.7, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 7.6, GlobalHWVar.gsx // 32 * 5.2, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 16.3, GlobalHWVar.gsy // 18 * 7.6, GlobalHWVar.gsx // 32 * 1.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 18.3, GlobalHWVar.gsy // 18 * 7.6, GlobalHWVar.gsx // 32 * 2.7, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 8.5, GlobalHWVar.gsx // 32 * 5.2, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 16.3, GlobalHWVar.gsy // 18 * 8.5, GlobalHWVar.gsx // 32 * 1.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 18.3, GlobalHWVar.gsy // 18 * 8.5, GlobalHWVar.gsx // 32 * 2.7, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 9.4, GlobalHWVar.gsx // 32 * 5.2, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 16.3, GlobalHWVar.gsy // 18 * 9.4, GlobalHWVar.gsx // 32 * 1.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 18.3, GlobalHWVar.gsy // 18 * 9.4, GlobalHWVar.gsx // 32 * 2.7, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 10.3, GlobalHWVar.gsx // 32 * 5.2, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 16.3, GlobalHWVar.gsy // 18 * 10.3, GlobalHWVar.gsx // 32 * 1.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 18.3, GlobalHWVar.gsy // 18 * 10.3, GlobalHWVar.gsx // 32 * 2.7, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 11.2, GlobalHWVar.gsx // 32 * 5.2, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 16.3, GlobalHWVar.gsy // 18 * 11.2, GlobalHWVar.gsx // 32 * 1.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 18.3, GlobalHWVar.gsy // 18 * 11.2, GlobalHWVar.gsx // 32 * 2.7, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 12.1, GlobalHWVar.gsx // 32 * 5.2, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 16.3, GlobalHWVar.gsy // 18 * 12.1, GlobalHWVar.gsx // 32 * 1.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 18.3, GlobalHWVar.gsy // 18 * 12.1, GlobalHWVar.gsx // 32 * 2.7, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gsx // 32 * 5.2, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 16.3, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gsx // 32 * 1.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 18.3, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gsx // 32 * 2.7, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 13.9, GlobalHWVar.gsx // 32 * 5.2, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 16.3, GlobalHWVar.gsy // 18 * 13.9, GlobalHWVar.gsx // 32 * 1.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 18.3, GlobalHWVar.gsy // 18 * 13.9, GlobalHWVar.gsx // 32 * 2.7, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 14.8, GlobalHWVar.gsx // 32 * 5.2, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 16.3, GlobalHWVar.gsy // 18 * 14.8, GlobalHWVar.gsx // 32 * 1.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 18.3, GlobalHWVar.gsy // 18 * 14.8, GlobalHWVar.gsx // 32 * 2.7, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 15.7, GlobalHWVar.gsx // 32 * 5.2, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 16.3, GlobalHWVar.gsy // 18 * 15.7, GlobalHWVar.gsx // 32 * 1.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 18.3, GlobalHWVar.gsy // 18 * 15.7, GlobalHWVar.gsx // 32 * 2.7, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 10.9, GlobalHWVar.gsy // 18 * 16.6, GlobalHWVar.gsx // 32 * 5.2, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 16.3, GlobalHWVar.gsy // 18 * 16.6, GlobalHWVar.gsx // 32 * 1.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 18.3, GlobalHWVar.gsy // 18 * 16.6, GlobalHWVar.gsx // 32 * 2.7, GlobalHWVar.gsy // 18 * 0.3))

                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gsx // 32 * 9.5, GlobalHWVar.gsy // 18 * 11))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15.5, GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 1))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2.5))
                if GlobalHWVar.mouseVisibile:
                    GenericFunc.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    GenericFunc.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    GenericFunc.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 9.5, GlobalHWVar.gsy // 18 * 4.5))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoDialogoMercante, (GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 4))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 4))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 7))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 7))
            if moneteInsufficienti:
                GenericFunc.messaggio("Non hai abbastanza monete!", GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 5.3, GlobalHWVar.gsy // 18 * 6.1, 40, centrale=True)
            if inventarioPieno:
                GenericFunc.messaggio("Non puoi prenderne altre...", GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 5.3, GlobalHWVar.gsy // 18 * 5.3, 40, centrale=True)

            # menu conferma
            if confermaOggettoDaAcquistare != 0:
                GenericFunc.messaggio("Quante te ne servono?", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, 50)
                # posizionare il cursore sul menu compra
                if usauno:
                    xpv = xp
                    ypv = yp
                    xp = GlobalHWVar.gsx // 32 * 5.3
                    yp = GlobalHWVar.gsy // 18 * 6.9
                    voceMarcata = 2
                    usauno = False
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xpv, ypv))
                GenericFunc.messaggio("x" + str(numeroOggettiAcquistati), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 7.5, GlobalHWVar.gsy // 18 * 4.5, 50)
                if oggetton == 11:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSuGiuBloccato, (GlobalHWVar.gsx // 32 * 8.5, GlobalHWVar.gsy // 18 * 4.3))
                    if dati[133] == 1:
                        GenericFunc.messaggio("(Monete necessarie: %i)" % (GlobalGameVar.costoOggetti[oggetton + 1] * numeroOggettiAcquistati), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5.3, 50)
                    elif dati[133] >= 2:
                        GenericFunc.messaggio("(Monete necessarie: %i)" % (GlobalGameVar.costoOggetti[oggetton + 2] * numeroOggettiAcquistati), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5.3, 50)
                    else:
                        GenericFunc.messaggio("(Monete necessarie: %i)" % (GlobalGameVar.costoOggetti[oggetton] * numeroOggettiAcquistati), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5.3, 50)
                else:
                    if voceMarcata != 0 and oggetton != 11 and (bottoneDown == pygame.K_w or (bottoneDown == "mouseSinistro" and mouseInquadraFrecciaSu) or bottoneDown == "padSu"):
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSuGiuBloccatoSu, (GlobalHWVar.gsx // 32 * 8.5, GlobalHWVar.gsy // 18 * 4.3))
                    elif voceMarcata != 0 and oggetton != 11 and (bottoneDown == pygame.K_s or (bottoneDown == "mouseSinistro" and mouseInquadraFrecciaGiu) or bottoneDown == "padGiu"):
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSuGiuBloccatoGiu, (GlobalHWVar.gsx // 32 * 8.5, GlobalHWVar.gsy // 18 * 4.3))
                    else:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSuGiu, (GlobalHWVar.gsx // 32 * 8.5, GlobalHWVar.gsy // 18 * 4.3))
                    GenericFunc.messaggio("(Monete necessarie: %i)" % (GlobalGameVar.costoOggetti[oggetton] * numeroOggettiAcquistati), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5.3, 50)
                GenericFunc.messaggio("Conferma", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.9, 50)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 5.3) - 1, int(GlobalHWVar.gpy * 6.8)), (int(GlobalHWVar.gpx * 5.3) - 1, int(GlobalHWVar.gpy * 7.5)), 2)
                GenericFunc.messaggio("Annulla", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 6.9, 50)
            else:
                GenericFunc.messaggio("Prendi quello che ti serve", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, 50)
                if primoFrame or oggettonVecchio != oggetton or voceMarcataVecchia != voceMarcata:
                    if 1 <= oggetton <= 10:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgOggetti[oggetton - 1], (GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 3))
                    elif oggetton == 0:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.frecciaMenu, (GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 3))
                    elif oggetton == 11:
                        if dati[133] == 0:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.faretra1Menu, (GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 3))
                        elif dati[133] == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.faretra2Menu, (GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 3))
                        else:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.faretra3Menu, (GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 3))

                    GenericFunc.messaggio("Monete: " + str(dati[131]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15.8, 50)

                    larghezzaTestoDescrizioni = GlobalHWVar.gpx * 8.5
                    spazioTraLeRigheTestoDescrizione = GlobalHWVar.gpy // 2
                    if oggetton == 0:
                        GenericFunc.messaggio("Freccia:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        GenericFunc.messaggio("Usate per attaccare i nemici a distanza.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if imgOggetti[0] != sconosciutoOggetto and oggetton == 1:
                        GenericFunc.messaggio("Pozione:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        GenericFunc.messaggio("Recupera 100 <*>#italic#Pv<*> di Lucy.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 1:
                        GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[1] != sconosciutoOggetto and oggetton == 2:
                        GenericFunc.messaggio("Alimentazione 100gr:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        GenericFunc.messaggio("Recupera 250 <*>#italic#Pe<*> di Impo.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 2:
                        GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[2] != sconosciutoOggetto and oggetton == 3:
                        GenericFunc.messaggio("Medicina:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        GenericFunc.messaggio("Cura avvelenamento a Lucy.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 3:
                        GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[3] != sconosciutoOggetto and oggetton == 4:
                        GenericFunc.messaggio("Super pozione:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        GenericFunc.messaggio("Recupera 300 <*>#italic#Pv<*> di Lucy.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 4:
                        GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[4] != sconosciutoOggetto and oggetton == 5:
                        GenericFunc.messaggio("Alimentazione 250gr:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        GenericFunc.messaggio("Recupera 600 <*>#italic#Pe<*> di Impo.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 5:
                        GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[5] != sconosciutoOggetto and oggetton == 6:
                        GenericFunc.messaggio("Bomba:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        GenericFunc.messaggio("Infligge un po' di danni ai nemici su cui viene lanciata.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 6:
                        GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[6] != sconosciutoOggetto and oggetton == 7:
                        GenericFunc.messaggio("Bomba velenosa:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        GenericFunc.messaggio("Infligge avvelenamento al nemico su cui viene lanciata.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 7:
                        GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[7] != sconosciutoOggetto and oggetton == 8:
                        GenericFunc.messaggio("Esca:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        GenericFunc.messaggio(u"Distrae i nemici finché non viene distrutta. È possibile riprenderla passandoci sopra.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 8:
                        GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[8] != sconosciutoOggetto and oggetton == 9:
                        GenericFunc.messaggio("Bomba appiccicosa:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        GenericFunc.messaggio(u"Dimezza la velocità del nemico su cui viene lanciata.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 9:
                        GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[9] != sconosciutoOggetto and oggetton == 10:
                        GenericFunc.messaggio("Bomba potenziata:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        GenericFunc.messaggio("Infligge molti danni ai nemici su cui viene lanciata in un vasto raggio.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 10:
                        GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if oggetton == 11:
                        GenericFunc.messaggio("Faretra:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        GenericFunc.messaggio(u"Permette di trasportare più frecce.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)

            primoFrame = False
            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            if confermaOggettoDaAcquistare == 0:
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xp + (int(GlobalHWVar.gpx * 0.5))), yp + (int(GlobalHWVar.gpy * 0.7))), (xp + (int(GlobalHWVar.gpx * 5.5)), yp + (int(GlobalHWVar.gpy * 0.7))), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xp + (int(GlobalHWVar.gpx * 5.9))), yp + (int(GlobalHWVar.gpy * 0.7))), (xp + (int(GlobalHWVar.gpx * 7.5)), yp + (int(GlobalHWVar.gpy * 0.7))), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xp + (int(GlobalHWVar.gpx * 7.9))), yp + (int(GlobalHWVar.gpy * 0.7))), (xp + (int(GlobalHWVar.gpx * 10.4)), yp + (int(GlobalHWVar.gpy * 0.7))), 2)
            else:
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xpv + (int(GlobalHWVar.gpx * 0.5))), ypv + (int(GlobalHWVar.gpy * 0.7))), (xpv + (int(GlobalHWVar.gpx * 5.5)), ypv + (int(GlobalHWVar.gpy * 0.7))), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xpv + (int(GlobalHWVar.gpx * 5.9))), ypv + (int(GlobalHWVar.gpy * 0.7))), (xpv + (int(GlobalHWVar.gpx * 7.5)), ypv + (int(GlobalHWVar.gpy * 0.7))), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xpv + (int(GlobalHWVar.gpx * 7.9))), ypv + (int(GlobalHWVar.gpy * 0.7))), (xpv + (int(GlobalHWVar.gpx * 10.4)), ypv + (int(GlobalHWVar.gpy * 0.7))), 2)

            GlobalHWVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)

    GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
    GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti)
    return dati
