# -*- coding: utf-8 -*-

from GenericFuncG2 import *
import math


def animaCamminataRalloCambiosta(npers, x, y, scudo, armatura, armaMov1, arco, faretra, guantiMov1, collana, avvele, fineanimaz):
    if npers == 1:
        x = x - (gpx * 2 // 3)
    if npers == 2:
        x = x + (gpx * 2 // 3)
    if npers == 3:
        y = y + (gpy * 2 // 3)
    if npers == 4:
        y = y - (gpy * 2 // 3)
    pers = False
    if 5 < fineanimaz <= 10:
        frame = 1
        disegnaRallo(npers, x, y, avvele, pers, armaMov1, armatura, scudo, collana, arco, faretra, guantiMov1, True, frame)


def animaCamminataRalloSpostato(npers, x, y, scudo, armatura, armaMov1, armaMov2, arco, faretra, guantiMov1, guantiMov2, collana, avvele, fineanimaz):
    if npers == 1:
        x = x - (gpx * fineanimaz // 10)
    if npers == 2:
        x = x + (gpx * fineanimaz // 10)
    if npers == 3:
        y = y + (gpy * fineanimaz // 10)
    if npers == 4:
        y = y - (gpy * fineanimaz // 10)
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


def animaCamminataRallo(sposta, x, y, vx, vy, primopasso, cambiosta, npers, scudo, armatura, armaMov1, armaMov2, arco, faretra, guantiMov1, guantiMov2, collana, avvele, attacco, difesa, tastop, animazioneRallo, fineanimaz):
    if sposta:
        # mentre ci si sposta
        if x != vx or y != vy:
            animazioneRallo = True
            if not canaleSoundPassiRallo.get_busy():
                canaleSoundPassiRallo.play(rumorecamminata)
            if primopasso and not cambiosta:
                primopasso = False
            # camminata quando si entra in una stanza
            if cambiosta:
                animaCamminataRalloCambiosta(npers, x, y, scudo, armatura, armaMov1, arco, faretra, guantiMov1, collana, avvele, fineanimaz)
                if fineanimaz == 0:
                    canaleSoundPassiRallo.stop()
            # camminata quando non si entra in una stanza
            else:
                animaCamminataRalloSpostato(npers, x, y, scudo, armatura, armaMov1, armaMov2, arco, faretra, guantiMov1, guantiMov2, collana, avvele, fineanimaz)
        # mentre non ci si sposta
        elif attacco == 0 and not difesa and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
            animazioneRallo = True
            if not canaleSoundPassiRallo.get_busy():
                canaleSoundPassiRallo.play(rumorecamminata)
            if primopasso:
                primopasso = False
            animaCamminataRalloFermo(npers, x, y, scudo, armatura, armaMov1, armaMov2, arco, faretra, guantiMov1, guantiMov2, collana, avvele, fineanimaz)
    elif canaleSoundPassiRallo.get_busy():
        canaleSoundPassiRallo.stop()
    return animazioneRallo, primopasso


def animaAttaccoRallo(sposta, x, y, npers, pers, scudo, armatura, collana, arco, faretra, armaAttacco, arcoAttacco, guantiAttacco, avvele, attacco, difesa, animazioneRallo, attaccoADistanza, fineanimaz):
    if sposta and fineanimaz != 0:
        if attacco == 1 and difesa == 0:
            animazioneRallo = True
            if attaccoADistanza:
                if fineanimaz == 10 and not canaleSoundAttacco.get_busy():
                    canaleSoundAttacco.play(rumoreAttaccoArco)
                disegnaRallo(npers, x, y, avvele, pers, armaAttacco, armatura, scudo, collana, arcoAttacco, faretra, guantiAttacco, False, False, False, True)
            else:
                if fineanimaz == 10 and not canaleSoundAttacco.get_busy():
                    canaleSoundAttacco.play(rumoreAttaccoSpada)
                disegnaRallo(npers, x, y, avvele, pers, armaAttacco, armatura, scudo, collana, arco, faretra, guantiAttacco, False, False, True)
    return animazioneRallo


def animaDifesaRallo(sposta, x, y, armaS, armaturaS, arcoS, faretraS, collanaS, scudoDifesa, guantiDifesa, avvele, difesa, animazioneRallo, nemicoAttaccante, fineanimaz):
    if nemicoAttaccante and nemicoAttaccante.ralloParato and fineanimaz == 10:
        canaleSoundAttacco.play(rumoreParata)
    if sposta and fineanimaz != 0:
        if difesa != 0 or (nemicoAttaccante and nemicoAttaccante.ralloParato):
            animazioneRallo = True
            schermo.blit(arcoS, (x, y))
            schermo.blit(faretraS, (x, y))
            schermo.blit(perss, (x, y))
            if avvele:
                schermo.blit(persAvvele, (x, y))
            schermo.blit(armaturaS, (x, y))
            schermo.blit(collanaS, (x, y))
            schermo.blit(persmbDifesa, (x, y))
            schermo.blit(armaS, (x, y))
            schermo.blit(guantiDifesa, (x, y))
            schermo.blit(scudoDifesa, (x, y))
    elif not sposta and (difesa != 0 or (nemicoAttaccante and nemicoAttaccante.ralloParato)) and fineanimaz != 0:
        animazioneRallo = True
        schermo.blit(arcoS, (x, y))
        schermo.blit(faretraS, (x, y))
        schermo.blit(perss, (x, y))
        if avvele:
            schermo.blit(persAvvele, (x, y))
        schermo.blit(armaturaS, (x, y))
        schermo.blit(collanaS, (x, y))
        schermo.blit(persmbDifesa, (x, y))
        schermo.blit(armaS, (x, y))
        schermo.blit(guantiDifesa, (x, y))
        schermo.blit(scudoDifesa, (x, y))
    return animazioneRallo


def animaLvUp(x, y, npers, pers, arma, armatura, scudo, collana, arco, faretra, guanti, liv, aumentoliv, carim, caricaTutto, tastop, animazioneRallo, fineanimaz):
    if aumentoliv and not carim:
        animazioneRallo = True
        if not canaleSoundLvUp.get_busy() and fineanimaz == 10:
            canaleSoundLvUp.play(rumorelevelup)
        avvele = False
        disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
        if 5 <= fineanimaz <= 10:
            schermo.blit(saliliv2, (x, y))
        if 1 < fineanimaz <= 5:
            schermo.blit(saliliv1, (x, y))
        if fineanimaz == 1:
            schermo.blit(saliliv, (x, y))

        schermo.blit(sfocontcof, (gsx // 32 * 0, gsy // 18 * 0))
        i = 1
        while i <= 100:
            if liv == i:
                messaggio("Liv +: Punti vita aumentati", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
                break
            i += 3
        i = 2
        while i <= 100:
            if liv == i:
                messaggio("Liv +: Attacco aumentato", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
                break
            i += 3
        i = 3
        while i <= 100:
            if liv == i:
                messaggio("Liv +: Difesa aumentata", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
                break
            i += 3
        if fineanimaz == 1:
            pygame.display.update()
            pygame.time.wait(500)
            risposta = False
            while not risposta:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        canaleSoundPuntatore.play(selezione)
                        risposta = True

        caricaTutto = True
        tastop = 0
    return animazioneRallo, caricaTutto, tastop


def animaRalloFermo(x, y, vx, vy, npers, pers, scudo, armatura, arma, arco, faretra, guanti, collana, avvele, azioniDaEseguire, animazioneRalloFatta, nemicoAttaccante, difesa, fineanimaz):
    if (not "attaccoRallo" in azioniDaEseguire and not "movimentoRallo" in azioniDaEseguire and not (nemicoAttaccante and nemicoAttaccante.ralloParato) and difesa == 0) or fineanimaz == 0:
        if animazioneRalloFatta:
            disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
        else:
            disegnaRallo(npers, vx, vy, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)


def animaCamminataRobo(nrob, rx, ry, vrx, vry, armrob, surriscalda, cambiosta, animazioneColco, fineanimaz):
    if (rx != vrx or ry != vry) and not cambiosta:
        animazioneColco = True
        # rumorecamminataRobo.play()
        if nrob == 1:
            if 5 < fineanimaz <= 10:
                schermo.blit(robodp, (rx - (gpx * fineanimaz // 10), ry))
                if surriscalda > 0:
                    schermo.blit(roboSurrisc, (rx - (gpx * fineanimaz // 10), ry))
                schermo.blit(armrob, (rx - (gpx * fineanimaz // 10), ry))
            if 0 < fineanimaz <= 5:
                schermo.blit(robodp, (rx - (gpx * fineanimaz // 10), ry))
                if surriscalda > 0:
                    schermo.blit(roboSurrisc, (rx - (gpx * fineanimaz // 10), ry))
                schermo.blit(armrob, (rx - (gpx * fineanimaz // 10), ry))
        if nrob == 2:
            if 5 < fineanimaz <= 10:
                schermo.blit(roboap, (rx + (gpx * fineanimaz // 10), ry))
                if surriscalda > 0:
                    schermo.blit(roboSurrisc, (rx + (gpx * fineanimaz // 10), ry))
                schermo.blit(armrob, (rx + (gpx * fineanimaz // 10), ry))
            if 0 < fineanimaz <= 5:
                schermo.blit(roboap, (rx + (gpx * fineanimaz // 10), ry))
                if surriscalda > 0:
                    schermo.blit(roboSurrisc, (rx + (gpx * fineanimaz // 10), ry))
                schermo.blit(armrob, (rx + (gpx * fineanimaz // 10), ry))
        if nrob == 4:
            if 5 < fineanimaz <= 10:
                schermo.blit(robow, (rx, ry + (gpy * fineanimaz // 10)))
                if surriscalda > 0:
                    schermo.blit(roboSurrisc, (rx, ry + (gpy * fineanimaz // 10)))
                schermo.blit(armrob, (rx, ry + (gpy * fineanimaz // 10)))
            if 0 < fineanimaz <= 5:
                schermo.blit(robow, (rx, ry + (gpy * fineanimaz // 10)))
                if surriscalda > 0:
                    schermo.blit(roboSurrisc, (rx, ry + (gpy * fineanimaz // 10)))
                schermo.blit(armrob, (rx, ry + (gpy * fineanimaz // 10)))
        if nrob == 3:
            if 5 < fineanimaz <= 10:
                schermo.blit(robos, (rx, ry - (gpy * fineanimaz // 10)))
                if surriscalda > 0:
                    schermo.blit(roboSurrisc, (rx, ry - (gpy * fineanimaz // 10)))
                schermo.blit(armrob, (rx, ry - (gpy * fineanimaz // 10)))
            if 0 < fineanimaz <= 5:
                schermo.blit(robos, (rx, ry - (gpy * fineanimaz // 10)))
                if surriscalda > 0:
                    schermo.blit(roboSurrisc, (rx, ry - (gpy * fineanimaz // 10)))
                schermo.blit(armrob, (rx, ry - (gpy * fineanimaz // 10)))
    return animazioneColco


def animaColcoFermo(rx, ry, vrx, vry, robot, armrob, surriscalda, tecnicaUsata, azioniDaEseguire, animazioneColcoFatta, fineanimaz):
    if (not "attaccoColco" in azioniDaEseguire and not ("movimentoColcoNemici" in azioniDaEseguire and tecnicaUsata == "spostamento")) or fineanimaz == 0:
        if animazioneColcoFatta:
            schermo.blit(robot, (rx, ry))
            if surriscalda > 0:
                schermo.blit(roboSurrisc, (rx, ry))
            schermo.blit(armrob, (rx, ry))
        else:
            schermo.blit(robot, (vrx, vry))
            if surriscalda > 0:
                schermo.blit(roboSurrisc, (vrx, vry))
            schermo.blit(armrob, (vrx, vry))


def animaSpostamentoNemici(listaNemici, animazioneNemici, cambiosta, fineanimaz):
    if not cambiosta:
        for nemico in listaNemici:
            if nemico.animaSpostamento and not nemico.morto and (nemico.x != nemico.vx or nemico.y != nemico.vy):
                nemico.animazioneFatta = True
                animazioneNemici = True
                # rumorecamminataNemico.play()
                if nemico.direzione == "d":
                    if 5 < fineanimaz <= 10:
                        schermo.blit(nemico.imgDMov1, (nemico.x - (gpx * fineanimaz // 10), nemico.y))
                        if nemico.appiccicato:
                            schermo.blit(nemico.imgAppiccicato, (nemico.x - (gpx * fineanimaz // 10), nemico.y))
                        if nemico.avvelenato:
                            schermo.blit(nemico.imgAvvelenamento, (nemico.x - (gpx * fineanimaz // 10), nemico.y))
                    if 0 < fineanimaz <= 5:
                        schermo.blit(nemico.imgDMov2, (nemico.x - (gpx * fineanimaz // 10), nemico.y))
                        if nemico.appiccicato:
                            schermo.blit(nemico.imgAppiccicato, (nemico.x - (gpx * fineanimaz // 10), nemico.y))
                        if nemico.avvelenato:
                            schermo.blit(nemico.imgAvvelenamento, (nemico.x - (gpx * fineanimaz // 10), nemico.y))
                if nemico.direzione == "a":
                    if 5 < fineanimaz <= 10:
                        schermo.blit(nemico.imgAMov1, (nemico.x + (gpx * fineanimaz // 10), nemico.y))
                        if nemico.appiccicato:
                            schermo.blit(nemico.imgAppiccicato, (nemico.x + (gpx * fineanimaz // 10), nemico.y))
                        if nemico.avvelenato:
                            schermo.blit(nemico.imgAvvelenamento, (nemico.x + (gpx * fineanimaz // 10), nemico.y))
                    if 0 < fineanimaz <= 5:
                        schermo.blit(nemico.imgAMov2, (nemico.x + (gpx * fineanimaz // 10), nemico.y))
                        if nemico.appiccicato:
                            schermo.blit(nemico.imgAppiccicato, (nemico.x + (gpx * fineanimaz // 10), nemico.y))
                        if nemico.avvelenato:
                            schermo.blit(nemico.imgAvvelenamento, (nemico.x + (gpx * fineanimaz // 10), nemico.y))
                if nemico.direzione == "w":
                    if 5 < fineanimaz <= 10:
                        schermo.blit(nemico.imgWMov1, (nemico.x, nemico.y + (gpy * fineanimaz // 10)))
                        if nemico.appiccicato:
                            schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y + (gpy * fineanimaz // 10)))
                        if nemico.avvelenato:
                            schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y + (gpy * fineanimaz // 10)))
                    if 0 < fineanimaz <= 5:
                        schermo.blit(nemico.imgWMov2, (nemico.x, nemico.y + (gpy * fineanimaz // 10)))
                        if nemico.appiccicato:
                            schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y + (gpy * fineanimaz // 10)))
                        if nemico.avvelenato:
                            schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y + (gpy * fineanimaz // 10)))
                if nemico.direzione == "s":
                    if 5 < fineanimaz <= 10:
                        schermo.blit(nemico.imgSMov1, (nemico.x, nemico.y - (gpy * fineanimaz // 10)))
                        if nemico.appiccicato:
                            schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y - (gpy * fineanimaz // 10)))
                        if nemico.avvelenato:
                            schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y - (gpy * fineanimaz // 10)))
                    if 0 < fineanimaz <= 5:
                        schermo.blit(nemico.imgSMov2, (nemico.x, nemico.y - (gpy * fineanimaz // 10)))
                        if nemico.appiccicato:
                            schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y - (gpy * fineanimaz // 10)))
                        if nemico.avvelenato:
                            schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y - (gpy * fineanimaz // 10)))
    return animazioneNemici


def animaAttaccoNemici(nemicoAttaccante, animazioneNemici, fineanimaz):
    if nemicoAttaccante and fineanimaz != 0:
        if nemicoAttaccante.animaAttacco and not nemicoAttaccante.animazioneFatta:
            if fineanimaz == 1:
                nemicoAttaccante.animazioneFatta = True
            animazioneNemici = True
            # if fineanimaz == 10 and not canaleSoundAttacco.get_busy():
            #     canaleSoundAttacco.play(rumoreattacco)
            if nemicoAttaccante.direzione == "w":
                schermo.blit(nemicoAttaccante.imgAttaccoW, (nemicoAttaccante.x, nemicoAttaccante.y - gpy))
            if nemicoAttaccante.direzione == "a":
                schermo.blit(nemicoAttaccante.imgAttaccoA, (nemicoAttaccante.x - gpx, nemicoAttaccante.y))
            if nemicoAttaccante.direzione == "s":
                schermo.blit(nemicoAttaccante.imgAttaccoS, (nemicoAttaccante.x, nemicoAttaccante.y))
            if nemicoAttaccante.direzione == "d":
                schermo.blit(nemicoAttaccante.imgAttaccoD, (nemicoAttaccante.x, nemicoAttaccante.y))
            if nemicoAttaccante.appiccicato:
                schermo.blit(nemicoAttaccante.imgAppiccicato, (nemicoAttaccante.x, nemicoAttaccante.y))
            if nemicoAttaccante.avvelenato:
                schermo.blit(nemicoAttaccante.imgAvvelenamento, (nemicoAttaccante.x, nemicoAttaccante.y))
    return animazioneNemici


def animaMorteNemici(listaNemici, animazioneNemici, cambiosta, fineanimaz):
    if not cambiosta:
        for nemico in listaNemici:
            if nemico.animaMorte:
                nemico.animazioneFatta = True
                animazioneNemici = True
                if 5 <= fineanimaz <= 10:
                    schermo.blit(nemico.imgMorte1, (nemico.x, nemico.y))
                if 1 < fineanimaz <= 5:
                    schermo.blit(nemico.imgMorte2, (nemico.x, nemico.y))
    return animazioneNemici


def animaDanneggiamentoNemici(listaNemici, animazioneNemici, cambiosta, azioniDaEseguire, attaccante):
    if not cambiosta:
        for nemico in listaNemici:
            if ("Rallo" in nemico.animaDanneggiamento and "attaccoRallo" in azioniDaEseguire) or ("Colco" in nemico.animaDanneggiamento and "attaccoColco" in azioniDaEseguire):
                animazioneNemici = True
                if attaccante == "Rallo":
                    schermo.blit(nemico.imgDanneggiamentoRallo, (nemico.vx, nemico.vy))
                if attaccante == "Colco":
                    schermo.blit(nemico.imgDanneggiamentoColco, (nemico.vx, nemico.vy))
                if nemico.appiccicato:
                    schermo.blit(nemico.imgAppiccicato, (nemico.vx, nemico.vy))
                if nemico.avvelenato:
                    schermo.blit(nemico.imgAvvelenamento, (nemico.vx, nemico.vy))
    return animazioneNemici


def animaNemiciFermi(listaNemici, azioniDaEseguire, cambiosta, nemicoAttaccante, fineanimaz):
    if not cambiosta:
        for nemico in listaNemici:
            if nemico.inCasellaVista and not (("movimentoColcoNemici" in azioniDaEseguire and (nemico.animaSpostamento or nemico.animaMorte)) or ("attaccoNemici" in azioniDaEseguire and nemico.animaAttacco and nemicoAttaccante == nemico)) and not (nemico.animaMorte and nemico.animazioneFatta) or (nemico.inCasellaVista and fineanimaz == 0 and not nemico.animaMorte):
                if nemico.animazioneFatta:
                    schermo.blit(nemico.imgAttuale, (nemico.x, nemico.y))
                    if nemico.appiccicato:
                        schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y))
                    if nemico.avvelenato:
                        schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y))
                else:
                    schermo.blit(nemico.imgAttuale, (nemico.vx, nemico.vy))
                    if nemico.appiccicato:
                        schermo.blit(nemico.imgAppiccicato, (nemico.vx, nemico.vy))
                    if nemico.avvelenato:
                        schermo.blit(nemico.imgAvvelenamento, (nemico.vx, nemico.vy))


def animaEsche(vitaesca, caseviste, sfondinoa, sfondinob):
    i = 0
    while i < len(vitaesca):
        j = 0
        while j < len(caseviste):
            if ((caseviste[j] == vitaesca[i + 2] - gpx and caseviste[j + 1] == vitaesca[i + 3]) or (caseviste[j] == vitaesca[i + 2] + gpx and caseviste[j + 1] == vitaesca[i + 3]) or (caseviste[j] == vitaesca[i + 2] and caseviste[j + 1] == vitaesca[i + 3] - gpy) or (caseviste[j] == vitaesca[i + 2] and caseviste[j + 1] == vitaesca[i + 3] + gpy)) and caseviste[j + 2]:
                if ((vitaesca[i + 2] / gpx) + (vitaesca[i + 3] / gpy)) % 2 == 0:
                    schermo.blit(sfondinoa, (vitaesca[i + 2], vitaesca[i + 3]))
                if ((vitaesca[i + 2] / gpx) + (vitaesca[i + 3] / gpy)) % 2 == 1:
                    schermo.blit(sfondinob, (vitaesca[i + 2], vitaesca[i + 3]))
                schermo.blit(esche, (vitaesca[i + 2], vitaesca[i + 3]))
                break
            j += 3
        i += 4


def animaDenaro(vettoreDenaro, caseviste, sfondinoa, sfondinob):
    i = 0
    while i < len(vettoreDenaro):
        j = 0
        while j < len(caseviste):
            if ((caseviste[j] == vettoreDenaro[i + 1] - gpx and caseviste[j + 1] == vettoreDenaro[i + 2]) or (caseviste[j] == vettoreDenaro[i + 1] + gpx and caseviste[j + 1] == vettoreDenaro[i + 2]) or (caseviste[j] == vettoreDenaro[i + 1] and caseviste[j + 1] == vettoreDenaro[i + 2] - gpy) or (caseviste[j] == vettoreDenaro[i + 1] and caseviste[j + 1] == vettoreDenaro[i + 2] + gpy)) and caseviste[j + 2]:
                if ((vettoreDenaro[i + 1] / gpx) + (vettoreDenaro[i + 2] / gpy)) % 2 == 0:
                    schermo.blit(sfondinoa, (vettoreDenaro[i + 1], vettoreDenaro[i + 2]))
                if ((vettoreDenaro[i + 1] / gpx) + (vettoreDenaro[i + 2] / gpy)) % 2 == 1:
                    schermo.blit(sfondinob, (vettoreDenaro[i + 1], vettoreDenaro[i + 2]))
                schermo.blit(sacchettoDenaro, (vettoreDenaro[i + 1], vettoreDenaro[i + 2]))
                break
            j += 3
        i += 3


def animaCofanetti(cofanetti, caseviste, sfondinoc):
    # cofanetti[stanza, x, y, True / False, ...]
    i = 0
    while i < len(cofanetti):
        j = 0
        while j < len(caseviste):
            if ((caseviste[j] == cofanetti[i + 1] - gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] + gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - gpy) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + gpy)) and caseviste[j + 2]:
                schermo.blit(sfondinoc, (cofanetti[i + 1], cofanetti[i + 2]))
                if cofanetti[i + 3]:
                    schermo.blit(cofaniaper, (cofanetti[i + 1], cofanetti[i + 2]))
                else:
                    schermo.blit(cofanichiu, (cofanetti[i + 1], cofanetti[i + 2]))
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
            murx, mury, inutile, inutile, inutile = muri_porte(vmurx, vmury, gpx, 0, numStanza, False, False, False, porte, cofanetti)
            schermo.blit(sfondinoc, (porte[i + 1], porte[i + 2]))
            if vmurx == murx and vmury == mury:
                schermo.blit(portaOriz, (porte[i + 1], porte[i + 2]))
            else:
                schermo.blit(portaVert, (porte[i + 1], porte[i + 2]))
        i = i + 4


def animaAperturaCofanetto(tesoro, x, y, npers, pers, avvele, armatura, arma, scudo, collana, arco, faretra, guanti, sfondinoc, animazioneRallo):
    if tesoro != -1:
        animazioneRallo = True
        disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
        if npers == 1:
            schermo.blit(sfondinoc, (x + gpx, y))
            schermo.blit(cofaniaper, (x + gpx, y))
        if npers == 2:
            schermo.blit(sfondinoc, (x - gpx, y))
            schermo.blit(cofaniaper, (x - gpx, y))
        if npers == 3:
            schermo.blit(sfondinoc, (x, y - gpy))
            schermo.blit(cofaniaper, (x, y - gpy))
        if npers == 4:
            schermo.blit(sfondinoc, (x, y + gpy))
            schermo.blit(cofaniaper, (x, y + gpy))
        schermo.blit(sfocontcof, (gsx // 32 * 0, gsy // 18 * 0))
        if tesoro == -2:
            messaggio("Hai trovato: Niente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        # 31-40 -> oggetti(10) / 41-70 -> armi(30) / 71-75 -> batterie(5) / 81-100 -> condizioni(20) / 101-120 -> gambit (=celle di memoria)(20) / 131 -> monete / 132 frecce
        if tesoro >= 11 and tesoro <= 30:
            messaggio("Hai trovato: Una nuova tecnica", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 31:
            messaggio("Hai trovato: Pozione", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 32:
            messaggio("Hai trovato: Caricabatterie", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 33:
            messaggio("Hai trovato: Medicina", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 34:
            messaggio("Hai trovato: Superpozione", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 35:
            messaggio("Hai trovato: Caricabatterie migliorato", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 36:
            messaggio("Hai trovato: Bomba", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 37:
            messaggio("Hai trovato: Bomba velenosa", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 38:
            messaggio("Hai trovato: Esca", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 39:
            messaggio("Hai trovato: Bomba appiccicosa", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 40:
            messaggio("Hai trovato: Bomba potenziata", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 41:
            messaggio("Hai trovato: Niente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 42:
            messaggio("Hai trovato: Spada di ferro", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 43:
            messaggio("Hai trovato: Spadone d'acciaio", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 44:
            messaggio("Hai trovato: Lykother", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 45:
            messaggio("Hai trovato: Mendaxritas", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 46:
            messaggio("Hai trovato: Niente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 47:
            messaggio("Hai trovato: Arco di legno", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 48:
            messaggio("Hai trovato: Arco di ferro", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 49:
            messaggio("Hai trovato: Arco di precisione", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 50:
            messaggio("Hai trovato: Accipiter", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 51:
            messaggio("Hai trovato: Niente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 52:
            messaggio("Hai trovato: Armatura di pelle", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 53:
            messaggio("Hai trovato: Armatura d'acciaio", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 54:
            messaggio("Hai trovato: Lykodes", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 55:
            messaggio("Hai trovato: Loriquam", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 56:
            messaggio("Hai trovato: Niente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 57:
            messaggio("Hai trovato: Scudo di pelle", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 58:
            messaggio("Hai trovato: Scudo d'acciaio", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 59:
            messaggio("Hai trovato: Lykethmos", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 60:
            messaggio("Hai trovato: Clipequam", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 61:
            messaggio("Hai trovato: Niente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 62:
            messaggio("Hai trovato: Guanti vitali", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 63:
            messaggio("Hai trovato: Guanti difensivi", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 64:
            messaggio("Hai trovato: Guanti offensivi", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 65:
            messaggio("Hai trovato: Guanti confortevoli", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 66:
            messaggio("Hai trovato: Niente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 67:
            messaggio("Hai trovato: Collana medicinale", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 68:
            messaggio("Hai trovato: Collana rigenerante", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 69:
            messaggio("Hai trovato: Apprendimaschera", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 70:
            messaggio("Hai trovato: Portafortuna", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 71:
            messaggio("Hai trovato: Batteria piccola", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 72:
            messaggio("Hai trovato: Batteria discreta", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 73:
            messaggio("Hai trovato: Batteria capiente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 74:
            messaggio("Hai trovato: Batteria enorme", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 75:
            messaggio("Hai trovato: Batteria illimitata", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro >= 81 and tesoro <= 100:
            messaggio("Hai trovato: Una nuova condizione", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro >= 101 and tesoro <= 120:
            messaggio("Hai trovato: Cella di memoria", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 131:
            messaggio("Hai trovato: 50 monete", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 132:
            messaggio("Hai trovato: 5 frecce", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)

    return animazioneRallo


def animaRaccoltaDenaro(x, y, vettoreDenaro, collana):
    denaroRaccolto = False
    i = 0
    while i < len(vettoreDenaro):
        if vettoreDenaro[i + 1] == x and vettoreDenaro[i + 2] == y:
            if canaleSoundPassiRallo.get_busy():
                canaleSoundPassiRallo.stop()
            denaroTrovato = vettoreDenaro[i]
            # effetto portafortuna
            if collana == 4:
                denaroTrovato += vettoreDenaro[i]
            schermo.blit(sfocontcof, (gsx // 32 * 0, gsy // 18 * 0))
            messaggio("Denaro trovato: " + str(denaroTrovato), grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            denaroRaccolto = True
            break
        i += 3
    return denaroRaccolto


def eliminaOggettoLanciato(x, y, attaccoADistanza, rx, ry, attaccoADistanzaRobo, nemicoAttaccante, schermo_prima_delle_animazioni, cambiosta, azioniDaEseguire, fineanimaz):
    # disegno il terreno sotto le frecce lanciate da Rallo
    if "attaccoRallo" in azioniDaEseguire and attaccoADistanza and not cambiosta:
        xInizioRetta = x
        xFineRetta = attaccoADistanza.vx
        yInizioRetta = y
        yFineRetta = attaccoADistanza.vy
        global quadrettoSottoLaFreccia
        if fineanimaz > 5:
            if fineanimaz != 10:
                schermo.blit(quadrettoSottoLaFreccia, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz) - gpx), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - gpy))
            quadrettoSottoLaFreccia = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)) - gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz)) - gpy, gpx * 3, gpy * 3))
        elif fineanimaz == 5:
            schermo.blit(quadrettoSottoLaFreccia, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz)) - gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - gpy))

    # disegno il terreno sotto gli oggetti lanciati dai nemici
    if "attaccoNemici" in azioniDaEseguire and nemicoAttaccante:
        if nemicoAttaccante.attaccaDaLontano and nemicoAttaccante.animaAttacco and not nemicoAttaccante.morto:
            xInizioRetta = nemicoAttaccante.x
            xFineRetta = nemicoAttaccante.xObbiettivo
            yInizioRetta = nemicoAttaccante.y
            yFineRetta = nemicoAttaccante.yObbiettivo
            if fineanimaz > 5:
                if fineanimaz != 10:
                    schermo.blit(nemicoAttaccante.quadrettoSottoOggettoLanciato, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz) - gpx), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - gpy))
                nemicoAttaccante.quadrettoSottoOggettoLanciato = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)) - gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz)) - gpy, gpx * 3, gpy * 3))
            elif fineanimaz == 5:
                schermo.blit(nemicoAttaccante.quadrettoSottoOggettoLanciato, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz)) - gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - gpy))


def disegnaCasellaAccantoAlPersCheAttacca(x, y, attacco, npers, rx, ry, nrob, nemicoAttaccante, schermo_prima_delle_animazioni, cambiosta, azioniDaEseguire, fineanimaz):
    if "attaccoRallo" in azioniDaEseguire and attacco == 1:
        global quadrettoSottoLaSpada
        xAttaccoPers = -gpx
        yAttaccoPers = -gpy
        # 1=d, 2=a, 3=w, 4=s
        if npers == 1:
            xAttaccoPers = x + gpx
            yAttaccoPers = y
        if npers == 2:
            xAttaccoPers = x - gpx
            yAttaccoPers = y
        if npers == 3:
            xAttaccoPers = x
            yAttaccoPers = y - gpy
        if npers == 4:
            xAttaccoPers = x
            yAttaccoPers = y + gpy
        if fineanimaz == 10:
            quadrettoSottoLaSpada = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xAttaccoPers, yAttaccoPers, gpx, gpy))
        else:
            schermo.blit(quadrettoSottoLaSpada, (xAttaccoPers, yAttaccoPers))

    if "attaccoNemici" in azioniDaEseguire and nemicoAttaccante and not cambiosta:
        if nemicoAttaccante.animaAttacco:
            xAttaccoNemico = 0
            yAttaccoNemico = 0
            if nemicoAttaccante.direzione == "w":
                xAttaccoNemico = nemicoAttaccante.x
                yAttaccoNemico = nemicoAttaccante.y - gpy
            if nemicoAttaccante.direzione == "a":
                xAttaccoNemico = nemicoAttaccante.x - gpx
                yAttaccoNemico = nemicoAttaccante.y
            if nemicoAttaccante.direzione == "s":
                xAttaccoNemico = nemicoAttaccante.x
                yAttaccoNemico = nemicoAttaccante.y + gpy
            if nemicoAttaccante.direzione == "d":
                xAttaccoNemico = nemicoAttaccante.x + gpx
                yAttaccoNemico = nemicoAttaccante.y
            if fineanimaz == 10:
                nemicoAttaccante.quadrettoSottoArma = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xAttaccoNemico, yAttaccoNemico, gpx, gpy))
            else:
                schermo.blit(nemicoAttaccante.quadrettoSottoArma, (xAttaccoNemico, yAttaccoNemico))


def animaFrecceLanciate(x, y, attaccoADistanza, rx, ry, attaccoADistanzaRobo, nemicoAttaccante, cambiosta, azioniDaEseguire, fineanimaz):
    # disegno le frecce lanciate da Rallo
    if "attaccoRallo" in azioniDaEseguire and attaccoADistanza and not cambiosta:
        xInizioRetta = x
        xFineRetta = attaccoADistanza.vx
        yInizioRetta = y
        yFineRetta = attaccoADistanza.vy
        deltaXRetta = xFineRetta - xInizioRetta
        deltaYRetta = yFineRetta - yInizioRetta
        angoloInRadianti = -math.atan2(deltaYRetta, deltaXRetta)
        angoloInGradi = math.degrees(angoloInRadianti)
        imgFrecciaLanciata_temp = pygame.transform.rotate(imgFrecciaLanciata, angoloInGradi)
        if fineanimaz > 5:
            schermo.blit(imgFrecciaLanciata_temp, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz))))

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
                schermo.blit(imgFrecciaLanciata_temp, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz))))
            elif fineanimaz != 0:
                schermo.blit(nemicoAttaccante.imgDanneggiamentoOggettoLanciato, (xFineRetta, yFineRetta))


def animaVitaRalloNemicoInquadrato(dati, nemicoInquadrato, vitaesca, difesa):
    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati, difesa)

    # vita-status personaggio
    lungvitatot = int(((gpx * pvtot) / float(4)) // 5)
    lungvita = (lungvitatot * dati[5]) // pvtot
    if lungvita < 0:
        lungvita = 0
    indvitapers = pygame.transform.scale(indvita, (lungvitatot, gpy // 4))
    fineindvitapers = pygame.transform.scale(fineindvita, (gpx // 12, gpy // 4))
    vitaral = pygame.transform.scale(vitapersonaggio, (lungvita, gpy // 4))
    schermo.blit(sfondoRallo, (gsx // 32 * 0, gsy // 18 * 17))
    schermo.blit(indvitapers, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 4 * 3)))
    schermo.blit(fineindvitapers, ((gsx // 32 * 1) + lungvitatot, (gsy // 18 * 17) + (gpy // 4 * 3)))
    schermo.blit(vitaral, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 4 * 3)))
    persbat = pygame.transform.scale(perso, (gpx, gpy))
    schermo.blit(persbat, (gsx // 32 * 0, gsy // 18 * 17))
    schermo.blit(perssb, (gsx // 32 * 0, gsy // 18 * 17))
    schermo.blit(imgNumFrecce, (int(gsx // 32 * 1.2), gsy // 18 * 17))
    messaggio("x " + str(dati[132]), grigiochi, int(gsx // 32 * 1.8), int(gsy // 18 * 17.2), 40)
    if dati[121]:
        schermo.blit(avvelenato, (gsx // 32 * 3, gsy // 18 * 17))
    if dati[123] > 0:
        schermo.blit(attaccopiu, (gsx // 32 * 4, gsy // 18 * 17))
    if dati[121] > 0:
        schermo.blit(difesapiu, (gsx // 32 * 5, gsy // 18 * 17))
    # disegno la vita del mostro / Colco / esca selezionato
    if nemicoInquadrato == "Colco":
        lungentot = int(((gpx * entot) / float(4)) // 15)
        lungen = int(((gpx * dati[10]) / float(4)) // 15)
        if lungen < 0:
            lungen = 0
        indvitarob = pygame.transform.scale(indvita, (lungentot, gpy // 4))
        fineindvitarob = pygame.transform.scale(fineindvita, (gpx // 12, gpy // 4))
        vitarob = pygame.transform.scale(vitarobo, (lungen, gpy // 4))
        schermo.blit(sfondoColco, (0, 0))
        schermo.blit(indvitarob, (gpx, 0))
        schermo.blit(fineindvitarob, (gpx + lungentot, 0))
        schermo.blit(vitarob, (gpx, 0))
        robobat = pygame.transform.scale(roboo, (gpx, gpy))
        schermo.blit(robobat, (0, 0))
        if dati[122] > 0:
            schermo.blit(surriscaldato, (gpx + (gpx // 8), gpy // 4))
        if dati[125] > 0:
            schermo.blit(velocitapiu, ((gpx * 2) + (gpx // 8), gpy // 4))
        if dati[126] > 0:
            schermo.blit(efficienzapiu, ((gpx * 3) + (gpx // 8), gpy // 4))
    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
        idEscaInquadrata = int(nemicoInquadrato[4:])
        i = 0
        while i < len(vitaesca):
            if idEscaInquadrata == vitaesca[i]:
                lungvita = (gpx * 8 * vitaesca[i + 1]) // 100
                if lungvita < 0:
                    lungvita = 0
                schermo.blit(sfondoEsche, (0, 0))
                schermo.blit(esche, (0, 0))
                indvitamost = pygame.transform.scale(indvita, (gpx * 8, gpy // 4))
                fineindvitamost = pygame.transform.scale(fineindvita, (gpx // 12, gpy // 4))
                vitaesche = pygame.transform.scale(vitanemico0, (lungvita, gpy // 4))
                schermo.blit(indvitamost, (gpx, 0))
                schermo.blit(fineindvitamost, (gpx + (gpx * 8), 0))
                schermo.blit(vitaesche, (gpx, 0))
                break
            i += 4
    elif nemicoInquadrato and not type(nemicoInquadrato) is str:
        pvm = nemicoInquadrato.vita
        pvmtot = nemicoInquadrato.vitaTotale
        schermo.blit(sfondoMostro, (0, 0))
        if nemicoInquadrato.avvelenato:
            schermo.blit(avvelenato, (gpx + (gpx // 8), gpy // 4))
        if nemicoInquadrato.appiccicato:
            schermo.blit(appiccicoso, ((gpx * 2) + (gpx // 8), gpy // 4))
        schermo.blit(nemicoInquadrato.imgS, (0, 0))
        fineindvitamost = pygame.transform.scale(fineindvita, (gpx // 12, gpy // 4))
        if pvmtot > 1500:
            indvitamost = pygame.transform.scale(indvita, (int(((gpx * 1500) / float(4)) // 15), gpy // 4))
            lungvitatot = int(((gpx * 1500) / float(4)) // 15)
            schermo.blit(fineindvitamost, (gpx + lungvitatot, 0))
            if pvm > 15000:
                pvm = 1500
                vitanemsucc = pygame.transform.scale(vitanemico00, (int(((gpx * 1500) / float(4)) // 15), gpy // 4))
                vitanemico = vitanemico9
            elif pvm > 13500:
                pvm -= 13500
                vitanemsucc = pygame.transform.scale(vitanemico8, (int(((gpx * 1500) / float(4)) // 15), gpy // 4))
                vitanemico = vitanemico9
            elif pvm > 12000:
                pvm -= 12000
                vitanemsucc = pygame.transform.scale(vitanemico7, (int(((gpx * 1500) / float(4)) // 15), gpy // 4))
                vitanemico = vitanemico8
            elif pvm > 10500:
                pvm -= 10500
                vitanemsucc = pygame.transform.scale(vitanemico6, (int(((gpx * 1500) / float(4)) // 15), gpy // 4))
                vitanemico = vitanemico7
            elif pvm > 9000:
                pvm -= 9000
                vitanemsucc = pygame.transform.scale(vitanemico5, (int(((gpx * 1500) / float(4)) // 15), gpy // 4))
                vitanemico = vitanemico6
            elif pvm > 7500:
                pvm -= 7500
                vitanemsucc = pygame.transform.scale(vitanemico4, (int(((gpx * 1500) / float(4)) // 15), gpy // 4))
                vitanemico = vitanemico5
            elif pvm > 6000:
                pvm -= 6000
                vitanemsucc = pygame.transform.scale(vitanemico3, (int(((gpx * 1500) / float(4)) // 15), gpy // 4))
                vitanemico = vitanemico4
            elif pvm > 4500:
                pvm -= 4500
                vitanemsucc = pygame.transform.scale(vitanemico2, (int(((gpx * 1500) / float(4)) // 15), gpy // 4))
                vitanemico = vitanemico3
            elif pvm > 3000:
                pvm -= 3000
                vitanemsucc = pygame.transform.scale(vitanemico1, (int(((gpx * 1500) / float(4)) // 15), gpy // 4))
                vitanemico = vitanemico2
            elif pvm > 1500:
                pvm -= 1500
                vitanemsucc = pygame.transform.scale(vitanemico0, (int(((gpx * 1500) / float(4)) // 15), gpy // 4))
                vitanemico = vitanemico1
            else:
                vitanemsucc = pygame.transform.scale(vitanemico00, (int(((gpx * 1500) / float(4)) // 15), gpy // 4))
                vitanemico = vitanemico0
        else:
            lungvitatot = int(((gpx * pvmtot) / float(4)) // 15)
            indvitamost = pygame.transform.scale(indvita, (lungvitatot, gpy // 4))
            schermo.blit(fineindvitamost, (gpx + lungvitatot, 0))
            vitanemsucc = pygame.transform.scale(vitanemico00, (lungvitatot, gpy // 4))
            vitanemico = vitanemico0
        lungvita = int(((gpx * pvm) / float(4)) // 15)
        if lungvita < 0:
            lungvita = 0
        vitanem = pygame.transform.scale(vitanemico, (lungvita, gpy // 4))
        schermo.blit(indvitamost, (gpx, 0))
        schermo.blit(vitanemsucc, (gpx, 0))
        schermo.blit(vitanem, (gpx, 0))


def anima(sposta, x, y, vx, vy, rx, ry, vrx, vry, pers, robot, npers, nrob, primopasso, cambiosta, sfondinoa, sfondinob, scudo, armatura, arma, armaMov1, armaMov2, armaAttacco, scudoDifesa, arco, faretra, arcoAttacco, guanti, guantiMov1, guantiMov2, guantiAttacco, guantiDifesa, collana, armaS, armaturaS, arcoS, faretraS, collanaS, armrob, dati, attacco, difesa, tastop, tesoro, sfondinoc, aumentoliv, carim, caricaTutto, listaNemici, vitaesca, vettoreDenaro, attaccoADistanza, caseviste, porte, cofanetti, portaOriz, portaVert, numStanza, attaccoADistanzaRobo, tecnicaUsata, nemicoInquadrato):
    schermo_prima_delle_animazioni = schermo.copy()

    azioniPossibili = ["attaccoColco", "movimentoColcoNemici", "attaccoNemici", "aumentaLv"]
    azioniDaEseguire = []
    if sposta and attacco != 0:
        azioniDaEseguire.append("attaccoRallo")
    elif sposta:
        azioniDaEseguire.append("movimentoRallo")
    if sposta and attacco == 0 and not cambiosta and tecnicaUsata and tecnicaUsata == "spostamento":
        azioniPossibili.remove("attaccoColco")
        azioniPossibili.remove("movimentoColcoNemici")
        azioniDaEseguire.append("movimentoColcoNemici")
    elif not sposta and not cambiosta:
        if tecnicaUsata and tecnicaUsata != "spostamento":
            azioniDaEseguire.append("attaccoColco")
            azioniPossibili.remove("attaccoColco")
        else:
            azioniPossibili.remove("attaccoColco")
            azioniPossibili.remove("movimentoColcoNemici")
            spostamentoNemico = False
            for nemico in listaNemici:
                if nemico.animaSpostamento or nemico.animaMorte:
                    spostamentoNemico = True
                    break
            if spostamentoNemico or (tecnicaUsata and tecnicaUsata == "spostamento"):
                azioniDaEseguire.append("movimentoColcoNemici")
            else:
                attaccoNemico = False
                for nemico in listaNemici:
                    if nemico.animaAttacco:
                        attaccoNemico = True
                        break
                if attaccoNemico:
                    azioniDaEseguire.append("attaccoNemici")
    if len(azioniDaEseguire) == 0 and aumentoliv and "aumentaLv" in azioniPossibili:
        azioniDaEseguire.append("aumentaLv")
        azioniPossibili.remove("aumentaLv")

    denaroRaccolto = False
    animazioneRalloFatta = False
    animazioneColcoFatta = False
    for nemico in listaNemici:
        nemico.animazioneFatta = False
    while len(azioniDaEseguire) > 0:
        # viene fatto un ciclo in più alla fine (senza clock) per ripulire le immagini delle animazioni rimaste (altrimenti le ultime non verrebbero cancellate)
        animazioneRallo = False
        animazioneColco = False
        animazioneNemici = False
        nemicoAttaccante = False
        if "attaccoNemici" in azioniDaEseguire:
            for nemico in listaNemici:
                if nemico.animaAttacco and not nemico.animazioneFatta:
                    nemicoAttaccante = nemico
        fineanimaz = 10
        while fineanimaz >= 0:
            # ridisegnare il quadratino dove sono i personaggi
            if cambiosta:
                if fineanimaz == 10:
                    if ((x / gpx) + (y / gpy)) % 2 == 0:
                        schermo.blit(sfondinob, (vx, vy))
                    if ((x / gpx) + (y / gpy)) % 2 == 1:
                        schermo.blit(sfondinoa, (vx, vy))
            else:
                if ((x / gpx) + (y / gpy)) % 2 == 0:
                    schermo.blit(sfondinob, (vx, vy))
                    schermo.blit(sfondinoa, (x, y))
                if ((x / gpx) + (y / gpy)) % 2 == 1:
                    schermo.blit(sfondinoa, (vx, vy))
                    schermo.blit(sfondinob, (x, y))
                if ((rx / gpx) + (ry / gpy)) % 2 == 0:
                    schermo.blit(sfondinob, (vrx, vry))
                    schermo.blit(sfondinoa, (rx, ry))
                if ((rx / gpx) + (ry / gpy)) % 2 == 1:
                    schermo.blit(sfondinoa, (vrx, vry))
                    schermo.blit(sfondinob, (rx, ry))
                for nemico in listaNemici:
                    if nemico.inCasellaVista:
                        if ((nemico.x / gpx) + (nemico.y / gpy)) % 2 == 0:
                            schermo.blit(sfondinob, (nemico.vx, nemico.vy))
                            schermo.blit(sfondinoa, (nemico.x, nemico.y))
                        if ((nemico.x / gpx) + (nemico.y / gpy)) % 2 == 1:
                            schermo.blit(sfondinoa, (nemico.vx, nemico.vy))
                            schermo.blit(sfondinob, (nemico.x, nemico.y))

            # disegno le esche e il denaro
            animaEsche(vitaesca, caseviste, sfondinoa, sfondinob)
            animaDenaro(vettoreDenaro, caseviste, sfondinoa, sfondinob)
            animaCofanetti(cofanetti, caseviste, sfondinoc)
            animaPorte(porte, cofanetti, numStanza, portaOriz, portaVert, sfondinoc)

            if fineanimaz == 10:
                schermo_prima_delle_animazioni = schermo.copy()
            eliminaOggettoLanciato(x, y, attaccoADistanza, rx, ry, attaccoADistanzaRobo, nemicoAttaccante, schermo_prima_delle_animazioni, cambiosta, azioniDaEseguire, fineanimaz)
            disegnaCasellaAccantoAlPersCheAttacca(x, y, attacco, npers, rx, ry, nrob, nemicoAttaccante, schermo_prima_delle_animazioni, cambiosta, azioniDaEseguire, fineanimaz)

            # disegna personaggi se ci sono animazioni ma non loro
            animaColcoFermo(rx, ry, vrx, vry, robot, armrob, dati[122], tecnicaUsata, azioniDaEseguire, animazioneColcoFatta, fineanimaz)
            animaNemiciFermi(listaNemici, azioniDaEseguire, cambiosta, nemicoAttaccante, fineanimaz)
            animaRalloFermo(x, y, vx, vy, npers, pers, scudo, armatura, arma, arco, faretra, guanti, collana, dati[121], azioniDaEseguire, animazioneRalloFatta, nemicoAttaccante, difesa, fineanimaz)

            # tolgo il rumore passi quando non c'è l'animazione
            if not "movimentoRallo" in azioniDaEseguire and canaleSoundPassiRallo.get_busy():
                canaleSoundPassiRallo.stop()
            # animazione difesa Rallo
            animazioneRallo = animaDifesaRallo(sposta, x, y, armaS, armaturaS, arcoS, faretraS, collanaS, scudoDifesa, guantiDifesa, dati[121], difesa, animazioneRallo, nemicoAttaccante, fineanimaz)

            if "aumentaLv" in azioniDaEseguire:
                # animazione aumento di livello
                animazioneRallo, caricaTutto, tastop = animaLvUp(x, y, npers, pers, arma, armatura, scudo, collana, arco, faretra, guanti, dati[4], aumentoliv, carim, caricaTutto, tastop, animazioneRallo, fineanimaz)

            # con movimentoColcoNemici vengono eseguite le animazioni di: movimento colco, movimento nemici, morti nemici
            if "movimentoColcoNemici" in azioniDaEseguire:
                # animazione camminata robo
                animazioneColco = animaCamminataRobo(nrob, rx, ry, vrx, vry, armrob, dati[122], cambiosta, animazioneColco, fineanimaz)
                # animazione camminata mostri
                animazioneNemici = animaSpostamentoNemici(listaNemici, animazioneNemici, cambiosta, fineanimaz)
                # animazione morte nemici
                animazioneNemici = animaMorteNemici(listaNemici, animazioneNemici, cambiosta, fineanimaz)

            if "movimentoRallo" in azioniDaEseguire:
                # animazione camminata personaggio
                animazioneRallo, primopasso = animaCamminataRallo(sposta, x, y, vx, vy, primopasso, cambiosta, npers, scudo, armatura, armaMov1, armaMov2, arco, faretra, guantiMov1, guantiMov2, collana, dati[121], attacco, difesa, tastop, animazioneRallo, fineanimaz)

            # con attaccoNemici vengono eseguite le animazioni di: frecce nemici, attacco nemici
            if "attaccoNemici" in azioniDaEseguire:
                # animazione attacco nemici
                animaFrecceLanciate(x, y, attaccoADistanza, rx, ry, attaccoADistanzaRobo, nemicoAttaccante, cambiosta, azioniDaEseguire, fineanimaz)
                animazioneNemici = animaAttaccoNemici(nemicoAttaccante, animazioneNemici, fineanimaz)

            if "attaccoRallo" in azioniDaEseguire:
                # animazione attacco Rallo
                animaFrecceLanciate(x, y, attaccoADistanza, rx, ry, attaccoADistanzaRobo, listaNemici, cambiosta, azioniDaEseguire, fineanimaz)
                animazioneRallo = animaAttaccoRallo(sposta, x, y, npers, pers, scudo, armatura, collana, arco, faretra, armaAttacco, arcoAttacco, guantiAttacco, dati[121], attacco, difesa, animazioneRallo, attaccoADistanza, fineanimaz)

                # animazione danneggiamento dei nemici
                animazioneNemici = animaDanneggiamentoNemici(listaNemici, animazioneNemici, cambiosta, azioniDaEseguire, "Rallo")

            if "attaccoColco" in azioniDaEseguire:
                # animazione attacco Colco
                animaFrecceLanciate(x, y, attaccoADistanza, rx, ry, attaccoADistanzaRobo, listaNemici, cambiosta, azioniDaEseguire, fineanimaz)

                # animazione danneggiamento dei nemici
                animazioneNemici = animaDanneggiamentoNemici(listaNemici, animazioneNemici, cambiosta, azioniDaEseguire, "Colco")

            # animazione apertura cofanetto
            animazioneRallo = animaAperturaCofanetto(tesoro, x, y, npers, pers, dati[121], armatura, arma, scudo, collana, arco, faretra, guanti, sfondinoc, animazioneRallo)
            # anima raccolta denaro
            denaroRaccolto = animaRaccoltaDenaro(x, y, vettoreDenaro, dati[130])

            if animazioneRallo:
                animazioneRalloFatta = True
            if animazioneColco:
                animazioneColcoFatta = True

            pygame.event.pump()
            if (animazioneNemici or animazioneRallo or animazioneColco) and fineanimaz > 0:
                pygame.display.update()
                clockAnimazioni.tick(fpsAnimazioni)
                # print (clockAnimazioni.get_fps())
            fineanimaz -= 1

        animaVitaRalloNemicoInquadrato(dati, nemicoInquadrato, vitaesca, difesa)

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
                if (spostamentoNemico or tecnicaUsata == "spostamento") and "movimentoColcoNemici" in azioniPossibili:
                    azioniDaEseguire.append("movimentoColcoNemici")
                    azioniPossibili.remove("movimentoColcoNemici")
                else:
                    if "movimentoColcoNemici" in azioniPossibili:
                        azioniPossibili.remove("movimentoColcoNemici")
                    attaccoNemico = False
                    for nemico in listaNemici:
                        if not nemico.animazioneFatta and nemico.animaAttacco:
                            attaccoNemico = True
                            break
                    if attaccoNemico and "attaccoNemici" in azioniPossibili:
                        azioniDaEseguire.append("attaccoNemici")
        if len(azioniDaEseguire) == 0 and aumentoliv and "aumentaLv" in azioniPossibili:
            azioniDaEseguire.append("aumentaLv")
            azioniPossibili.remove("aumentaLv")

    if tesoro != -1:
        pygame.display.update()
        risposta = False
        while not risposta:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        canaleSoundPuntatore.play(selezione)
                        risposta = True
        caricaTutto = True
        tesoro = -1
    if denaroRaccolto:
        pygame.display.update()
        risposta = False
        while not risposta:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        canaleSoundPuntatore.play(selezione)
                        risposta = True
        caricaTutto = True
        tastop = 0

    return primopasso, caricaTutto, tesoro, tastop
