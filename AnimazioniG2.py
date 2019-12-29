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


def animaCamminataRallo(sposta, x, y, vx, vy, primopasso, cambiosta, npers, scudo, armatura, armaMov1, armaMov2, arco, faretra, guantiMov1, guantiMov2, collana, avvele, attacco, difesa, tastop, animazione, aumentoliv, fineanimaz):
    animazCamminataBreve = False
    if sposta and not aumentoliv:
        # mentre ci si sposta
        if x != vx or y != vy:
            animazione = True
            if not canaleSoundPassiRallo.get_busy():
                canaleSoundPassiRallo.play(rumorecamminata)
            if primopasso and not cambiosta:
                primopasso = False
            # camminata quando si entra in una stanza
            if cambiosta:
                animazCamminataBreve = True
                animaCamminataRalloCambiosta(npers, x, y, scudo, armatura, armaMov1, arco, faretra, guantiMov1, collana, avvele, fineanimaz)
            # camminata quando non si entra in una stanza
            else:
                animaCamminataRalloSpostato(npers, x, y, scudo, armatura, armaMov1, armaMov2, arco, faretra, guantiMov1, guantiMov2, collana, avvele, fineanimaz)
        # mentre non ci si sposta
        elif attacco == 0 and not difesa and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
            animazione = True
            if not canaleSoundPassiRallo.get_busy():
                canaleSoundPassiRallo.play(rumorecamminata)
            if primopasso:
                primopasso = False
            animaCamminataRalloFermo(npers, x, y, scudo, armatura, armaMov1, armaMov2, arco, faretra, guantiMov1, guantiMov2, collana, avvele, fineanimaz)
    else:
        canaleSoundPassiRallo.stop()
    return animazione, primopasso, animazCamminataBreve


def animaAttaccoDifesaRallo(sposta, x, y, npers, pers, scudo, armatura, collana, arco, faretra, guanti, armaS, armaturaS, arcoS, faretraS, guantiS, collanaS, armaAttacco, arcoAttacco, guantiAttacco, scudoDifesa, guantiDifesa, avvele, attacco, difesa, animazioneRallo, animazione, aumentoliv, attaccoADistanza, fineanimaz):
    if sposta:
        if attacco == 1 and difesa == 0:
            animazioneRallo = True
            if attaccoADistanza:
                if fineanimaz == 10 and not canaleSoundAttacco.get_busy():
                    canaleSoundAttacco.play(rumoreAttaccoArco)
                if not aumentoliv:
                    disegnaRallo(npers, x, y, avvele, pers, armaAttacco, armatura, scudo, collana, arcoAttacco, faretra, guantiAttacco, False, False, False, True)
            else:
                if fineanimaz == 10 and not canaleSoundAttacco.get_busy():
                    canaleSoundAttacco.play(rumoreAttaccoSpada)
                if not aumentoliv:
                    disegnaRallo(npers, x, y, avvele, pers, armaAttacco, armatura, scudo, collana, arco, faretra, guantiAttacco, False, False, True)
        if difesa != 0 and not aumentoliv:
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
    elif not sposta and not aumentoliv and difesa != 0 and animazione:
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


def animaLvUp(npers, x, y, pers, scudo, armatura, arma, arco, faretra, guanti, collana, liv, aumentoliv, carim, animazione, caricaTutto, tastop, fineanimaz):
    if aumentoliv and not carim:
        animazione = True
        if not canaleSoundLvUp.get_busy() and fineanimaz > 1:
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
    return animazione, caricaTutto, tastop


def animaRalloFermo(x, y, npers, pers, scudo, armatura, arma, arco, faretra, guanti, collana, avvele, animazioneRallo):
    if not animazioneRallo:
        disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)


def animaCamminataRobo(nrob, rx, ry, vrx, vry, armrob, surriscalda, cambiosta, animazione, robot, fineanimaz):
    if (rx != vrx or ry != vry) and not cambiosta:
        animazione = True
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
    else:
        schermo.blit(robot, (rx, ry))
        if surriscalda > 0:
            schermo.blit(roboSurrisc, (rx, ry))
        schermo.blit(armrob, (rx, ry))
    return animazione


def animaSpostamentoNemici(listaNemici, animazione, cambiosta, fineanimaz):
    if not cambiosta:
        for nemico in listaNemici:
            if nemico.animaSpostamento and not nemico.morto and (nemico.x != nemico.vx or nemico.y != nemico.vy):
                animazione = True
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
    return animazione


def animaAttaccoNemici(listaNemici, animazione, cambiosta, fineanimaz):
    if not cambiosta:
        for nemico in listaNemici:
            if nemico.animaAttacco and not nemico.morto:
                animazione = True
                # if fineanimaz == 10 and not canaleSoundAttacco.get_busy():
                #     canaleSoundAttacco.play(rumoreattacco)
                if nemico.attaccaDaLontano:
                    if nemico.direzione == "w":
                        schermo.blit(nemico.imgAttaccoW, (nemico.x, nemico.y))
                    if nemico.direzione == "a":
                        schermo.blit(nemico.imgAttaccoA, (nemico.x, nemico.y))
                    if nemico.direzione == "s":
                        schermo.blit(nemico.imgAttaccoS, (nemico.x, nemico.y))
                    if nemico.direzione == "d":
                        schermo.blit(nemico.imgAttaccoD, (nemico.x, nemico.y))
                    if nemico.appiccicato:
                        schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y))
                    if nemico.avvelenato:
                        schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y))
                    print "animazione attacco da lontano: x=" + str(nemico.xObbiettivo) + " y=" + str(nemico.yObbiettivo)
                else:
                    # rumoreattaccoNemico.play()
                    if nemico.direzione == "w":
                        schermo.blit(nemico.imgAttaccoW, (nemico.x, nemico.y - gpy))
                    if nemico.direzione == "a":
                        schermo.blit(nemico.imgAttaccoA, (nemico.x - gpx, nemico.y))
                    if nemico.direzione == "s":
                        schermo.blit(nemico.imgAttaccoS, (nemico.x, nemico.y))
                    if nemico.direzione == "d":
                        schermo.blit(nemico.imgAttaccoD, (nemico.x, nemico.y))
                    if nemico.appiccicato:
                        schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y))
                    if nemico.avvelenato:
                        schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y))
    return animazione


def animaMorteNemici(listaNemici, animazione, cambiosta, fineanimaz):
    if not cambiosta:
        for nemico in listaNemici:
            if nemico.animaMorte and nemico.morto:
                animazione = True
                if 5 <= fineanimaz <= 10:
                    schermo.blit(nemico.imgMorte1, (nemico.x, nemico.y))
                if 1 < fineanimaz <= 5:
                    schermo.blit(nemico.imgMorte2, (nemico.x, nemico.y))
    return animazione


def animaDanneggiamentoNemici(listaNemici, animazione, cambiosta, fineanimaz):
    if not cambiosta:
        for nemico in listaNemici:
            if nemico.animaDanneggiamento and not nemico.morto:
                if not nemico.animaAttacco and not nemico.animaSpostamento:
                    schermo.blit(nemico.imgAttuale, (nemico.x, nemico.y))
                animazione = True
                if nemico.animaDanneggiamento == "Rallo":
                    schermo.blit(nemico.imgDanneggiamentoRallo, (nemico.vx, nemico.vy))
                if nemico.animaDanneggiamento == "Colco":
                    schermo.blit(nemico.imgDanneggiamentoColco, (nemico.vx, nemico.vy))
                if nemico.appiccicato:
                    schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y))
                if nemico.avvelenato:
                    schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y))
    return animazione


def animaCofanetto(tesoro, x, y, npers, pers, avvele, armatura, arma, scudo, collana, arco, faretra, guanti, sfondinoc, caricaTutto):
    if tesoro != -1:
        schermo.blit(sfocontcof, (gsx // 32 * 0, gsy // 18 * 0))
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
        pygame.display.update()
        pygame.time.wait(500)
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

    return caricaTutto, tesoro


def animaEsche(vitaesca, sfondinoa, sfondinob):
    i = 0
    while i < len(vitaesca):
        if ((vitaesca[i + 2] / gpx) + (vitaesca[i + 3] / gpy)) % 2 == 0:
            schermo.blit(sfondinoa, (vitaesca[i + 2], vitaesca[i + 3]))
        if ((vitaesca[i + 2] / gpx) + (vitaesca[i + 3] / gpy)) % 2 == 1:
            schermo.blit(sfondinob, (vitaesca[i + 2], vitaesca[i + 3]))
        schermo.blit(esche, (vitaesca[i + 2], vitaesca[i + 3]))
        i += 4


def animaDenaro(vettoreDenaro, sfondinoa, sfondinob):
    i = 0
    while i < len(vettoreDenaro):
        if ((vettoreDenaro[i + 1] / gpx) + (vettoreDenaro[i + 2] / gpy)) % 2 == 0:
            schermo.blit(sfondinoa, (vettoreDenaro[i + 1], vettoreDenaro[i + 2]))
        if ((vettoreDenaro[i + 1] / gpx) + (vettoreDenaro[i + 2] / gpy)) % 2 == 1:
            schermo.blit(sfondinob, (vettoreDenaro[i + 1], vettoreDenaro[i + 2]))
        schermo.blit(sacchettoDenaro, (vettoreDenaro[i + 1], vettoreDenaro[i + 2]))
        i += 3


def animaRaccoltaDenaro(x, y, vettoreDenaro, collana, caricaTutto, tastop, fineanimaz):
    if fineanimaz == 1:
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
                break
            i += 3
    return caricaTutto, tastop


def animaFrecceLanciate(x, y, attaccoADistanza, schermo_prima_delle_animazioni, fineanimaz):
    # disegno le frecce lanciate
    if attaccoADistanza:
        xInizioRetta = x
        xFineRetta = attaccoADistanza.vx
        yInizioRetta = y
        yFineRetta = attaccoADistanza.vy
        deltaXRetta = xFineRetta - xInizioRetta
        deltaYRetta = yFineRetta - yInizioRetta
        angoloInRadianti = -math.atan2(deltaYRetta, deltaXRetta)
        angoloInGradi = math.degrees(angoloInRadianti)
        imgFrecciaLanciata_temp = pygame.transform.rotate(imgFrecciaLanciata, angoloInGradi)
        global quadrettoSottoLaFreccia
        if fineanimaz > 5:
            if fineanimaz != 10:
                schermo.blit(quadrettoSottoLaFreccia, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz) - gpx), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - gpy))
            quadrettoSottoLaFreccia = schermo_prima_delle_animazioni.subsurface(pygame.Rect(xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)) - gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz)) - gpy, gpx * 3, gpy * 3))
            schermo.blit(imgFrecciaLanciata_temp, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (10 - fineanimaz)), yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (10 - fineanimaz))))
        elif fineanimaz == 5:
            schermo.blit(quadrettoSottoLaFreccia, (xInizioRetta + ((xFineRetta - xInizioRetta) // 5 * (9 - fineanimaz)) - gpx, yInizioRetta + ((yFineRetta - yInizioRetta) // 5 * (9 - fineanimaz)) - gpy))


def scriviDannoInflitto(listaNemici, fineanimaz):
    if fineanimaz > 0:
        for nemico in listaNemici:
            i = len(nemico.danniRicevuti) - 1
            while i >= 0:
                messaggio("-" + str(nemico.danniRicevuti[i]), bianco, nemico.x - (gpx // 3), nemico.y - (gpy // 3 * (i + 1)), 40)
                i -= 1


def cancellaDanniInflitti(listaNemici, schermo_prima_delle_animazioni, fineanimaz):
    if fineanimaz == 0:
        for nemico in listaNemici:
            i = len(nemico.danniRicevuti) - 1
            while i >= 0:
                del nemico.danniRicevuti[i]
                schermo.blit(schermo_prima_delle_animazioni.subsurface(pygame.Rect(nemico.x - (gpx // 3), nemico.y - (gpy // 3 * 3), gpx * 2, gpy * 2)), (nemico.x - (gpx // 3), nemico.y - (gpy // 3 * 3)))
                i -= 1


def anima(sposta, x, y, vx, vy, rx, ry, vrx, vry, pers, robot, npers, nrob, primopasso, cambiosta, sfondinoa, sfondinob, scudo, armatura, arma, armaMov1, armaMov2, armaAttacco, scudoDifesa, arco, faretra, arcoAttacco, guanti, guantiMov1, guantiMov2, guantiAttacco, guantiDifesa, collana, armaS, armaturaS, arcoS, faretraS, guantiS, collanaS, armrob, dati, attacco, difesa, tastop, tesoro, sfondinoc, aumentoliv, carim, caricaTutto, listaNemici, vitaesca, vettoreDenaro, attaccoADistanza):
    animazione = False
    animazioneRallo = False
    schermo_prima_delle_animazioni = schermo.copy()
    # viene fatto un ciclo in più alla fine (senza clock) per ripulire le immagini delle animazioni rimaste (altrimenti le ultime non verrebbero cancellate)
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
                if nemico.animaSpostamento or nemico.animaAttacco or nemico.animaMorte or nemico.animaDanneggiamento:
                    if ((nemico.x / gpx) + (nemico.y / gpy)) % 2 == 0:
                        schermo.blit(sfondinob, (nemico.vx, nemico.vy))
                        schermo.blit(sfondinoa, (nemico.x, nemico.y))
                    if ((nemico.x / gpx) + (nemico.y / gpy)) % 2 == 1:
                        schermo.blit(sfondinoa, (nemico.vx, nemico.vy))
                        schermo.blit(sfondinob, (nemico.x, nemico.y))

        # disegno le esche e il denaro
        animaEsche(vitaesca, sfondinoa, sfondinob)
        animaDenaro(vettoreDenaro, sfondinoa, sfondinob)

        if fineanimaz == 10:
            schermo_prima_delle_animazioni = schermo.copy()

        # all'ultimo frame cancello tutti i numeri che indicano i danni inflitti
        cancellaDanniInflitti(listaNemici, schermo_prima_delle_animazioni, fineanimaz)

        # animazioni di tutte le frecce lanciate nel turno
        animaFrecceLanciate(x, y, attaccoADistanza, schermo_prima_delle_animazioni, fineanimaz)

        # animazione camminata robo
        animazione = animaCamminataRobo(nrob, rx, ry, vrx, vry, armrob, dati[122], cambiosta, animazione, robot, fineanimaz)
        # animazione camminata personaggio
        animazioneRallo, primopasso, animazCamminataBreve = animaCamminataRallo(sposta, x, y, vx, vy, primopasso, cambiosta, npers, scudo, armatura, armaMov1, armaMov2, arco, faretra, guantiMov1, guantiMov2, collana, dati[121], attacco, difesa, tastop, animazioneRallo, aumentoliv, fineanimaz)
        # animazione camminata mostri
        animazione = animaSpostamentoNemici(listaNemici, animazione, cambiosta, fineanimaz)

        # animazione morte nemici
        animazione = animaMorteNemici(listaNemici, animazione, cambiosta, fineanimaz)

        # animazione attacco personaggio (ultima animazione perchè per animare la difesa devo sapere se sono in corso altre animazioni)
        animazioneRallo = animaAttaccoDifesaRallo(sposta, x, y, npers, pers, scudo, armatura, collana, arco, faretra, guanti, armaS, armaturaS, arcoS, faretraS, guantiS, collanaS, armaAttacco, arcoAttacco, guantiAttacco, scudoDifesa, guantiDifesa, dati[121], attacco, difesa, animazioneRallo, animazione, aumentoliv, attaccoADistanza, fineanimaz)

        # animazione attacco nemici
        animazione = animaAttaccoNemici(listaNemici, animazione, cambiosta, fineanimaz)

        # animazione danneggiamento dei nemici
        animazione = animaDanneggiamentoNemici(listaNemici, animazione, cambiosta, fineanimaz)

        # animazione apertura cofanetto
        caricaTutto, tesoro = animaCofanetto(tesoro, x, y, npers, pers, dati[121], armatura, arma, scudo, collana, arco, faretra, guanti, sfondinoc, caricaTutto)

        # animazione aumento di livello
        animazioneRallo, caricaTutto, tastop = animaLvUp(npers, x, y, pers, scudo, armatura, arma, arco, faretra, guanti, collana, dati[4], aumentoliv, carim, animazioneRallo, caricaTutto, tastop, fineanimaz)

        # anima raccolta denaro
        caricaTutto, tastop = animaRaccoltaDenaro(x, y, vettoreDenaro, dati[130], caricaTutto, tastop, fineanimaz)

        # disegna Rallo se ci sono animazioni ma non di Rallo
        animaRalloFermo(x, y, npers, pers, scudo, armatura, arma, arco, faretra, guanti, collana, dati[121], animazioneRallo)

        # scrivo i danni infilli e ricevuti sopra le img dei personaggi
        scriviDannoInflitto(listaNemici, fineanimaz)

        fineanimaz -= 1
        pygame.event.pump()
        if (animazione or animazioneRallo) and fineanimaz > -1:
            pygame.display.update()
            clockAnimazioni.tick(fpsAnimazioni)
            #print (clockAnimazioni.get_fps())

    return primopasso, caricaTutto, tesoro, tastop
