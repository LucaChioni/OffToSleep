# -*- coding: utf-8 -*-

from GenericFuncG2 import *


def animaCofanetto(tesoro, x, y, npers, sfondinoc):
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
    caricaini = True
    tesoro = -1

    return caricaini, tesoro


def animaPersCambiosta(npers, x, y, vx, vy, sfondinoa, sfondinob, scudo, armatura, arma, avvele):
    fineanimaz = 1
    while fineanimaz > 0:
        n = 0
        while fineanimaz == 1 and n < 32:
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
        if fineanimaz == 1:
            rumorecamminata.stop()
            rumorecamminata.play()
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
        fineanimaz = fineanimaz - 1
        pygame.display.update()
        clock.tick(fpsanimazioni)
        pygame.display.update()


def animaPersSpostato(npers, x, y, vx, vy, sfondinoa, sfondinob, scudo, armatura, arma, avvele):
    fineanimaz = 2
    while fineanimaz != 0:
        n = 0
        while fineanimaz <= 2 and n < 32:
            if x == gpx * n:
                m = 0
                while m < 18:
                    if y == gpy * m:
                        if (n + m) % 2 == 0:
                            schermo.blit(sfondinoa, (x, y))
                            schermo.blit(sfondinob, (vx, vy))
                        if (n + m) % 2 != 0:
                            schermo.blit(sfondinob, (x, y))
                            schermo.blit(sfondinoa, (vx, vy))
                    m = m + 1
            n = n + 1
        if npers == 1:
            if fineanimaz == 2:
                schermo.blit(scudo, (vx + (gpx // 3), y))
                schermo.blit(persdm, (vx + (gpx // 3), y))
                if avvele:
                    schermo.blit(persAvvele, (vx + (gpx // 3), y))
                schermo.blit(armatura, (vx + (gpx // 3), y))
                schermo.blit(persdmb1, (vx + (gpx // 3), y))
                schermo.blit(arma, (vx + (gpx // 3), y))
            if fineanimaz == 1:
                schermo.blit(scudo, (vx + (gpx * 2 // 3), y))
                schermo.blit(persdm, (vx + (gpx * 2 // 3), y))
                if avvele:
                    schermo.blit(persAvvele, (vx + (gpx * 2 // 3), y))
                schermo.blit(armatura, (vx + (gpx * 2 // 3), y))
                schermo.blit(persdmb2, (vx + (gpx * 2 // 3), y))
                schermo.blit(arma, (vx + (gpx * 2 // 3), y))
        if npers == 2:
            if fineanimaz == 2:
                schermo.blit(arma, (vx - (gpx // 3), y))
                schermo.blit(persam, (vx - (gpx // 3), y))
                if avvele:
                    schermo.blit(persAvvele, (vx - (gpx // 3), y))
                schermo.blit(armatura, (vx - (gpx // 3), y))
                schermo.blit(persamb1, (vx - (gpx // 3), y))
                schermo.blit(scudo, (vx - (gpx // 3), y))
            if fineanimaz == 1:
                schermo.blit(arma, (vx - (gpx * 2 // 3), y))
                schermo.blit(persam, (vx - (gpx * 2 // 3), y))
                if avvele:
                    schermo.blit(persAvvele, (vx - (gpx * 2 // 3), y))
                schermo.blit(armatura, (vx - (gpx * 2 // 3), y))
                schermo.blit(persamb2, (vx - (gpx * 2 // 3), y))
                schermo.blit(scudo, (vx - (gpx * 2 // 3), y))
        if npers == 3:
            if fineanimaz == 2:
                schermo.blit(arma, (x, vy - (gpy // 3)))
                schermo.blit(scudo, (x, vy - (gpy // 3)))
                schermo.blit(perswm, (x, vy - (gpy // 3)))
                if avvele:
                    schermo.blit(persAvvele, (x, vy - (gpy // 3)))
                schermo.blit(armatura, (x, vy - (gpy // 3)))
                schermo.blit(perswmb1, (x, vy - (gpy // 3)))
            if fineanimaz == 1:
                schermo.blit(arma, (x, vy - (gpy * 2 // 3)))
                schermo.blit(scudo, (x, vy - (gpy * 2 // 3)))
                schermo.blit(perswm, (x, vy - (gpy * 2 // 3)))
                if avvele:
                    schermo.blit(persAvvele, (x, vy - (gpy * 2 // 3)))
                schermo.blit(armatura, (x, vy - (gpy * 2 // 3)))
                schermo.blit(perswmb2, (x, vy - (gpy * 2 // 3)))
        if npers == 4:
            if fineanimaz == 2:
                schermo.blit(perssm, (x, vy + (gpy // 3)))
                if avvele:
                    schermo.blit(persAvvele, (x, vy + (gpy // 3)))
                schermo.blit(armatura, (x, vy + (gpy // 3)))
                schermo.blit(perssmb1, (x, vy + (gpy // 3)))
                schermo.blit(arma, (x, vy + (gpy // 3)))
                schermo.blit(scudo, (x, vy + (gpy // 3)))
            if fineanimaz == 1:
                schermo.blit(perssm, (x, vy + (gpy * 2 // 3)))
                if avvele:
                    schermo.blit(persAvvele, (x, vy + (gpy * 2 // 3)))
                schermo.blit(armatura, (x, vy + (gpy * 2 // 3)))
                schermo.blit(perssmb2, (x, vy + (gpy * 2 // 3)))
                schermo.blit(arma, (x, vy + (gpy * 2 // 3)))
                schermo.blit(scudo, (x, vy + (gpy * 2 // 3)))
        pygame.display.update()
        clock.tick(fpsanimazioni)
        fineanimaz = fineanimaz - 1
    n = 0
    while n < 32:
        if x == gpx * n:
            m = 0
            while m < 18:
                if y == gpy * m:
                    if (n + m) % 2 == 0:
                        schermo.blit(sfondinoa, (x, y))
                        schermo.blit(sfondinob, (vx, vy))
                    if (n + m) % 2 != 0:
                        schermo.blit(sfondinob, (x, y))
                        schermo.blit(sfondinoa, (vx, vy))
                m = m + 1
        n = n + 1
    if npers == 1:
        schermo.blit(scudo, (x, y))
        schermo.blit(persd, (x, y))
        if avvele:
            schermo.blit(persAvvele, (x, y))
        schermo.blit(armatura, (x, y))
        schermo.blit(persdb, (x, y))
        schermo.blit(arma, (x, y))
    if npers == 2:
        schermo.blit(arma, (x, y))
        schermo.blit(persa, (x, y))
        if avvele:
            schermo.blit(persAvvele, (x, y))
        schermo.blit(armatura, (x, y))
        schermo.blit(persab, (x, y))
        schermo.blit(scudo, (x, y))
    if npers == 3:
        schermo.blit(arma, (x, y))
        schermo.blit(scudo, (x, y))
        schermo.blit(persw, (x, y))
        if avvele:
            schermo.blit(persAvvele, (x, y))
        schermo.blit(armatura, (x, y))
        schermo.blit(perswb, (x, y))
    if npers == 4:
        schermo.blit(perss, (x, y))
        if avvele:
            schermo.blit(persAvvele, (x, y))
        schermo.blit(armatura, (x, y))
        schermo.blit(perssb, (x, y))
        schermo.blit(arma, (x, y))
        schermo.blit(scudo, (x, y))


def animaPersFermo(npers, x, y, vx, vy, sfondinoa, sfondinob, scudo, armatura, arma, avvele):
    fineanimaz = 2
    while fineanimaz != 0:
        n = 0
        while fineanimaz <= 2 and n < 32:
            if x == gpx * n:
                m = 0
                while m < 18:
                    if y == gpy * m:
                        if (n + m) % 2 == 0:
                            schermo.blit(sfondinoa, (x, y))
                        if (n + m) % 2 != 0:
                            schermo.blit(sfondinob, (x, y))
                    m = m + 1
            n = n + 1
        if npers == 1:
            if fineanimaz == 2:
                schermo.blit(scudo, (vx, y))
                schermo.blit(persdm, (vx, y))
                if avvele:
                    schermo.blit(persAvvele, (vx, y))
                schermo.blit(armatura, (vx, y))
                schermo.blit(persdmb1, (vx, y))
                schermo.blit(arma, (vx, y))
            if fineanimaz == 1:
                schermo.blit(scudo, (vx, y))
                schermo.blit(persdm, (vx, y))
                if avvele:
                    schermo.blit(persAvvele, (vx, y))
                schermo.blit(armatura, (vx, y))
                schermo.blit(persdmb2, (vx, y))
                schermo.blit(arma, (vx, y))
        if npers == 2:
            if fineanimaz == 2:
                schermo.blit(arma, (vx, y))
                schermo.blit(persam, (vx, y))
                if avvele:
                    schermo.blit(persAvvele, (vx, y))
                schermo.blit(armatura, (vx, y))
                schermo.blit(persamb1, (vx, y))
                schermo.blit(scudo, (vx, y))
            if fineanimaz == 1:
                schermo.blit(arma, (vx, y))
                schermo.blit(persam, (vx, y))
                if avvele:
                    schermo.blit(persAvvele, (vx, y))
                schermo.blit(armatura, (vx, y))
                schermo.blit(persamb2, (vx, y))
                schermo.blit(scudo, (vx, y))
        if npers == 3:
            if fineanimaz == 2:
                schermo.blit(arma, (x, vy))
                schermo.blit(scudo, (x, vy))
                schermo.blit(perswm, (x, vy))
                if avvele:
                    schermo.blit(persAvvele, (x, vy))
                schermo.blit(armatura, (x, vy))
                schermo.blit(perswmb1, (x, vy))
            if fineanimaz == 1:
                schermo.blit(arma, (x, vy))
                schermo.blit(scudo, (x, vy))
                schermo.blit(perswm, (x, vy))
                if avvele:
                    schermo.blit(persAvvele, (x, vy))
                schermo.blit(armatura, (x, vy))
                schermo.blit(perswmb2, (x, vy))
        if npers == 4:
            if fineanimaz == 2:
                schermo.blit(perssm, (x, vy))
                if avvele:
                    schermo.blit(persAvvele, (x, vy))
                schermo.blit(armatura, (x, vy))
                schermo.blit(perssmb1, (x, vy))
                schermo.blit(arma, (x, vy))
                schermo.blit(scudo, (x, vy))
            if fineanimaz == 1:
                schermo.blit(perssm, (x, vy))
                if avvele:
                    schermo.blit(persAvvele, (x, vy))
                schermo.blit(armatura, (x, vy))
                schermo.blit(perssmb2, (x, vy))
                schermo.blit(arma, (x, vy))
                schermo.blit(scudo, (x, vy))
        pygame.display.update()
        clock.tick(fpsanimazioni)
        fineanimaz = fineanimaz - 1


def animaMorteNemici(mortoa, mxa, mya, mortob, mxb, myb, mortoc, mxc, myc, mortod, mxd, myd, mortoe, mxe, mye, mortof, mxf, myf, mortog, mxg, myg, mortoh, mxh, myh, mortoi, mxi, myi, mortol, mxl, myl, sfondinoa, sfondinob):
    vetNemiciMorti = [mortoa, mxa, mya, mortob, mxb, myb, mortoc, mxc, myc, mortod, mxd, myd, mortoe, mxe, mye, mortof, mxf, myf, mortog, mxg, myg, mortoh, mxh, myh, mortoi, mxi, myi, mortol, mxl, myl]
    i = 0
    while i < len(vetNemiciMorti):
        mortoMo = vetNemiciMorti[i]
        mx = vetNemiciMorti[i + 1]
        my = vetNemiciMorti[i + 2]
        if mortoMo == 1:
            n = 0
            while n < 32:
                if mx == gpx * n:
                    m = 0
                    while m < 18:
                        if my == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mx, my))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mx, my))
                        m = m + 1
                n = n + 1
        i += 3


def animaLvUp(npers, x, y, pers, sfondinoa, sfondinob, scudo, armatura, arma, liv):
    fineanimaz = 3
    while fineanimaz != -1:
        n = 0
        while fineanimaz <= 3 and n < 32:
            if x == gpx * n:
                m = 0
                while m < 18:
                    if y == gpy * m:
                        if (n + m) % 2 == 0:
                            schermo.blit(sfondinoa, (x, y))
                        if (n + m) % 2 != 0:
                            schermo.blit(sfondinob, (x, y))
                    m = m + 1
            n = n + 1
        if npers == 1:
            schermo.blit(scudo, (x, y))
            schermo.blit(pers, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(persdb, (x, y))
            schermo.blit(arma, (x, y))
            if fineanimaz == 0:
                schermo.blit(saliliv, (x, y))
            if fineanimaz == 1:
                schermo.blit(saliliv1, (x, y))
            if fineanimaz == 2:
                schermo.blit(saliliv2, (x, y))
            if fineanimaz == 3:
                schermo.blit(saliliv3, (x, y))
        if npers == 2:
            schermo.blit(arma, (x, y))
            schermo.blit(pers, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(persab, (x, y))
            schermo.blit(scudo, (x, y))
            if fineanimaz == 0:
                schermo.blit(saliliv, (x, y))
            if fineanimaz == 1:
                schermo.blit(saliliv1, (x, y))
            if fineanimaz == 2:
                schermo.blit(saliliv2, (x, y))
            if fineanimaz == 3:
                schermo.blit(saliliv3, (x, y))
        if npers == 3:
            schermo.blit(arma, (x, y))
            schermo.blit(scudo, (x, y))
            schermo.blit(pers, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(perswb, (x, y))
            if fineanimaz == 0:
                schermo.blit(saliliv, (x, y))
            if fineanimaz == 1:
                schermo.blit(saliliv1, (x, y))
            if fineanimaz == 2:
                schermo.blit(saliliv2, (x, y))
            if fineanimaz == 3:
                schermo.blit(saliliv3, (x, y))
        if npers == 4:
            schermo.blit(pers, (x, y))
            schermo.blit(armatura, (x, y))
            schermo.blit(perssb, (x, y))
            schermo.blit(arma, (x, y))
            schermo.blit(scudo, (x, y))
            if fineanimaz == 0:
                schermo.blit(saliliv, (x, y))
            if fineanimaz == 1:
                schermo.blit(saliliv1, (x, y))
            if fineanimaz == 2:
                schermo.blit(saliliv2, (x, y))
            if fineanimaz == 3:
                schermo.blit(saliliv3, (x, y))

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

        pygame.display.update()
        clock.tick(fpsanimazioni)
        if fineanimaz == 0:
            pygame.time.wait(1000)
        fineanimaz = fineanimaz - 1


def animaRoboSpostato(nrob, rx, ry, vrx, vry, sfondinoa, sfondinob, armrob, surriscalda):
    fineanimaz = 2
    while fineanimaz != 0:
        n = 0
        while fineanimaz <= 2 and n < 32:
            if rx == gpx * n:
                m = 0
                while m < 18:
                    if ry == gpy * m:
                        if (n + m) % 2 == 0:
                            schermo.blit(sfondinoa, (rx, ry))
                            schermo.blit(sfondinob, (vrx, vry))
                        if (n + m) % 2 != 0:
                            schermo.blit(sfondinob, (rx, ry))
                            schermo.blit(sfondinoa, (vrx, vry))
                    m = m + 1
            n = n + 1
        if nrob == 1:
            if fineanimaz == 2:
                schermo.blit(robodp, (vrx + (gpx // 3), ry))
                if surriscalda:
                    schermo.blit(roboSurrisc, (vrx + (gpx // 3), ry))
                schermo.blit(armrob, (vrx + (gpx // 3), ry))
            if fineanimaz == 1:
                schermo.blit(robodp, (vrx + (gpx * 2 // 3), ry))
                if surriscalda:
                    schermo.blit(roboSurrisc, (vrx + (gpx * 2 // 3), ry))
                schermo.blit(armrob, (vrx + (gpx * 2 // 3), ry))
        if nrob == 2:
            if fineanimaz == 2:
                schermo.blit(roboap, (vrx - (gpx // 3), ry))
                if surriscalda:
                    schermo.blit(roboSurrisc, (vrx - (gpx // 3), ry))
                schermo.blit(armrob, (vrx - (gpx // 3), ry))
            if fineanimaz == 1:
                schermo.blit(roboap, (vrx - (gpx * 2 // 3), ry))
                if surriscalda:
                    schermo.blit(roboSurrisc, (vrx - (gpx * 2 // 3), ry))
                schermo.blit(armrob, (vrx - (gpx * 2 // 3), ry))
        if nrob == 4:
            if fineanimaz == 2:
                schermo.blit(robow, (rx, vry - (gpy // 3)))
                if surriscalda:
                    schermo.blit(roboSurrisc, (rx, vry - (gpy // 3)))
                schermo.blit(armrob, (rx, vry - (gpy // 3)))
            if fineanimaz == 1:
                schermo.blit(robow, (rx, vry - (gpy * 2 // 3)))
                if surriscalda:
                    schermo.blit(roboSurrisc, (rx, vry - (gpy * 2 // 3)))
                schermo.blit(armrob, (rx, vry - (gpy * 2 // 3)))
        if nrob == 3:
            if fineanimaz == 2:
                schermo.blit(robos, (rx, vry + (gpy // 3)))
                if surriscalda:
                    schermo.blit(roboSurrisc, (rx, vry + (gpy // 3)))
                schermo.blit(armrob, (rx, vry + (gpy // 3)))
            if fineanimaz == 1:
                schermo.blit(robos, (rx, vry + (gpy * 2 // 3)))
                if surriscalda:
                    schermo.blit(roboSurrisc, (rx, vry + (gpy * 2 // 3)))
                schermo.blit(armrob, (rx, vry + (gpy * 2 // 3)))
        pygame.display.update()
        clock.tick(fpsanimazioni)
        fineanimaz = fineanimaz - 1
    n = 0
    while n < 32:
        if rx == gpx * n:
            m = 0
            while m < 18:
                if ry == gpy * m:
                    if (n + m) % 2 == 0:
                        schermo.blit(sfondinoa, (rx, ry))
                        schermo.blit(sfondinob, (vrx, vry))
                    if (n + m) % 2 != 0:
                        schermo.blit(sfondinob, (rx, ry))
                        schermo.blit(sfondinoa, (vrx, vry))
                m = m + 1
        n = n + 1
    if nrob == 1:
        schermo.blit(robod, (rx, ry))
        if surriscalda:
            schermo.blit(roboSurrisc, (rx, ry))
        schermo.blit(armrob, (rx, ry))
    if nrob == 2:
        schermo.blit(roboa, (rx, ry))
        if surriscalda:
            schermo.blit(roboSurrisc, (rx, ry))
        schermo.blit(armrob, (rx, ry))
    if nrob == 4:
        schermo.blit(robow, (rx, ry))
        if surriscalda:
            schermo.blit(roboSurrisc, (rx, ry))
        schermo.blit(armrob, (rx, ry))
    if nrob == 3:
        schermo.blit(robos, (rx, ry))
        if surriscalda:
            schermo.blit(roboSurrisc, (rx, ry))
        schermo.blit(armrob, (rx, ry))
