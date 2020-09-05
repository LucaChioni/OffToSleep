# -*- coding: utf-8 -*-

from SottoMenuA import *


def menu(caricaSalvataggio):
    GlobalVar.canaleSoundCanzone.stop()
    canzone = False

    # per aggiungere porte e cofanetti => aggiungi "numStanza, x, y, False"
    xInizialie = 0
    yInizialie = 0
    rxInizialie = 0
    ryInizialie = 0
    # progresso - stanza - x - y - liv - pv - spada - scudo - armatura - armrob - energiarob - tecniche(20) - oggetti(10) - equipaggiamento(30) - batterie(10) - condizioni(20) - gambit(20) -
    # veleno - surriscalda - attp - difp - velp(x2) - efficienza - esperienza - arco - guanti - collana - monete - frecce - faretra -
    # rx - ry - raffredda - autoRic1 - autoRic2 - mosseRimasteRob - npers - nrob -
    # porte(142-?) - cofanetti(?-?) // dimensione: 0-141 (=> 142 variabili) + porte e cofanetti
    datiIniziali = [0, 1, xInizialie, yInizialie, 1, 55, 0, 0, 0, 0, 220,  # <- statistiche
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # <- tecniche
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  # <- oggetti
        2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, # <- equpaggiamento
        2, 0, 0, 0, 0, -1, -1, -1, -1, -1,  # <- batterie (sono utilizzati solo i primi 5)
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # <- condizioni
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  # <- gambit
        False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # <- altre statistiche
        rxInizialie, ryInizialie, -1, -1, -1, 0, 4, 3,  # <- info aggiunte per poter salvare ovunque
        ]

    # posizione porte e cofanetti nel vettore dati
    vetPorte = GlobalVar.initVetPorteGlobale
    vetCofanetti = GlobalVar.initVetCofanettiGlobale

    porteini = len(datiIniziali)
    portefin = len(datiIniziali) + len(vetPorte) - 1
    cofaniini = portefin + 1
    cofanifin = len(datiIniziali) + len(vetPorte) + len(vetCofanetti) - 1
    datiIniziali += vetPorte
    datiIniziali += vetCofanetti
    lunghezzadati = len(datiIniziali)

    if caricaSalvataggio:
        dati, listaNemiciTotali, listaEsche, listaMonete, stanzeGiaVisitate, listaPersonaggiTotali = caricaPartita(caricaSalvataggio, lunghezzadati, porteini, portefin, cofaniini, cofanifin, canzone)
        return dati, porteini, portefin, cofaniini, cofanifin, listaNemiciTotali, listaEsche, listaMonete, stanzeGiaVisitate, listaPersonaggiTotali

    # video
    fermavideo = guardaVideo('Video/videoinizio')
    # attesa dopo video
    if not fermavideo:
        if GlobalVar.mouseBloccato:
            GlobalVar.configuraCursore(False)
        GlobalVar.schermo.fill(GlobalVar.grigioscu)
        messaggio("Premi un tasto per continuare...", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 13, 100)
        pygame.display.update()
        finevideo = True
        sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
        while finevideo:
            for event in pygame.event.get():
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
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN or (event.type == pygame.MOUSEBUTTONDOWN and (sinistroMouse or centraleMouse or destroMouse) and not rotellaConCentralePremuto):
                    if event.type == pygame.KEYDOWN and GlobalVar.mouseVisibile:
                        pygame.mouse.set_visible(False)
                        GlobalVar.mouseVisibile = False
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                    finevideo = False

    xp = GlobalVar.gsx // 32 * 1.5
    yp = GlobalVar.gsy // 18 * 2.5
    voceMarcata = 1
    primoFrame = True
    aggiornaSchermo = False
    puntatore = GlobalVar.puntatore
    puntatorevecchio = GlobalVar.puntatorevecchio
    robomenuinizio = GlobalVar.robograf0
    aggiornaInterfacciaPerMouse = False
    mostraTutorial = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
    deltaXMouse, deltaYMouse = pygame.mouse.get_rel()

    tastop = 0
    tastotempfps = 5

    # numero per la posizione di robo all'avvio
    c = random.randint(1, 4)

    canzone = GlobalVar.canzoneMenuPrincipale
    GlobalVar.canaleSoundCanzone.play(canzone)
    while True:
        if canzone and not GlobalVar.canaleSoundCanzone.get_busy():
            GlobalVar.canaleSoundCanzone.play(canzone)

        # rallenta per i 30 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        else:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        suTutorial = False
        suTogliTutorial = False
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVar.mouseVisibile:
            aggiornaInterfacciaPerMouse = True
            pygame.mouse.set_visible(True)
            GlobalVar.mouseVisibile = True
        if GlobalVar.mouseVisibile:
            if not mostraTutorial:
                if 0 <= xMouse <= GlobalVar.gsx // 32 * 7.5 and GlobalVar.gsy // 18 * 16.2 <= yMouse <= GlobalVar.gsy:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    suTutorial = True
                elif 0 <= xMouse <= GlobalVar.gsx // 32 * 11:
                    if GlobalVar.gsy // 18 * 1.5 <= yMouse <= GlobalVar.gsy // 18 * 4:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalVar.gsx // 32 * 1.5
                        yp = GlobalVar.gsy // 18 * 2.5
                    elif GlobalVar.gsy // 18 * 4 <= yMouse <= GlobalVar.gsy // 18 * 6.5:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalVar.gsx // 32 * 1.5
                        yp = GlobalVar.gsy // 18 * 5
                    elif GlobalVar.gsy // 18 * 6.5 <= yMouse <= GlobalVar.gsy // 18 * 9:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 3
                        xp = GlobalVar.gsx // 32 * 1.5
                        yp = GlobalVar.gsy // 18 * 7.5
                    elif GlobalVar.gsy // 18 * 11.5 <= yMouse <= GlobalVar.gsy // 18 * 14:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 4
                        xp = GlobalVar.gsx // 32 * 1.5
                        yp = GlobalVar.gsy // 18 * 12.5
                    else:
                        if not GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(True)
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            else:
                if GlobalVar.gsx // 32 * 21.5 <= xMouse <= GlobalVar.gsx and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    suTogliTutorial = True
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)

        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
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
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato and voceMarcataVecchia == voceMarcata:
                if GlobalVar.mouseVisibile:
                    aggiornaInterfacciaPerMouse = True
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                tastop = event.key
                tastotempfps = 5
                if event.key == pygame.K_q and not tastoTrovato and mostraTutorial:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    mostraTutorial = False
                    tastoTrovato = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or (GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse and not rotellaConCentralePremuto):
                tastoTrovato = True
                tastop = "escOdestroMouse"
                if event.type == pygame.KEYDOWN and GlobalVar.mouseVisibile:
                    aggiornaInterfacciaPerMouse = True
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if not mostraTutorial:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                    mostraTutorial = True
                else:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    mostraTutorial = False
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and not GlobalVar.mouseBloccato):
                tastoTrovato = True
                tastop = "spazioOsinistroMouse"
                if event.type == pygame.KEYDOWN and GlobalVar.mouseVisibile:
                    aggiornaInterfacciaPerMouse = True
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if suTutorial and event.type == pygame.MOUSEBUTTONDOWN:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                    mostraTutorial = True
                else:
                    if not mostraTutorial:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                        # nuova partita
                        if voceMarcata == 1:
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                            GlobalVar.schermo.blit(puntatorevecchio, (xp, yp))
                            schermo_temp = GlobalVar.schermo.copy()
                            background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalVar.gsx, GlobalVar.gsy))
                            inutile, conferma = chiediconferma(3, canzone)
                            if conferma:
                                dati = datiIniziali
                                xInizialie = GlobalVar.gsx // 32 * 15
                                yInizialie = GlobalVar.gsy // 18 * 7
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
                                GlobalVar.canaleSoundCanzone.stop()
                                i = porteini
                                while i <= portefin:
                                    dati[i + 1] = dati[i + 1] * GlobalVar.gpx
                                    dati[i + 2] = dati[i + 2] * GlobalVar.gpy
                                    i = i + 4
                                i = cofaniini
                                while i <= cofanifin:
                                    dati[i + 1] = dati[i + 1] * GlobalVar.gpx
                                    dati[i + 2] = dati[i + 2] * GlobalVar.gpy
                                    i = i + 4
                                return dati, porteini, portefin, cofaniini, cofanifin, datiNemici, datiEsche, datiMonete, stanzeGiaVisitate, listaPersonaggiTotali
                            else:
                                GlobalVar.schermo.blit(background, (0, 0))

                        # carica partita
                        if voceMarcata == 2:
                            n, inutile = scegli_sal(False, lunghezzadati, porteini, portefin, cofaniini, cofanifin, canzone)

                            # lettura salvataggio
                            if n != -1:
                                dati, datiNemici, datiEsche, datiMonete, stanzeGiaVisitate, listaPersonaggiTotali = caricaPartita(n, lunghezzadati, porteini, portefin, cofaniini, cofanifin, canzone)
                                if dati:
                                    return dati, porteini, portefin, cofaniini, cofanifin, datiNemici, datiEsche, datiMonete, stanzeGiaVisitate, listaPersonaggiTotali

                        # Impostazioni
                        if voceMarcata == 3:
                            menuImpostazioni(canzone, True, False)
                            primoFrame = True

                        # esci dal gioco
                        if voceMarcata == 4:
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                            GlobalVar.schermo.blit(puntatorevecchio, (xp, yp))
                            schermo_temp = GlobalVar.schermo.copy()
                            background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalVar.gsx, GlobalVar.gsy))
                            inizio, inutile = chiediconferma(2, canzone)
                            if not inizio:
                                GlobalVar.schermo.blit(background, (0, 0))
                    elif suTogliTutorial and event.type == pygame.MOUSEBUTTONDOWN:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                        mostraTutorial = False
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

        if aggiornaSchermo or primoMovimento or tastop == "spazioOsinistroMouse" or tastop == "escOdestroMouse" or ((tastop == pygame.K_q) or (tastop == pygame.K_s or tastop == pygame.K_w) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerMouse:
            aggiornaInterfacciaPerMouse = False
            aggiornaSchermo = False
            if primoFrame:
                puntatore = GlobalVar.puntatore
                xp = GlobalVar.gsx // 32 * 1.5
                if voceMarcata == 1:
                    yp = GlobalVar.gsy // 18 * 2.5
                if voceMarcata == 2:
                    yp = GlobalVar.gsy // 18 * 5
                if voceMarcata == 3:
                    yp = GlobalVar.gsy // 18 * 7.5
                if voceMarcata == 4:
                    yp = GlobalVar.gsy // 18 * 12.5
                primoFrame = False
            if not primoMovimento and (tastop == pygame.K_s or tastop == pygame.K_w):
                tastotempfps = 2
            if not mostraTutorial:
                if tastop == pygame.K_s:
                    if GlobalVar.mouseVisibile:
                        pygame.mouse.set_visible(False)
                        GlobalVar.mouseVisibile = False
                    if voceMarcata != 4:
                        if voceMarcata == 1:
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                            yp = GlobalVar.gsy // 18 * 5
                        elif voceMarcata == 2:
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                            yp = GlobalVar.gsy // 18 * 7.5
                        elif voceMarcata == 3:
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                            yp = GlobalVar.gsy // 18 * 12.5
                        voceMarcata += 1
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        yp = GlobalVar.gsy // 18 * 2.5
                        voceMarcata -= 3
                if tastop == pygame.K_w:
                    if GlobalVar.mouseVisibile:
                        pygame.mouse.set_visible(False)
                        GlobalVar.mouseVisibile = False
                    if voceMarcata != 1:
                        if voceMarcata == 2:
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                            yp = GlobalVar.gsy // 18 * 2.5
                        elif voceMarcata == 3:
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                            yp = GlobalVar.gsy // 18 * 5
                        elif voceMarcata == 4:
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                            yp = GlobalVar.gsy // 18 * 7.5
                        voceMarcata -= 1
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        yp = GlobalVar.gsy // 18 * 12.5
                        voceMarcata += 3
                GlobalVar.schermo.fill(GlobalVar.grigioscu)
                persomenuinizio = GlobalVar.persGrafMenu
                if c == 1:
                    robomenuinizio = GlobalVar.robograf0
                if c == 2:
                    robomenuinizio = GlobalVar.robograf1
                if c == 3:
                    robomenuinizio = GlobalVar.robograf2
                if c == 4:
                    robomenuinizio = GlobalVar.robograf3
                GlobalVar.schermo.blit(persomenuinizio, (GlobalVar.gpx * 15, 0))
                GlobalVar.schermo.blit(robomenuinizio, (GlobalVar.gpx * 3, 0))
                messaggio("Inizia", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2.5, GlobalVar.gsy // 18 * 2, 90)
                messaggio("Continua", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2.5, GlobalVar.gsy // 18 * 4.5, 90)
                messaggio("Impostazioni", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2.5, GlobalVar.gsy // 18 * 7, 90)
                messaggio("Esci", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2.5, GlobalVar.gsy // 18 * 12, 90)

                if GlobalVar.mouseVisibile:
                    messaggio("Tasto destro: comandi", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 16.8, 50)
                else:
                    messaggio("Esc: comandi", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1.7, GlobalVar.gsy // 18 * 16.8, 50)

                GlobalVar.schermo.blit(puntatore, (xp, yp))
            else:
                GlobalVar.schermo.fill(GlobalVar.grigioscu)
                if GlobalVar.mouseVisibile:
                    messaggio("Comandi mouse", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 1, 150)

                    messaggio("Mod. movimento", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4.2, 80)
                    GlobalVar.schermo.blit(GlobalVar.tutorialMouse, (GlobalVar.gsx // 32 * 0.2, GlobalVar.gsy // 18 * 6))
                    messaggio("Movimento (su casella libera) /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 6.8, 35)
                    messaggio("Interagisci (su casella interagibile) /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 7.3, 35)
                    messaggio("Attiva o disattiva Colco (su telecolco) /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 7.8, 35)
                    messaggio("Menu (su stato personaggio) /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 8.3, 35)
                    messaggio(u"Modalità interazione (su stato nemico)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 8.8, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 9.8), (GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 9.8), 2)
                    messaggio(u"Modalità interazione /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 11.1, 35)
                    messaggio("Rimuovi selezione (su stato nemico)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 11.6, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 13.2), (GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 13.2), 2)
                    messaggio("Menu", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 14.7, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 4), (GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 17), 2)

                    messaggio("Mod. interazione", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 4.2, 80)
                    GlobalVar.schermo.blit(GlobalVar.tutorialMouse, (GlobalVar.gsx // 32 * 10.7, GlobalVar.gsy // 18 * 6))
                    messaggio("Inquadra o attacca (su casella nemica) /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 13.5, GlobalVar.gsy // 18 * 6.8, 35)
                    messaggio("Interagisci (su casella interagibile) /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 13.5, GlobalVar.gsy // 18 * 7.3, 35)
                    messaggio("Attiva o disattiva Colco (su telecolco) /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 13.5, GlobalVar.gsy // 18 * 7.8, 35)
                    messaggio("Menu (su stato personaggio) /", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 13.5, GlobalVar.gsy // 18 * 8.3, 35)
                    messaggio(u"Modalità movimento (su stato nemico)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 13.5, GlobalVar.gsy // 18 * 8.8, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 9.8), (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 9.8), 2)
                    messaggio(u"Modalità movimento", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 13.5, GlobalVar.gsy // 18 * 11.3, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 13.2), (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 13.2), 2)
                    messaggio("Menu", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 13.5, GlobalVar.gsy // 18 * 14.7, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 4), (GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 17), 2)

                    messaggio("Menu", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 4.2, 80)
                    GlobalVar.schermo.blit(GlobalVar.tutorialMouse, (GlobalVar.gsx // 32 * 21.2, GlobalVar.gsy // 18 * 6))
                    messaggio("Seleziona", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 7.8, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 21.5, GlobalVar.gsy // 18 * 9.8), (GlobalVar.gsx // 32 * 31, GlobalVar.gsy // 18 * 9.8), 2)
                    messaggio("Indietro / Esci", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 11.3, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 21.5, GlobalVar.gsy // 18 * 13.2), (GlobalVar.gsx // 32 * 31, GlobalVar.gsy // 18 * 13.2), 2)
                    messaggio("Cambia operazione (se consentito)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 14.7, 35)
                else:
                    messaggio("Comandi tastiera", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 1, 150)
                    messaggio("Mod. movimento", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4.2, 80)
                    GlobalVar.schermo.blit(GlobalVar.tutorialTastieraInGioco, (GlobalVar.gsx // 32 * 0.2, GlobalVar.gsy // 18 * 6))
                    messaggio("Menu", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 4.2, GlobalVar.gsy // 18 * 6.7, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 7.3), (GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 7.3), 2)
                    messaggio("Cambia bersaglio inquadrato", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 4.2, GlobalVar.gsy // 18 * 7.9, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 8.7), (GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 8.7), 2)
                    messaggio("Deseleziona bersaglio", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 4.2, GlobalVar.gsy // 18 * 9.3, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 10.1), (GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 10.1), 2)
                    messaggio(u"Modalità interazione", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 4.2, GlobalVar.gsy // 18 * 10.7, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 11.5), (GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 11.5), 2)
                    messaggio("Movimento", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 4.2, GlobalVar.gsy // 18 * 12.7, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 14), (GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 14), 2)
                    messaggio("Attiva o disattiva Colco", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 4.2, GlobalVar.gsy // 18 * 14.6, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 15.4), (GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 15.4), 2)
                    messaggio("Interagisci", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 4.2, GlobalVar.gsy // 18 * 16, 35)

                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 4), (GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 17), 2)
                    messaggio("Mod. interazione", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 4.2, 80)
                    GlobalVar.schermo.blit(GlobalVar.tutorialTastieraInGioco, (GlobalVar.gsx // 32 * 10.7, GlobalVar.gsy // 18 * 6))
                    messaggio("Menu", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 6.7, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 7.3), (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 7.3), 2)
                    messaggio("Punta sul prossimo bersaglio", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 7.9, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 8.7), (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 8.7), 2)
                    messaggio(u"Modalità movimento", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 9.3, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 10.1), (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 10.1), 2)
                    messaggio("Inquadra bersaglio puntato", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 10.7, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 11.5), (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 11.5), 2)
                    messaggio("Sposta puntatore", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 12.7, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 14), (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 14), 2)
                    messaggio("Attiva o disattiva Colco", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 14.6, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 15.4), (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 15.4), 2)
                    messaggio("Attacca / Interagisci", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 14.7, GlobalVar.gsy // 18 * 16, 35)

                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 4), (GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 17), 2)
                    messaggio("Menu", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 4.2, 80)
                    GlobalVar.schermo.blit(GlobalVar.tutorialTastieraInMenu, (GlobalVar.gsx // 32 * 21.2, GlobalVar.gsy // 18 * 6))
                    messaggio("Esci (dove specificato)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25.2, GlobalVar.gsy // 18 * 8.1, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 21.5, GlobalVar.gsy // 18 * 8.7), (GlobalVar.gsx // 32 * 31, GlobalVar.gsy // 18 * 8.7), 2)
                    messaggio("Indietro / Esci", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25.2, GlobalVar.gsy // 18 * 9.3, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 21.5, GlobalVar.gsy // 18 * 10.1), (GlobalVar.gsx // 32 * 31, GlobalVar.gsy // 18 * 10.1), 2)
                    messaggio("Sposta puntatore", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25.2, GlobalVar.gsy // 18 * 11.3, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 21.5, GlobalVar.gsy // 18 * 12.6), (GlobalVar.gsx // 32 * 31, GlobalVar.gsy // 18 * 12.6), 2)
                    messaggio("Cambia operazione (se consentito)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25.2, GlobalVar.gsy // 18 * 13.2, 35)
                    pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 21.5, GlobalVar.gsy // 18 * 14), (GlobalVar.gsx // 32 * 31, GlobalVar.gsy // 18 * 14), 2)
                    messaggio("Seleziona", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25.2, GlobalVar.gsy // 18 * 14.6, 35)

                if GlobalVar.mouseVisibile:
                    messaggio("Tasto destro: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 1, 50)
                else:
                    messaggio("Esc / Q: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 1, 50)
            pygame.display.update()

        GlobalVar.clockMenu.tick(GlobalVar.fpsMenu)


def start(dati, porteini, portefin, cofaniini, cofanifin, porte, cofanetti, listaNemiciTotali, vitaesca, vettoreDenaro, stanzeGiaVisitate, listaPersonaggiTotali, canzone):
    sfondostastart = GlobalVar.sfondostax3
    if GlobalVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= dati[0] < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
        perssta = GlobalVar.fraMaggioreGrafMenu
    else:
        perssta = GlobalVar.saraGrafMenu
    robosta = GlobalVar.robograf1b
    puntatore = GlobalVar.puntatore
    puntatoreVecchio = GlobalVar.puntatorevecchio
    avvelenatosta = pygame.transform.smoothscale(GlobalVar.avvelenatoo, (GlobalVar.gpx, GlobalVar.gpy))
    surriscaldatosta = pygame.transform.smoothscale(GlobalVar.surriscaldatoo, (GlobalVar.gpx, GlobalVar.gpy))
    attaccopiusta = pygame.transform.smoothscale(GlobalVar.attaccopiuo, (GlobalVar.gpx, GlobalVar.gpy))
    difesapiusta = pygame.transform.smoothscale(GlobalVar.difesapiuo, (GlobalVar.gpx, GlobalVar.gpy))
    velocitapiusta = pygame.transform.smoothscale(GlobalVar.velocitapiuo, (GlobalVar.gpx, GlobalVar.gpy))
    efficienzapiusta = pygame.transform.smoothscale(GlobalVar.efficienzapiuo, (GlobalVar.gpx, GlobalVar.gpy))
    if dati[133] == 0:
        faretraFrecceStart = GlobalVar.faretraFrecceStart0
        maxFrecce = 1
    elif dati[133] == 1:
        faretraFrecceStart = GlobalVar.faretraFrecceStart1
        maxFrecce = 5
    elif dati[133] == 2:
        faretraFrecceStart = GlobalVar.faretraFrecceStart2
        maxFrecce = 20
    elif dati[133] == 3:
        faretraFrecceStart = GlobalVar.faretraFrecceStart3
        maxFrecce = 60
    else:
        faretraFrecceStart = 0
        maxFrecce = 0
    xp = GlobalVar.gsx // 32 * 1
    yp = GlobalVar.gsy // 18 * 5
    carim = True
    risposta = False
    attacco = 0
    conferma = 0
    inizio = False
    voceMarcata = 1
    primoFrame = True
    aggiornaSchermo = False
    aggiornaInterfacciaPerMouse = False
    caricaSalvataggio = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    tastop = 0
    tastotempfps = 5

    GlobalVar.canaleSoundCanzone.set_volume(GlobalVar.volumeCanzoni / 2)
    while not risposta:
        if canzone and not GlobalVar.canaleSoundCanzone.get_busy():
            GlobalVar.canaleSoundCanzone.play(canzone)

        # rallenta per i 30 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        else:
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
            if GlobalVar.gsx // 32 * 19 <= xMouse <= GlobalVar.gsx and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalVar.gsx // 32 * 1 <= xMouse <= GlobalVar.gsx // 32 * 11:
                if GlobalVar.gsy // 18 * 4.8 <= yMouse <= GlobalVar.gsy // 18 * 5.8:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 5
                elif GlobalVar.gsy // 18 * 5.8 <= yMouse <= GlobalVar.gsy // 18 * 6.8:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 6
                elif dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] and GlobalVar.gsy // 18 * 6.8 <= yMouse <= GlobalVar.gsy // 18 * 7.8:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 7
                elif dati[0] >= GlobalVar.dictAvanzamentoStoria["trovatoMappaDiario"] and GlobalVar.gsy // 18 * 7.8 <= yMouse <= GlobalVar.gsy // 18 * 8.8:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 8
                elif dati[0] >= GlobalVar.dictAvanzamentoStoria["trovatoMappaDiario"] and GlobalVar.gsy // 18 * 8.8 <= yMouse <= GlobalVar.gsy // 18 * 9.8:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 9
                elif GlobalVar.gsy // 18 * 12.8 <= yMouse <= GlobalVar.gsy // 18 * 13.8:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 13
                elif GlobalVar.gsy // 18 * 13.8 <= yMouse <= GlobalVar.gsy // 18 * 14.8:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 14
                elif GlobalVar.gsy // 18 * 14.8 <= yMouse <= GlobalVar.gsy // 18 * 15.8:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 15
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
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato and voceMarcataVecchia == voceMarcata:
                if GlobalVar.mouseVisibile:
                    aggiornaInterfacciaPerMouse = True
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                tastop = event.key
                tastotempfps = 5
                if (event.key == pygame.K_q or event.key == pygame.K_ESCAPE) and not tastoTrovato:
                    tastoTrovato = True
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    inizio = False
                    risposta = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and ((destroMouse or centraleMouse) and not rotellaConCentralePremuto):
                tastoTrovato = True
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                inizio = False
                risposta = True
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and not GlobalVar.mouseBloccato):
                tastoTrovato = True
                tastop = "spazioOsinistroMouse"
                inizio = False
                if event.type == pygame.MOUSEBUTTONDOWN and suTornaIndietro:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    risposta = True
                else:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                    # oggetti
                    if voceMarcata == 1:
                        dati, attacco = oggetti(dati, canzone)
                        carim = True
                    # equip pers
                    if voceMarcata == 2:
                        dati = equip(dati, canzone)
                        carim = True
                    # equip robot
                    if voceMarcata == 3:
                        dati = equiprobo(dati, canzone)
                        carim = True
                    # mappa
                    if voceMarcata == 4:
                        menuMappa(dati[0], canzone)
                    # diario
                    if voceMarcata == 5:
                        menuDiario(dati, canzone)
                    # salva
                    if voceMarcata == 6:
                        # azioneFatta contiene 3 se è stato fatto un salvataggio, altrimenti 1 se è stato caricato un salvataggio
                        n, azioneFatta = scegli_sal(True, len(dati), porteini, portefin, cofaniini, cofanifin, canzone)
                        if n != -1 and azioneFatta == 3:
                            salvataggio(n, dati, porteini, portefin, cofaniini, cofanifin, porte, cofanetti, listaNemiciTotali, vitaesca, vettoreDenaro, stanzeGiaVisitate, listaPersonaggiTotali)
                        elif n != -1 and azioneFatta == 1:
                            caricaSalvataggio = n
                            risposta = True
                    # impostazioni
                    if voceMarcata == 7:
                        menuImpostazioni(canzone, False, True)
                    # menu principale
                    if voceMarcata == 8:
                        GlobalVar.schermo.blit(puntatoreVecchio, (xp, yp))
                        conferma = 1
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

        if aggiornaSchermo or primoMovimento or tastop == "spazioOsinistroMouse" or ((tastop == pygame.K_s or tastop == pygame.K_w) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerMouse:
            aggiornaInterfacciaPerMouse = False
            aggiornaSchermo = False
            primoFrame = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_s:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if dati[0] < GlobalVar.dictAvanzamentoStoria["trovatoMappaDiario"] and voceMarcata == 2:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = yp + GlobalVar.gsy // 18 * 7
                    voceMarcata += 4
                elif dati[0] < GlobalVar.dictAvanzamentoStoria["trovatoMappaDiario"] and voceMarcata == 2:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = yp + GlobalVar.gsy // 18 * 2
                    voceMarcata += 2
                elif voceMarcata != 5 and voceMarcata != 8:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = yp + GlobalVar.gsy // 18 * 1
                    voceMarcata += 1
                else:
                    if voceMarcata == 5:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        yp = yp + GlobalVar.gsy // 18 * 4
                        voceMarcata += 1
                    elif voceMarcata == 8:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        yp = GlobalVar.gsy // 18 * 5
                        voceMarcata = 1
            if tastop == pygame.K_w:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if dati[0] < GlobalVar.dictAvanzamentoStoria["trovatoMappaDiario"] and voceMarcata == 6:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = yp - GlobalVar.gsy // 18 * 7
                    voceMarcata -= 4
                elif dati[0] < GlobalVar.dictAvanzamentoStoria["incontratoColco"] and voceMarcata == 4:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = yp - GlobalVar.gsy // 18 * 2
                    voceMarcata -= 2
                elif voceMarcata != 6 and voceMarcata != 1:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = yp - GlobalVar.gsy // 18 * 1
                    voceMarcata -= 1
                else:
                    if voceMarcata == 6:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        yp = yp - GlobalVar.gsy // 18 * 4
                        voceMarcata -= 1
                    elif voceMarcata == 1:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        yp = GlobalVar.gsy // 18 * 15
                        voceMarcata = 8
            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

            # chiedere conferma per uscire
            if conferma != 0:
                inizio, risposta = chiediconferma(conferma, canzone)
                conferma = 0

            GlobalVar.schermo.fill(GlobalVar.grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 12.5))
            GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4))
            GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoDestra, (GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 4))
            GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoBassoDestra, (GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 15.5))
            GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoBassoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 15.5))
            messaggio("Menu", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 1, 150)
            messaggio("Oggetti", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 5, 50)
            messaggio("Equipaggiamento", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 6, 50)
            if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
                messaggio("Setta Colco", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7, 50)
            if dati[0] >= GlobalVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
                messaggio("Mappa", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 8, 50)
                messaggio("Diario", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 9, 50)
            messaggio("Salva", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13, 50)
            messaggio("Impostazioni", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 14, 50)
            messaggio("Menu principale", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 15, 50)
            if GlobalVar.mouseVisibile:
                messaggio("Tasto destro / centrale: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 1, 50)
            else:
                messaggio("Esc / Q: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 1, 50)
            if carim:
                if dati[10] <= 0:
                    robosta = GlobalVar.robograf2b
                else:
                    robosta = GlobalVar.robograf1b
                carim = False

            # vita-status personaggio
            if dati[5] < 0:
                dati[5] = 0
            messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 13.5, GlobalVar.gsy // 18 * 13, 50)
            messaggio("Lv:  " + str(dati[4]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 13.5, GlobalVar.gsy // 18 * 14, 50)
            if dati[4] < 100:
                messaggio("Esp:  " + str(dati[127]) + " / " + str(esptot), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 14, 50)
            else:
                messaggio("Esp:  -- / --", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 14, 50)
            messaggio("Status alterati: ", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 13.5, GlobalVar.gsy // 18 * 15, 50)
            GlobalVar.schermo.blit(sfondostastart, (GlobalVar.gsx // 32 * 13.5, (GlobalVar.gsy // 18 * 16) + (GlobalVar.gpy // 8)))
            if dati[121]:
                GlobalVar.schermo.blit(avvelenatosta, (GlobalVar.gsx // 32 * 13.5, GlobalVar.gsy // 18 * 16))
            if dati[123] > 0:
                GlobalVar.schermo.blit(attaccopiusta, ((GlobalVar.gsx // 32 * 13.5) + (2 * GlobalVar.gpx // 4 * 3), GlobalVar.gsy // 18 * 16))
            if dati[124] > 0:
                GlobalVar.schermo.blit(difesapiusta, ((GlobalVar.gsx // 32 * 13.5) + (4 * GlobalVar.gpx // 4 * 3), GlobalVar.gsy // 18 * 16))
            GlobalVar.schermo.blit(perssta, (GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 2))

            if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
                # vita-status robo
                if dati[10] < 0:
                    dati[10] = 0
                messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23.5, GlobalVar.gsy // 18 * 13, 50)
                messaggio("Status alterati: ", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23.5, GlobalVar.gsy // 18 * 14, 50)
                GlobalVar.schermo.blit(sfondostastart, (GlobalVar.gsx // 32 * 23.5, (GlobalVar.gsy // 18 * 15) + (GlobalVar.gpy // 8)))
                if dati[122] > 0:
                    GlobalVar.schermo.blit(surriscaldatosta, (GlobalVar.gsx // 32 * 23.5, GlobalVar.gsy // 18 * 15))
                if dati[125] > 0:
                    GlobalVar.schermo.blit(velocitapiusta, ((GlobalVar.gsx // 32 * 23.5) + (2 * GlobalVar.gpx // 4 * 3), GlobalVar.gsy // 18 * 15))
                if dati[126] > 0:
                    GlobalVar.schermo.blit(efficienzapiusta, ((GlobalVar.gsx // 32 * 23.5) + (4 * GlobalVar.gpx // 4 * 3), GlobalVar.gsy // 18 * 15))
                GlobalVar.schermo.blit(robosta, (GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 2))

            if attacco != 0:
                risposta = True

            if faretraFrecceStart != 0:
                GlobalVar.schermo.blit(faretraFrecceStart, (GlobalVar.gsx // 32 * 21.5, GlobalVar.gsy // 18 * 2.5))
                messaggio("Frecce: " + str(dati[132]) + " / " + str(maxFrecce), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 21.5, GlobalVar.gsy // 18 * 6, 50)
            GlobalVar.schermo.blit(GlobalVar.sacchettoDenaroStart, (GlobalVar.gsx // 32 * 26.5, GlobalVar.gsy // 18 * 2.5))
            messaggio("Monete: " + str(dati[131]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 26.5, GlobalVar.gsy // 18 * 6, 50)

            GlobalVar.schermo.blit(puntatore, (xp, yp))
            if not risposta:
                pygame.display.update()
            else:
                GlobalVar.schermo.fill(GlobalVar.grigioscu)

        GlobalVar.clockMenu.tick(GlobalVar.fpsMenu)
    GlobalVar.canaleSoundCanzone.set_volume(GlobalVar.volumeCanzoni)
    return dati, inizio, attacco, caricaSalvataggio


def startBattaglia(dati, animaOggetto, x, y, npers, rx, ry, inizio, canzone):
    xp = GlobalVar.gpx * 1
    yp = GlobalVar.gpy * 13.8
    puntatore = GlobalVar.puntatore
    puntatorevecchio = GlobalVar.puntatorevecchio
    sconosciutoOggetto = pygame.transform.scale(GlobalVar.sconosciutoOggettoMenu, (GlobalVar.gpx * 4, GlobalVar.gpy * 4))
    sconosciutoOggettoIco = pygame.transform.scale(GlobalVar.sconosciutoOggettoIcoMenu, (GlobalVar.gpx, GlobalVar.gpy))

    schermo_temp = GlobalVar.schermo.copy()
    background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalVar.gsx, GlobalVar.gsy))
    dark = pygame.Surface((GlobalVar.gsx, GlobalVar.gsy), flags=pygame.SRCALPHA)
    dark.fill((0, 0, 0, 80))
    background.blit(dark, (0, 0))
    GlobalVar.schermo.blit(background, (0, 0))

    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

    attacco = 0
    disegnoOggetto = 0
    risposta = False
    voceMarcata = 1
    voceMarcataOggetto = voceMarcata
    primoFrame = True
    aggiornaSchermo = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    tastop = 0
    tastotempfps = 5

    difensivi = True
    offensivi = False
    sposta = False
    caricaSalvataggio = False

    oggetton = 1
    vettoreOggettiGraf = []
    vettoreOggettiIco = []
    while oggetton <= 10:
        if dati[oggetton + 30] >= 0:
            vettoreOggettiGraf.append(GlobalVar.vetImgOggettiStart[oggetton - 1])
            vettoreOggettiIco.append(GlobalVar.vetIcoOggettiMenu[oggetton - 1])
        else:
            vettoreOggettiGraf.append(sconosciutoOggetto)
            vettoreOggettiIco.append(sconosciutoOggettoIco)
        oggetton += 1

    GlobalVar.canaleSoundCanzone.set_volume(GlobalVar.volumeCanzoni / 2)
    while not risposta:
        if canzone and not GlobalVar.canaleSoundCanzone.get_busy():
            GlobalVar.canaleSoundCanzone.play(canzone)

        # rallenta per i 30 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        else:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        mouseInquadraFreccia = False
        suTornaIndietro = False
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVar.mouseVisibile:
            pygame.mouse.set_visible(True)
            GlobalVar.mouseVisibile = True
        if GlobalVar.mouseVisibile:
            if dati[0] >= GlobalVar.dictAvanzamentoStoria["trovatoMappaDiario"] and GlobalVar.gsy // 18 * 15.6 <= yMouse <= GlobalVar.gsy // 18 * 17 and 0 <= xMouse <= GlobalVar.gsx // 32 * 3.5:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                xp = 0
                yp = GlobalVar.gsy // 18 * 16.05
                voceMarcata = -1
            elif GlobalVar.gsy // 18 * 15.6 <= yMouse <= GlobalVar.gsy // 18 * 17 and GlobalVar.gsx // 32 * 3.5 <= xMouse <= GlobalVar.gsx // 32 * 6.8:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                xp = GlobalVar.gsx // 32 * 3.5
                yp = GlobalVar.gsy // 18 * 16.05
                voceMarcata = -2
            elif GlobalVar.gsy // 18 * 17 <= yMouse <= GlobalVar.gsy and GlobalVar.gsx // 32 * 0 <= xMouse <= GlobalVar.gsx // 32 * 7:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                suTornaIndietro = True
            elif difensivi:
                if GlobalVar.gsy // 18 * 14.8 <= yMouse <= GlobalVar.gsy // 18 * 15.3 and GlobalVar.gsx // 32 * 3 <= xMouse <= GlobalVar.gsx // 32 * 4:
                    mouseInquadraFreccia = True
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                elif GlobalVar.gsy // 18 * 13.8 <= yMouse <= GlobalVar.gsy // 18 * 14.8:
                    if GlobalVar.gsx // 32 * 1 <= xMouse <= GlobalVar.gsx // 32 * 2:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalVar.gsx // 32 * 1
                        yp = GlobalVar.gsy // 18 * 13.8
                    elif GlobalVar.gsx // 32 * 2 <= xMouse <= GlobalVar.gsx // 32 * 3:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalVar.gsx // 32 * 2
                        yp = GlobalVar.gsy // 18 * 13.8
                    elif GlobalVar.gsx // 32 * 3 <= xMouse <= GlobalVar.gsx // 32 * 4:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 3
                        xp = GlobalVar.gsx // 32 * 3
                        yp = GlobalVar.gsy // 18 * 13.8
                    elif GlobalVar.gsx // 32 * 4 <= xMouse <= GlobalVar.gsx // 32 * 5:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 4
                        xp = GlobalVar.gsx // 32 * 4
                        yp = GlobalVar.gsy // 18 * 13.8
                    elif GlobalVar.gsx // 32 * 5 <= xMouse <= GlobalVar.gsx // 32 * 6:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 5
                        xp = GlobalVar.gsx // 32 * 5
                        yp = GlobalVar.gsy // 18 * 13.8
                    else:
                        if not GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(True)
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            elif offensivi:
                if GlobalVar.gsy // 18 * 13.8 <= yMouse <= GlobalVar.gsy // 18 * 14.3 and GlobalVar.gsx // 32 * 3 <= xMouse <= GlobalVar.gsx // 32 * 4:
                    mouseInquadraFreccia = True
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                elif GlobalVar.gsy // 18 * 14.3 <= yMouse <= GlobalVar.gsy // 18 * 15.3:
                    if GlobalVar.gsx // 32 * 1 <= xMouse <= GlobalVar.gsx // 32 * 2:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalVar.gsx // 32 * 1
                        yp = GlobalVar.gsy // 18 * 14.3
                    elif GlobalVar.gsx // 32 * 2 <= xMouse <= GlobalVar.gsx // 32 * 3:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalVar.gsx // 32 * 2
                        yp = GlobalVar.gsy // 18 * 14.3
                    elif GlobalVar.gsx // 32 * 3 <= xMouse <= GlobalVar.gsx // 32 * 4:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 3
                        xp = GlobalVar.gsx // 32 * 3
                        yp = GlobalVar.gsy // 18 * 14.3
                    elif GlobalVar.gsx // 32 * 4 <= xMouse <= GlobalVar.gsx // 32 * 5:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 4
                        xp = GlobalVar.gsx // 32 * 4
                        yp = GlobalVar.gsy // 18 * 14.3
                    elif GlobalVar.gsx // 32 * 5 <= xMouse <= GlobalVar.gsx // 32 * 6:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 5
                        xp = GlobalVar.gsx // 32 * 5
                        yp = GlobalVar.gsy // 18 * 14.3
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
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato and voceMarcataVecchia == voceMarcata:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                tastop = event.key
                tastotempfps = 5
                if (event.key == pygame.K_q or event.key == pygame.K_ESCAPE) and not tastoTrovato:
                    tastoTrovato = True
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    risposta = True
                if event.key == pygame.K_a and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and ((destroMouse or centraleMouse) and not rotellaConCentralePremuto):
                tastoTrovato = True
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                risposta = True
            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and not GlobalVar.mouseBloccato and mouseInquadraFreccia:
                tastoTrovato = True
                tastop = "spazioOsinistroMouse"
                if difensivi:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = GlobalVar.gpy * 14.3
                    difensivi = False
                    offensivi = True
                elif offensivi:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = GlobalVar.gpy * 13.8
                    offensivi = False
                    difensivi = True
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and not GlobalVar.mouseBloccato and not mouseInquadraFreccia):
                tastoTrovato = True
                tastop = "spazioOsinistroMouse"
                if suTornaIndietro:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    risposta = True
                elif voceMarcata < 0:
                    if voceMarcata == -1:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                        GlobalVar.schermo.blit(puntatorevecchio, (xp, yp))
                        schermo_temp = GlobalVar.schermo.copy()
                        background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalVar.gsx, GlobalVar.gsy))
                        menuMappa(dati[0], False)
                        GlobalVar.schermo.blit(background, (0, 0))
                    elif voceMarcata == -2:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                        GlobalVar.schermo.blit(puntatorevecchio, (xp, yp))
                        schermo_temp = GlobalVar.schermo.copy()
                        background = schermo_temp.subsurface(pygame.Rect(0, 0, GlobalVar.gsx, GlobalVar.gsy))
                        inizio, risposta = chiediconferma(1)
                        if not inizio:
                            GlobalVar.schermo.blit(background, (0, 0))
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
                        if voceMarcata == 2 and dati[32] > 0 and (abs(x - rx) + abs(y - ry)) <= GlobalVar.gpx:
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
                        if voceMarcata == 5 and dati[35] > 0 and (abs(x - rx) + abs(y - ry)) <= GlobalVar.gpx:
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
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
            elif GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and GlobalVar.mouseBloccato:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
            if (sinistroMouse or centraleMouse or destroMouse) and not rotellaConCentralePremuto and not GlobalVar.mouseVisibile:
                pygame.mouse.set_visible(True)
                GlobalVar.mouseVisibile = True

            if tastop != 0:
                aggiornaSchermo = True

            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0
            if event.type == pygame.MOUSEBUTTONUP:
                tastop = 0

        if not caricaSalvataggio and (aggiornaSchermo or primoMovimento or tastop == "spazioOsinistroMouse" or ((tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d or tastop == pygame.K_w) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata):
            primoFrame = False
            aggiornaSchermo = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if voceMarcata < 0:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    offensivi = True
                    difensivi = False
                    if voceMarcata == -1:
                        xp = GlobalVar.gpx * 1
                        yp = GlobalVar.gpy * 14.3
                        voceMarcata = 1
                    elif voceMarcata == -2:
                        xp = GlobalVar.gpx * 3
                        yp = GlobalVar.gpy * 14.3
                        voceMarcata = 3
                elif offensivi:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = GlobalVar.gpy * 13.8
                    offensivi = False
                    difensivi = True
            if tastop == pygame.K_a:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if voceMarcata < 0:
                    if voceMarcata == -2 and dati[0] >= GlobalVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
                        voceMarcata += 1
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        xp = 0
                elif voceMarcata != 1:
                    voceMarcata -= 1
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    xp = xp - GlobalVar.gpx
                else:
                    voceMarcata += 4
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    xp = GlobalVar.gpx * 5
            if tastop == pygame.K_s:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if difensivi:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    yp = GlobalVar.gpy * 14.3
                    difensivi = False
                    offensivi = True
                elif voceMarcata >= 0:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    if voceMarcata < 3 and dati[0] >= GlobalVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
                        xp = 0
                        yp = GlobalVar.gsy // 18 * 16.05
                        voceMarcata = -1
                    else:
                        xp = GlobalVar.gsx // 32 * 3.5
                        yp = GlobalVar.gsy // 18 * 16.05
                        voceMarcata = -2
            if tastop == pygame.K_d:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if voceMarcata < 0:
                    if voceMarcata == -1:
                        voceMarcata -= 1
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        xp = GlobalVar.gsx // 32 * 3.5
                elif voceMarcata != 5:
                    voceMarcata += 1
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    xp = xp + GlobalVar.gpx
                else:
                    voceMarcata -= 4
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    xp = GlobalVar.gpx * 1

            if voceMarcata >= 0:
                voceMarcataOggetto = voceMarcata

            GlobalVar.schermo.blit(GlobalVar.sfondoStartBattaglia, (0, GlobalVar.gsy // 18 * 8))
            if dati[0] >= GlobalVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
                messaggio("Mappa", GlobalVar.grigiochi, int(GlobalVar.gpx * 0.7), int(GlobalVar.gpy * 16.05), 45)
            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscu, (int(GlobalVar.gpx * 3.5), int(GlobalVar.gpy * 15.8)), (int(GlobalVar.gpx * 3.5), int(GlobalVar.gpy * 16.8)), 2)
            messaggio("Esci", GlobalVar.grigiochi, int(GlobalVar.gpx * 4.2), int(GlobalVar.gpy * 16.05), 45)
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
            GlobalVar.schermo.blit(vettoreOggettiGraf[disegnoOggetto], (GlobalVar.gpx // 2, GlobalVar.gpy * 9.7))
            if dati[disegnoOggetto + 31] <= 0:
                if voceMarcata < 0:
                    GlobalVar.schermo.blit(puntatore, (xp, yp))
                else:
                    GlobalVar.schermo.blit(GlobalVar.puntatOut, (xp, yp))
                qta = 0
            elif (disegnoOggetto == 1 or disegnoOggetto == 4) and abs(x - rx) + abs(y - ry) > GlobalVar.gpx:
                if voceMarcata < 0:
                    GlobalVar.schermo.blit(puntatore, (xp, yp))
                else:
                    GlobalVar.schermo.blit(GlobalVar.puntatOut, (xp, yp))
                qta = dati[disegnoOggetto + 31]
            else:
                if voceMarcata < 0:
                    GlobalVar.schermo.blit(puntatore, (xp, yp))
                else:
                    GlobalVar.schermo.blit(GlobalVar.puntatIn, (xp, yp))
                qta = dati[disegnoOggetto + 31]
            messaggio("x%i" % qta, GlobalVar.grigiochi, (GlobalVar.gpx * 4) + (GlobalVar.gpx // 2), GlobalVar.gpy * 11.2, 80)
            disegnati = 0
            i = 0
            while i < 10:
                if difensivi and (i == 0 or i == 1 or i == 2 or i == 3 or i == 4):
                    GlobalVar.schermo.blit(vettoreOggettiIco[i], (GlobalVar.gpx * (disegnati + 1), GlobalVar.gpy * 13.8))
                    disegnati += 1
                if offensivi and (i == 5 or i == 6 or i == 7 or i == 8 or i == 9):
                    GlobalVar.schermo.blit(vettoreOggettiIco[i], (GlobalVar.gpx * (disegnati + 1), (GlobalVar.gpy * 13.8) + (GlobalVar.gpy // 2)))
                    disegnati += 1
                i += 1
            if difensivi:
                if voceMarcata == 1 or voceMarcataOggetto == 1:
                    if dati[31] >= 0:
                        messaggio("Pozione", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                    else:
                        messaggio("???", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                if voceMarcata == 2 or voceMarcataOggetto == 2:
                    if dati[32] >= 0:
                        messaggio("Alimentaz. 100gr", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                    else:
                        messaggio("???", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                if voceMarcata == 3 or voceMarcataOggetto == 3:
                    if dati[33] >= 0:
                        messaggio("Medicina", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                    else:
                        messaggio("???", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                if voceMarcata == 4 or voceMarcataOggetto == 4:
                    if dati[34] >= 0:
                        messaggio("Super pozione", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                    else:
                        messaggio("???", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                if voceMarcata == 5 or voceMarcataOggetto == 5:
                    if dati[35] >= 0:
                        messaggio("Alimentaz. 250gr", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                    else:
                        messaggio("???", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                GlobalVar.schermo.blit(GlobalVar.scorriGiu, (GlobalVar.gpx * 3, GlobalVar.gpy * 14.8))
            if offensivi:
                if voceMarcata == 1 or voceMarcataOggetto == 1:
                    if dati[36] >= 0:
                        messaggio("Bomba", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                    else:
                        messaggio("???", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                if voceMarcata == 2 or voceMarcataOggetto == 2:
                    if dati[37] >= 0:
                        messaggio("Bomba velenosa", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                    else:
                        messaggio("???", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                if voceMarcata == 3 or voceMarcataOggetto == 3:
                    if dati[38] >= 0:
                        messaggio("Esca", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                    else:
                        messaggio("???", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                if voceMarcata == 4 or voceMarcataOggetto == 4:
                    if dati[39] >= 0:
                        messaggio("Bomba appiccicosa", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                    else:
                        messaggio("???", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                if voceMarcata == 5 or voceMarcataOggetto == 5:
                    if dati[40] >= 0:
                        messaggio("Bomba potenziata", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                    else:
                        messaggio("???", GlobalVar.grigiochi, GlobalVar.gpx // 3, int(GlobalVar.gpy * 8.9), 55)
                GlobalVar.schermo.blit(GlobalVar.scorriSu, (GlobalVar.gpx * 3, GlobalVar.gpy * 13.3))

            # vita-status rallo
            lungvitatot = int(((GlobalVar.gpx * pvtot) / float(4)) // 5)
            lungvita = (lungvitatot * dati[5]) // pvtot
            if lungvita < 0:
                lungvita = 0
            indvitapers = pygame.transform.smoothscale(GlobalVar.indvita, (lungvitatot, GlobalVar.gpy // 4))
            fineindvitapers = pygame.transform.smoothscale(GlobalVar.fineindvita, (GlobalVar.gpx // 12, GlobalVar.gpy // 4))
            vitaral = pygame.transform.smoothscale(GlobalVar.vitapersonaggio, (lungvita, GlobalVar.gpy // 4))
            GlobalVar.schermo.blit(GlobalVar.sfondoRallo, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 17))
            GlobalVar.schermo.blit(indvitapers, (GlobalVar.gsx // 32 * 1, (GlobalVar.gsy // 18 * 17) + (GlobalVar.gpy // 4 * 3)))
            GlobalVar.schermo.blit(fineindvitapers, ((GlobalVar.gsx // 32 * 1) + lungvitatot, (GlobalVar.gsy // 18 * 17) + (GlobalVar.gpy // 4 * 3)))
            GlobalVar.schermo.blit(vitaral, (GlobalVar.gsx // 32 * 1, (GlobalVar.gsy // 18 * 17) + (GlobalVar.gpy // 4 * 3)))
            GlobalVar.schermo.blit(GlobalVar.perss, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 17))
            GlobalVar.schermo.blit(GlobalVar.perssb, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 17))
            GlobalVar.schermo.blit(GlobalVar.imgNumFrecce, (int(GlobalVar.gsx // 32 * 1.2), GlobalVar.gsy // 18 * 17))
            messaggio(" x" + str(dati[132]), GlobalVar.grigiochi, int(GlobalVar.gsx // 32 * 1.8), int(GlobalVar.gsy // 18 * 17.2), 40)
            if dati[121]:
                GlobalVar.schermo.blit(GlobalVar.avvelenato, (GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 17))
            if dati[123] > 0:
                GlobalVar.schermo.blit(GlobalVar.attaccopiu, (GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 17))
            if dati[124] > 0:
                GlobalVar.schermo.blit(GlobalVar.difesapiu, (GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 17))

            if not risposta:
                pygame.display.update()

        GlobalVar.clockMenu.tick(GlobalVar.fpsMenu)
    GlobalVar.canaleSoundCanzone.set_volume(GlobalVar.volumeCanzoni)
    return dati, attacco, sposta, animaOggetto, npers, caricaSalvataggio, inizio


def menuMercante(dati, canzone):
    puntatore = GlobalVar.puntatore
    puntatorevecchio = GlobalVar.puntatorevecchio
    sconosciutoOggetto = pygame.transform.scale(GlobalVar.sconosciutoOggettoMenu, (GlobalVar.gpx * 10, GlobalVar.gpy * 10))
    xp = GlobalVar.gsx // 32 * 10.5
    yp = GlobalVar.gsy // 18 * 6.1
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
    primoFrame = True
    aggiornaSchermo = False
    mouseSinistroPremuto = False
    aggiornaInterfacciaPerMouse = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    maxFrecce = 1
    if dati[133] == 1:
        maxFrecce = 5
    elif dati[133] == 2:
        maxFrecce = 20
    elif dati[133] == 3:
        maxFrecce = 60

    tastop = 0
    tastotempfps = 5

    imgOggetti = []
    i = 1
    while i <= 10:
        if (i == 1 and dati[0] > -1) or (i == 2 and dati[0] > -1) or (i == 3 and dati[0] > -1) or (i == 4 and dati[0] > -1) or (i == 5 and dati[0] > -1) or (i == 6 and dati[0] > -1) or (i == 7 and dati[0] > -1) or (i == 8 and dati[0] > -1) or (i == 9 and dati[0] > -1) or (i == 10 and dati[0] > -1):
            imgOggetti.append(GlobalVar.vetImgOggettiMercante[i - 1])
        else:
            imgOggetti.append(sconosciutoOggetto)
        i += 1

    GlobalVar.canaleSoundCanzone.set_volume(GlobalVar.volumeCanzoni / 2)
    while not risposta:
        if canzone and not GlobalVar.canaleSoundCanzone.get_busy():
            GlobalVar.canaleSoundCanzone.play(canzone)

        # rallenta per i 30 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        else:
            tastotempfps = 2

        oggettonVecchio = oggetton
        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        mouseInquadraFrecciaSu = False
        mouseInquadraFrecciaGiu = False
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
            elif voceMarcata == 0:
                if GlobalVar.gsx // 32 * 10.5 <= xMouse <= GlobalVar.gsx // 32 * 21.5:
                    if GlobalVar.gsy // 18 * 6 <= yMouse <= GlobalVar.gsy // 18 * 6.8:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 0
                        xp = GlobalVar.gsx // 32 * 10.5
                        yp = GlobalVar.gsy // 18 * 6.1
                    elif GlobalVar.gsy // 18 * 6.8 <= yMouse <= GlobalVar.gsy // 18 * 7.7:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 1
                        xp = GlobalVar.gsx // 32 * 10.5
                        yp = GlobalVar.gsy // 18 * 7
                    elif GlobalVar.gsy // 18 * 7.7 <= yMouse <= GlobalVar.gsy // 18 * 8.6:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 2
                        xp = GlobalVar.gsx // 32 * 10.5
                        yp = GlobalVar.gsy // 18 * 7.9
                    elif GlobalVar.gsy // 18 * 8.6 <= yMouse <= GlobalVar.gsy // 18 * 9.5:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 3
                        xp = GlobalVar.gsx // 32 * 10.5
                        yp = GlobalVar.gsy // 18 * 8.8
                    elif GlobalVar.gsy // 18 * 9.5 <= yMouse <= GlobalVar.gsy // 18 * 10.4:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 4
                        xp = GlobalVar.gsx // 32 * 10.5
                        yp = GlobalVar.gsy // 18 * 9.7
                    elif GlobalVar.gsy // 18 * 10.4 <= yMouse <= GlobalVar.gsy // 18 * 11.3:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 5
                        xp = GlobalVar.gsx // 32 * 10.5
                        yp = GlobalVar.gsy // 18 * 10.6
                    elif GlobalVar.gsy // 18 * 11.3 <= yMouse <= GlobalVar.gsy // 18 * 12.2:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 6
                        xp = GlobalVar.gsx // 32 * 10.5
                        yp = GlobalVar.gsy // 18 * 11.5
                    elif GlobalVar.gsy // 18 * 12.2 <= yMouse <= GlobalVar.gsy // 18 * 13.1:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 7
                        xp = GlobalVar.gsx // 32 * 10.5
                        yp = GlobalVar.gsy // 18 * 12.4
                    elif GlobalVar.gsy // 18 * 13.1 <= yMouse <= GlobalVar.gsy // 18 * 14:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 8
                        xp = GlobalVar.gsx // 32 * 10.5
                        yp = GlobalVar.gsy // 18 * 13.3
                    elif GlobalVar.gsy // 18 * 14 <= yMouse <= GlobalVar.gsy // 18 * 14.9:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 9
                        xp = GlobalVar.gsx // 32 * 10.5
                        yp = GlobalVar.gsy // 18 * 14.2
                    elif GlobalVar.gsy // 18 * 14.9 <= yMouse <= GlobalVar.gsy // 18 * 15.8:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 10
                        xp = GlobalVar.gsx // 32 * 10.5
                        yp = GlobalVar.gsy // 18 * 15.1
                    elif GlobalVar.gsy // 18 * 15.8 <= yMouse <= GlobalVar.gsy // 18 * 16.7:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 11
                        xp = GlobalVar.gsx // 32 * 10.5
                        yp = GlobalVar.gsy // 18 * 16
                    else:
                        if not GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(True)
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            else:
                if GlobalVar.gsy // 18 * 4.3 <= yMouse <= GlobalVar.gsy // 18 * 4.8 and GlobalVar.gsx // 32 * 8.5 <= xMouse <= GlobalVar.gsx // 32 * 9.5:
                    mouseInquadraFrecciaSu = True
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                elif GlobalVar.gsy // 18 * 4.8 <= yMouse <= GlobalVar.gsy // 18 * 5.3 and GlobalVar.gsx // 32 * 8.5 <= xMouse <= GlobalVar.gsx // 32 * 9.5:
                    mouseInquadraFrecciaGiu = True
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                elif GlobalVar.gsy // 18 * 6.6 <= yMouse <= GlobalVar.gsy // 18 * 7.6:
                    if GlobalVar.gsx // 32 * 1.3 <= xMouse <= GlobalVar.gsx // 32 * 5.3:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalVar.gsx // 32 * 1.3
                        yp = GlobalVar.gsy // 18 * 6.9
                    elif GlobalVar.gsx // 32 * 5.3 <= xMouse <= GlobalVar.gsx // 32 * 9.2:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalVar.gsx // 32 * 5.3
                        yp = GlobalVar.gsy // 18 * 6.9
                    else:
                        if not GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(True)
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            if (oggettonVecchio != oggetton or voceMarcataVecchia != voceMarcata) and not primoFrame:
                inventarioPieno = False
                moneteInsufficienti = False
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)

        buttonUp = False
        primoMovimento = False
        tastoTrovato = False
        for event in pygame.event.get():
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
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato and oggettonVecchio == oggetton and voceMarcataVecchia == voceMarcata:
                if GlobalVar.mouseVisibile:
                    aggiornaInterfacciaPerMouse = True
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                tastop = event.key
                tastotempfps = 5
                if event.key == pygame.K_q and not tastoTrovato:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    numeroOggettiAcquistati = 1
                    moneteInsufficienti = False
                    inventarioPieno = False
                    tastoTrovato = True
                    voceMarcata = 0
                    if confermaOggettoDaAcquistare != 0:
                        xp = GlobalVar.gsx // 32 * 10.5
                        if confermaOggettoDaAcquistare == -1:
                            yp = GlobalVar.gsy // 18 * 6.1
                        if confermaOggettoDaAcquistare == 1:
                            yp = GlobalVar.gsy // 18 * 7
                        if confermaOggettoDaAcquistare == 2:
                            yp = GlobalVar.gsy // 18 * 7.9
                        if confermaOggettoDaAcquistare == 3:
                            yp = GlobalVar.gsy // 18 * 8.8
                        if confermaOggettoDaAcquistare == 4:
                            yp = GlobalVar.gsy // 18 * 9.7
                        if confermaOggettoDaAcquistare == 5:
                            yp = GlobalVar.gsy // 18 * 10.6
                        if confermaOggettoDaAcquistare == 6:
                            yp = GlobalVar.gsy // 18 * 11.5
                        if confermaOggettoDaAcquistare == 7:
                            yp = GlobalVar.gsy // 18 * 12.4
                        if confermaOggettoDaAcquistare == 8:
                            yp = GlobalVar.gsy // 18 * 13.3
                        if confermaOggettoDaAcquistare == 9:
                            yp = GlobalVar.gsy // 18 * 14.2
                        if confermaOggettoDaAcquistare == 10:
                            yp = GlobalVar.gsy // 18 * 15.1
                        if confermaOggettoDaAcquistare == 11:
                            yp = GlobalVar.gsy // 18 * 16
                        confermaOggettoDaAcquistare = 0
                    else:
                        risposta = True
                if event.key == pygame.K_s and not tastoTrovato:
                    moneteInsufficienti = False
                    inventarioPieno = False
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    moneteInsufficienti = False
                    inventarioPieno = False
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and voceMarcata != 0 and not tastoTrovato:
                    moneteInsufficienti = False
                    inventarioPieno = False
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and voceMarcata != 0 and not tastoTrovato:
                    moneteInsufficienti = False
                    inventarioPieno = False
                    primoMovimento = True
                    tastoTrovato = True
            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse and not rotellaConCentralePremuto:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                numeroOggettiAcquistati = 1
                moneteInsufficienti = False
                inventarioPieno = False
                tastoTrovato = True
                voceMarcata = 0
                if confermaOggettoDaAcquistare != 0:
                    xp = GlobalVar.gsx // 32 * 10.5
                    if confermaOggettoDaAcquistare == -1:
                        yp = GlobalVar.gsy // 18 * 6.1
                    if confermaOggettoDaAcquistare == 1:
                        yp = GlobalVar.gsy // 18 * 7
                    if confermaOggettoDaAcquistare == 2:
                        yp = GlobalVar.gsy // 18 * 7.9
                    if confermaOggettoDaAcquistare == 3:
                        yp = GlobalVar.gsy // 18 * 8.8
                    if confermaOggettoDaAcquistare == 4:
                        yp = GlobalVar.gsy // 18 * 9.7
                    if confermaOggettoDaAcquistare == 5:
                        yp = GlobalVar.gsy // 18 * 10.6
                    if confermaOggettoDaAcquistare == 6:
                        yp = GlobalVar.gsy // 18 * 11.5
                    if confermaOggettoDaAcquistare == 7:
                        yp = GlobalVar.gsy // 18 * 12.4
                    if confermaOggettoDaAcquistare == 8:
                        yp = GlobalVar.gsy // 18 * 13.3
                    if confermaOggettoDaAcquistare == 9:
                        yp = GlobalVar.gsy // 18 * 14.2
                    if confermaOggettoDaAcquistare == 10:
                        yp = GlobalVar.gsy // 18 * 15.1
                    if confermaOggettoDaAcquistare == 11:
                        yp = GlobalVar.gsy // 18 * 16
                    confermaOggettoDaAcquistare = 0
                else:
                    risposta = True
            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and not GlobalVar.mouseBloccato and (mouseInquadraFrecciaSu or mouseInquadraFrecciaGiu):
                tastoTrovato = True
                tastotempfps = 5
                primoMovimento = True
                tastop = "spazioOsinistroMouse"
                mouseSinistroPremuto = True
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and not GlobalVar.mouseBloccato and not (mouseInquadraFrecciaSu or mouseInquadraFrecciaGiu)):
                moneteInsufficienti = False
                inventarioPieno = False
                tastotempfps = 5
                primoMovimento = True
                tastoTrovato = True
                procediAllAcquisto = True
                tastop = "spazioOsinistroMouse"

                # confermaOggettoDaAcquistare?
                if voceMarcata == 1 and not (event.type == pygame.MOUSEBUTTONDOWN and suTornaIndietro):
                    if 0 <= oggetton <= 10 and GlobalVar.costoOggetti[oggetton] * numeroOggettiAcquistati <= dati[131]:
                        GlobalVar.canaleSoundInterazioni.play(GlobalVar.rumoreAcquisto)
                        dati[131] -= GlobalVar.costoOggetti[oggetton] * numeroOggettiAcquistati
                        voceMarcata = 0
                        xp = GlobalVar.gsx // 32 * 10.5
                        # freccia
                        if confermaOggettoDaAcquistare == -1:
                            dati[132] += numeroOggettiAcquistati
                            yp = GlobalVar.gsy // 18 * 6.1
                        # pozione
                        if confermaOggettoDaAcquistare == 1:
                            dati[31] += numeroOggettiAcquistati
                            yp = GlobalVar.gsy // 18 * 7
                        # carica batt
                        if confermaOggettoDaAcquistare == 2:
                            dati[32] += numeroOggettiAcquistati
                            yp = GlobalVar.gsy // 18 * 7.9
                        # antidoto
                        if confermaOggettoDaAcquistare == 3:
                            dati[33] += numeroOggettiAcquistati
                            yp = GlobalVar.gsy // 18 * 8.8
                        # super pozione
                        if confermaOggettoDaAcquistare == 4:
                            dati[34] += numeroOggettiAcquistati
                            yp = GlobalVar.gsy // 18 * 9.7
                        # carica migliorato
                        if confermaOggettoDaAcquistare == 5:
                            dati[35] += numeroOggettiAcquistati
                            yp = GlobalVar.gsy // 18 * 10.6
                        # bomba
                        if confermaOggettoDaAcquistare == 6:
                            dati[36] += numeroOggettiAcquistati
                            yp = GlobalVar.gsy // 18 * 11.5
                        # bomba veleno
                        if confermaOggettoDaAcquistare == 7:
                            dati[37] += numeroOggettiAcquistati
                            yp = GlobalVar.gsy // 18 * 12.4
                        # esca
                        if confermaOggettoDaAcquistare == 8:
                            dati[38] += numeroOggettiAcquistati
                            yp = GlobalVar.gsy // 18 * 13.3
                        # bomba appiccicosa
                        if confermaOggettoDaAcquistare == 9:
                            dati[39] += numeroOggettiAcquistati
                            yp = GlobalVar.gsy // 18 * 14.2
                        # bomba potenziata
                        if confermaOggettoDaAcquistare == 10:
                            dati[40] += numeroOggettiAcquistati
                            yp = GlobalVar.gsy // 18 * 15.1
                        confermaOggettoDaAcquistare = 0
                        procediAllAcquisto = False
                    elif oggetton == 11:
                        if dati[133] == 0 and GlobalVar.costoOggetti[oggetton] * numeroOggettiAcquistati <= dati[131]:
                            GlobalVar.canaleSoundInterazioni.play(GlobalVar.rumoreAcquisto)
                            dati[131] -= GlobalVar.costoOggetti[oggetton] * numeroOggettiAcquistati
                            voceMarcata = 0
                            xp = GlobalVar.gsx // 32 * 10.5
                            # faretra
                            if confermaOggettoDaAcquistare == 10:
                                dati[40] += numeroOggettiAcquistati
                                yp = GlobalVar.gsy // 18 * 15.1
                            confermaOggettoDaAcquistare = 0
                            procediAllAcquisto = False
                        elif dati[133] == 1 and GlobalVar.costoOggetti[oggetton + 1] * numeroOggettiAcquistati <= dati[131]:
                            GlobalVar.canaleSoundInterazioni.play(GlobalVar.rumoreAcquisto)
                            dati[131] -= GlobalVar.costoOggetti[oggetton + 1] * numeroOggettiAcquistati
                            voceMarcata = 0
                            xp = GlobalVar.gsx // 32 * 10.5
                            # faretra
                            if confermaOggettoDaAcquistare == 10:
                                dati[40] += numeroOggettiAcquistati
                                yp = GlobalVar.gsy // 18 * 15.1
                            confermaOggettoDaAcquistare = 0
                            procediAllAcquisto = False
                        elif dati[133] == 2 and GlobalVar.costoOggetti[oggetton + 2] * numeroOggettiAcquistati <= dati[131]:
                            GlobalVar.canaleSoundInterazioni.play(GlobalVar.rumoreAcquisto)
                            dati[131] -= GlobalVar.costoOggetti[oggetton + 2] * numeroOggettiAcquistati
                            voceMarcata = 0
                            xp = GlobalVar.gsx // 32 * 10.5
                            # faretra
                            if confermaOggettoDaAcquistare == 10:
                                dati[40] += numeroOggettiAcquistati
                                yp = GlobalVar.gsy // 18 * 15.1
                            confermaOggettoDaAcquistare = 0
                            procediAllAcquisto = False
                        else:
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                            moneteInsufficienti = True
                            procediAllAcquisto = False
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                        moneteInsufficienti = True
                        procediAllAcquisto = False
                elif voceMarcata == 2 or (voceMarcata == 1 and event.type == pygame.MOUSEBUTTONDOWN and suTornaIndietro):
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    voceMarcata = 0
                    numeroOggettiAcquistati = 1
                    moneteInsufficienti = False
                    inventarioPieno = False
                    xp = GlobalVar.gsx // 32 * 10.5
                    if confermaOggettoDaAcquistare == -1:
                        yp = GlobalVar.gsy // 18 * 6.1
                    if confermaOggettoDaAcquistare == 1:
                        yp = GlobalVar.gsy // 18 * 7
                    if confermaOggettoDaAcquistare == 2:
                        yp = GlobalVar.gsy // 18 * 7.9
                    if confermaOggettoDaAcquistare == 3:
                        yp = GlobalVar.gsy // 18 * 8.8
                    if confermaOggettoDaAcquistare == 4:
                        yp = GlobalVar.gsy // 18 * 9.7
                    if confermaOggettoDaAcquistare == 5:
                        yp = GlobalVar.gsy // 18 * 10.6
                    if confermaOggettoDaAcquistare == 6:
                        yp = GlobalVar.gsy // 18 * 11.5
                    if confermaOggettoDaAcquistare == 7:
                        yp = GlobalVar.gsy // 18 * 12.4
                    if confermaOggettoDaAcquistare == 8:
                        yp = GlobalVar.gsy // 18 * 13.3
                    if confermaOggettoDaAcquistare == 9:
                        yp = GlobalVar.gsy // 18 * 14.2
                    if confermaOggettoDaAcquistare == 10:
                        yp = GlobalVar.gsy // 18 * 15.1
                    if confermaOggettoDaAcquistare == 11:
                        yp = GlobalVar.gsy // 18 * 16
                    confermaOggettoDaAcquistare = 0
                    procediAllAcquisto = False
                elif voceMarcata == 0 and event.type == pygame.MOUSEBUTTONDOWN and suTornaIndietro:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
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
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                                confermaOggettoDaAcquistare = 1
                                usauno = True
                            else:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                        if oggetton == 2:
                            if imgOggetti[1] != sconosciutoOggetto:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                                confermaOggettoDaAcquistare = 2
                                usauno = True
                            else:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                        if oggetton == 3:
                            if imgOggetti[2] != sconosciutoOggetto:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                                confermaOggettoDaAcquistare = 3
                                usauno = True
                            else:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                        if oggetton == 4:
                            if imgOggetti[3] != sconosciutoOggetto:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                                confermaOggettoDaAcquistare = 4
                                usauno = True
                            else:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                        if oggetton == 5:
                            if imgOggetti[4] != sconosciutoOggetto:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                                confermaOggettoDaAcquistare = 5
                                usauno = True
                            else:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                        if oggetton == 6:
                            if imgOggetti[5] != sconosciutoOggetto:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                                confermaOggettoDaAcquistare = 6
                                usauno = True
                            else:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                        if oggetton == 7:
                            if imgOggetti[6] != sconosciutoOggetto:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                                confermaOggettoDaAcquistare = 7
                                usauno = True
                            else:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                        if oggetton == 8:
                            if imgOggetti[7] != sconosciutoOggetto:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                                confermaOggettoDaAcquistare = 8
                                usauno = True
                            else:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                        if oggetton == 9:
                            if imgOggetti[8] != sconosciutoOggetto:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                                confermaOggettoDaAcquistare = 9
                                usauno = True
                            else:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                        if oggetton == 10:
                            if imgOggetti[9] != sconosciutoOggetto:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                                confermaOggettoDaAcquistare = 10
                                usauno = True
                            else:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                    elif oggetton == 0 and dati[132] < maxFrecce:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                        confermaOggettoDaAcquistare = -1
                        usauno = True
                    elif oggetton == 11 and dati[133] != 3:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                        confermaOggettoDaAcquistare = 11
                        usauno = True
                    else:
                        inventarioPieno = True
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
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
                mouseSinistroPremuto = False
                tastop = 0
                buttonUp = True

        if aggiornaSchermo or primoMovimento or buttonUp or tastop == pygame.K_q or ((tastop == "spazioOsinistroMouse" or tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame or oggettonVecchio != oggetton or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerMouse:
            aggiornaInterfacciaPerMouse = False
            aggiornaSchermo = False
            primoFrame = False
            if not primoMovimento and (tastop == "spazioOsinistroMouse" or tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if voceMarcata == 0:
                    if oggetton != 0:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        oggetton = oggetton - 1
                        yp = yp - GlobalVar.gsy // 18 * 0.9
                    elif oggetton == 0:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        yp = GlobalVar.gsy // 18 * 16
                        oggetton = 11
                elif voceMarcata != 0:
                    if oggetton != 11:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        numOggettiPosseduti = dati[30 + oggetton]
                        if numOggettiPosseduti < 0:
                            numOggettiPosseduti = 0
                        if 1 <= oggetton <= 10 and numeroOggettiAcquistati + numOggettiPosseduti >= 99:
                            numeroOggettiAcquistati = 1
                        elif oggetton == 0 and numeroOggettiAcquistati + dati[132] >= maxFrecce:
                            numeroOggettiAcquistati = 1
                        else:
                            numeroOggettiAcquistati += 1
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                        numeroOggettiAcquistati = 1
            if tastop == pygame.K_a and voceMarcata != 0:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if voceMarcata == 2:
                    voceMarcata -= 1
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    xp = xp - GlobalVar.gsx // 32 * 4
            if tastop == pygame.K_s:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if voceMarcata == 0:
                    if oggetton != 11:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        oggetton = oggetton + 1
                        yp = yp + GlobalVar.gsy // 18 * 0.9
                    elif oggetton == 11:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        yp = GlobalVar.gsy // 18 * 6.1
                        oggetton = 0
                elif voceMarcata != 0:
                    if oggetton != 11:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                        numOggettiPosseduti = dati[30 + oggetton]
                        if numOggettiPosseduti < 0:
                            numOggettiPosseduti = 0
                        if 1 <= oggetton <= 10 and numeroOggettiAcquistati == 1:
                            numeroOggettiAcquistati = 99 - numOggettiPosseduti
                        elif oggetton == 0 and numeroOggettiAcquistati == 1:
                            numeroOggettiAcquistati = maxFrecce - dati[132]
                        else:
                            numeroOggettiAcquistati -= 1
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                        numeroOggettiAcquistati = 1
            if tastop == pygame.K_d and voceMarcata != 0:
                if GlobalVar.mouseVisibile:
                    pygame.mouse.set_visible(False)
                    GlobalVar.mouseVisibile = False
                if voceMarcata == 1:
                    voceMarcata += 1
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                    xp = xp + GlobalVar.gsx // 32 * 4
            if mouseSinistroPremuto and (mouseInquadraFrecciaSu or mouseInquadraFrecciaGiu):
                if mouseInquadraFrecciaSu:
                    if voceMarcata != 0:
                        if oggetton != 11:
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                            numOggettiPosseduti = dati[30 + oggetton]
                            if numOggettiPosseduti < 0:
                                numOggettiPosseduti = 0
                            if 1 <= oggetton <= 10 and numeroOggettiAcquistati + numOggettiPosseduti >= 99:
                                numeroOggettiAcquistati = 1
                            elif oggetton == 0 and numeroOggettiAcquistati + dati[132] >= maxFrecce:
                                numeroOggettiAcquistati = 1
                            else:
                                numeroOggettiAcquistati += 1
                        else:
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                            numeroOggettiAcquistati = 1
                elif mouseInquadraFrecciaGiu:
                    if voceMarcata != 0:
                        if oggetton != 11:
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostapun)
                            numOggettiPosseduti = dati[30 + oggetton]
                            if numOggettiPosseduti < 0:
                                numOggettiPosseduti = 0
                            if 1 <= oggetton <= 10 and numeroOggettiAcquistati == 1:
                                numeroOggettiAcquistati = 99 - numOggettiPosseduti
                            elif oggetton == 0 and numeroOggettiAcquistati == 1:
                                numeroOggettiAcquistati = maxFrecce - dati[132]
                            else:
                                numeroOggettiAcquistati -= 1
                        else:
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                            numeroOggettiAcquistati = 1

            maxFrecce = 1
            if dati[133] == 1:
                maxFrecce = 5
            elif dati[133] == 2:
                maxFrecce = 20
            elif dati[133] == 3:
                maxFrecce = 60

            GlobalVar.schermo.fill(GlobalVar.grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 13.5))
            GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoSinistra, (GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 4))
            GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoAltoDestra, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 4))
            GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoBassoDestra, (GlobalVar.gsx // 32 * 20.5, GlobalVar.gsy // 18 * 16.5))
            GlobalVar.schermo.blit(GlobalVar.sfondoTriangolinoBassoSinistra, (GlobalVar.gsx // 32 * 10.5, GlobalVar.gsy // 18 * 16.5))

            GlobalVar.schermo.blit(GlobalVar.sacchettoDenaroMercante, (GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 14))
            messaggio("Monete: " + str(dati[131]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 15.8, 50)

            GlobalVar.schermo.blit(GlobalVar.mercanteMenu, (GlobalVar.gsx // 32 * (-1), GlobalVar.gsy // 18 * 8))
            GlobalVar.schermo.blit(GlobalVar.sfondoDialogoMercante, (GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 4))
            if moneteInsufficienti:
                messaggio("Non hai abbastanza monete!", GlobalVar.rosso, GlobalVar.gsx // 32 * 2.1, GlobalVar.gsy // 18 * 6.1, 40)
            if inventarioPieno:
                messaggio("Non puoi prenderne altre...", GlobalVar.rosso, GlobalVar.gsx // 32 * 2.4, GlobalVar.gsy // 18 * 5.3, 40)
            if confermaOggettoDaAcquistare == 0:
                messaggio("Prendi quello che ti serve", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4.5, 50)
            else:
                messaggio("Quante te ne servono?", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4.5, 50)

            if GlobalVar.mouseVisibile:
                messaggio("Tasto destro: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 1, 50)
            else:
                messaggio("Q: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 1, 50)
            if 1 <= oggetton <= 10:
                GlobalVar.schermo.blit(imgOggetti[oggetton - 1], (GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3))
            elif oggetton == 0:
                GlobalVar.schermo.blit(GlobalVar.frecciaMenu, (GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3))
            elif oggetton == 11:
                if dati[133] == 0:
                    GlobalVar.schermo.blit(GlobalVar.faretra1Menu, (GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3))
                elif dati[133] == 1:
                    GlobalVar.schermo.blit(GlobalVar.faretra2Menu, (GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3))
                else:
                    GlobalVar.schermo.blit(GlobalVar.faretra3Menu, (GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3))

            # menu conferma
            if confermaOggettoDaAcquistare != 0:
                # posizionare il cursore sul menu compra
                if usauno:
                    xpv = xp
                    ypv = yp
                    xp = GlobalVar.gsx // 32 * 5.3
                    yp = GlobalVar.gsy // 18 * 6.9
                    voceMarcata = 2
                    usauno = False
                GlobalVar.schermo.blit(puntatorevecchio, (xpv, ypv))
                messaggio("x" + str(numeroOggettiAcquistati), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 7.5, GlobalVar.gsy // 18 * 4.5, 50)
                if oggetton == 11:
                    GlobalVar.schermo.blit(GlobalVar.scorriSuGiuBloccato, (GlobalVar.gsx // 32 * 8.5, GlobalVar.gsy // 18 * 4.3))
                    if dati[133] == 1:
                        messaggio("(Monete necessarie: %i)" % (GlobalVar.costoOggetti[oggetton + 1] * numeroOggettiAcquistati), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 5.3, 50)
                    elif dati[133] >= 2:
                        messaggio("(Monete necessarie: %i)" % (GlobalVar.costoOggetti[oggetton + 2] * numeroOggettiAcquistati), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 5.3, 50)
                    else:
                        messaggio("(Monete necessarie: %i)" % (GlobalVar.costoOggetti[oggetton] * numeroOggettiAcquistati), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 5.3, 50)
                else:
                    if voceMarcata != 0 and oggetton != 11 and (tastop == pygame.K_w or (mouseSinistroPremuto and mouseInquadraFrecciaSu)):
                        GlobalVar.schermo.blit(GlobalVar.scorriSuGiuBloccatoSu, (GlobalVar.gsx // 32 * 8.5, GlobalVar.gsy // 18 * 4.3))
                    elif voceMarcata != 0 and oggetton != 11 and (tastop == pygame.K_s or (mouseSinistroPremuto and mouseInquadraFrecciaGiu)):
                        GlobalVar.schermo.blit(GlobalVar.scorriSuGiuBloccatoGiu, (GlobalVar.gsx // 32 * 8.5, GlobalVar.gsy // 18 * 4.3))
                    else:
                        GlobalVar.schermo.blit(GlobalVar.scorriSuGiu, (GlobalVar.gsx // 32 * 8.5, GlobalVar.gsy // 18 * 4.3))
                    messaggio("(Monete necessarie: %i)" % (GlobalVar.costoOggetti[oggetton] * numeroOggettiAcquistati), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 5.3, 50)
                messaggio("Conferma", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 6.9, 50)
                messaggio("Annulla", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 6.9, 50)

            messaggio("Acquista oggetti", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 1, 150)
            messaggio("Oggetti acquistabili", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 4.8, 40)
            messaggio("Costo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16.5, GlobalVar.gsy // 18 * 4.8, 40)
            messaggio("Posseduti", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18.5, GlobalVar.gsy // 18 * 4.8, 40)
            pygame.draw.line(GlobalVar.schermo, GlobalVar.grigiochi, (int(GlobalVar.gpx * 11), int(GlobalVar.gpy * 5.5)), (int(GlobalVar.gpx * 21), int(GlobalVar.gpy * 5.5)), 1)

            messaggio("Freccia", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 6.2, 40)
            messaggio(str(GlobalVar.costoOggetti[0]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16.8, GlobalVar.gsy // 18 * 6.2, 40)
            messaggio("x%i" % dati[132], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 6.2, 40)
            if oggetton == 0:
                messaggio("Freccia:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 11.5, 60)
                messaggio("Usate per attaccare i nemici a distanza", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 12.5, 35)
                messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13, 35)
                messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13.5, 35)
            if imgOggetti[0] != sconosciutoOggetto:
                messaggio("Pozione", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 7.1, 40)
                messaggio(str(GlobalVar.costoOggetti[1]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16.8, GlobalVar.gsy // 18 * 7.1, 40)
                if dati[31] < 0:
                    messaggio("x0", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 7.1, 40)
                else:
                    messaggio("x%i" % dati[31], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 7.1, 40)
                if oggetton == 1:
                    messaggio("Pozione:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 11.5, 60)
                    messaggio("Recupera 100 pv di Sara", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 12.5, 35)
                    messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13, 35)
                    messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 7.1, 40)
            if imgOggetti[1] != sconosciutoOggetto:
                messaggio("Alimentazione 100gr", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 8, 40)
                messaggio(str(GlobalVar.costoOggetti[2]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16.8, GlobalVar.gsy // 18 * 8, 40)
                if dati[32] < 0:
                    messaggio("x0", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 8, 40)
                else:
                    messaggio("x%i" % dati[32], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 8, 40)
                if oggetton == 2:
                    messaggio("Alimentazione 100gr:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 11.5, 60)
                    messaggio("Recupera 250 pe di Colco", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 12.5, 35)
                    messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13, 35)
                    messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 8, 40)
            if imgOggetti[2] != sconosciutoOggetto:
                messaggio("Medicina", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 8.9, 40)
                messaggio(str(GlobalVar.costoOggetti[3]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16.8, GlobalVar.gsy // 18 * 8.9, 40)
                if dati[33] < 0:
                    messaggio("x0", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 8.9, 40)
                else:
                    messaggio("x%i" % dati[33], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 8.9, 40)
                if oggetton == 3:
                    messaggio("Medicina:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 11.5, 60)
                    messaggio("Cura avvelenamento a Sara", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 12.5, 35)
                    messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13, 35)
                    messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 8.9, 40)
            if imgOggetti[3] != sconosciutoOggetto:
                messaggio("Super pozione", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 9.8, 40)
                messaggio(str(GlobalVar.costoOggetti[4]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16.8, GlobalVar.gsy // 18 * 9.8, 40)
                if dati[34] < 0:
                    messaggio("x0", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 9.8, 40)
                else:
                    messaggio("x%i" % dati[34], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 9.8, 40)
                if oggetton == 4:
                    messaggio("Super pozione:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 11.5, 60)
                    messaggio("Recupera 300 pv di Sara", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 12.5, 35)
                    messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13, 35)
                    messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 9.8, 40)
            if imgOggetti[4] != sconosciutoOggetto:
                messaggio("Alimentazione 250gr", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 10.7, 40)
                messaggio(str(GlobalVar.costoOggetti[5]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16.8, GlobalVar.gsy // 18 * 10.7, 40)
                if dati[35] < 0:
                    messaggio("x0", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 10.7, 40)
                else:
                    messaggio("x%i" % dati[35], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 10.7, 40)
                if oggetton == 5:
                    messaggio("Alimentazione 250gr:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 11.5, 60)
                    messaggio("Recupera 600 pe di Colco", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 12.5, 35)
                    messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13, 35)
                    messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 10.7, 40)
            if imgOggetti[5] != sconosciutoOggetto:
                messaggio("Bomba", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 11.6, 40)
                messaggio(str(GlobalVar.costoOggetti[6]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16.8, GlobalVar.gsy // 18 * 11.6, 40)
                if dati[36] < 0:
                    messaggio("x0", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 11.6, 40)
                else:
                    messaggio("x%i" % dati[36], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 11.6, 40)
                if oggetton == 6:
                    messaggio("Bomba:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 11.5, 60)
                    messaggio("Infligge un po' di danni ai nemici su cui viene", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 12.5, 35)
                    messaggio("lanciata", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13, 35)
                    messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 11.6, 40)
            if imgOggetti[6] != sconosciutoOggetto:
                messaggio("Bomba velenosa", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 12.5, 40)
                messaggio(str(GlobalVar.costoOggetti[7]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16.8, GlobalVar.gsy // 18 * 12.5, 40)
                if dati[37] < 0:
                    messaggio("x0", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 12.5, 40)
                else:
                    messaggio("x%i" % dati[37], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 12.5, 40)
                if oggetton == 7:
                    messaggio("Bomba velenosa:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 11.5, 60)
                    messaggio("Infligge avvelenamento al nemico su cui viene", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 12.5, 35)
                    messaggio("lanciata", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13, 35)
                    messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 12.5, 40)
            if imgOggetti[7] != sconosciutoOggetto:
                messaggio("Esca", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 13.4, 40)
                messaggio(str(GlobalVar.costoOggetti[8]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16.8, GlobalVar.gsy // 18 * 13.4, 40)
                if dati[38] < 0:
                    messaggio("x0", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 13.4, 40)
                else:
                    messaggio("x%i" % dati[38], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 13.4, 40)
                if oggetton == 8:
                    messaggio("Esca:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 11.5, 60)
                    messaggio(u"Distrae i nemici finché non viene distrutta. È", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 12.5, 35)
                    messaggio("possibile riprenderla passandoci sopra", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13, 35)
                    messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 13.4, 40)
            if imgOggetti[8] != sconosciutoOggetto:
                messaggio("Bomba appiccicosa", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 14.3, 40)
                messaggio(str(GlobalVar.costoOggetti[9]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16.8, GlobalVar.gsy // 18 * 14.3, 40)
                if dati[39] < 0:
                    messaggio("x0", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 14.3, 40)
                else:
                    messaggio("x%i" % dati[39], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 14.3, 40)
                if oggetton == 9:
                    messaggio("Bomba appiccicosa:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 11.5, 60)
                    messaggio(u"Dimezza la velocità del nemico su cui viene", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 12.5, 35)
                    messaggio("lanciata", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13, 35)
                    messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 14.3, 40)
            if imgOggetti[9] != sconosciutoOggetto:
                messaggio("Bomba potenziata", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 15.2, 40)
                messaggio(str(GlobalVar.costoOggetti[10]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16.8, GlobalVar.gsy // 18 * 15.2, 40)
                if dati[40] < 0:
                    messaggio("x0", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 15.2, 40)
                else:
                    messaggio("x%i" % dati[40], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 15.2, 40)
                if oggetton == 10:
                    messaggio("Bomba potenziata:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 11.5, 60)
                    messaggio("Infligge molti danni ai nemici su cui viene", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 12.5, 35)
                    messaggio("lanciata in un vasto raggio", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13, 35)
                    messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 15.2, 40)
            messaggio("Faretra", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 16.1, 40)
            if dati[133] == 0:
                messaggio(str(GlobalVar.costoOggetti[11]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16.8, GlobalVar.gsy // 18 * 16.1, 40)
            if dati[133] == 1:
                messaggio(str(GlobalVar.costoOggetti[12]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16.8, GlobalVar.gsy // 18 * 16.1, 40)
            if dati[133] >= 2:
                messaggio(str(GlobalVar.costoOggetti[13]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 16.8, GlobalVar.gsy // 18 * 16.1, 40)
            if dati[133] == 3:
                messaggio("x1", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 16.1, 40)
            else:
                messaggio("x0", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 16.1, 40)
            if oggetton == 11:
                messaggio("Faretra:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 11.5, 60)
                messaggio(u"Permette di trasportare più frecce", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 12.5, 35)
                messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13, 35)
                messaggio("", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 13.5, 35)

            GlobalVar.schermo.blit(puntatore, (xp, yp))
            if confermaOggettoDaAcquistare == 0:
                pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscu, ((xp + (int(GlobalVar.gpx // 1.5))), yp + (int(GlobalVar.gpy * 0.7))), (xp + (int(GlobalVar.gpx * 9.5)), yp + (int(GlobalVar.gpy * 0.7))), 2)
            else:
                pygame.draw.line(GlobalVar.schermo, GlobalVar.grigioscu, ((xpv + (int(GlobalVar.gpx // 1.5))), ypv + (int(GlobalVar.gpy * 0.7))), (xpv + (int(GlobalVar.gpx * 9.5)), ypv + (int(GlobalVar.gpy * 0.7))), 2)
            pygame.display.update()

        GlobalVar.clockMenu.tick(GlobalVar.fpsMenu)

    GlobalVar.canaleSoundCanzone.set_volume(GlobalVar.volumeCanzoni)
    return dati
