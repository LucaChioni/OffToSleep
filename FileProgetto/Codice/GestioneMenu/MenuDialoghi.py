# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche


def dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi):
    GlobalHWVar.canaleSoundPassiRallo.stop()
    oggettoRicevuto = False
    menuMercante = False
    sceltaEffettuata = 0
    voceMarcata = 1
    puntatoreSpostato = False
    puntatore = GlobalImgVar.puntatore
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
        imgPersDialogo = GlobalImgVar.imgDialogoLucy1
        nomePersonaggio = "Lucy"
    elif GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
        imgPersDialogo = GlobalImgVar.imgDialogoFraMaggiore
        nomePersonaggio = "Hans"
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
        imgPersDialogo = GlobalImgVar.imgDialogoLucy1
        nomePersonaggio = "Lucy"
    else:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            imgPersDialogo = GlobalImgVar.imgDialogoLucyAssonnata
        else:
            imgPersDialogo = GlobalImgVar.imgDialogoLucy2
        nomePersonaggio = "Lucy"

    if personaggio.nome != "Tutorial":
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersDialogo, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 3.5))
    if personaggio.nome != "Tutorial" and personaggio.nome != "Nessuno":
        GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgDialogo, (GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 3.5))
    schermo_prima_del_dialogo = GlobalHWVar.schermo.copy().convert()
    background = schermo_prima_del_dialogo.subsurface(pygame.Rect(0, 0, GlobalHWVar.gsx, GlobalHWVar.gsy)).convert()
    dark = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
    dark.fill((0, 0, 0, 150))
    background.blit(dark, (0, 0))
    GlobalHWVar.disegnaImmagineSuSchermo(background, (0, 0))

    schermo_prima_del_dialogo = GlobalHWVar.schermo.copy().convert()
    background = schermo_prima_del_dialogo.subsurface(pygame.Rect(0, GlobalHWVar.gsy // 18 * 3.5, GlobalHWVar.gsx, GlobalHWVar.gsy // 18 * 14.5)).convert()

    primoframe = True
    numeroMessaggiTotali = len(personaggio.partiDialogo)
    numeromessaggioAttuale = 0
    prosegui = True
    fineDialogo = False

    aggiornaInterfacciaPerCambioInput = True
    bottoneDown = False

    # GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni / 2)
    # GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti / 2)
    while not fineDialogo:
        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        if GlobalHWVar.mouseVisibile:
            if numeromessaggioAttuale < len(personaggio.partiDialogo) and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                if GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 15.1 <= yMouse <= GlobalHWVar.gsy // 18 * 16.2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 1
                elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 16.2 <= yMouse <= GlobalHWVar.gsy // 18 * 17.3:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 2
                elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 31 and GlobalHWVar.gsy // 18 * 15.1 <= yMouse <= GlobalHWVar.gsy // 18 * 16.2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 3
                elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 31 and GlobalHWVar.gsy // 18 * 16.2 <= yMouse <= GlobalHWVar.gsy // 18 * 17.3:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 4
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            else:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
            if voceMarcataVecchia != voceMarcata and not primoframe:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
        primoframe = False

        # gestione degli input
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            fineDialogo = True
            bottoneDown = False
        if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
            puntatoreSpostato = True
            prosegui = True
            if voceMarcata != 1 and voceMarcata != 3:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                voceMarcata -= 1
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
            puntatoreSpostato = True
            prosegui = True
            if voceMarcata != 1 and voceMarcata != 2:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                voceMarcata -= 2
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
            puntatoreSpostato = True
            prosegui = True
            if voceMarcata != 2 and voceMarcata != 4:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                voceMarcata += 1
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
            puntatoreSpostato = True
            prosegui = True
            if voceMarcata != 3 and voceMarcata != 4:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                voceMarcata += 2
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        elif bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
            if sceltaEffettuata != 0 and sceltaEffettuata != personaggio.scelta:
                fineDialogo = True
            elif numeromessaggioAttuale == numeroMessaggiTotali:
                if not personaggio.scelta or (personaggio.scelta and personaggio.scelta == sceltaEffettuata):
                    if personaggio.avanzaStoria:
                        avanzamentoStoria = avanzamentoStoria + 1
                    if personaggio.oggettoDato:
                        oggettoRicevuto = personaggio.oggettoDato
                    if personaggio.menuMercante:
                        menuMercante = personaggio.menuMercante
                if personaggio.avanzaColDialogo:
                    personaggio.avanzamentoDialogo += 1
                    personaggio.avanzaColDialogo = False
                    i = 0
                    while i < len(listaAvanzamentoDialoghi):
                        if personaggio.tipo == listaAvanzamentoDialoghi[i]:
                            listaAvanzamentoDialoghi[i + 1] = personaggio.avanzamentoDialogo
                            break
                        i += 2
                fineDialogo = True
            else:
                if personaggio.scelta and personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                    sceltaEffettuata = voceMarcata
                prosegui = True
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if bottoneDown:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False

        if (prosegui or aggiornaInterfacciaPerCambioInput) and not fineDialogo:
            if aggiornaInterfacciaPerCambioInput and numeromessaggioAttuale != 0:
                numeromessaggioAttuale -= 1
                aggiornaInterfacciaPerCambioInput = False
            if puntatoreSpostato:
                numeromessaggioAttuale -= 1
                puntatoreSpostato = False
            GlobalHWVar.disegnaImmagineSuSchermo(background, (0, GlobalHWVar.gsy // 18 * 3.5))
            if personaggio.nome != "Tutorial":
                if personaggio.partiDialogo[numeromessaggioAttuale][0] == "personaggio" and personaggio.nome != "Nessuno":
                    GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgDialogo, (GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 3.5))
                if personaggio.partiDialogo[numeromessaggioAttuale][0] == "tu" or personaggio.partiDialogo[numeromessaggioAttuale][1] == "???DOMANDA???":
                    GlobalHWVar.disegnaImmagineSuSchermo(imgPersDialogo, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 3.5))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoDialoghi, (0, GlobalHWVar.gsy * 2 // 3))
            if personaggio.partiDialogo[numeromessaggioAttuale][0] == "personaggio":
                FunzioniGraficheGeneriche.messaggio(personaggio.nome + ":", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 4 // 5), 80)
            elif personaggio.partiDialogo[numeromessaggioAttuale][0] == "tu":
                FunzioniGraficheGeneriche.messaggio(nomePersonaggio + ":", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 4 // 5), 80)
            if personaggio.partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                FunzioniGraficheGeneriche.messaggio(personaggio.partiDialogo[numeromessaggioAttuale][sceltaEffettuata + 1], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3), 50)
            elif personaggio.partiDialogo[numeromessaggioAttuale][1] == "???DOMANDA???":
                FunzioniGraficheGeneriche.messaggio(personaggio.partiDialogo[numeromessaggioAttuale][2], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3), 50)
                FunzioniGraficheGeneriche.messaggio(personaggio.partiDialogo[numeromessaggioAttuale][3], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 1.2), 50)
                FunzioniGraficheGeneriche.messaggio(personaggio.partiDialogo[numeromessaggioAttuale][4], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 2.2), 50)
                FunzioniGraficheGeneriche.messaggio(personaggio.partiDialogo[numeromessaggioAttuale][5], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 1.2), 50)
                FunzioniGraficheGeneriche.messaggio(personaggio.partiDialogo[numeromessaggioAttuale][6], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 2.2), 50)
                if voceMarcata == 1:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (GlobalHWVar.gsx // 32 * 1, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 1.2)))
                if voceMarcata == 2:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (GlobalHWVar.gsx // 32 * 1, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 2.2)))
                if voceMarcata == 3:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (GlobalHWVar.gsx // 32 * 16, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 1.2)))
                if voceMarcata == 4:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (GlobalHWVar.gsx // 32 * 16, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 2.2)))
            else:
                FunzioniGraficheGeneriche.messaggio(personaggio.partiDialogo[numeromessaggioAttuale][1], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3), 50, GlobalHWVar.gpx * 30, GlobalHWVar.gpy * 4 // 5)
            numeromessaggioAttuale += 1
            prosegui = False
            GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    # GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
    # GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti)

    return avanzamentoStoria, oggettoRicevuto, menuMercante, listaAvanzamentoDialoghi


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

                FunzioniGraficheGeneriche.messaggio("Acquista oggetti", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                FunzioniGraficheGeneriche.messaggio("Oggetti acquistabili", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.5, GlobalHWVar.gsy // 18 * 4.7, 45, centrale=True)
                FunzioniGraficheGeneriche.messaggio("Costo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 4.7, 45, centrale=True)
                FunzioniGraficheGeneriche.messaggio("Posseduti", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 4.7, 45, centrale=True)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 11), int(GlobalHWVar.gpy * 5.5)), (int(GlobalHWVar.gpx * 20.9), int(GlobalHWVar.gpy * 5.5)), 1)

                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 16.2) - 1, int(GlobalHWVar.gpy * 4.5)), (int(GlobalHWVar.gpx * 16.2) - 1, int(GlobalHWVar.gpy * 5.3)), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 16.2) - 1, int(GlobalHWVar.gpy * 5.7)), (int(GlobalHWVar.gpx * 16.2) - 1, int(GlobalHWVar.gpy * 17)), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 18.2) - 1, int(GlobalHWVar.gpy * 4.5)), (int(GlobalHWVar.gpx * 18.2) - 1, int(GlobalHWVar.gpy * 5.3)), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 18.2) - 1, int(GlobalHWVar.gpy * 5.7)), (int(GlobalHWVar.gpx * 18.2) - 1, int(GlobalHWVar.gpy * 17)), 2)

                FunzioniGraficheGeneriche.messaggio("Freccia", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 6.2, 40)
                FunzioniGraficheGeneriche.messaggio(str(GlobalGameVar.costoOggetti[0]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 6.2, 40, centrale=True)
                FunzioniGraficheGeneriche.messaggio("x%i" % dati[132], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 6.2, 40, centrale=True)
                if imgOggetti[0] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio("Pozione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 7.1, 40)
                    FunzioniGraficheGeneriche.messaggio(str(GlobalGameVar.costoOggetti[1]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 7.1, 40, centrale=True)
                    if dati[31] < 0:
                        FunzioniGraficheGeneriche.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 7.1, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio("x%i" % dati[31], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 7.1, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 7.1, 40)
                if imgOggetti[1] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio("Alimentazione 100gr", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 8, 40)
                    FunzioniGraficheGeneriche.messaggio(str(GlobalGameVar.costoOggetti[2]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 8, 40, centrale=True)
                    if dati[32] < 0:
                        FunzioniGraficheGeneriche.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 8, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio("x%i" % dati[32], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 8, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 8, 40)
                if imgOggetti[2] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio("Medicina", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 8.9, 40)
                    FunzioniGraficheGeneriche.messaggio(str(GlobalGameVar.costoOggetti[3]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 8.9, 40, centrale=True)
                    if dati[33] < 0:
                        FunzioniGraficheGeneriche.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 8.9, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio("x%i" % dati[33], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 8.9, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 8.9, 40)
                if imgOggetti[3] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio("Super pozione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 9.8, 40)
                    FunzioniGraficheGeneriche.messaggio(str(GlobalGameVar.costoOggetti[4]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 9.8, 40, centrale=True)
                    if dati[34] < 0:
                        FunzioniGraficheGeneriche.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 9.8, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio("x%i" % dati[34], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 9.8, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 9.8, 40)
                if imgOggetti[4] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio("Alimentazione 250gr", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 10.7, 40)
                    FunzioniGraficheGeneriche.messaggio(str(GlobalGameVar.costoOggetti[5]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 10.7, 40, centrale=True)
                    if dati[35] < 0:
                        FunzioniGraficheGeneriche.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 10.7, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio("x%i" % dati[35], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 10.7, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 10.7, 40)
                if imgOggetti[5] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio("Bomba", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 11.6, 40)
                    FunzioniGraficheGeneriche.messaggio(str(GlobalGameVar.costoOggetti[6]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 11.6, 40, centrale=True)
                    if dati[36] < 0:
                        FunzioniGraficheGeneriche.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 11.6, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio("x%i" % dati[36], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 11.6, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 11.6, 40)
                if imgOggetti[6] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio("Bomba velenosa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 12.5, 40)
                    FunzioniGraficheGeneriche.messaggio(str(GlobalGameVar.costoOggetti[7]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 12.5, 40, centrale=True)
                    if dati[37] < 0:
                        FunzioniGraficheGeneriche.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 12.5, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio("x%i" % dati[37], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 12.5, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 12.5, 40)
                if imgOggetti[7] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio("Esca", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 13.4, 40)
                    FunzioniGraficheGeneriche.messaggio(str(GlobalGameVar.costoOggetti[8]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 13.4, 40, centrale=True)
                    if dati[38] < 0:
                        FunzioniGraficheGeneriche.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 13.4, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio("x%i" % dati[38], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 13.4, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 13.4, 40)
                if imgOggetti[8] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio("Bomba appiccicosa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 14.3, 40)
                    FunzioniGraficheGeneriche.messaggio(str(GlobalGameVar.costoOggetti[9]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 14.3, 40, centrale=True)
                    if dati[39] < 0:
                        FunzioniGraficheGeneriche.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 14.3, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio("x%i" % dati[39], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 14.3, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 14.3, 40)
                if imgOggetti[9] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio("Bomba potenziata", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 15.2, 40)
                    FunzioniGraficheGeneriche.messaggio(str(GlobalGameVar.costoOggetti[10]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 15.2, 40, centrale=True)
                    if dati[40] < 0:
                        FunzioniGraficheGeneriche.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 15.2, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio("x%i" % dati[40], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 15.2, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 15.2, 40)
                FunzioniGraficheGeneriche.messaggio("Faretra", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 16.1, 40)
                if dati[133] == 0:
                    FunzioniGraficheGeneriche.messaggio(str(GlobalGameVar.costoOggetti[11]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 16.1, 40, centrale=True)
                if dati[133] == 1:
                    FunzioniGraficheGeneriche.messaggio(str(GlobalGameVar.costoOggetti[12]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 16.1, 40, centrale=True)
                if dati[133] >= 2:
                    FunzioniGraficheGeneriche.messaggio(str(GlobalGameVar.costoOggetti[13]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 16.1, 40, centrale=True)
                if dati[133] == 3:
                    FunzioniGraficheGeneriche.messaggio("x1", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 16.1, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("x0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 16.1, 40, centrale=True)
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
                    FunzioniGraficheGeneriche.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 9.5, GlobalHWVar.gsy // 18 * 4.5))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoDialogoMercante, (GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 4))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 4))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 7))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 7))
            if moneteInsufficienti:
                FunzioniGraficheGeneriche.messaggio("Non hai abbastanza monete!", GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 5.3, GlobalHWVar.gsy // 18 * 6.1, 40, centrale=True)
            if inventarioPieno:
                FunzioniGraficheGeneriche.messaggio("Non puoi prenderne altre...", GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 5.3, GlobalHWVar.gsy // 18 * 5.3, 40, centrale=True)

            # menu conferma
            if confermaOggettoDaAcquistare != 0:
                FunzioniGraficheGeneriche.messaggio("Quante te ne servono?", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, 50)
                # posizionare il cursore sul menu compra
                if usauno:
                    xpv = xp
                    ypv = yp
                    xp = GlobalHWVar.gsx // 32 * 5.3
                    yp = GlobalHWVar.gsy // 18 * 6.9
                    voceMarcata = 2
                    usauno = False
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xpv, ypv))
                FunzioniGraficheGeneriche.messaggio("x" + str(numeroOggettiAcquistati), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 7.5, GlobalHWVar.gsy // 18 * 4.5, 50)
                if oggetton == 11:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSuGiuBloccato, (GlobalHWVar.gsx // 32 * 8.5, GlobalHWVar.gsy // 18 * 4.3))
                    if dati[133] == 1:
                        FunzioniGraficheGeneriche.messaggio("(Monete necessarie: %i)" % (GlobalGameVar.costoOggetti[oggetton + 1] * numeroOggettiAcquistati), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5.3, 50)
                    elif dati[133] >= 2:
                        FunzioniGraficheGeneriche.messaggio("(Monete necessarie: %i)" % (GlobalGameVar.costoOggetti[oggetton + 2] * numeroOggettiAcquistati), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5.3, 50)
                    else:
                        FunzioniGraficheGeneriche.messaggio("(Monete necessarie: %i)" % (GlobalGameVar.costoOggetti[oggetton] * numeroOggettiAcquistati), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5.3, 50)
                else:
                    if voceMarcata != 0 and oggetton != 11 and (bottoneDown == pygame.K_w or (bottoneDown == "mouseSinistro" and mouseInquadraFrecciaSu) or bottoneDown == "padSu"):
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSuGiuBloccatoSu, (GlobalHWVar.gsx // 32 * 8.5, GlobalHWVar.gsy // 18 * 4.3))
                    elif voceMarcata != 0 and oggetton != 11 and (bottoneDown == pygame.K_s or (bottoneDown == "mouseSinistro" and mouseInquadraFrecciaGiu) or bottoneDown == "padGiu"):
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSuGiuBloccatoGiu, (GlobalHWVar.gsx // 32 * 8.5, GlobalHWVar.gsy // 18 * 4.3))
                    else:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSuGiu, (GlobalHWVar.gsx // 32 * 8.5, GlobalHWVar.gsy // 18 * 4.3))
                    FunzioniGraficheGeneriche.messaggio("(Monete necessarie: %i)" % (GlobalGameVar.costoOggetti[oggetton] * numeroOggettiAcquistati), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5.3, 50)
                FunzioniGraficheGeneriche.messaggio("Conferma", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.9, 50)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 5.3) - 1, int(GlobalHWVar.gpy * 6.8)), (int(GlobalHWVar.gpx * 5.3) - 1, int(GlobalHWVar.gpy * 7.5)), 2)
                FunzioniGraficheGeneriche.messaggio("Annulla", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 6.9, 50)
            else:
                FunzioniGraficheGeneriche.messaggio("Prendi quello che ti serve", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, 50)
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

                    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 22), int(GlobalHWVar.gpy * 14.5)), (int(GlobalHWVar.gpx * 31.5), int(GlobalHWVar.gpy * 14.5)), 2)
                    FunzioniGraficheGeneriche.messaggio("Monete: " + str(dati[131]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15.8, 50)

                    grandezzaCarettereDescrizioni = 40
                    larghezzaTestoDescrizioni = GlobalHWVar.gpx * 8.5
                    spazioTraLeRigheTestoDescrizione = int(GlobalHWVar.gpy * 0.6)
                    if oggetton == 0:
                        FunzioniGraficheGeneriche.messaggio("Freccia:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio("Usate per attaccare i nemici a distanza.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if imgOggetti[0] != sconosciutoOggetto and oggetton == 1:
                        FunzioniGraficheGeneriche.messaggio("Pozione:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio("Recupera 100 <*>#italic#Pv<*> di Lucy.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 1:
                        FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[1] != sconosciutoOggetto and oggetton == 2:
                        FunzioniGraficheGeneriche.messaggio("Alimentazione 100gr:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio("Recupera 250 <*>#italic#Pe<*> di Impo.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 2:
                        FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[2] != sconosciutoOggetto and oggetton == 3:
                        FunzioniGraficheGeneriche.messaggio("Medicina:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio("Cura avvelenamento a Lucy.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 3:
                        FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[3] != sconosciutoOggetto and oggetton == 4:
                        FunzioniGraficheGeneriche.messaggio("Super pozione:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio("Recupera 300 <*>#italic#Pv<*> di Lucy.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 4:
                        FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[4] != sconosciutoOggetto and oggetton == 5:
                        FunzioniGraficheGeneriche.messaggio("Alimentazione 250gr:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio("Recupera 600 <*>#italic#Pe<*> di Impo.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 5:
                        FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[5] != sconosciutoOggetto and oggetton == 6:
                        FunzioniGraficheGeneriche.messaggio("Bomba:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio("Infligge un po' di danni ai nemici su cui viene lanciata.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 6:
                        FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[6] != sconosciutoOggetto and oggetton == 7:
                        FunzioniGraficheGeneriche.messaggio("Bomba velenosa:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio("Infligge avvelenamento al nemico su cui viene lanciata.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 7:
                        FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[7] != sconosciutoOggetto and oggetton == 8:
                        FunzioniGraficheGeneriche.messaggio("Esca:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio(u"Distrae i nemici finché non viene distrutta. È possibile riprenderla passandoci sopra.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 8:
                        FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[8] != sconosciutoOggetto and oggetton == 9:
                        FunzioniGraficheGeneriche.messaggio("Bomba appiccicosa:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio(u"Dimezza la velocità del nemico su cui viene lanciata.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 9:
                        FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[9] != sconosciutoOggetto and oggetton == 10:
                        FunzioniGraficheGeneriche.messaggio("Bomba potenziata:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio("Infligge molti danni ai nemici su cui viene lanciata in un vasto raggio.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 10:
                        FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if oggetton == 11:
                        FunzioniGraficheGeneriche.messaggio("Faretra:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio(u"Permette di trasportare più frecce.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)

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

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)

    GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
    GlobalHWVar.canaleSoundSottofondoAmbientale.set_volume(GlobalHWVar.volumeEffetti)
    return dati
