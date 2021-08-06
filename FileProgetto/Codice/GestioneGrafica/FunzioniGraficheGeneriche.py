# -*- coding: utf-8 -*-

import os
import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput


def messaggio(msg, colore, x, y, gr, largezzaFoglio=-1, spazioTraLeRighe=-1, daDestra=False, centrale=False, lungMax=False, superficie=False):
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


def messaggioParlato(bottoneDown, fineDialogo, msg, colore, x, y, gr, largezzaFoglio, spazioTraLeRighe, scriviTutto=False):
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
                        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                            fineDialogo = True
                            bottoneDown = False
                        elif bottoneDown == pygame.K_SPACE or bottoneDown == "mouseSinistro" or bottoneDown == "padCroce":
                            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreSkipDialoghi)
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
                                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreDialoghi)
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


def controllaMorteRallo(vitaRallo, inizio, gameover):
    if vitaRallo <= 0:
        gameover = True
        if GlobalHWVar.mouseBloccato:
            GlobalHWVar.configuraCursore(False)
        GlobalHWVar.canaleSoundPuntatoreSposta.stop()
        GlobalHWVar.canaleSoundPuntatoreSeleziona.stop()
        GlobalHWVar.canaleSoundPassiRallo.stop()
        GlobalHWVar.canaleSoundPassiColco.stop()
        GlobalHWVar.canaleSoundPassiNemiciPersonaggi.stop()
        GlobalHWVar.canaleSoundMorteNemici.stop()
        GlobalHWVar.canaleSoundLvUp.stop()
        GlobalHWVar.canaleSoundInterazioni.stop()
        GlobalHWVar.canaleSoundAttacco.stop()
        i = GlobalHWVar.volumeCanzoni
        j = GlobalHWVar.volumeEffetti
        while i > 0 or j > 0:
            GlobalHWVar.canaleSoundCanzone.set_volume(i)
            GlobalHWVar.canaliSoundSottofondoAmbientale.settaVolume(j)
            i -= GlobalHWVar.volumeCanzoni / 10
            j -= GlobalHWVar.volumeEffetti / 10
            pygame.time.wait(30)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.canaleSoundCanzone.stop()
        GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
        GlobalHWVar.canaliSoundSottofondoAmbientale.arresta()
        GlobalHWVar.canaliSoundSottofondoAmbientale.settaVolume(GlobalHWVar.volumeEffetti)

        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreMorte)
        oscuraIlluminaSchermo(illumina=False, tipoOscuramento=2)

        messaggio("Sei morto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 13, 150)
        GlobalHWVar.aggiornaSchermo()

        bottoneDown = False
        continua = False
        while not continua:
            # gestione degli input
            bottoneDown, inutile = GestioneInput.getInput(bottoneDown, False)
            if bottoneDown:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                continua = True
                bottoneDown = False

            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
        inizio = True

    return inizio, gameover


def disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti, inMovimento=False, frame=False, attaccoRavvicinato=False, attaccoDaLontano=False):
    # personaggio: 1=d, 2=a, 3=w, 4=s
    if attaccoDaLontano:
        if npers == 1:
            GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persdmbAttacco, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (x, y))
        if npers == 2:
            GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
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
            GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
        if npers == 4:
            GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
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
            GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
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
            GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
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
            GlobalHWVar.disegnaImmagineSuSchermo(armatura, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y))
        if npers == 4:
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(faretra, (x, y))
            if inMovimento:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssm, (x, y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(pers, (x, y))
            if avvele:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
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
    messaggio("Hai ottenuto: " + oggettoRicevuto, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
    GlobalHWVar.aggiornaSchermo()
    i = 0
    while i < 10:
        pygame.time.wait(100)
        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        i += 1
    bottoneDown = False
    risposta = False
    while not risposta:
        # gestione degli input
        bottoneDown, inutile = GestioneInput.getInput(bottoneDown, False)
        if bottoneDown == pygame.K_SPACE or bottoneDown == "mouseSinistro" or bottoneDown == "padCroce":
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


def animaEvento(pathImgs, coordinateImgAnimata, dimensioniImgAnimata, listaAudio):
    dimX, dimY = dimensioniImgAnimata
    vetImgAnimazione = []
    if pathImgs:
        numImgAnimazione = len(os.listdir(GlobalHWVar.gamePath + pathImgs))
    else:
        numImgAnimazione = 0
    i = 1
    while i <= numImgAnimazione:
        vetImgAnimazione.append(CaricaFileProgetto.loadImage(pathImgs + "img" + str(i) + ".png", dimX, dimY, True))
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
        if len(listaAudio) > 0 and listaAudio[0] == numFrameAttuale:
            GlobalHWVar.canaleSoundInterazioni.play(listaAudio[1])
            del listaAudio[1]
            del listaAudio[0]
        GlobalHWVar.disegnaImmagineSuSchermo(vetImgAnimazione.pop(0), coordinateImgAnimata)

        GlobalHWVar.aggiornaSchermo()
        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockAnimazioni.tick(GlobalHWVar.fpsAnimazioni)
        numFrameAttuale += 1


def disegnaVitaRallo(pv, pvtot, numFrecce, avvele, attp, difp):
    lungvitatot = int(((GlobalHWVar.gpx * pvtot) / float(4)) // 5)
    lungvita = (lungvitatot * pv) // pvtot
    if lungvita < 0:
        lungvita = 0

    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoRallo, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perss, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssb, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgNumFrecce, (int(GlobalHWVar.gsx // 32 * 1.2), GlobalHWVar.gsy // 18 * 17))
    messaggio(u" ×" + str(numFrecce), GlobalHWVar.grigiochi, int(GlobalHWVar.gsx // 32 * 1.8), int(GlobalHWVar.gsy // 18 * 17.3), 40)
    if avvele:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.avvelenato, (GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 17))
    if attp > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.attaccopiu, (GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 17))
    if difp > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.difesapiu, (GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 17))
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx, (GlobalHWVar.gpy * 17) + (GlobalHWVar.gpy * 0.75), lungvitatot + (GlobalHWVar.gpx * 0.1), GlobalHWVar.gpy // 2))
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gpx, (GlobalHWVar.gpy * 17) + (GlobalHWVar.gpy * 0.8), lungvitatot, GlobalHWVar.gpy * 0.15))
    if lungvita > 0:
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.verdeVita, (GlobalHWVar.gpx, (GlobalHWVar.gpy * 17) + (GlobalHWVar.gpy * 0.8), lungvita, GlobalHWVar.gpy * 0.15))
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx + lungvita, (GlobalHWVar.gpy * 17) + (GlobalHWVar.gpy * 0.8), GlobalHWVar.gpx * 0.05, GlobalHWVar.gpy * 0.15))


def disegnaVitaColco(entot, enrob, surrisc, velp, effp):
    lungentot = int(((GlobalHWVar.gpx * entot) / float(4)) // 15)
    lungen = int(((GlobalHWVar.gpx * enrob) / float(4)) // 15)
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
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx, 0, lungentot + (GlobalHWVar.gpx * 0.1), GlobalHWVar.gpy * 0.25))
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gpx, GlobalHWVar.gpy * 0.05, lungentot, GlobalHWVar.gpy * 0.15))
    if lungen > 0:
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.azzurroVitaColco, (GlobalHWVar.gpx, GlobalHWVar.gpy * 0.05, lungen, GlobalHWVar.gpy * 0.15))
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx + lungen, GlobalHWVar.gpy * 0.05, GlobalHWVar.gpx * 0.05, GlobalHWVar.gpy * 0.15))


def disegnaVitaEsche(pvEsca):
    lungvitatot = int(((GlobalHWVar.gpx * GlobalGameVar.vitaTotEsche) / float(4)) // 15)
    lungvita = int(((GlobalHWVar.gpx * pvEsca) / float(4)) // 15)
    if lungvita < 0:
        lungvita = 0

    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoEsche, (0, 0))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.esche, (0, 0))
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx, 0, lungvitatot + (GlobalHWVar.gpx * 0.1), GlobalHWVar.gpy * 0.25))
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gpx, GlobalHWVar.gpy * 0.05, lungvitatot, GlobalHWVar.gpy * 0.15))
    if lungvita > 0:
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.verdeVita, (GlobalHWVar.gpx, GlobalHWVar.gpy * 0.05, lungvita, GlobalHWVar.gpy * 0.15))
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx + lungvita, GlobalHWVar.gpy * 0.05, GlobalHWVar.gpx * 0.05, GlobalHWVar.gpy * 0.15))


def disegnaVitaNemici(pvm, pvmtot, nemicoAvvelenato, nemicoAppiccicato, immagineS):
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoMostro, (0, 0))
    if nemicoAvvelenato:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.avvelenato, (GlobalHWVar.gpx + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
    if nemicoAppiccicato:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.appiccicoso, ((GlobalHWVar.gpx * 2) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
    GlobalHWVar.disegnaImmagineSuSchermo(immagineS, (0, 0))

    if pvmtot > 1500:
        lungvitatot = int(((GlobalHWVar.gpx * 1500) / float(4)) // 15)
        if pvm > 7500:
            pvm = 1500
            coloreVita = (120, 50, 120)
            coloreVitaSuccessiva = (180, 50, 70)
        elif pvm > 6000:
            pvm -= 6000
            coloreVita = (120, 50, 120)
            coloreVitaSuccessiva = (180, 50, 70)
        elif pvm > 4500:
            pvm -= 4500
            coloreVita = (180, 50, 70)
            coloreVitaSuccessiva = (170, 110, 50)
        elif pvm > 3000:
            pvm -= 3000
            coloreVita = (170, 110, 50)
            coloreVitaSuccessiva = (170, 160, 40)
        elif pvm > 1500:
            pvm -= 1500
            coloreVita = (170, 160, 40)
            coloreVitaSuccessiva = (80, 180, 80)
        else:
            coloreVita = (80, 180, 80)
            coloreVitaSuccessiva = (80, 80, 80)
    else:
        lungvitatot = int(((GlobalHWVar.gpx * pvmtot) / float(4)) // 15)
        coloreVita = (80, 180, 80)
        coloreVitaSuccessiva = (80, 80, 80)

    lungvita = int(((GlobalHWVar.gpx * pvm) / float(4)) // 15)
    if lungvita < 0:
        lungvita = 0

    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx, 0, lungvitatot + (GlobalHWVar.gpx * 0.1), GlobalHWVar.gpy * 0.25))
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gpx, GlobalHWVar.gpy * 0.05, lungvitatot, GlobalHWVar.gpy * 0.15))
    if lungvita > 0:
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, coloreVitaSuccessiva, (GlobalHWVar.gpx, GlobalHWVar.gpy * 0.05, lungvitatot, GlobalHWVar.gpy * 0.15))
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, coloreVita, (GlobalHWVar.gpx, GlobalHWVar.gpy * 0.05, lungvita, GlobalHWVar.gpy * 0.15))
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx + lungvita, GlobalHWVar.gpy * 0.05, GlobalHWVar.gpx * 0.05, GlobalHWVar.gpy * 0.15))
