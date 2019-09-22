# -*- coding: utf-8 -*-

from GenericFuncG2 import *


def animaPersCambiosta(npers, x, y, vx, vy, scudo, armatura, arma, avvele, fineanimaz):
    if 5 < fineanimaz <= 10:
        if npers == 1:
            schermo.blit(scudo, (vx + (gpx // 3), y))
            schermo.blit(persdm, (vx + (gpx // 3), y))
            if avvele:
                schermo.blit(persAvvele, (vx + (gpx // 3), y))
            schermo.blit(armatura, (vx + (gpx // 3), y))
            schermo.blit(persdmb1, (vx + (gpx // 3), y))
            schermo.blit(arma, (vx + (gpx // 3), y))
        if npers == 2:
            schermo.blit(arma, (vx - (gpx // 3), y))
            schermo.blit(persam, (vx - (gpx // 3), y))
            if avvele:
                schermo.blit(persAvvele, (vx - (gpx // 3), y))
            schermo.blit(armatura, (vx - (gpx // 3), y))
            schermo.blit(persamb1, (vx - (gpx // 3), y))
            schermo.blit(scudo, (vx - (gpx // 3), y))
        if npers == 3:
            schermo.blit(arma, (x, vy - (gpy // 3)))
            schermo.blit(scudo, (x, vy - (gpy // 3)))
            schermo.blit(perswm, (x, vy - (gpy // 3)))
            if avvele:
                schermo.blit(persAvvele, (x, vy - (gpy // 3)))
            schermo.blit(armatura, (x, vy - (gpy // 3)))
            schermo.blit(perswmb1, (x, vy - (gpy // 3)))
        if npers == 4:
            schermo.blit(perssm, (x, vy + (gpy // 3)))
            if avvele:
                schermo.blit(persAvvele, (x, vy + (gpy // 3)))
            schermo.blit(armatura, (x, vy + (gpy // 3)))
            schermo.blit(perssmb1, (x, vy + (gpy // 3)))
            schermo.blit(arma, (x, vy + (gpy // 3)))
            schermo.blit(scudo, (x, vy + (gpy // 3)))


def animaPersSpostato(npers, x, y, scudo, armatura, arma, avvele, fineanimaz):
    if npers == 1:
        if 5 < fineanimaz <= 10:
            schermo.blit(scudo, (x - (gpx * fineanimaz // 10), y))
            schermo.blit(persdm, (x - (gpx * fineanimaz // 10), y))
            if avvele:
                schermo.blit(persAvvele, (x - (gpx * fineanimaz // 10), y))
            schermo.blit(armatura, (x - (gpx * fineanimaz // 10), y))
            schermo.blit(persdmb1, (x - (gpx * fineanimaz // 10), y))
            schermo.blit(arma, (x - (gpx * fineanimaz // 10), y))
        if 0 < fineanimaz <= 5:
            schermo.blit(scudo, (x - (gpx * fineanimaz // 10), y))
            schermo.blit(persdm, (x - (gpx * fineanimaz // 10), y))
            if avvele:
                schermo.blit(persAvvele, (x - (gpx * fineanimaz // 10), y))
            schermo.blit(armatura, (x - (gpx * fineanimaz // 10), y))
            schermo.blit(persdmb2, (x - (gpx * fineanimaz // 10), y))
            schermo.blit(arma, (x - (gpx * fineanimaz // 10), y))
    if npers == 2:
        if 5 < fineanimaz <= 10:
            schermo.blit(arma, (x + (gpx * fineanimaz // 10), y))
            schermo.blit(persam, (x + (gpx * fineanimaz // 10), y))
            if avvele:
                schermo.blit(persAvvele, (x + (gpx * fineanimaz // 10), y))
            schermo.blit(armatura, (x + (gpx * fineanimaz // 10), y))
            schermo.blit(persamb1, (x + (gpx * fineanimaz // 10), y))
            schermo.blit(scudo, (x + (gpx * fineanimaz // 10), y))
        if 0 < fineanimaz <= 5:
            schermo.blit(arma, (x + (gpx * fineanimaz // 10), y))
            schermo.blit(persam, (x + (gpx * fineanimaz // 10), y))
            if avvele:
                schermo.blit(persAvvele, (x + (gpx * fineanimaz // 10), y))
            schermo.blit(armatura, (x + (gpx * fineanimaz // 10), y))
            schermo.blit(persamb2, (x + (gpx * fineanimaz // 10), y))
            schermo.blit(scudo, (x + (gpx * fineanimaz // 10), y))
    if npers == 3:
        if 5 < fineanimaz <= 10:
            schermo.blit(arma, (x, y + (gpy * fineanimaz // 10)))
            schermo.blit(scudo, (x, y + (gpy * fineanimaz // 10)))
            schermo.blit(perswm, (x, y + (gpy * fineanimaz // 10)))
            if avvele:
                schermo.blit(persAvvele, (x, y + (gpy * fineanimaz // 10)))
            schermo.blit(armatura, (x, y + (gpy * fineanimaz // 10)))
            schermo.blit(perswmb1, (x, y + (gpy * fineanimaz // 10)))
        if 0 < fineanimaz <= 5:
            schermo.blit(arma, (x, y + (gpy * fineanimaz // 10)))
            schermo.blit(scudo, (x, y + (gpy * fineanimaz // 10)))
            schermo.blit(perswm, (x, y + (gpy * fineanimaz // 10)))
            if avvele:
                schermo.blit(persAvvele, (x, y + (gpy * fineanimaz // 10)))
            schermo.blit(armatura, (x, y + (gpy * fineanimaz // 10)))
            schermo.blit(perswmb2, (x, y + (gpy * fineanimaz // 10)))
    if npers == 4:
        if 5 < fineanimaz <= 10:
            schermo.blit(perssm, (x, y - (gpy * fineanimaz // 10)))
            if avvele:
                schermo.blit(persAvvele, (x, y - (gpy * fineanimaz // 10)))
            schermo.blit(armatura, (x, y - (gpy * fineanimaz // 10)))
            schermo.blit(perssmb1, (x, y - (gpy * fineanimaz // 10)))
            schermo.blit(arma, (x, y - (gpy * fineanimaz // 10)))
            schermo.blit(scudo, (x, y - (gpy * fineanimaz // 10)))
        if 0 < fineanimaz <= 5:
            schermo.blit(perssm, (x, y - (gpy * fineanimaz // 10)))
            if avvele:
                schermo.blit(persAvvele, (x, y - (gpy * fineanimaz // 10)))
            schermo.blit(armatura, (x, y - (gpy * fineanimaz // 10)))
            schermo.blit(perssmb2, (x, y - (gpy * fineanimaz // 10)))
            schermo.blit(arma, (x, y - (gpy * fineanimaz // 10)))
            schermo.blit(scudo, (x, y - (gpy * fineanimaz // 10)))


def animaPersFermo(npers, x, y, vx, vy, scudo, armatura, arma, avvele, fineanimaz):
    if npers == 1:
        if 5 < fineanimaz <= 10:
            schermo.blit(scudo, (vx, y))
            schermo.blit(persdm, (vx, y))
            if avvele:
                schermo.blit(persAvvele, (vx, y))
            schermo.blit(armatura, (vx, y))
            schermo.blit(persdmb1, (vx, y))
            schermo.blit(arma, (vx, y))
        if 0 < fineanimaz <= 5:
            schermo.blit(scudo, (vx, y))
            schermo.blit(persdm, (vx, y))
            if avvele:
                schermo.blit(persAvvele, (vx, y))
            schermo.blit(armatura, (vx, y))
            schermo.blit(persdmb2, (vx, y))
            schermo.blit(arma, (vx, y))
    if npers == 2:
        if 5 < fineanimaz <= 10:
            schermo.blit(arma, (vx, y))
            schermo.blit(persam, (vx, y))
            if avvele:
                schermo.blit(persAvvele, (vx, y))
            schermo.blit(armatura, (vx, y))
            schermo.blit(persamb1, (vx, y))
            schermo.blit(scudo, (vx, y))
        if 0 < fineanimaz <= 5:
            schermo.blit(arma, (vx, y))
            schermo.blit(persam, (vx, y))
            if avvele:
                schermo.blit(persAvvele, (vx, y))
            schermo.blit(armatura, (vx, y))
            schermo.blit(persamb2, (vx, y))
            schermo.blit(scudo, (vx, y))
    if npers == 3:
        if 5 < fineanimaz <= 10:
            schermo.blit(arma, (x, vy))
            schermo.blit(scudo, (x, vy))
            schermo.blit(perswm, (x, vy))
            if avvele:
                schermo.blit(persAvvele, (x, vy))
            schermo.blit(armatura, (x, vy))
            schermo.blit(perswmb1, (x, vy))
        if 0 < fineanimaz <= 5:
            schermo.blit(arma, (x, vy))
            schermo.blit(scudo, (x, vy))
            schermo.blit(perswm, (x, vy))
            if avvele:
                schermo.blit(persAvvele, (x, vy))
            schermo.blit(armatura, (x, vy))
            schermo.blit(perswmb2, (x, vy))
    if npers == 4:
        if 5 < fineanimaz <= 10:
            schermo.blit(perssm, (x, vy))
            if avvele:
                schermo.blit(persAvvele, (x, vy))
            schermo.blit(armatura, (x, vy))
            schermo.blit(perssmb1, (x, vy))
            schermo.blit(arma, (x, vy))
            schermo.blit(scudo, (x, vy))
        if 0 < fineanimaz <= 5:
            schermo.blit(perssm, (x, vy))
            if avvele:
                schermo.blit(persAvvele, (x, vy))
            schermo.blit(armatura, (x, vy))
            schermo.blit(perssmb2, (x, vy))
            schermo.blit(arma, (x, vy))
            schermo.blit(scudo, (x, vy))


def animaCamminataRallo(sposta, x, y, vx, vy, primopasso, cambiosta, npers, scudo, armatura, arma, dati, attacco, difesa, tastop, animazione, pers, fineanimaz):
    animazioneFatta = False
    if sposta:
        # mentre ci si sposta
        if x != vx or y != vy:
            animazione = True
            animazioneFatta = True
            if not passiRallo.get_busy():
                passiRallo.play(rumorecamminata)
            if primopasso and not cambiosta:
                primopasso = False
            # camminata quando si entra in una stanza
            if cambiosta:
                animaPersCambiosta(npers, x, y, vx, vy, scudo, armatura, arma, dati[121], fineanimaz)
            # camminata quando non si entra in una stanza
            else:
                animaPersSpostato(npers, x, y, scudo, armatura, arma, dati[121], fineanimaz)
        # mentre non ci si sposta
        elif attacco == 0 and not difesa and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
            animazione = True
            animazioneFatta = True
            if not passiRallo.get_busy():
                passiRallo.play(rumorecamminata)
            if primopasso:
                primopasso = False
            animaPersFermo(npers, x, y, vx, vy, scudo, armatura, arma, dati[121], fineanimaz)
    if not animazioneFatta:
        if npers == 1:
            schermo.blit(scudo, (x, y))
            schermo.blit(pers, (x, y))
            if dati[121]:
                schermo.blit(persAvvele, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(persdb, (x, y))
            schermo.blit(arma, (x, y))
        if npers == 2:
            schermo.blit(arma, (x, y))
            schermo.blit(pers, (x, y))
            if dati[121]:
                schermo.blit(persAvvele, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(persab, (x, y))
            schermo.blit(scudo, (x, y))
        if npers == 3:
            schermo.blit(arma, (x, y))
            schermo.blit(scudo, (x, y))
            schermo.blit(pers, (x, y))
            if dati[121]:
                schermo.blit(persAvvele, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(perswb, (x, y))
        if npers == 4:
            schermo.blit(pers, (x, y))
            if dati[121]:
                schermo.blit(persAvvele, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(perssb, (x, y))
            schermo.blit(arma, (x, y))
            schermo.blit(scudo, (x, y))
    return animazione, primopasso


def animaCofanetto(tesoro, x, y, npers, sfondinoc, caricaTutto):
    if tesoro != -1:
        schermo.blit(sfocontcof, (gsx // 32 * 0, gsy // 18 * 0))
        # 31-40 -> oggetti(10) / 41-70 -> armi(30) / 71-80 -> batterie(10) / 81-100 -> condizioni(20) / 101-120 -> gambit (=celle di memoria)(20)
        if tesoro >= 11 and tesoro <= 30:
            messaggio("Hai trovato: Una nuova tecnica", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 31:
            messaggio("Hai trovato: Pozione", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 32:
            messaggio("Hai trovato: Caricabatterie", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 33:
            messaggio("Hai trovato: Bomba", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 34:
            messaggio("Hai trovato: Medicina", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 35:
            messaggio("Hai trovato: Bomba velenosa", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 36:
            messaggio("Hai trovato: Esca", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 37:
            messaggio("Hai trovato: Superpozione", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 38:
            messaggio("Hai trovato: Caricabatterie migliorato", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 39:
            messaggio("Hai trovato: Bomba appiccicosa", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 40:
            messaggio("Hai trovato: Bomba potenziata", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 41:
            messaggio("Hai trovato: Niente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 42:
            messaggio("Hai trovato: Spada di legno", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 43:
            messaggio("Hai trovato: Spada di ferro", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 44:
            messaggio("Hai trovato: Spadone d'acciaio", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 45:
            messaggio("Hai trovato: Spada del toro", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 46:
            messaggio("Hai trovato: Spada di diamante", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 47:
            messaggio("Hai trovato: Excalibur", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 48:
            messaggio("Hai trovato: Lykother", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 49:
            messaggio("Hai trovato: Sinego", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 50:
            messaggio("Hai trovato: Mendaxritas", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 51:
            messaggio("Hai trovato: Niente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 52:
            messaggio("Hai trovato: Armatura di pelle", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 53:
            messaggio("Hai trovato: Armatura di ferro", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 54:
            messaggio("Hai trovato: Armatura d'acciaio", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 55:
            messaggio("Hai trovato: Armatura del toro", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 56:
            messaggio("Hai trovato: Armatura di diamante", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 57:
            messaggio("Hai trovato: Armatura leggendaria", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 58:
            messaggio("Hai trovato: Lykodes", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 59:
            messaggio("Hai trovato: Armatura antica", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 60:
            messaggio("Hai trovato: Loriquam", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 61:
            messaggio("Hai trovato: Niente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 62:
            messaggio("Hai trovato: Scudo di pelle", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 63:
            messaggio("Hai trovato: Scudo di ferro", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 64:
            messaggio("Hai trovato: Scudo d'acciaio", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 65:
            messaggio("Hai trovato: Scudo del toro", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 66:
            messaggio("Hai trovato: Scudo di diamante", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 67:
            messaggio("Hai trovato: Scudo leggentario", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 68:
            messaggio("Hai trovato: Lykethmos", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 69:
            messaggio("Hai trovato: Scudo antico", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 70:
            messaggio("Hai trovato: Clipequam", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 71:
            messaggio("Hai trovato: Niente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 72:
            messaggio("Hai trovato: Batteria scarica", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 73:
            messaggio("Hai trovato: Batteria piccola", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 74:
            messaggio("Hai trovato: Batteria media", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 75:
            messaggio("Hai trovato: Batteria grande", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 76:
            messaggio("Hai trovato: Batteria discreta", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 77:
            messaggio("Hai trovato: Batteria affidabile", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 78:
            messaggio("Hai trovato: Batteria extra", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 79:
            messaggio("Hai trovato: Batteria efficiente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro == 80:
            messaggio("Hai trovato: Batteria illimitata", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro >= 81 and tesoro <= 100:
            messaggio("Hai trovato: Una nuova condizione", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if tesoro >= 101 and tesoro <= 120:
            messaggio("Hai trovato: Cella di memoria", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
        if npers == 1:
            schermo.blit(sfondinoc, (x + gpx, y))
            schermo.blit(cofaniaper, (x + gpx, y))
        if npers == 2:
            schermo.blit(sfondinoc, (x - gpx, y))
            schermo.blit(cofaniaper, (x - gpx, y))
        if npers == 4:
            schermo.blit(sfondinoc, (x, y + gpy))
            schermo.blit(cofaniaper, (x, y + gpy))
        if npers == 3:
            schermo.blit(sfondinoc, (x, y - gpy))
            schermo.blit(cofaniaper, (x, y - gpy))
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
                        selezione.play()
                        risposta = True
        caricaTutto = True
        tesoro = -1

    return caricaTutto, tesoro


def animaLvUp(npers, x, y, pers, scudo, armatura, arma, liv, aumentoliv, carim, animazione, caricaTutto, fineanimaz):
    if aumentoliv and not carim:
        animazione = True
        caricaTutto = True
        if not effetti.get_busy():
            effetti.play(rumorelevelup)
        if npers == 1:
            schermo.blit(scudo, (x, y))
            schermo.blit(pers, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(persdb, (x, y))
            schermo.blit(arma, (x, y))
        if npers == 2:
            schermo.blit(arma, (x, y))
            schermo.blit(pers, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(persab, (x, y))
            schermo.blit(scudo, (x, y))
        if npers == 3:
            schermo.blit(arma, (x, y))
            schermo.blit(scudo, (x, y))
            schermo.blit(pers, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(perswb, (x, y))
        if npers == 4:
            schermo.blit(pers, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(perssb, (x, y))
            schermo.blit(arma, (x, y))
            schermo.blit(scudo, (x, y))
        if 5 < fineanimaz <= 10:
            schermo.blit(saliliv2, (x, y))
        if 0 < fineanimaz <= 5:
            schermo.blit(saliliv1, (x, y))
        if fineanimaz == 0:
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
    return animazione, caricaTutto


def animaRoboSpostato(nrob, rx, ry, vrx, vry, armrob, surriscalda, cambiosta, animazione, robot, fineanimaz):
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


def animaMorteNemici(listaNemici, sfondinoa, sfondinob, fineanimaz):
    for nemico in listaNemici:
        if nemico.morto:
            n = 0
            while n < 32:
                if nemico.x == gpx * n:
                    m = 0
                    while m < 18:
                        if nemico.y == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (nemico.x, nemico.y))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (nemico.x, nemico.y))
                        m = m + 1
                n = n + 1


def animaSpostamentoNemici(listaNemici, animazione, cambiosta, fineanimaz):
    if not cambiosta:
        for nemico in listaNemici:
            if nemico.anima and not nemico.morto and (nemico.x != nemico.vx or nemico.y != nemico.vy):
                animazione = True
                # rumorecamminataNemico.play()
                if nemico.direzione == "d":
                    if 5 < fineanimaz <= 10:
                        schermo.blit(nemico.imgDMov1, (nemico.x - (gpx * fineanimaz // 10), nemico.y))
                        if nemico.avvelenato:
                            schermo.blit(roboSurrisc, (nemico.x - (gpx * fineanimaz // 10), nemico.y))
                        if nemico.appiccicato:
                            schermo.blit(roboSurrisc, (nemico.x - (gpx * fineanimaz // 10), nemico.y))
                    if 0 < fineanimaz <= 5:
                        schermo.blit(nemico.imgDMov2, (nemico.x - (gpx * fineanimaz // 10), nemico.y))
                        if nemico.avvelenato:
                            schermo.blit(roboSurrisc, (nemico.x - (gpx * fineanimaz // 10), nemico.y))
                        if nemico.appiccicato:
                            schermo.blit(roboSurrisc, (nemico.x - (gpx * fineanimaz // 10), nemico.y))
                if nemico.direzione == "a":
                    if 5 < fineanimaz <= 10:
                        schermo.blit(nemico.imgAMov1, (nemico.x + (gpx * fineanimaz // 10), nemico.y))
                        if nemico.avvelenato:
                            schermo.blit(roboSurrisc, (nemico.x + (gpx * fineanimaz // 10), nemico.y))
                        if nemico.appiccicato:
                            schermo.blit(roboSurrisc, (nemico.x + (gpx * fineanimaz // 10), nemico.y))
                    if 0 < fineanimaz <= 5:
                        schermo.blit(nemico.imgAMov2, (nemico.x + (gpx * fineanimaz // 10), nemico.y))
                        if nemico.avvelenato:
                            schermo.blit(roboSurrisc, (nemico.x + (gpx * fineanimaz // 10), nemico.y))
                        if nemico.appiccicato:
                            schermo.blit(roboSurrisc, (nemico.x + (gpx * fineanimaz // 10), nemico.y))
                if nemico.direzione == "w":
                    if 5 < fineanimaz <= 10:
                        schermo.blit(nemico.imgWMov1, (nemico.x, nemico.y + (gpy * fineanimaz // 10)))
                        if nemico.avvelenato:
                            schermo.blit(roboSurrisc, (nemico.x, nemico.y + (gpy * fineanimaz // 10)))
                        if nemico.appiccicato:
                            schermo.blit(roboSurrisc, (nemico.x, nemico.y + (gpy * fineanimaz // 10)))
                    if 0 < fineanimaz <= 5:
                        schermo.blit(nemico.imgWMov2, (nemico.x, nemico.y + (gpy * fineanimaz // 10)))
                        if nemico.avvelenato:
                            schermo.blit(roboSurrisc, (nemico.x, nemico.y + (gpy * fineanimaz // 10)))
                        if nemico.appiccicato:
                            schermo.blit(roboSurrisc, (nemico.x, nemico.y + (gpy * fineanimaz // 10)))
                if nemico.direzione == "s":
                    if 5 < fineanimaz <= 10:
                        schermo.blit(nemico.imgSMov1, (nemico.x, nemico.y - (gpy * fineanimaz // 10)))
                        if nemico.avvelenato:
                            schermo.blit(roboSurrisc, (nemico.x, nemico.y - (gpy * fineanimaz // 10)))
                        if nemico.appiccicato:
                            schermo.blit(roboSurrisc, (nemico.x, nemico.y - (gpy * fineanimaz // 10)))
                    if 0 < fineanimaz <= 5:
                        schermo.blit(nemico.imgSMov2, (nemico.x, nemico.y - (gpy * fineanimaz // 10)))
                        if nemico.avvelenato:
                            schermo.blit(roboSurrisc, (nemico.x, nemico.y - (gpy * fineanimaz // 10)))
                        if nemico.appiccicato:
                            schermo.blit(roboSurrisc, (nemico.x, nemico.y - (gpy * fineanimaz // 10)))
    return animazione


def anima(sposta, x, y, vx, vy, rx, ry, vrx, vry, pers, robot, npers, nrob, primopasso, cambiosta, sfondinoa, sfondinob, scudo, armatura, arma, armrob, dati, attacco, difesa, tastop, tesoro, sfondinoc, aumentoliv, carim, caricaTutto, listaNemici):
    animazione = False
    # viene fatto un ciclo in più alla fine (senza clock) per ripulire le immagini delle animazioni rimaste (altrimenti le ultime non verrebbero cancellate)
    fineanimaz = 10
    while fineanimaz >= 0:
        # ridisegnare il quadratino dove sono i personaggi
        if cambiosta:
            n = 0
            while fineanimaz == 10 and n < 32:
                if x == gpx * n:
                    m = 0
                    while m < 18:
                        if y == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinob, (vx, vy))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinoa, (vx, vy))
                        m = m + 1
                n = n + 1
        else:
            n = 0
            while n < 32:
                if x == gpx * n:
                    m = 0
                    while m < 18:
                        if y == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinob, (vx, vy))
                                schermo.blit(sfondinoa, (x, y))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinoa, (vx, vy))
                                schermo.blit(sfondinob, (x, y))
                        m = m + 1
                if rx == gpx * n:
                    m = 0
                    while m < 18:
                        if ry == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinob, (vrx, vry))
                                schermo.blit(sfondinoa, (rx, ry))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinoa, (vrx, vry))
                                schermo.blit(sfondinob, (rx, ry))
                        m = m + 1
                for nemico in listaNemici:
                    if nemico.anima:
                        if nemico.x == gpx * n:
                            m = 0
                            while m < 18:
                                if nemico.y == gpy * m:
                                    if (n + m) % 2 == 0:
                                        schermo.blit(sfondinob, (nemico.vx, nemico.vy))
                                        schermo.blit(sfondinoa, (nemico.x, nemico.y))
                                    if (n + m) % 2 != 0:
                                        schermo.blit(sfondinoa, (nemico.vx, nemico.vy))
                                        schermo.blit(sfondinob, (nemico.x, nemico.y))
                                m = m + 1
                n = n + 1

        if y < ry:
            # animazione camminata personaggio
            animazione, primopasso = animaCamminataRallo(sposta, x, y, vx, vy, primopasso, cambiosta, npers, scudo, armatura, arma, dati, attacco, difesa, tastop, animazione, pers, fineanimaz)
            # animazione camminata robo
            animazione = animaRoboSpostato(nrob, rx, ry, vrx, vry, armrob, dati[122], cambiosta, animazione, robot, fineanimaz)
        else:
            # animazione camminata robo
            animazione = animaRoboSpostato(nrob, rx, ry, vrx, vry, armrob, dati[122], cambiosta, animazione, robot, fineanimaz)
            # animazione camminata personaggio
            animazione, primopasso = animaCamminataRallo(sposta, x, y, vx, vy, primopasso, cambiosta, npers, scudo, armatura, arma, dati, attacco, difesa, tastop, animazione, pers, fineanimaz)

        animazione = animaSpostamentoNemici(listaNemici, animazione, cambiosta, fineanimaz)

        # animazione apertura cofanetto
        caricaTutto, tesoro = animaCofanetto(tesoro, x, y, npers, sfondinoc, caricaTutto)

        # animazione aumento di livello
        animazione, caricaTutto = animaLvUp(npers, x, y, pers, scudo, armatura, arma, dati[4], aumentoliv, carim, animazione, caricaTutto, fineanimaz)

        # animazione morte nemici
        animaMorteNemici(listaNemici, sfondinoa, sfondinob, fineanimaz)

        fineanimaz -= 1
        if animazione and fineanimaz != -1:
            pygame.display.update()
            clockAnimazioni.tick(fpsAnimazioni)
            #print (clockAnimazioni.get_fps())
        if fineanimaz == -1 and aumentoliv:
            pygame.display.update()
            pygame.time.wait(1000)

    return primopasso, caricaTutto, tesoro
