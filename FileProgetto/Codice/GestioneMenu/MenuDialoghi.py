# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche
import Codice.SettaggiLivelli.SetDialoghiPersonaggi as SetDialoghiPersonaggi
import Codice.SettaggiLivelli.SetImgOggettiMappaPersonaggi as SetImgOggettiMappaPersonaggi
import Codice.SettaggiLivelli.SetPosizProtagonistaAudio as SetPosizProtagonistaAudio
import Codice.Localizzazione.LocalizInterfaccia as LI


def dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone):
    avanzamentoStoria = SetDialoghiPersonaggi.gestisciEventiPreDialoghi(avanzamentoStoria, personaggio, canzone)

    GlobalHWVar.canaleSoundPassiRallo.stop()
    oggettoRicevuto = False
    menuMercante = False
    sceltaEffettuata = 0
    voceMarcata = 1
    puntatoreSpostato = False
    puntatore = GlobalImgVar.puntatore
    nomePersonaggio = GlobalGameVar.nomePersonaggioDialoghi
    imgPersDialogo = GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgPersonaggioDialoghi"]

    nomeInterlocutore = personaggio.nome[GlobalHWVar.linguaImpostata]
    partiDialogo = []
    for dialogo in personaggio.partiDialogoTradotte:
        dialogoTemp = []
        for pezzoDialogo in dialogo:
            dialogoTemp.append(pezzoDialogo[GlobalHWVar.linguaImpostata])
        partiDialogo.append(dialogoTemp)
    oggettoDato = personaggio.oggettoDato[GlobalHWVar.linguaImpostata]

    xProtagonista = 0
    xInterlocutore = GlobalHWVar.gpx * 16
    grandezzaTestoNome = 80
    grandezzaTestoDialoghi = 50
    spazioTraLeRigheDialoghi = int(GlobalHWVar.gpy * 0.75)

    usandoCalcolatore = False
    if GlobalGameVar.dictAvanzamentoStoria["monologoPostSedutaSulCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
        usandoCalcolatore = True
    # diaologoTraAltri => ?? "True" quando sei nel calcolatore e c'?? un dialogo tra due personaggi
    diaologoTraAltri = False
    if GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroNelTempoAPrimaCheNeilLasciasseIlSuoUfficio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogo2Ren??NeilPostAvvioSequenzaNelCalcolatore"]:
        diaologoTraAltri = True
    elif GlobalGameVar.dictAvanzamentoStoria["uscitoRodDalPalazzoPreLancioMissile"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["avvioLancioMissileNucleare"]:
        diaologoTraAltri = True
    elif GlobalGameVar.dictAvanzamentoStoria["arrivataInForestaCadetta5Calcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoHansSamCalcolatore"]:
        diaologoTraAltri = True

    if nomeInterlocutore != "Tutorial" and not (usandoCalcolatore and not diaologoTraAltri):
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersDialogo, (xProtagonista, GlobalHWVar.gsy // 18 * 3.5))
    if personaggio.imgDialogo and nomeInterlocutore != "Tutorial" and nomeInterlocutore != "Nessuno":
        GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgDialogo, (xInterlocutore, GlobalHWVar.gsy // 18 * 3.5))
    elif nomeInterlocutore == "Impo":
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgDialogoColco, (xInterlocutore, GlobalHWVar.gsy // 18 * 3.5))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoDialoghi, (0, GlobalHWVar.gsy * 2 // 3))
    if diaologoTraAltri or not (usandoCalcolatore and (personaggio.tipo == "Nessuno" or not personaggio.imgDialogo)):
        FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False, tipoOscuramento=4, imgIlluminata=[GlobalImgVar.sfondoDialoghi, (0, GlobalHWVar.gsy * 2 // 3)])

    usandoRod = False
    if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
        usandoRod = True

    schermo_prima_del_dialogo = GlobalHWVar.schermo.copy()
    background = schermo_prima_del_dialogo.subsurface(pygame.Rect(0, GlobalHWVar.gsy // 18 * 3.5, GlobalHWVar.gsx, GlobalHWVar.gsy // 18 * 14.5)).convert()

    primoframe = True
    numeroMessaggiTotali = len(partiDialogo)
    numeromessaggioAttuale = 0
    prosegui = True
    fineDialogo = False
    bottoneDown = False

    if not usandoCalcolatore:
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [GlobalHWVar.volumeCanzoni / 2.0], True, posizioneCanaleMusica=0)
    while not fineDialogo:
        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        if GlobalHWVar.mouseVisibile:
            if numeromessaggioAttuale < len(partiDialogo) and partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
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
                puntatoreSpostato = True
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)

        # gestione degli input
        if not primoframe:
            bottoneDown, inutile = GestioneInput.getInput(bottoneDown, False)
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["Q"] or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            fineDialogo = True
            bottoneDown = False
        if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == "padSu") and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
            puntatoreSpostato = True
            if voceMarcata != 1 and voceMarcata != 3:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                voceMarcata -= 1
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["A"] or bottoneDown == "padSinistra") and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
            puntatoreSpostato = True
            if voceMarcata != 1 and voceMarcata != 2:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                voceMarcata -= 2
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == "padGiu") and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
            puntatoreSpostato = True
            if voceMarcata != 2 and voceMarcata != 4:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                voceMarcata += 1
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["D"] or bottoneDown == "padDestra") and personaggio.scelta and numeromessaggioAttuale < numeroMessaggiTotali and partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
            puntatoreSpostato = True
            if voceMarcata != 3 and voceMarcata != 4:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                voceMarcata += 2
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
            if sceltaEffettuata != 0 and sceltaEffettuata != personaggio.scelta and personaggio.scelta != -1:
                fineDialogo = True
            elif numeromessaggioAttuale == numeroMessaggiTotali:
                if personaggio.tipo == "Pazzo1" and personaggio.avanzamentoDialogo == 2 and sceltaEffettuata == 3:
                    GlobalGameVar.pazzoStrabico = True
                elif personaggio.tipo == "OggettoArmadioCastello" and not usandoRod and (sceltaEffettuata == 1 or sceltaEffettuata == 2):
                    if GlobalGameVar.cambiataAlCastello[0]:
                        GlobalGameVar.cambiataAlCastello[0] = False
                    else:
                        GlobalGameVar.cambiataAlCastello[0] = True
                if not personaggio.scelta or (personaggio.scelta and personaggio.scelta == sceltaEffettuata) or personaggio.scelta == -1:
                    if personaggio.avanzaStoria:
                        avanzamentoStoria += 1
                    if oggettoDato:
                        oggettoRicevuto = oggettoDato
                    if personaggio.menuMercante:
                        menuMercante = personaggio.menuMercante
                if personaggio.avanzaColDialogo:
                    personaggio.avanzamentoDialogo += 1
                    personaggio.avanzaColDialogo = False
                    i = 0
                    while i < len(listaAvanzamentoDialoghi):
                        if personaggio.tipoId == listaAvanzamentoDialoghi[i]:
                            listaAvanzamentoDialoghi[i + 1] = personaggio.avanzamentoDialogo
                            break
                        i += 2
                fineDialogo = True
                # segno il dialogo come gi?? letto
                if personaggio.idDialogoCorrente and not personaggio.idDialogoCorrente in GlobalGameVar.idDialoghiLetti:
                    GlobalGameVar.idDialoghiLetti.append(personaggio.idDialogoCorrente)
            else:
                if personaggio.scelta and partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                    sceltaEffettuata = voceMarcata
                    if sceltaEffettuata != personaggio.scelta and personaggio.scelta != -1:
                        SetDialoghiPersonaggi.gestisciRisposteSbagliate(avanzamentoStoria)
                    elif sceltaEffettuata == personaggio.scelta and personaggio.scelta != -1:
                        SetDialoghiPersonaggi.gestisciRisposteCorrette(avanzamentoStoria, personaggio.tipo)
                prosegui = True
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        if bottoneDown:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False

        if (prosegui or puntatoreSpostato) and not fineDialogo:
            parlante = "tu"
            if puntatoreSpostato and not prosegui:
                numeromessaggioAttuale -= 1
            GlobalHWVar.disegnaImmagineSuSchermo(background, (0, GlobalHWVar.gsy // 18 * 3.5))
            if nomeInterlocutore != "Tutorial":
                if personaggio.imgDialogo and partiDialogo[numeromessaggioAttuale][0] == "personaggio" and nomeInterlocutore != "Nessuno":
                    GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgDialogo, (xInterlocutore, GlobalHWVar.gsy // 18 * 3.5))
                elif partiDialogo[numeromessaggioAttuale][0] == "personaggio" and nomeInterlocutore == "Impo":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgDialogoColco, (xInterlocutore, GlobalHWVar.gsy // 18 * 3.5))
                if (partiDialogo[numeromessaggioAttuale][0] == "tu" or partiDialogo[numeromessaggioAttuale][1] == "???DOMANDA???") and not (usandoCalcolatore and not diaologoTraAltri):
                    GlobalHWVar.disegnaImmagineSuSchermo(imgPersDialogo, (xProtagonista, GlobalHWVar.gsy // 18 * 3.5))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoDialoghi, (0, GlobalHWVar.gsy * 2 // 3))
            if partiDialogo[numeromessaggioAttuale][0] == "personaggio":
                parlante = personaggio.gender
                FunzioniGraficheGeneriche.messaggio(nomeInterlocutore + ":", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy * 2 // 3) + int(GlobalHWVar.gpy * 0.75), grandezzaTestoNome)
            elif partiDialogo[numeromessaggioAttuale][0] == "tu":
                FunzioniGraficheGeneriche.messaggio(nomePersonaggio + ":", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy * 2 // 3) + int(GlobalHWVar.gpy * 0.75), grandezzaTestoNome)
            if partiDialogo[numeromessaggioAttuale][1] == "!!!RISPOSTA!!!":
                bottoneDown, fineDialogo = FunzioniGraficheGeneriche.messaggioParlato(bottoneDown, fineDialogo, partiDialogo[numeromessaggioAttuale][sceltaEffettuata + 1], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy * 2 // 3) + int(GlobalHWVar.gpy * 2.15), grandezzaTestoDialoghi, GlobalHWVar.gpx * 30, spazioTraLeRigheDialoghi, parlante)
            elif partiDialogo[numeromessaggioAttuale][1] == "???DOMANDA???":
                if puntatoreSpostato and not prosegui:
                    bottoneDown, fineDialogo = FunzioniGraficheGeneriche.messaggioParlato(bottoneDown, fineDialogo, partiDialogo[numeromessaggioAttuale][2], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy * 2 // 3) + int(GlobalHWVar.gpy * 2.15), grandezzaTestoDialoghi, GlobalHWVar.gpx * 30, spazioTraLeRigheDialoghi, parlante, scriviTutto=True)
                else:
                    bottoneDown, fineDialogo = FunzioniGraficheGeneriche.messaggioParlato(bottoneDown, fineDialogo, partiDialogo[numeromessaggioAttuale][2], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy * 2 // 3) + int(GlobalHWVar.gpy * 2.15), grandezzaTestoDialoghi, GlobalHWVar.gpx * 30, spazioTraLeRigheDialoghi, parlante)
                FunzioniGraficheGeneriche.messaggio(partiDialogo[numeromessaggioAttuale][3], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, ((GlobalHWVar.gsy * 2 // 3) + int(GlobalHWVar.gpy * 2.15)) + int(GlobalHWVar.gpy * 1.32), grandezzaTestoDialoghi)
                FunzioniGraficheGeneriche.messaggio(partiDialogo[numeromessaggioAttuale][4], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, ((GlobalHWVar.gsy * 2 // 3) + int(GlobalHWVar.gpy * 2.15)) + int(GlobalHWVar.gpy * 2.32), grandezzaTestoDialoghi)
                FunzioniGraficheGeneriche.messaggio(partiDialogo[numeromessaggioAttuale][5], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, ((GlobalHWVar.gsy * 2 // 3) + int(GlobalHWVar.gpy * 2.15)) + int(GlobalHWVar.gpy * 1.32), grandezzaTestoDialoghi)
                FunzioniGraficheGeneriche.messaggio(partiDialogo[numeromessaggioAttuale][6], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, ((GlobalHWVar.gsy * 2 // 3) + int(GlobalHWVar.gpy * 2.15)) + int(GlobalHWVar.gpy * 2.32), grandezzaTestoDialoghi)
                if voceMarcata == 1:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (GlobalHWVar.gsx // 32 * 1, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 1.2)))
                if voceMarcata == 2:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (GlobalHWVar.gsx // 32 * 1, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 2.2)))
                if voceMarcata == 3:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (GlobalHWVar.gsx // 32 * 16, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 1.2)))
                if voceMarcata == 4:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (GlobalHWVar.gsx // 32 * 16, ((GlobalHWVar.gsy * 2 // 3) + (GlobalHWVar.gpy * 7 // 3)) + int(GlobalHWVar.gpy * 2.2)))
            else:
                bottoneDown, fineDialogo = FunzioniGraficheGeneriche.messaggioParlato(bottoneDown, fineDialogo, partiDialogo[numeromessaggioAttuale][1], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy * 2 // 3) + int(GlobalHWVar.gpy * 2.15), grandezzaTestoDialoghi, GlobalHWVar.gpx * 30, spazioTraLeRigheDialoghi, parlante)
            numeromessaggioAttuale += 1
            prosegui = False
            puntatoreSpostato = False
            GlobalHWVar.aggiornaSchermo()

        primoframe = False
        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    SetPosizProtagonistaAudio.decidiSeDimezzareVolumeMusica(avanzamentoStoria)
    if not usandoCalcolatore:
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [GlobalHWVar.volumeCanzoni], True, posizioneCanaleMusica=0)

    avanzamentoStoria = SetDialoghiPersonaggi.gestisciEventiPostDialoghi(avanzamentoStoria, personaggio, canzone)
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

    interlocutore = SetImgOggettiMappaPersonaggi.setImgMercanteMenu(dati[0], dati[1])
    imgMercante = GlobalImgVar.mercanteMenu
    if interlocutore == "Pappagallo":
        imgMercante = GlobalImgVar.pappagalloMenuMercante
    elif interlocutore == "Sara":
        imgMercante = GlobalImgVar.saraMenuMercante

    # tolgo tutte le monete se il tempo ?? bloccato
    if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
        dati[131] = 0

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    maxFrecce = GlobalGameVar.frecceMaxPerFaretra[dati[133]]
    costoOggettiTemp = GlobalGameVar.costoOggetti[:]
    if dati[0] > GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
        i = 0
        while i < len(costoOggettiTemp):
            costoOggettiTemp[i] = 0
            i += 1

    imgOggetti = []
    i = 1
    while i <= 10:
        if (i == 1 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercantePozione"]) or (i == 2 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteAlimantaz"]) or (i == 3 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteMedicina"]) or (i == 4 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteSuperPoz"]) or (i == 5 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteAlimMiglio"]) or (i == 6 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteBomba"]) or (i == 7 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteBomVele"]) or (i == 8 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteEsca"]) or (i == 9 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteBomAppi"]) or (i == 10 and dati[0] > GlobalGameVar.dictAvanzamentoStoria["mercanteBomPote"]):
            imgOggetti.append(GlobalImgVar.vetImgOggettiMercante[i - 1])
        else:
            imgOggetti.append(sconosciutoOggetto)
        i += 1

    GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone, GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeCanzoni / 2.0, GlobalHWVar.volumeEffetti / 3.0], True, posizioneCanaleMusica=0)
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
            if GlobalHWVar.gsx // 32 * 22.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
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
                if GlobalHWVar.gsy // 18 * 4.3 <= yMouse <= GlobalHWVar.gsy // 18 * 4.8 and GlobalHWVar.gsx // 32 * 7.45 <= xMouse <= GlobalHWVar.gsx // 32 * 8.45:
                    mouseInquadraFrecciaSu = True
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                elif GlobalHWVar.gsy // 18 * 4.8 <= yMouse <= GlobalHWVar.gsy // 18 * 5.3 and GlobalHWVar.gsx // 32 * 7.45 <= xMouse <= GlobalHWVar.gsx // 32 * 8.45:
                    mouseInquadraFrecciaGiu = True
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                elif GlobalHWVar.gsy // 18 * 6.7 <= yMouse <= GlobalHWVar.gsy // 18 * 8:
                    if GlobalHWVar.gsx // 32 * 0.5 <= xMouse <= GlobalHWVar.gsx // 32 * 5.3:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalHWVar.gsx // 32 * 1.3
                        yp = GlobalHWVar.gsy // 18 * 7.05
                    elif GlobalHWVar.gsx // 32 * 5.3 <= xMouse <= GlobalHWVar.gsx // 32 * 10:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalHWVar.gsx // 32 * 5.3
                        yp = GlobalHWVar.gsy // 18 * 7.05
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
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["Q"] or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
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
                    if 0 <= oggetton <= 10 and costoOggettiTemp[oggetton] * numeroOggettiAcquistati <= dati[131]:
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAcquisto)
                        primoFrame = True
                        dati[131] -= costoOggettiTemp[oggetton] * numeroOggettiAcquistati
                        dati[145] += costoOggettiTemp[oggetton] * numeroOggettiAcquistati
                        voceMarcata = 0
                        xp = GlobalHWVar.gsx // 32 * 10.5
                        # freccia
                        if confermaOggettoDaAcquistare == -1:
                            dati[132] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 6.1
                        # pozione
                        if confermaOggettoDaAcquistare == 1:
                            if dati[31] == -1:
                                dati[31] = 0
                            dati[31] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 7
                        # carica batt
                        if confermaOggettoDaAcquistare == 2:
                            if dati[32] == -1:
                                dati[32] = 0
                            dati[32] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 7.9
                        # antidoto
                        if confermaOggettoDaAcquistare == 3:
                            if dati[33] == -1:
                                dati[33] = 0
                            dati[33] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 8.8
                        # super pozione
                        if confermaOggettoDaAcquistare == 4:
                            if dati[34] == -1:
                                dati[34] = 0
                            dati[34] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 9.7
                        # carica migliorato
                        if confermaOggettoDaAcquistare == 5:
                            if dati[35] == -1:
                                dati[35] = 0
                            dati[35] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 10.6
                        # bomba
                        if confermaOggettoDaAcquistare == 6:
                            if dati[36] == -1:
                                dati[36] = 0
                            dati[36] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 11.5
                        # bomba veleno
                        if confermaOggettoDaAcquistare == 7:
                            if dati[37] == -1:
                                dati[37] = 0
                            dati[37] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 12.4
                        # esca
                        if confermaOggettoDaAcquistare == 8:
                            if dati[38] == -1:
                                dati[38] = 0
                            dati[38] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 13.3
                        # bomba appiccicosa
                        if confermaOggettoDaAcquistare == 9:
                            if dati[39] == -1:
                                dati[39] = 0
                            dati[39] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 14.2
                        # bomba potenziata
                        if confermaOggettoDaAcquistare == 10:
                            if dati[40] == -1:
                                dati[40] = 0
                            dati[40] += numeroOggettiAcquistati
                            yp = GlobalHWVar.gsy // 18 * 15.1
                        confermaOggettoDaAcquistare = 0
                        procediAllAcquisto = False
                    elif oggetton == 11:
                        if dati[133] == 0 and costoOggettiTemp[oggetton] * numeroOggettiAcquistati <= dati[131]:
                            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAcquisto)
                            primoFrame = True
                            dati[131] -= costoOggettiTemp[oggetton] * numeroOggettiAcquistati
                            dati[145] += costoOggettiTemp[oggetton] * numeroOggettiAcquistati
                            voceMarcata = 0
                            xp = GlobalHWVar.gsx // 32 * 10.5
                            # faretra
                            if confermaOggettoDaAcquistare == 11:
                                dati[133] += numeroOggettiAcquistati
                                yp = GlobalHWVar.gsy // 18 * 16
                            confermaOggettoDaAcquistare = 0
                            procediAllAcquisto = False
                        elif dati[133] == 1 and costoOggettiTemp[oggetton + 1] * numeroOggettiAcquistati <= dati[131]:
                            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAcquisto)
                            primoFrame = True
                            dati[131] -= costoOggettiTemp[oggetton + 1] * numeroOggettiAcquistati
                            dati[145] += costoOggettiTemp[oggetton] * numeroOggettiAcquistati
                            voceMarcata = 0
                            xp = GlobalHWVar.gsx // 32 * 10.5
                            # faretra
                            if confermaOggettoDaAcquistare == 11:
                                dati[133] += numeroOggettiAcquistati
                                yp = GlobalHWVar.gsy // 18 * 16
                            confermaOggettoDaAcquistare = 0
                            procediAllAcquisto = False
                        elif dati[133] == 2 and costoOggettiTemp[oggetton + 2] * numeroOggettiAcquistati <= dati[131]:
                            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAcquisto)
                            primoFrame = True
                            dati[131] -= costoOggettiTemp[oggetton + 2] * numeroOggettiAcquistati
                            dati[145] += costoOggettiTemp[oggetton] * numeroOggettiAcquistati
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
        if bottoneDown == "mouseSinistro" or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["A"] or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["D"] or bottoneDown == "padGiu" or bottoneDown == "padSu" or bottoneDown == "padSinistra" or bottoneDown == "padDestra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or oggettonVecchio != oggetton or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
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
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["A"] or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 2:
                    voceMarcata -= 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = xp - GlobalHWVar.gsx // 32 * 4
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
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
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["D"] or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
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

            maxFrecce = GlobalGameVar.frecceMaxPerFaretra[dati[133]]

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13.1))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 16.1))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 16.1))

                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sacchettoDenaroMercante, (GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 14))
                GlobalHWVar.disegnaImmagineSuSchermo(imgMercante, (GlobalHWVar.gsx // 32 * (-1), GlobalHWVar.gsy // 18 * 8))

                FunzioniGraficheGeneriche.messaggio(LI.ACQUISTA_OGGETTI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                FunzioniGraficheGeneriche.messaggio(LI.OGGETTI_ACQUISTABILI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.5, GlobalHWVar.gsy // 18 * 4.7, 45, centrale=True)
                FunzioniGraficheGeneriche.messaggio(LI.COSTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 4.7, 45, centrale=True)
                FunzioniGraficheGeneriche.messaggio(LI.POSSEDUTI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 4.7, 45, centrale=True)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 11), int(GlobalHWVar.gpy * 5.5)), (int(GlobalHWVar.gpx * 20.9), int(GlobalHWVar.gpy * 5.5)), 1)

                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 16.2) - 1, int(GlobalHWVar.gpy * 4.5)), (int(GlobalHWVar.gpx * 16.2) - 1, int(GlobalHWVar.gpy * 5.3)), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 16.2) - 1, int(GlobalHWVar.gpy * 5.7)), (int(GlobalHWVar.gpx * 16.2) - 1, int(GlobalHWVar.gpy * 16.8)), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 18.2) - 1, int(GlobalHWVar.gpy * 4.5)), (int(GlobalHWVar.gpx * 18.2) - 1, int(GlobalHWVar.gpy * 5.3)), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 18.2) - 1, int(GlobalHWVar.gpy * 5.7)), (int(GlobalHWVar.gpx * 18.2) - 1, int(GlobalHWVar.gpy * 16.8)), 2)

                FunzioniGraficheGeneriche.messaggio(LI.FRECCIA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 6.2, 40)
                FunzioniGraficheGeneriche.messaggio(str(costoOggettiTemp[0]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 6.2, 40, centrale=True)
                FunzioniGraficheGeneriche.messaggio(u"??%i" % dati[132], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 6.2, 40, centrale=True)
                if imgOggetti[0] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio(LI.POZIONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 7.1, 40)
                    FunzioniGraficheGeneriche.messaggio(str(costoOggettiTemp[1]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 7.1, 40, centrale=True)
                    if dati[31] < 0:
                        FunzioniGraficheGeneriche.messaggio(u"??0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 7.1, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio(u"??%i" % dati[31], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 7.1, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 7.1, 40)
                if imgOggetti[1] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio(LI.IMPOFRUTTO_PICCOLO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 8, 40)
                    FunzioniGraficheGeneriche.messaggio(str(costoOggettiTemp[2]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 8, 40, centrale=True)
                    if dati[32] < 0:
                        FunzioniGraficheGeneriche.messaggio(u"??0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 8, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio(u"??%i" % dati[32], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 8, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 8, 40)
                if imgOggetti[2] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio(LI.MEDICINA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 8.9, 40)
                    FunzioniGraficheGeneriche.messaggio(str(costoOggettiTemp[3]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 8.9, 40, centrale=True)
                    if dati[33] < 0:
                        FunzioniGraficheGeneriche.messaggio(u"??0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 8.9, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio(u"??%i" % dati[33], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 8.9, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 8.9, 40)
                if imgOggetti[3] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio(LI.SUPER_POZIONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 9.8, 40)
                    FunzioniGraficheGeneriche.messaggio(str(costoOggettiTemp[4]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 9.8, 40, centrale=True)
                    if dati[34] < 0:
                        FunzioniGraficheGeneriche.messaggio(u"??0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 9.8, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio(u"??%i" % dati[34], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 9.8, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 9.8, 40)
                if imgOggetti[4] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio(LI.IMPOFRUTTO_GRANDE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 10.7, 40)
                    FunzioniGraficheGeneriche.messaggio(str(costoOggettiTemp[5]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 10.7, 40, centrale=True)
                    if dati[35] < 0:
                        FunzioniGraficheGeneriche.messaggio(u"??0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 10.7, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio(u"??%i" % dati[35], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 10.7, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 10.7, 40)
                if imgOggetti[5] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio(LI.BOMBA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 11.6, 40)
                    FunzioniGraficheGeneriche.messaggio(str(costoOggettiTemp[6]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 11.6, 40, centrale=True)
                    if dati[36] < 0:
                        FunzioniGraficheGeneriche.messaggio(u"??0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 11.6, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio(u"??%i" % dati[36], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 11.6, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 11.6, 40)
                if imgOggetti[6] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio(LI.BOMBA_VELENOSA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 12.5, 40)
                    FunzioniGraficheGeneriche.messaggio(str(costoOggettiTemp[7]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 12.5, 40, centrale=True)
                    if dati[37] < 0:
                        FunzioniGraficheGeneriche.messaggio(u"??0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 12.5, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio(u"??%i" % dati[37], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 12.5, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 12.5, 40)
                if imgOggetti[7] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio(LI.ESCA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 13.4, 40)
                    FunzioniGraficheGeneriche.messaggio(str(costoOggettiTemp[8]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 13.4, 40, centrale=True)
                    if dati[38] < 0:
                        FunzioniGraficheGeneriche.messaggio(u"??0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 13.4, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio(u"??%i" % dati[38], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 13.4, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 13.4, 40)
                if imgOggetti[8] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio(LI.BOMBA_APPICCICOSA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 14.3, 40)
                    FunzioniGraficheGeneriche.messaggio(str(costoOggettiTemp[9]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 14.3, 40, centrale=True)
                    if dati[39] < 0:
                        FunzioniGraficheGeneriche.messaggio(u"??0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 14.3, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio(u"??%i" % dati[39], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 14.3, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 14.3, 40)
                if imgOggetti[9] != sconosciutoOggetto:
                    FunzioniGraficheGeneriche.messaggio(LI.BOMBA_POTENZIATA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 15.2, 40)
                    FunzioniGraficheGeneriche.messaggio(str(costoOggettiTemp[10]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 15.2, 40, centrale=True)
                    if dati[40] < 0:
                        FunzioniGraficheGeneriche.messaggio(u"??0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 15.2, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio(u"??%i" % dati[40], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 15.2, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 15.2, 40)
                FunzioniGraficheGeneriche.messaggio(LI.FARETRA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 16.1, 40)
                if dati[133] == 0:
                    FunzioniGraficheGeneriche.messaggio(str(costoOggettiTemp[11]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 16.1, 40, centrale=True)
                if dati[133] == 1:
                    FunzioniGraficheGeneriche.messaggio(str(costoOggettiTemp[12]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 16.1, 40, centrale=True)
                if dati[133] >= 2:
                    FunzioniGraficheGeneriche.messaggio(str(costoOggettiTemp[13]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.2, GlobalHWVar.gsy // 18 * 16.1, 40, centrale=True)
                if dati[133] == 3:
                    FunzioniGraficheGeneriche.messaggio(u"??1", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 16.1, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio(u"??0", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.6, GlobalHWVar.gsy // 18 * 16.1, 40, centrale=True)
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

                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gsx // 32 * 9.5, GlobalHWVar.gsy // 18 * 11.4))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15.5, GlobalHWVar.gsx // 32 * 5.5, GlobalHWVar.gsy // 18 * 1))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2.5))
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio(LI.TAS_DES_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio(LI.B_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio(LI.Q_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)

            GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 9.5, GlobalHWVar.gsy // 18 * 4.5))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoDialogoMercante, (GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 4))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 4))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 7))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 7))
            if moneteInsufficienti:
                if interlocutore == "Rod":
                    FunzioniGraficheGeneriche.messaggio(LI.NON_HAI_ABB_MON[GlobalHWVar.linguaImpostata], GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 5.25, GlobalHWVar.gsy // 18 * 6.1, 40, centrale=True)
                elif interlocutore == "Pappagallo":
                    FunzioniGraficheGeneriche.messaggio(LI.MONETE_INSUFFICIENTI[GlobalHWVar.linguaImpostata], GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 5.25, GlobalHWVar.gsy // 18 * 6.1, 40, centrale=True)
                elif interlocutore == "Sara":
                    FunzioniGraficheGeneriche.messaggio(LI.NON_HO_ABB_MON_DOV[GlobalHWVar.linguaImpostata], GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 5.25, GlobalHWVar.gsy // 18 * 6.1, 40, centrale=True)
            if inventarioPieno:
                if interlocutore == "Rod":
                    FunzioniGraficheGeneriche.messaggio(LI.NON_PUO_PRE_ALT[GlobalHWVar.linguaImpostata], GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 5.25, GlobalHWVar.gsy // 18 * 5.3, 40, centrale=True)
                elif interlocutore == "Pappagallo":
                    FunzioniGraficheGeneriche.messaggio(LI.SPAZIO_INSUFFICIENTE[GlobalHWVar.linguaImpostata], GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 5.25, GlobalHWVar.gsy // 18 * 5.3, 40, centrale=True)
                elif interlocutore == "Sara":
                    FunzioniGraficheGeneriche.messaggio(LI.NON_POS_TRA_ALT[GlobalHWVar.linguaImpostata], GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 5.25, GlobalHWVar.gsy // 18 * 5.3, 40, centrale=True)

            # menu conferma
            if confermaOggettoDaAcquistare != 0:
                if interlocutore == "Rod":
                    FunzioniGraficheGeneriche.messaggio(LI.QUA_TE_NE_SER[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 7.5, GlobalHWVar.gsy // 18 * 4.5, 50, daDestra=True)
                elif interlocutore == "Pappagallo":
                    FunzioniGraficheGeneriche.messaggio(LI.QUANTI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.8, GlobalHWVar.gsy // 18 * 4.5, 50, centrale=True)
                elif interlocutore == "Sara":
                    FunzioniGraficheGeneriche.messaggio(LI.QUA_ME_NE_SER[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 7.5, GlobalHWVar.gsy // 18 * 4.5, 50, daDestra=True)
                # posizionare il cursore sul menu compra
                if usauno:
                    xpv = xp
                    ypv = yp
                    xp = GlobalHWVar.gsx // 32 * 5.3
                    yp = GlobalHWVar.gsy // 18 * 7.05
                    voceMarcata = 2
                    usauno = False
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xpv, ypv))
                FunzioniGraficheGeneriche.messaggio(u"??" + str(numeroOggettiAcquistati), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 8.3, GlobalHWVar.gsy // 18 * 4.5, 50)
                if oggetton == 11:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSuGiuBloccato, (GlobalHWVar.gsx // 32 * 7.45, GlobalHWVar.gsy // 18 * 4.3))
                    if dati[133] == 1:
                        FunzioniGraficheGeneriche.messaggio(LI.MON_NEC_I[GlobalHWVar.linguaImpostata] % (costoOggettiTemp[oggetton + 1] * numeroOggettiAcquistati), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5.25, GlobalHWVar.gsy // 18 * 5.3, 50, centrale=True)
                    elif dati[133] >= 2:
                        FunzioniGraficheGeneriche.messaggio(LI.MON_NEC_I[GlobalHWVar.linguaImpostata] % (costoOggettiTemp[oggetton + 2] * numeroOggettiAcquistati), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5.25, GlobalHWVar.gsy // 18 * 5.3, 50, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio(LI.MON_NEC_I[GlobalHWVar.linguaImpostata] % (costoOggettiTemp[oggetton] * numeroOggettiAcquistati), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5.25, GlobalHWVar.gsy // 18 * 5.3, 50, centrale=True)
                else:
                    if voceMarcata != 0 and oggetton != 11 and (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or (bottoneDown == "mouseSinistro" and mouseInquadraFrecciaSu) or bottoneDown == "padSu"):
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSuGiuBloccatoSu, (GlobalHWVar.gsx // 32 * 7.45, GlobalHWVar.gsy // 18 * 4.3))
                    elif voceMarcata != 0 and oggetton != 11 and (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or (bottoneDown == "mouseSinistro" and mouseInquadraFrecciaGiu) or bottoneDown == "padGiu"):
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSuGiuBloccatoGiu, (GlobalHWVar.gsx // 32 * 7.45, GlobalHWVar.gsy // 18 * 4.3))
                    else:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSuGiu, (GlobalHWVar.gsx // 32 * 7.45, GlobalHWVar.gsy // 18 * 4.3))
                    FunzioniGraficheGeneriche.messaggio(LI.MON_NEC_I[GlobalHWVar.linguaImpostata] % (costoOggettiTemp[oggetton] * numeroOggettiAcquistati), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5.25, GlobalHWVar.gsy // 18 * 5.3, 50, centrale=True)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 1), int(GlobalHWVar.gpy * 6.7) - 1), (int(GlobalHWVar.gpx * 9.5), int(GlobalHWVar.gpy * 6.7) - 1), 2)
                FunzioniGraficheGeneriche.messaggio(LI.CONFERMA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.3, GlobalHWVar.gsy // 18 * 7, 50, centrale=True)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 5.3) - 1, int(GlobalHWVar.gpy * 6.9)), (int(GlobalHWVar.gpx * 5.3) - 1, int(GlobalHWVar.gpy * 7.7)), 2)
                FunzioniGraficheGeneriche.messaggio(LI.ANNULLA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 7.3, GlobalHWVar.gsy // 18 * 7, 50, centrale=True)
            else:
                if interlocutore == "Rod":
                    FunzioniGraficheGeneriche.messaggio(LI.PRE_QUE_CHE_TI_SER[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5.25, GlobalHWVar.gsy // 18 * 4.5, 50, centrale=True)
                elif interlocutore == "Pappagallo":
                    FunzioniGraficheGeneriche.messaggio(LI.COMPRA_[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5.25, GlobalHWVar.gsy // 18 * 4.5, 50, centrale=True)
                elif interlocutore == "Sara":
                    FunzioniGraficheGeneriche.messaggio(LI.COS_MI_SER[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5.25, GlobalHWVar.gsy // 18 * 4.5, 50, centrale=True)
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
                    FunzioniGraficheGeneriche.messaggio(LI.MONETE_[GlobalHWVar.linguaImpostata] + str(dati[131]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15.8, 50)

                    grandezzaCarettereDescrizioni = 40
                    larghezzaTestoDescrizioni = GlobalHWVar.gpx * 8.5
                    spazioTraLeRigheTestoDescrizione = int(GlobalHWVar.gpy * 0.6)
                    if oggetton == 0:
                        FunzioniGraficheGeneriche.messaggio(LI.FRECCIA_[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio(LI.USA_PER_ATT_I_NEM_A_DIS[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if imgOggetti[0] != sconosciutoOggetto and oggetton == 1:
                        FunzioniGraficheGeneriche.messaggio(LI.POZIONE_[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio(LI.REC_100_PV_DI_SAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 1:
                        FunzioniGraficheGeneriche.messaggio(LI.SCONOSCIUTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[1] != sconosciutoOggetto and oggetton == 2:
                        FunzioniGraficheGeneriche.messaggio(LI.IMPOFRUTTO_PICCOLO_[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio(LI.REC_250_PE_DI_IMP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 2:
                        FunzioniGraficheGeneriche.messaggio(LI.SCONOSCIUTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[2] != sconosciutoOggetto and oggetton == 3:
                        FunzioniGraficheGeneriche.messaggio(LI.MEDICINA_[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio(LI.CUR_AVV_A_SAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 3:
                        FunzioniGraficheGeneriche.messaggio(LI.SCONOSCIUTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[3] != sconosciutoOggetto and oggetton == 4:
                        FunzioniGraficheGeneriche.messaggio(LI.SUPER_POZIONE_[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio(LI.REC_300_PV_DI_SAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 4:
                        FunzioniGraficheGeneriche.messaggio(LI.SCONOSCIUTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[4] != sconosciutoOggetto and oggetton == 5:
                        FunzioniGraficheGeneriche.messaggio(LI.IMPOFRUTTO_GRANDE_[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio(LI.REC_600_PE_DI_IMP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 5:
                        FunzioniGraficheGeneriche.messaggio(LI.SCONOSCIUTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[5] != sconosciutoOggetto and oggetton == 6:
                        FunzioniGraficheGeneriche.messaggio(LI.BOMBA_[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio(LI.INF_UN_PO_DI_DAN_AI_NEM_SU_CUI_VIE_LAN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 6:
                        FunzioniGraficheGeneriche.messaggio(LI.SCONOSCIUTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[6] != sconosciutoOggetto and oggetton == 7:
                        FunzioniGraficheGeneriche.messaggio(LI.BOMBA_VELENOSA_[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio(LI.INF_AVV_AL_NEM_SU_CUI_VIE_LAN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 7:
                        FunzioniGraficheGeneriche.messaggio(LI.SCONOSCIUTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[7] != sconosciutoOggetto and oggetton == 8:
                        FunzioniGraficheGeneriche.messaggio(LI.ESCA_[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio(LI.DIS_I_NEM_FIN_NON_VIE_DIS__POS_RIP_PAS_SOP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 8:
                        FunzioniGraficheGeneriche.messaggio(LI.SCONOSCIUTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[8] != sconosciutoOggetto and oggetton == 9:
                        FunzioniGraficheGeneriche.messaggio(LI.BOMBA_APPICCICOSA_[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio(LI.DIM_LA_VEL_DEL_NEM_SU_CUI_VIE_LAN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 9:
                        FunzioniGraficheGeneriche.messaggio(LI.SCONOSCIUTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if imgOggetti[9] != sconosciutoOggetto and oggetton == 10:
                        FunzioniGraficheGeneriche.messaggio(LI.BOMBA_POTENZIATA_[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio(LI.INF_MOL_DAN_AI_NEM_SU_CUI_VIE_LAN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    elif oggetton == 10:
                        FunzioniGraficheGeneriche.messaggio(LI.SCONOSCIUTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                    if oggetton == 11:
                        FunzioniGraficheGeneriche.messaggio(LI.FARETRA_[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 11.5, 60)
                        FunzioniGraficheGeneriche.messaggio(LI.PER_DI_TRA_PI_FRE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 12.5, grandezzaCarettereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)

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

    GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone, GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeCanzoni, GlobalHWVar.volumeEffetti], True, posizioneCanaleMusica=0)
    return dati
