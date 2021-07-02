# -*- coding: utf-8 -*-

import math
import pygame
import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import FunzioniGraficheGeneriche


def animaCamminataRalloCambiosta(npers, x, y, scudo, armatura, armaMov1, arco, faretra, guantiMov1, collana, avvele, fineanimaz):
    if npers == 1:
        x = x - (GlobalHWVar.gpx * fineanimaz // 10)
    if npers == 2:
        x = x + (GlobalHWVar.gpx * fineanimaz // 10)
    if npers == 3:
        y = y + (GlobalHWVar.gpy * fineanimaz // 10)
    if npers == 4:
        y = y - (GlobalHWVar.gpy * fineanimaz // 10)
    pers = False
    if 5 < fineanimaz <= 10:
        frame = 1
        FunzioniGraficheGeneriche.disegnaRallo(npers, x, y, avvele, pers, armaMov1, armatura, scudo, collana, arco, faretra, guantiMov1, True, frame)
    else:
        fineanimaz = 0

    return fineanimaz


def animaCamminataRalloSpostato(npers, x, y, scudo, armatura, armaMov1, armaMov2, arco, faretra, guantiMov1, guantiMov2, collana, avvele, fineanimaz):
    if npers == 1:
        x = x - (GlobalHWVar.gpx * fineanimaz // 10)
    if npers == 2:
        x = x + (GlobalHWVar.gpx * fineanimaz // 10)
    if npers == 3:
        y = y + (GlobalHWVar.gpy * fineanimaz // 10)
    if npers == 4:
        y = y - (GlobalHWVar.gpy * fineanimaz // 10)
    pers = False
    if 5 < fineanimaz <= 10:
        frame = 1
        FunzioniGraficheGeneriche.disegnaRallo(npers, x, y, avvele, pers, armaMov1, armatura, scudo, collana, arco, faretra, guantiMov1, True, frame)
    elif 0 < fineanimaz <= 5:
        frame = 2
        FunzioniGraficheGeneriche.disegnaRallo(npers, x, y, avvele, pers, armaMov2, armatura, scudo, collana, arco, faretra, guantiMov2, True, frame)


def animaCamminataRallo(sposta, x, y, vx, vy, primopasso, cambiosta, npers, pers, arma, scudo, armatura, armaMov1, armaMov2, arco, faretra, guanti, guantiMov1, guantiMov2, collana, avvele, difesa, animazioneRallo, fineanimaz, nonMostrarePersonaggio):
    if sposta:
        # mentre ci si sposta
        if x != vx or y != vy:
            animazioneRallo = True
            if not GlobalHWVar.canaleSoundPassiRallo.get_busy():
                GlobalHWVar.canaleSoundPassiRallo.play(GlobalSndVar.rumorecamminata)
            if primopasso and not cambiosta:
                primopasso = False
            # camminata quando si entra in una stanza
            if cambiosta:
                fineanimaz = animaCamminataRalloCambiosta(npers, x, y, scudo, armatura, armaMov1, arco, faretra, guantiMov1, collana, avvele, fineanimaz)
                if fineanimaz == 0:
                    GlobalHWVar.canaleSoundPassiRallo.stop()
            # camminata quando non si entra in una stanza
            else:
                animaCamminataRalloSpostato(npers, x, y, scudo, armatura, armaMov1, armaMov2, arco, faretra, guantiMov1, guantiMov2, collana, avvele, fineanimaz)
        # quando si apre una porta o un cofanetto oppure quando ci si sposta verso un muro
        elif difesa == 0 and fineanimaz > 0:
            animazioneRallo = True
            if not nonMostrarePersonaggio:
                FunzioniGraficheGeneriche.disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
    elif GlobalHWVar.canaleSoundPassiRallo.get_busy():
        GlobalHWVar.canaleSoundPassiRallo.stop()
    return animazioneRallo, primopasso, fineanimaz


def animaAttaccoRallo(sposta, x, y, npers, pers, arma, scudo, armatura, collana, arco, faretra, guanti, armaAttacco, arcoAttacco, guantiAttacco, avvele, attacco, difesa, vrx, vry, armrobS, animazioneRallo, attaccoADistanza, animaOggetto, vettoreImgCaselle, fineanimaz):
    if sposta and fineanimaz != 0:
        if attacco == 1 and difesa == 0:
            animazioneRallo = True
            if attaccoADistanza:
                if fineanimaz == 10:
                    GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.rumoreLancioFreccia)
                elif fineanimaz == 5:
                    GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.rumoreAttaccoArco)
                FunzioniGraficheGeneriche.disegnaRallo(npers, x, y, avvele, pers, armaAttacco, armatura, scudo, collana, arcoAttacco, faretra, guantiAttacco, False, False, False, True)
            else:
                if fineanimaz == 10:
                    GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.rumoreAttaccoSpada)
                FunzioniGraficheGeneriche.disegnaRallo(npers, x, y, avvele, pers, armaAttacco, armatura, scudo, collana, arco, faretra, guantiAttacco, False, False, True)
        elif animaOggetto[0]:
            animazioneRallo = True
            if animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata":
                FunzioniGraficheGeneriche.disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
            if animaOggetto[0] == "pozione" or animaOggetto[0] == "superPozione":
                if fineanimaz == 10:
                    GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.suonoUsoPozione)
                FunzioniGraficheGeneriche.disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
                if fineanimaz > 5:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgAnimaPozione1, (x, y))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgAnimaPozione2, (x, y))
            elif animaOggetto[0] == "medicina":
                if fineanimaz == 10:
                    GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.suonoUsoMedicina)
                FunzioniGraficheGeneriche.disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
                if fineanimaz > 5:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgAnimaMedicina1, (x, y))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgAnimaMedicina2, (x, y))
            elif animaOggetto[0] == "caricaBatterie" or animaOggetto[0] == "caricaBatterieMigliorato":
                if fineanimaz == 10:
                    GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.suonoUsoCaricabatterie)
                i = 0
                while i < len(vettoreImgCaselle):
                    if vrx == vettoreImgCaselle[i] and vry == vettoreImgCaselle[i + 1]:
                        GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                        FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                        break
                    i += 3
                GlobalHWVar.disegnaImmagineSuSchermo(armrobS, (vrx, vry))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robos, (vrx, vry))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgAnimaCaricabatterie, (vrx, vry))
                FunzioniGraficheGeneriche.disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
    return animazioneRallo


def animaDifesaRallo(x, y, armaS, armaturaS, arcoS, faretraS, collanaS, scudoDifesa, guantiDifesa, avvele, difesa, animazioneRallo, nemicoAttaccante, fineanimaz):
    if nemicoAttaccante and nemicoAttaccante.ralloParato and fineanimaz == 4:
        GlobalHWVar.canaleSoundAttacco.stop()
        GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.rumoreParata)
    if difesa != 0 or (nemicoAttaccante and nemicoAttaccante.ralloParato):
        animazioneRallo = True
        GlobalHWVar.disegnaImmagineSuSchermo(arcoS, (x, y))
        GlobalHWVar.disegnaImmagineSuSchermo(faretraS, (x, y))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perss, (x, y))
        if avvele:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persAvvele, (x, y))
        GlobalHWVar.disegnaImmagineSuSchermo(armaturaS, (x, y))
        GlobalHWVar.disegnaImmagineSuSchermo(collanaS, (x, y))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.persmbDifesa, (x, y))
        GlobalHWVar.disegnaImmagineSuSchermo(armaS, (x, y))
        GlobalHWVar.disegnaImmagineSuSchermo(guantiDifesa, (x, y))
        GlobalHWVar.disegnaImmagineSuSchermo(scudoDifesa, (x, y))
    return animazioneRallo


def animaLvUp(x, y, npers, pers, arma, armatura, scudo, collana, arco, faretra, guanti, liv, aumentoliv, caricaTutto, bottoneDown, animazioneRallo, movimentoPerMouse, fineanimaz):
    if aumentoliv != 0:
        liv -= aumentoliv
        animazioneRallo = True
        if fineanimaz == 10:
            GlobalHWVar.canaleSoundLvUp.play(GlobalSndVar.rumorelevelup)
        avvele = False
        FunzioniGraficheGeneriche.disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
        if 5 <= fineanimaz <= 10:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.saliliv2, (x, y))
        if 1 < fineanimaz <= 5:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.saliliv1, (x, y))
        if fineanimaz == 1:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.saliliv, (x, y))

        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfocontcof, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 0))
        i = 1
        while i <= 100:
            if liv == i:
                FunzioniGraficheGeneriche.messaggio("Liv +: Attacco aumentato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
                break
            i += 3
        i = 2
        while i <= 100:
            if liv == i:
                FunzioniGraficheGeneriche.messaggio("Liv +: Difesa aumentata", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
                break
            i += 3
        i = 3
        while i <= 100:
            if liv == i:
                FunzioniGraficheGeneriche.messaggio("Liv +: Punti vita aumentati", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
                break
            i += 3
        if fineanimaz == 1:
            if GlobalHWVar.mouseBloccato:
                GlobalHWVar.configuraCursore(False)
            GlobalHWVar.aggiornaSchermo()
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            risposta = False
            bottoneDown = False
            while not risposta:
                # gestione degli input
                bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, False)
                if bottoneDown == pygame.K_SPACE or bottoneDown == "mouseSinistro" or bottoneDown == "padCroce":
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    risposta = True
                    aumentoliv -= 1
                    bottoneDown = False
                if bottoneDown:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False

                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)

        caricaTutto = True
        movimentoPerMouse = False
        bottoneDown = False
    return animazioneRallo, caricaTutto, bottoneDown, aumentoliv, movimentoPerMouse


def animaDanneggiamentoRallo(x, y, attaccoDiColco, attaccoDiRallo, tecnicaUsata, azioniDaEseguire, fineanimaz):
    if "attaccoRallo" in azioniDaEseguire and "Rallo" in attaccoDiRallo and fineanimaz <= 5:
        i = 0
        while i < len(attaccoDiRallo):
            if attaccoDiRallo[i] == "Rallo":
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgDanneggiamentoCausaRallo, (x, y))
            i += 3
    if "attaccoColco" in azioniDaEseguire and "Rallo" in attaccoDiColco and fineanimaz <= 5:
        if tecnicaUsata.startswith("scossa") or tecnicaUsata.startswith("freccia") or tecnicaUsata.startswith("tempesta"):
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgDanneggiamentoCausaColco, (x, y))


def animaRalloFermo(x, y, vx, vy, npers, pers, scudo, armatura, arma, arco, faretra, guanti, collana, avvele, azioniDaEseguire, animazioneRalloFatta, nemicoAttaccante, difesa, fineanimaz):
    if (not "attaccoRallo" in azioniDaEseguire and not "movimentoRallo" in azioniDaEseguire and not (nemicoAttaccante and nemicoAttaccante.ralloParato) and difesa == 0) or (fineanimaz == 0 and difesa == 0):
        if animazioneRalloFatta:
            FunzioniGraficheGeneriche.disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
        else:
            FunzioniGraficheGeneriche.disegnaRallo(npers, vx, vy, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)


def animaCamminataColco(nrob, rx, ry, vrx, vry, robot, armrob, surriscalda, cambiosta, animazioneColco, nemicoInquadrato, fineanimaz):
    if (rx != vrx or ry != vry) and not cambiosta and robot != GlobalImgVar.robomo:
        animazioneColco = True
        if nrob != 0 and fineanimaz == 10:
            GlobalHWVar.canaleSoundPassiColco.play(GlobalSndVar.rumoreCamminataColco)
        # nrob => 1=d, 2=a, 3=s, 4=w
        if nrob == 1:
            if 5 < fineanimaz <= 10:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robodp, (rx - (GlobalHWVar.gpx * fineanimaz // 10), ry))
                if surriscalda > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboSurrisc, (rx - (GlobalHWVar.gpx * fineanimaz // 10), ry))
                GlobalHWVar.disegnaImmagineSuSchermo(armrob, (rx - (GlobalHWVar.gpx * fineanimaz // 10), ry))
                if nemicoInquadrato == "Colco":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx - (GlobalHWVar.gpy * fineanimaz // 10), ry))
            if 0 < fineanimaz <= 5:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robodp, (rx - (GlobalHWVar.gpx * fineanimaz // 10), ry))
                if surriscalda > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboSurrisc, (rx - (GlobalHWVar.gpx * fineanimaz // 10), ry))
                GlobalHWVar.disegnaImmagineSuSchermo(armrob, (rx - (GlobalHWVar.gpx * fineanimaz // 10), ry))
                if nemicoInquadrato == "Colco":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx - (GlobalHWVar.gpy * fineanimaz // 10), ry))
        if nrob == 2:
            if 5 < fineanimaz <= 10:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboap, (rx + (GlobalHWVar.gpx * fineanimaz // 10), ry))
                if surriscalda > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboSurrisc, (rx + (GlobalHWVar.gpx * fineanimaz // 10), ry))
                GlobalHWVar.disegnaImmagineSuSchermo(armrob, (rx + (GlobalHWVar.gpx * fineanimaz // 10), ry))
                if nemicoInquadrato == "Colco":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx + (GlobalHWVar.gpy * fineanimaz // 10), ry))
            if 0 < fineanimaz <= 5:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboap, (rx + (GlobalHWVar.gpx * fineanimaz // 10), ry))
                if surriscalda > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboSurrisc, (rx + (GlobalHWVar.gpx * fineanimaz // 10), ry))
                GlobalHWVar.disegnaImmagineSuSchermo(armrob, (rx + (GlobalHWVar.gpx * fineanimaz // 10), ry))
                if nemicoInquadrato == "Colco":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx + (GlobalHWVar.gpy * fineanimaz // 10), ry))
        if nrob == 4:
            if 5 < fineanimaz <= 10:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robow, (rx, ry + (GlobalHWVar.gpy * fineanimaz // 10)))
                if surriscalda > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboSurrisc, (rx, ry + (GlobalHWVar.gpy * fineanimaz // 10)))
                GlobalHWVar.disegnaImmagineSuSchermo(armrob, (rx, ry + (GlobalHWVar.gpy * fineanimaz // 10)))
                if nemicoInquadrato == "Colco":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx, ry + (GlobalHWVar.gpy * fineanimaz // 10)))
            if 0 < fineanimaz <= 5:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robow, (rx, ry + (GlobalHWVar.gpy * fineanimaz // 10)))
                if surriscalda > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboSurrisc, (rx, ry + (GlobalHWVar.gpy * fineanimaz // 10)))
                GlobalHWVar.disegnaImmagineSuSchermo(armrob, (rx, ry + (GlobalHWVar.gpy * fineanimaz // 10)))
                if nemicoInquadrato == "Colco":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx, ry + (GlobalHWVar.gpy * fineanimaz // 10)))
        if nrob == 3:
            if 5 < fineanimaz <= 10:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robos, (rx, ry - (GlobalHWVar.gpy * fineanimaz // 10)))
                if surriscalda > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboSurrisc, (rx, ry - (GlobalHWVar.gpy * fineanimaz // 10)))
                GlobalHWVar.disegnaImmagineSuSchermo(armrob, (rx, ry - (GlobalHWVar.gpy * fineanimaz // 10)))
                if nemicoInquadrato == "Colco":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx, ry - (GlobalHWVar.gpy * fineanimaz // 10)))
            if 0 < fineanimaz <= 5:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robos, (rx, ry - (GlobalHWVar.gpy * fineanimaz // 10)))
                if surriscalda > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboSurrisc, (rx, ry - (GlobalHWVar.gpy * fineanimaz // 10)))
                GlobalHWVar.disegnaImmagineSuSchermo(armrob, (rx, ry - (GlobalHWVar.gpy * fineanimaz // 10)))
                if nemicoInquadrato == "Colco":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx, ry - (GlobalHWVar.gpy * fineanimaz // 10)))
    return animazioneColco


def animaTecnicaColco(rx, ry, nrob, robot, armrob, armrobS, tecnicaUsata, cambiosta, animazioneColco, surriscalda, nemicoInquadrato, fineanimaz):
    if not cambiosta and fineanimaz != 0:
        animazioneColco = True

        imgAnimazioneSelf = 0
        imgAnimazione1w = 0
        imgAnimazione2w = 0
        imgAnimazione1a = 0
        imgAnimazione2a = 0
        imgAnimazione1s = 0
        imgAnimazione2s = 0
        imgAnimazione1d = 0
        imgAnimazione2d = 0
        imgAnimazione1 = 0
        imgAnimazione2 = 0
        imgAnimazione = 0

        i = 0
        while i < len(GlobalImgVar.vetAnimazioniTecniche):
            if GlobalImgVar.vetAnimazioniTecniche[i] == tecnicaUsata:
                if tecnicaUsata.startswith("scossa") or tecnicaUsata.startswith("freccia") or tecnicaUsata.startswith("cura") or tecnicaUsata == "antidoto" or tecnicaUsata == "attP" or tecnicaUsata == "difP":
                    imgAnimazione1w = GlobalImgVar.vetAnimazioniTecniche[i + 1][0]
                    imgAnimazione2w = GlobalImgVar.vetAnimazioniTecniche[i + 1][1]
                    imgAnimazione1a = GlobalImgVar.vetAnimazioniTecniche[i + 1][2]
                    imgAnimazione2a = GlobalImgVar.vetAnimazioniTecniche[i + 1][3]
                    imgAnimazione1s = GlobalImgVar.vetAnimazioniTecniche[i + 1][4]
                    imgAnimazione2s = GlobalImgVar.vetAnimazioniTecniche[i + 1][5]
                    imgAnimazione1d = GlobalImgVar.vetAnimazioniTecniche[i + 1][6]
                    imgAnimazione2d = GlobalImgVar.vetAnimazioniTecniche[i + 1][7]
                    imgAnimazioneSelf = GlobalImgVar.vetAnimazioniTecniche[i + 1][8]
                elif tecnicaUsata.startswith("tempesta"):
                    imgAnimazione1 = GlobalImgVar.vetAnimazioniTecniche[i + 1][0]
                    imgAnimazione2 = GlobalImgVar.vetAnimazioniTecniche[i + 1][1]
                else:
                    imgAnimazione = GlobalImgVar.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2

        if fineanimaz == 10:
            if tecnicaUsata.startswith("scossa") or tecnicaUsata.startswith("freccia"):
                GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.rumoreScossaFreccia)
            elif tecnicaUsata.startswith("tempesta"):
                GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.rumoreTempestaElettrica)
            elif tecnicaUsata.startswith("cura"):
                GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.rumoreCuraRobo)
            elif tecnicaUsata == "antidoto":
                GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.rumoreAntidoto)
            elif tecnicaUsata == "attP" or tecnicaUsata == "difP":
                GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.rumoreAttPDifP)
            elif tecnicaUsata.startswith("ricarica"):
                GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.rumoreAutoricarica)
            elif tecnicaUsata == "raffred":
                GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.rumoreRaffreddamento)
            elif tecnicaUsata == "velocizza" or tecnicaUsata == "efficienza":
                GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.rumoreVelocizzaEfficienza)

        if tecnicaUsata.startswith("scossa") or tecnicaUsata.startswith("freccia") or tecnicaUsata.startswith("cura") or tecnicaUsata == "antidoto" or tecnicaUsata == "attP" or tecnicaUsata == "difP":
            GlobalHWVar.disegnaImmagineSuSchermo(robot, (rx, ry))
            if surriscalda > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboSurrisc, (rx, ry))
            GlobalHWVar.disegnaImmagineSuSchermo(armrob, (rx, ry))
            # nrob => 1=d, 2=a, 3=s, 4=w
            if 7 < fineanimaz <= 10:
                if nrob == 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazioneSelf, (rx, ry))
                if nrob == 1:
                    GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione1d, (rx, ry))
                if nrob == 2:
                    GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione1a, (rx - GlobalHWVar.gpx, ry))
                if nrob == 3:
                    GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione1s, (rx, ry))
                if nrob == 4:
                    GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione1w, (rx, ry - GlobalHWVar.gpy))
            if 0 < fineanimaz <= 7:
                if nrob == 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazioneSelf, (rx, ry))
                if nrob == 1:
                    GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione2d, (rx, ry))
                if nrob == 2:
                    GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione2a, (rx - GlobalHWVar.gpx, ry))
                if nrob == 3:
                    GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione2s, (rx, ry))
                if nrob == 4:
                    GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione2w, (rx, ry - GlobalHWVar.gpy))
            if nemicoInquadrato == "Colco":
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx, ry))
        if tecnicaUsata.startswith("ricarica") or tecnicaUsata == "raffred" or tecnicaUsata == "velocizza" or tecnicaUsata == "efficienza":
            if tecnicaUsata.startswith("ricarica"):
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robomo, (rx, ry))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(armrobS, (rx, ry))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robos, (rx, ry))
            GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione, (rx, ry))
            if nemicoInquadrato == "Colco":
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx, ry))
        if tecnicaUsata.startswith("tempesta"):
            GlobalHWVar.disegnaImmagineSuSchermo(robot, (rx, ry))
            if surriscalda > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboSurrisc, (rx, ry))
            GlobalHWVar.disegnaImmagineSuSchermo(armrob, (rx, ry))
            if 7 < fineanimaz <= 10:
                GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione1, (rx - (GlobalHWVar.gpx * 6), ry - (GlobalHWVar.gpy * 6)))
            if 0 < fineanimaz <= 7:
                GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione2, (rx - (GlobalHWVar.gpx * 6), ry - (GlobalHWVar.gpy * 6)))
            if nemicoInquadrato == "Colco":
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx, ry))

    return animazioneColco


def animaDanneggiamentoColco(rx, ry, robot, armrob, surriscalda, nemicoAttaccante, attaccoDiRallo, cambiosta, azioniDaEseguire, fineanimaz):
    if not cambiosta and fineanimaz != 0:
        if "attaccoRallo" in azioniDaEseguire and "Colco" in attaccoDiRallo and fineanimaz <= 5:
            i = 0
            while i < len(attaccoDiRallo):
                if attaccoDiRallo[i] == "Colco":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgDanneggiamentoColco, (rx, ry))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgDanneggiamentoCausaRallo, (rx, ry))
                    if attaccoDiRallo[i + 2]:
                        robot = GlobalImgVar.robomo
                        armrob = GlobalImgVar.armrobmo
                        surriscalda = 0
                i += 3
        elif "attaccoNemici" in azioniDaEseguire and nemicoAttaccante.bersaglioColpito[0] == "Colco":
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgDanneggiamentoColco, (rx, ry))
            if nemicoAttaccante.bersaglioColpito[3]:
                robot = GlobalImgVar.robomo
                armrob = GlobalImgVar.armrobmo
                surriscalda = 0
    return robot, armrob, surriscalda


def animaColcoFermo(rx, ry, vrx, vry, robot, armrob, armrobS, surriscalda, tecnicaUsata, azioniDaEseguire, animazioneColcoFatta, raffreddamento, ricarica1, ricarica2, raffredda, autoRic1, autoRic2, nemicoInquadrato, fineanimaz):
    if (not ("attaccoColco" in azioniDaEseguire and tecnicaUsata != "spostamento") and not ("movimentoColcoNemiciPersonaggi" in azioniDaEseguire and tecnicaUsata == "spostamento")) or fineanimaz == 0:
        if animazioneColcoFatta or robot == GlobalImgVar.robomo:
            x = rx
            y = ry
        else:
            x = vrx
            y = vry
        if (raffreddamento and animazioneColcoFatta) or (raffredda >= 0 and not raffreddamento):
            GlobalHWVar.disegnaImmagineSuSchermo(armrobS, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robos, (x, y))
            imgAnimazione = 0
            i = 0
            while i < len(GlobalImgVar.vetAnimazioniTecniche):
                if GlobalImgVar.vetAnimazioniTecniche[i] == "raffred":
                    imgAnimazione = GlobalImgVar.vetAnimazioniTecniche[i + 1][0]
                    break
                i += 2
            GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione, (x, y))
        elif (ricarica1 and animazioneColcoFatta) or (autoRic1 >= 0 and not ricarica1):
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robomo, (x, y))
            imgAnimazione = 0
            i = 0
            while i < len(GlobalImgVar.vetAnimazioniTecniche):
                if GlobalImgVar.vetAnimazioniTecniche[i] == "ricarica":
                    imgAnimazione = GlobalImgVar.vetAnimazioniTecniche[i + 1][0]
                    break
                i += 2
            GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione, (x, y))
        elif (ricarica2 and animazioneColcoFatta) or (autoRic2 >= 0 and not ricarica2):
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robomo, (x, y))
            imgAnimazione = 0
            i = 0
            while i < len(GlobalImgVar.vetAnimazioniTecniche):
                if GlobalImgVar.vetAnimazioniTecniche[i] == "ricarica+":
                    imgAnimazione = GlobalImgVar.vetAnimazioniTecniche[i + 1][0]
                    break
                i += 2
            GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione, (x, y))
        else:
            GlobalHWVar.disegnaImmagineSuSchermo(robot, (x, y))
            if surriscalda > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboSurrisc, (x, y))
            GlobalHWVar.disegnaImmagineSuSchermo(armrob, (x, y))
        if nemicoInquadrato == "Colco":
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (x, y))


def animaSpostamentoNemici(listaNemici, animazioneNemici, cambiosta, nemicoInquadrato, fineanimaz):
    if not cambiosta:
        for nemico in listaNemici:
            if nemico.animaSpostamento and not nemico.morto and (nemico.x != nemico.vx or nemico.y != nemico.vy):
                if not GlobalHWVar.canaleSoundPassiNemiciPersonaggi.get_busy() and fineanimaz > 6:
                    GlobalHWVar.canaleSoundPassiNemiciPersonaggi.play(GlobalSndVar.rumoreMovimentoNemici)
                nemico.animazioneFatta = True
                animazioneNemici = True
                # rumorecamminataNemico.play()
                if nemico.direzione == "d":
                    if 5 < fineanimaz <= 10:
                        GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgDMov1, (nemico.x - (GlobalHWVar.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[1]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAvvelenamento, (nemico.x - (GlobalHWVar.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[2]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAppiccicato, (nemico.x - (GlobalHWVar.gpx * fineanimaz // 10), nemico.y))
                    if 0 < fineanimaz <= 5:
                        GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgDMov2, (nemico.x - (GlobalHWVar.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[1]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAvvelenamento, (nemico.x - (GlobalHWVar.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[2]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAppiccicato, (nemico.x - (GlobalHWVar.gpx * fineanimaz // 10), nemico.y))
                    if not type(nemicoInquadrato) is str and nemicoInquadrato == nemico:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (nemicoInquadrato.x - (GlobalHWVar.gpx * fineanimaz // 10), nemicoInquadrato.y))
                if nemico.direzione == "a":
                    if 5 < fineanimaz <= 10:
                        GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAMov1, (nemico.x + (GlobalHWVar.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[1]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAvvelenamento, (nemico.x + (GlobalHWVar.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[2]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAppiccicato, (nemico.x + (GlobalHWVar.gpx * fineanimaz // 10), nemico.y))
                    if 0 < fineanimaz <= 5:
                        GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAMov2, (nemico.x + (GlobalHWVar.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[1]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAvvelenamento, (nemico.x + (GlobalHWVar.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[2]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAppiccicato, (nemico.x + (GlobalHWVar.gpx * fineanimaz // 10), nemico.y))
                    if not type(nemicoInquadrato) is str and nemicoInquadrato == nemico:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (nemicoInquadrato.x + (GlobalHWVar.gpx * fineanimaz // 10), nemicoInquadrato.y))
                if nemico.direzione == "w":
                    if 5 < fineanimaz <= 10:
                        GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgWMov1, (nemico.x, nemico.y + (GlobalHWVar.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[1]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAvvelenamento, (nemico.x, nemico.y + (GlobalHWVar.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[2]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAppiccicato, (nemico.x, nemico.y + (GlobalHWVar.gpy * fineanimaz // 10)))
                    if 0 < fineanimaz <= 5:
                        GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgWMov2, (nemico.x, nemico.y + (GlobalHWVar.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[1]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAvvelenamento, (nemico.x, nemico.y + (GlobalHWVar.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[2]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAppiccicato, (nemico.x, nemico.y + (GlobalHWVar.gpy * fineanimaz // 10)))
                    if not type(nemicoInquadrato) is str and nemicoInquadrato == nemico:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (nemicoInquadrato.x, nemicoInquadrato.y + (GlobalHWVar.gpy * fineanimaz // 10)))
                if nemico.direzione == "s":
                    if 5 < fineanimaz <= 10:
                        GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgSMov1, (nemico.x, nemico.y - (GlobalHWVar.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[1]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAvvelenamento, (nemico.x, nemico.y - (GlobalHWVar.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[2]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAppiccicato, (nemico.x, nemico.y - (GlobalHWVar.gpy * fineanimaz // 10)))
                    if 0 < fineanimaz <= 5:
                        GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgSMov2, (nemico.x, nemico.y - (GlobalHWVar.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[1]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAvvelenamento, (nemico.x, nemico.y - (GlobalHWVar.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[2]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAppiccicato, (nemico.x, nemico.y - (GlobalHWVar.gpy * fineanimaz // 10)))
                    if not type(nemicoInquadrato) is str and nemicoInquadrato == nemico:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (nemicoInquadrato.x, nemicoInquadrato.y - (GlobalHWVar.gpy * fineanimaz // 10)))
    return animazioneNemici


def animaAttaccoNemici(nemicoAttaccante, animazioneNemici, nemicoInquadrato, fineanimaz):
    if nemicoAttaccante and fineanimaz != 0:
        if nemicoAttaccante.animaAttacco and not nemicoAttaccante.animazioneFatta:
            if fineanimaz == 1:
                nemicoAttaccante.animazioneFatta = True
            animazioneNemici = True
            if fineanimaz == 10:
                if nemicoAttaccante.attaccaDaLontano:
                    GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.rumoreLancioOggettoNemico)
                else:
                    GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.rumoreAttaccoNemico)
            if fineanimaz == 5 and nemicoAttaccante.attaccaDaLontano:
                GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.rumoreAttaccoNemico)
            if nemicoAttaccante.direzione == "w":
                GlobalHWVar.disegnaImmagineSuSchermo(nemicoAttaccante.imgAttaccoW, (nemicoAttaccante.x, nemicoAttaccante.y - GlobalHWVar.gpy))
            if nemicoAttaccante.direzione == "a":
                GlobalHWVar.disegnaImmagineSuSchermo(nemicoAttaccante.imgAttaccoA, (nemicoAttaccante.x - GlobalHWVar.gpx, nemicoAttaccante.y))
            if nemicoAttaccante.direzione == "s":
                GlobalHWVar.disegnaImmagineSuSchermo(nemicoAttaccante.imgAttaccoS, (nemicoAttaccante.x, nemicoAttaccante.y))
            if nemicoAttaccante.direzione == "d":
                GlobalHWVar.disegnaImmagineSuSchermo(nemicoAttaccante.imgAttaccoD, (nemicoAttaccante.x, nemicoAttaccante.y))
            if nemicoAttaccante.statoInizioTurno[1]:
                GlobalHWVar.disegnaImmagineSuSchermo(nemicoAttaccante.imgAvvelenamento, (nemicoAttaccante.x, nemicoAttaccante.y))
            if nemicoAttaccante.statoInizioTurno[2]:
                GlobalHWVar.disegnaImmagineSuSchermo(nemicoAttaccante.imgAppiccicato, (nemicoAttaccante.x, nemicoAttaccante.y))
            if not type(nemicoInquadrato) is str and nemicoInquadrato == nemicoAttaccante:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (nemicoInquadrato.x, nemicoInquadrato.y))
    return animazioneNemici


def animaDanneggiamentoNemici(attaccoADistanza, animaOggetto, listaNemici, animazioneNemici, cambiosta, azioniDaEseguire, attaccante, nemicoInquadrato, fineanimaz):
    if not cambiosta:
        for nemico in listaNemici:
            if (len(nemico.animaDanneggiamento) > 0 and "Rallo" in nemico.animaDanneggiamento and "attaccoRallo" in azioniDaEseguire) or (len(nemico.animaDanneggiamento) > 0 and "Colco" in nemico.animaDanneggiamento and "attaccoColco" in azioniDaEseguire):
                animazioneNemici = True

                nemicoUccisoDallAttualeAttacante = False
                i = 0
                while i < len(nemico.animaDanneggiamento):
                    if "attaccoRallo" in azioniDaEseguire and nemico.animaDanneggiamento[i] == "Rallo":
                        nemicoUccisoDallAttualeAttacante = nemico.animaDanneggiamento[i + 1]
                    if "attaccoColco" in azioniDaEseguire and nemico.animaDanneggiamento[i] == "Colco":
                        nemicoUccisoDallAttualeAttacante = nemico.animaDanneggiamento[i + 1]
                    i += 2
                if nemico.animaMorte and nemicoUccisoDallAttualeAttacante:
                    if not GlobalHWVar.canaleSoundMorteNemici.get_busy() and fineanimaz == 5:
                        GlobalHWVar.canaleSoundMorteNemici.play(GlobalSndVar.rumoreMorteNemico)
                    nemico.animazioneFatta = True
                    if fineanimaz > 5 or (0 < fineanimaz <= 5 and fineanimaz % 4 == 0):
                        GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAttuale, (nemico.vx, nemico.vy))
                        if nemico.statoInizioTurno[1]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAvvelenamento, (nemico.vx, nemico.vy))
                        if nemico.statoInizioTurno[2]:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAppiccicato, (nemico.vx, nemico.vy))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAttuale, (nemico.vx, nemico.vy))
                    if nemico.statoInizioTurno[1]:
                        GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAvvelenamento, (nemico.vx, nemico.vy))
                    if nemico.statoInizioTurno[2]:
                        GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAppiccicato, (nemico.vx, nemico.vy))
                    if not type(nemicoInquadrato) is str and nemicoInquadrato == nemico:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (nemicoInquadrato.vx, nemicoInquadrato.vy))

                if attaccante == "Rallo":
                    if attaccoADistanza or animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata":
                        if fineanimaz <= 5:
                            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgDanneggiamentoRallo, (nemico.vx, nemico.vy))
                    else:
                        GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgDanneggiamentoRallo, (nemico.vx, nemico.vy))
                if attaccante == "Colco" and fineanimaz <= 5:
                    GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgDanneggiamentoColco, (nemico.vx, nemico.vy))
    return animazioneNemici


def animaNemiciFermi(listaNemici, azioniDaEseguire, cambiosta, nemicoAttaccante, nemicoInquadrato, fineanimaz):
    if not cambiosta:
        for nemico in listaNemici:
            if nemico.inCasellaVista and ((not (("movimentoColcoNemiciPersonaggi" in azioniDaEseguire and (nemico.animaSpostamento or nemico.animaMorte)) or ("attaccoNemici" in azioniDaEseguire and nemico.animaAttacco and nemicoAttaccante == nemico) or ("attaccoRallo" in azioniDaEseguire and len(nemico.animaDanneggiamento) > 0 and "Rallo" in nemico.animaDanneggiamento) or ("attaccoColco" in azioniDaEseguire and len(nemico.animaDanneggiamento) > 0 and "Colco" in nemico.animaDanneggiamento)) and not (nemico.animaMorte and nemico.animazioneFatta)) or (fineanimaz == 0 and not nemico.animaMorte)):
                if nemico.animazioneFatta:
                    GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAttuale, (nemico.x, nemico.y))
                    if nemico.statoInizioTurno[1]:
                        GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAvvelenamento, (nemico.x, nemico.y))
                    if nemico.statoInizioTurno[2]:
                        GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAppiccicato, (nemico.x, nemico.y))
                    if not type(nemicoInquadrato) is str and nemicoInquadrato == nemico:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (nemicoInquadrato.x, nemicoInquadrato.y))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAttuale, (nemico.vx, nemico.vy))
                    if nemico.statoInizioTurno[1]:
                        GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAvvelenamento, (nemico.vx, nemico.vy))
                    if nemico.statoInizioTurno[2]:
                        GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAppiccicato, (nemico.vx, nemico.vy))
                    if not type(nemicoInquadrato) is str and nemicoInquadrato == nemico:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (nemicoInquadrato.vx, nemicoInquadrato.vy))


def animaEsche(vettoreEsche, caseviste, azioniDaEseguire, animaOggetto, vettoreImgCaselle, morteEscheAnimata, nemicoInquadrato):
    if "attaccoRallo" in azioniDaEseguire and animaOggetto[0] == "esca":
        c = 0
        while c < len(vettoreImgCaselle):
            if animaOggetto[1] == vettoreImgCaselle[c] and animaOggetto[2] == vettoreImgCaselle[c + 1]:
                GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[c + 2], (vettoreImgCaselle[c], vettoreImgCaselle[c + 1]))
                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[c], vettoreImgCaselle[c + 1])
                break
            c += 3
    elif not "attaccoRallo" in azioniDaEseguire and animaOggetto[0] == "esca":
        c = 0
        while c < len(vettoreImgCaselle):
            if animaOggetto[1] == vettoreImgCaselle[c] and animaOggetto[2] == vettoreImgCaselle[c + 1]:
                GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[c + 2], (vettoreImgCaselle[c], vettoreImgCaselle[c + 1]))
                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[c], vettoreImgCaselle[c + 1])
                break
            c += 3
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.vetIcoOggettiMenu[7], (animaOggetto[1], animaOggetto[2]))
    i = 0
    while i < len(vettoreEsche):
        if not (animaOggetto[0] == "esca" and animaOggetto[1] == vettoreEsche[i + 2] and animaOggetto[2] == vettoreEsche[i + 3]):
            contatore = 0
            while contatore < len(morteEscheAnimata):
                if morteEscheAnimata[contatore] == vettoreEsche[i] and not morteEscheAnimata[contatore + 1]:
                    j = 0
                    while j < len(caseviste):
                        if caseviste[j] == vettoreEsche[i + 2] and caseviste[j + 1] == vettoreEsche[i + 3]:
                            if caseviste[j + 2]:
                                c = 0
                                while c < len(vettoreImgCaselle):
                                    if vettoreEsche[i + 2] == vettoreImgCaselle[c] and vettoreEsche[i + 3] == vettoreImgCaselle[c + 1]:
                                        GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[c + 2], (vettoreImgCaselle[c], vettoreImgCaselle[c + 1]))
                                        FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[c], vettoreImgCaselle[c + 1])
                                        break
                                    c += 3
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.esche, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                                if type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
                                    idEscaInquadrata = int(nemicoInquadrato[4:])
                                    if idEscaInquadrata == vettoreEsche[i]:
                                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                            break
                        j += 3
                    break
                contatore += 2
        i += 4


def animaMorteEsche(x, y, vettoreEsche, vettoreImgCaselle, nemicoAttaccante, attaccoDiColco, attaccoDiRallo, morteEscheAnimata, azioniDaEseguire, fineanimaz):
    escheMorte = []
    if "attaccoRallo" in azioniDaEseguire and len(attaccoDiRallo) > 0:
        i = 0
        while i < len(vettoreEsche):
            k = 0
            while k < len(attaccoDiRallo):
                if type(attaccoDiRallo[k]) is str and attaccoDiRallo[k].startswith("Esca") and int(attaccoDiRallo[k].split(":")[1]) == vettoreEsche[i]:
                    if (abs(x - vettoreEsche[i + 2]) == GlobalHWVar.gpx and abs(y - vettoreEsche[i + 3]) == 0) or (abs(x - vettoreEsche[i + 2]) == 0 and abs(y - vettoreEsche[i + 3]) == GlobalHWVar.gpy):
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgDanneggiamentoCausaRallo, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                    elif fineanimaz <= 5:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgDanneggiamentoCausaRallo, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                    numEsca = int(attaccoDiRallo[k].split(":")[1])
                    if attaccoDiRallo[k + 2] == "morte":
                        escheMorte.append(numEsca)
                    break
                k += 3
            i += 4
    if "attaccoColco" in azioniDaEseguire and len(attaccoDiColco) > 0:
        i = 0
        while i < len(vettoreEsche):
            k = 0
            while k < len(attaccoDiColco):
                if type(attaccoDiColco[k]) is str and attaccoDiColco[k].startswith("Esca") and int(attaccoDiColco[k].split(":")[1]) == vettoreEsche[i]:
                    if fineanimaz <= 5:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgDanneggiamentoCausaColco, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                    numEsca = int(attaccoDiColco[k].split(":")[1])
                    if attaccoDiColco[k + 2] == "morte":
                        escheMorte.append(numEsca)
                    break
                k += 3
            i += 4
    elif "attaccoNemici" in azioniDaEseguire and len(nemicoAttaccante.bersaglioColpito) > 0 and nemicoAttaccante.bersaglioColpito[0].startswith("Esca"):
        numEsca = int(nemicoAttaccante.bersaglioColpito[0].replace("Esca", ""))
        if nemicoAttaccante.bersaglioColpito[3]:
            escheMorte.append(numEsca)

    if len(escheMorte) > 0:
        i = 0
        while i < len(vettoreEsche):
            if vettoreEsche[i] in escheMorte:
                if not GlobalHWVar.canaleSoundMorteNemici.get_busy() and fineanimaz == 5:
                    GlobalHWVar.canaleSoundMorteNemici.play(GlobalSndVar.rumoreMorteNemico)
                c = 0
                while c < len(vettoreImgCaselle):
                    if vettoreEsche[i + 2] == vettoreImgCaselle[c] and vettoreEsche[i + 3] == vettoreImgCaselle[c + 1]:
                        GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[c + 2], (vettoreImgCaselle[c], vettoreImgCaselle[c + 1]))
                        FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[c], vettoreImgCaselle[c + 1])
                        break
                    c += 3
                if fineanimaz > 5 or (0 < fineanimaz <= 5 and fineanimaz % 4 == 0):
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.esche, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                if "attaccoRallo" in azioniDaEseguire:
                    if (abs(x - vettoreEsche[i + 2]) == GlobalHWVar.gpx and abs(y - vettoreEsche[i + 3]) == 0) or (abs(x - vettoreEsche[i + 2]) == 0 and abs(y - vettoreEsche[i + 3]) == GlobalHWVar.gpy):
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgDanneggiamentoCausaRallo, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                    elif fineanimaz <= 5:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgDanneggiamentoCausaRallo, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                if "attaccoColco" in azioniDaEseguire:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgDanneggiamentoCausaColco, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                j = 0
                while j < len(morteEscheAnimata):
                    if vettoreEsche[i] == morteEscheAnimata[j]:
                        morteEscheAnimata[j + 1] = True
                        break
                    j += 2
            i += 4

    return morteEscheAnimata


def animaDenaro(vettoreDenaro, caseviste, vettoreImgCaselle):
    i = 0
    while i < len(vettoreDenaro):
        j = 0
        while j < len(caseviste):
            if caseviste[j] == vettoreDenaro[i + 1] and caseviste[j + 1] == vettoreDenaro[i + 2]:
                if caseviste[j + 2]:
                    c = 0
                    while c < len(vettoreImgCaselle):
                        if vettoreDenaro[i + 1] == vettoreImgCaselle[c] and vettoreDenaro[i + 2] == vettoreImgCaselle[c + 1]:
                            GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[c + 2], (vettoreImgCaselle[c], vettoreImgCaselle[c + 1]))
                            FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[c], vettoreImgCaselle[c + 1])
                            break
                        c += 3
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sacchettoDenaro, (vettoreDenaro[i + 1], vettoreDenaro[i + 2]))
                break
            j += 3
        i += 3


def animaAperturaCofanetto(tesoro, x, y, npers, vettoreImgCaselle, animazioneRallo):
    if tesoro != -1:
        animazioneRallo = True
        i = 0
        while i < len(vettoreImgCaselle):
            if (npers == 1 and x + GlobalHWVar.gpx == vettoreImgCaselle[i] and y == vettoreImgCaselle[i + 1]) or (npers == 2 and x - GlobalHWVar.gpx == vettoreImgCaselle[i] and y == vettoreImgCaselle[i + 1]) or (npers == 3 and x == vettoreImgCaselle[i] and y - GlobalHWVar.gpy == vettoreImgCaselle[i + 1]) or (npers == 4 and x == vettoreImgCaselle[i] and y + GlobalHWVar.gpy == vettoreImgCaselle[i + 1]):
                GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                break
            i += 3
        if npers == 1:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.cofaniaper, (x + GlobalHWVar.gpx, y))
        if npers == 2:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.cofaniaper, (x - GlobalHWVar.gpx, y))
        if npers == 3:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.cofaniaper, (x, y - GlobalHWVar.gpy))
        if npers == 4:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.cofaniaper, (x, y + GlobalHWVar.gpy))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfocontcof, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 0))
        if tesoro == -2:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Niente", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        # 31-40 -> oggetti(10) / 41-70 -> armi(30) / 71-75 -> batterie(5) / 81-100 -> condizioni(20) / 101-120 -> gambit (=celle di memoria)(20) / 131 -> monete / 132 frecce
        elif tesoro >= 11 and tesoro <= 30:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Azio-ImpoFoglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 31:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Pozione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == -31:
            FunzioniGraficheGeneriche.messaggio(u"Hai già troppe Pozioni!", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 32:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: ImpoFrutto piccolo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == -32:
            FunzioniGraficheGeneriche.messaggio(u"Hai già troppi ImpoFrutti piccoli!", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 33:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Medicina", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == -33:
            FunzioniGraficheGeneriche.messaggio(u"Hai già troppe Medicine!", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 34:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Superpozione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == -34:
            FunzioniGraficheGeneriche.messaggio(u"Hai già troppe Superpozioni!", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 35:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: ImpoFrutto grande", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == -35:
            FunzioniGraficheGeneriche.messaggio(u"Hai già troppi ImpoFrutti grandi!", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 36:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Bomba", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == -36:
            FunzioniGraficheGeneriche.messaggio(u"Hai già troppe Bombe!", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 37:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Bomba velenosa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == -37:
            FunzioniGraficheGeneriche.messaggio(u"Hai già troppe Bombe velenose!", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 38:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Esca", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == -38:
            FunzioniGraficheGeneriche.messaggio(u"Hai già troppe Esche!", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 39:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Bomba appiccicosa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == -39:
            FunzioniGraficheGeneriche.messaggio(u"Hai già troppe Bombe appiccicose!", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 40:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Bomba potenziata", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == -40:
            FunzioniGraficheGeneriche.messaggio(u"Hai già troppe Bombe potenziate!", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 41:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Niente", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 42:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Spada di ferro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 43:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Spadone d'acciaio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 44:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Lykother", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 45:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Mendaxritas", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 46:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Niente", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 47:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Arco di legno", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 48:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Arco di ferro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 49:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Arco di precisione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 50:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Accipiter", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 51:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Niente", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 52:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Armatura di pelle", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 53:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Armatura d'acciaio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 54:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Lykodes", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 55:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Loriquam", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 56:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Niente", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 57:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Scudo di pelle", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 58:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Scudo d'acciaio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 59:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Lykethmos", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 60:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Clipequam", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 61:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Niente", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 62:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Guanti vitali", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 63:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Guanti difensivi", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 64:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Guanti offensivi", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 65:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Guanti confortevoli", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 66:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Niente", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 67:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Collana rigenerante", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 68:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Collana medicinale", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 69:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Apprendimaschera", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 70:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Portafortuna", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 71:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Sacca Energetica piccola", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 72:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Sacca Energetica discreta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 73:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Sacca Energetica capiente", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 74:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Sacca Energetica enorme", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 75:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Sacca Energetica illimitata", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro >= 81 and tesoro <= 100:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Condizio-ImpoFoglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 1000:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: Cella di memoria", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 131:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: 50 monete", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == 132:
            FunzioniGraficheGeneriche.messaggio("Hai trovato: 1 freccia", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
        elif tesoro == -132:
            FunzioniGraficheGeneriche.messaggio(u"Hai già troppe frecce!", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)

    return animazioneRallo


def animaRaccoltaDenaro(x, y, vettoreDenaro, fineanimaz):
    denaroRaccolto = False
    i = 0
    while i < len(vettoreDenaro):
        if vettoreDenaro[i + 1] == x and vettoreDenaro[i + 2] == y:
            if fineanimaz == 1:
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoRaccoltaMonete)
            if GlobalHWVar.canaleSoundPassiRallo.get_busy():
                GlobalHWVar.canaleSoundPassiRallo.stop()
            denaroTrovato = vettoreDenaro[i]
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfocontcof, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 0))
            FunzioniGraficheGeneriche.messaggio("Monete trovate: " + str(denaroTrovato), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, 60)
            denaroRaccolto = True
            break
        i += 3
    return denaroRaccolto


def eliminaOggettoLanciato(x, y, attaccoADistanza, animaOggetto, rx, ry, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoAttaccante, schermo_prima_delle_animazioni, cambiosta, azioniDaEseguire, vettoreEsche, fineanimaz):
    # disegno il terreno sotto le frecce lanciate da Rallo
    if "attaccoRallo" in azioniDaEseguire and (attaccoADistanza or animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata") and not cambiosta:
        xInizioRetta = x
        yInizioRetta = y
        if animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata":
            xFineRetta = animaOggetto[1]
            yFineRetta = animaOggetto[2]
        else:
            if type(attaccoADistanza) is str and attaccoADistanza.startswith("Esca"):
                idEsca = int(attaccoADistanza.split(":")[1])
                xFineRetta = 0
                yFineRetta = 0
                i = 0
                while i < len(vettoreEsche):
                    if vettoreEsche[i] == idEsca:
                        xFineRetta = vettoreEsche[i + 2]
                        yFineRetta = vettoreEsche[i + 3]
                        break
                    i += 4
            else:
                xFineRetta = attaccoADistanza.vx
                yFineRetta = attaccoADistanza.vy
        global quadrettoSottoLaFreccia
        global quadrettoSottoEsplosione
        if fineanimaz > 5:
            if fineanimaz == 10 and (animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata"):
                quadrettoSottoEsplosione = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xFineRetta - (GlobalHWVar.gpx * 2), yFineRetta - (GlobalHWVar.gpy * 2), GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5)).convert()
            if fineanimaz != 10:
                GlobalHWVar.disegnaImmagineSuSchermo(quadrettoSottoLaFreccia, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz) - GlobalHWVar.gpx), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalHWVar.gpy))
            quadrettoSottoLaFreccia = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)) - GlobalHWVar.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz)) - GlobalHWVar.gpy, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3)).convert()
        elif fineanimaz == 5:
            GlobalHWVar.disegnaImmagineSuSchermo(quadrettoSottoLaFreccia, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz)) - GlobalHWVar.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalHWVar.gpy))
        elif fineanimaz == 0 and (animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata"):
            GlobalHWVar.disegnaImmagineSuSchermo(quadrettoSottoEsplosione, ((xFineRetta - (GlobalHWVar.gpx * 2), yFineRetta - (GlobalHWVar.gpy * 2))))

    # disegno il terreno sotto le frecce elettriche lanciate da Colco
    if "attaccoColco" in azioniDaEseguire and listaNemiciAttaccatiADistanzaRobo and len(listaNemiciAttaccatiADistanzaRobo) == 1 and tecnicaUsata.startswith("freccia") and not cambiosta:
        xInizioRetta = rx
        yInizioRetta = ry
        if listaNemiciAttaccatiADistanzaRobo[0] == "Rallo":
            xFineRetta = x
            yFineRetta = y
        else:
            xFineRetta = listaNemiciAttaccatiADistanzaRobo[0].vx
            yFineRetta = listaNemiciAttaccatiADistanzaRobo[0].vy
        global quadrettoSottoLaFrecciaElettrica
        if fineanimaz > 5:
            if fineanimaz != 10:
                GlobalHWVar.disegnaImmagineSuSchermo(quadrettoSottoLaFrecciaElettrica, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz) - GlobalHWVar.gpx), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalHWVar.gpy))
            quadrettoSottoLaFrecciaElettrica = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)) - GlobalHWVar.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz)) - GlobalHWVar.gpy, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3)).convert()
        elif fineanimaz == 5:
            GlobalHWVar.disegnaImmagineSuSchermo(quadrettoSottoLaFrecciaElettrica, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz)) - GlobalHWVar.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalHWVar.gpy))

    # disegno il terreno sotto gli oggetti lanciati dai nemici
    if "attaccoNemici" in azioniDaEseguire and nemicoAttaccante:
        if nemicoAttaccante.attaccaDaLontano and nemicoAttaccante.animaAttacco and not nemicoAttaccante.morto:
            xInizioRetta = nemicoAttaccante.x
            xFineRetta = nemicoAttaccante.obbiettivo[1]
            yInizioRetta = nemicoAttaccante.y
            yFineRetta = nemicoAttaccante.obbiettivo[2]
            if fineanimaz > 5:
                if fineanimaz != 10:
                    GlobalHWVar.disegnaImmagineSuSchermo(nemicoAttaccante.quadrettoSottoOggettoLanciato, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz) - GlobalHWVar.gpx), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalHWVar.gpy))
                nemicoAttaccante.quadrettoSottoOggettoLanciato = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)) - GlobalHWVar.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz)) - GlobalHWVar.gpy, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3)).convert()
            elif fineanimaz == 5:
                GlobalHWVar.disegnaImmagineSuSchermo(nemicoAttaccante.quadrettoSottoOggettoLanciato, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz)) - GlobalHWVar.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalHWVar.gpy))


def disegnaCasellaAccantoAlPersCheAttacca(x, y, attacco, npers, rx, ry, nrob, tecnicaUsata, nemicoAttaccante, schermo_prima_delle_animazioni, cambiosta, azioniDaEseguire, fineanimaz):
    if "attaccoRallo" in azioniDaEseguire and attacco == 1:
        global quadrettoSottoLaSpada
        xAttaccoPers = 0
        yAttaccoPers = 0
        # 1=d, 2=a, 3=w, 4=s
        if npers == 1:
            xAttaccoPers = x + GlobalHWVar.gpx
            yAttaccoPers = y
        if npers == 2:
            xAttaccoPers = x - GlobalHWVar.gpx
            yAttaccoPers = y
        if npers == 3:
            xAttaccoPers = x
            yAttaccoPers = y - GlobalHWVar.gpy
        if npers == 4:
            xAttaccoPers = x
            yAttaccoPers = y + GlobalHWVar.gpy
        if fineanimaz == 10:
            quadrettoSottoLaSpada = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xAttaccoPers, yAttaccoPers, GlobalHWVar.gpx, GlobalHWVar.gpy)).convert()
        else:
            GlobalHWVar.disegnaImmagineSuSchermo(quadrettoSottoLaSpada, (xAttaccoPers, yAttaccoPers))

    if "attaccoColco" in azioniDaEseguire:
        global quadrettoSottoAttaccoColco
        if tecnicaUsata.startswith("scossa") or tecnicaUsata.startswith("freccia") or tecnicaUsata.startswith("cura") or tecnicaUsata == "antidoto" or tecnicaUsata == "attP" or tecnicaUsata == "difP":
            xAttaccoPers = 0
            yAttaccoPers = 0
            # nrob => 1=d, 2=a, 3=s, 4=w
            if nrob == 1:
                xAttaccoPers = rx + GlobalHWVar.gpx
                yAttaccoPers = ry
            if nrob == 2:
                xAttaccoPers = rx - GlobalHWVar.gpx
                yAttaccoPers = ry
            if nrob == 3:
                xAttaccoPers = rx
                yAttaccoPers = ry + GlobalHWVar.gpy
            if nrob == 4:
                xAttaccoPers = rx
                yAttaccoPers = ry - GlobalHWVar.gpy
            if fineanimaz == 10:
                quadrettoSottoAttaccoColco = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xAttaccoPers, yAttaccoPers, GlobalHWVar.gpx, GlobalHWVar.gpy)).convert()
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(quadrettoSottoAttaccoColco, (xAttaccoPers, yAttaccoPers))
        elif tecnicaUsata.startswith("tempesta"):
            xAttaccoPers = rx - (GlobalHWVar.gpx * 8)
            yAttaccoPers = ry - (GlobalHWVar.gpy * 8)
            xFineAttaccoPers = GlobalHWVar.gpx * 8
            yFineAttaccoPers = GlobalHWVar.gpy * 8
            if xAttaccoPers < 0:
                xAttaccoPers = 0
            if yAttaccoPers < 0:
                yAttaccoPers = 0
            if rx + xFineAttaccoPers >= GlobalHWVar.gsx:
                xFineAttaccoPers = GlobalHWVar.gsx - rx - GlobalHWVar.gpx
            if ry + yFineAttaccoPers >= GlobalHWVar.gsy:
                yFineAttaccoPers = GlobalHWVar.gsy - ry - GlobalHWVar.gpy
            if fineanimaz == 10:
                quadrettoSottoAttaccoColco = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xAttaccoPers, yAttaccoPers, (GlobalHWVar.gpx * 9) + xFineAttaccoPers, (GlobalHWVar.gpy * 9) + yFineAttaccoPers)).convert()
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(quadrettoSottoAttaccoColco, (xAttaccoPers, yAttaccoPers))

    if "attaccoNemici" in azioniDaEseguire and nemicoAttaccante and not cambiosta:
        if nemicoAttaccante.animaAttacco:
            xAttaccoNemico = 0
            yAttaccoNemico = 0
            if nemicoAttaccante.direzione == "w":
                xAttaccoNemico = nemicoAttaccante.x
                yAttaccoNemico = nemicoAttaccante.y - GlobalHWVar.gpy
            if nemicoAttaccante.direzione == "a":
                xAttaccoNemico = nemicoAttaccante.x - GlobalHWVar.gpx
                yAttaccoNemico = nemicoAttaccante.y
            if nemicoAttaccante.direzione == "s":
                xAttaccoNemico = nemicoAttaccante.x
                yAttaccoNemico = nemicoAttaccante.y + GlobalHWVar.gpy
            if nemicoAttaccante.direzione == "d":
                xAttaccoNemico = nemicoAttaccante.x + GlobalHWVar.gpx
                yAttaccoNemico = nemicoAttaccante.y
            if fineanimaz == 10:
                nemicoAttaccante.quadrettoSottoArma = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xAttaccoNemico, yAttaccoNemico, GlobalHWVar.gpx, GlobalHWVar.gpy)).convert()
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(nemicoAttaccante.quadrettoSottoArma, (xAttaccoNemico, yAttaccoNemico))


def animaFrecceLanciate(x, y, attaccoADistanza, animaOggetto, rx, ry, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoAttaccante, cambiosta, azioniDaEseguire, vettoreEsche, fineanimaz):
    # disegno le frecce e gli oggetti lanciati da Rallo
    if "attaccoRallo" in azioniDaEseguire and (attaccoADistanza or animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata") and not cambiosta:
        xInizioRetta = x
        yInizioRetta = y
        if animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata":
            if fineanimaz == 10:
                GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.suonoLancioOggetti)
            xFineRetta = animaOggetto[1]
            yFineRetta = animaOggetto[2]
            imgFrecciaLanciata_temp = 0
            if animaOggetto[0] == "bomba":
                imgFrecciaLanciata_temp = GlobalImgVar.vetIcoOggettiMenu[5]
            elif animaOggetto[0] == "bombaVeleno":
                imgFrecciaLanciata_temp = GlobalImgVar.vetIcoOggettiMenu[6]
            elif animaOggetto[0] == "esca":
                imgFrecciaLanciata_temp = GlobalImgVar.vetIcoOggettiMenu[7]
            elif animaOggetto[0] == "bombaAppiccicosa":
                imgFrecciaLanciata_temp = GlobalImgVar.vetIcoOggettiMenu[8]
            elif animaOggetto[0] == "bombaPotenziata":
                imgFrecciaLanciata_temp = GlobalImgVar.vetIcoOggettiMenu[9]
        else:
            if type(attaccoADistanza) is str and attaccoADistanza.startswith("Esca"):
                idEsca = int(attaccoADistanza.split(":")[1])
                xFineRetta = 0
                yFineRetta = 0
                i = 0
                while i < len(vettoreEsche):
                    if vettoreEsche[i] == idEsca:
                        xFineRetta = vettoreEsche[i + 2]
                        yFineRetta = vettoreEsche[i + 3]
                        break
                    i += 4
            else:
                xFineRetta = attaccoADistanza.vx
                yFineRetta = attaccoADistanza.vy
            deltaXRetta = xFineRetta - xInizioRetta
            deltaYRetta = yFineRetta - yInizioRetta
            angoloInRadianti = -math.atan2(deltaYRetta, deltaXRetta)
            angoloInGradi = math.degrees(angoloInRadianti)
            imgFrecciaLanciata_temp = pygame.transform.rotate(GlobalImgVar.imgFrecciaLanciata, angoloInGradi)
        if fineanimaz > 5:
            GlobalHWVar.disegnaImmagineSuSchermo(imgFrecciaLanciata_temp, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz))))
        elif animaOggetto[0] and fineanimaz > 0:
            if animaOggetto[0] == "bomba":
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgAnimaBomba, (animaOggetto[1] - GlobalHWVar.gpx, animaOggetto[2] - GlobalHWVar.gpy))
                if fineanimaz == 5:
                    GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.suonoUsoBomba)
            elif animaOggetto[0] == "bombaVeleno":
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgAnimaBombaVeleno, (animaOggetto[1], animaOggetto[2]))
                if fineanimaz == 5:
                    GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.suonoUsoBombaVeleno)
            elif animaOggetto[0] == "esca":
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.vetIcoOggettiMenu[7], (animaOggetto[1], animaOggetto[2]))
                if fineanimaz == 5:
                    GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.suonoUsoEsca)
            elif animaOggetto[0] == "bombaAppiccicosa":
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgAnimaBombaAppiccicosa, (animaOggetto[1], animaOggetto[2]))
                if fineanimaz == 5:
                    GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.suonoUsoBombaAppiccicosa)
            elif animaOggetto[0] == "bombaPotenziata":
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgAnimaBombaPotenziata, (animaOggetto[1] - (GlobalHWVar.gpx * 2), animaOggetto[2] - (GlobalHWVar.gpy * 2)))
                if fineanimaz == 5:
                    GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.suonoUsoBombaPotenziata)

    # disegno le frecce elettriche lanciate da Colco
    if "attaccoColco" in azioniDaEseguire and listaNemiciAttaccatiADistanzaRobo and len(listaNemiciAttaccatiADistanzaRobo) == 1 and tecnicaUsata.startswith("freccia") and not cambiosta:
        xInizioRetta = rx
        yInizioRetta = ry
        if listaNemiciAttaccatiADistanzaRobo[0] == "Rallo":
            xFineRetta = x
            yFineRetta = y
        else:
            xFineRetta = listaNemiciAttaccatiADistanzaRobo[0].vx
            yFineRetta = listaNemiciAttaccatiADistanzaRobo[0].vy
        deltaXRetta = xFineRetta - xInizioRetta
        deltaYRetta = yFineRetta - yInizioRetta
        angoloInRadianti = -math.atan2(deltaYRetta, deltaXRetta)
        angoloInGradi = math.degrees(angoloInRadianti)
        imgFrecciaLanciata_temp = 0
        if tecnicaUsata == "freccia":
            imgFrecciaLanciata_temp = pygame.transform.rotate(GlobalImgVar.imgFrecciaEletttricaLanciata, angoloInGradi)
        elif tecnicaUsata == "freccia+":
            imgFrecciaLanciata_temp = pygame.transform.rotate(GlobalImgVar.imgFrecciaEletttricaLanciataP, angoloInGradi)
        elif tecnicaUsata == "freccia++":
            imgFrecciaLanciata_temp = pygame.transform.rotate(GlobalImgVar.imgFrecciaEletttricaLanciataPP, angoloInGradi)
        if fineanimaz > 5:
            GlobalHWVar.disegnaImmagineSuSchermo(imgFrecciaLanciata_temp, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz))))

    # disegno gli oggetti lanciati dai nemici
    if "attaccoNemici" in azioniDaEseguire and nemicoAttaccante:
        if nemicoAttaccante.attaccaDaLontano and nemicoAttaccante.animaAttacco and not nemicoAttaccante.morto:
            xInizioRetta = nemicoAttaccante.x
            xFineRetta = nemicoAttaccante.obbiettivo[1]
            yInizioRetta = nemicoAttaccante.y
            yFineRetta = nemicoAttaccante.obbiettivo[2]
            deltaXRetta = xFineRetta - xInizioRetta
            deltaYRetta = yFineRetta - yInizioRetta
            angoloInRadianti = -math.atan2(deltaYRetta, deltaXRetta)
            angoloInGradi = math.degrees(angoloInRadianti)
            imgFrecciaLanciata_temp = pygame.transform.rotate(nemicoAttaccante.imgOggettoLanciato, angoloInGradi)
            if fineanimaz > 5:
                GlobalHWVar.disegnaImmagineSuSchermo(imgFrecciaLanciata_temp, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz))))
            elif fineanimaz != 0:
                GlobalHWVar.disegnaImmagineSuSchermo(nemicoAttaccante.imgDanneggiamentoOggettoLanciato, (xFineRetta, yFineRetta))


def animaVitaRalloNemicoInquadrato(dati, nemicoInquadrato, vettoreEsche, difesa, azioniDaEseguire, nemicoAttaccante, attaccoDiRallo, attaccoDiColco, statoRalloInizioTurno, statoColcoInizioTurno, statoEscheInizioTurno, listaNemici, fineanimaz, aumentoliv, apriocchio, chiamarob, saltaTurno):
    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati, difesa)

    # vita-status personaggio (statoRalloInizioTurno[pv, veleno, attP, difP])
    if "attaccoRallo" in azioniDaEseguire and len(attaccoDiRallo) > 0 and "Rallo" in attaccoDiRallo and fineanimaz == 5:
        i = 0
        while i < len(attaccoDiRallo):
            if attaccoDiRallo[i] == "Rallo":
                statoRalloInizioTurno[0] += attaccoDiRallo[i + 1]
                if attaccoDiRallo[i + 2] == "avvelena":
                    statoRalloInizioTurno[1] = True
            i += 3
    if "attaccoNemici" in azioniDaEseguire and len(nemicoAttaccante.bersaglioColpito) > 0 and nemicoAttaccante.bersaglioColpito[0] == "Rallo" and fineanimaz == 5:
        statoRalloInizioTurno[0] += nemicoAttaccante.bersaglioColpito[1]
        if nemicoAttaccante.bersaglioColpito[2] == "avvelena":
            statoRalloInizioTurno[1] = True
    if "attaccoColco" in azioniDaEseguire and len(attaccoDiColco) > 0 and "Rallo" in attaccoDiColco and fineanimaz == 5:
        i = 0
        while i < len(attaccoDiColco):
            if attaccoDiColco[i] == "Rallo":
                statoRalloInizioTurno[0] += attaccoDiColco[i + 1]
                if attaccoDiColco[i + 2] == "antidoto":
                    statoRalloInizioTurno[1] = False
                if attaccoDiColco[i + 2] == "attP":
                    statoRalloInizioTurno[2] = 10
                if attaccoDiColco[i + 2] == "difP":
                    statoRalloInizioTurno[3] = 10
                break
            i += 3
    pvRallo = statoRalloInizioTurno[0]
    velenoRallo = statoRalloInizioTurno[1]
    attPRallo = statoRalloInizioTurno[2]
    difPRallo = statoRalloInizioTurno[3]
    if aumentoliv != 0:
        pvtot = GenericFunc.getVitaTotRallo(dati[4] - aumentoliv, dati[129])
        pvRallo = pvtot
        velenoRallo = False
    lungvitatot = int(((GlobalHWVar.gpx * pvtot) / float(4)) // 5)
    lungvita = (lungvitatot * pvRallo) // pvtot
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
    FunzioniGraficheGeneriche.messaggio(u" ×" + str(dati[132]), GlobalHWVar.grigiochi, int(GlobalHWVar.gsx // 32 * 1.8), int(GlobalHWVar.gsy // 18 * 17.3), 40)
    if velenoRallo:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.avvelenato, (GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 17))
    if attPRallo > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.attaccopiu, (GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 17))
    if difPRallo > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.difesapiu, (GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 17))

    # disegno la vita del Colco / esca / mostro selezionato
    if nemicoInquadrato == "Colco" or (not nemicoInquadrato and dati[0] >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]):
        if "attaccoRallo" in azioniDaEseguire and len(attaccoDiRallo) > 0 and "Colco" in attaccoDiRallo and fineanimaz == 5:
            i = 0
            while i < len(attaccoDiRallo):
                if attaccoDiRallo[i] == "Colco":
                    statoColcoInizioTurno[0] += attaccoDiRallo[i + 1]
                i += 3
        if "attaccoNemici" in azioniDaEseguire and len(nemicoAttaccante.bersaglioColpito) > 0 and nemicoAttaccante.bersaglioColpito[0] == "Colco" and fineanimaz == 5:
            statoColcoInizioTurno[0] += nemicoAttaccante.bersaglioColpito[1]
            if nemicoAttaccante.bersaglioColpito[2] == "surriscalda":
                statoColcoInizioTurno[1] = 10
        if "attaccoColco" in azioniDaEseguire and len(attaccoDiColco) > 0 and "Colco" in attaccoDiColco and fineanimaz == 5:
            i = 0
            while i < len(attaccoDiColco):
                if attaccoDiColco[i] == "Colco":
                    statoColcoInizioTurno[0] += attaccoDiColco[i + 1]
                    if attaccoDiColco[i + 2] == "velocizza":
                        statoColcoInizioTurno[2] = 15
                    if attaccoDiColco[i + 2] == "efficienza":
                        statoColcoInizioTurno[3] = 15
                i += 3
        pvColco = statoColcoInizioTurno[0]
        surriscaldaColco = statoColcoInizioTurno[1]
        velPColco = statoColcoInizioTurno[2]
        effPColco = statoColcoInizioTurno[3]
        lungentot = int(((GlobalHWVar.gpx * entot) / float(4)) // 15)
        lungen = int(((GlobalHWVar.gpx * pvColco) / float(4)) // 15)
        if lungen < 0:
            lungen = 0
        indvitarob = pygame.transform.smoothscale(GlobalImgVar.indvita, (lungentot, GlobalHWVar.gpy // 4))
        fineindvitarob = GlobalImgVar.fineindvita
        vitarob = pygame.transform.smoothscale(GlobalImgVar.vitarobo, (lungen, GlobalHWVar.gpy // 4))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoColco, (0, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(indvitarob, (GlobalHWVar.gpx, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(fineindvitarob, (GlobalHWVar.gpx + lungentot, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(vitarob, (GlobalHWVar.gpx, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robos, (0, 0))
        if surriscaldaColco > 0:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.surriscaldato, (GlobalHWVar.gpx + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
        if velPColco > 0:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.velocitapiu, ((GlobalHWVar.gpx * 2) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
        if effPColco > 0:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.efficienzapiu, ((GlobalHWVar.gpx * 3) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))

    if type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
        idEscaInquadrata = int(nemicoInquadrato[4:])
        i = 0
        while i < len(vettoreEsche):
            if idEscaInquadrata == vettoreEsche[i]:
                idEscaInizioturno = 0
                j = 0
                while j < len(statoEscheInizioTurno):
                    if statoEscheInizioTurno[j] == nemicoInquadrato:
                        idEscaInizioturno = j
                        break
                    j += 2
                if "attaccoNemici" in azioniDaEseguire and len(nemicoAttaccante.bersaglioColpito) > 0 and nemicoAttaccante.bersaglioColpito[0].startswith("Esca") and nemicoAttaccante.bersaglioColpito[0] == nemicoInquadrato and fineanimaz == 5:
                    statoEscheInizioTurno[idEscaInizioturno + 1] += nemicoAttaccante.bersaglioColpito[1]
                if "attaccoColco" in azioniDaEseguire and len(attaccoDiColco) > 0 and fineanimaz == 5:
                    k = 0
                    while k < len(attaccoDiColco):
                        if type(attaccoDiColco[k]) is str and attaccoDiColco[k].startswith("Esca") and int(attaccoDiColco[k].split(":")[1]) == vettoreEsche[i]:
                            statoEscheInizioTurno[idEscaInizioturno + 1] += attaccoDiColco[k + 1]
                            break
                        k += 3
                if "attaccoRallo" in azioniDaEseguire and len(attaccoDiRallo) > 0 and fineanimaz == 5:
                    k = 0
                    while k < len(attaccoDiRallo):
                        if type(attaccoDiRallo[k]) is str and attaccoDiRallo[k].startswith("Esca") and int(attaccoDiRallo[k].split(":")[1]) == vettoreEsche[i]:
                            statoEscheInizioTurno[idEscaInizioturno + 1] += attaccoDiRallo[k + 1]
                            break
                        k += 3
                pvEsca = statoEscheInizioTurno[idEscaInizioturno + 1]
                lungvita = int(((GlobalHWVar.gpx * pvEsca) / float(4)) // 15)
                if lungvita < 0:
                    lungvita = 0
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoEsche, (0, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.esche, (0, 0))
                indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (int(((GlobalHWVar.gpx * GlobalGameVar.vitaTotEsche) / float(4)) // 15), GlobalHWVar.gpy // 4))
                fineindvitamost = GlobalImgVar.fineindvita
                vitaesche = pygame.transform.smoothscale(GlobalImgVar.vitanemico0, (lungvita, GlobalHWVar.gpy // 4))
                GlobalHWVar.disegnaImmagineSuSchermo(indvitamost, (GlobalHWVar.gpx, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + (int(((GlobalHWVar.gpx * GlobalGameVar.vitaTotEsche) / float(4)) // 15)), 0))
                GlobalHWVar.disegnaImmagineSuSchermo(vitaesche, (GlobalHWVar.gpx, 0))
                break
            i += 4

    for nemico in listaNemici:
        if "attaccoRallo" in azioniDaEseguire and len(attaccoDiRallo) > 0 and nemico in attaccoDiRallo and fineanimaz == 5:
            i = 0
            while i < len(attaccoDiRallo):
                if attaccoDiRallo[i] == nemico:
                    nemico.statoInizioTurno[0] += attaccoDiRallo[i + 1]
                    if attaccoDiRallo[i + 2] == "avvelena":
                        nemico.statoInizioTurno[1] = True
                    if attaccoDiRallo[i + 2] == "appiccica":
                        nemico.statoInizioTurno[2] = True
                    break
                i += 3
        if "attaccoColco" in azioniDaEseguire and len(attaccoDiColco) > 0 and nemico in attaccoDiColco and fineanimaz == 5:
            i = 0
            while i < len(attaccoDiColco):
                if attaccoDiColco[i] == nemico:
                    nemico.statoInizioTurno[0] += attaccoDiColco[i + 1]
                    if attaccoDiColco[i + 2] == "antidoto":
                        nemico.statoInizioTurno[1] = False
                    break
                i += 3
    if nemicoInquadrato and not type(nemicoInquadrato) is str:
        pvm = nemicoInquadrato.statoInizioTurno[0]
        nemicoAvvelenato = nemicoInquadrato.statoInizioTurno[1]
        nemicoAppiccicato = nemicoInquadrato.statoInizioTurno[2]
        pvmtot = nemicoInquadrato.vitaTotale
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoMostro, (0, 0))
        if nemicoAvvelenato:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.avvelenato, (GlobalHWVar.gpx + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
        if nemicoAppiccicato:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.appiccicoso, ((GlobalHWVar.gpx * 2) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
        GlobalHWVar.disegnaImmagineSuSchermo(nemicoInquadrato.imgS, (0, 0))
        fineindvitamost = GlobalImgVar.fineindvita
        if pvmtot > 1500:
            indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
            lungvitatot = int(((GlobalHWVar.gpx * 1500) / float(4)) // 15)
            GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + lungvitatot, 0))
            if pvm > 15000:
                pvm = 1500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico9
            elif pvm > 13500:
                pvm -= 13500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico8, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico9
            elif pvm > 12000:
                pvm -= 12000
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico7, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico8
            elif pvm > 10500:
                pvm -= 10500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico6, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico7
            elif pvm > 9000:
                pvm -= 9000
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico5, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico6
            elif pvm > 7500:
                pvm -= 7500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico4, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico5
            elif pvm > 6000:
                pvm -= 6000
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico3, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico4
            elif pvm > 4500:
                pvm -= 4500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico2, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico3
            elif pvm > 3000:
                pvm -= 3000
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico1, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico2
            elif pvm > 1500:
                pvm -= 1500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico0, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico1
            else:
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico0
        else:
            lungvitatot = int(((GlobalHWVar.gpx * pvmtot) / float(4)) // 15)
            indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (lungvitatot, GlobalHWVar.gpy // 4))
            GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + lungvitatot, 0))
            vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (lungvitatot, GlobalHWVar.gpy // 4))
            vitanemico = GlobalImgVar.vitanemico0
        lungvita = int(((GlobalHWVar.gpx * pvm) / float(4)) // 15)
        if lungvita < 0:
            lungvita = 0
        vitanem = pygame.transform.smoothscale(vitanemico, (lungvita, GlobalHWVar.gpy // 4))
        GlobalHWVar.disegnaImmagineSuSchermo(indvitamost, (GlobalHWVar.gpx, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(vitanemsucc, (GlobalHWVar.gpx, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(vitanem, (GlobalHWVar.gpx, 0))

    # backbround saltaTurno/occhio/chiave
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfochiaveocchio, (GlobalHWVar.gpx * 28.5, 0))
    if saltaTurno:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgSaltaTurnoCliccato, (GlobalHWVar.gpx * 30.9, 0))
    else:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgSaltaTurno, (GlobalHWVar.gpx * 30.9, 0))
    # vista nemici
    if apriocchio:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhioape, (GlobalHWVar.gpx * 29.8, 0))
    else:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhiochiu, (GlobalHWVar.gpx * 29.8, 0))
    # chiave robo
    if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
        if chiamarob:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaveroboacc, (GlobalHWVar.gpx * 28.7, 0))
        else:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaverobospe, (GlobalHWVar.gpx * 28.7, 0))

    return statoRalloInizioTurno, statoColcoInizioTurno


def animaPersonaggiFermi(listaPersonaggi, azioniDaEseguire, cambiosta, fineanimaz):
    if not cambiosta:
        for personaggio in listaPersonaggi:
            if personaggio.imgAttuale:
                if (personaggio.inCasellaVista and not personaggio.mantieniSempreASchermo and not ("movimentoColcoNemiciPersonaggi" in azioniDaEseguire and personaggio.animaSpostamento)) or (personaggio.inCasellaVista and fineanimaz == 0):
                    if personaggio.animazioneFatta:
                        GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgAttuale, (personaggio.x, personaggio.y))
                    else:
                        GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgAttuale, (personaggio.vx, personaggio.vy))


def animaSpostamentoPersonaggi(listaPersonaggi, animazionePersonaggi, cambiosta, fineanimaz):
    if not cambiosta:
        for personaggio in listaPersonaggi:
            if personaggio.inCasellaVista and not personaggio.mantieniSempreASchermo and personaggio.animaSpostamento and (personaggio.x != personaggio.vx or personaggio.y != personaggio.vy):
                personaggio.animazioneFatta = True
                animazionePersonaggi = True
                if personaggio.direzione == "d":
                    if 5 < fineanimaz <= 10:
                        GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgDMov1, (personaggio.x - (GlobalHWVar.gpx * fineanimaz // 10), personaggio.y))
                    if 0 < fineanimaz <= 5:
                        GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgDMov2, (personaggio.x - (GlobalHWVar.gpx * fineanimaz // 10), personaggio.y))
                if personaggio.direzione == "a":
                    if 5 < fineanimaz <= 10:
                        GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgAMov1, (personaggio.x + (GlobalHWVar.gpx * fineanimaz // 10), personaggio.y))
                    if 0 < fineanimaz <= 5:
                        GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgAMov2, (personaggio.x + (GlobalHWVar.gpx * fineanimaz // 10), personaggio.y))
                if personaggio.direzione == "w":
                    if 5 < fineanimaz <= 10:
                        GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgWMov1, (personaggio.x, personaggio.y + (GlobalHWVar.gpy * fineanimaz // 10)))
                    if 0 < fineanimaz <= 5:
                        GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgWMov2, (personaggio.x, personaggio.y + (GlobalHWVar.gpy * fineanimaz // 10)))
                if personaggio.direzione == "s":
                    if 5 < fineanimaz <= 10:
                        GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgSMov1, (personaggio.x, personaggio.y - (GlobalHWVar.gpy * fineanimaz // 10)))
                    if 0 < fineanimaz <= 5:
                        GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgSMov2, (personaggio.x, personaggio.y - (GlobalHWVar.gpy * fineanimaz // 10)))
    return animazionePersonaggi


def anima(sposta, x, y, vx, vy, rx, ry, vrx, vry, pers, robot, npers, nrob, primopasso, cambiosta, scudo, armatura, arma, armaMov1, armaMov2, armaAttacco, scudoDifesa, arco, faretra, arcoAttacco, guanti, guantiMov1, guantiMov2, guantiAttacco, guantiDifesa, collana, armaS, armaturaS, arcoS, faretraS, collanaS, armrob, armrobS, dati, attacco, difesa, bottoneDown, tesoro, aumentoliv, caricaTutto, listaNemici, vettoreEsche, vettoreDenaro, attaccoADistanza, caseviste, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoInquadrato, attaccoDiRallo, attaccoDiColco, statoRalloInizioTurno, statoColcoInizioTurno, statoEscheInizioTurno, raffreddamento, ricarica1, ricarica2, raffredda, autoRic1, autoRic2, animaOggetto, listaPersonaggi, apriocchio, chiamarob, movimentoPerMouse, vettoreImgCaselle, nonMostrarePersonaggio, saltaTurno):
    schermo_prima_delle_animazioni = GlobalHWVar.schermo.copy()

    azioniPossibili = ["attaccoColco", "movimentoColcoNemiciPersonaggi", "attaccoNemici", "aumentaLv"]
    azioniDaEseguire = []
    if sposta and (attacco == 1 or animaOggetto[0]):
        azioniDaEseguire.append("attaccoRallo")
    elif sposta:
        azioniDaEseguire.append("movimentoRallo")
    spostamentoNemico = False
    for nemico in listaNemici:
        if nemico.animaSpostamento or nemico.animaMorte:
            spostamentoNemico = True
            break
    spostamentoPersonaggio = False
    for personaggio in listaPersonaggi:
        if personaggio.animaSpostamento:
            spostamentoPersonaggio = True
            break
    if sposta and attacco == 0 and not animaOggetto[0] and not cambiosta and ((tecnicaUsata and tecnicaUsata == "spostamento") or spostamentoNemico or spostamentoPersonaggio) and not (tecnicaUsata and tecnicaUsata != "spostamento"):
        azioniPossibili.remove("attaccoColco")
        azioniPossibili.remove("movimentoColcoNemiciPersonaggi")
        azioniDaEseguire.append("movimentoColcoNemiciPersonaggi")
    elif not sposta and not cambiosta:
        if tecnicaUsata and tecnicaUsata != "spostamento":
            azioniDaEseguire.append("attaccoColco")
            azioniPossibili.remove("attaccoColco")
        else:
            azioniPossibili.remove("attaccoColco")
            azioniPossibili.remove("movimentoColcoNemiciPersonaggi")
            spostamentoNemico = False
            for nemico in listaNemici:
                if nemico.animaSpostamento or nemico.animaMorte:
                    spostamentoNemico = True
                    break
            if spostamentoNemico or (tecnicaUsata and tecnicaUsata == "spostamento"):
                azioniDaEseguire.append("movimentoColcoNemiciPersonaggi")
            else:
                attaccoNemico = False
                for nemico in listaNemici:
                    if nemico.animaAttacco:
                        attaccoNemico = True
                        break
                if attaccoNemico:
                    azioniDaEseguire.append("attaccoNemici")
    if len(azioniDaEseguire) == 0 and aumentoliv != 0 and "aumentaLv" in azioniPossibili:
        azioniDaEseguire.append("aumentaLv")
        azioniPossibili.remove("aumentaLv")

    # disegno l'occhio in alto a destra (non viene disegnato prima delle animazioni)
    if apriocchio:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhioape, (GlobalHWVar.gpx * 29.8, 0))
    else:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhiochiu, (GlobalHWVar.gpx * 29.8, 0))
    # disegno img saltaTurno
    if saltaTurno:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgSaltaTurnoCliccato, (GlobalHWVar.gpx * 30.9, 0))
    else:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgSaltaTurno, (GlobalHWVar.gpx * 30.9, 0))

    morteEscheAnimata = []
    i = 0
    while i < len(vettoreEsche):
        morteEscheAnimata.append(vettoreEsche[i])
        morteEscheAnimata.append(False)
        i += 4

    denaroRaccolto = False
    animazioneRalloFatta = False
    animazioneColcoFatta = False
    for nemico in listaNemici:
        nemico.animazioneFatta = False
    for personaggio in listaPersonaggi:
        personaggio.animazioneFatta = False
    while len(azioniDaEseguire) > 0:
        # viene fatto un ciclo in più alla fine (senza clock) per ripulire le immagini delle animazioni rimaste (altrimenti le ultime non verrebbero cancellate)
        nemicoAttaccante = False
        if "attaccoNemici" in azioniDaEseguire:
            for nemico in listaNemici:
                if nemico.animaAttacco and not nemico.animazioneFatta:
                    nemicoAttaccante = nemico
                    break
        fineanimaz = 10
        while fineanimaz >= 0:
            animazioneRallo = False
            animazioneColco = False
            animazioneNemici = False
            animazionePersonaggi = False
            # ridisegnare il quadratino dove sono i personaggi
            if cambiosta:
                if fineanimaz == 10:
                    i = 0
                    while i < len(vettoreImgCaselle):
                        if vx == vettoreImgCaselle[i] and vy == vettoreImgCaselle[i + 1]:
                            GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                            FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                            break
                        i += 3
            else:
                i = 0
                while i < len(vettoreImgCaselle):
                    if x == vettoreImgCaselle[i] and y == vettoreImgCaselle[i + 1]:
                        GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                        FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                    if vx == vettoreImgCaselle[i] and vy == vettoreImgCaselle[i + 1]:
                        GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                        FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                    if rx == vettoreImgCaselle[i] and ry == vettoreImgCaselle[i + 1]:
                        GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                        FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                    if vrx == vettoreImgCaselle[i] and vry == vettoreImgCaselle[i + 1]:
                        GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                        FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                    for nemico in listaNemici:
                        if nemico.inCasellaVista:
                            if nemico.x == vettoreImgCaselle[i] and nemico.y == vettoreImgCaselle[i + 1]:
                                GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                            if nemico.vx == vettoreImgCaselle[i] and nemico.vy == vettoreImgCaselle[i + 1]:
                                GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                    for personaggio in listaPersonaggi:
                        if personaggio.inCasellaVista and not personaggio.mantieniSempreASchermo:
                            if personaggio.x == vettoreImgCaselle[i] and personaggio.y == vettoreImgCaselle[i + 1]:
                                GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                            if personaggio.vx == vettoreImgCaselle[i] and personaggio.vy == vettoreImgCaselle[i + 1]:
                                GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                    i += 3

            # disegno: esche e denaro
            animaEsche(vettoreEsche, caseviste, azioniDaEseguire, animaOggetto, vettoreImgCaselle, morteEscheAnimata, nemicoInquadrato)
            animaDenaro(vettoreDenaro, caseviste, vettoreImgCaselle)

            if fineanimaz == 10:
                schermo_prima_delle_animazioni = GlobalHWVar.schermo.copy().convert()
            eliminaOggettoLanciato(x, y, attaccoADistanza, animaOggetto, rx, ry, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoAttaccante, schermo_prima_delle_animazioni, cambiosta, azioniDaEseguire, vettoreEsche, fineanimaz)
            disegnaCasellaAccantoAlPersCheAttacca(x, y, attacco, npers, rx, ry, nrob, tecnicaUsata, nemicoAttaccante, schermo_prima_delle_animazioni, cambiosta, azioniDaEseguire, fineanimaz)

            if cambiosta:
                quadrettoSottoRallo = schermo_prima_delle_animazioni.subsurface(pygame.Rect(x - GlobalHWVar.gpx, y - GlobalHWVar.gpy, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3)).convert()
                GlobalHWVar.disegnaImmagineSuSchermo(quadrettoSottoRallo, (x - GlobalHWVar.gpx, y - GlobalHWVar.gpy))

            # disegna personaggi se ci sono animazioni ma non loro
            animaColcoFermo(rx, ry, vrx, vry, robot, armrob, armrobS, statoColcoInizioTurno[1], tecnicaUsata, azioniDaEseguire, animazioneColcoFatta, raffreddamento, ricarica1, ricarica2, raffredda, autoRic1, autoRic2, nemicoInquadrato, fineanimaz)
            animaNemiciFermi(listaNemici, azioniDaEseguire, cambiosta, nemicoAttaccante, nemicoInquadrato, fineanimaz)
            animaPersonaggiFermi(listaPersonaggi, azioniDaEseguire, cambiosta, fineanimaz)
            if not cambiosta and not nonMostrarePersonaggio:
                animaRalloFermo(x, y, vx, vy, npers, pers, scudo, armatura, arma, arco, faretra, guanti, collana, statoRalloInizioTurno[1], azioniDaEseguire, animazioneRalloFatta, nemicoAttaccante, difesa, fineanimaz)

            # tolgo il rumore passi quando non c'è l'animazione
            if not "movimentoRallo" in azioniDaEseguire and GlobalHWVar.canaleSoundPassiRallo.get_busy():
                GlobalHWVar.canaleSoundPassiRallo.stop()
            # animazione difesa Rallo
            animazioneRallo = animaDifesaRallo(x, y, armaS, armaturaS, arcoS, faretraS, collanaS, scudoDifesa, guantiDifesa, statoRalloInizioTurno[1], difesa, animazioneRallo, nemicoAttaccante, fineanimaz)

            if "movimentoColcoNemiciPersonaggi" in azioniDaEseguire:
                # animazione camminata robo
                animazioneColco = animaCamminataColco(nrob, rx, ry, vrx, vry, robot, armrob, statoColcoInizioTurno[1], cambiosta, animazioneColco, nemicoInquadrato, fineanimaz)
                # animazione camminata mostri
                animazioneNemici = animaSpostamentoNemici(listaNemici, animazioneNemici, cambiosta, nemicoInquadrato, fineanimaz)
                # animazione camminata personaggi
                animazionePersonaggi = animaSpostamentoPersonaggi(listaPersonaggi, animazionePersonaggi, cambiosta, fineanimaz)

            if "movimentoRallo" in azioniDaEseguire:
                # animazione camminata personaggio
                animazioneRallo, primopasso, fineanimaz = animaCamminataRallo(sposta, x, y, vx, vy, primopasso, cambiosta, npers, pers, arma, scudo, armatura, armaMov1, armaMov2, arco, faretra, guanti, guantiMov1, guantiMov2, collana, statoRalloInizioTurno[1], difesa, animazioneRallo, fineanimaz, nonMostrarePersonaggio)

            if "attaccoNemici" in azioniDaEseguire:
                # animazione danneggiamento Colco
                robot, armrob, statoColcoInizioTurno[1] = animaDanneggiamentoColco(rx, ry, robot, armrob, statoColcoInizioTurno[1], nemicoAttaccante, attaccoDiRallo, cambiosta, azioniDaEseguire, fineanimaz)
                # animazione morte esche
                morteEscheAnimata = animaMorteEsche(x, y, vettoreEsche, vettoreImgCaselle, nemicoAttaccante, attaccoDiColco, attaccoDiRallo, morteEscheAnimata, azioniDaEseguire, fineanimaz)

                # animazione attacco nemici
                animaFrecceLanciate(x, y, attaccoADistanza, animaOggetto, rx, ry, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoAttaccante, cambiosta, azioniDaEseguire, vettoreEsche, fineanimaz)
                animazioneNemici = animaAttaccoNemici(nemicoAttaccante, animazioneNemici, nemicoInquadrato, fineanimaz)

            if "attaccoRallo" in azioniDaEseguire:
                # animazione danneggiamento Colco
                robot, armrob, statoColcoInizioTurno[1] = animaDanneggiamentoColco(rx, ry, robot, armrob, statoColcoInizioTurno[1], nemicoAttaccante, attaccoDiRallo, cambiosta, azioniDaEseguire, fineanimaz)
                # animazione morte esche
                morteEscheAnimata = animaMorteEsche(x, y, vettoreEsche, vettoreImgCaselle, nemicoAttaccante, attaccoDiColco, attaccoDiRallo, morteEscheAnimata, azioniDaEseguire, fineanimaz)

                # animazione attacco Rallo
                animazioneRallo = animaAttaccoRallo(sposta, x, y, npers, pers, arma, scudo, armatura, collana, arco, faretra, guanti, armaAttacco, arcoAttacco, guantiAttacco, statoRalloInizioTurno[1], attacco, difesa, vrx, vry, armrobS, animazioneRallo, attaccoADistanza, animaOggetto, vettoreImgCaselle, fineanimaz)
                # animazione danneggiamento Rallo
                animaDanneggiamentoRallo(x, y, attaccoDiColco, attaccoDiRallo, tecnicaUsata, azioniDaEseguire, fineanimaz)
                # animazione oggetto lanciato
                animaFrecceLanciate(x, y, attaccoADistanza, animaOggetto, rx, ry, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, listaNemici, cambiosta, azioniDaEseguire, vettoreEsche, fineanimaz)

                # animazione danneggiamento dei nemici
                animazioneNemici = animaDanneggiamentoNemici(attaccoADistanza, animaOggetto, listaNemici, animazioneNemici, cambiosta, azioniDaEseguire, "Rallo", nemicoInquadrato, fineanimaz)

            if "attaccoColco" in azioniDaEseguire:
                # animazione morte esche
                morteEscheAnimata = animaMorteEsche(x, y, vettoreEsche, vettoreImgCaselle, nemicoAttaccante, attaccoDiColco, attaccoDiRallo, morteEscheAnimata, azioniDaEseguire, fineanimaz)

                # animazione attacco Colco
                animaFrecceLanciate(x, y, attaccoADistanza, animaOggetto, rx, ry, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, listaNemici, cambiosta, azioniDaEseguire, vettoreEsche, fineanimaz)
                animazioneColco = animaTecnicaColco(rx, ry, nrob, robot, armrob, armrobS, tecnicaUsata, cambiosta, animazioneColco, statoColcoInizioTurno[1], nemicoInquadrato, fineanimaz)

                # animazione danneggiamento dei nemici
                animazioneNemici = animaDanneggiamentoNemici(attaccoADistanza, animaOggetto, listaNemici, animazioneNemici, cambiosta, azioniDaEseguire, "Colco", nemicoInquadrato, fineanimaz)
                # animazione danneggiamento Rallo
                animaDanneggiamentoRallo(x, y, attaccoDiColco, attaccoDiRallo, tecnicaUsata, azioniDaEseguire, fineanimaz)

            statoRalloInizioTurno, statoColcoInizioTurno = animaVitaRalloNemicoInquadrato(dati, nemicoInquadrato, vettoreEsche, difesa, azioniDaEseguire, nemicoAttaccante, attaccoDiRallo, attaccoDiColco, statoRalloInizioTurno, statoColcoInizioTurno, statoEscheInizioTurno, listaNemici, fineanimaz, aumentoliv, apriocchio, chiamarob, saltaTurno)

            if "aumentaLv" in azioniDaEseguire:
                # animazione aumento di livello
                animazioneRallo, caricaTutto, bottoneDown, aumentoliv, movimentoPerMouse = animaLvUp(x, y, npers, pers, arma, armatura, scudo, collana, arco, faretra, guanti, dati[4], aumentoliv, caricaTutto, bottoneDown, animazioneRallo, movimentoPerMouse, fineanimaz)

            # animazione apertura cofanetto
            animazioneRallo = animaAperturaCofanetto(tesoro, x, y, npers, vettoreImgCaselle, animazioneRallo)
            # anima raccolta denaro
            denaroRaccolto = animaRaccoltaDenaro(x, y, vettoreDenaro, fineanimaz)

            if animazioneRallo:
                animazioneRalloFatta = True
            if animazioneColco:
                animazioneColcoFatta = True

            if (animazioneNemici or animazioneRallo or animazioneColco or animazionePersonaggi) and fineanimaz >= 0:
                GlobalHWVar.aggiornaSchermo()
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                if fineanimaz > 0:
                    GlobalHWVar.clockAnimazioni.tick(GlobalHWVar.fpsAnimazioni)
                    # print (GlobalHWVar.clockAnimazioni.get_fps())
            fineanimaz -= 1

        azioniDaEseguire = []
        if not cambiosta:
            if tecnicaUsata and tecnicaUsata != "spostamento" and "attaccoColco" in azioniPossibili:
                azioniDaEseguire.append("attaccoColco")
                azioniPossibili.remove("attaccoColco")
            else:
                if "attaccoColco" in azioniPossibili:
                    azioniPossibili.remove("attaccoColco")
                spostamentoNemico = False
                for nemico in listaNemici:
                    if nemico.animaSpostamento or nemico.animaMorte:
                        spostamentoNemico = True
                        break
                spostamentoPersonaggio = False
                for personaggio in listaPersonaggi:
                    if personaggio.animaSpostamento:
                        spostamentoPersonaggio = True
                        break
                if (spostamentoNemico or tecnicaUsata == "spostamento" or spostamentoPersonaggio) and "movimentoColcoNemiciPersonaggi" in azioniPossibili:
                    azioniDaEseguire.append("movimentoColcoNemiciPersonaggi")
                    azioniPossibili.remove("movimentoColcoNemiciPersonaggi")
                else:
                    if "movimentoColcoNemiciPersonaggi" in azioniPossibili:
                        azioniPossibili.remove("movimentoColcoNemiciPersonaggi")
                    attaccoNemico = False
                    for nemico in listaNemici:
                        if not nemico.animazioneFatta and nemico.animaAttacco:
                            attaccoNemico = True
                            break
                    if attaccoNemico and "attaccoNemici" in azioniPossibili:
                        azioniDaEseguire.append("attaccoNemici")
        if len(azioniDaEseguire) == 0 and aumentoliv != 0 and "aumentaLv" in azioniPossibili:
            azioniDaEseguire.append("aumentaLv")
            if aumentoliv == 0:
                azioniPossibili.remove("aumentaLv")

    if tesoro != -1:
        if GlobalHWVar.mouseBloccato:
            GlobalHWVar.configuraCursore(False)
        GlobalHWVar.aggiornaSchermo()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        risposta = False
        bottoneDown = False
        while not risposta:
            # gestione degli input
            bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, False)
            if bottoneDown == pygame.K_SPACE or bottoneDown == "mouseSinistro" or bottoneDown == "padCroce":
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                risposta = True
                bottoneDown = False
            if bottoneDown:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                bottoneDown = False

            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
        movimentoPerMouse = False
        caricaTutto = True
        tesoro = -1
    if denaroRaccolto:
        if GlobalHWVar.mouseBloccato:
            GlobalHWVar.configuraCursore(False)
        GlobalHWVar.aggiornaSchermo()
        risposta = False
        bottoneDown = False
        while not risposta:
            # gestione degli input
            bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, False)
            if bottoneDown == pygame.K_SPACE or bottoneDown == "mouseSinistro" or bottoneDown == "padCroce":
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                risposta = True
                bottoneDown = False
            if bottoneDown:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                bottoneDown = False

            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
        movimentoPerMouse = False
        caricaTutto = True
        bottoneDown = False

    return primopasso, caricaTutto, tesoro, bottoneDown, movimentoPerMouse, robot, armrob
