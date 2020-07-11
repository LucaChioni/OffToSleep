# -*- coding: utf-8 -*-

from GenericFuncG2 import *
import math


def animaCamminataRalloCambiosta(npers, x, y, scudo, armatura, armaMov1, arco, faretra, guantiMov1, collana, avvele, fineanimaz):
    if npers == 1:
        x = x - (GlobalVarG2.gpx * fineanimaz // 10)
    if npers == 2:
        x = x + (GlobalVarG2.gpx * fineanimaz // 10)
    if npers == 3:
        y = y + (GlobalVarG2.gpy * fineanimaz // 10)
    if npers == 4:
        y = y - (GlobalVarG2.gpy * fineanimaz // 10)
    pers = False
    if 5 < fineanimaz <= 10:
        frame = 1
        disegnaRallo(npers, x, y, avvele, pers, armaMov1, armatura, scudo, collana, arco, faretra, guantiMov1, True, frame)


def animaCamminataRalloSpostato(npers, x, y, scudo, armatura, armaMov1, armaMov2, arco, faretra, guantiMov1, guantiMov2, collana, avvele, fineanimaz):
    if npers == 1:
        x = x - (GlobalVarG2.gpx * fineanimaz // 10)
    if npers == 2:
        x = x + (GlobalVarG2.gpx * fineanimaz // 10)
    if npers == 3:
        y = y + (GlobalVarG2.gpy * fineanimaz // 10)
    if npers == 4:
        y = y - (GlobalVarG2.gpy * fineanimaz // 10)
    pers = False
    if 5 < fineanimaz <= 10:
        frame = 1
        disegnaRallo(npers, x, y, avvele, pers, armaMov1, armatura, scudo, collana, arco, faretra, guantiMov1, True, frame)
    elif 0 < fineanimaz <= 5:
        frame = 2
        disegnaRallo(npers, x, y, avvele, pers, armaMov2, armatura, scudo, collana, arco, faretra, guantiMov2, True, frame)


def animaCamminataRalloFermo(npers, x, y, scudo, armatura, armaMov1, armaMov2, arco, faretra, guantiMov1, guantiMov2, collana, avvele, fineanimaz):
    pers = False
    if 5 < fineanimaz <= 10:
        frame = 1
        disegnaRallo(npers, x, y, avvele, pers, armaMov1, armatura, scudo, collana, arco, faretra, guantiMov1, True, frame)
    elif 0 < fineanimaz <= 5:
        frame = 2
        disegnaRallo(npers, x, y, avvele, pers, armaMov2, armatura, scudo, collana, arco, faretra, guantiMov2, True, frame)


def animaCamminataRallo(sposta, x, y, vx, vy, primopasso, cambiosta, npers, pers, arma, scudo, armatura, armaMov1, armaMov2, arco, faretra, guanti, guantiMov1, guantiMov2, collana, avvele, attacco, difesa, tastop, animazioneRallo, movimentoPerMouse, fineanimaz):
    if sposta:
        # mentre ci si sposta
        if x != vx or y != vy:
            animazioneRallo = True
            if not GlobalVarG2.canaleSoundPassiRallo.get_busy():
                GlobalVarG2.canaleSoundPassiRallo.play(GlobalVarG2.rumorecamminata)
            if primopasso and not cambiosta:
                primopasso = False
            # camminata quando si entra in una stanza
            if cambiosta:
                animaCamminataRalloCambiosta(npers, x, y, scudo, armatura, armaMov1, arco, faretra, guantiMov1, collana, avvele, fineanimaz)
                if fineanimaz == 0:
                    GlobalVarG2.canaleSoundPassiRallo.stop()
            # camminata quando non si entra in una stanza
            else:
                animaCamminataRalloSpostato(npers, x, y, scudo, armatura, armaMov1, armaMov2, arco, faretra, guantiMov1, guantiMov2, collana, avvele, fineanimaz)
        # mentre non ci si sposta
        elif attacco == 0 and not difesa and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d or (tastop == "mouseSinistro" and movimentoPerMouse)):
            animazioneRallo = True
            if not GlobalVarG2.canaleSoundPassiRallo.get_busy():
                GlobalVarG2.canaleSoundPassiRallo.play(GlobalVarG2.rumorecamminata)
            if primopasso:
                primopasso = False
            animaCamminataRalloFermo(npers, x, y, scudo, armatura, armaMov1, armaMov2, arco, faretra, guantiMov1, guantiMov2, collana, avvele, fineanimaz)
        # quando si apre una porta
        elif difesa == 0:
            animazioneRallo = True
            disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
    elif GlobalVarG2.canaleSoundPassiRallo.get_busy():
        GlobalVarG2.canaleSoundPassiRallo.stop()
    return animazioneRallo, primopasso


def animaAttaccoRallo(sposta, x, y, npers, pers, arma, scudo, armatura, collana, arco, faretra, guanti, armaAttacco, arcoAttacco, guantiAttacco, avvele, attacco, difesa, vrx, vry, armrobS, sfondinoa, sfondinob, animazioneRallo, attaccoADistanza, animaOggetto, fineanimaz):
    if sposta and fineanimaz != 0:
        if attacco == 1 and difesa == 0:
            animazioneRallo = True
            if attaccoADistanza:
                if fineanimaz == 10:
                    GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.rumoreLancioFreccia)
                elif fineanimaz == 5:
                    GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.rumoreAttaccoArco)
                disegnaRallo(npers, x, y, avvele, pers, armaAttacco, armatura, scudo, collana, arcoAttacco, faretra, guantiAttacco, False, False, False, True)
            else:
                if fineanimaz == 10:
                    GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.rumoreAttaccoSpada)
                disegnaRallo(npers, x, y, avvele, pers, armaAttacco, armatura, scudo, collana, arco, faretra, guantiAttacco, False, False, True)
        elif animaOggetto[0]:
            animazioneRallo = True
            if animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata":
                disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
            if animaOggetto[0] == "pozione" or animaOggetto[0] == "superPozione":
                if fineanimaz == 10:
                    GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.suonoUsoPozione)
                disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
                if fineanimaz > 5:
                    GlobalVarG2.schermo.blit(GlobalVarG2.imgAnimaPozione1, (x, y))
                else:
                    GlobalVarG2.schermo.blit(GlobalVarG2.imgAnimaPozione2, (x, y))
            elif animaOggetto[0] == "medicina":
                if fineanimaz == 10:
                    GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.suonoUsoMedicina)
                disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
                if fineanimaz > 5:
                    GlobalVarG2.schermo.blit(GlobalVarG2.imgAnimaMedicina1, (x, y))
                else:
                    GlobalVarG2.schermo.blit(GlobalVarG2.imgAnimaMedicina2, (x, y))
            elif animaOggetto[0] == "caricaBatterie" or animaOggetto[0] == "caricaBatterieMigliorato":
                if fineanimaz == 10:
                    GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.suonoUsoCaricabatterie)
                if ((vrx / GlobalVarG2.gpx) + (vry / GlobalVarG2.gpy)) % 2 == 0:
                    GlobalVarG2.schermo.blit(sfondinoa, (vrx, vry))
                if ((vrx / GlobalVarG2.gpx) + (vry / GlobalVarG2.gpy)) % 2 == 1:
                    GlobalVarG2.schermo.blit(sfondinob, (vrx, vry))
                GlobalVarG2.schermo.blit(armrobS, (vrx, vry))
                GlobalVarG2.schermo.blit(GlobalVarG2.robos, (vrx, vry))
                GlobalVarG2.schermo.blit(GlobalVarG2.imgAnimaCaricabatterie, (vrx, vry))
                disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
    return animazioneRallo


def animaDifesaRallo(x, y, armaS, armaturaS, arcoS, faretraS, collanaS, scudoDifesa, guantiDifesa, avvele, difesa, animazioneRallo, nemicoAttaccante, fineanimaz):
    if nemicoAttaccante and nemicoAttaccante.ralloParato and fineanimaz == 10:
        GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.rumoreParata)
    if fineanimaz != 0 and (difesa != 0 or (nemicoAttaccante and nemicoAttaccante.ralloParato)):
            animazioneRallo = True
            GlobalVarG2.schermo.blit(arcoS, (x, y))
            GlobalVarG2.schermo.blit(faretraS, (x, y))
            GlobalVarG2.schermo.blit(GlobalVarG2.perss, (x, y))
            if avvele:
                GlobalVarG2.schermo.blit(GlobalVarG2.persAvvele, (x, y))
            GlobalVarG2.schermo.blit(armaturaS, (x, y))
            GlobalVarG2.schermo.blit(collanaS, (x, y))
            GlobalVarG2.schermo.blit(GlobalVarG2.persmbDifesa, (x, y))
            GlobalVarG2.schermo.blit(armaS, (x, y))
            GlobalVarG2.schermo.blit(guantiDifesa, (x, y))
            GlobalVarG2.schermo.blit(scudoDifesa, (x, y))
    return animazioneRallo


def animaLvUp(x, y, npers, pers, arma, armatura, scudo, collana, arco, faretra, guanti, liv, aumentoliv, carim, caricaTutto, tastop, animazioneRallo, movimentoPerMouse, fineanimaz):
    if aumentoliv != 0 and not carim:
        liv -= aumentoliv
        animazioneRallo = True
        if fineanimaz == 10:
            GlobalVarG2.canaleSoundLvUp.play(GlobalVarG2.rumorelevelup)
        avvele = False
        disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
        if 5 <= fineanimaz <= 10:
            GlobalVarG2.schermo.blit(GlobalVarG2.saliliv2, (x, y))
        if 1 < fineanimaz <= 5:
            GlobalVarG2.schermo.blit(GlobalVarG2.saliliv1, (x, y))
        if fineanimaz == 1:
            GlobalVarG2.schermo.blit(GlobalVarG2.saliliv, (x, y))

        GlobalVarG2.schermo.blit(GlobalVarG2.sfocontcof, (GlobalVarG2.gsx // 32 * 0, GlobalVarG2.gsy // 18 * 0))
        i = 1
        while i <= 100:
            if liv == i:
                messaggio("Liv +: Attacco aumentato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
                break
            i += 3
        i = 2
        while i <= 100:
            if liv == i:
                messaggio("Liv +: Difesa aumentata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
                break
            i += 3
        i = 3
        while i <= 100:
            if liv == i:
                messaggio("Liv +: Punti vita aumentati", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
                break
            i += 3
        if fineanimaz == 1:
            if GlobalVarG2.mouseBloccato:
                GlobalVarG2.configuraCursore(False)
            pygame.display.update()
            pygame.time.wait(500)
            risposta = False
            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
            while not risposta:
                deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
                if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVarG2.mouseVisibile:
                    pygame.mouse.set_visible(True)
                    GlobalVarG2.mouseVisibile = True
                for event in pygame.event.get():
                    sinistroMouseVecchio = sinistroMouse
                    centraleMouseVecchio = centraleMouse
                    destroMouseVecchio = destroMouse
                    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
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
                    if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse):
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        risposta = True
                        aumentoliv -= 1
                    if event.type == pygame.KEYDOWN:
                        if GlobalVarG2.mouseVisibile:
                            pygame.mouse.set_visible(False)
                            GlobalVarG2.mouseVisibile = False

        caricaTutto = True
        movimentoPerMouse = False
        tastop = 0
    return animazioneRallo, caricaTutto, tastop, aumentoliv, movimentoPerMouse


def animaRalloFermo(x, y, vx, vy, npers, pers, scudo, armatura, arma, arco, faretra, guanti, collana, avvele, azioniDaEseguire, animazioneRalloFatta, nemicoAttaccante, difesa, fineanimaz):
    if (not "attaccoRallo" in azioniDaEseguire and not "movimentoRallo" in azioniDaEseguire and not (nemicoAttaccante and nemicoAttaccante.ralloParato) and difesa == 0) or fineanimaz == 0:
        if animazioneRalloFatta:
            disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
        else:
            disegnaRallo(npers, vx, vy, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)


def animaCamminataRobo(nrob, rx, ry, vrx, vry, armrob, surriscalda, cambiosta, animazioneColco, fineanimaz):
    if (rx != vrx or ry != vry) and not cambiosta:
        animazioneColco = True
        if nrob != 0 and fineanimaz == 10:
            GlobalVarG2.canaleSoundPassiColco.play(GlobalVarG2.rumoreCamminataColco)
        # nrob => 1=d, 2=a, 3=s, 4=w
        if nrob == 1:
            if 5 < fineanimaz <= 10:
                GlobalVarG2.schermo.blit(GlobalVarG2.robodp, (rx - (GlobalVarG2.gpx * fineanimaz // 10), ry))
                if surriscalda > 0:
                    GlobalVarG2.schermo.blit(GlobalVarG2.roboSurrisc, (rx - (GlobalVarG2.gpx * fineanimaz // 10), ry))
                GlobalVarG2.schermo.blit(armrob, (rx - (GlobalVarG2.gpx * fineanimaz // 10), ry))
            if 0 < fineanimaz <= 5:
                GlobalVarG2.schermo.blit(GlobalVarG2.robodp, (rx - (GlobalVarG2.gpx * fineanimaz // 10), ry))
                if surriscalda > 0:
                    GlobalVarG2.schermo.blit(GlobalVarG2.roboSurrisc, (rx - (GlobalVarG2.gpx * fineanimaz // 10), ry))
                GlobalVarG2.schermo.blit(armrob, (rx - (GlobalVarG2.gpx * fineanimaz // 10), ry))
        if nrob == 2:
            if 5 < fineanimaz <= 10:
                GlobalVarG2.schermo.blit(GlobalVarG2.roboap, (rx + (GlobalVarG2.gpx * fineanimaz // 10), ry))
                if surriscalda > 0:
                    GlobalVarG2.schermo.blit(GlobalVarG2.roboSurrisc, (rx + (GlobalVarG2.gpx * fineanimaz // 10), ry))
                GlobalVarG2.schermo.blit(armrob, (rx + (GlobalVarG2.gpx * fineanimaz // 10), ry))
            if 0 < fineanimaz <= 5:
                GlobalVarG2.schermo.blit(GlobalVarG2.roboap, (rx + (GlobalVarG2.gpx * fineanimaz // 10), ry))
                if surriscalda > 0:
                    GlobalVarG2.schermo.blit(GlobalVarG2.roboSurrisc, (rx + (GlobalVarG2.gpx * fineanimaz // 10), ry))
                GlobalVarG2.schermo.blit(armrob, (rx + (GlobalVarG2.gpx * fineanimaz // 10), ry))
        if nrob == 4:
            if 5 < fineanimaz <= 10:
                GlobalVarG2.schermo.blit(GlobalVarG2.robow, (rx, ry + (GlobalVarG2.gpy * fineanimaz // 10)))
                if surriscalda > 0:
                    GlobalVarG2.schermo.blit(GlobalVarG2.roboSurrisc, (rx, ry + (GlobalVarG2.gpy * fineanimaz // 10)))
                GlobalVarG2.schermo.blit(armrob, (rx, ry + (GlobalVarG2.gpy * fineanimaz // 10)))
            if 0 < fineanimaz <= 5:
                GlobalVarG2.schermo.blit(GlobalVarG2.robow, (rx, ry + (GlobalVarG2.gpy * fineanimaz // 10)))
                if surriscalda > 0:
                    GlobalVarG2.schermo.blit(GlobalVarG2.roboSurrisc, (rx, ry + (GlobalVarG2.gpy * fineanimaz // 10)))
                GlobalVarG2.schermo.blit(armrob, (rx, ry + (GlobalVarG2.gpy * fineanimaz // 10)))
        if nrob == 3:
            if 5 < fineanimaz <= 10:
                GlobalVarG2.schermo.blit(GlobalVarG2.robos, (rx, ry - (GlobalVarG2.gpy * fineanimaz // 10)))
                if surriscalda > 0:
                    GlobalVarG2.schermo.blit(GlobalVarG2.roboSurrisc, (rx, ry - (GlobalVarG2.gpy * fineanimaz // 10)))
                GlobalVarG2.schermo.blit(armrob, (rx, ry - (GlobalVarG2.gpy * fineanimaz // 10)))
            if 0 < fineanimaz <= 5:
                GlobalVarG2.schermo.blit(GlobalVarG2.robos, (rx, ry - (GlobalVarG2.gpy * fineanimaz // 10)))
                if surriscalda > 0:
                    GlobalVarG2.schermo.blit(GlobalVarG2.roboSurrisc, (rx, ry - (GlobalVarG2.gpy * fineanimaz // 10)))
                GlobalVarG2.schermo.blit(armrob, (rx, ry - (GlobalVarG2.gpy * fineanimaz // 10)))
    return animazioneColco


def animaTecnicaColco(rx, ry, nrob, robot, armrob, armrobS, tecnicaUsata, cambiosta, animazioneColco, fineanimaz):
    if not cambiosta and fineanimaz != 0:
        animazioneColco = True

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
        while i < len(GlobalVarG2.vetAnimazioniTecniche):
            if GlobalVarG2.vetAnimazioniTecniche[i] == tecnicaUsata:
                if tecnicaUsata.startswith("scossa") or tecnicaUsata.startswith("freccia") or tecnicaUsata.startswith("cura") or tecnicaUsata == "antidoto" or tecnicaUsata == "attP" or tecnicaUsata == "difP":
                    imgAnimazione1w = GlobalVarG2.vetAnimazioniTecniche[i + 1][0]
                    imgAnimazione2w = GlobalVarG2.vetAnimazioniTecniche[i + 1][1]
                    imgAnimazione1a = GlobalVarG2.vetAnimazioniTecniche[i + 1][2]
                    imgAnimazione2a = GlobalVarG2.vetAnimazioniTecniche[i + 1][3]
                    imgAnimazione1s = GlobalVarG2.vetAnimazioniTecniche[i + 1][4]
                    imgAnimazione2s = GlobalVarG2.vetAnimazioniTecniche[i + 1][5]
                    imgAnimazione1d = GlobalVarG2.vetAnimazioniTecniche[i + 1][6]
                    imgAnimazione2d = GlobalVarG2.vetAnimazioniTecniche[i + 1][7]
                elif tecnicaUsata.startswith("tempesta"):
                    imgAnimazione1 = GlobalVarG2.vetAnimazioniTecniche[i + 1][0]
                    imgAnimazione2 = GlobalVarG2.vetAnimazioniTecniche[i + 1][1]
                else:
                    imgAnimazione = GlobalVarG2.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2

        if fineanimaz == 10:
            if tecnicaUsata.startswith("scossa") or tecnicaUsata.startswith("freccia"):
                GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.rumoreScossaFreccia)
            elif tecnicaUsata.startswith("tempesta"):
                GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.rumoreTempestaElettrica)
            elif tecnicaUsata.startswith("cura"):
                GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.rumoreCuraRobo)
            elif tecnicaUsata == "antidoto":
                GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.rumoreAntidoto)
            elif tecnicaUsata == "attP" or tecnicaUsata == "difP":
                GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.rumoreAttPDifP)
            elif tecnicaUsata.startswith("ricarica"):
                GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.rumoreAutoricarica)
            elif tecnicaUsata == "raffred":
                GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.rumoreRaffreddamento)
            elif tecnicaUsata == "velocizza" or tecnicaUsata == "efficienza":
                GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.rumoreVelocizzaEfficienza)

        if tecnicaUsata.startswith("scossa") or tecnicaUsata.startswith("freccia") or tecnicaUsata.startswith("cura") or tecnicaUsata == "antidoto" or tecnicaUsata == "attP" or tecnicaUsata == "difP":
            GlobalVarG2.schermo.blit(robot, (rx, ry))
            GlobalVarG2.schermo.blit(armrob, (rx, ry))
            # nrob => 1=d, 2=a, 3=s, 4=w
            if 7 < fineanimaz <= 10:
                if nrob == 1:
                    GlobalVarG2.schermo.blit(imgAnimazione1d, (rx, ry))
                if nrob == 2:
                    GlobalVarG2.schermo.blit(imgAnimazione1a, (rx - GlobalVarG2.gpx, ry))
                if nrob == 3:
                    GlobalVarG2.schermo.blit(imgAnimazione1s, (rx, ry))
                if nrob == 4:
                    GlobalVarG2.schermo.blit(imgAnimazione1w, (rx, ry - GlobalVarG2.gpy))
            if 0 < fineanimaz <= 7:
                if nrob == 1:
                    GlobalVarG2.schermo.blit(imgAnimazione2d, (rx, ry))
                if nrob == 2:
                    GlobalVarG2.schermo.blit(imgAnimazione2a, (rx - GlobalVarG2.gpx, ry))
                if nrob == 3:
                    GlobalVarG2.schermo.blit(imgAnimazione2s, (rx, ry))
                if nrob == 4:
                    GlobalVarG2.schermo.blit(imgAnimazione2w, (rx, ry - GlobalVarG2.gpy))
        if tecnicaUsata.startswith("ricarica") or tecnicaUsata == "raffred" or tecnicaUsata == "velocizza" or tecnicaUsata == "efficienza":
            if tecnicaUsata.startswith("ricarica"):
                GlobalVarG2.schermo.blit(GlobalVarG2.robomo, (rx, ry))
            else:
                GlobalVarG2.schermo.blit(armrobS, (rx, ry))
                GlobalVarG2.schermo.blit(GlobalVarG2.robos, (rx, ry))
            GlobalVarG2.schermo.blit(imgAnimazione, (rx, ry))
        if tecnicaUsata.startswith("tempesta"):
            GlobalVarG2.schermo.blit(robot, (rx, ry))
            GlobalVarG2.schermo.blit(armrob, (rx, ry))
            if 7 < fineanimaz <= 10:
                GlobalVarG2.schermo.blit(imgAnimazione1, (rx - (GlobalVarG2.gpx * 8), ry - (GlobalVarG2.gpx * 8)))
            if 0 < fineanimaz <= 7:
                GlobalVarG2.schermo.blit(imgAnimazione2, (rx - (GlobalVarG2.gpx * 8), ry - (GlobalVarG2.gpx * 8)))

    return animazioneColco


def animaDanneggiamentoColco(rx, ry, nemicoAttaccante, cambiosta, fineanimaz):
    if nemicoAttaccante.bersaglioColpito[0] == "Colco" and not cambiosta and fineanimaz != 0:
        GlobalVarG2.schermo.blit(GlobalVarG2.imgDanneggiamentoColco, (rx, ry))


def animaColcoFermo(rx, ry, vrx, vry, robot, armrob, armrobS, surriscalda, tecnicaUsata, azioniDaEseguire, animazioneColcoFatta, raffreddamento, ricarica1, ricarica2, raffredda, autoRic1, autoRic2, fineanimaz):
    if (not ("attaccoColco" in azioniDaEseguire and tecnicaUsata != "spostamento") and not ("movimentoColcoNemiciPersonaggi" in azioniDaEseguire and tecnicaUsata == "spostamento")) or fineanimaz == 0:
        if animazioneColcoFatta:
            x = rx
            y = ry
        else:
            x = vrx
            y = vry
        if (raffreddamento and animazioneColcoFatta) or (raffredda >= 0 and not raffreddamento):
            GlobalVarG2.schermo.blit(armrobS, (x, y))
            GlobalVarG2.schermo.blit(GlobalVarG2.robos, (x, y))
            imgAnimazione = 0
            i = 0
            while i < len(GlobalVarG2.vetAnimazioniTecniche):
                if GlobalVarG2.vetAnimazioniTecniche[i] == "raffred":
                    imgAnimazione = GlobalVarG2.vetAnimazioniTecniche[i + 1][0]
                    break
                i += 2
            GlobalVarG2.schermo.blit(imgAnimazione, (x, y))
        elif (ricarica1 and animazioneColcoFatta) or (autoRic1 >= 0 and not ricarica1):
            GlobalVarG2.schermo.blit(GlobalVarG2.robomo, (x, y))
            imgAnimazione = 0
            i = 0
            while i < len(GlobalVarG2.vetAnimazioniTecniche):
                if GlobalVarG2.vetAnimazioniTecniche[i] == "ricarica":
                    imgAnimazione = GlobalVarG2.vetAnimazioniTecniche[i + 1][0]
                    break
                i += 2
            GlobalVarG2.schermo.blit(imgAnimazione, (x, y))
        elif (ricarica2 and animazioneColcoFatta) or (autoRic2 >= 0 and not ricarica2):
            GlobalVarG2.schermo.blit(GlobalVarG2.robomo, (x, y))
            imgAnimazione = 0
            i = 0
            while i < len(GlobalVarG2.vetAnimazioniTecniche):
                if GlobalVarG2.vetAnimazioniTecniche[i] == "ricarica+":
                    imgAnimazione = GlobalVarG2.vetAnimazioniTecniche[i + 1][0]
                    break
                i += 2
            GlobalVarG2.schermo.blit(imgAnimazione, (x, y))
        else:
            GlobalVarG2.schermo.blit(robot, (x, y))
            if surriscalda > 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.roboSurrisc, (x, y))
            GlobalVarG2.schermo.blit(armrob, (x, y))


def animaSpostamentoNemici(listaNemici, animazioneNemici, cambiosta, fineanimaz):
    if not cambiosta:
        for nemico in listaNemici:
            if nemico.animaSpostamento and not nemico.morto and (nemico.x != nemico.vx or nemico.y != nemico.vy):
                nemico.animazioneFatta = True
                animazioneNemici = True
                # rumorecamminataNemico.play()
                if nemico.direzione == "d":
                    if 5 < fineanimaz <= 10:
                        GlobalVarG2.schermo.blit(nemico.imgDMov1, (nemico.x - (GlobalVarG2.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[2]:
                            GlobalVarG2.schermo.blit(nemico.imgAppiccicato, (nemico.x - (GlobalVarG2.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[1]:
                            GlobalVarG2.schermo.blit(nemico.imgAvvelenamento, (nemico.x - (GlobalVarG2.gpx * fineanimaz // 10), nemico.y))
                    if 0 < fineanimaz <= 5:
                        GlobalVarG2.schermo.blit(nemico.imgDMov2, (nemico.x - (GlobalVarG2.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[2]:
                            GlobalVarG2.schermo.blit(nemico.imgAppiccicato, (nemico.x - (GlobalVarG2.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[1]:
                            GlobalVarG2.schermo.blit(nemico.imgAvvelenamento, (nemico.x - (GlobalVarG2.gpx * fineanimaz // 10), nemico.y))
                if nemico.direzione == "a":
                    if 5 < fineanimaz <= 10:
                        GlobalVarG2.schermo.blit(nemico.imgAMov1, (nemico.x + (GlobalVarG2.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[2]:
                            GlobalVarG2.schermo.blit(nemico.imgAppiccicato, (nemico.x + (GlobalVarG2.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[1]:
                            GlobalVarG2.schermo.blit(nemico.imgAvvelenamento, (nemico.x + (GlobalVarG2.gpx * fineanimaz // 10), nemico.y))
                    if 0 < fineanimaz <= 5:
                        GlobalVarG2.schermo.blit(nemico.imgAMov2, (nemico.x + (GlobalVarG2.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[2]:
                            GlobalVarG2.schermo.blit(nemico.imgAppiccicato, (nemico.x + (GlobalVarG2.gpx * fineanimaz // 10), nemico.y))
                        if nemico.statoInizioTurno[1]:
                            GlobalVarG2.schermo.blit(nemico.imgAvvelenamento, (nemico.x + (GlobalVarG2.gpx * fineanimaz // 10), nemico.y))
                if nemico.direzione == "w":
                    if 5 < fineanimaz <= 10:
                        GlobalVarG2.schermo.blit(nemico.imgWMov1, (nemico.x, nemico.y + (GlobalVarG2.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[2]:
                            GlobalVarG2.schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y + (GlobalVarG2.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[1]:
                            GlobalVarG2.schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y + (GlobalVarG2.gpy * fineanimaz // 10)))
                    if 0 < fineanimaz <= 5:
                        GlobalVarG2.schermo.blit(nemico.imgWMov2, (nemico.x, nemico.y + (GlobalVarG2.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[2]:
                            GlobalVarG2.schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y + (GlobalVarG2.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[1]:
                            GlobalVarG2.schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y + (GlobalVarG2.gpy * fineanimaz // 10)))
                if nemico.direzione == "s":
                    if 5 < fineanimaz <= 10:
                        GlobalVarG2.schermo.blit(nemico.imgSMov1, (nemico.x, nemico.y - (GlobalVarG2.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[2]:
                            GlobalVarG2.schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y - (GlobalVarG2.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[1]:
                            GlobalVarG2.schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y - (GlobalVarG2.gpy * fineanimaz // 10)))
                    if 0 < fineanimaz <= 5:
                        GlobalVarG2.schermo.blit(nemico.imgSMov2, (nemico.x, nemico.y - (GlobalVarG2.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[2]:
                            GlobalVarG2.schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y - (GlobalVarG2.gpy * fineanimaz // 10)))
                        if nemico.statoInizioTurno[1]:
                            GlobalVarG2.schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y - (GlobalVarG2.gpy * fineanimaz // 10)))
    return animazioneNemici


def animaAttaccoNemici(nemicoAttaccante, animazioneNemici, fineanimaz):
    if nemicoAttaccante and fineanimaz != 0:
        if nemicoAttaccante.animaAttacco and not nemicoAttaccante.animazioneFatta:
            if fineanimaz == 1:
                nemicoAttaccante.animazioneFatta = True
            animazioneNemici = True
            # if fineanimaz == 10 and not GlobalVarG2.canaleSoundAttacco.get_busy():
            #     GlobalVarG2.canaleSoundAttacco.play(rumoreattacco)
            if nemicoAttaccante.direzione == "w":
                GlobalVarG2.schermo.blit(nemicoAttaccante.imgAttaccoW, (nemicoAttaccante.x, nemicoAttaccante.y - GlobalVarG2.gpy))
            if nemicoAttaccante.direzione == "a":
                GlobalVarG2.schermo.blit(nemicoAttaccante.imgAttaccoA, (nemicoAttaccante.x - GlobalVarG2.gpx, nemicoAttaccante.y))
            if nemicoAttaccante.direzione == "s":
                GlobalVarG2.schermo.blit(nemicoAttaccante.imgAttaccoS, (nemicoAttaccante.x, nemicoAttaccante.y))
            if nemicoAttaccante.direzione == "d":
                GlobalVarG2.schermo.blit(nemicoAttaccante.imgAttaccoD, (nemicoAttaccante.x, nemicoAttaccante.y))
            if nemicoAttaccante.statoInizioTurno[2]:
                GlobalVarG2.schermo.blit(nemicoAttaccante.imgAppiccicato, (nemicoAttaccante.x, nemicoAttaccante.y))
            if nemicoAttaccante.statoInizioTurno[1]:
                GlobalVarG2.schermo.blit(nemicoAttaccante.imgAvvelenamento, (nemicoAttaccante.x, nemicoAttaccante.y))
    return animazioneNemici


def animaMorteNemici(listaNemici, animazioneNemici, cambiosta, fineanimaz):
    if not cambiosta:
        for nemico in listaNemici:
            if nemico.animaMorte:
                nemico.animazioneFatta = True
                animazioneNemici = True
                if fineanimaz > 0 and (fineanimaz % 4 == 0):
                    GlobalVarG2.schermo.blit(nemico.imgAttuale, (nemico.x, nemico.y))
                    if nemico.statoInizioTurno[2]:
                        GlobalVarG2.schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y))
                    if nemico.statoInizioTurno[1]:
                        GlobalVarG2.schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y))
    return animazioneNemici


def animaDanneggiamentoNemici(listaNemici, animazioneNemici, cambiosta, azioniDaEseguire, attaccante):
    if not cambiosta:
        for nemico in listaNemici:
            if (nemico.animaDanneggiamento == "Rallo" and "attaccoRallo" in azioniDaEseguire) or (nemico.animaDanneggiamento == "Colco" and "attaccoColco" in azioniDaEseguire):
                animazioneNemici = True
                if attaccante == "Rallo":
                    GlobalVarG2.schermo.blit(nemico.imgDanneggiamentoRallo, (nemico.vx, nemico.vy))
                if attaccante == "Colco":
                    GlobalVarG2.schermo.blit(nemico.imgDanneggiamentoColco, (nemico.vx, nemico.vy))
                if nemico.statoInizioTurno[2]:
                    GlobalVarG2.schermo.blit(nemico.imgAppiccicato, (nemico.vx, nemico.vy))
                if nemico.statoInizioTurno[1]:
                    GlobalVarG2.schermo.blit(nemico.imgAvvelenamento, (nemico.vx, nemico.vy))
    return animazioneNemici


def animaNemiciFermi(listaNemici, azioniDaEseguire, cambiosta, nemicoAttaccante, fineanimaz):
    if not cambiosta:
        for nemico in listaNemici:
            if nemico.inCasellaVista and not (("movimentoColcoNemiciPersonaggi" in azioniDaEseguire and (nemico.animaSpostamento or nemico.animaMorte)) or ("attaccoNemici" in azioniDaEseguire and nemico.animaAttacco and nemicoAttaccante == nemico)) and not (nemico.animaMorte and nemico.animazioneFatta) or (nemico.inCasellaVista and fineanimaz == 0 and not nemico.animaMorte):
                if nemico.animazioneFatta:
                    GlobalVarG2.schermo.blit(nemico.imgAttuale, (nemico.x, nemico.y))
                    if nemico.statoInizioTurno[2]:
                        GlobalVarG2.schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y))
                    if nemico.statoInizioTurno[1]:
                        GlobalVarG2.schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y))
                else:
                    GlobalVarG2.schermo.blit(nemico.imgAttuale, (nemico.vx, nemico.vy))
                    if nemico.statoInizioTurno[2]:
                        GlobalVarG2.schermo.blit(nemico.imgAppiccicato, (nemico.vx, nemico.vy))
                    if nemico.statoInizioTurno[1]:
                        GlobalVarG2.schermo.blit(nemico.imgAvvelenamento, (nemico.vx, nemico.vy))


def animaEsche(vitaesca, eschePrimaDelTurno, caseviste, sfondinoa, sfondinob, azioniDaEseguire, animaOggetto):
    if not "attaccoRallo" in azioniDaEseguire and animaOggetto[0] == "esca":
        if ((animaOggetto[1] / GlobalVarG2.gpx) + (animaOggetto[2] / GlobalVarG2.gpy)) % 2 == 0:
            GlobalVarG2.schermo.blit(sfondinoa, (animaOggetto[1], animaOggetto[2]))
        if ((animaOggetto[1] / GlobalVarG2.gpx) + (animaOggetto[2] / GlobalVarG2.gpy)) % 2 == 1:
            GlobalVarG2.schermo.blit(sfondinob, (animaOggetto[1], animaOggetto[2]))
        GlobalVarG2.schermo.blit(GlobalVarG2.vetIcoOggettiMenu[7], (animaOggetto[1], animaOggetto[2]))
    i = 0
    while i < len(vitaesca):
        j = 0
        while j < len(caseviste):
            if caseviste[j] == vitaesca[i + 2] and caseviste[j + 1] == vitaesca[i + 3] and caseviste[j + 2]:
                k = 0
                while k < len(eschePrimaDelTurno):
                    if eschePrimaDelTurno[k] == vitaesca[i]:
                        if ((vitaesca[i + 2] / GlobalVarG2.gpx) + (vitaesca[i + 3] / GlobalVarG2.gpy)) % 2 == 0:
                            GlobalVarG2.schermo.blit(sfondinoa, (vitaesca[i + 2], vitaesca[i + 3]))
                        if ((vitaesca[i + 2] / GlobalVarG2.gpx) + (vitaesca[i + 3] / GlobalVarG2.gpy)) % 2 == 1:
                            GlobalVarG2.schermo.blit(sfondinob, (vitaesca[i + 2], vitaesca[i + 3]))
                        GlobalVarG2.schermo.blit(GlobalVarG2.esche, (vitaesca[i + 2], vitaesca[i + 3]))
                        break
                    k += 2
                break
            j += 3
        i += 4


def animaDenaro(vettoreDenaro, caseviste, sfondinoa, sfondinob):
    i = 0
    while i < len(vettoreDenaro):
        j = 0
        while j < len(caseviste):
            if ((caseviste[j] == vettoreDenaro[i + 1] - GlobalVarG2.gpx and caseviste[j + 1] == vettoreDenaro[i + 2]) or (caseviste[j] == vettoreDenaro[i + 1] + GlobalVarG2.gpx and caseviste[j + 1] == vettoreDenaro[i + 2]) or (caseviste[j] == vettoreDenaro[i + 1] and caseviste[j + 1] == vettoreDenaro[i + 2] - GlobalVarG2.gpy) or (caseviste[j] == vettoreDenaro[i + 1] and caseviste[j + 1] == vettoreDenaro[i + 2] + GlobalVarG2.gpy)) and caseviste[j + 2]:
                if ((vettoreDenaro[i + 1] / GlobalVarG2.gpx) + (vettoreDenaro[i + 2] / GlobalVarG2.gpy)) % 2 == 0:
                    GlobalVarG2.schermo.blit(sfondinoa, (vettoreDenaro[i + 1], vettoreDenaro[i + 2]))
                if ((vettoreDenaro[i + 1] / GlobalVarG2.gpx) + (vettoreDenaro[i + 2] / GlobalVarG2.gpy)) % 2 == 1:
                    GlobalVarG2.schermo.blit(sfondinob, (vettoreDenaro[i + 1], vettoreDenaro[i + 2]))
                GlobalVarG2.schermo.blit(GlobalVarG2.sacchettoDenaro, (vettoreDenaro[i + 1], vettoreDenaro[i + 2]))
                break
            j += 3
        i += 3


def animaCofanetti(cofanetti, caseviste, sfondinoc):
    # cofanetti[stanza, x, y, True / False, ...]
    i = 0
    while i < len(cofanetti):
        j = 0
        while j < len(caseviste):
            if ((caseviste[j] == cofanetti[i + 1] - GlobalVarG2.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] + GlobalVarG2.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - GlobalVarG2.gpy) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + GlobalVarG2.gpy)) and caseviste[j + 2]:
                GlobalVarG2.schermo.blit(sfondinoc, (cofanetti[i + 1], cofanetti[i + 2]))
                if cofanetti[i + 3]:
                    GlobalVarG2.schermo.blit(GlobalVarG2.cofaniaper, (cofanetti[i + 1], cofanetti[i + 2]))
                else:
                    GlobalVarG2.schermo.blit(GlobalVarG2.cofanichiu, (cofanetti[i + 1], cofanetti[i + 2]))
                break
            j += 3
        i += 4


def animaPorte(porte, cofanetti, numStanza, portaOriz, portaVert, sfondinoc):
    # porte[stanza, x, y, True / False, ...]
    i = 0
    while i < len(porte):
        if not porte[i + 3]:
            vmurx = porte[i + 1]
            vmury = porte[i + 2]
            murx, mury, inutile, inutile, inutile = muri_porte(vmurx, vmury, GlobalVarG2.gpx, 0, numStanza, False, False, False, porte, cofanetti)
            GlobalVarG2.schermo.blit(sfondinoc, (porte[i + 1], porte[i + 2]))
            if vmurx == murx and vmury == mury:
                GlobalVarG2.schermo.blit(portaOriz, (porte[i + 1], porte[i + 2]))
            else:
                GlobalVarG2.schermo.blit(portaVert, (porte[i + 1], porte[i + 2]))
        i = i + 4


def animaAperturaCofanetto(tesoro, x, y, npers, pers, avvele, armatura, arma, scudo, collana, arco, faretra, guanti, sfondinoc, animazioneRallo):
    if tesoro != -1:
        animazioneRallo = True
        disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
        if npers == 1:
            GlobalVarG2.schermo.blit(sfondinoc, (x + GlobalVarG2.gpx, y))
            GlobalVarG2.schermo.blit(GlobalVarG2.cofaniaper, (x + GlobalVarG2.gpx, y))
        if npers == 2:
            GlobalVarG2.schermo.blit(sfondinoc, (x - GlobalVarG2.gpx, y))
            GlobalVarG2.schermo.blit(GlobalVarG2.cofaniaper, (x - GlobalVarG2.gpx, y))
        if npers == 3:
            GlobalVarG2.schermo.blit(sfondinoc, (x, y - GlobalVarG2.gpy))
            GlobalVarG2.schermo.blit(GlobalVarG2.cofaniaper, (x, y - GlobalVarG2.gpy))
        if npers == 4:
            GlobalVarG2.schermo.blit(sfondinoc, (x, y + GlobalVarG2.gpy))
            GlobalVarG2.schermo.blit(GlobalVarG2.cofaniaper, (x, y + GlobalVarG2.gpy))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfocontcof, (GlobalVarG2.gsx // 32 * 0, GlobalVarG2.gsy // 18 * 0))
        if tesoro == -2:
            messaggio("Hai trovato: Niente", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        # 31-40 -> oggetti(10) / 41-70 -> armi(30) / 71-75 -> batterie(5) / 81-100 -> condizioni(20) / 101-120 -> gambit (=celle di memoria)(20) / 131 -> monete / 132 frecce
        if tesoro >= 11 and tesoro <= 30:
            messaggio("Hai trovato: Una nuova tecnica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 31:
            messaggio("Hai trovato: Pozione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 32:
            messaggio("Hai trovato: Alimentazione 100gr", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 33:
            messaggio("Hai trovato: Medicina", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 34:
            messaggio("Hai trovato: Superpozione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 35:
            messaggio("Hai trovato: Alimentazione 250gr", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 36:
            messaggio("Hai trovato: Bomba", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 37:
            messaggio("Hai trovato: Bomba velenosa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 38:
            messaggio("Hai trovato: Esca", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 39:
            messaggio("Hai trovato: Bomba appiccicosa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 40:
            messaggio("Hai trovato: Bomba potenziata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 41:
            messaggio("Hai trovato: Niente", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 42:
            messaggio("Hai trovato: Spada di ferro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 43:
            messaggio("Hai trovato: Spadone d'acciaio", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 44:
            messaggio("Hai trovato: Lykother", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 45:
            messaggio("Hai trovato: Mendaxritas", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 46:
            messaggio("Hai trovato: Niente", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 47:
            messaggio("Hai trovato: Arco di legno", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 48:
            messaggio("Hai trovato: Arco di ferro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 49:
            messaggio("Hai trovato: Arco di precisione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 50:
            messaggio("Hai trovato: Accipiter", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 51:
            messaggio("Hai trovato: Niente", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 52:
            messaggio("Hai trovato: Armatura di pelle", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 53:
            messaggio("Hai trovato: Armatura d'acciaio", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 54:
            messaggio("Hai trovato: Lykodes", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 55:
            messaggio("Hai trovato: Loriquam", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 56:
            messaggio("Hai trovato: Niente", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 57:
            messaggio("Hai trovato: Scudo di pelle", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 58:
            messaggio("Hai trovato: Scudo d'acciaio", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 59:
            messaggio("Hai trovato: Lykethmos", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 60:
            messaggio("Hai trovato: Clipequam", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 61:
            messaggio("Hai trovato: Niente", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 62:
            messaggio("Hai trovato: Guanti vitali", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 63:
            messaggio("Hai trovato: Guanti difensivi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 64:
            messaggio("Hai trovato: Guanti offensivi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 65:
            messaggio("Hai trovato: Guanti confortevoli", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 66:
            messaggio("Hai trovato: Niente", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 67:
            messaggio("Hai trovato: Collana medicinale", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 68:
            messaggio("Hai trovato: Collana rigenerante", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 69:
            messaggio("Hai trovato: Apprendimaschera", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 70:
            messaggio("Hai trovato: Portafortuna", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 71:
            messaggio("Hai trovato: Batteria piccola", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 72:
            messaggio("Hai trovato: Batteria discreta", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 73:
            messaggio("Hai trovato: Batteria capiente", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 74:
            messaggio("Hai trovato: Batteria enorme", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 75:
            messaggio("Hai trovato: Batteria illimitata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro >= 81 and tesoro <= 100:
            messaggio("Hai trovato: Una nuova condizione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro >= 101 and tesoro <= 120:
            messaggio("Hai trovato: Cella di memoria", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 131:
            messaggio("Hai trovato: 50 monete", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
        if tesoro == 132:
            messaggio("Hai trovato: 5 frecce", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)

    return animazioneRallo


def animaRaccoltaDenaro(x, y, vettoreDenaro, collana, fineanimaz):
    denaroRaccolto = False
    i = 0
    while i < len(vettoreDenaro):
        if vettoreDenaro[i + 1] == x and vettoreDenaro[i + 2] == y:
            if fineanimaz == 1:
                GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.suonoRaccoltaMonete)
            if GlobalVarG2.canaleSoundPassiRallo.get_busy():
                GlobalVarG2.canaleSoundPassiRallo.stop()
            denaroTrovato = vettoreDenaro[i]
            # effetto portafortuna
            if collana == 4:
                denaroTrovato += vettoreDenaro[i]
            GlobalVarG2.schermo.blit(GlobalVarG2.sfocontcof, (GlobalVarG2.gsx // 32 * 0, GlobalVarG2.gsy // 18 * 0))
            messaggio("Denaro trovato: " + str(denaroTrovato), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 1, 60)
            denaroRaccolto = True
            break
        i += 3
    return denaroRaccolto


def eliminaOggettoLanciato(x, y, attaccoADistanza, animaOggetto, rx, ry, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoAttaccante, schermo_prima_delle_animazioni, cambiosta, azioniDaEseguire, fineanimaz):
    # disegno il terreno sotto le frecce lanciate da Rallo
    if "attaccoRallo" in azioniDaEseguire and (attaccoADistanza or animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata") and not cambiosta:
        xInizioRetta = x
        yInizioRetta = y
        if animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata":
            xFineRetta = animaOggetto[1]
            yFineRetta = animaOggetto[2]
        else:
            xFineRetta = attaccoADistanza.vx
            yFineRetta = attaccoADistanza.vy
        global quadrettoSottoLaFreccia
        global quadrettoSottoEsplosione
        if fineanimaz > 5:
            if fineanimaz == 10 and (animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata"):
                quadrettoSottoEsplosione = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xFineRetta - (GlobalVarG2.gpx * 2), yFineRetta - (GlobalVarG2.gpy * 2), GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
            if fineanimaz != 10:
                GlobalVarG2.schermo.blit(quadrettoSottoLaFreccia, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz) - GlobalVarG2.gpx), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVarG2.gpy))
            quadrettoSottoLaFreccia = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)) - GlobalVarG2.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz)) - GlobalVarG2.gpy, GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
        elif fineanimaz == 5:
            GlobalVarG2.schermo.blit(quadrettoSottoLaFreccia, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVarG2.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVarG2.gpy))
        elif fineanimaz == 0 and (animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata"):
            GlobalVarG2.schermo.blit(quadrettoSottoEsplosione, ((xFineRetta - (GlobalVarG2.gpx * 2), yFineRetta - (GlobalVarG2.gpy * 2))))

    # disegno il terreno sotto le frecce elettriche lanciate da Colco
    if "attaccoColco" in azioniDaEseguire and listaNemiciAttaccatiADistanzaRobo and len(listaNemiciAttaccatiADistanzaRobo) == 1 and tecnicaUsata.startswith("freccia") and not cambiosta:
        xInizioRetta = rx
        xFineRetta = listaNemiciAttaccatiADistanzaRobo[0].vx
        yInizioRetta = ry
        yFineRetta = listaNemiciAttaccatiADistanzaRobo[0].vy
        global quadrettoSottoLaFrecciaElettrica
        if fineanimaz > 5:
            if fineanimaz != 10:
                GlobalVarG2.schermo.blit(quadrettoSottoLaFrecciaElettrica, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz) - GlobalVarG2.gpx), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVarG2.gpy))
            quadrettoSottoLaFrecciaElettrica = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)) - GlobalVarG2.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz)) - GlobalVarG2.gpy, GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
        elif fineanimaz == 5:
            GlobalVarG2.schermo.blit(quadrettoSottoLaFrecciaElettrica, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVarG2.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVarG2.gpy))

    # disegno il terreno sotto gli oggetti lanciati dai nemici
    if "attaccoNemici" in azioniDaEseguire and nemicoAttaccante:
        if nemicoAttaccante.attaccaDaLontano and nemicoAttaccante.animaAttacco and not nemicoAttaccante.morto:
            xInizioRetta = nemicoAttaccante.x
            xFineRetta = nemicoAttaccante.xObbiettivo
            yInizioRetta = nemicoAttaccante.y
            yFineRetta = nemicoAttaccante.yObbiettivo
            if fineanimaz > 5:
                if fineanimaz != 10:
                    GlobalVarG2.schermo.blit(nemicoAttaccante.quadrettoSottoOggettoLanciato, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz) - GlobalVarG2.gpx), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVarG2.gpy))
                nemicoAttaccante.quadrettoSottoOggettoLanciato = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)) - GlobalVarG2.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz)) - GlobalVarG2.gpy, GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
            elif fineanimaz == 5:
                GlobalVarG2.schermo.blit(nemicoAttaccante.quadrettoSottoOggettoLanciato, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVarG2.gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - GlobalVarG2.gpy))


def disegnaCasellaAccantoAlPersCheAttacca(x, y, attacco, npers, rx, ry, nrob, tecnicaUsata, nemicoAttaccante, schermo_prima_delle_animazioni, cambiosta, azioniDaEseguire, fineanimaz):
    if "attaccoRallo" in azioniDaEseguire and attacco == 1:
        global quadrettoSottoLaSpada
        xAttaccoPers = 0
        yAttaccoPers = 0
        # 1=d, 2=a, 3=w, 4=s
        if npers == 1:
            xAttaccoPers = x + GlobalVarG2.gpx
            yAttaccoPers = y
        if npers == 2:
            xAttaccoPers = x - GlobalVarG2.gpx
            yAttaccoPers = y
        if npers == 3:
            xAttaccoPers = x
            yAttaccoPers = y - GlobalVarG2.gpy
        if npers == 4:
            xAttaccoPers = x
            yAttaccoPers = y + GlobalVarG2.gpy
        if fineanimaz == 10:
            quadrettoSottoLaSpada = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xAttaccoPers, yAttaccoPers, GlobalVarG2.gpx, GlobalVarG2.gpy))
        else:
            GlobalVarG2.schermo.blit(quadrettoSottoLaSpada, (xAttaccoPers, yAttaccoPers))

    if "attaccoColco" in azioniDaEseguire:
        global quadrettoSottoAttaccoColco
        if tecnicaUsata.startswith("scossa") or tecnicaUsata.startswith("freccia") or tecnicaUsata.startswith("cura") or tecnicaUsata == "antidoto" or tecnicaUsata == "attP" or tecnicaUsata == "difP":
            xAttaccoPers = 0
            yAttaccoPers = 0
            # nrob => 1=d, 2=a, 3=s, 4=w
            if nrob == 1:
                xAttaccoPers = rx + GlobalVarG2.gpx
                yAttaccoPers = ry
            if nrob == 2:
                xAttaccoPers = rx - GlobalVarG2.gpx
                yAttaccoPers = ry
            if nrob == 3:
                xAttaccoPers = rx
                yAttaccoPers = ry + GlobalVarG2.gpy
            if nrob == 4:
                xAttaccoPers = rx
                yAttaccoPers = ry - GlobalVarG2.gpy
            if fineanimaz == 10:
                quadrettoSottoAttaccoColco = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xAttaccoPers, yAttaccoPers, GlobalVarG2.gpx, GlobalVarG2.gpy))
            else:
                GlobalVarG2.schermo.blit(quadrettoSottoAttaccoColco, (xAttaccoPers, yAttaccoPers))
        elif tecnicaUsata.startswith("tempesta"):
            xAttaccoPers = rx - (GlobalVarG2.gpx * 8)
            yAttaccoPers = ry - (GlobalVarG2.gpy * 8)
            xFineAttaccoPers = GlobalVarG2.gpx * 8
            yFineAttaccoPers = GlobalVarG2.gpy * 8
            if xAttaccoPers < 0:
                xAttaccoPers = 0
            if yAttaccoPers < 0:
                yAttaccoPers = 0
            if rx + xFineAttaccoPers >= GlobalVarG2.gsx:
                xFineAttaccoPers = GlobalVarG2.gsx - rx - GlobalVarG2.gpx
            if ry + yFineAttaccoPers >= GlobalVarG2.gsy:
                yFineAttaccoPers = GlobalVarG2.gsy - ry - GlobalVarG2.gpy
            if fineanimaz == 10:
                quadrettoSottoAttaccoColco = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xAttaccoPers, yAttaccoPers, (GlobalVarG2.gpx * 9) + xFineAttaccoPers, (GlobalVarG2.gpy * 9) + yFineAttaccoPers))
            else:
                GlobalVarG2.schermo.blit(quadrettoSottoAttaccoColco, (xAttaccoPers, yAttaccoPers))

    if "attaccoNemici" in azioniDaEseguire and nemicoAttaccante and not cambiosta:
        if nemicoAttaccante.animaAttacco:
            xAttaccoNemico = 0
            yAttaccoNemico = 0
            if nemicoAttaccante.direzione == "w":
                xAttaccoNemico = nemicoAttaccante.x
                yAttaccoNemico = nemicoAttaccante.y - GlobalVarG2.gpy
            if nemicoAttaccante.direzione == "a":
                xAttaccoNemico = nemicoAttaccante.x - GlobalVarG2.gpx
                yAttaccoNemico = nemicoAttaccante.y
            if nemicoAttaccante.direzione == "s":
                xAttaccoNemico = nemicoAttaccante.x
                yAttaccoNemico = nemicoAttaccante.y + GlobalVarG2.gpy
            if nemicoAttaccante.direzione == "d":
                xAttaccoNemico = nemicoAttaccante.x + GlobalVarG2.gpx
                yAttaccoNemico = nemicoAttaccante.y
            if fineanimaz == 10:
                nemicoAttaccante.quadrettoSottoArma = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xAttaccoNemico, yAttaccoNemico, GlobalVarG2.gpx, GlobalVarG2.gpy))
            else:
                GlobalVarG2.schermo.blit(nemicoAttaccante.quadrettoSottoArma, (xAttaccoNemico, yAttaccoNemico))


def animaFrecceLanciate(x, y, attaccoADistanza, animaOggetto, rx, ry, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoAttaccante, cambiosta, azioniDaEseguire, fineanimaz):
    # disegno le frecce e gli oggetti lanciati da Rallo
    if "attaccoRallo" in azioniDaEseguire and (attaccoADistanza or animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata") and not cambiosta:
        xInizioRetta = x
        yInizioRetta = y
        if animaOggetto[0] == "bomba" or animaOggetto[0] == "bombaVeleno" or animaOggetto[0] == "esca" or animaOggetto[0] == "bombaAppiccicosa" or animaOggetto[0] == "bombaPotenziata":
            if fineanimaz == 10:
                GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.suonoLancioOggetti)
            xFineRetta = animaOggetto[1]
            yFineRetta = animaOggetto[2]
            imgFrecciaLanciata_temp = 0
            if animaOggetto[0] == "bomba":
                imgFrecciaLanciata_temp = GlobalVarG2.vetIcoOggettiMenu[5]
            elif animaOggetto[0] == "bombaVeleno":
                imgFrecciaLanciata_temp = GlobalVarG2.vetIcoOggettiMenu[6]
            elif animaOggetto[0] == "esca":
                imgFrecciaLanciata_temp = GlobalVarG2.vetIcoOggettiMenu[7]
            elif animaOggetto[0] == "bombaAppiccicosa":
                imgFrecciaLanciata_temp = GlobalVarG2.vetIcoOggettiMenu[8]
            elif animaOggetto[0] == "bombaPotenziata":
                imgFrecciaLanciata_temp = GlobalVarG2.vetIcoOggettiMenu[9]
        else:
            xFineRetta = attaccoADistanza.vx
            yFineRetta = attaccoADistanza.vy
            deltaXRetta = xFineRetta - xInizioRetta
            deltaYRetta = yFineRetta - yInizioRetta
            angoloInRadianti = -math.atan2(deltaYRetta, deltaXRetta)
            angoloInGradi = math.degrees(angoloInRadianti)
            imgFrecciaLanciata_temp = pygame.transform.rotate(GlobalVarG2.imgFrecciaLanciata, angoloInGradi)
        if fineanimaz > 5:
            GlobalVarG2.schermo.blit(imgFrecciaLanciata_temp, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz))))
        elif animaOggetto[0] and fineanimaz > 0:
            if animaOggetto[0] == "bomba":
                GlobalVarG2.schermo.blit(GlobalVarG2.imgAnimaBomba, (animaOggetto[1] - GlobalVarG2.gpx, animaOggetto[2] - GlobalVarG2.gpy))
                if fineanimaz == 5:
                    GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.suonoUsoBomba)
            elif animaOggetto[0] == "bombaVeleno":
                GlobalVarG2.schermo.blit(GlobalVarG2.imgAnimaBombaVeleno, (animaOggetto[1], animaOggetto[2]))
                if fineanimaz == 5:
                    GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.suonoUsoBombaVeleno)
            elif animaOggetto[0] == "esca":
                GlobalVarG2.schermo.blit(GlobalVarG2.vetIcoOggettiMenu[7], (animaOggetto[1], animaOggetto[2]))
                if fineanimaz == 5:
                    GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.suonoUsoEsca)
            elif animaOggetto[0] == "bombaAppiccicosa":
                GlobalVarG2.schermo.blit(GlobalVarG2.imgAnimaBombaAppiccicosa, (animaOggetto[1], animaOggetto[2]))
                if fineanimaz == 5:
                    GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.suonoUsoBombaAppiccicosa)
            elif animaOggetto[0] == "bombaPotenziata":
                GlobalVarG2.schermo.blit(GlobalVarG2.imgAnimaBombaPotenziata, (animaOggetto[1] - (GlobalVarG2.gpx * 2), animaOggetto[2] - (GlobalVarG2.gpy * 2)))
                if fineanimaz == 5:
                    GlobalVarG2.canaleSoundAttacco.play(GlobalVarG2.suonoUsoBombaPotenziata)

    # disegno le frecce elettriche lanciate da Colco
    if "attaccoColco" in azioniDaEseguire and listaNemiciAttaccatiADistanzaRobo and len(listaNemiciAttaccatiADistanzaRobo) == 1 and tecnicaUsata.startswith("freccia") and not cambiosta:
        xInizioRetta = rx
        xFineRetta = listaNemiciAttaccatiADistanzaRobo[0].vx
        yInizioRetta = ry
        yFineRetta = listaNemiciAttaccatiADistanzaRobo[0].vy
        deltaXRetta = xFineRetta - xInizioRetta
        deltaYRetta = yFineRetta - yInizioRetta
        angoloInRadianti = -math.atan2(deltaYRetta, deltaXRetta)
        angoloInGradi = math.degrees(angoloInRadianti)
        imgFrecciaLanciata_temp = 0
        if tecnicaUsata == "freccia":
            imgFrecciaLanciata_temp = pygame.transform.rotate(GlobalVarG2.imgFrecciaEletttricaLanciata, angoloInGradi)
        elif tecnicaUsata == "freccia+":
            imgFrecciaLanciata_temp = pygame.transform.rotate(GlobalVarG2.imgFrecciaEletttricaLanciataP, angoloInGradi)
        elif tecnicaUsata == "freccia++":
            imgFrecciaLanciata_temp = pygame.transform.rotate(GlobalVarG2.imgFrecciaEletttricaLanciataPP, angoloInGradi)
        if fineanimaz > 5:
            GlobalVarG2.schermo.blit(imgFrecciaLanciata_temp, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz))))

    # disegno gli oggetti lanciati dai nemici
    if "attaccoNemici" in azioniDaEseguire and nemicoAttaccante:
        if nemicoAttaccante.attaccaDaLontano and nemicoAttaccante.animaAttacco and not nemicoAttaccante.morto:
            xInizioRetta = nemicoAttaccante.x
            xFineRetta = nemicoAttaccante.xObbiettivo
            yInizioRetta = nemicoAttaccante.y
            yFineRetta = nemicoAttaccante.yObbiettivo
            deltaXRetta = xFineRetta - xInizioRetta
            deltaYRetta = yFineRetta - yInizioRetta
            angoloInRadianti = -math.atan2(deltaYRetta, deltaXRetta)
            angoloInGradi = math.degrees(angoloInRadianti)
            imgFrecciaLanciata_temp = pygame.transform.rotate(nemicoAttaccante.imgOggettoLanciato, angoloInGradi)
            if fineanimaz > 5:
                GlobalVarG2.schermo.blit(imgFrecciaLanciata_temp, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz))))
            elif fineanimaz != 0:
                GlobalVarG2.schermo.blit(nemicoAttaccante.imgDanneggiamentoOggettoLanciato, (xFineRetta, yFineRetta))


def animaVitaRalloNemicoInquadrato(dati, nemicoInquadrato, vitaesca, difesa, azioniDaEseguire, nemicoAttaccante, attaccoDiRallo, attaccoDiColco, statoRalloInizioTurno, statoColcoInizioTurno, statoEscheInizioTurno, listaNemici, fineanimaz, aumentoliv):
    if fineanimaz == 5:
        esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati, difesa)

        # vita-status personaggio (statoRalloInizioTurno[pv, veleno, attP, difP])
        if "attaccoNemici" in azioniDaEseguire and len(nemicoAttaccante.bersaglioColpito) > 0 and nemicoAttaccante.bersaglioColpito[0] == "Rallo":
            statoRalloInizioTurno[0] += nemicoAttaccante.bersaglioColpito[1]
            if nemicoAttaccante.bersaglioColpito[2] == "avvelena":
                statoRalloInizioTurno[1] = True
        if "attaccoColco" in azioniDaEseguire and len(attaccoDiColco) > 0 and "Rallo" in attaccoDiColco:
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
        lungvitatot = int(((GlobalVarG2.gpx * pvtot) / float(4)) // 5)
        lungvita = (lungvitatot * pvRallo) // pvtot
        if lungvita < 0:
            lungvita = 0
        indvitapers = pygame.transform.scale(GlobalVarG2.indvita, (lungvitatot, GlobalVarG2.gpy // 4))
        fineindvitapers = pygame.transform.scale(GlobalVarG2.fineindvita, (GlobalVarG2.gpx // 12, GlobalVarG2.gpy // 4))
        vitaral = pygame.transform.scale(GlobalVarG2.vitapersonaggio, (lungvita, GlobalVarG2.gpy // 4))
        GlobalVarG2.schermo.blit(GlobalVarG2.sfondoRallo, (GlobalVarG2.gsx // 32 * 0, GlobalVarG2.gsy // 18 * 17))
        GlobalVarG2.schermo.blit(indvitapers, (GlobalVarG2.gsx // 32 * 1, (GlobalVarG2.gsy // 18 * 17) + (GlobalVarG2.gpy // 4 * 3)))
        GlobalVarG2.schermo.blit(fineindvitapers, ((GlobalVarG2.gsx // 32 * 1) + lungvitatot, (GlobalVarG2.gsy // 18 * 17) + (GlobalVarG2.gpy // 4 * 3)))
        GlobalVarG2.schermo.blit(vitaral, (GlobalVarG2.gsx // 32 * 1, (GlobalVarG2.gsy // 18 * 17) + (GlobalVarG2.gpy // 4 * 3)))
        persbat = pygame.transform.scale(GlobalVarG2.perso, (GlobalVarG2.gpx, GlobalVarG2.gpy))
        GlobalVarG2.schermo.blit(persbat, (GlobalVarG2.gsx // 32 * 0, GlobalVarG2.gsy // 18 * 17))
        GlobalVarG2.schermo.blit(GlobalVarG2.perssb, (GlobalVarG2.gsx // 32 * 0, GlobalVarG2.gsy // 18 * 17))
        GlobalVarG2.schermo.blit(GlobalVarG2.imgNumFrecce, (int(GlobalVarG2.gsx // 32 * 1.2), GlobalVarG2.gsy // 18 * 17))
        messaggio(" x" + str(dati[132]), GlobalVarG2.grigiochi, int(GlobalVarG2.gsx // 32 * 1.8), int(GlobalVarG2.gsy // 18 * 17.2), 40)
        if velenoRallo:
            GlobalVarG2.schermo.blit(GlobalVarG2.avvelenato, (GlobalVarG2.gsx // 32 * 3, GlobalVarG2.gsy // 18 * 17))
        if attPRallo > 0:
            GlobalVarG2.schermo.blit(GlobalVarG2.attaccopiu, (GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 17))
        if difPRallo > 0:
            GlobalVarG2.schermo.blit(GlobalVarG2.difesapiu, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 17))

        # disegno la vita del Colco / esca / mostro selezionato
        if nemicoInquadrato == "Colco" or not nemicoInquadrato:
            if "attaccoNemici" in azioniDaEseguire and len(nemicoAttaccante.bersaglioColpito) > 0 and nemicoAttaccante.bersaglioColpito[0] == "Colco":
                statoColcoInizioTurno[0] += nemicoAttaccante.bersaglioColpito[1]
                if nemicoAttaccante.bersaglioColpito[2] == "surriscalda":
                    statoColcoInizioTurno[1] = 15
            if "attaccoColco" in azioniDaEseguire and len(attaccoDiColco) > 0 and "Colco" in attaccoDiColco:
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
            lungentot = int(((GlobalVarG2.gpx * entot) / float(4)) // 15)
            lungen = int(((GlobalVarG2.gpx * pvColco) / float(4)) // 15)
            if lungen < 0:
                lungen = 0
            indvitarob = pygame.transform.scale(GlobalVarG2.indvita, (lungentot, GlobalVarG2.gpy // 4))
            fineindvitarob = pygame.transform.scale(GlobalVarG2.fineindvita, (GlobalVarG2.gpx // 12, GlobalVarG2.gpy // 4))
            vitarob = pygame.transform.scale(GlobalVarG2.vitarobo, (lungen, GlobalVarG2.gpy // 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoColco, (0, 0))
            GlobalVarG2.schermo.blit(indvitarob, (GlobalVarG2.gpx, 0))
            GlobalVarG2.schermo.blit(fineindvitarob, (GlobalVarG2.gpx + lungentot, 0))
            GlobalVarG2.schermo.blit(vitarob, (GlobalVarG2.gpx, 0))
            robobat = pygame.transform.scale(GlobalVarG2.roboo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
            GlobalVarG2.schermo.blit(robobat, (0, 0))
            if surriscaldaColco > 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.surriscaldato, (GlobalVarG2.gpx + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
            if velPColco > 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.velocitapiu, ((GlobalVarG2.gpx * 2) + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
            if effPColco > 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.efficienzapiu, ((GlobalVarG2.gpx * 3) + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))

        if type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
            idEscaInquadrata = int(nemicoInquadrato[4:])
            i = 0
            while i < len(vitaesca):
                if idEscaInquadrata == vitaesca[i]:
                    idEscaInizioturno = 0
                    j = 0
                    while j < len(statoEscheInizioTurno):
                        if statoEscheInizioTurno[j] == nemicoInquadrato:
                            idEscaInizioturno = j
                            break
                        j += 2
                    if "attaccoNemici" in azioniDaEseguire and len(nemicoAttaccante.bersaglioColpito) > 0 and nemicoAttaccante.bersaglioColpito[0].startswith("Esca") and nemicoAttaccante.bersaglioColpito[0] == nemicoInquadrato:
                        statoEscheInizioTurno[idEscaInizioturno + 1] += nemicoAttaccante.bersaglioColpito[1]
                    pvEsca = statoEscheInizioTurno[idEscaInizioturno + 1]
                    lungvita = int(((GlobalVarG2.gpx * pvEsca) / float(4)) // 15)
                    if lungvita < 0:
                        lungvita = 0
                    GlobalVarG2.schermo.blit(GlobalVarG2.sfondoEsche, (0, 0))
                    GlobalVarG2.schermo.blit(GlobalVarG2.esche, (0, 0))
                    indvitamost = pygame.transform.scale(GlobalVarG2.indvita, (int(((GlobalVarG2.gpx * 1000) / float(4)) // 15), GlobalVarG2.gpy // 4))
                    fineindvitamost = pygame.transform.scale(GlobalVarG2.fineindvita, (GlobalVarG2.gpx // 12, GlobalVarG2.gpy // 4))
                    vitaesche = pygame.transform.scale(GlobalVarG2.vitanemico0, (lungvita, GlobalVarG2.gpy // 4))
                    GlobalVarG2.schermo.blit(indvitamost, (GlobalVarG2.gpx, 0))
                    GlobalVarG2.schermo.blit(fineindvitamost, (GlobalVarG2.gpx + (int(((GlobalVarG2.gpx * 1000) / float(4)) // 15)), 0))
                    GlobalVarG2.schermo.blit(vitaesche, (GlobalVarG2.gpx, 0))
                    break
                i += 4

        for nemico in listaNemici:
            if "attaccoRallo" in azioniDaEseguire and len(attaccoDiRallo) > 0 and nemico in attaccoDiRallo:
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
            if "attaccoColco" in azioniDaEseguire and len(attaccoDiColco) > 0 and nemico in attaccoDiColco:
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
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoMostro, (0, 0))
            if nemicoAvvelenato:
                GlobalVarG2.schermo.blit(GlobalVarG2.avvelenato, (GlobalVarG2.gpx + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
            if nemicoAppiccicato:
                GlobalVarG2.schermo.blit(GlobalVarG2.appiccicoso, ((GlobalVarG2.gpx * 2) + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
            GlobalVarG2.schermo.blit(nemicoInquadrato.imgS, (0, 0))
            fineindvitamost = pygame.transform.scale(GlobalVarG2.fineindvita, (GlobalVarG2.gpx // 12, GlobalVarG2.gpy // 4))
            if pvmtot > 1500:
                indvitamost = pygame.transform.scale(GlobalVarG2.indvita, (int(((GlobalVarG2.gpx * 1500) / float(4)) // 15), GlobalVarG2.gpy // 4))
                lungvitatot = int(((GlobalVarG2.gpx * 1500) / float(4)) // 15)
                GlobalVarG2.schermo.blit(fineindvitamost, (GlobalVarG2.gpx + lungvitatot, 0))
                if pvm > 15000:
                    pvm = 1500
                    vitanemsucc = pygame.transform.scale(GlobalVarG2.vitanemico00, (int(((GlobalVarG2.gpx * 1500) / float(4)) // 15), GlobalVarG2.gpy // 4))
                    vitanemico = GlobalVarG2.vitanemico9
                elif pvm > 13500:
                    pvm -= 13500
                    vitanemsucc = pygame.transform.scale(GlobalVarG2.vitanemico8, (int(((GlobalVarG2.gpx * 1500) / float(4)) // 15), GlobalVarG2.gpy // 4))
                    vitanemico = GlobalVarG2.vitanemico9
                elif pvm > 12000:
                    pvm -= 12000
                    vitanemsucc = pygame.transform.scale(GlobalVarG2.vitanemico7, (int(((GlobalVarG2.gpx * 1500) / float(4)) // 15), GlobalVarG2.gpy // 4))
                    vitanemico = GlobalVarG2.vitanemico8
                elif pvm > 10500:
                    pvm -= 10500
                    vitanemsucc = pygame.transform.scale(GlobalVarG2.vitanemico6, (int(((GlobalVarG2.gpx * 1500) / float(4)) // 15), GlobalVarG2.gpy // 4))
                    vitanemico = GlobalVarG2.vitanemico7
                elif pvm > 9000:
                    pvm -= 9000
                    vitanemsucc = pygame.transform.scale(GlobalVarG2.vitanemico5, (int(((GlobalVarG2.gpx * 1500) / float(4)) // 15), GlobalVarG2.gpy // 4))
                    vitanemico = GlobalVarG2.vitanemico6
                elif pvm > 7500:
                    pvm -= 7500
                    vitanemsucc = pygame.transform.scale(GlobalVarG2.vitanemico4, (int(((GlobalVarG2.gpx * 1500) / float(4)) // 15), GlobalVarG2.gpy // 4))
                    vitanemico = GlobalVarG2.vitanemico5
                elif pvm > 6000:
                    pvm -= 6000
                    vitanemsucc = pygame.transform.scale(GlobalVarG2.vitanemico3, (int(((GlobalVarG2.gpx * 1500) / float(4)) // 15), GlobalVarG2.gpy // 4))
                    vitanemico = GlobalVarG2.vitanemico4
                elif pvm > 4500:
                    pvm -= 4500
                    vitanemsucc = pygame.transform.scale(GlobalVarG2.vitanemico2, (int(((GlobalVarG2.gpx * 1500) / float(4)) // 15), GlobalVarG2.gpy // 4))
                    vitanemico = GlobalVarG2.vitanemico3
                elif pvm > 3000:
                    pvm -= 3000
                    vitanemsucc = pygame.transform.scale(GlobalVarG2.vitanemico1, (int(((GlobalVarG2.gpx * 1500) / float(4)) // 15), GlobalVarG2.gpy // 4))
                    vitanemico = GlobalVarG2.vitanemico2
                elif pvm > 1500:
                    pvm -= 1500
                    vitanemsucc = pygame.transform.scale(GlobalVarG2.vitanemico0, (int(((GlobalVarG2.gpx * 1500) / float(4)) // 15), GlobalVarG2.gpy // 4))
                    vitanemico = GlobalVarG2.vitanemico1
                else:
                    vitanemsucc = pygame.transform.scale(GlobalVarG2.vitanemico00, (int(((GlobalVarG2.gpx * 1500) / float(4)) // 15), GlobalVarG2.gpy // 4))
                    vitanemico = GlobalVarG2.vitanemico0
            else:
                lungvitatot = int(((GlobalVarG2.gpx * pvmtot) / float(4)) // 15)
                indvitamost = pygame.transform.scale(GlobalVarG2.indvita, (lungvitatot, GlobalVarG2.gpy // 4))
                GlobalVarG2.schermo.blit(fineindvitamost, (GlobalVarG2.gpx + lungvitatot, 0))
                vitanemsucc = pygame.transform.scale(GlobalVarG2.vitanemico00, (lungvitatot, GlobalVarG2.gpy // 4))
                vitanemico = GlobalVarG2.vitanemico0
            lungvita = int(((GlobalVarG2.gpx * pvm) / float(4)) // 15)
            if lungvita < 0:
                lungvita = 0
            vitanem = pygame.transform.scale(vitanemico, (lungvita, GlobalVarG2.gpy // 4))
            GlobalVarG2.schermo.blit(indvitamost, (GlobalVarG2.gpx, 0))
            GlobalVarG2.schermo.blit(vitanemsucc, (GlobalVarG2.gpx, 0))
            GlobalVarG2.schermo.blit(vitanem, (GlobalVarG2.gpx, 0))

    return statoRalloInizioTurno, statoColcoInizioTurno


def disagnaPuntatoreInquadraNemici(nemicoInquadrato, rx, ry, vitaesca):
    if nemicoInquadrato == "Colco":
        GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreInquadraNemici, (rx, ry))
    elif not type(nemicoInquadrato) is str and nemicoInquadrato:
        GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreInquadraNemici, (nemicoInquadrato.x, nemicoInquadrato.y))
    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
        idEscaInquadrata = int(nemicoInquadrato[4:])
        i = 0
        while i < len(vitaesca):
            if idEscaInquadrata == vitaesca[i]:
                GlobalVarG2.schermo.blit(GlobalVarG2.puntatoreInquadraNemici, (vitaesca[i + 2], vitaesca[i + 3]))
                break
            i += 4


def animaPersonaggiFermi(listaPersonaggi, azioniDaEseguire, cambiosta, fineanimaz):
    if not cambiosta:
        for personaggio in listaPersonaggi:
            if personaggio.inCasellaVista and not ("movimentoColcoNemiciPersonaggi" in azioniDaEseguire and personaggio.animaSpostamento) and not personaggio.animazioneFatta or (personaggio.inCasellaVista and fineanimaz == 0):
                if personaggio.animazioneFatta:
                    GlobalVarG2.schermo.blit(personaggio.imgAttuale, (personaggio.x, personaggio.y))
                else:
                    GlobalVarG2.schermo.blit(personaggio.imgAttuale, (personaggio.vx, personaggio.vy))


def animaSpostamentoPersonaggi(listaPersonaggi, animazionePersonaggi, cambiosta, fineanimaz):
    if not cambiosta:
        for personaggio in listaPersonaggi:
            if personaggio.inCasellaVista and personaggio.animaSpostamento and (personaggio.x != personaggio.vx or personaggio.y != personaggio.vy):
                personaggio.animazioneFatta = True
                animazionePersonaggi = True
                # rumorecamminataPersonaggi.play()
                if personaggio.direzione == "d":
                    if 5 < fineanimaz <= 10:
                        GlobalVarG2.schermo.blit(personaggio.imgDMov1, (personaggio.x - (GlobalVarG2.gpx * fineanimaz // 10), personaggio.y))
                    if 0 < fineanimaz <= 5:
                        GlobalVarG2.schermo.blit(personaggio.imgDMov2, (personaggio.x - (GlobalVarG2.gpx * fineanimaz // 10), personaggio.y))
                if personaggio.direzione == "a":
                    if 5 < fineanimaz <= 10:
                        GlobalVarG2.schermo.blit(personaggio.imgAMov1, (personaggio.x + (GlobalVarG2.gpx * fineanimaz // 10), personaggio.y))
                    if 0 < fineanimaz <= 5:
                        GlobalVarG2.schermo.blit(personaggio.imgAMov2, (personaggio.x + (GlobalVarG2.gpx * fineanimaz // 10), personaggio.y))
                if personaggio.direzione == "w":
                    if 5 < fineanimaz <= 10:
                        GlobalVarG2.schermo.blit(personaggio.imgWMov1, (personaggio.x, personaggio.y + (GlobalVarG2.gpy * fineanimaz // 10)))
                    if 0 < fineanimaz <= 5:
                        GlobalVarG2.schermo.blit(personaggio.imgWMov2, (personaggio.x, personaggio.y + (GlobalVarG2.gpy * fineanimaz // 10)))
                if personaggio.direzione == "s":
                    if 5 < fineanimaz <= 10:
                        GlobalVarG2.schermo.blit(personaggio.imgSMov1, (personaggio.x, personaggio.y - (GlobalVarG2.gpy * fineanimaz // 10)))
                    if 0 < fineanimaz <= 5:
                        GlobalVarG2.schermo.blit(personaggio.imgSMov2, (personaggio.x, personaggio.y - (GlobalVarG2.gpy * fineanimaz // 10)))
    return animazionePersonaggi


def anima(sposta, x, y, vx, vy, rx, ry, vrx, vry, pers, robot, npers, nrob, primopasso, cambiosta, sfondinoa, sfondinob, scudo, armatura, arma, armaMov1, armaMov2, armaAttacco, scudoDifesa, arco, faretra, arcoAttacco, guanti, guantiMov1, guantiMov2, guantiAttacco, guantiDifesa, collana, armaS, armaturaS, arcoS, faretraS, collanaS, armrob, armrobS, dati, attacco, difesa, tastop, tesoro, sfondinoc, aumentoliv, carim, caricaTutto, listaNemici, vitaesca, vettoreDenaro, attaccoADistanza, caseviste, porte, cofanetti, portaOriz, portaVert, numStanza, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoInquadrato, attaccoDiRallo, attaccoDiColco, statoRalloInizioTurno, statoColcoInizioTurno, statoEscheInizioTurno, raffreddamento, ricarica1, ricarica2, raffredda, autoRic1, autoRic2, animaOggetto, eschePrimaDelTurno, listaPersonaggi, movimentoPerMouse):
    schermo_prima_delle_animazioni = GlobalVarG2.schermo.copy()

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
                    if ((x / GlobalVarG2.gpx) + (y / GlobalVarG2.gpy)) % 2 == 0:
                        GlobalVarG2.schermo.blit(sfondinob, (vx, vy))
                    if ((x / GlobalVarG2.gpx) + (y / GlobalVarG2.gpy)) % 2 == 1:
                        GlobalVarG2.schermo.blit(sfondinoa, (vx, vy))
            else:
                if ((x / GlobalVarG2.gpx) + (y / GlobalVarG2.gpy)) % 2 == 0:
                    GlobalVarG2.schermo.blit(sfondinob, (vx, vy))
                    GlobalVarG2.schermo.blit(sfondinoa, (x, y))
                if ((x / GlobalVarG2.gpx) + (y / GlobalVarG2.gpy)) % 2 == 1:
                    GlobalVarG2.schermo.blit(sfondinoa, (vx, vy))
                    GlobalVarG2.schermo.blit(sfondinob, (x, y))
                if ((rx / GlobalVarG2.gpx) + (ry / GlobalVarG2.gpy)) % 2 == 0:
                    GlobalVarG2.schermo.blit(sfondinob, (vrx, vry))
                    GlobalVarG2.schermo.blit(sfondinoa, (rx, ry))
                if ((rx / GlobalVarG2.gpx) + (ry / GlobalVarG2.gpy)) % 2 == 1:
                    GlobalVarG2.schermo.blit(sfondinoa, (vrx, vry))
                    GlobalVarG2.schermo.blit(sfondinob, (rx, ry))
                for nemico in listaNemici:
                    if nemico.inCasellaVista:
                        if ((nemico.x / GlobalVarG2.gpx) + (nemico.y / GlobalVarG2.gpy)) % 2 == 0:
                            GlobalVarG2.schermo.blit(sfondinob, (nemico.vx, nemico.vy))
                            GlobalVarG2.schermo.blit(sfondinoa, (nemico.x, nemico.y))
                        if ((nemico.x / GlobalVarG2.gpx) + (nemico.y / GlobalVarG2.gpy)) % 2 == 1:
                            GlobalVarG2.schermo.blit(sfondinoa, (nemico.vx, nemico.vy))
                            GlobalVarG2.schermo.blit(sfondinob, (nemico.x, nemico.y))
                for personaggio in listaPersonaggi:
                    if personaggio.inCasellaVista:
                        if ((personaggio.x / GlobalVarG2.gpx) + (personaggio.y / GlobalVarG2.gpy)) % 2 == 0:
                            GlobalVarG2.schermo.blit(sfondinob, (personaggio.vx, personaggio.vy))
                            GlobalVarG2.schermo.blit(sfondinoa, (personaggio.x, personaggio.y))
                        if ((personaggio.x / GlobalVarG2.gpx) + (personaggio.y / GlobalVarG2.gpy)) % 2 == 1:
                            GlobalVarG2.schermo.blit(sfondinoa, (personaggio.vx, personaggio.vy))
                            GlobalVarG2.schermo.blit(sfondinob, (personaggio.x, personaggio.y))

            # disegno le GlobalVarG2.esche e il denaro
            animaEsche(vitaesca, eschePrimaDelTurno, caseviste, sfondinoa, sfondinob, azioniDaEseguire, animaOggetto)
            animaDenaro(vettoreDenaro, caseviste, sfondinoa, sfondinob)
            animaCofanetti(cofanetti, caseviste, sfondinoc)
            animaPorte(porte, cofanetti, numStanza, portaOriz, portaVert, sfondinoc)

            statoRalloInizioTurno, statoColcoInizioTurno = animaVitaRalloNemicoInquadrato(dati, nemicoInquadrato, vitaesca, difesa, azioniDaEseguire, nemicoAttaccante, attaccoDiRallo, attaccoDiColco, statoRalloInizioTurno, statoColcoInizioTurno, statoEscheInizioTurno, listaNemici, fineanimaz, aumentoliv)

            if fineanimaz == 10:
                schermo_prima_delle_animazioni = GlobalVarG2.schermo.copy()
            eliminaOggettoLanciato(x, y, attaccoADistanza, animaOggetto, rx, ry, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoAttaccante, schermo_prima_delle_animazioni, cambiosta, azioniDaEseguire, fineanimaz)
            disegnaCasellaAccantoAlPersCheAttacca(x, y, attacco, npers, rx, ry, nrob, tecnicaUsata, nemicoAttaccante, schermo_prima_delle_animazioni, cambiosta, azioniDaEseguire, fineanimaz)

            if cambiosta:
                quadrettoSottoRallo = schermo_prima_delle_animazioni.subsurface(pygame.Rect(x - GlobalVarG2.gpx, y - GlobalVarG2.gpy, GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
                GlobalVarG2.schermo.blit(quadrettoSottoRallo, (x - GlobalVarG2.gpx, y - GlobalVarG2.gpy))

            # disegna personaggi se ci sono animazioni ma non loro
            animaColcoFermo(rx, ry, vrx, vry, robot, armrob, armrobS, statoColcoInizioTurno[1], tecnicaUsata, azioniDaEseguire, animazioneColcoFatta, raffreddamento, ricarica1, ricarica2, raffredda, autoRic1, autoRic2, fineanimaz)
            animaNemiciFermi(listaNemici, azioniDaEseguire, cambiosta, nemicoAttaccante, fineanimaz)
            animaPersonaggiFermi(listaPersonaggi, azioniDaEseguire, cambiosta, fineanimaz)
            if not cambiosta:
                animaRalloFermo(x, y, vx, vy, npers, pers, scudo, armatura, arma, arco, faretra, guanti, collana, statoRalloInizioTurno[1], azioniDaEseguire, animazioneRalloFatta, nemicoAttaccante, difesa, fineanimaz)

            # tolgo il rumore passi quando non c'è l'animazione
            if not "movimentoRallo" in azioniDaEseguire and GlobalVarG2.canaleSoundPassiRallo.get_busy():
                GlobalVarG2.canaleSoundPassiRallo.stop()
            # animazione difesa Rallo
            animazioneRallo = animaDifesaRallo(x, y, armaS, armaturaS, arcoS, faretraS, collanaS, scudoDifesa, guantiDifesa, statoRalloInizioTurno[1], difesa, animazioneRallo, nemicoAttaccante, fineanimaz)

            if "aumentaLv" in azioniDaEseguire:
                # animazione aumento di livello
                animazioneRallo, caricaTutto, tastop, aumentoliv, movimentoPerMouse = animaLvUp(x, y, npers, pers, arma, armatura, scudo, collana, arco, faretra, guanti, dati[4], aumentoliv, carim, caricaTutto, tastop, animazioneRallo, movimentoPerMouse, fineanimaz)

            if "movimentoColcoNemiciPersonaggi" in azioniDaEseguire:
                # animazione camminata robo
                animazioneColco = animaCamminataRobo(nrob, rx, ry, vrx, vry, armrob, statoColcoInizioTurno[1], cambiosta, animazioneColco, fineanimaz)
                # animazione camminata mostri
                animazioneNemici = animaSpostamentoNemici(listaNemici, animazioneNemici, cambiosta, fineanimaz)
                # animazione camminata personaggi
                animazionePersonaggi = animaSpostamentoPersonaggi(listaPersonaggi, animazionePersonaggi, cambiosta, fineanimaz)
                # animazione morte nemici
                animazioneNemici = animaMorteNemici(listaNemici, animazioneNemici, cambiosta, fineanimaz)

            if "movimentoRallo" in azioniDaEseguire:
                # animazione camminata personaggio
                animazioneRallo, primopasso = animaCamminataRallo(sposta, x, y, vx, vy, primopasso, cambiosta, npers, pers, arma, scudo, armatura, armaMov1, armaMov2, arco, faretra, guanti, guantiMov1, guantiMov2, collana, statoRalloInizioTurno[1], attacco, difesa, tastop, animazioneRallo, movimentoPerMouse, fineanimaz)

            if "attaccoNemici" in azioniDaEseguire:
                # animazione danneggiamento Colco
                animaDanneggiamentoColco(rx, ry, nemicoAttaccante, cambiosta, fineanimaz)

                # animazione attacco nemici
                animaFrecceLanciate(x, y, attaccoADistanza, animaOggetto, rx, ry, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoAttaccante, cambiosta, azioniDaEseguire, fineanimaz)
                animazioneNemici = animaAttaccoNemici(nemicoAttaccante, animazioneNemici, fineanimaz)

            if "attaccoRallo" in azioniDaEseguire:
                # animazione attacco Rallo
                animaFrecceLanciate(x, y, attaccoADistanza, animaOggetto, rx, ry, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, listaNemici, cambiosta, azioniDaEseguire, fineanimaz)
                animazioneRallo = animaAttaccoRallo(sposta, x, y, npers, pers, arma, scudo, armatura, collana, arco, faretra, guanti, armaAttacco, arcoAttacco, guantiAttacco, statoRalloInizioTurno[1], attacco, difesa, vrx, vry, armrobS, sfondinoa, sfondinob, animazioneRallo, attaccoADistanza, animaOggetto, fineanimaz)

                # animazione danneggiamento dei nemici
                animazioneNemici = animaDanneggiamentoNemici(listaNemici, animazioneNemici, cambiosta, azioniDaEseguire, "Rallo")

            if "attaccoColco" in azioniDaEseguire:
                # animazione attacco Colco
                animaFrecceLanciate(x, y, attaccoADistanza, animaOggetto, rx, ry, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, listaNemici, cambiosta, azioniDaEseguire, fineanimaz)
                animazioneColco = animaTecnicaColco(rx, ry, nrob, robot, armrob, armrobS, tecnicaUsata, cambiosta, animazioneColco, fineanimaz)

                # animazione danneggiamento dei nemici
                animazioneNemici = animaDanneggiamentoNemici(listaNemici, animazioneNemici, cambiosta, azioniDaEseguire, "Colco")

            # animazione apertura cofanetto
            animazioneRallo = animaAperturaCofanetto(tesoro, x, y, npers, pers, statoRalloInizioTurno[1], armatura, arma, scudo, collana, arco, faretra, guanti, sfondinoc, animazioneRallo)
            # anima raccolta denaro
            denaroRaccolto = animaRaccoltaDenaro(x, y, vettoreDenaro, dati[130], fineanimaz)

            # disegno img GlobalVarG2.puntatoreInquadraNemici
            disagnaPuntatoreInquadraNemici(nemicoInquadrato, rx, ry, vitaesca)

            if animazioneRallo:
                animazioneRalloFatta = True
            if animazioneColco:
                animazioneColcoFatta = True

            pygame.event.pump()
            if (animazioneNemici or animazioneRallo or animazioneColco or animazionePersonaggi) and fineanimaz > 0:
                pygame.display.update()
                GlobalVarG2.clockAnimazioni.tick(GlobalVarG2.fpsAnimazioni)
                # print (GlobalVarG2.clockAnimazioni.get_fps())
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
        if GlobalVarG2.mouseBloccato:
            GlobalVarG2.configuraCursore(False)
        pygame.display.update()
        risposta = False
        sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
        while not risposta:
            deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
            if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVarG2.mouseVisibile:
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True
            for event in pygame.event.get():
                sinistroMouseVecchio = sinistroMouse
                centraleMouseVecchio = centraleMouse
                destroMouseVecchio = destroMouse
                sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
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
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse):
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                    risposta = True
                if event.type == pygame.KEYDOWN:
                    if GlobalVarG2.mouseVisibile:
                        pygame.mouse.set_visible(False)
                        GlobalVarG2.mouseVisibile = False
        movimentoPerMouse = False
        caricaTutto = True
        tesoro = -1
    if denaroRaccolto:
        if GlobalVarG2.mouseBloccato:
            GlobalVarG2.configuraCursore(False)
        pygame.display.update()
        risposta = False
        sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
        while not risposta:
            deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
            if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVarG2.mouseVisibile:
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True
            for event in pygame.event.get():
                sinistroMouseVecchio = sinistroMouse
                centraleMouseVecchio = centraleMouse
                destroMouseVecchio = destroMouse
                sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
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
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse):
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                    risposta = True
                if event.type == pygame.KEYDOWN:
                    if GlobalVarG2.mouseVisibile:
                        pygame.mouse.set_visible(False)
                        GlobalVarG2.mouseVisibile = False
        movimentoPerMouse = False
        caricaTutto = True
        tastop = 0

    return primopasso, caricaTutto, tesoro, tastop, movimentoPerMouse
