# -*- coding: utf-8 -*-

from GenericFunc import *
import math


def animaCamminataRalloCambiosta(npers, x, y, scudo, armatura, armaMov1, arco, faretra, guantiMov1, collana, avvele, fineanimaz):
    if npers == 1:
        x = x - (GlobalVar.gpx * fineanimaz // 10)
    if npers == 2:
        x = x + (GlobalVar.gpx * fineanimaz // 10)
    if npers == 3:
        y = y + (GlobalVar.gpy * fineanimaz // 10)
    if npers == 4:
        y = y - (GlobalVar.gpy * fineanimaz // 10)
    pers = False
    if 5 < fineanimaz <= 10:
        frame = 1
        disegnaRallo(npers, x, y, avvele, pers, armaMov1, armatura, scudo, collana, arco, faretra, guantiMov1, True, frame)


def animaCamminataRalloSpostato(npers, x, y, scudo, armatura, armaMov1, armaMov2, arco, faretra, guantiMov1, guantiMov2, collana, avvele, fineanimaz):
    if npers == 1:
        x = x - (GlobalVar.gpx * fineanimaz // 10)
    if npers == 2:
        x = x + (GlobalVar.gpx * fineanimaz // 10)
    if npers == 3:
        y = y + (GlobalVar.gpy * fineanimaz // 10)
    if npers == 4:
        y = y - (GlobalVar.gpy * fineanimaz // 10)
    pers = False
    if 5 < fineanimaz <= 10:
        frame = 1
        disegnaRallo(npers, x, y, avvele, pers, armaMov1, armatura, scudo, collana, arco, faretra, guantiMov1, True, frame)
    elif 0 < fineanimaz <= 5:
        frame = 2
        disegnaRallo(npers, x, y, avvele, pers, armaMov2, armatura, scudo, collana, arco, faretra, guantiMov2, True, frame)


def animaCamminataRallo(sposta, x, y, vx, vy, primopasso, cambiosta, npers, pers, arma, scudo, armatura, armaMov1, armaMov2, arco, faretra, guanti, guantiMov1, guantiMov2, collana, avvele, difesa, animazioneRallo, fineanimaz):
    if sposta:
        # mentre ci si sposta
        if x != vx or y != vy:
            animazioneRallo = True
            if not GlobalVar.canaleSoundPassiRallo.get_busy():
                GlobalVar.canaleSoundPassiRallo.play(GlobalVar.rumorecamminata)
            if primopasso and not cambiosta:
                primopasso = False
            # camminata quando si entra in una stanza
            if cambiosta:
                animaCamminataRalloCambiosta(npers, x, y, scudo, armatura, armaMov1, arco, faretra, guantiMov1, collana, avvele, fineanimaz)
                if fineanimaz == 0:
                    GlobalVar.canaleSoundPassiRallo.stop()
            # camminata quando non si entra in una stanza
            else:
                animaCamminataRalloSpostato(npers, x, y, scudo, armatura, armaMov1, armaMov2, arco, faretra, guantiMov1, guantiMov2, collana, avvele, fineanimaz)
        # quando si apre una porta o un cofanetto oppure quando ci si sposta verso un muro
        elif difesa == 0 and fineanimaz > 0:
            animazioneRallo = True
            disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
    elif GlobalVar.canaleSoundPassiRallo.get_busy():
        GlobalVar.canaleSoundPassiRallo.stop()
    return animazioneRallo, primopasso


def animaAttaccoRallo(sposta, x, y, npers, pers, arma, scudo, armatura, collana, arco, faretra, guanti, armaAttacco, arcoAttacco, guantiAttacco, avvele, attacco, difesa, vrx, vry, armrobS, casellaChiara, casellaScura, animazioneRallo, attaccoADistanza, animaOggetto, vettoreImgCaselle, fineanimaz):
    if sposta and fineanimaz != 0:
        if attacco == 1 and difesa == 0:
            animazioneRallo = True
            if attaccoADistanza:
                if fineanimaz == 10:
                    GlobalVar.canaleSoundAttacco.play(GlobalVar.rumoreLancioFreccia)
                elif fineanimaz == 5:
                    GlobalVar.canaleSoundAttacco.play(GlobalVar.rumoreAttaccoArco)
                disegnaRallo(npers, x, y, avvele, pers, armaAttacco, armatura, scudo, collana, arcoAttacco, faretra, guantiAttacco, False, False, False, True)
            else:
                if fineanimaz == 10:
                    GlobalVar.canaleSoundAttacco.play(GlobalVar.rumoreAttaccoSpada)
                disegnaRallo(npers, x, y, avvele, pers, armaAttacco, armatura, scudo, collana, arco, faretra, guantiAttacco, False, False, True)
        elif animaOggetto[0]:
            animazioneRallo = True
            if animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata":
                disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
            if animaOggetto[0] == "pozione" or animaOggetto[0] == "superPozione":
                if fineanimaz == 10:
                    GlobalVar.canaleSoundAttacco.play(GlobalVar.suonoUsoPozione)
                disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
                if fineanimaz > 5:
                    GlobalVar.schermo.blit(GlobalVar.imgAnimaPozione1, (x, y))
                else:
                    GlobalVar.schermo.blit(GlobalVar.imgAnimaPozione2, (x, y))
            elif animaOggetto[0] == "medicina":
                if fineanimaz == 10:
                    GlobalVar.canaleSoundAttacco.play(GlobalVar.suonoUsoMedicina)
                disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
                if fineanimaz > 5:
                    GlobalVar.schermo.blit(GlobalVar.imgAnimaMedicina1, (x, y))
                else:
                    GlobalVar.schermo.blit(GlobalVar.imgAnimaMedicina2, (x, y))
            elif animaOggetto[0] == "caricaBatterie" or animaOggetto[0] == "caricaBatterieMigliorato":
                if fineanimaz == 10:
                    GlobalVar.canaleSoundAttacco.play(GlobalVar.suonoUsoCaricabatterie)
                i = 0
                while i < len(vettoreImgCaselle):
                    if vrx == vettoreImgCaselle[i] and vry == vettoreImgCaselle[i + 1]:
                        GlobalVar.schermo.blit(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                        disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1], casellaChiara, casellaScura)
                        break
                    i += 3
                GlobalVar.schermo.blit(armrobS, (vrx, vry))
                GlobalVar.schermo.blit(GlobalVar.robos, (vrx, vry))
                GlobalVar.schermo.blit(GlobalVar.imgAnimaCaricabatterie, (vrx, vry))
                disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
    return animazioneRallo


def animaDifesaRallo(x, y, armaS, armaturaS, arcoS, faretraS, collanaS, scudoDifesa, guantiDifesa, avvele, difesa, animazioneRallo, nemicoAttaccante, fineanimaz):
    if nemicoAttaccante and nemicoAttaccante.ralloParato and fineanimaz == 4:
        GlobalVar.canaleSoundAttacco.stop()
        GlobalVar.canaleSoundAttacco.play(GlobalVar.rumoreParata)
    if difesa != 0 or (nemicoAttaccante and nemicoAttaccante.ralloParato):
        animazioneRallo = True
        GlobalVar.schermo.blit(arcoS, (x, y))
        GlobalVar.schermo.blit(faretraS, (x, y))
        GlobalVar.schermo.blit(GlobalVar.perss, (x, y))
        if avvele:
            GlobalVar.schermo.blit(GlobalVar.persAvvele, (x, y))
        GlobalVar.schermo.blit(armaturaS, (x, y))
        GlobalVar.schermo.blit(collanaS, (x, y))
        GlobalVar.schermo.blit(GlobalVar.persmbDifesa, (x, y))
        GlobalVar.schermo.blit(armaS, (x, y))
        GlobalVar.schermo.blit(guantiDifesa, (x, y))
        GlobalVar.schermo.blit(scudoDifesa, (x, y))
    return animazioneRallo


def animaLvUp(x, y, npers, pers, arma, armatura, scudo, collana, arco, faretra, guanti, liv, aumentoliv, caricaTutto, bottoneDown, animazioneRallo, movimentoPerMouse, fineanimaz):
    if aumentoliv != 0:
        liv -= aumentoliv
        animazioneRallo = True
        if fineanimaz == 10:
            GlobalVar.canaleSoundLvUp.play(GlobalVar.rumorelevelup)
        avvele = False
        disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
        if 5 <= fineanimaz <= 10:
            GlobalVar.schermo.blit(GlobalVar.saliliv2, (x, y))
        if 1 < fineanimaz <= 5:
            GlobalVar.schermo.blit(GlobalVar.saliliv1, (x, y))
        if fineanimaz == 1:
            GlobalVar.schermo.blit(GlobalVar.saliliv, (x, y))

        GlobalVar.schermo.blit(GlobalVar.sfocontcof, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 0))
        i = 1
        while i <= 100:
            if liv == i:
                messaggio("Liv +: Attacco aumentato", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
                break
            i += 3
        i = 2
        while i <= 100:
            if liv == i:
                messaggio("Liv +: Difesa aumentata", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
                break
            i += 3
        i = 3
        while i <= 100:
            if liv == i:
                messaggio("Liv +: Punti vita aumentati", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
                break
            i += 3
        if fineanimaz == 1:
            if GlobalVar.mouseBloccato:
                GlobalVar.configuraCursore(False)
            pygame.display.update()
            pygame.time.wait(500)
            risposta = False
            bottoneDown = False
            while not risposta:
                # gestione degli input
                bottoneDown, aggiornaInterfacciaPerCambioInput = getInput(bottoneDown, False)
                if bottoneDown == pygame.K_SPACE or bottoneDown == "mouseSinistro" or bottoneDown == "padCroce":
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                    risposta = True
                    aumentoliv -= 1
                    bottoneDown = False
                if bottoneDown:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                    bottoneDown = False

        caricaTutto = True
        movimentoPerMouse = False
        bottoneDown = False
    return animazioneRallo, caricaTutto, bottoneDown, aumentoliv, movimentoPerMouse


def animaDanneggiamentoRallo(x, y, attaccoDiColco, attaccoDiRallo, tecnicaUsata, azioniDaEseguire, fineanimaz):
    if "attaccoRallo" in azioniDaEseguire and "Rallo" in attaccoDiRallo and fineanimaz <= 5:
        i = 0
        while i < len(attaccoDiRallo):
            if attaccoDiRallo[i] == "Rallo":
                GlobalVar.schermo.blit(GlobalVar.imgDanneggiamentoCausaRallo, (x, y))
            i += 3
    if "attaccoColco" in azioniDaEseguire and "Rallo" in attaccoDiColco and fineanimaz <= 5:
        if tecnicaUsata.startswith("scossa") or tecnicaUsata.startswith("freccia") or tecnicaUsata.startswith("tempesta"):
            GlobalVar.schermo.blit(GlobalVar.imgDanneggiamentoCausaColco, (x, y))


def animaRalloFermo(x, y, vx, vy, npers, pers, scudo, armatura, arma, arco, faretra, guanti, collana, avvele, azioniDaEseguire, animazioneRalloFatta, nemicoAttaccante, difesa, fineanimaz):
    if (not "attaccoRallo" in azioniDaEseguire and not "movimentoRallo" in azioniDaEseguire and not (nemicoAttaccante and nemicoAttaccante.ralloParato) and difesa == 0) or (fineanimaz == 0 and difesa == 0):
        if animazioneRalloFatta:
            disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
        else:
            disegnaRallo(npers, vx, vy, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)


def animaCamminataRobo(nrob, rx, ry, vrx, vry, robot, armrob, surriscalda, cambiosta, animazioneColco, fineanimaz):
    if (rx != vrx or ry != vry) and not cambiosta and robot != GlobalVar.robomo:
        animazioneColco = True
        if nrob != 0 and fineanimaz == 10:
            GlobalVar.canaleSoundPassiColco.play(GlobalVar.rumoreCamminataColco)
        # nrob => 1=d, 2=a, 3=s, 4=w
        if nrob == 1:
            if 5 < fineanimaz <= 10:
                GlobalVar.schermo.blit(GlobalVar.robodp, (rx - (GlobalVar.gpx * fineanimaz // 10), ry))
                if surriscalda > 0:
                    GlobalVar.schermo.blit(GlobalVar.roboSurrisc, (rx - (GlobalVar.gpx * fineanimaz // 10), ry))
                GlobalVar.schermo.blit(armrob, (rx - (GlobalVar.gpx * fineanimaz // 10), ry))
            if 0 < fineanimaz <= 5:
                GlobalVar.schermo.blit(GlobalVar.robodp, (rx - (GlobalVar.gpx * fineanimaz // 10), ry))
                if surriscalda > 0:
                    GlobalVar.schermo.blit(GlobalVar.roboSurrisc, (rx - (GlobalVar.gpx * fineanimaz // 10), ry))
                GlobalVar.schermo.blit(armrob, (rx - (GlobalVar.gpx * fineanimaz // 10), ry))
        if nrob == 2:
            if 5 < fineanimaz <= 10:
                GlobalVar.schermo.blit(GlobalVar.roboap, (rx + (GlobalVar.gpx * fineanimaz // 10), ry))
                if surriscalda > 0:
                    GlobalVar.schermo.blit(GlobalVar.roboSurrisc, (rx + (GlobalVar.gpx * fineanimaz // 10), ry))
                GlobalVar.schermo.blit(armrob, (rx + (GlobalVar.gpx * fineanimaz // 10), ry))
            if 0 < fineanimaz <= 5:
                GlobalVar.schermo.blit(GlobalVar.roboap, (rx + (GlobalVar.gpx * fineanimaz // 10), ry))
                if surriscalda > 0:
                    GlobalVar.schermo.blit(GlobalVar.roboSurrisc, (rx + (GlobalVar.gpx * fineanimaz // 10), ry))
                GlobalVar.schermo.blit(armrob, (rx + (GlobalVar.gpx * fineanimaz // 10), ry))
        if nrob == 4:
            if 5 < fineanimaz <= 10:
                GlobalVar.schermo.blit(GlobalVar.robow, (rx, ry + (GlobalVar.gpy * fineanimaz // 10)))
                if surriscalda > 0:
                    GlobalVar.schermo.blit(GlobalVar.roboSurrisc, (rx, ry + (GlobalVar.gpy * fineanimaz // 10)))
                GlobalVar.schermo.blit(armrob, (rx, ry + (GlobalVar.gpy * fineanimaz // 10)))
            if 0 < fineanimaz <= 5:
                GlobalVar.schermo.blit(GlobalVar.robow, (rx, ry + (GlobalVar.gpy * fineanimaz // 10)))
                if surriscalda > 0:
                    GlobalVar.schermo.blit(GlobalVar.roboSurrisc, (rx, ry + (GlobalVar.gpy * fineanimaz // 10)))
                GlobalVar.schermo.blit(armrob, (rx, ry + (GlobalVar.gpy * fineanimaz // 10)))
        if nrob == 3:
            if 5 < fineanimaz <= 10:
                GlobalVar.schermo.blit(GlobalVar.robos, (rx, ry - (GlobalVar.gpy * fineanimaz // 10)))
                if surriscalda > 0:
                    GlobalVar.schermo.blit(GlobalVar.roboSurrisc, (rx, ry - (GlobalVar.gpy * fineanimaz // 10)))
                GlobalVar.schermo.blit(armrob, (rx, ry - (GlobalVar.gpy * fineanimaz // 10)))
            if 0 < fineanimaz <= 5:
                GlobalVar.schermo.blit(GlobalVar.robos, (rx, ry - (GlobalVar.gpy * fineanimaz // 10)))
                if surriscalda > 0:
                    GlobalVar.schermo.blit(GlobalVar.roboSurrisc, (rx, ry - (GlobalVar.gpy * fineanimaz // 10)))
                GlobalVar.schermo.blit(armrob, (rx, ry - (GlobalVar.gpy * fineanimaz // 10)))
    return animazioneColco


def animaTecnicaColco(rx, ry, nrob, robot, armrob, armrobS, tecnicaUsata, cambiosta, animazioneColco, surriscalda, fineanimaz):
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
        while i < len(GlobalVar.vetAnimazioniTecniche):
            if GlobalVar.vetAnimazioniTecniche[i] == tecnicaUsata:
                if tecnicaUsata.startswith("scossa") or tecnicaUsata.startswith("freccia") or tecnicaUsata.startswith("cura") or tecnicaUsata == "antidoto" or tecnicaUsata == "attP" or tecnicaUsata == "difP":
                    imgAnimazione1w = GlobalVar.vetAnimazioniTecniche[i + 1][0]
                    imgAnimazione2w = GlobalVar.vetAnimazioniTecniche[i + 1][1]
                    imgAnimazione1a = GlobalVar.vetAnimazioniTecniche[i + 1][2]
                    imgAnimazione2a = GlobalVar.vetAnimazioniTecniche[i + 1][3]
                    imgAnimazione1s = GlobalVar.vetAnimazioniTecniche[i + 1][4]
                    imgAnimazione2s = GlobalVar.vetAnimazioniTecniche[i + 1][5]
                    imgAnimazione1d = GlobalVar.vetAnimazioniTecniche[i + 1][6]
                    imgAnimazione2d = GlobalVar.vetAnimazioniTecniche[i + 1][7]
                    imgAnimazioneSelf = GlobalVar.vetAnimazioniTecniche[i + 1][8]
                elif tecnicaUsata.startswith("tempesta"):
                    imgAnimazione1 = GlobalVar.vetAnimazioniTecniche[i + 1][0]
                    imgAnimazione2 = GlobalVar.vetAnimazioniTecniche[i + 1][1]
                else:
                    imgAnimazione = GlobalVar.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2

        if fineanimaz == 10:
            if tecnicaUsata.startswith("scossa") or tecnicaUsata.startswith("freccia"):
                GlobalVar.canaleSoundAttacco.play(GlobalVar.rumoreScossaFreccia)
            elif tecnicaUsata.startswith("tempesta"):
                GlobalVar.canaleSoundAttacco.play(GlobalVar.rumoreTempestaElettrica)
            elif tecnicaUsata.startswith("cura"):
                GlobalVar.canaleSoundAttacco.play(GlobalVar.rumoreCuraRobo)
            elif tecnicaUsata == "antidoto":
                GlobalVar.canaleSoundAttacco.play(GlobalVar.rumoreAntidoto)
            elif tecnicaUsata == "attP" or tecnicaUsata == "difP":
                GlobalVar.canaleSoundAttacco.play(GlobalVar.rumoreAttPDifP)
            elif tecnicaUsata.startswith("ricarica"):
                GlobalVar.canaleSoundAttacco.play(GlobalVar.rumoreAutoricarica)
            elif tecnicaUsata == "raffred":
                GlobalVar.canaleSoundAttacco.play(GlobalVar.rumoreRaffreddamento)
            elif tecnicaUsata == "velocizza" or tecnicaUsata == "efficienza":
                GlobalVar.canaleSoundAttacco.play(GlobalVar.rumoreVelocizzaEfficienza)

        if tecnicaUsata.startswith("scossa") or tecnicaUsata.startswith("freccia") or tecnicaUsata.startswith("cura") or tecnicaUsata == "antidoto" or tecnicaUsata == "attP" or tecnicaUsata == "difP":
            GlobalVar.schermo.blit(robot, (rx, ry))
            if surriscalda > 0:
                GlobalVar.schermo.blit(GlobalVar.roboSurrisc, (rx, ry))
            GlobalVar.schermo.blit(armrob, (rx, ry))
            # nrob => 1=d, 2=a, 3=s, 4=w
            if 7 < fineanimaz <= 10:
                if nrob == 0:
                    GlobalVar.schermo.blit(imgAnimazioneSelf, (rx, ry))
                if nrob == 1:
                    GlobalVar.schermo.blit(imgAnimazione1d, (rx, ry))
                if nrob == 2:
                    GlobalVar.schermo.blit(imgAnimazione1a, (rx - GlobalVar.gpx, ry))
                if nrob == 3:
                    GlobalVar.schermo.blit(imgAnimazione1s, (rx, ry))
                if nrob == 4:
                    GlobalVar.schermo.blit(imgAnimazione1w, (rx, ry - GlobalVar.gpy))
            if 0 < fineanimaz <= 7:
                if nrob == 0:
                    GlobalVar.schermo.blit(imgAnimazioneSelf, (rx, ry))
                if nrob == 1:
                    GlobalVar.schermo.blit(imgAnimazione2d, (rx, ry))
                if nrob == 2:
                    GlobalVar.schermo.blit(imgAnimazione2a, (rx - GlobalVar.gpx, ry))
                if nrob == 3:
                    GlobalVar.schermo.blit(imgAnimazione2s, (rx, ry))
                if nrob == 4:
                    GlobalVar.schermo.blit(imgAnimazione2w, (rx, ry - GlobalVar.gpy))
        if tecnicaUsata.startswith("ricarica") or tecnicaUsata == "raffred" or tecnicaUsata == "velocizza" or tecnicaUsata == "efficienza":
            if tecnicaUsata.startswith("ricarica"):
                GlobalVar.schermo.blit(GlobalVar.robomo, (rx, ry))
            else:
                GlobalVar.schermo.blit(armrobS, (rx, ry))
                GlobalVar.schermo.blit(GlobalVar.robos, (rx, ry))
            GlobalVar.schermo.blit(imgAnimazione, (rx, ry))
        if tecnicaUsata.startswith("tempesta"):
            GlobalVar.schermo.blit(robot, (rx, ry))
            if surriscalda > 0:
                GlobalVar.schermo.blit(GlobalVar.roboSurrisc, (rx, ry))
            GlobalVar.schermo.blit(armrob, (rx, ry))
            if 7 < fineanimaz <= 10:
                GlobalVar.schermo.blit(imgAnimazione1, (rx - (GlobalVar.gpx * 6), ry - (GlobalVar.gpx * 6)))
            if 0 < fineanimaz <= 7:
                GlobalVar.schermo.blit(imgAnimazione2, (rx - (GlobalVar.gpx * 6), ry - (GlobalVar.gpx * 6)))

    return animazioneColco


def animaDanneggiamentoColco(rx, ry, robot, armrob, surriscalda, nemicoAttaccante, attaccoDiRallo, cambiosta, azioniDaEseguire, fineanimaz):
    if not cambiosta and fineanimaz != 0:
        if "attaccoRallo" in azioniDaEseguire and "Colco" in attaccoDiRallo and fineanimaz <= 5:
            i = 0
            while i < len(attaccoDiRallo):
                if attaccoDiRallo[i] == "Colco":
                    GlobalVar.schermo.blit(GlobalVar.imgDanneggiamentoColco, (rx, ry))
                    GlobalVar.schermo.blit(GlobalVar.imgDanneggiamentoCausaRallo, (rx, ry))
                    if attaccoDiRallo[i + 2]:
                        robot = GlobalVar.robomo
                        armrob = GlobalVar.armrobmo
                        surriscalda = 0
                i += 3
        elif "attaccoNemici" in azioniDaEseguire and nemicoAttaccante.bersaglioColpito[0] == "Colco":
            GlobalVar.schermo.blit(GlobalVar.imgDanneggiamentoColco, (rx, ry))
            if nemicoAttaccante.bersaglioColpito[3]:
                robot = GlobalVar.robomo
                armrob = GlobalVar.armrobmo
                surriscalda = 0
    return robot, armrob, surriscalda


def animaColcoFermo(rx, ry, vrx, vry, robot, armrob, armrobS, surriscalda, tecnicaUsata, azioniDaEseguire, animazioneColcoFatta, raffreddamento, ricarica1, ricarica2, raffredda, autoRic1, autoRic2, fineanimaz):
    if (not ("attaccoColco" in azioniDaEseguire and tecnicaUsata != "spostamento") and not ("movimentoColcoNemiciPersonaggi" in azioniDaEseguire and tecnicaUsata == "spostamento")) or fineanimaz == 0:
        if animazioneColcoFatta or robot == GlobalVar.robomo:
            x = rx
            y = ry
        else:
            x = vrx
            y = vry
        if (raffreddamento and animazioneColcoFatta) or (raffredda >= 0 and not raffreddamento):
            GlobalVar.schermo.blit(armrobS, (x, y))
            GlobalVar.schermo.blit(GlobalVar.robos, (x, y))
            imgAnimazione = 0
            i = 0
            while i < len(GlobalVar.vetAnimazioniTecniche):
                if GlobalVar.vetAnimazioniTecniche[i] == "raffred":
                    imgAnimazione = GlobalVar.vetAnimazioniTecniche[i + 1][0]
                    break
                i += 2
            GlobalVar.schermo.blit(imgAnimazione, (x, y))
        elif (ricarica1 and animazioneColcoFatta) or (autoRic1 >= 0 and not ricarica1):
            GlobalVar.schermo.blit(GlobalVar.robomo, (x, y))
            imgAnimazione = 0
            i = 0
            while i < len(GlobalVar.vetAnimazioniTecniche):
                if GlobalVar.vetAnimazioniTecniche[i] == "ricarica":
                    imgAnimazione = GlobalVar.vetAnimazioniTecniche[i + 1][0]
                    break
                i += 2
            GlobalVar.schermo.blit(imgAnimazione, (x, y))
        elif (ricarica2 and animazioneColcoFatta) or (autoRic2 >= 0 and not ricarica2):
            GlobalVar.schermo.blit(GlobalVar.robomo, (x, y))
            imgAnimazione = 0
            i = 0
            while i < len(GlobalVar.vetAnimazioniTecniche):
                if GlobalVar.vetAnimazioniTecniche[i] == "ricarica+":
                    imgAnimazione = GlobalVar.vetAnimazioniTecniche[i + 1][0]
                    break
                i += 2
            GlobalVar.schermo.blit(imgAnimazione, (x, y))
        else:
            GlobalVar.schermo.blit(robot, (x, y))
            if surriscalda > 0:
                GlobalVar.schermo.blit(GlobalVar.roboSurrisc, (x, y))
            GlobalVar.schermo.blit(armrob, (x, y))


def animaSpostamentoNemici(listaNemici, animazioneNemici, cambiosta, fineanimaz):
    if not cambiosta:
        for nemico in listaNemici:
            if nemico.animaSpostamento and not nemico.morto and (nemico.x != nemico.vx or nemico.y != nemico.vy):
                if not GlobalVar.canaleSoundPassiNemiciPersonaggi.get_busy() and fineanimaz > 6:
                    GlobalVar.canaleSoundPassiNemiciPersonaggi.play(GlobalVar.rumoreMovimentoNemiciPersonaggi)
                nemico.animazioneFatta = True
                animazioneNemici = True
                # rumorecamminataNemico.play()
                if nemico.direzione == "d":
                    if 5 < fineanimaz <= 10:
                        GlobalVar.schermo.blit(nemico.imgDMov1, (nemico.x - (GlobalVar.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[1]:
                            GlobalVar.schermo.blit(nemico.imgAvvelenamento, (nemico.x - (GlobalVar.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[2]:
                            GlobalVar.schermo.blit(nemico.imgAppiccicato, (nemico.x - (GlobalVar.gpx * fineanimaz // 10), nemico.y))
                    if 0 < fineanimaz <= 5:
                        GlobalVar.schermo.blit(nemico.imgDMov2, (nemico.x - (GlobalVar.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[1]:
                            GlobalVar.schermo.blit(nemico.imgAvvelenamento, (nemico.x - (GlobalVar.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[2]:
                            GlobalVar.schermo.blit(nemico.imgAppiccicato, (nemico.x - (GlobalVar.gpx * fineanimaz // 10), nemico.y))
                if nemico.direzione == "a":
                    if 5 < fineanimaz <= 10:
                        GlobalVar.schermo.blit(nemico.imgAMov1, (nemico.x + (GlobalVar.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[1]:
                            GlobalVar.schermo.blit(nemico.imgAvvelenamento, (nemico.x + (GlobalVar.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[2]:
                            GlobalVar.schermo.blit(nemico.imgAppiccicato, (nemico.x + (GlobalVar.gpx * fineanimaz // 10), nemico.y))
                    if 0 < fineanimaz <= 5:
                        GlobalVar.schermo.blit(nemico.imgAMov2, (nemico.x + (GlobalVar.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[1]:
                            GlobalVar.schermo.blit(nemico.imgAvvelenamento, (nemico.x + (GlobalVar.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[2]:
                            GlobalVar.schermo.blit(nemico.imgAppiccicato, (nemico.x + (GlobalVar.gpx * fineanimaz // 10), nemico.y))
                if nemico.direzione == "w":
                    if 5 < fineanimaz <= 10:
                        GlobalVar.schermo.blit(nemico.imgWMov1, (nemico.x, nemico.y + (GlobalVar.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[1]:
                            GlobalVar.schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y + (GlobalVar.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[2]:
                            GlobalVar.schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y + (GlobalVar.gpy * fineanimaz // 10)))
                    if 0 < fineanimaz <= 5:
                        GlobalVar.schermo.blit(nemico.imgWMov2, (nemico.x, nemico.y + (GlobalVar.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[1]:
                            GlobalVar.schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y + (GlobalVar.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[2]:
                            GlobalVar.schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y + (GlobalVar.gpy * fineanimaz // 10)))
                if nemico.direzione == "s":
                    if 5 < fineanimaz <= 10:
                        GlobalVar.schermo.blit(nemico.imgSMov1, (nemico.x, nemico.y - (GlobalVar.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[1]:
                            GlobalVar.schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y - (GlobalVar.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[2]:
                            GlobalVar.schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y - (GlobalVar.gpy * fineanimaz // 10)))
                    if 0 < fineanimaz <= 5:
                        GlobalVar.schermo.blit(nemico.imgSMov2, (nemico.x, nemico.y - (GlobalVar.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[1]:
                            GlobalVar.schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y - (GlobalVar.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[2]:
                            GlobalVar.schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y - (GlobalVar.gpy * fineanimaz // 10)))
    return animazioneNemici


def animaAttaccoNemici(nemicoAttaccante, animazioneNemici, fineanimaz):
    if nemicoAttaccante and fineanimaz != 0:
        if nemicoAttaccante.animaAttacco and not nemicoAttaccante.animazioneFatta:
            if fineanimaz == 1:
                nemicoAttaccante.animazioneFatta = True
            animazioneNemici = True
            if fineanimaz == 10:
                if nemicoAttaccante.attaccaDaLontano:
                    GlobalVar.canaleSoundAttacco.play(GlobalVar.rumoreLancioOggettoNemico)
                else:
                    GlobalVar.canaleSoundAttacco.play(GlobalVar.rumoreAttaccoNemico)
            if fineanimaz == 5 and nemicoAttaccante.attaccaDaLontano:
                GlobalVar.canaleSoundAttacco.play(GlobalVar.rumoreAttaccoNemico)
            if nemicoAttaccante.direzione == "w":
                GlobalVar.schermo.blit(nemicoAttaccante.imgAttaccoW, (nemicoAttaccante.x, nemicoAttaccante.y - GlobalVar.gpy))
            if nemicoAttaccante.direzione == "a":
                GlobalVar.schermo.blit(nemicoAttaccante.imgAttaccoA, (nemicoAttaccante.x - GlobalVar.gpx, nemicoAttaccante.y))
            if nemicoAttaccante.direzione == "s":
                GlobalVar.schermo.blit(nemicoAttaccante.imgAttaccoS, (nemicoAttaccante.x, nemicoAttaccante.y))
            if nemicoAttaccante.direzione == "d":
                GlobalVar.schermo.blit(nemicoAttaccante.imgAttaccoD, (nemicoAttaccante.x, nemicoAttaccante.y))
            if nemicoAttaccante.statoInizioTurno[1]:
                GlobalVar.schermo.blit(nemicoAttaccante.imgAvvelenamento, (nemicoAttaccante.x, nemicoAttaccante.y))
            if nemicoAttaccante.statoInizioTurno[2]:
                GlobalVar.schermo.blit(nemicoAttaccante.imgAppiccicato, (nemicoAttaccante.x, nemicoAttaccante.y))
    return animazioneNemici


def animaDanneggiamentoNemici(attaccoADistanza, animaOggetto, listaNemici, animazioneNemici, cambiosta, azioniDaEseguire, attaccante, fineanimaz):
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
                    if not GlobalVar.canaleSoundMorteNemici.get_busy() and fineanimaz == 5:
                        GlobalVar.canaleSoundMorteNemici.play(GlobalVar.rumoreMorteNemico)
                    nemico.animazioneFatta = True
                    if fineanimaz > 5 or (0 < fineanimaz <= 5 and fineanimaz % 4 == 0):
                        GlobalVar.schermo.blit(nemico.imgAttuale, (nemico.vx, nemico.vy))
                        if nemico.statoInizioTurno[1]:
                            GlobalVar.schermo.blit(nemico.imgAvvelenamento, (nemico.vx, nemico.vy))
                        if nemico.statoInizioTurno[2]:
                            GlobalVar.schermo.blit(nemico.imgAppiccicato, (nemico.vx, nemico.vy))
                else:
                    GlobalVar.schermo.blit(nemico.imgAttuale, (nemico.vx, nemico.vy))
                    if nemico.statoInizioTurno[1]:
                        GlobalVar.schermo.blit(nemico.imgAvvelenamento, (nemico.vx, nemico.vy))
                    if nemico.statoInizioTurno[2]:
                        GlobalVar.schermo.blit(nemico.imgAppiccicato, (nemico.vx, nemico.vy))

                if attaccante == "Rallo":
                    if attaccoADistanza or animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata":
                        if fineanimaz <= 5:
                            GlobalVar.schermo.blit(nemico.imgDanneggiamentoRallo, (nemico.vx, nemico.vy))
                    else:
                        GlobalVar.schermo.blit(nemico.imgDanneggiamentoRallo, (nemico.vx, nemico.vy))
                if attaccante == "Colco" and fineanimaz <= 5:
                    GlobalVar.schermo.blit(nemico.imgDanneggiamentoColco, (nemico.vx, nemico.vy))
    return animazioneNemici


def animaNemiciFermi(listaNemici, azioniDaEseguire, cambiosta, nemicoAttaccante, fineanimaz):
    if not cambiosta:
        for nemico in listaNemici:
            if nemico.inCasellaVista and ((not (("movimentoColcoNemiciPersonaggi" in azioniDaEseguire and (nemico.animaSpostamento or nemico.animaMorte)) or ("attaccoNemici" in azioniDaEseguire and nemico.animaAttacco and nemicoAttaccante == nemico) or ("attaccoRallo" in azioniDaEseguire and len(nemico.animaDanneggiamento) > 0 and "Rallo" in nemico.animaDanneggiamento) or ("attaccoColco" in azioniDaEseguire and len(nemico.animaDanneggiamento) > 0 and "Colco" in nemico.animaDanneggiamento)) and not (nemico.animaMorte and nemico.animazioneFatta)) or (fineanimaz == 0 and not nemico.animaMorte)):
                if nemico.animazioneFatta:
                    GlobalVar.schermo.blit(nemico.imgAttuale, (nemico.x, nemico.y))
                    if nemico.statoInizioTurno[1]:
                        GlobalVar.schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y))
                    if nemico.statoInizioTurno[2]:
                        GlobalVar.schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y))
                else:
                    GlobalVar.schermo.blit(nemico.imgAttuale, (nemico.vx, nemico.vy))
                    if nemico.statoInizioTurno[1]:
                        GlobalVar.schermo.blit(nemico.imgAvvelenamento, (nemico.vx, nemico.vy))
                    if nemico.statoInizioTurno[2]:
                        GlobalVar.schermo.blit(nemico.imgAppiccicato, (nemico.vx, nemico.vy))


def animaEsche(vettoreEsche, caseviste, casellaChiara, casellaScura, azioniDaEseguire, animaOggetto, vettoreImgCaselle, morteEscheAnimata):
    if "attaccoRallo" in azioniDaEseguire and animaOggetto[0] == "esca":
        c = 0
        while c < len(vettoreImgCaselle):
            if animaOggetto[1] == vettoreImgCaselle[c] and animaOggetto[2] == vettoreImgCaselle[c + 1]:
                GlobalVar.schermo.blit(vettoreImgCaselle[c + 2], (vettoreImgCaselle[c], vettoreImgCaselle[c + 1]))
                disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[c], vettoreImgCaselle[c + 1], casellaChiara, casellaScura)
                break
            c += 3
    elif not "attaccoRallo" in azioniDaEseguire and animaOggetto[0] == "esca":
        c = 0
        while c < len(vettoreImgCaselle):
            if animaOggetto[1] == vettoreImgCaselle[c] and animaOggetto[2] == vettoreImgCaselle[c + 1]:
                GlobalVar.schermo.blit(vettoreImgCaselle[c + 2], (vettoreImgCaselle[c], vettoreImgCaselle[c + 1]))
                disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[c], vettoreImgCaselle[c + 1], casellaChiara, casellaScura)
                break
            c += 3
        GlobalVar.schermo.blit(GlobalVar.vetIcoOggettiMenu[7], (animaOggetto[1], animaOggetto[2]))
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
                                        GlobalVar.schermo.blit(vettoreImgCaselle[c + 2], (vettoreImgCaselle[c], vettoreImgCaselle[c + 1]))
                                        disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[c], vettoreImgCaselle[c + 1], casellaChiara, casellaScura)
                                        break
                                    c += 3
                                GlobalVar.schermo.blit(GlobalVar.esche, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                            break
                        j += 3
                    break
                contatore += 2
        i += 4


def animaMorteEsche(x, y, vettoreEsche, casellaChiara, casellaScura, vettoreImgCaselle, nemicoAttaccante, attaccoDiColco, attaccoDiRallo, morteEscheAnimata, azioniDaEseguire, fineanimaz):
    escheMorte = []
    if "attaccoRallo" in azioniDaEseguire and len(attaccoDiRallo) > 0:
        i = 0
        while i < len(vettoreEsche):
            k = 0
            while k < len(attaccoDiRallo):
                if type(attaccoDiRallo[k]) is str and attaccoDiRallo[k].startswith("Esca") and int(attaccoDiRallo[k].split(":")[1]) == vettoreEsche[i]:
                    if (abs(x - vettoreEsche[i + 2]) == GlobalVar.gpx and abs(y - vettoreEsche[i + 3]) == 0) or (abs(x - vettoreEsche[i + 2]) == 0 and abs(y - vettoreEsche[i + 3]) == GlobalVar.gpy):
                        GlobalVar.schermo.blit(GlobalVar.imgDanneggiamentoCausaRallo, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                    elif fineanimaz <= 5:
                        GlobalVar.schermo.blit(GlobalVar.imgDanneggiamentoCausaRallo, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
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
                        GlobalVar.schermo.blit(GlobalVar.imgDanneggiamentoCausaColco, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
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
                if not GlobalVar.canaleSoundMorteNemici.get_busy() and fineanimaz == 5:
                    GlobalVar.canaleSoundMorteNemici.play(GlobalVar.rumoreMorteNemico)
                c = 0
                while c < len(vettoreImgCaselle):
                    if vettoreEsche[i + 2] == vettoreImgCaselle[c] and vettoreEsche[i + 3] == vettoreImgCaselle[c + 1]:
                        GlobalVar.schermo.blit(vettoreImgCaselle[c + 2], (vettoreImgCaselle[c], vettoreImgCaselle[c + 1]))
                        disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[c], vettoreImgCaselle[c + 1], casellaChiara, casellaScura)
                        break
                    c += 3
                if fineanimaz > 5 or (0 < fineanimaz <= 5 and fineanimaz % 4 == 0):
                    GlobalVar.schermo.blit(GlobalVar.esche, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                if "attaccoRallo" in azioniDaEseguire:
                    if (abs(x - vettoreEsche[i + 2]) == GlobalVar.gpx and abs(y - vettoreEsche[i + 3]) == 0) or (abs(x - vettoreEsche[i + 2]) == 0 and abs(y - vettoreEsche[i + 3]) == GlobalVar.gpy):
                        GlobalVar.schermo.blit(GlobalVar.imgDanneggiamentoCausaRallo, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                    elif fineanimaz <= 5:
                        GlobalVar.schermo.blit(GlobalVar.imgDanneggiamentoCausaRallo, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                if "attaccoColco" in azioniDaEseguire:
                    GlobalVar.schermo.blit(GlobalVar.imgDanneggiamentoCausaColco, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                j = 0
                while j < len(morteEscheAnimata):
                    if vettoreEsche[i] == morteEscheAnimata[j]:
                        morteEscheAnimata[j + 1] = True
                        break
                    j += 2
            i += 4

    return morteEscheAnimata


def animaDenaro(vettoreDenaro, caseviste, casellaChiara, casellaScura, vettoreImgCaselle):
    i = 0
    while i < len(vettoreDenaro):
        j = 0
        while j < len(caseviste):
            if ((caseviste[j] == vettoreDenaro[i + 1] - GlobalVar.gpx and caseviste[j + 1] == vettoreDenaro[i + 2]) or (caseviste[j] == vettoreDenaro[i + 1] + GlobalVar.gpx and caseviste[j + 1] == vettoreDenaro[i + 2]) or (caseviste[j] == vettoreDenaro[i + 1] and caseviste[j + 1] == vettoreDenaro[i + 2] - GlobalVar.gpy) or (caseviste[j] == vettoreDenaro[i + 1] and caseviste[j + 1] == vettoreDenaro[i + 2] + GlobalVar.gpy)) and caseviste[j + 2]:
                c = 0
                while c < len(vettoreImgCaselle):
                    if vettoreDenaro[i + 1] == vettoreImgCaselle[c] and vettoreDenaro[i + 2] == vettoreImgCaselle[c + 1]:
                        GlobalVar.schermo.blit(vettoreImgCaselle[c + 2], (vettoreImgCaselle[c], vettoreImgCaselle[c + 1]))
                        disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[c], vettoreImgCaselle[c + 1], casellaChiara, casellaScura)
                        break
                    c += 3
                GlobalVar.schermo.blit(GlobalVar.sacchettoDenaro, (vettoreDenaro[i + 1], vettoreDenaro[i + 2]))
                break
            j += 3
        i += 3


def animaCofanetti(cofanetti, caseviste):
    # cofanetti[stanza, x, y, True / False, ...]
    i = 0
    while i < len(cofanetti):
        j = 0
        while j < len(caseviste):
            if ((caseviste[j] == cofanetti[i + 1] - GlobalVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] + GlobalVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - GlobalVar.gpy) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + GlobalVar.gpy)) and caseviste[j + 2]:
                if cofanetti[i + 3]:
                    GlobalVar.schermo.blit(GlobalVar.cofaniaper, (cofanetti[i + 1], cofanetti[i + 2]))
                else:
                    GlobalVar.schermo.blit(GlobalVar.cofanichiu, (cofanetti[i + 1], cofanetti[i + 2]))
                break
            j += 3
        i += 4


def animaPorte(porte, caseviste, portaOriz, portaVert):
    # porte[stanza, x, y, True / False, ...]
    i = 0
    while i < len(porte):
        if not porte[i + 3]:
            j = 0
            while j < len(caseviste):
                if ((caseviste[j] == porte[i + 1] - GlobalVar.gpx and caseviste[j + 1] == porte[i + 2]) or (caseviste[j] == porte[i + 1] + GlobalVar.gpx and caseviste[j + 1] == porte[i + 2]) or (caseviste[j] == porte[i + 1] and caseviste[j + 1] == porte[i + 2] - GlobalVar.gpy) or (caseviste[j] == porte[i + 1] and caseviste[j + 1] == porte[i + 2] + GlobalVar.gpy)) and caseviste[j + 2]:
                    if (caseviste[j] == porte[i + 1] - GlobalVar.gpx and caseviste[j + 1] == porte[i + 2]) or (caseviste[j] == porte[i + 1] + GlobalVar.gpx and caseviste[j + 1] == porte[i + 2]):
                        GlobalVar.schermo.blit(portaVert, (porte[i + 1], porte[i + 2]))
                    else:
                        GlobalVar.schermo.blit(portaOriz, (porte[i + 1], porte[i + 2]))
                    break
                j += 3
        i = i + 4


def animaAperturaCofanetto(tesoro, x, y, npers, animazioneRallo):
    if tesoro != -1:
        animazioneRallo = True
        if npers == 1:
            GlobalVar.schermo.blit(GlobalVar.cofaniaper, (x + GlobalVar.gpx, y))
        if npers == 2:
            GlobalVar.schermo.blit(GlobalVar.cofaniaper, (x - GlobalVar.gpx, y))
        if npers == 3:
            GlobalVar.schermo.blit(GlobalVar.cofaniaper, (x, y - GlobalVar.gpy))
        if npers == 4:
            GlobalVar.schermo.blit(GlobalVar.cofaniaper, (x, y + GlobalVar.gpy))
        GlobalVar.schermo.blit(GlobalVar.sfocontcof, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 0))
        if tesoro == -2:
            messaggio("Hai trovato: Niente", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        # 31-40 -> oggetti(10) / 41-70 -> armi(30) / 71-75 -> batterie(5) / 81-100 -> condizioni(20) / 101-120 -> gambit (=celle di memoria)(20) / 131 -> monete / 132 frecce
        elif tesoro >= 11 and tesoro <= 30:
            messaggio("Hai trovato: Una nuova tecnica", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 31:
            messaggio("Hai trovato: Pozione", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == -31:
            messaggio(u"Hai già troppe Pozioni!", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 32:
            messaggio("Hai trovato: Alimentazione 100gr", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == -32:
            messaggio(u"Hai già troppe Alimentazioni 100gr!", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 33:
            messaggio("Hai trovato: Medicina", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == -33:
            messaggio(u"Hai già troppe Medicine!", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 34:
            messaggio("Hai trovato: Superpozione", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == -34:
            messaggio(u"Hai già troppe Superpozioni!", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 35:
            messaggio("Hai trovato: Alimentazione 250gr", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == -35:
            messaggio(u"Hai già troppe Alimentazioni 250gr!", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 36:
            messaggio("Hai trovato: Bomba", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == -36:
            messaggio(u"Hai già troppe Bombe!", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 37:
            messaggio("Hai trovato: Bomba velenosa", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == -37:
            messaggio(u"Hai già troppe Bombe velenose!", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 38:
            messaggio("Hai trovato: Esca", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == -38:
            messaggio(u"Hai già troppe Esche!", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 39:
            messaggio("Hai trovato: Bomba appiccicosa", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == -39:
            messaggio(u"Hai già troppe Bombe appiccicose!", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 40:
            messaggio("Hai trovato: Bomba potenziata", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == -40:
            messaggio(u"Hai già troppe Bombe potenziate!", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 41:
            messaggio("Hai trovato: Niente", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 42:
            messaggio("Hai trovato: Spada di ferro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 43:
            messaggio("Hai trovato: Spadone d'acciaio", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 44:
            messaggio("Hai trovato: Lykother", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 45:
            messaggio("Hai trovato: Mendaxritas", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 46:
            messaggio("Hai trovato: Niente", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 47:
            messaggio("Hai trovato: Arco di legno", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 48:
            messaggio("Hai trovato: Arco di ferro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 49:
            messaggio("Hai trovato: Arco di precisione", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 50:
            messaggio("Hai trovato: Accipiter", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 51:
            messaggio("Hai trovato: Niente", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 52:
            messaggio("Hai trovato: Armatura di pelle", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 53:
            messaggio("Hai trovato: Armatura d'acciaio", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 54:
            messaggio("Hai trovato: Lykodes", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 55:
            messaggio("Hai trovato: Loriquam", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 56:
            messaggio("Hai trovato: Niente", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 57:
            messaggio("Hai trovato: Scudo di pelle", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 58:
            messaggio("Hai trovato: Scudo d'acciaio", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 59:
            messaggio("Hai trovato: Lykethmos", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 60:
            messaggio("Hai trovato: Clipequam", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 61:
            messaggio("Hai trovato: Niente", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 62:
            messaggio("Hai trovato: Guanti vitali", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 63:
            messaggio("Hai trovato: Guanti difensivi", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 64:
            messaggio("Hai trovato: Guanti offensivi", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 65:
            messaggio("Hai trovato: Guanti confortevoli", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 66:
            messaggio("Hai trovato: Niente", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 67:
            messaggio("Hai trovato: Collana medicinale", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 68:
            messaggio("Hai trovato: Collana rigenerante", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 69:
            messaggio("Hai trovato: Apprendimaschera", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 70:
            messaggio("Hai trovato: Portafortuna", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 71:
            messaggio("Hai trovato: Batteria piccola", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 72:
            messaggio("Hai trovato: Batteria discreta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 73:
            messaggio("Hai trovato: Batteria capiente", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 74:
            messaggio("Hai trovato: Batteria enorme", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 75:
            messaggio("Hai trovato: Batteria illimitata", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro >= 81 and tesoro <= 100:
            messaggio("Hai trovato: Una nuova condizione", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro >= 101 and tesoro <= 120:
            messaggio("Hai trovato: Cella di memoria", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 131:
            messaggio("Hai trovato: 50 monete", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == 132:
            messaggio("Hai trovato: 1 freccia", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
        elif tesoro == -132:
            messaggio(u"Hai già troppe frecce!", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)

    return animazioneRallo


def animaRaccoltaDenaro(x, y, vettoreDenaro, fineanimaz):
    denaroRaccolto = False
    i = 0
    while i < len(vettoreDenaro):
        if vettoreDenaro[i + 1] == x and vettoreDenaro[i + 2] == y:
            if fineanimaz == 1:
                GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoRaccoltaMonete)
            if GlobalVar.canaleSoundPassiRallo.get_busy():
                GlobalVar.canaleSoundPassiRallo.stop()
            denaroTrovato = vettoreDenaro[i]
            GlobalVar.schermo.blit(GlobalVar.sfocontcof, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 0))
            messaggio("Monete trovate: " + str(denaroTrovato), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 1, 60)
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
                quadrettoSottoEsplosione = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xFineRetta - (GlobalVar.gpx * 2), yFineRetta - (GlobalVar.gpy * 2), GlobalVar.gpx * 5, GlobalVar.gpy * 5))
            if fineanimaz != 10:
                GlobalVar.schermo.blit(quadrettoSottoLaFreccia, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz) - GlobalVar.gpx), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVar.gpy))
            quadrettoSottoLaFreccia = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)) - GlobalVar.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz)) - GlobalVar.gpy, GlobalVar.gpx * 3, GlobalVar.gpy * 3))
        elif fineanimaz == 5:
            GlobalVar.schermo.blit(quadrettoSottoLaFreccia, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVar.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVar.gpy))
        elif fineanimaz == 0 and (animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata"):
            GlobalVar.schermo.blit(quadrettoSottoEsplosione, ((xFineRetta - (GlobalVar.gpx * 2), yFineRetta - (GlobalVar.gpy * 2))))

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
                GlobalVar.schermo.blit(quadrettoSottoLaFrecciaElettrica, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz) - GlobalVar.gpx), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVar.gpy))
            quadrettoSottoLaFrecciaElettrica = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)) - GlobalVar.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz)) - GlobalVar.gpy, GlobalVar.gpx * 3, GlobalVar.gpy * 3))
        elif fineanimaz == 5:
            GlobalVar.schermo.blit(quadrettoSottoLaFrecciaElettrica, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVar.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVar.gpy))

    # disegno il terreno sotto gli oggetti lanciati dai nemici
    if "attaccoNemici" in azioniDaEseguire and nemicoAttaccante:
        if nemicoAttaccante.attaccaDaLontano and nemicoAttaccante.animaAttacco and not nemicoAttaccante.morto:
            xInizioRetta = nemicoAttaccante.x
            xFineRetta = nemicoAttaccante.obbiettivo[1]
            yInizioRetta = nemicoAttaccante.y
            yFineRetta = nemicoAttaccante.obbiettivo[2]
            if fineanimaz > 5:
                if fineanimaz != 10:
                    GlobalVar.schermo.blit(nemicoAttaccante.quadrettoSottoOggettoLanciato, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz) - GlobalVar.gpx), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVar.gpy))
                nemicoAttaccante.quadrettoSottoOggettoLanciato = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)) - GlobalVar.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz)) - GlobalVar.gpy, GlobalVar.gpx * 3, GlobalVar.gpy * 3))
            elif fineanimaz == 5:
                GlobalVar.schermo.blit(nemicoAttaccante.quadrettoSottoOggettoLanciato, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVar.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVar.gpy))


def disegnaCasellaAccantoAlPersCheAttacca(x, y, attacco, npers, rx, ry, nrob, tecnicaUsata, nemicoAttaccante, schermo_prima_delle_animazioni, cambiosta, azioniDaEseguire, fineanimaz):
    if "attaccoRallo" in azioniDaEseguire and attacco == 1:
        global quadrettoSottoLaSpada
        xAttaccoPers = 0
        yAttaccoPers = 0
        # 1=d, 2=a, 3=w, 4=s
        if npers == 1:
            xAttaccoPers = x + GlobalVar.gpx
            yAttaccoPers = y
        if npers == 2:
            xAttaccoPers = x - GlobalVar.gpx
            yAttaccoPers = y
        if npers == 3:
            xAttaccoPers = x
            yAttaccoPers = y - GlobalVar.gpy
        if npers == 4:
            xAttaccoPers = x
            yAttaccoPers = y + GlobalVar.gpy
        if fineanimaz == 10:
            quadrettoSottoLaSpada = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xAttaccoPers, yAttaccoPers, GlobalVar.gpx, GlobalVar.gpy))
        else:
            GlobalVar.schermo.blit(quadrettoSottoLaSpada, (xAttaccoPers, yAttaccoPers))

    if "attaccoColco" in azioniDaEseguire:
        global quadrettoSottoAttaccoColco
        if tecnicaUsata.startswith("scossa") or tecnicaUsata.startswith("freccia") or tecnicaUsata.startswith("cura") or tecnicaUsata == "antidoto" or tecnicaUsata == "attP" or tecnicaUsata == "difP":
            xAttaccoPers = 0
            yAttaccoPers = 0
            # nrob => 1=d, 2=a, 3=s, 4=w
            if nrob == 1:
                xAttaccoPers = rx + GlobalVar.gpx
                yAttaccoPers = ry
            if nrob == 2:
                xAttaccoPers = rx - GlobalVar.gpx
                yAttaccoPers = ry
            if nrob == 3:
                xAttaccoPers = rx
                yAttaccoPers = ry + GlobalVar.gpy
            if nrob == 4:
                xAttaccoPers = rx
                yAttaccoPers = ry - GlobalVar.gpy
            if fineanimaz == 10:
                quadrettoSottoAttaccoColco = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xAttaccoPers, yAttaccoPers, GlobalVar.gpx, GlobalVar.gpy))
            else:
                GlobalVar.schermo.blit(quadrettoSottoAttaccoColco, (xAttaccoPers, yAttaccoPers))
        elif tecnicaUsata.startswith("tempesta"):
            xAttaccoPers = rx - (GlobalVar.gpx * 8)
            yAttaccoPers = ry - (GlobalVar.gpy * 8)
            xFineAttaccoPers = GlobalVar.gpx * 8
            yFineAttaccoPers = GlobalVar.gpy * 8
            if xAttaccoPers < 0:
                xAttaccoPers = 0
            if yAttaccoPers < 0:
                yAttaccoPers = 0
            if rx + xFineAttaccoPers >= GlobalVar.gsx:
                xFineAttaccoPers = GlobalVar.gsx - rx - GlobalVar.gpx
            if ry + yFineAttaccoPers >= GlobalVar.gsy:
                yFineAttaccoPers = GlobalVar.gsy - ry - GlobalVar.gpy
            if fineanimaz == 10:
                quadrettoSottoAttaccoColco = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xAttaccoPers, yAttaccoPers, (GlobalVar.gpx * 9) + xFineAttaccoPers, (GlobalVar.gpy * 9) + yFineAttaccoPers))
            else:
                GlobalVar.schermo.blit(quadrettoSottoAttaccoColco, (xAttaccoPers, yAttaccoPers))

    if "attaccoNemici" in azioniDaEseguire and nemicoAttaccante and not cambiosta:
        if nemicoAttaccante.animaAttacco:
            xAttaccoNemico = 0
            yAttaccoNemico = 0
            if nemicoAttaccante.direzione == "w":
                xAttaccoNemico = nemicoAttaccante.x
                yAttaccoNemico = nemicoAttaccante.y - GlobalVar.gpy
            if nemicoAttaccante.direzione == "a":
                xAttaccoNemico = nemicoAttaccante.x - GlobalVar.gpx
                yAttaccoNemico = nemicoAttaccante.y
            if nemicoAttaccante.direzione == "s":
                xAttaccoNemico = nemicoAttaccante.x
                yAttaccoNemico = nemicoAttaccante.y + GlobalVar.gpy
            if nemicoAttaccante.direzione == "d":
                xAttaccoNemico = nemicoAttaccante.x + GlobalVar.gpx
                yAttaccoNemico = nemicoAttaccante.y
            if fineanimaz == 10:
                nemicoAttaccante.quadrettoSottoArma = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xAttaccoNemico, yAttaccoNemico, GlobalVar.gpx, GlobalVar.gpy))
            else:
                GlobalVar.schermo.blit(nemicoAttaccante.quadrettoSottoArma, (xAttaccoNemico, yAttaccoNemico))


def animaFrecceLanciate(x, y, attaccoADistanza, animaOggetto, rx, ry, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoAttaccante, cambiosta, azioniDaEseguire, vettoreEsche, fineanimaz):
    # disegno le frecce e gli oggetti lanciati da Rallo
    if "attaccoRallo" in azioniDaEseguire and (attaccoADistanza or animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata") and not cambiosta:
        xInizioRetta = x
        yInizioRetta = y
        if animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata":
            if fineanimaz == 10:
                GlobalVar.canaleSoundAttacco.play(GlobalVar.suonoLancioOggetti)
            xFineRetta = animaOggetto[1]
            yFineRetta = animaOggetto[2]
            imgFrecciaLanciata_temp = 0
            if animaOggetto[0] == "bomba":
                imgFrecciaLanciata_temp = GlobalVar.vetIcoOggettiMenu[5]
            elif animaOggetto[0] == "bombaVeleno":
                imgFrecciaLanciata_temp = GlobalVar.vetIcoOggettiMenu[6]
            elif animaOggetto[0] == "esca":
                imgFrecciaLanciata_temp = GlobalVar.vetIcoOggettiMenu[7]
            elif animaOggetto[0] == "bombaAppiccicosa":
                imgFrecciaLanciata_temp = GlobalVar.vetIcoOggettiMenu[8]
            elif animaOggetto[0] == "bombaPotenziata":
                imgFrecciaLanciata_temp = GlobalVar.vetIcoOggettiMenu[9]
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
            imgFrecciaLanciata_temp = pygame.transform.rotate(GlobalVar.imgFrecciaLanciata, angoloInGradi)
        if fineanimaz > 5:
            GlobalVar.schermo.blit(imgFrecciaLanciata_temp, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz))))
        elif animaOggetto[0] and fineanimaz > 0:
            if animaOggetto[0] == "bomba":
                GlobalVar.schermo.blit(GlobalVar.imgAnimaBomba, (animaOggetto[1] - GlobalVar.gpx, animaOggetto[2] - GlobalVar.gpy))
                if fineanimaz == 5:
                    GlobalVar.canaleSoundAttacco.play(GlobalVar.suonoUsoBomba)
            elif animaOggetto[0] == "bombaVeleno":
                GlobalVar.schermo.blit(GlobalVar.imgAnimaBombaVeleno, (animaOggetto[1], animaOggetto[2]))
                if fineanimaz == 5:
                    GlobalVar.canaleSoundAttacco.play(GlobalVar.suonoUsoBombaVeleno)
            elif animaOggetto[0] == "esca":
                GlobalVar.schermo.blit(GlobalVar.vetIcoOggettiMenu[7], (animaOggetto[1], animaOggetto[2]))
                if fineanimaz == 5:
                    GlobalVar.canaleSoundAttacco.play(GlobalVar.suonoUsoEsca)
            elif animaOggetto[0] == "bombaAppiccicosa":
                GlobalVar.schermo.blit(GlobalVar.imgAnimaBombaAppiccicosa, (animaOggetto[1], animaOggetto[2]))
                if fineanimaz == 5:
                    GlobalVar.canaleSoundAttacco.play(GlobalVar.suonoUsoBombaAppiccicosa)
            elif animaOggetto[0] == "bombaPotenziata":
                GlobalVar.schermo.blit(GlobalVar.imgAnimaBombaPotenziata, (animaOggetto[1] - (GlobalVar.gpx * 2), animaOggetto[2] - (GlobalVar.gpy * 2)))
                if fineanimaz == 5:
                    GlobalVar.canaleSoundAttacco.play(GlobalVar.suonoUsoBombaPotenziata)

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
            imgFrecciaLanciata_temp = pygame.transform.rotate(GlobalVar.imgFrecciaEletttricaLanciata, angoloInGradi)
        elif tecnicaUsata == "freccia+":
            imgFrecciaLanciata_temp = pygame.transform.rotate(GlobalVar.imgFrecciaEletttricaLanciataP, angoloInGradi)
        elif tecnicaUsata == "freccia++":
            imgFrecciaLanciata_temp = pygame.transform.rotate(GlobalVar.imgFrecciaEletttricaLanciataPP, angoloInGradi)
        if fineanimaz > 5:
            GlobalVar.schermo.blit(imgFrecciaLanciata_temp, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz))))

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
                GlobalVar.schermo.blit(imgFrecciaLanciata_temp, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz))))
            elif fineanimaz != 0:
                GlobalVar.schermo.blit(nemicoAttaccante.imgDanneggiamentoOggettoLanciato, (xFineRetta, yFineRetta))


def animaVitaRalloNemicoInquadrato(dati, nemicoInquadrato, vettoreEsche, difesa, azioniDaEseguire, nemicoAttaccante, attaccoDiRallo, attaccoDiColco, statoRalloInizioTurno, statoColcoInizioTurno, statoEscheInizioTurno, listaNemici, fineanimaz, aumentoliv, apriocchio, chiamarob):
    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati, difesa)

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
        pvtot = getVitaTotRallo(dati[4] - aumentoliv, dati[129])
        pvRallo = pvtot
        velenoRallo = False
    lungvitatot = int(((GlobalVar.gpx * pvtot) / float(4)) // 5)
    lungvita = (lungvitatot * pvRallo) // pvtot
    if lungvita < 0:
        lungvita = 0
    indvitapers = pygame.transform.smoothscale(GlobalVar.indvita, (lungvitatot, GlobalVar.gpy // 4))
    fineindvitapers = GlobalVar.fineindvita
    vitaral = pygame.transform.smoothscale(GlobalVar.vitapersonaggio, (lungvita, GlobalVar.gpy // 4))
    GlobalVar.schermo.blit(GlobalVar.sfondoRallo, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 17))
    GlobalVar.schermo.blit(indvitapers, (GlobalVar.gsx // 32 * 1, (GlobalVar.gsy // 18 * 17) + (GlobalVar.gpy // 4 * 3)))
    GlobalVar.schermo.blit(fineindvitapers, ((GlobalVar.gsx // 32 * 1) + lungvitatot, (GlobalVar.gsy // 18 * 17) + (GlobalVar.gpy // 4 * 3)))
    GlobalVar.schermo.blit(vitaral, (GlobalVar.gsx // 32 * 1, (GlobalVar.gsy // 18 * 17) + (GlobalVar.gpy // 4 * 3)))
    GlobalVar.schermo.blit(GlobalVar.perss, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 17))
    GlobalVar.schermo.blit(GlobalVar.perssb, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 17))
    GlobalVar.schermo.blit(GlobalVar.imgNumFrecce, (int(GlobalVar.gsx // 32 * 1.2), GlobalVar.gsy // 18 * 17))
    messaggio(" x" + str(dati[132]), GlobalVar.grigiochi, int(GlobalVar.gsx // 32 * 1.8), int(GlobalVar.gsy // 18 * 17.3), 40)
    if velenoRallo:
        GlobalVar.schermo.blit(GlobalVar.avvelenato, (GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 17))
    if attPRallo > 0:
        GlobalVar.schermo.blit(GlobalVar.attaccopiu, (GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 17))
    if difPRallo > 0:
        GlobalVar.schermo.blit(GlobalVar.difesapiu, (GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 17))

    # disegno la vita del Colco / esca / mostro selezionato
    if nemicoInquadrato == "Colco" or (not nemicoInquadrato and dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]):
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
        lungentot = int(((GlobalVar.gpx * entot) / float(4)) // 15)
        lungen = int(((GlobalVar.gpx * pvColco) / float(4)) // 15)
        if lungen < 0:
            lungen = 0
        indvitarob = pygame.transform.smoothscale(GlobalVar.indvita, (lungentot, GlobalVar.gpy // 4))
        fineindvitarob = GlobalVar.fineindvita
        vitarob = pygame.transform.smoothscale(GlobalVar.vitarobo, (lungen, GlobalVar.gpy // 4))
        GlobalVar.schermo.blit(GlobalVar.sfondoColco, (0, 0))
        GlobalVar.schermo.blit(indvitarob, (GlobalVar.gpx, 0))
        GlobalVar.schermo.blit(fineindvitarob, (GlobalVar.gpx + lungentot, 0))
        GlobalVar.schermo.blit(vitarob, (GlobalVar.gpx, 0))
        GlobalVar.schermo.blit(GlobalVar.robos, (0, 0))
        if surriscaldaColco > 0:
            GlobalVar.schermo.blit(GlobalVar.surriscaldato, (GlobalVar.gpx + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
        if velPColco > 0:
            GlobalVar.schermo.blit(GlobalVar.velocitapiu, ((GlobalVar.gpx * 2) + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
        if effPColco > 0:
            GlobalVar.schermo.blit(GlobalVar.efficienzapiu, ((GlobalVar.gpx * 3) + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))

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
                lungvita = int(((GlobalVar.gpx * pvEsca) / float(4)) // 15)
                if lungvita < 0:
                    lungvita = 0
                GlobalVar.schermo.blit(GlobalVar.sfondoEsche, (0, 0))
                GlobalVar.schermo.blit(GlobalVar.esche, (0, 0))
                indvitamost = pygame.transform.smoothscale(GlobalVar.indvita, (int(((GlobalVar.gpx * 1000) / float(4)) // 15), GlobalVar.gpy // 4))
                fineindvitamost = GlobalVar.fineindvita
                vitaesche = pygame.transform.smoothscale(GlobalVar.vitanemico0, (lungvita, GlobalVar.gpy // 4))
                GlobalVar.schermo.blit(indvitamost, (GlobalVar.gpx, 0))
                GlobalVar.schermo.blit(fineindvitamost, (GlobalVar.gpx + (int(((GlobalVar.gpx * 1000) / float(4)) // 15)), 0))
                GlobalVar.schermo.blit(vitaesche, (GlobalVar.gpx, 0))
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
        GlobalVar.schermo.blit(GlobalVar.sfondoMostro, (0, 0))
        if nemicoAvvelenato:
            GlobalVar.schermo.blit(GlobalVar.avvelenato, (GlobalVar.gpx + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
        if nemicoAppiccicato:
            GlobalVar.schermo.blit(GlobalVar.appiccicoso, ((GlobalVar.gpx * 2) + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
        GlobalVar.schermo.blit(nemicoInquadrato.imgS, (0, 0))
        fineindvitamost = GlobalVar.fineindvita
        if pvmtot > 1500:
            indvitamost = pygame.transform.smoothscale(GlobalVar.indvita, (int(((GlobalVar.gpx * 1500) / float(4)) // 15), GlobalVar.gpy // 4))
            lungvitatot = int(((GlobalVar.gpx * 1500) / float(4)) // 15)
            GlobalVar.schermo.blit(fineindvitamost, (GlobalVar.gpx + lungvitatot, 0))
            if pvm > 15000:
                pvm = 1500
                vitanemsucc = pygame.transform.smoothscale(GlobalVar.vitanemico00, (int(((GlobalVar.gpx * 1500) / float(4)) // 15), GlobalVar.gpy // 4))
                vitanemico = GlobalVar.vitanemico9
            elif pvm > 13500:
                pvm -= 13500
                vitanemsucc = pygame.transform.smoothscale(GlobalVar.vitanemico8, (int(((GlobalVar.gpx * 1500) / float(4)) // 15), GlobalVar.gpy // 4))
                vitanemico = GlobalVar.vitanemico9
            elif pvm > 12000:
                pvm -= 12000
                vitanemsucc = pygame.transform.smoothscale(GlobalVar.vitanemico7, (int(((GlobalVar.gpx * 1500) / float(4)) // 15), GlobalVar.gpy // 4))
                vitanemico = GlobalVar.vitanemico8
            elif pvm > 10500:
                pvm -= 10500
                vitanemsucc = pygame.transform.smoothscale(GlobalVar.vitanemico6, (int(((GlobalVar.gpx * 1500) / float(4)) // 15), GlobalVar.gpy // 4))
                vitanemico = GlobalVar.vitanemico7
            elif pvm > 9000:
                pvm -= 9000
                vitanemsucc = pygame.transform.smoothscale(GlobalVar.vitanemico5, (int(((GlobalVar.gpx * 1500) / float(4)) // 15), GlobalVar.gpy // 4))
                vitanemico = GlobalVar.vitanemico6
            elif pvm > 7500:
                pvm -= 7500
                vitanemsucc = pygame.transform.smoothscale(GlobalVar.vitanemico4, (int(((GlobalVar.gpx * 1500) / float(4)) // 15), GlobalVar.gpy // 4))
                vitanemico = GlobalVar.vitanemico5
            elif pvm > 6000:
                pvm -= 6000
                vitanemsucc = pygame.transform.smoothscale(GlobalVar.vitanemico3, (int(((GlobalVar.gpx * 1500) / float(4)) // 15), GlobalVar.gpy // 4))
                vitanemico = GlobalVar.vitanemico4
            elif pvm > 4500:
                pvm -= 4500
                vitanemsucc = pygame.transform.smoothscale(GlobalVar.vitanemico2, (int(((GlobalVar.gpx * 1500) / float(4)) // 15), GlobalVar.gpy // 4))
                vitanemico = GlobalVar.vitanemico3
            elif pvm > 3000:
                pvm -= 3000
                vitanemsucc = pygame.transform.smoothscale(GlobalVar.vitanemico1, (int(((GlobalVar.gpx * 1500) / float(4)) // 15), GlobalVar.gpy // 4))
                vitanemico = GlobalVar.vitanemico2
            elif pvm > 1500:
                pvm -= 1500
                vitanemsucc = pygame.transform.smoothscale(GlobalVar.vitanemico0, (int(((GlobalVar.gpx * 1500) / float(4)) // 15), GlobalVar.gpy // 4))
                vitanemico = GlobalVar.vitanemico1
            else:
                vitanemsucc = pygame.transform.smoothscale(GlobalVar.vitanemico00, (int(((GlobalVar.gpx * 1500) / float(4)) // 15), GlobalVar.gpy // 4))
                vitanemico = GlobalVar.vitanemico0
        else:
            lungvitatot = int(((GlobalVar.gpx * pvmtot) / float(4)) // 15)
            indvitamost = pygame.transform.smoothscale(GlobalVar.indvita, (lungvitatot, GlobalVar.gpy // 4))
            GlobalVar.schermo.blit(fineindvitamost, (GlobalVar.gpx + lungvitatot, 0))
            vitanemsucc = pygame.transform.smoothscale(GlobalVar.vitanemico00, (lungvitatot, GlobalVar.gpy // 4))
            vitanemico = GlobalVar.vitanemico0
        lungvita = int(((GlobalVar.gpx * pvm) / float(4)) // 15)
        if lungvita < 0:
            lungvita = 0
        vitanem = pygame.transform.smoothscale(vitanemico, (lungvita, GlobalVar.gpy // 4))
        GlobalVar.schermo.blit(indvitamost, (GlobalVar.gpx, 0))
        GlobalVar.schermo.blit(vitanemsucc, (GlobalVar.gpx, 0))
        GlobalVar.schermo.blit(vitanem, (GlobalVar.gpx, 0))

    # backbround occhio/chiave
    GlobalVar.schermo.blit(GlobalVar.sfochiaveocchio, (GlobalVar.gsx - (GlobalVar.gpx * 5), 0))
    # vista nemici
    if apriocchio:
        GlobalVar.schermo.blit(GlobalVar.occhioape, (GlobalVar.gsx - (GlobalVar.gpx * 1.4), GlobalVar.gpy * 0.3))
    else:
        GlobalVar.schermo.blit(GlobalVar.occhiochiu, (GlobalVar.gsx - (GlobalVar.gpx * 1.4), GlobalVar.gpy * 0.3))
    # chiave robo
    if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
        if chiamarob:
            GlobalVar.schermo.blit(GlobalVar.chiaveroboacc, (GlobalVar.gsx - (GlobalVar.gpx * 4), 0))
        else:
            GlobalVar.schermo.blit(GlobalVar.chiaverobospe, (GlobalVar.gsx - (GlobalVar.gpx * 4), 0))

    return statoRalloInizioTurno, statoColcoInizioTurno


def disagnaPuntatoreInquadraNemici(nemicoInquadrato, rx, ry, vettoreEsche):
    if nemicoInquadrato == "Colco":
        GlobalVar.schermo.blit(GlobalVar.puntatoreInquadraNemici, (rx, ry))
    elif not type(nemicoInquadrato) is str and nemicoInquadrato:
        GlobalVar.schermo.blit(GlobalVar.puntatoreInquadraNemici, (nemicoInquadrato.x, nemicoInquadrato.y))
    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
        idEscaInquadrata = int(nemicoInquadrato[4:])
        i = 0
        while i < len(vettoreEsche):
            if idEscaInquadrata == vettoreEsche[i]:
                GlobalVar.schermo.blit(GlobalVar.puntatoreInquadraNemici, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                break
            i += 4


def animaPersonaggiFermi(listaPersonaggi, azioniDaEseguire, cambiosta, fineanimaz):
    if not cambiosta:
        for personaggio in listaPersonaggi:
            if personaggio.inCasellaVista and not personaggio.mantieniSempreASchermo and not ("movimentoColcoNemiciPersonaggi" in azioniDaEseguire and personaggio.animaSpostamento) and not personaggio.animazioneFatta or (personaggio.inCasellaVista and fineanimaz == 0):
                if personaggio.animazioneFatta:
                    GlobalVar.schermo.blit(personaggio.imgAttuale, (personaggio.x, personaggio.y))
                else:
                    GlobalVar.schermo.blit(personaggio.imgAttuale, (personaggio.vx, personaggio.vy))


def animaSpostamentoPersonaggi(listaPersonaggi, animazionePersonaggi, cambiosta, fineanimaz):
    if not cambiosta:
        for personaggio in listaPersonaggi:
            if personaggio.inCasellaVista and not personaggio.mantieniSempreASchermo and personaggio.animaSpostamento and (personaggio.x != personaggio.vx or personaggio.y != personaggio.vy):
                personaggio.animazioneFatta = True
                animazionePersonaggi = True
                if not GlobalVar.canaleSoundPassiNemiciPersonaggi.get_busy() and fineanimaz > 6:
                    GlobalVar.canaleSoundPassiNemiciPersonaggi.play(GlobalVar.rumoreMovimentoNemiciPersonaggi)
                if personaggio.direzione == "d":
                    if 5 < fineanimaz <= 10:
                        GlobalVar.schermo.blit(personaggio.imgDMov1, (personaggio.x - (GlobalVar.gpx * fineanimaz // 10), personaggio.y))
                    if 0 < fineanimaz <= 5:
                        GlobalVar.schermo.blit(personaggio.imgDMov2, (personaggio.x - (GlobalVar.gpx * fineanimaz // 10), personaggio.y))
                if personaggio.direzione == "a":
                    if 5 < fineanimaz <= 10:
                        GlobalVar.schermo.blit(personaggio.imgAMov1, (personaggio.x + (GlobalVar.gpx * fineanimaz // 10), personaggio.y))
                    if 0 < fineanimaz <= 5:
                        GlobalVar.schermo.blit(personaggio.imgAMov2, (personaggio.x + (GlobalVar.gpx * fineanimaz // 10), personaggio.y))
                if personaggio.direzione == "w":
                    if 5 < fineanimaz <= 10:
                        GlobalVar.schermo.blit(personaggio.imgWMov1, (personaggio.x, personaggio.y + (GlobalVar.gpy * fineanimaz // 10)))
                    if 0 < fineanimaz <= 5:
                        GlobalVar.schermo.blit(personaggio.imgWMov2, (personaggio.x, personaggio.y + (GlobalVar.gpy * fineanimaz // 10)))
                if personaggio.direzione == "s":
                    if 5 < fineanimaz <= 10:
                        GlobalVar.schermo.blit(personaggio.imgSMov1, (personaggio.x, personaggio.y - (GlobalVar.gpy * fineanimaz // 10)))
                    if 0 < fineanimaz <= 5:
                        GlobalVar.schermo.blit(personaggio.imgSMov2, (personaggio.x, personaggio.y - (GlobalVar.gpy * fineanimaz // 10)))
    return animazionePersonaggi


def anima(sposta, x, y, vx, vy, rx, ry, vrx, vry, pers, robot, npers, nrob, primopasso, cambiosta, casellaChiara, casellaScura, scudo, armatura, arma, armaMov1, armaMov2, armaAttacco, scudoDifesa, arco, faretra, arcoAttacco, guanti, guantiMov1, guantiMov2, guantiAttacco, guantiDifesa, collana, armaS, armaturaS, arcoS, faretraS, collanaS, armrob, armrobS, dati, attacco, difesa, bottoneDown, tesoro, aumentoliv, caricaTutto, listaNemici, vettoreEsche, vettoreDenaro, attaccoADistanza, caseviste, porte, cofanetti, portaOriz, portaVert, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoInquadrato, attaccoDiRallo, attaccoDiColco, statoRalloInizioTurno, statoColcoInizioTurno, statoEscheInizioTurno, raffreddamento, ricarica1, ricarica2, raffredda, autoRic1, autoRic2, animaOggetto, listaPersonaggi, apriocchio, chiamarob, movimentoPerMouse, vettoreImgCaselle):
    schermo_prima_delle_animazioni = GlobalVar.schermo.copy().convert()

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
        GlobalVar.schermo.blit(GlobalVar.occhioape, (GlobalVar.gsx - (GlobalVar.gpx * 1.4), GlobalVar.gpy * 0.3))
    else:
        GlobalVar.schermo.blit(GlobalVar.occhiochiu, (GlobalVar.gsx - (GlobalVar.gpx * 1.4), GlobalVar.gpy * 0.3))

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
                            GlobalVar.schermo.blit(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                            disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1], casellaChiara, casellaScura)
                            break
                        i += 3
            else:
                i = 0
                while i < len(vettoreImgCaselle):
                    if x == vettoreImgCaselle[i] and y == vettoreImgCaselle[i + 1]:
                        GlobalVar.schermo.blit(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                        disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1], casellaChiara, casellaScura)
                    if vx == vettoreImgCaselle[i] and vy == vettoreImgCaselle[i + 1]:
                        GlobalVar.schermo.blit(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                        disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1], casellaChiara, casellaScura)
                    if rx == vettoreImgCaselle[i] and ry == vettoreImgCaselle[i + 1]:
                        GlobalVar.schermo.blit(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                        disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1], casellaChiara, casellaScura)
                    if vrx == vettoreImgCaselle[i] and vry == vettoreImgCaselle[i + 1]:
                        GlobalVar.schermo.blit(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                        disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1], casellaChiara, casellaScura)
                    for nemico in listaNemici:
                        if nemico.inCasellaVista:
                            if nemico.x == vettoreImgCaselle[i] and nemico.y == vettoreImgCaselle[i + 1]:
                                GlobalVar.schermo.blit(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                                disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1], casellaChiara, casellaScura)
                            if nemico.vx == vettoreImgCaselle[i] and nemico.vy == vettoreImgCaselle[i + 1]:
                                GlobalVar.schermo.blit(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                                disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1], casellaChiara, casellaScura)
                    for personaggio in listaPersonaggi:
                        if personaggio.inCasellaVista and not personaggio.mantieniSempreASchermo:
                            if personaggio.x == vettoreImgCaselle[i] and personaggio.y == vettoreImgCaselle[i + 1]:
                                GlobalVar.schermo.blit(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                                disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1], casellaChiara, casellaScura)
                            if personaggio.vx == vettoreImgCaselle[i] and personaggio.vy == vettoreImgCaselle[i + 1]:
                                GlobalVar.schermo.blit(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                                disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1], casellaChiara, casellaScura)
                    i += 3

            # disegno: esche, denaro, cofanetti e porte
            animaEsche(vettoreEsche, caseviste, casellaChiara, casellaScura, azioniDaEseguire, animaOggetto, vettoreImgCaselle, morteEscheAnimata)
            animaDenaro(vettoreDenaro, caseviste, casellaChiara, casellaScura, vettoreImgCaselle)
            animaCofanetti(cofanetti, caseviste)
            animaPorte(porte, caseviste, portaOriz, portaVert)

            if fineanimaz == 10:
                schermo_prima_delle_animazioni = GlobalVar.schermo.copy().convert()
            eliminaOggettoLanciato(x, y, attaccoADistanza, animaOggetto, rx, ry, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoAttaccante, schermo_prima_delle_animazioni, cambiosta, azioniDaEseguire, vettoreEsche, fineanimaz)
            disegnaCasellaAccantoAlPersCheAttacca(x, y, attacco, npers, rx, ry, nrob, tecnicaUsata, nemicoAttaccante, schermo_prima_delle_animazioni, cambiosta, azioniDaEseguire, fineanimaz)

            if cambiosta:
                quadrettoSottoRallo = schermo_prima_delle_animazioni.subsurface(pygame.Rect(x - GlobalVar.gpx, y - GlobalVar.gpy, GlobalVar.gpx * 3, GlobalVar.gpy * 3))
                GlobalVar.schermo.blit(quadrettoSottoRallo, (x - GlobalVar.gpx, y - GlobalVar.gpy))

            # disegna personaggi se ci sono animazioni ma non loro
            animaColcoFermo(rx, ry, vrx, vry, robot, armrob, armrobS, statoColcoInizioTurno[1], tecnicaUsata, azioniDaEseguire, animazioneColcoFatta, raffreddamento, ricarica1, ricarica2, raffredda, autoRic1, autoRic2, fineanimaz)
            animaNemiciFermi(listaNemici, azioniDaEseguire, cambiosta, nemicoAttaccante, fineanimaz)
            animaPersonaggiFermi(listaPersonaggi, azioniDaEseguire, cambiosta, fineanimaz)
            if not cambiosta:
                animaRalloFermo(x, y, vx, vy, npers, pers, scudo, armatura, arma, arco, faretra, guanti, collana, statoRalloInizioTurno[1], azioniDaEseguire, animazioneRalloFatta, nemicoAttaccante, difesa, fineanimaz)

            # tolgo il rumore passi quando non c'è l'animazione
            if not "movimentoRallo" in azioniDaEseguire and GlobalVar.canaleSoundPassiRallo.get_busy():
                GlobalVar.canaleSoundPassiRallo.stop()
            # animazione difesa Rallo
            animazioneRallo = animaDifesaRallo(x, y, armaS, armaturaS, arcoS, faretraS, collanaS, scudoDifesa, guantiDifesa, statoRalloInizioTurno[1], difesa, animazioneRallo, nemicoAttaccante, fineanimaz)

            if "aumentaLv" in azioniDaEseguire:
                # animazione aumento di livello
                animazioneRallo, caricaTutto, bottoneDown, aumentoliv, movimentoPerMouse = animaLvUp(x, y, npers, pers, arma, armatura, scudo, collana, arco, faretra, guanti, dati[4], aumentoliv, caricaTutto, bottoneDown, animazioneRallo, movimentoPerMouse, fineanimaz)

            if "movimentoColcoNemiciPersonaggi" in azioniDaEseguire:
                # animazione camminata robo
                animazioneColco = animaCamminataRobo(nrob, rx, ry, vrx, vry, robot, armrob, statoColcoInizioTurno[1], cambiosta, animazioneColco, fineanimaz)
                # animazione camminata mostri
                animazioneNemici = animaSpostamentoNemici(listaNemici, animazioneNemici, cambiosta, fineanimaz)
                # animazione camminata personaggi
                animazionePersonaggi = animaSpostamentoPersonaggi(listaPersonaggi, animazionePersonaggi, cambiosta, fineanimaz)

            if "movimentoRallo" in azioniDaEseguire:
                # animazione camminata personaggio
                animazioneRallo, primopasso = animaCamminataRallo(sposta, x, y, vx, vy, primopasso, cambiosta, npers, pers, arma, scudo, armatura, armaMov1, armaMov2, arco, faretra, guanti, guantiMov1, guantiMov2, collana, statoRalloInizioTurno[1], difesa, animazioneRallo, fineanimaz)

            if "attaccoNemici" in azioniDaEseguire:
                # animazione danneggiamento Colco
                robot, armrob, statoColcoInizioTurno[1] = animaDanneggiamentoColco(rx, ry, robot, armrob, statoColcoInizioTurno[1], nemicoAttaccante, attaccoDiRallo, cambiosta, azioniDaEseguire, fineanimaz)
                # animazione morte esche
                morteEscheAnimata = animaMorteEsche(x, y, vettoreEsche, casellaChiara, casellaScura, vettoreImgCaselle, nemicoAttaccante, attaccoDiColco, attaccoDiRallo, morteEscheAnimata, azioniDaEseguire, fineanimaz)

                # animazione attacco nemici
                animaFrecceLanciate(x, y, attaccoADistanza, animaOggetto, rx, ry, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoAttaccante, cambiosta, azioniDaEseguire, vettoreEsche, fineanimaz)
                animazioneNemici = animaAttaccoNemici(nemicoAttaccante, animazioneNemici, fineanimaz)

            if "attaccoRallo" in azioniDaEseguire:
                # animazione danneggiamento Colco
                robot, armrob, statoColcoInizioTurno[1] = animaDanneggiamentoColco(rx, ry, robot, armrob, statoColcoInizioTurno[1], nemicoAttaccante, attaccoDiRallo, cambiosta, azioniDaEseguire, fineanimaz)
                # animazione morte esche
                morteEscheAnimata = animaMorteEsche(x, y, vettoreEsche, casellaChiara, casellaScura, vettoreImgCaselle, nemicoAttaccante, attaccoDiColco, attaccoDiRallo, morteEscheAnimata, azioniDaEseguire, fineanimaz)

                # animazione attacco Rallo
                animazioneRallo = animaAttaccoRallo(sposta, x, y, npers, pers, arma, scudo, armatura, collana, arco, faretra, guanti, armaAttacco, arcoAttacco, guantiAttacco, statoRalloInizioTurno[1], attacco, difesa, vrx, vry, armrobS, casellaChiara, casellaScura, animazioneRallo, attaccoADistanza, animaOggetto, vettoreImgCaselle, fineanimaz)
                # animazione danneggiamento Rallo
                animaDanneggiamentoRallo(x, y, attaccoDiColco, attaccoDiRallo, tecnicaUsata, azioniDaEseguire, fineanimaz)
                # animazione oggetto lanciato
                animaFrecceLanciate(x, y, attaccoADistanza, animaOggetto, rx, ry, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, listaNemici, cambiosta, azioniDaEseguire, vettoreEsche, fineanimaz)

                # animazione danneggiamento dei nemici
                animazioneNemici = animaDanneggiamentoNemici(attaccoADistanza, animaOggetto, listaNemici, animazioneNemici, cambiosta, azioniDaEseguire, "Rallo", fineanimaz)

            if "attaccoColco" in azioniDaEseguire:
                # animazione morte esche
                morteEscheAnimata = animaMorteEsche(x, y, vettoreEsche, casellaChiara, casellaScura, vettoreImgCaselle, nemicoAttaccante, attaccoDiColco, attaccoDiRallo, morteEscheAnimata, azioniDaEseguire, fineanimaz)

                # animazione attacco Colco
                animaFrecceLanciate(x, y, attaccoADistanza, animaOggetto, rx, ry, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, listaNemici, cambiosta, azioniDaEseguire, vettoreEsche, fineanimaz)
                animazioneColco = animaTecnicaColco(rx, ry, nrob, robot, armrob, armrobS, tecnicaUsata, cambiosta, animazioneColco, statoColcoInizioTurno[1], fineanimaz)

                # animazione danneggiamento dei nemici
                animazioneNemici = animaDanneggiamentoNemici(attaccoADistanza, animaOggetto, listaNemici, animazioneNemici, cambiosta, azioniDaEseguire, "Colco", fineanimaz)
                # animazione danneggiamento Rallo
                animaDanneggiamentoRallo(x, y, attaccoDiColco, attaccoDiRallo, tecnicaUsata, azioniDaEseguire, fineanimaz)

            statoRalloInizioTurno, statoColcoInizioTurno = animaVitaRalloNemicoInquadrato(dati, nemicoInquadrato, vettoreEsche, difesa, azioniDaEseguire, nemicoAttaccante, attaccoDiRallo, attaccoDiColco, statoRalloInizioTurno, statoColcoInizioTurno, statoEscheInizioTurno, listaNemici, fineanimaz, aumentoliv, apriocchio, chiamarob)

            # animazione apertura cofanetto
            animazioneRallo = animaAperturaCofanetto(tesoro, x, y, npers, animazioneRallo)
            # anima raccolta denaro
            denaroRaccolto = animaRaccoltaDenaro(x, y, vettoreDenaro, fineanimaz)

            # disegno img puntatoreInquadraNemici
            disagnaPuntatoreInquadraNemici(nemicoInquadrato, rx, ry, vettoreEsche)

            if animazioneRallo:
                animazioneRalloFatta = True
            if animazioneColco:
                animazioneColcoFatta = True

            pygame.event.pump()
            if (animazioneNemici or animazioneRallo or animazioneColco or animazionePersonaggi) and fineanimaz >= 0:
                pygame.display.update()
                GlobalVar.clockAnimazioni.tick(GlobalVar.fpsAnimazioni)
                # print (GlobalVar.clockAnimazioni.get_fps())
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
        if GlobalVar.mouseBloccato:
            GlobalVar.configuraCursore(False)
        pygame.display.update()
        risposta = False
        bottoneDown = False
        while not risposta:
            # gestione degli input
            bottoneDown, aggiornaInterfacciaPerCambioInput = getInput(bottoneDown, False)
            if bottoneDown == pygame.K_SPACE or bottoneDown == "mouseSinistro" or bottoneDown == "padCroce":
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                risposta = True
                bottoneDown = False
            if bottoneDown:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                bottoneDown = False
        movimentoPerMouse = False
        caricaTutto = True
        tesoro = -1
    if denaroRaccolto:
        if GlobalVar.mouseBloccato:
            GlobalVar.configuraCursore(False)
        pygame.display.update()
        risposta = False
        bottoneDown = False
        while not risposta:
            # gestione degli input
            bottoneDown, aggiornaInterfacciaPerCambioInput = getInput(bottoneDown, False)
            if bottoneDown == pygame.K_SPACE or bottoneDown == "mouseSinistro" or bottoneDown == "padCroce":
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                risposta = True
                bottoneDown = False
            if bottoneDown:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                bottoneDown = False
        movimentoPerMouse = False
        caricaTutto = True
        bottoneDown = False

    return primopasso, caricaTutto, tesoro, bottoneDown, movimentoPerMouse, robot, armrob
