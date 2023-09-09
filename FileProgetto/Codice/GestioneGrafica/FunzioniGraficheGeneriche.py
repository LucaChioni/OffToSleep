# -*- coding: utf-8 -*-

import os
import random
import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.Localizzazione.LocalizInterfaccia as LI


def messaggio(msg, colore, x, y, gr, largezzaFoglio=-1, spazioTraLeRighe=-1, daDestra=False, centrale=False, lungMax=False, superficie=False, restituisciLarghezza=False):
    x = int(x)
    y = int(y)

    gr = gr - 10
    gr = GlobalHWVar.gpx * gr // 60
    y = y - (GlobalHWVar.gpy // 8)
    font = pygame.font.Font(GlobalHWVar.fontUtilizzato, gr)
    italic = False
    bold = False
    coloreOrig = colore
    xOrig = x

    testoComplesso = False
    if "<*>" in msg or "<br>" in msg or largezzaFoglio != -1 or spazioTraLeRighe != -1:
        testoComplesso = True

    # per mettere parti in italic, bold o colorate: "Premi <*>#bold#un<*> <*>#italic#tasto<*> per <*>#color#100,0,0#continuare<*>..."
    if daDestra:
        testo = font.render(msg, True, colore)
        dimX, dimY = font.size(msg)
        GlobalHWVar.disegnaImmagineSuSchermo(testo, (x - dimX, y))
    elif centrale:
        if "<br>" in msg and spazioTraLeRighe != -1:
            righeMsg = msg.split(" <br> ")
            i = 0
            while i < len(righeMsg):
                font.render(righeMsg[i], True, colore)
                testo = font.render(righeMsg[i], True, colore)
                dimX, dimY = font.size(righeMsg[i])
                GlobalHWVar.disegnaImmagineSuSchermo(testo, (x - (dimX // 2), y + (i * spazioTraLeRighe)))
                i += 1
        else:
            msgIniziale = msg
            font.render(msg, True, colore)
            dimX, dimY = font.size(msg)
            if lungMax and dimX > lungMax * GlobalHWVar.gpx:
                while dimX > lungMax * GlobalHWVar.gpx:
                    msg = msg[:-1]
                    font.render(msg + "...", True, colore)
                    dimX, dimY = font.size(msg)
            if msgIniziale != msg:
                msg += "..."
            testo = font.render(msg, True, colore)
            dimX, dimY = font.size(msg)
            GlobalHWVar.disegnaImmagineSuSchermo(testo, (x - (dimX // 2), y))
    elif superficie:
        testo = font.render(msg, True, colore)
        GlobalHWVar.disegnaImmagineSuSchermo(testo, (x, y), superficie=superficie)
    elif testoComplesso:
        vetMsg = msg.split("<*>")
        for text in vetMsg:
            colore = coloreOrig
            if italic or bold:
                font = pygame.font.Font(GlobalHWVar.fontUtilizzato, gr)
                italic = False
                bold = False
            if text.startswith("#italic#"):
                text = text.replace("#italic#", "")
                font = pygame.font.Font(GlobalHWVar.fontUtilizzatoItalic, gr)
                italic = True
            elif text.startswith("#bold#"):
                text = text.replace("#bold#", "")
                font = pygame.font.Font(GlobalHWVar.fontUtilizzatoBold, gr)
                bold = True
            elif text.startswith("#color#"):
                text = text.replace("#color#", "")
                coloreRgb = text.split("#")[0]
                text = text.split("#")[1]
                colore = (int(coloreRgb.split(",")[0]), int(coloreRgb.split(",")[1]), int(coloreRgb.split(",")[2]))
            vetParole = text.split(" ")
            for parola in vetParole:
                if parola != "":
                    if parola == "<br>":
                        x = xOrig
                        y += spazioTraLeRighe
                    else:
                        testo = font.render(parola, True, colore)
                        dimX, dimY = font.size(parola + " ")
                        if largezzaFoglio != -1 and x + dimX > xOrig + largezzaFoglio:
                            x = xOrig
                            if spazioTraLeRighe != 1:
                                y += spazioTraLeRighe
                            else:
                                y += dimY
                        GlobalHWVar.disegnaImmagineSuSchermo(testo, (x, y))
                        x += dimX
    else:
        testo = font.render(msg, True, colore)
        GlobalHWVar.disegnaImmagineSuSchermo(testo, (x, y))
        if restituisciLarghezza:
            dimX, dimY = font.size(msg)
            return dimX


def messaggioParlato(bottoneDown, fineDialogo, msg, colore, x, y, gr, largezzaFoglio, spazioTraLeRighe, parlante, scriviTutto=False):
    x = int(x)
    y = int(y)

    gr = gr - 10
    gr = GlobalHWVar.gpx * gr // 60
    y = y - (GlobalHWVar.gpy // 8)
    font = pygame.font.Font(GlobalHWVar.fontUtilizzato, gr)
    italic = False
    bold = False
    coloreOrig = colore
    xOrig = x
    if parlante == "m":
        suonoDialogo = GlobalSndVar.rumoreDialoghiInterlocutoriM
    elif parlante == "f":
        suonoDialogo = GlobalSndVar.rumoreDialoghiInterlocutoriF
    else:
        suonoDialogo = GlobalSndVar.rumoreDialoghiInterlocutoriN

    intervalloSuonoDialogo = 3
    vetMsg = msg.split("<*>")
    for text in vetMsg:
        if fineDialogo:
            break
        colore = coloreOrig
        if italic or bold:
            font = pygame.font.Font(GlobalHWVar.fontUtilizzato, gr)
            italic = False
            bold = False
        if text.startswith("#italic#"):
            text = text.replace("#italic#", "")
            font = pygame.font.Font(GlobalHWVar.fontUtilizzatoItalic, gr)
            italic = True
        elif text.startswith("#bold#"):
            text = text.replace("#bold#", "")
            font = pygame.font.Font(GlobalHWVar.fontUtilizzatoBold, gr)
            bold = True
        elif text.startswith("#color#"):
            text = text.replace("#color#", "")
            coloreRgb = text.split("#")[0]
            text = text.split("#")[1]
            colore = (int(coloreRgb.split(",")[0]), int(coloreRgb.split(",")[1]), int(coloreRgb.split(",")[2]))
        vetParole = text.split(" ")
        for parola in vetParole:
            if fineDialogo:
                break
            if parola != "":
                if parola == "<br>":
                    x = xOrig
                    y += spazioTraLeRighe
                else:
                    dimX, dimY = font.size(parola + " ")
                    if largezzaFoglio != -1 and x + dimX > xOrig + largezzaFoglio:
                        x = xOrig
                        if spazioTraLeRighe != 1:
                            y += spazioTraLeRighe
                        else:
                            y += dimY
                    for lettera in parola:
                        if fineDialogo:
                            break
                        bottoneDown, inutile = GestioneInput.getInput(bottoneDown, False)
                        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["Q"] or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                            fineDialogo = True
                            bottoneDown = False
                        elif bottoneDown == pygame.K_SPACE or bottoneDown == "mouseSinistro" or bottoneDown == "padCroce":
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(suonoDialogo)
                            scriviTutto = True
                            bottoneDown = False
                        if bottoneDown:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                            bottoneDown = False

                        letteraRenderizzata = font.render(lettera, True, colore)
                        GlobalHWVar.disegnaImmagineSuSchermo(letteraRenderizzata, (x, y))
                        dimX, dimY = font.size(lettera)
                        x += dimX

                        if not scriviTutto:
                            if intervalloSuonoDialogo % 3 == 0:
                                GlobalHWVar.canaleSoundPuntatoreSposta.play(suonoDialogo)
                            intervalloSuonoDialogo += 1
                            GlobalHWVar.aggiornaSchermo()
                            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                            GlobalHWVar.clockScritturaDialogo.tick(GlobalHWVar.fpsScritturaDialogo)
                    dimX, dimY = font.size(" ")
                    x += dimX

    return bottoneDown, fineDialogo


def guardaVideo(listaImg, audio, loop):
    if GlobalHWVar.mouseBloccato:
        GlobalHWVar.configuraCursore(False)
    bottoneDown = False

    # play video
    countdownInizioVideo = 10
    continua = False
    i = 0
    while i < len(listaImg) and not continua:
        if countdownInizioVideo == 0:
            if audio and i == 0:
                GlobalHWVar.canaleSoundCanzone.play(audio)
            GlobalHWVar.disegnaImmagineSuSchermo(listaImg[i], (0, 0))
            GlobalHWVar.aggiornaSchermo()

        # gestione degli input
        bottoneDown, inutile = GestioneInput.getInput(bottoneDown, False)
        if bottoneDown:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
            continua = True
            bottoneDown = False

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockVideo.tick(GlobalHWVar.fpsVideo)
        if countdownInizioVideo > 0:
            countdownInizioVideo -= 1
        else:
            i += 1
            if loop and i == len(listaImg):
                i = 0

    # oscura lo schermo
    # oscuraIlluminaSchermo(illumina=False)


def controllaMorteRallo(vitaRallo, pvtot, numFrecce, avvele, attp, difp, inizio, gameover, caricaSalvataggio, riavviaAudioMusica, riavviaAudioAmbiente, avanzamentoStoria):
    if vitaRallo <= 0:
        if GlobalHWVar.mouseBloccato:
            GlobalHWVar.configuraCursore(False)

        if GlobalHWVar.canaleSoundCanzone.get_busy():
            riavviaAudioMusica = True
        if GlobalHWVar.canaliSoundSottofondoAmbientale.getBusy():
            riavviaAudioAmbiente = True
        GlobalHWVar.canaleSoundPuntatoreSposta.stop()
        GlobalHWVar.canaleSoundPuntatoreSeleziona.stop()
        GlobalHWVar.canaleSoundPassiRallo.stop()
        GlobalHWVar.canaleSoundPassiColco.stop()
        GlobalHWVar.canaleSoundPassiNemici.stop()
        GlobalHWVar.canaleSoundPassiPersonaggi.stop()
        GlobalHWVar.canaleSoundMorteNemici.stop()
        GlobalHWVar.canaleSoundLvUp.stop()
        GlobalHWVar.canaleSoundInterazioni.stop()
        GlobalHWVar.canaleSoundAttacco.stop()
        GlobalHWVar.canaleSoundMelodieEventi.stop()
        GlobalHWVar.canaleSoundBattitoCardiaco.stop()
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone, GlobalHWVar.canaliSoundSottofondoAmbientale], [0, 0], False, posizioneCanaleMusica=0)
        GlobalHWVar.canaleSoundCanzone.stop()
        GlobalHWVar.canaliSoundSottofondoAmbientale.arresta()
        GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
        GlobalHWVar.canaliSoundSottofondoAmbientale.settaVolume(GlobalHWVar.volumeEffetti)

        disegnaVitaRallo(vitaRallo, pvtot, numFrecce, avvele, attp, difp, avanzamentoStoria)
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreMorte)
        oscuraIlluminaSchermo(illumina=False, tipoOscuramento=2)

        messaggio(LI.SEI_MORTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6.3, 150, centrale=True)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (GlobalHWVar.gsx // 32 * 4.5, GlobalHWVar.gsy // 18 * 8.8), (GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 8.8), 1)
        messaggio(LI.CONTINUA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.9, GlobalHWVar.gsy // 18 * 9.8, 90)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 16), int(GlobalHWVar.gpy * 9.3)), (int(GlobalHWVar.gpx * 16), int(GlobalHWVar.gpy * 11.6)), 1)
        messaggio(LI.CARICA_PARTITA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17.1, GlobalHWVar.gsy // 18 * 9.8, 90)
        GlobalHWVar.aggiornaSchermo()

        schermo_temp = GlobalHWVar.schermo.copy()
        backgroundUpdate = schermo_temp.subsurface(pygame.Rect(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 3)).convert()

        puntatore = GlobalImgVar.puntatore
        xp = GlobalHWVar.gsx // 32 * 9.2
        yp = GlobalHWVar.gsy // 18 * 10.2

        primoFrame = True
        tastotempfps = 8
        voceMarcata = 1

        bottoneDown = False
        while True:
            # rallenta per i 30 fps
            if tastotempfps != 0 and bottoneDown:
                tastotempfps -= 1
            elif tastotempfps == 0 and bottoneDown:
                tastotempfps = 2

            voceMarcataVecchia = voceMarcata
            xMouse, yMouse = pygame.mouse.get_pos()
            if GlobalHWVar.mouseVisibile:
                if GlobalHWVar.gsy // 18 * 8.8 <= yMouse <= GlobalHWVar.gsy // 18 * 12:
                    if GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 16:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalHWVar.gsx // 32 * 9.2
                        yp = GlobalHWVar.gsy // 18 * 10.2
                    elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 25:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalHWVar.gsx // 32 * 16.4
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
            bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, False)
            if bottoneDownVecchio != bottoneDown:
                primoMovimento = True
                tastotempfps = 8
            if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
                if voceMarcata == 1:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    gameover = True
                    break
                elif voceMarcata == 2:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    oscuraIlluminaSchermo(illumina=False)
                    caricaSalvataggio = GlobalGameVar.numSalvataggioCaricato
                    break
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

            if primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata:
                primoFrame = False
                if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["A"] or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                    if voceMarcata == 2:
                        voceMarcata -= 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 9.2
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        bottoneDown = False
                if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["D"] or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                    if voceMarcata == 1:
                        voceMarcata += 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 16.4
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        bottoneDown = False
                if not primoMovimento and tastoMovimentoPremuto:
                    tastotempfps = 2

                GlobalHWVar.disegnaImmagineSuSchermo(backgroundUpdate, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9))
                GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
                GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
        inizio = True

    return inizio, gameover, caricaSalvataggio, riavviaAudioMusica, riavviaAudioAmbiente


def disegnaRallo(avanzamentoStoria, npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti, inMovimento=False, frame=False, attaccoRavvicinato=False, attaccoDaLontano=False, difesa=False):
    mostraArmatura = True
    if GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] or \
            GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"] or \
            GlobalGameVar.dictAvanzamentoStoria["inizioSognoCasaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCasaDavid"] or \
            GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"] or \
            GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
        mostraArmatura = False

    # personaggio: 1=d, 2=a, 3=w, 4=s
    if difesa:
        GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y))
        if mostraArmatura:
            GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
        GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
        if avvele:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
        if mostraArmatura:
            GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
        GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persmbDifesa, (x, y))
        GlobalHWVar.disegnaImmagineSuSchermo(arma, (x, y))
        GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
        GlobalHWVar.disegnaImmagineSuSchermo(scudo, (x, y))
    elif attaccoDaLontano:
        if npers == 1:
            GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            if mostraArmatura:
                GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            if mostraArmatura:
                GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persdmbAttacco, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
        if npers == 2:
            GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            if mostraArmatura:
                GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            if mostraArmatura:
                GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persambAttacco, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x - GlobalHWVar.gpx, y))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
        if npers == 3:
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y - GlobalHWVar.gpy))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perswmbAttacco, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            if mostraArmatura:
                GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            if mostraArmatura:
                GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
        if npers == 4:
            if mostraArmatura:
                GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            if mostraArmatura:
                GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssmbAttacco, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
    else:
        if npers == 1:
            GlobalHWVar.disegnaImmagineSuSchermo(scudo, (x, y))
            if inMovimento:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persdm, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            if mostraArmatura:
                GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            if mostraArmatura:
                GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y))
            if attaccoRavvicinato:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persdmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persdmb1, (x, y))
                elif frame == 2:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persdmb2, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persdb, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arma, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
        if npers == 2:
            if attaccoRavvicinato:
                GlobalHWVar.disegnaImmagineSuSchermo(arma, (x - GlobalHWVar.gpx, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(arma, (x, y))
            if inMovimento:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persam, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            if mostraArmatura:
                GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            if mostraArmatura:
                GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y))
            if attaccoRavvicinato:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persambAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persamb1, (x, y))
                elif frame == 2:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persamb2, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persab, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(scudo, (x, y))
        if npers == 3:
            if attaccoRavvicinato:
                GlobalHWVar.disegnaImmagineSuSchermo(arma, (x, y - GlobalHWVar.gpy))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(arma, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(scudo, (x, y))
            if attaccoRavvicinato:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perswmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perswmb1, (x, y))
                elif frame == 2:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perswmb2, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perswb, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
            if inMovimento:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perswm, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            if mostraArmatura:
                GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            if mostraArmatura:
                GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y))
        if npers == 4:
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y))
            if mostraArmatura:
                GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            if inMovimento:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssm, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            if mostraArmatura:
                GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            if attaccoRavvicinato:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssmbAttacco, (x, y))
            elif inMovimento:
                if frame == 1:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssmb1, (x, y))
                elif frame == 2:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssmb2, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssb, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arma, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(scudo, (x, y))


def animaOggettoSpecialeRicevuto(oggettoRicevuto):
    if GlobalHWVar.mouseBloccato:
        GlobalHWVar.configuraCursore(False)
    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoRaccoltaOggetto)
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfocontcof, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 0))
    messaggio(LI.HAI_OTT_[GlobalHWVar.linguaImpostata] + oggettoRicevuto, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
    GlobalHWVar.aggiornaSchermo()
    i = 0
    while i < 5:
        pygame.time.wait(100)
        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        i += 1
    bottoneDown = False
    risposta = False
    while not risposta:
        # gestione degli input
        bottoneDown, inutile = GestioneInput.getInput(bottoneDown, False)
        if bottoneDown == pygame.K_SPACE or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["Q"] or bottoneDown == "mouseSinistro" or bottoneDown == "mouseDestro" or bottoneDown == "padCroce" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
            risposta = True
            bottoneDown = False
        if bottoneDown:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def disegnaOmbreggiaturaNellaCasellaSpecifica(x, y):
    if ((x / GlobalHWVar.gpx) + (y / GlobalHWVar.gpy)) % 2 == 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.casellaChiara, (x, y))
    if ((x / GlobalHWVar.gpx) + (y / GlobalHWVar.gpy)) % 2 == 1:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.casellaScura, (x, y))


def oscuraIlluminaSchermo(illumina, tipoOscuramento=1, imgIlluminata=False):
    if not imgIlluminata:
        imgIlluminata = []

    # se "screen" è False oscura lo schermo
    if not illumina:
        rect = pygame.display.get_surface().get_rect()
        image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
        if tipoOscuramento == 1:
            image.fill((0, 0, 0, 100))
            image = image.convert_alpha(GlobalHWVar.schermo)
            i = 0
            while i <= 5:
                GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
                if imgIlluminata:
                    GlobalHWVar.disegnaImmagineSuSchermo(imgIlluminata[0], imgIlluminata[1])
                GlobalHWVar.aggiornaSchermo()
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                i += 1
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
            GlobalHWVar.aggiornaSchermo()
        elif tipoOscuramento == 2:
            image.fill((0, 0, 0, 8))
            image = image.convert_alpha(GlobalHWVar.schermo)
            i = 0
            while i <= 30:
                if i % 2 == 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
                    if imgIlluminata:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgIlluminata[0], imgIlluminata[1])
                    GlobalHWVar.aggiornaSchermo()
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                i += 1
        elif tipoOscuramento == 3:
            image.fill((0, 0, 0, 100))
            image = image.convert_alpha(GlobalHWVar.schermo)
            i = 0
            while i <= 3:
                GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
                if imgIlluminata:
                    GlobalHWVar.disegnaImmagineSuSchermo(imgIlluminata[0], imgIlluminata[1])
                GlobalHWVar.aggiornaSchermo()
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                i += 1
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
            GlobalHWVar.aggiornaSchermo()
        elif tipoOscuramento == 4:
            image.fill((0, 0, 0, 25))
            image = image.convert_alpha(GlobalHWVar.schermo)
            i = 0
            while i <= 6:
                GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
                if imgIlluminata:
                    GlobalHWVar.disegnaImmagineSuSchermo(imgIlluminata[0], imgIlluminata[1])
                GlobalHWVar.aggiornaSchermo()
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                i += 1
            GlobalHWVar.aggiornaSchermo()
        elif tipoOscuramento == 5:
            image.fill((0, 0, 0, 30))
            image = image.convert_alpha(GlobalHWVar.schermo)
            i = 0
            while i <= 50:
                if i % 2 == 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
                    if imgIlluminata:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgIlluminata[0], imgIlluminata[1])
                    GlobalHWVar.aggiornaSchermo()
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                i += 1
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
    else:
        screen = GlobalHWVar.schermo.copy().convert()
        rect = pygame.display.get_surface().get_rect()
        vetImg = []
        if illumina == 1:
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 200))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 150))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 100))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 50))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            i = 0
            while i <= 3:
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(vetImg[i], (0, 0))
                GlobalHWVar.aggiornaSchermo()
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                i += 1
        elif illumina == 2:
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 250))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 200))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 150))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 100))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 60))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, 20))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            i = 0
            while i <= 5:
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(vetImg[i], (0, 0))
                GlobalHWVar.aggiornaSchermo()
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                i += 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        GlobalHWVar.aggiornaSchermo()


def animaEvento(pathImgs, coordinateImgAnimata, dimensioniImgAnimata, listaAudio, tuttoSchermo=False, battito=-1):
    casellaVuotaPreset = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
    screen = False
    if tuttoSchermo:
        screen = GlobalHWVar.schermo.copy().convert()
    dimX, dimY = dimensioniImgAnimata
    vetImgAnimazione = []
    numImgAnimazione = 0
    if pathImgs:
        listaImg = os.listdir(GlobalHWVar.gamePath + pathImgs)
        for img in listaImg:
            numImg = int(img[3:-4])
            if numImg > numImgAnimazione:
                numImgAnimazione = numImg
    ultimaImgAnimazione = casellaVuotaPreset
    i = 1
    while i <= numImgAnimazione:
        aumenteRisoluzione = True
        if tuttoSchermo:
            aumenteRisoluzione = False
        if os.path.exists(GlobalHWVar.gamePath + pathImgs + "img" + str(i) + ".png"):
            ultimaImgAnimazione = CaricaFileProgetto.loadImage(pathImgs + "img" + str(i) + ".png", dimX, dimY, aumenteRisoluzione)
        vetImgAnimazione.append(ultimaImgAnimazione)
        i += 1
    # metto i suoni marcati con "-1" nell'ultimo frame dell'animazione
    i = 0
    while i < len(listaAudio):
        if listaAudio[i] == -1:
            listaAudio[i] = len(vetImgAnimazione) - 1
        i += 2

    # animazione effettiva
    numFrameAttuale = 0
    while len(vetImgAnimazione) > 0:
        if battito > -1 and battito == numFrameAttuale:
            if not GlobalHWVar.canaleSoundBattitoCardiaco.get_busy():
                GlobalHWVar.canaleSoundBattitoCardiaco.play(GlobalSndVar.rumoreBattitoCardiaco, -1)
            else:
                GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundBattitoCardiaco], [0], False, posizioneCanaleMusica=0)
                GlobalHWVar.canaleSoundBattitoCardiaco.stop()
                GlobalHWVar.canaleSoundBattitoCardiaco.set_volume(GlobalHWVar.volumeEffetti)
        if len(listaAudio) > 0 and listaAudio[0] == numFrameAttuale:
            GlobalHWVar.canaleSoundInterazioni.play(listaAudio[1])
            del listaAudio[1]
            del listaAudio[0]
        if tuttoSchermo:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(vetImgAnimazione.pop(0), coordinateImgAnimata)

        GlobalHWVar.aggiornaSchermo()
        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        if tuttoSchermo:
            GlobalHWVar.clockAnimazioni.tick(GlobalHWVar.fpsVideo)
        else:
            GlobalHWVar.clockAnimazioni.tick(GlobalHWVar.fpsAnimazioni)
        numFrameAttuale += 1


def disegnaVitaRallo(pv, pvtot, numFrecce, avvele, attp, difp, avanzamentoStoria):
    lungvitatot = int(((GlobalHWVar.gpx * pvtot) / float(4)) // 5)
    lungvita = (lungvitatot * pv) // pvtot
    if lungvita < 0:
        lungvita = 0

    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoRallo, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perss, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssb, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgNumFrecce, (int(GlobalHWVar.gsx // 32 * 1.1), GlobalHWVar.gsy // 18 * 17))
    if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
        numFrecce = 0
    messaggio(u" ×" + str(numFrecce), GlobalHWVar.grigiochi, int(GlobalHWVar.gsx // 32 * 1.7), int(GlobalHWVar.gsy // 18 * 17.23), 40)
    if avvele:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.avvelenato, (GlobalHWVar.gsx // 32 * 3.1, GlobalHWVar.gsy // 18 * 17))
    if attp > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.attaccopiu, (GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 17))
    if difp > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.difesapiu, (GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 17))
    yInizioBarra = int((GlobalHWVar.gpy * 17) + (GlobalHWVar.gpy * 0.75))
    yInizioVita = int((GlobalHWVar.gpy * 17) + (GlobalHWVar.gpy * 0.8))
    yFineVita = int((GlobalHWVar.gpy * 17) + (GlobalHWVar.gpy * 0.8) + (GlobalHWVar.gpy * 0.15))
    yFineBarra = GlobalHWVar.gsy
    if abs(yInizioBarra - yInizioVita) != abs(yFineVita - yFineBarra):
        if abs(yInizioBarra - yInizioVita) < abs(yFineVita - yFineBarra):
            yInizioVita += 1
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx, yInizioBarra, lungvitatot + (GlobalHWVar.gpx * 0.1), GlobalHWVar.gpy // 2))
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gpx, yInizioVita, lungvitatot, GlobalHWVar.gpy * 0.15))
    if lungvita > 0:
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.verdeVita, (GlobalHWVar.gpx, yInizioVita, lungvita, GlobalHWVar.gpy * 0.15))
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx + lungvita, yInizioVita, GlobalHWVar.gpx * 0.05, GlobalHWVar.gpy * 0.15))

    if GlobalGameVar.datiAnimazioniDanniInflitti["dannoRallo"][1] != 0 and GlobalGameVar.datiAnimazioniDanniInflitti["dannoRallo"][2] > 0:
        colore = GlobalHWVar.bianco
        valore = 0
        if GlobalGameVar.datiAnimazioniDanniInflitti["dannoRallo"][0] == "danno":
            colore = GlobalHWVar.rosso
            valore = GlobalGameVar.datiAnimazioniDanniInflitti["dannoRallo"][1]
        elif GlobalGameVar.datiAnimazioniDanniInflitti["dannoRallo"][0] == "cura":
            colore = GlobalHWVar.verde
            valore = GlobalGameVar.datiAnimazioniDanniInflitti["dannoRallo"][1]
        elif GlobalGameVar.datiAnimazioniDanniInflitti["dannoRallo"][0] == "veleno":
            colore = GlobalHWVar.violaVeleno
            valore = GlobalGameVar.datiAnimazioniDanniInflitti["dannoRallo"][1]
        if valore > 9999:
            valore = 9999
        elif valore < -9999:
            valore = -9999
        if valore > 0:
            valore = "+" + str(valore)
        elif valore < 0:
            valore = str(valore)

        messaggio(valore, colore, GlobalHWVar.gpx * 6.97, GlobalHWVar.gpy * 17.13, 50, centrale=True)


def disegnaVitaColco(entot, enrob, surrisc, velp, effp):
    lungentot = int(((GlobalHWVar.gpx * entot) / float(4)) // 14)
    lungen = int(((GlobalHWVar.gpx * enrob) / float(4)) // 14)
    if lungen < 0:
        lungen = 0

    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoColco, (0, 0))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robos, (0, 0))
    if surrisc > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.surriscaldato, (GlobalHWVar.gpx + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
    if velp > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.velocitapiu, ((GlobalHWVar.gpx * 2) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
    if effp > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.efficienzapiu, ((GlobalHWVar.gpx * 3) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
    yInizioBarra = 0
    yInizioVita = int(GlobalHWVar.gpy * 0.05)
    yFineVita = int((GlobalHWVar.gpy * 0.05) + (GlobalHWVar.gpy * 0.15))
    yFineBarra = int(GlobalHWVar.gpy * 0.25)
    if abs(yInizioBarra - yInizioVita) != abs(yFineVita - yFineBarra):
        if abs(yInizioBarra - yInizioVita) < abs(yFineVita - yFineBarra):
            yInizioVita += 1
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx, yInizioBarra, lungentot + (GlobalHWVar.gpx * 0.1), GlobalHWVar.gpy * 0.25))
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gpx, yInizioVita, lungentot, GlobalHWVar.gpy * 0.15))
    if lungen > 0:
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.azzurroVitaColco, (GlobalHWVar.gpx, yInizioVita, lungen, GlobalHWVar.gpy * 0.15))
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx + lungen, yInizioVita, GlobalHWVar.gpx * 0.05, GlobalHWVar.gpy * 0.15))

    if GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"][1] != 0 and GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"][2] > 0:
        colore = GlobalHWVar.bianco
        valore = 0
        if GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"][0] == "danno":
            colore = GlobalHWVar.rosso
            valore = GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"][1]
        elif GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"][0] == "surriscaldamento":
            colore = GlobalHWVar.rossoSurriscaldamento
            valore = GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"][1]
        elif GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"][0] == "cura":
            colore = GlobalHWVar.azzurro
            valore = GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"][1]
        elif GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"][0] == "consumo":
            colore = GlobalHWVar.grigiochiarino
            valore = GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"][1]
        if valore > 9999:
            valore = 9999
        elif valore < -9999:
            valore = -9999
        if valore > 0:
            valore = "+" + str(valore)
        elif valore < 0:
            valore = str(valore)

        messaggio(valore, colore, GlobalHWVar.gpx * 4.98, GlobalHWVar.gpy * 0.36, 50, centrale=True)


def disegnaVitaEsche(pvEsca):
    lungvitatot = int(((GlobalHWVar.gpx * GlobalGameVar.vitaTotEsche) / float(4)) // 5)
    lungvita = int(((GlobalHWVar.gpx * pvEsca) / float(4)) // 5)
    if lungvita < 0:
        lungvita = 0

    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoEsche, (0, 0))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.esche, (0, 0))
    yInizioBarra = 0
    yInizioVita = int(GlobalHWVar.gpy * 0.05)
    yFineVita = int((GlobalHWVar.gpy * 0.05) + (GlobalHWVar.gpy * 0.15))
    yFineBarra = int(GlobalHWVar.gpy * 0.25)
    if abs(yInizioBarra - yInizioVita) != abs(yFineVita - yFineBarra):
        if abs(yInizioBarra - yInizioVita) < abs(yFineVita - yFineBarra):
            yInizioVita += 1
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx, yInizioBarra, lungvitatot + (GlobalHWVar.gpx * 0.1), GlobalHWVar.gpy * 0.25))
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gpx, yInizioVita, lungvitatot, GlobalHWVar.gpy * 0.15))
    if lungvita > 0:
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.verdeVita, (GlobalHWVar.gpx, yInizioVita, lungvita, GlobalHWVar.gpy * 0.15))
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx + lungvita, yInizioVita, GlobalHWVar.gpx * 0.05, GlobalHWVar.gpy * 0.15))

    if GlobalGameVar.datiAnimazioniDanniInflitti["dannoEsche"][1] != 0 and GlobalGameVar.datiAnimazioniDanniInflitti["dannoEsche"][2] > 0:
        colore = GlobalHWVar.bianco
        valore = 0
        if GlobalGameVar.datiAnimazioniDanniInflitti["dannoEsche"][0] == "danno":
            colore = GlobalHWVar.rosso
            valore = GlobalGameVar.datiAnimazioniDanniInflitti["dannoEsche"][1]
        if valore < -9999:
            valore = -9999
        valore = str(valore)

        messaggio(valore, colore, GlobalHWVar.gpx * 1.98, GlobalHWVar.gpy * 0.36, 50, centrale=True)


def disegnaVitaNemici(pvm, pvmtot, nemicoAvvelenato, nemicoAppiccicato, immagineS):
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoMostro, (0, 0))
    if nemicoAvvelenato:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.avvelenato, (GlobalHWVar.gpx + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
    if nemicoAppiccicato:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.appiccicoso, ((GlobalHWVar.gpx * 2) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
    GlobalHWVar.disegnaImmagineSuSchermo(immagineS, (0, 0))

    if pvmtot > 500:
        lungvitatot = int(((GlobalHWVar.gpx * 500) / float(4)) // 5)
        if pvm > 2500:
            pvm = 500
            coloreVita = (120, 50, 120)
            coloreVitaSuccessiva = (180, 50, 70)
        elif pvm > 2000:
            pvm -= 2000
            coloreVita = (120, 50, 120)
            coloreVitaSuccessiva = (180, 50, 70)
        elif pvm > 1500:
            pvm -= 1500
            coloreVita = (180, 50, 70)
            coloreVitaSuccessiva = (170, 110, 50)
        elif pvm > 1000:
            pvm -= 1000
            coloreVita = (170, 110, 50)
            coloreVitaSuccessiva = (170, 160, 40)
        elif pvm > 500:
            pvm -= 500
            coloreVita = (170, 160, 40)
            coloreVitaSuccessiva = (80, 180, 80)
        else:
            coloreVita = (80, 180, 80)
            coloreVitaSuccessiva = (80, 80, 80)
    else:
        lungvitatot = int(((GlobalHWVar.gpx * pvmtot) / float(4)) // 5)
        coloreVita = (80, 180, 80)
        coloreVitaSuccessiva = (80, 80, 80)

    lungvita = int(((GlobalHWVar.gpx * pvm) / float(4)) // 5)
    if lungvita < 0:
        lungvita = 0

    yInizioBarra = 0
    yInizioVita = int(GlobalHWVar.gpy * 0.05)
    yFineVita = int((GlobalHWVar.gpy * 0.05) + (GlobalHWVar.gpy * 0.15))
    yFineBarra = int(GlobalHWVar.gpy * 0.25)
    if abs(yInizioBarra - yInizioVita) != abs(yFineVita - yFineBarra):
        if abs(yInizioBarra - yInizioVita) < abs(yFineVita - yFineBarra):
            yInizioVita += 1
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx, yInizioBarra, lungvitatot + (GlobalHWVar.gpx * 0.1), GlobalHWVar.gpy * 0.25))
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gpx, yInizioVita, lungvitatot, GlobalHWVar.gpy * 0.15))
    if lungvita > 0:
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, coloreVitaSuccessiva, (GlobalHWVar.gpx, yInizioVita, lungvitatot, GlobalHWVar.gpy * 0.15))
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, coloreVita, (GlobalHWVar.gpx, yInizioVita, lungvita, GlobalHWVar.gpy * 0.15))
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx + lungvita, yInizioVita, GlobalHWVar.gpx * 0.05, GlobalHWVar.gpy * 0.15))

    if GlobalGameVar.datiAnimazioniDanniInflitti["dannoNemico"][1] != 0 and GlobalGameVar.datiAnimazioniDanniInflitti["dannoNemico"][2] > 0:
        colore = GlobalHWVar.bianco
        valore = 0
        if GlobalGameVar.datiAnimazioniDanniInflitti["dannoNemico"][0] == "danno":
            colore = GlobalHWVar.rosso
            valore = GlobalGameVar.datiAnimazioniDanniInflitti["dannoNemico"][1]
        elif GlobalGameVar.datiAnimazioniDanniInflitti["dannoNemico"][0] == "cura":
            colore = GlobalHWVar.verde
            valore = GlobalGameVar.datiAnimazioniDanniInflitti["dannoNemico"][1]
        elif GlobalGameVar.datiAnimazioniDanniInflitti["dannoNemico"][0] == "veleno":
            colore = GlobalHWVar.violaVeleno
            valore = GlobalGameVar.datiAnimazioniDanniInflitti["dannoNemico"][1]
        if valore > 9999:
            valore = 9999
        elif valore < -9999:
            valore = -9999
        if valore > 0:
            valore = "+" + str(valore)
        elif valore < 0:
            valore = str(valore)

        messaggio(valore, colore, GlobalHWVar.gpx * 3.98, GlobalHWVar.gpy * 0.36, 50, centrale=True)


def aggiornaBarreStatusPerValoriDanniCureScaduti(dati, pvtot, nemicoInquadrato, entot, vettoreEsche, turnoAvanzato):
    aggiornaVitaRallo = False
    aggiornaVitaImpo = False
    aggiornaVitaEsca = False
    aggiornaVitaNemico = False
    # cancello i danni dei turni vecchi
    if turnoAvanzato and GlobalGameVar.datiAnimazioniDanniInflitti["dannoRallo"][2] < GlobalGameVar.datiAnimazioniDanniInflitti["tempoAnimazione"] and GlobalGameVar.datiAnimazioniDanniInflitti["dannoRallo"][0]:
        GlobalGameVar.datiAnimazioniDanniInflitti["dannoRallo"] = [False, 0, -1]
        aggiornaVitaRallo = True
    if turnoAvanzato and GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"][2] < GlobalGameVar.datiAnimazioniDanniInflitti["tempoAnimazione"] and GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"][0]:
        GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"] = [False, 0, -1]
        aggiornaVitaImpo = True
    if turnoAvanzato and GlobalGameVar.datiAnimazioniDanniInflitti["dannoEsche"][2] < GlobalGameVar.datiAnimazioniDanniInflitti["tempoAnimazione"] and GlobalGameVar.datiAnimazioniDanniInflitti["dannoEsche"][0]:
        GlobalGameVar.datiAnimazioniDanniInflitti["dannoEsche"] = [False, 0, -1]
        aggiornaVitaEsca = True
    if turnoAvanzato and GlobalGameVar.datiAnimazioniDanniInflitti["dannoNemico"][2] < GlobalGameVar.datiAnimazioniDanniInflitti["tempoAnimazione"] and GlobalGameVar.datiAnimazioniDanniInflitti["dannoNemico"][0]:
        GlobalGameVar.datiAnimazioniDanniInflitti["dannoNemico"] = [False, 0, -1]
        aggiornaVitaNemico = True

    if GlobalGameVar.datiAnimazioniDanniInflitti["dannoRallo"][2] >= 0:
        GlobalGameVar.datiAnimazioniDanniInflitti["dannoRallo"][2] -= 1
        aggiornaVitaRallo = True
    if GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"][2] >= 0:
        GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"][2] -= 1
        aggiornaVitaImpo = True
    if GlobalGameVar.datiAnimazioniDanniInflitti["dannoEsche"][2] >= 0:
        GlobalGameVar.datiAnimazioniDanniInflitti["dannoEsche"][2] -= 1
        aggiornaVitaEsca = True
    if GlobalGameVar.datiAnimazioniDanniInflitti["dannoNemico"][2] >= 0:
        GlobalGameVar.datiAnimazioniDanniInflitti["dannoNemico"][2] -= 1
        aggiornaVitaNemico = True

    if GlobalGameVar.datiAnimazioniDanniInflitti["dannoRallo"][2] < 0 and aggiornaVitaRallo:
        disegnaVitaRallo(dati[5], pvtot, dati[132], dati[121], dati[123], dati[124], dati[0])
        GlobalHWVar.aggiornaSchermo()
    if (type(nemicoInquadrato) is str and nemicoInquadrato == "Colco") or (not nemicoInquadrato and GlobalGameVar.impoPresente):
        if GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"][2] < 0 and aggiornaVitaImpo:
            disegnaVitaColco(entot, dati[10], dati[122], dati[125], dati[126])
            GlobalHWVar.aggiornaSchermo()
    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
        if GlobalGameVar.datiAnimazioniDanniInflitti["dannoEsche"][2] < 0 and aggiornaVitaEsca:
            idEscaInquadrata = int(nemicoInquadrato[4:])
            i = 0
            while i < len(vettoreEsche):
                if idEscaInquadrata == vettoreEsche[i]:
                    disegnaVitaEsche(vettoreEsche[i + 1])
                    GlobalHWVar.aggiornaSchermo()
                    break
                i += 4
    elif nemicoInquadrato and not type(nemicoInquadrato) is str:
        if GlobalGameVar.datiAnimazioniDanniInflitti["dannoNemico"][2] < 0 and aggiornaVitaNemico:
            disegnaVitaNemici(nemicoInquadrato.vita, nemicoInquadrato.vitaTotale, nemicoInquadrato.avvelenato, nemicoInquadrato.appiccicato, nemicoInquadrato.imgS)
            GlobalHWVar.aggiornaSchermo()


def mostraSchermataCitazione():
    i = 0
    while i < 10:
        pygame.time.wait(100)
        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        i += 1
    GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
    messaggio(LI.A_NOI_UOM_NAS__TOC_UN_TRI_PRI_QUE_DI_SEN_VIV_CON_LA_BEL_ILL_DI_PRE_COM_UNA_REA_FUO_DI_NOI_QUE_NOS_INT_SEN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 8, 60, largezzaFoglio=GlobalHWVar.gpx * 22, spazioTraLeRighe=GlobalHWVar.gpy * 1)
    oscuraIlluminaSchermo(illumina=2)

    if GlobalHWVar.mouseBloccato:
        GlobalHWVar.configuraCursore(False)
    risposta = False
    bottoneDown = False
    mostratoAutore = False
    while not risposta:
        # gestione degli input
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, False)
        if bottoneDown:
            bottoneDown = False
            if not mostratoAutore:
                blackImage = pygame.Surface((GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 2))
                blackImage.fill((0, 0, 0))
                rect = pygame.display.get_surface().get_rect()
                vetImg = []
                image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
                image.fill((0, 0, 0, 250))
                vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
                image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
                image.fill((0, 0, 0, 200))
                vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
                image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
                image.fill((0, 0, 0, 150))
                vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
                image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
                image.fill((0, 0, 0, 100))
                vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
                image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
                image.fill((0, 0, 0, 60))
                vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
                image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
                image.fill((0, 0, 0, 20))
                vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
                i = 0
                while i <= 5:
                    GlobalHWVar.disegnaImmagineSuSchermo(blackImage, (GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 11.5))
                    messaggio(LI._LUI_PIR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 12, 50, daDestra=True)
                    GlobalHWVar.disegnaImmagineSuSchermo(vetImg[i], (GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 11.5))
                    GlobalHWVar.aggiornaSchermo()
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                    i += 1
                GlobalHWVar.disegnaImmagineSuSchermo(blackImage, (GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 11.5))
                messaggio(LI._LUI_PIR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 12, 50, daDestra=True)
                GlobalHWVar.aggiornaSchermo()
                mostratoAutore = True
            else:
                risposta = True

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)

    oscuraIlluminaSchermo(illumina=False)
    i = 0
    while i < 10:
        pygame.time.wait(100)
        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        i += 1


def animaTremolioSchermo(nelVulcano=False):
    rect = pygame.display.get_surface().get_rect()
    oscuramento = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    oscuramento.fill((0, 0, 0, 100))
    oscuramento = oscuramento.convert_alpha(GlobalHWVar.schermo)

    schermoOriginale = GlobalHWVar.schermo.copy().convert()
    if not nelVulcano:
        i = 50
        while i > 0:
            apprI = int(i // 5)
            n = random.randint(-apprI, apprI) / 20.0
            m = random.randint(-apprI, apprI) / 20.0
            GlobalHWVar.disegnaImmagineSuSchermo(oscuramento, (0, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(schermoOriginale, (GlobalHWVar.gpx * n, GlobalHWVar.gpy * m))
            GlobalHWVar.aggiornaSchermo()
            pygame.time.wait(20)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i -= 1
        GlobalHWVar.disegnaImmagineSuSchermo(schermoOriginale, (0, 0))
        GlobalHWVar.aggiornaSchermo()
    elif nelVulcano == 1:
        # oscuro anche lo schermo con marrone-sabbia
        oscuramentoSabbia = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
        oscuramentoSabbia.fill((79, 43, 38, 0))
        oscuramentoSabbia = oscuramentoSabbia.convert_alpha(GlobalHWVar.schermo)
        i = 0
        while i <= 50:
            apprI = int(i // 5)
            n = random.randint(-apprI, apprI) / 20.0
            m = random.randint(-apprI, apprI) / 20.0
            GlobalHWVar.disegnaImmagineSuSchermo(oscuramento, (0, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(schermoOriginale, (GlobalHWVar.gpx * n, GlobalHWVar.gpy * m))
            oscuramentoSabbia.fill((79, 43, 38, i * 4))
            GlobalHWVar.disegnaImmagineSuSchermo(oscuramentoSabbia, (GlobalHWVar.gpx * n, GlobalHWVar.gpy * m))
            GlobalHWVar.aggiornaSchermo(ignoraBloccoAggiornamento=True)
            pygame.time.wait(20)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.disegnaImmagineSuSchermo(schermoOriginale, (0, 0))
        oscuramentoSabbia.fill((79, 43, 38, 200))
        GlobalHWVar.disegnaImmagineSuSchermo(oscuramentoSabbia, (0, 0))
        GlobalHWVar.aggiornaSchermo(ignoraBloccoAggiornamento=True)
    elif nelVulcano == 2:
        # oscuro anche lo schermo con marrone-sabbia
        oscuramentoSabbia = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
        oscuramentoSabbia.fill((79, 43, 38, 200))
        oscuramentoSabbia = oscuramentoSabbia.convert_alpha(GlobalHWVar.schermo)
        i = 0
        while i <= 10:
            apprI = int(50 // 5)
            n = random.randint(-apprI, apprI) / 20.0
            m = random.randint(-apprI, apprI) / 20.0
            GlobalHWVar.disegnaImmagineSuSchermo(oscuramento, (0, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(schermoOriginale, (GlobalHWVar.gpx * n, GlobalHWVar.gpy * m))
            GlobalHWVar.disegnaImmagineSuSchermo(oscuramentoSabbia, (GlobalHWVar.gpx * n, GlobalHWVar.gpy * m))
            GlobalHWVar.aggiornaSchermo(ignoraBloccoAggiornamento=True)
            pygame.time.wait(20)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.disegnaImmagineSuSchermo(schermoOriginale, (0, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(oscuramentoSabbia, (0, 0))
        GlobalHWVar.aggiornaSchermo(ignoraBloccoAggiornamento=True)
    elif nelVulcano == 3:
        # oscuro anche lo schermo con marrone-sabbia
        oscuramentoSabbia = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
        oscuramentoSabbia.fill((79, 43, 38, 200))
        oscuramentoSabbia = oscuramentoSabbia.convert_alpha(GlobalHWVar.schermo)
        i = 50
        while i > 0:
            apprI = int(i // 5)
            n = random.randint(-apprI, apprI) / 20.0
            m = random.randint(-apprI, apprI) / 20.0
            GlobalHWVar.disegnaImmagineSuSchermo(oscuramento, (0, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(schermoOriginale, (GlobalHWVar.gpx * n, GlobalHWVar.gpy * m))
            oscuramentoSabbia.fill((79, 43, 38, i * 4))
            GlobalHWVar.disegnaImmagineSuSchermo(oscuramentoSabbia, (GlobalHWVar.gpx * n, GlobalHWVar.gpy * m))
            GlobalHWVar.aggiornaSchermo(ignoraBloccoAggiornamento=True)
            pygame.time.wait(20)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i -= 1
        GlobalHWVar.disegnaImmagineSuSchermo(schermoOriginale, (0, 0))
        GlobalHWVar.aggiornaSchermo(ignoraBloccoAggiornamento=True)


def disegnaCasellaSulloSchermo(imgCasella, xCasella, yCasella, listaNemiciSotterrati, imgNemicoSotterrato, listaBacchePv):
    GlobalHWVar.disegnaImmagineSuSchermo(imgCasella, (xCasella, yCasella))
    for nemicoSotterrato in listaNemiciSotterrati:
        if nemicoSotterrato[0] == xCasella and nemicoSotterrato[1] == yCasella:
            GlobalHWVar.disegnaImmagineSuSchermo(imgNemicoSotterrato, (nemicoSotterrato[0], nemicoSotterrato[1]))
    for baccaPv in listaBacchePv:
        if GlobalHWVar.gpx * baccaPv[0] == xCasella and GlobalHWVar.gpy * baccaPv[1] == yCasella:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgBacchePv, (GlobalHWVar.gpx * baccaPv[0], GlobalHWVar.gpy * baccaPv[1]))


def animaDormiveglia(illumina, screen):
    rect = pygame.display.get_surface().get_rect()
    if illumina:
        # fase 1: illuminazione parziale
        qtaIlluminazione = 5
        vetImg = []
        i = 250
        while i > 120:
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, i))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            i -= qtaIlluminazione
        i = 0
        while i < len(vetImg):
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(vetImg[i], (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        # fase 2: rioscuramento
        image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
        image.fill((0, 0, 0, 30))
        image = image.convert_alpha(GlobalHWVar.schermo)
        i = 0
        while i <= 20:
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
        GlobalHWVar.aggiornaSchermo()
        # fase 3: illuminazione totale
        qtaIlluminazione = 5
        rect = pygame.display.get_surface().get_rect()
        vetImg = []
        i = 250
        while i > 0:
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, i))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            i -= qtaIlluminazione
        i = 0
        while i < len(vetImg):
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(vetImg[i], (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
    else:
        # fase 1: oscuramento
        image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
        image.fill((0, 0, 0, 30))
        image = image.convert_alpha(GlobalHWVar.schermo)
        i = 0
        while i <= 20:
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
        GlobalHWVar.aggiornaSchermo()
        # fase 2: reilluminazione parziale
        qtaIlluminazione = 5
        vetImg = []
        i = 250
        while i > 180:
            image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
            image.fill((0, 0, 0, i))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            i -= qtaIlluminazione
        i = 0
        while i < len(vetImg):
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(vetImg[i], (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        # fase 3: oscuramento totale
        image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
        image.fill((0, 0, 0, 30))
        image = image.convert_alpha(GlobalHWVar.schermo)
        i = 0
        while i <= 20:
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
        GlobalHWVar.aggiornaSchermo()


def animaCambioScenaCalcolatore(x, y, direzione, stato, nonMostrarePersonaggio, carim, caricaTutto, personaggioGiaNelloScreen=False):
    if stato == "avvia":
        GlobalHWVar.canaliSoundSottofondoAmbientale.mettiInPausa()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        image = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
        image.fill((255, 255, 255, 50))
        image = image.convert_alpha(GlobalHWVar.schermo)
        i = 0
        while i <= 20:
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco)
        GlobalHWVar.aggiornaSchermo()
        GlobalHWVar.nonAggiornareSchermo = True
        nonMostrarePersonaggio = True
        carim = True
        caricaTutto = True
    elif stato == "compari":
        GlobalHWVar.nonAggiornareSchermo = False
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco)
        GlobalHWVar.aggiornaSchermo()
        # carico le img del personaggio
        imgPers = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
        imgPersb = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
        if direzione == "w":
            imgPers = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio4.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            imgPersb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio4b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        elif direzione == "a":
            imgPers = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio3.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            imgPersb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio3b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        elif direzione == "s":
            imgPers = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            imgPersb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio1b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        elif direzione == "d":
            imgPers = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            imgPersb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio2b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        image = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
        i = 0
        while i <= 255:
            GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco, (x, y, GlobalHWVar.gpx, GlobalHWVar.gpy))
            GlobalHWVar.disegnaImmagineSuSchermo(imgPers, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(imgPersb, (x, y))
            image.fill((255, 255, 255, 255 - i))
            GlobalHWVar.disegnaImmagineSuSchermo(image, (x, y))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 10
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco)
        GlobalHWVar.disegnaImmagineSuSchermo(imgPers, (x, y))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersb, (x, y))
        GlobalHWVar.aggiornaSchermo()
        GlobalHWVar.nonAggiornareSchermo = True
    elif stato == "concludi":
        screen = GlobalHWVar.schermo.copy().convert()
        GlobalHWVar.nonAggiornareSchermo = False
        # carico le img del personaggio
        imgPers = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
        imgPersb = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
        if direzione == "w":
            imgPers = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio4.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            imgPersb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio4b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        elif direzione == "a":
            imgPers = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio3.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            imgPersb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio3b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        elif direzione == "s":
            imgPers = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            imgPersb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio1b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        elif direzione == "d":
            imgPers = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            imgPersb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio2b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco)
        GlobalHWVar.disegnaImmagineSuSchermo(imgPers, (x, y))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersb, (x, y))
        GlobalHWVar.aggiornaSchermo()
        # animazione apparizione stanza
        image = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
        imgTrasparenza = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), pygame.SRCALPHA)
        i = 0
        while i <= 255:
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco)
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((255, 255, 255, 255 - i))
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            if personaggioGiaNelloScreen:
                imgTrasparenza.fill((255, 255, 255, 255 - i))
                imgPersTemp = imgPers.copy()
                imgPersTemp.blit(imgTrasparenza, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                GlobalHWVar.disegnaImmagineSuSchermo(imgPersTemp, (x, y))
                imgPersbTemp = imgPersb.copy()
                imgPersbTemp.blit(imgTrasparenza, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                GlobalHWVar.disegnaImmagineSuSchermo(imgPersbTemp, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(imgPers, (x, y))
                GlobalHWVar.disegnaImmagineSuSchermo(imgPersb, (x, y))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 10
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        if not personaggioGiaNelloScreen:
            GlobalHWVar.disegnaImmagineSuSchermo(imgPers, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(imgPersb, (x, y))
        GlobalHWVar.aggiornaSchermo()
        GlobalHWVar.canaliSoundSottofondoAmbientale.togliPausa()
        nonMostrarePersonaggio = False
        carim = True
        caricaTutto = True

    return nonMostrarePersonaggio, carim, caricaTutto


def animaMancamento(intensita):
    screen = GlobalHWVar.schermo.copy().convert()
    image = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
    if intensita == "lieve":
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.8], True)
        i = 0
        while i < 10:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((0, 0, 0, i * 10))
            image = image.convert_alpha(GlobalHWVar.schermo)
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        image.fill((0, 0, 0, 100))
        image = image.convert_alpha(GlobalHWVar.schermo)
        GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.6], True)

        i = 20
        while i > 5:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((0, 0, 0, i * 5))
            image = image.convert_alpha(GlobalHWVar.schermo)
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i -= 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        image.fill((0, 0, 0, 25))
        image = image.convert_alpha(GlobalHWVar.schermo)
        GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.8], True)

        i = 6
        while i < 10:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((0, 0, 0, i * 5))
            image = image.convert_alpha(GlobalHWVar.schermo)
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        image.fill((0, 0, 0, 50))
        image = image.convert_alpha(GlobalHWVar.schermo)
        GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.7], True)

        i = 10
        while i > 0:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((0, 0, 0, i * 5))
            image = image.convert_alpha(GlobalHWVar.schermo)
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i -= 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti], True)
    elif intensita == "media":
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.6], True)
        i = 0
        while i < 20:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((0, 0, 0, i * 10))
            image = image.convert_alpha(GlobalHWVar.schermo)
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        image.fill((0, 0, 0, 200))
        image = image.convert_alpha(GlobalHWVar.schermo)
        GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.2], True)

        i = 40
        while i > 10:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((0, 0, 0, i * 5))
            image = image.convert_alpha(GlobalHWVar.schermo)
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i -= 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        image.fill((0, 0, 0, 100))
        image = image.convert_alpha(GlobalHWVar.schermo)
        GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.4], True)

        i = 10
        while i < 15:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((0, 0, 0, i * 10))
            image = image.convert_alpha(GlobalHWVar.schermo)
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        image.fill((0, 0, 0, 150))
        image = image.convert_alpha(GlobalHWVar.schermo)
        GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.6], True)

        i = 30
        while i > 0:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((0, 0, 0, i * 5))
            image = image.convert_alpha(GlobalHWVar.schermo)
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i -= 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti], True)
    elif intensita == "pesanteOut":
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.6], True)
        i = 0
        while i < 22:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((0, 0, 0, i * 10))
            image = image.convert_alpha(GlobalHWVar.schermo)
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        image.fill((0, 0, 0, 220))
        image = image.convert_alpha(GlobalHWVar.schermo)
        GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.2], True)

        i = 22
        while i > 15:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((0, 0, 0, i * 10))
            image = image.convert_alpha(GlobalHWVar.schermo)
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i -= 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        image.fill((0, 0, 0, 150))
        image = image.convert_alpha(GlobalHWVar.schermo)
        GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.4], True)

        i = 15
        while i < 20:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((0, 0, 0, i * 10))
            image = image.convert_alpha(GlobalHWVar.schermo)
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        image.fill((0, 0, 0, 200))
        image = image.convert_alpha(GlobalHWVar.schermo)
        GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.3], True)

        i = 20
        while i > 12:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((0, 0, 0, i * 10))
            image = image.convert_alpha(GlobalHWVar.schermo)
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i -= 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        image.fill((0, 0, 0, 120))
        image = image.convert_alpha(GlobalHWVar.schermo)
        GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.6], True)

        i = 12
        while i < 25:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((0, 0, 0, i * 10))
            image = image.convert_alpha(GlobalHWVar.schermo)
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
        GlobalHWVar.aggiornaSchermo()
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.1], True)
    elif intensita == "pesanteIn":
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.2], True)
        i = 25
        while i > 15:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((0, 0, 0, i * 10))
            image = image.convert_alpha(GlobalHWVar.schermo)
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i -= 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        image.fill((0, 0, 0, 150))
        image = image.convert_alpha(GlobalHWVar.schermo)
        GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.4], True)

        i = 15
        while i < 20:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((0, 0, 0, i * 10))
            image = image.convert_alpha(GlobalHWVar.schermo)
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        image.fill((0, 0, 0, 200))
        image = image.convert_alpha(GlobalHWVar.schermo)
        GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.3], True)

        i = 20
        while i > 0:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((0, 0, 0, i * 10))
            image = image.convert_alpha(GlobalHWVar.schermo)
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i -= 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.6], True)
